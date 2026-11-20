#!/usr/bin/env python3
"""ChatGPT가 만든 입상·장면 CG의 그림체를 마스터에 맞춘다. 사용자 PC에서 실행한다.

워크플로: Source/tools/comfyui/master_style_api.json
  img2img + ControlNet(애니 선화 0.85, 깊이 0.5)로 구도·윤곽을 잠그고,
  IP-Adapter(strong style transfer)로 마스터 그림(REF_MASTER)의 선·눈·채색을 입힌다.
  얼굴·옷·구도는 원본 그대로, 그리는 방식만 마스터를 따른다.

준비 (한 번만)
  1. ComfyUI에서 master_style_api.json 을 끌어다 놓는다.
  2. CKPT·CN_LINEART·CN_DEPTH 노드에서 CHANGE_ME 로 된 모델을 내 PC의 파일로 고른다.
     SAMPLER 노드의 steps·cfg·sampler는 마스터를 만든 값으로 바꾼다.
  3. 메뉴 Workflow → Export (API) 로 다시 저장한다. 예: my_master_style_api.json

실행 예
  # 입상: 투명 배경을 유지하고, 같은 포즈의 표정들은 neutral 몸 + 각 표정 얼굴로 합친다
  python Source/tools/comfy_style_unify.py --workflow my_master_style_api.json \
      --files "CharacterArt/candidates/chatgpt-v002/jihyun_casual_pose02_*_v001.png" --out-version v002

  # 최근 ChatGPT 그림 전부(목록 파일 사용, 결과는 별도 폴더)
  python Source/tools/comfy_style_unify.py --workflow my_master_style_api.json \
      --list Docs/unify-list-v001.txt --out-dir CharacterArt/candidates/unified-v001 --out-version v101

  # 장면 CG·타이틀
  python Source/tools/comfy_style_unify.py --workflow my_master_style_api.json \
      --files "CharacterArt/candidates/cg-chatgpt-v001/*_v001.png" --out-version v002

  --first 1 로 한 장만 시험한다. --denoise, --style-weight 로 세기를 덮어쓴다.
  결과는 같은 폴더에 버전만 바꾼 이름으로 저장한다. 기존 파일은 덮어쓰지 않는다.

표준 라이브러리 + Pillow만 쓰고, 로컬 ComfyUI(127.0.0.1:8188)에만 접속한다.
"""
import argparse
import glob
import io
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import uuid
import zlib
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

MASTER = "CharacterArt/candidates/heroine-masters-v001/final_2048x3072/ria_office_pose01_neutral_v001.png"
HEROINE = {
    "ria": "kang ria, very long wavy honey-blonde high ponytail, blue scrunchie, straight bangs, blue eyes",
    "jihyun": "baek jihyun, very long wavy crimson hair, side-swept bangs, red-brown eyes",
    "yujin": "cha yujin, silver-gray bob hair, gold hairpin, thin round metal glasses, amber eyes",
    "seoyun": "han seoyun, very long wavy dark plum hair, pink inner hair, half-lidded blue eyes, mole under left eye",
}
STYLE = "anime visual novel illustration, clean bold lineart, cel shading, two-tone hard-edged shadows, crisp highlights"
SPRITE_TAIL = ", 1girl, solo, adult woman, full body, standing, simple gray background"
CG_TAIL = ", detailed background, adult women"
BG_PROMPT = STYLE + ", scenery, no humans, background art, clean thin lineart, muted slightly desaturated colors"
GRAY = (128, 128, 128, 255)
VERSION = re.compile(r"_v\d{3}(?=\.png$)")
SPRITE_NAME = re.compile(r"^(?P<stem>[a-z]+_[a-z]+_pose\d\d)_(?P<expr>[a-z]+)_v\d{3}\.png$")


