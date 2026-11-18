"""퇴근 후, 우리 — 배경음과 효과음을 직접 합성한다.

외부 음원·샘플을 쓰지 않고 numpy 계산만으로 소리를 만든다.
그래서 저작권·라이선스 걱정 없이 상업 배포에 넣을 수 있다.

사용법(저장소 루트에서):
    python3 -I Source/tools/make_audio.py

필요: numpy, ffmpeg(ogg 변환). 결과는 Source/game/audio/{bgm,sfx}/*.ogg.
같은 시드면 같은 소리가 나온다. 이 스크립트는 배포판에 넣지 않는다.
"""

import os
import subprocess
import sys
import tempfile
import wave

import numpy as np

SR = 44100
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "game", "audio")

NOTE = {"C": 0, "Db": 1, "D": 2, "Eb": 3, "E": 4, "F": 5, "Gb": 6, "G": 7, "Ab": 8, "A": 9, "Bb": 10, "B": 11}
QUAL = {
    "M": [0, 4, 7], "m": [0, 3, 7],
    "maj7": [0, 4, 7, 11], "m7": [0, 3, 7, 10], "7": [0, 4, 7, 10],
    "maj9": [0, 4, 7, 11, 14], "m9": [0, 3, 7, 10, 14], "13": [0, 4, 10, 14, 21],
    "sus": [0, 5, 7, 10, 14], "add9": [0, 4, 7, 14],
}


def hz(m):
    return 440.0 * 2 ** ((m - 69) / 12.0)


def chord(name):
    root, q = name.split(" ")
    r = NOTE[root]
    bass = 36 + r if r >= 4 else 48 + r
    tones = []
    for iv in QUAL[q]:
        n = 60 + r + iv
        while n > 74:
            n -= 12
        while n < 55:
            n += 12
        tones.append(n)
    return bass, sorted(set(tones)), [60 + r + iv for iv in QUAL[q]]


# ── 악기 ───────────────────────────────────────────────────────
def env(n, a, d, sustain=0.0, rel=0.08):
    t = np.arange(n) / SR
    e = np.minimum(1.0, t / max(a, 1e-4)) * (sustain + (1 - sustain) * np.exp(-t / d))
    r = int(rel * SR)
    if r and n > r:
        e[-r:] *= np.linspace(1, 0, r)
    return e


def epiano(f, dur, vel=1.0):
    n = int((dur + 1.2) * SR)
    t = np.arange(n) / SR
    idx = 1.4 * np.exp(-t / 0.35) + 0.15
    mod = np.sin(2 * np.pi * f * t) * idx
    body = np.sin(2 * np.pi * f * t + mod)
    tine = 0.18 * np.sin(2 * np.pi * f * 4.0 * t) * np.exp(-t / 0.08)
    e = env(n, 0.004, 1.4, 0.0, 0.0)
    off = int(dur * SR)
    if off < n:
        e[off:] *= np.exp(-np.arange(n - off) / (0.18 * SR))
    return (body + tine) * e * vel * 0.32


