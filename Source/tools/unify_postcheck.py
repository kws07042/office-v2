#!/usr/bin/env python3
"""그림체 통일 결과의 선 굵기를 검사하고, 필요하면 원본 선을 다시 얹는다. (Pillow, numpy)

검사:  python Source/tools/unify_postcheck.py check --index CharacterArt/candidates/unified-v003/INDEX.md
  INDEX.md의 '| `결과` | `원본` |' 행을 읽어, 얼굴 영역의 진한 선 비율을 원본·결과로 비교한다.
  결과가 원본의 90% 미만이면 FAIL로 표시한다(v002는 리아 0.21→0.05로 떨어져 탈락).

선 되얹기:  python Source/tools/unify_postcheck.py lines --index ... [--strength 0.8]
  원본에서 어두운 선만 뽑아 결과 위에 곱하기로 얹는다. 결과 파일을 덮어쓰지 않고 _lines.png 로 따로 저장한다.
외부 접속 없음.
"""
import argparse
import re
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

ROW = re.compile(r"\| `([^`]+\.png)` \| `([^`]+\.png)` \|")


def face_box(img):
    a = img.getchannel("A") if img.mode == "RGBA" else None
    if a is None or a.getextrema()[0] >= 250:
        w, h = img.size
        return (int(w * 0.25), 0, int(w * 0.75), int(h * 0.6))  # 장면 CG는 위쪽 가운데
    x0, y0, x1, y1 = a.getbbox()
    hh, cx = y1 - y0, (x0 + x1) // 2
    return (cx - int(hh * 0.075), y0 + int(hh * 0.05), cx + int(hh * 0.075), y0 + int(hh * 0.2))


def dark_ratio(path, box=None):
    img = Image.open(path).convert("RGBA")
    box = box or face_box(img)
    g = np.array(img.crop(box).convert("L"))
    return float((g < 70).mean()), box


def rows(index):
    base = Path(index).parent
    for out, src in ROW.findall(Path(index).read_text(encoding="utf-8")):
        yield base / out, Path(src)


def check(args):
    fails = 0
    for out, src in rows(args.index):
        s, box = dark_ratio(src)
        r, _ = dark_ratio(out, box)
        ok = r >= s * 0.9
        fails += not ok
        print("%s  원본 %.3f  결과 %.3f  %s" % ("PASS" if ok else "FAIL", s, r, out.name))
    print("FAIL %d장" % fails)


def lines(args):
    for out, src in rows(args.index):
        o = Image.open(out).convert("RGBA")
        s = Image.open(src).convert("RGBA").resize(o.size, Image.LANCZOS)
        g = np.array(s.convert("L")).astype(np.float32)
        mask = np.clip((110 - g) / 60.0, 0, 1) * args.strength  # 어두운 선일수록 1
        mask = np.array(Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))).astype(np.float32) / 255
        oa = np.array(o).astype(np.float32)
        sl = np.array(s).astype(np.float32)
        oa[..., :3] = oa[..., :3] * (1 - mask[..., None]) + np.minimum(oa[..., :3], sl[..., :3]) * mask[..., None]
        Image.fromarray(oa.clip(0, 255).astype(np.uint8)).save(out.with_name(out.stem + "_lines.png"))
        print("저장:", out.stem + "_lines.png")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["check", "lines"])
    ap.add_argument("--index", required=True)
    ap.add_argument("--strength", type=float, default=0.8)
    a = ap.parse_args()
    (check if a.mode == "check" else lines)(a)