def find_node(wf, title):
    for node in wf.values():
        if node.get("_meta", {}).get("title") == title:
            return node
    sys.exit("워크플로에서 제목이 '%s'인 노드를 찾지 못했습니다. master_style_api.json 을 기준으로 만들었는지 확인하세요." % title)


def http(server, path, data=None, headers=None):
    req = urllib.request.Request("http://%s%s" % (server, path), data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=900) as resp:
        return resp.read()


def upload(server, name, png_bytes):
    boundary = uuid.uuid4().hex
    body = (("--%s\r\nContent-Disposition: form-data; name=\"image\"; filename=\"%s\"\r\nContent-Type: image/png\r\n\r\n" % (boundary, name)).encode()
            + png_bytes + ("\r\n--%s\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue\r\n--%s--\r\n" % (boundary, boundary)).encode())
    return json.loads(http(server, "/upload/image", body, {"Content-Type": "multipart/form-data; boundary=" + boundary}))["name"]


def png(img):
    buf = io.BytesIO()
    img.save(buf, "PNG")
    return buf.getvalue()


def prompt_for(name, sprite):
    if name.startswith("bg_"):
        return BG_PROMPT
    who = [k for k in HEROINE if name.startswith(k + "_")]
    if who:
        base = HEROINE[who[0]]
    else:  # 공통·타이틀·이듬해 봄: 네 명 모두
        base = "multiple girls, " + "; ".join(HEROINE.values())
    return STYLE + ", " + base + (SPRITE_TAIL if sprite else CG_TAIL)


def is_sprite(img):
    return img.mode == "RGBA" and img.getchannel("A").getextrema()[0] < 250