def pad(f, dur):
    n = int((dur + 1.5) * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for det in (-0.0018, 0.0, 0.0021):
        for h in range(1, 7):
            s += np.sin(2 * np.pi * f * (1 + det) * h * t + h * 1.7) / h ** 1.6
    e = np.minimum(1.0, t / 0.9)
    off = int(dur * SR)
    e[off:] *= np.exp(-np.arange(n - off) / (0.55 * SR))
    return s * e * 0.05


def bass(f, dur, vel=1.0):
    n = int((dur + 0.3) * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(4 * np.pi * f * t) * np.exp(-t / 0.2)
    e = env(n, 0.006, 0.9, 0.35, 0.0)
    off = int(dur * SR)
    e[off:] *= np.exp(-np.arange(n - off) / (0.05 * SR))
    return s * e * vel * 0.42


def bell(f, dur=2.5, vel=1.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for ratio, amp, dec in ((1, 1, 1.6), (2.0, 0.45, 0.9), (2.76, 0.3, 0.6), (5.4, 0.18, 0.25), (8.93, 0.08, 0.12)):
        s += amp * np.sin(2 * np.pi * f * ratio * t) * np.exp(-t / dec)
    return s * np.minimum(1.0, t / 0.002) * vel * 0.16


def kick(vel=1.0):
    n = int(0.35 * SR)
    t = np.arange(n) / SR
    fr = 45 + 80 * np.exp(-t / 0.03)
    ph = 2 * np.pi * np.cumsum(fr) / SR
    return np.sin(ph) * np.exp(-t / 0.13) * vel * 0.55


def lowpass(x, fc, order=2):
    X = np.fft.rfft(x, axis=0)
    f = np.fft.rfftfreq(x.shape[0], 1 / SR)
    g = 1 / np.sqrt(1 + (f / fc) ** (2 * order))
    if x.ndim == 2:
        g = g[:, None]
    return np.fft.irfft(X * g, n=x.shape[0], axis=0)


def highpass(x, fc, order=2):
    return x - lowpass(x, fc, order)


def noise_hit(dur, fc_lo, fc_hi, dec, vel, rng):
    n = int(dur * SR)
    s = rng.standard_normal(n)
    s = highpass(lowpass(s, fc_hi), fc_lo)
    t = np.arange(n) / SR
    return s * np.exp(-t / dec) * vel


# ── 믹스 도우미 ─────────────────────────────────────────────────
class Bus:
    def __init__(self, n):
        self.x = np.zeros((n, 2))

    def add(self, sig, at, pan=0.0, gain=1.0):
        i = int(at * SR)
        if i >= len(self.x):
            return
        j = min(len(self.x), i + len(sig))
        l = np.cos((pan + 1) * np.pi / 4) * gain
        r = np.sin((pan + 1) * np.pi / 4) * gain
        self.x[i:j, 0] += sig[: j - i] * l
        self.x[i:j, 1] += sig[: j - i] * r


def reverb(x, seconds, rng, tone=5000):
    n = int(seconds * SR)
    t = np.arange(n) / SR
    ir = rng.standard_normal((n, 2)) * np.exp(-t / (seconds / 5.5))[:, None]
    ir = lowpass(ir, tone)
    ir[: int(0.012 * SR)] = 0
    ir /= np.sqrt((ir ** 2).sum(axis=0))
    m = len(x) + n
    size = 1 << (m - 1).bit_length()
    out = np.fft.irfft(np.fft.rfft(x, size, axis=0) * np.fft.rfft(ir, size, axis=0), size, axis=0)
    return out[:m]


def master(x, target_rms=0.11):
    x = x - x.mean(axis=0)
    rms = np.sqrt((x ** 2).mean())
    x = x * (target_rms / max(rms, 1e-9))
    x = np.tanh(x * 1.1) / np.tanh(1.1)
    peak = np.abs(x).max()
    if peak > 0.89:
        x *= 0.89 / peak
    return x


def save_ogg(x, path, quality=5):
    pcm = (np.clip(x, -1, 1) * 32767).astype("<i2")
    with tempfile.TemporaryDirectory() as tmp:
        wav = os.path.join(tmp, "a.wav")
        with wave.open(wav, "wb") as w:
            w.setnchannels(2 if x.ndim == 2 else 1)
            w.setsampwidth(2)
            w.setframerate(SR)
            w.writeframes(pcm.tobytes())
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", wav, "-map_metadata", "-1",
                        "-c:a", "libvorbis", "-q:a", str(quality), path], check=True)


# ── 곡 ─────────────────────────────────────────────────────────
TRACKS = {
    # 이름: (bpm, 코드 진행, 코드당 마디, 반복, 스타일, 리버브 비율, 시드)
    "title": (72, ["F maj9", "E m7", "D m9", "C add9"], 2, 2, "ballad", 0.36, 11),
    "office": (92, ["C maj9", "A m9", "D m9", "G 13"], 1, 4, "lofi", 0.18, 21),
    "cafe": (84, ["Bb maj7", "G m7", "C m9", "F 13"], 1, 4, "jazz", 0.24, 31),
    "evening": (76, ["Db maj9", "C m7", "Bb m9", "Eb sus"], 2, 2, "walk", 0.30, 41),
    "night": (68, ["A m9", "F maj7", "D m9", "E sus"], 2, 2, "night", 0.32, 51),
    "home": (60, ["Eb maj9", "Ab maj7", "C m9", "Bb sus"], 2, 2, "quiet", 0.42, 61),
    "pitch": (112, ["D m", "Bb M", "F M", "C M"], 1, 4, "drive", 0.16, 71),
    "ending": (66, ["F maj9", "E m7", "D m9", "Bb maj7", "F maj9", "A m7", "D m9", "C add9"], 2, 1, "ending", 0.42, 81),
}


def melody(rng, chords_seq, bars_per, beat, bar, start_note=72, density=0.55, low=64, high=84):
    notes = []
    cur = start_note
    for ci, name in enumerate(chords_seq):
        _, _, full = chord(name)
        pool = sorted({n + o for n in full for o in (0, 12, 24) if low <= n + o <= high})
        for b in range(bars_per):
            t0 = (ci * bars_per + b) * bar
            pos = 0.0
            while pos < 4:
                step = rng.choice([0.5, 1.0, 1.0, 1.5, 2.0])
                if rng.random() < density:
                    near = sorted(pool, key=lambda n: abs(n - cur) + rng.random() * 3)
                    cur = near[0] if rng.random() < 0.6 else near[min(2, len(near) - 1)]
                    notes.append((t0 + pos * beat, cur, min(step, 4 - pos) * beat))
                pos += step
    return notes


def render_track(name):
    bpm, prog, bars_per, reps, style, wet, seed = TRACKS[name]
    rng = np.random.default_rng(seed)
    beat = 60.0 / bpm
    bar = beat * 4
    seq = prog * reps
    length = len(seq) * bars_per * bar
    tail = 4.0
    n = int((length + tail) * SR)
    dry = Bus(n)
    verb = Bus(n)

    for ci, cname in enumerate(seq):
        b, tones, _ = chord(cname)
        t0 = ci * bars_per * bar
        dur = bars_per * bar
        # 패드
        if style in ("ballad", "walk", "night", "quiet", "drive", "ending"):
            for k, m in enumerate(tones):
                s = pad(hz(m), dur)
                dry.add(s, t0, pan=-0.4 + 0.8 * k / max(1, len(tones) - 1), gain=0.8)
                verb.add(s, t0, gain=0.6)
        # 베이스
        if style in ("lofi", "walk", "night", "drive"):
            if style == "drive":
                for i in range(int(dur / (beat / 2))):
                    s = bass(hz(b), beat * 0.42, 0.7 + 0.3 * (i % 2 == 0))
                    dry.add(s, t0 + i * beat / 2, gain=0.9)
            else:
                for bb in range(bars_per):
                    dry.add(bass(hz(b), beat * 2.6), t0 + bb * bar)
                    dry.add(bass(hz(b + 7 if b + 7 < 52 else b - 5), beat * 1.2, 0.8), t0 + bb * bar + beat * 2.5)
        elif style == "jazz":
            walk = [b, b + 4, b + 7, b + 5]
            for i, m in enumerate(walk * bars_per):
                dry.add(bass(hz(m), beat * 0.9, 0.85), t0 + i * beat)
        elif style in ("ballad", "ending", "quiet"):
            dry.add(bass(hz(b), dur * 0.9, 0.6), t0, gain=0.7)
        # 전자 피아노
        if style in ("ballad", "ending"):
            arp = tones + tones[-2:0:-1]
            for i in range(int(dur / beat)):
                m = arp[i % len(arp)]
                s = epiano(hz(m), beat * 1.5, 0.55 + 0.15 * rng.random())
                dry.add(s, t0 + i * beat, pan=0.3 * np.sin(i), gain=0.8)
                verb.add(s, t0 + i * beat, gain=0.7)
        elif style in ("lofi", "jazz"):
            hits = [0.0, 1.5, 2.75] if style == "lofi" else [0.0, 1.5, 3.0]
            for bb in range(bars_per):
                for h in hits:
                    sw = 0.06 * beat if (h % 1) else 0.0
                    for k, m in enumerate(tones):
                        s = epiano(hz(m), beat * (1.3 if h == 0 else 0.6), 0.5 + 0.1 * rng.random())
                        at = t0 + bb * bar + h * beat + sw + k * 0.008
                        dry.add(s, at, pan=-0.25 + 0.5 * k / len(tones), gain=0.7)
                        verb.add(s, at, gain=0.4)
        elif style in ("walk", "night"):
            arp = tones + tones[-2:0:-1]
            step = beat / 2
            for i in range(int(dur / step)):
                if style == "night" and i % 2:
                    continue
                m = arp[i % len(arp)]
                s = epiano(hz(m), step * 1.6, 0.42 + 0.12 * rng.random())
                dry.add(s, t0 + i * step, pan=0.35 * np.sin(i * 0.7), gain=0.75)
                verb.add(s, t0 + i * step, gain=0.6)
        elif style == "quiet":
            for i in (0, 3, 5):
                m = tones[i % len(tones)]
                s = epiano(hz(m), beat * 2.5, 0.45)
                dry.add(s, t0 + i * beat, pan=-0.2 + 0.1 * i, gain=0.8)
                verb.add(s, t0 + i * beat, gain=0.9)
        elif style == "drive":
            arp = tones + [tones[0] + 12]
            step = beat / 4
            for i in range(int(dur / step)):
                m = arp[i % len(arp)]
                s = epiano(hz(m), step * 1.2, 0.3 + 0.1 * (i % 4 == 0))
                dry.add(s, t0 + i * step, pan=0.4 * np.sin(i * 0.5), gain=0.55)
                verb.add(s, t0 + i * step, gain=0.35)

    # 멜로디
    if style != "drive":
        dens = {"ballad": 0.45, "ending": 0.6, "quiet": 0.3, "lofi": 0.45, "jazz": 0.5, "walk": 0.45, "night": 0.4}[style]
        for at, m, d in melody(rng, seq, bars_per, beat, bar, density=dens):
            if style in ("ballad", "ending", "quiet", "night"):
                s = bell(hz(m), 2.6, 0.8)
                dry.add(s, at, pan=0.15, gain=0.75)
                verb.add(s, at, gain=1.0)
            else:
                s = epiano(hz(m), d * 0.9, 0.6)
                dry.add(s, at, pan=0.1, gain=0.8)
                verb.add(s, at, gain=0.6)

    # 리듬
    if style in ("lofi", "jazz", "walk", "night", "drive"):
        total_beats = int(length / beat)
        for i in range(total_beats):
            at = i * beat
            if style == "drive":
                dry.add(kick(0.9), at)
            elif style in ("lofi", "night") and i % 4 in (0, 2) and not (style == "night" and i % 4 == 2):
                dry.add(kick(0.8), at)
                if style == "lofi" and i % 8 == 2:
                    dry.add(kick(0.5), at + beat * 0.75)
            elif style == "walk" and i % 4 == 0:
                dry.add(kick(0.6), at)
            if style in ("lofi", "drive", "night") and i % 4 in (1, 3):
                s = noise_hit(0.25, 900, 6000, 0.07, 0.22, rng)
                dry.add(s, at, gain=0.9)
                verb.add(s, at, gain=0.3)
            if style == "jazz" and i % 4 in (1, 3):
                dry.add(noise_hit(0.35, 1500, 7000, 0.12, 0.12, rng), at, pan=0.2)
            for sub in ((0.0, 0.5) if style != "drive" else (0.0, 0.25, 0.5, 0.75)):
                sw = 0.05 * beat if sub == 0.5 and style != "drive" else 0.0
                vel = 0.08 if sub == 0.0 else 0.05
                if style == "walk":
                    vel *= 0.8
                dry.add(noise_hit(0.05, 6000, 14000, 0.012, vel, rng), at + sub * beat + sw, pan=0.3)

    mix = dry.x + reverb(verb.x, 2.6 if wet > 0.3 else 2.0, rng)[:n] * wet * 3.0
    if style in ("lofi", "jazz"):
        hiss = lowpass(rng.standard_normal((n, 2)), 3500) * 0.0035
        crack = np.zeros((n, 2))
        pos = rng.integers(0, n, int(length * 6))
        crack[pos, rng.integers(0, 2, len(pos))] = rng.uniform(0.05, 0.25, len(pos))
        mix += hiss + lowpass(crack, 4000) * 0.5
        mix = lowpass(mix, 9000, 1)
    # 끝의 잔향을 처음에 겹쳐 이음매 없이 반복되게 한다.
    L = int(length * SR)
    out = mix[:L].copy()
    out[: n - L] += mix[L:]
    return master(out, 0.05 if style in ("quiet", "ballad", "ending") else 0.056)


# ── 효과음 ─────────────────────────────────────────────────────
def sfx_all():
    rng = np.random.default_rng(7)
    def stereo(x, width=0.0):
        return np.stack([x, x], axis=1)

    def fin(x, peak):
        x = x - x.mean()
        fade = min(len(x), int(0.01 * SR))
        x[-fade:] *= np.linspace(1, 0, fade)
        return stereo(x / max(np.abs(x).max(), 1e-9) * peak)

    out = {}
    t = np.arange(int(0.05 * SR)) / SR
    out["hover"] = fin(np.sin(2 * np.pi * 2600 * t) * np.exp(-t / 0.008) + 0.4 * np.sin(2 * np.pi * 3900 * t) * np.exp(-t / 0.004), 0.22)

    t = np.arange(int(0.16 * SR)) / SR
    out["click"] = fin(np.sin(2 * np.pi * 880 * t) * np.exp(-t / 0.03) + 0.5 * np.sin(2 * np.pi * 1320 * t) * np.exp(-t / 0.02), 0.42)

    x = np.zeros(int(1.1 * SR))
    for i, m in enumerate((79, 83, 88)):
        b = bell(hz(m), 0.9, 1.0)
        j = int(i * 0.06 * SR)
        x[j:j + len(b)] += b[: len(x) - j]
    out["pick"] = fin(x, 0.5)

    x = np.zeros(int(1.0 * SR))
    for at, m in ((0.0, 84), (0.13, 91)):
        b = bell(hz(m), 0.8, 1.0)
        j = int(at * SR)
        x[j:j + len(b)] += b[: len(x) - j]
    out["phone"] = fin(x, 0.42)

    t = np.arange(int(0.9 * SR)) / SR
    sweep = 900 + 1600 * (t / t[-1]) ** 0.6
    ph = 2 * np.pi * np.cumsum(sweep) / SR
    shimmer = np.sin(ph) * np.exp(-t / 0.35) * (0.6 + 0.4 * np.sin(2 * np.pi * 18 * t))
    for m in (88, 92, 95):
        b = np.pad(bell(hz(m), 0.6, 1.0), (int((m - 86) * 0.025 * SR), 0))[: len(t)]
        shimmer[: len(b)] += 0.5 * b
    out["heart"] = fin(shimmer, 0.4)

    n = int(0.8 * SR)
    t = np.arange(n) / SR
    w = rng.standard_normal(n)
    shape = np.sin(np.pi * np.clip(t / 0.7, 0, 1)) ** 2
    lo = lowpass(w, 1800, 1)
    hi = lowpass(w, 6000, 1)
    mixw = lo * (1 - t / t[-1]) + hi * (t / t[-1])
    out["whoosh"] = fin(highpass(mixw, 250) * shape, 0.35)

    n = int(0.45 * SR)
    t = np.arange(n) / SR
    w = highpass(lowpass(rng.standard_normal(n), 3000), 400) * np.sin(np.pi * np.clip(t / 0.3, 0, 1)) ** 2
    tone = np.sin(2 * np.pi * 523 * t) * np.exp(-t / 0.12) * 0.6
    out["menu"] = fin(w * 0.5 + tone, 0.3)

    x = np.zeros(int(4.0 * SR))
    for at, m in ((0.0, 65), (0.0, 72), (0.18, 76), (0.36, 79), (0.54, 84)):
        b = bell(hz(m), 3.4, 1.0)
        j = int(at * SR)
        x[j:j + len(b)] += b[: len(x) - j]
    out["ending"] = fin(x, 0.6)
    return out


def main():
    os.makedirs(os.path.join(OUT, "bgm"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "sfx"), exist_ok=True)
    only = set(sys.argv[1:])
    for name in TRACKS:
        if only and name not in only:
            continue
        x = render_track(name)
        save_ogg(x, os.path.join(OUT, "bgm", name + ".ogg"))
        print("bgm", name, "%.1fs" % (len(x) / SR))
    if not only or "sfx" in only:
        for name, x in sfx_all().items():
            save_ogg(x, os.path.join(OUT, "sfx", name + ".ogg"), quality=6)
            print("sfx", name)


if __name__ == "__main__":
    main()