def fit(img, max_side):
    """SDXL 계열이 다루기 좋은 크기(64의 배수, 긴 변 max_side)로 줄인다."""
    w, h = img.size
    s = min(1.0, max_side / float(max(w, h)))
    nw, nh = max(64, int(w * s) // 64 * 64), max(64, int(h * s) // 64 * 64)
    return img.resize((nw, nh), Image.LANCZOS)


def run(args, template, ref_name, img, name, sprite):
    src = img
    if sprite:
        flat = Image.new("RGBA", img.size, GRAY)
        flat.alpha_composite(img)
        src = flat
    work = fit(src.convert("RGB"), args.max_side)
    wf = json.loads(json.dumps(template))
    find_node(wf, "IN_IMAGE")["inputs"]["image"] = upload(args.server, "unify_in.png", png(work))
    find_node(wf, "REF_MASTER")["inputs"]["image"] = ref_name
    find_node(wf, "POSITIVE")["inputs"]["text"] = prompt_for(name, sprite)
    sampler = find_node(wf, "SAMPLER")["inputs"]
    sampler["seed"] = zlib.crc32(name.encode()) % (2 ** 32)
    sampler["denoise"] = args.denoise if args.denoise is not None else (0.30 if sprite else (0.35 if name.startswith("bg_") else 0.38))
    if args.style_weight is not None:
        find_node(wf, "STYLE_IPA")["inputs"]["weight"] = args.style_weight
    pid = json.loads(http(args.server, "/prompt", json.dumps({"prompt": wf, "client_id": uuid.uuid4().hex}).encode(),
                          {"Content-Type": "application/json"}))["prompt_id"]
    while True:
        hist = json.loads(http(args.server, "/history/" + pid))
        if pid in hist:
            break
        time.sleep(2)
    for out in hist[pid]["outputs"].values():
        for im in out.get("images", []):
            q = urllib.parse.urlencode({"filename": im["filename"], "subfolder": im.get("subfolder", ""), "type": im["type"]})
            result = Image.open(io.BytesIO(http(args.server, "/view?" + q))).convert("RGB").resize(img.size, Image.LANCZOS)
            if sprite:
                result = result.convert("RGBA")
                result.putalpha(img.getchannel("A"))  # 원본 누끼 그대로: 윤곽·크기·위치가 바뀌지 않는다
            return result
    sys.exit("결과 이미지가 없습니다. SAVE 노드를 확인하세요.")


def face_mask(neutral, other):
    """두 원본이 다른 곳(얼굴)만 넉넉히 골라 부드럽게 한다."""
    diff = ImageChops.difference(neutral.convert("RGB"), other.convert("RGB")).convert("L").point(lambda v: 255 if v > 12 else 0)
    box = diff.getbbox()
    mask = Image.new("L", neutral.size, 0)
    if box:
        x0, y0, x1, y1 = box
        mask.paste(255, (max(0, x0 - 18), max(0, y0 - 18), x1 + 18, y1 + 18))
    return mask.filter(ImageFilter.GaussianBlur(8))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workflow", required=True, type=Path)
    ap.add_argument("--files", nargs="+", default=[], help="파일 또는 glob 패턴")
    ap.add_argument("--list", type=Path, help="처리할 파일 경로를 한 줄에 하나씩 적은 목록")
    ap.add_argument("--out-dir", type=Path, help="결과를 이 폴더에 원래 폴더 이름별로 저장(파일 이름은 _vNNN 만 바꿈)")
    ap.add_argument("--out-version", required=True, help="예: v002")
    ap.add_argument("--ref", default=MASTER, type=Path, help="마스터 그림")
    ap.add_argument("--server", default="127.0.0.1:8188")
    ap.add_argument("--denoise", type=float, help="기본: 입상 0.30, CG 0.38")
    ap.add_argument("--style-weight", type=float, help="IP-Adapter 세기. 기본은 워크플로 값(0.85)")
    ap.add_argument("--max-side", type=int, default=1536)
    ap.add_argument("--first", type=int, help="앞에서 N장만")
    args = ap.parse_args()
    if not re.fullmatch(r"v\d{3}", args.out_version):
        sys.exit("--out-version 은 v002 같은 형식이어야 합니다.")
    template = json.loads(args.workflow.read_text(encoding="utf-8"))
    pats = list(args.files)
    if args.list:
        pats += [l.strip() for l in args.list.read_text(encoding="utf-8").splitlines() if l.strip()]
    files = sorted({Path(p) for pat in pats for p in glob.glob(pat)})
    files = [f for f in files if f.suffix == ".png" and VERSION.search(f.name) and not f.name.endswith("_%s.png" % args.out_version)]
    if args.first:
        files = files[:args.first]
    if not files:
        sys.exit("처리할 파일이 없습니다.")
    ref_name = upload(args.server, "master_ref.png", args.ref.read_bytes())
    done = {}  # 같은 포즈 neutral의 (원본, 결과)
    # neutral 먼저 처리해서 같은 포즈 표정들이 몸을 공유하게 한다
    files.sort(key=lambda f: (0 if "_neutral_" in f.name else 1, f.name))
    for path in files:
        out = path.with_name(VERSION.sub("_" + args.out_version, path.name))
        if args.out_dir:
            out = args.out_dir / path.parent.name / out.name
            out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            print("건너뜀(이미 있음):", out.name)
            continue
        img = Image.open(path)
        sprite = is_sprite(img)
        img = img.convert("RGBA") if sprite else img.convert("RGB")
        print("처리 중:", path.name, "(입상)" if sprite else "(CG)", flush=True)
        result = run(args, template, ref_name, img, path.name, sprite)
        m = SPRITE_NAME.match(path.name)
        if sprite and m:
            key = (path.parent, m.group("stem"))
            if m.group("expr") == "neutral":
                done[key] = (img, result)
            elif key in done and done[key][0].size == img.size:
                n_src, n_out = done[key]
                merged = n_out.copy()
                merged.paste(result, (0, 0), face_mask(n_src, img))  # 몸은 neutral 결과, 얼굴만 이 표정
                merged.putalpha(img.getchannel("A"))
                result = merged
        result.save(out)
    print("완료")


if __name__ == "__main__":
    main()
