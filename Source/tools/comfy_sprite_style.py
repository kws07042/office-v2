#!/usr/bin/env python3
"""ComfyUI로 입상(투명 PNG)의 그림체를 마스터에 맞춘다. 사용자 PC에서 실행한다.

ComfyUI는 투명 배경을 그대로 다루지 못하므로:
  1. 입상을 중간 회색(#808080) 배경에 얹어 ComfyUI로 보낸다.
  2. 결과에 원본 누끼(알파)를 그대로 다시 씌운다. 윤곽·크기·위치가 원본과 같게 유지된다.
  3. 같은 포즈의 표정들은 neutral 결과의 몸 + 각 표정 결과의 얼굴 부분만 합쳐, 몸이 픽셀 단위로 같게 만든다.

준비 (ComfyUI에서 한 번만, 배경용과 같은 방식)
  - img2img + ControlNet lineart(anime) 0.85 + depth 0.5 + IP-Adapter(마스터, style transfer 0.55)
  - 노드 제목: SP_INPUT(Load Image), SP_POSITIVE(긍정 프롬프트), SP_SAMPLER(KSampler)
  - denoise 0.30 안팎. Workflow → Export (API) → sprite_workflow_api.json

실행 예
  python Source/tools/comfy_sprite_style.py --workflow sprite_workflow_api.json \
      --who seoyun --outfit casual --poses pose01 pose02 --src-version v003 --out-version v004 \
      --folder CharacterArt/candidates/chatgpt-v001

  --only-neutral 을 붙이면 각 포즈 neutral만 돌린다(값을 정할 때).
표준 라이브러리 + Pillow만 쓰고, 로컬 ComfyUI(127.0.0.1:8188)에만 접속한다. 기존 파일은 덮어쓰지 않는다.
"""
import argparse
import io
import json
import sys
import time
import urllib.parse
import urllib.request
import uuid
import zlib
from pathlib import Path

from PIL import Image, ImageChops, ImageFilter

PROMPT = {
    "seoyun": "1girl, solo, adult woman, long wavy dark plum hair, pink inner hair, half-lidded blue eyes, mole under left eye",
    "ria": "1girl, solo, adult woman, very long wavy blonde high ponytail, blue scrunchie, straight bangs, blue eyes",
    "jihyun": "1girl, solo, adult woman, very long crimson hair, side-swept bangs, red-brown eyes",
    "yujin": "1girl, solo, adult woman, silver-white bob hair, gold hairpin, thin round metal glasses, amber eyes",
}
COMMON = ", full body, standing, simple gray background, clean bold lineart, cel shading, two-tone hard-edged shadows, anime visual novel sprite"
GRAY = (128, 128, 128, 255)


def find_node(workflow, title):
    for node in workflow.values():
        if node.get("_meta", {}).get("title") == title:
            return node
    sys.exit("워크플로에서 제목이 '%s'인 노드를 찾지 못했습니다." % title)


def http(server, path, data=None, headers=None):
    req = urllib.request.Request("http://%s%s" % (server, path), data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=900) as resp:
        return resp.read()


def upload(server, name, png_bytes):
    boundary = uuid.uuid4().hex
    body = (("--%s\r\nContent-Disposition: form-data; name=\"image\"; filename=\"%s\"\r\nContent-Type: image/png\r\n\r\n" % (boundary, name)).encode()
            + png_bytes + ("\r\n--%s\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue\r\n--%s--\r\n" % (boundary, boundary)).encode())
    return json.loads(http(server, "/upload/image", body, {"Content-Type": "multipart/form-data; boundary=" + boundary}))["name"]


def run(server, template, sprite, prompt, seed):
    flat = Image.new("RGBA", sprite.size, GRAY)
    flat.alpha_composite(sprite)
    buf = io.BytesIO()
    flat.convert("RGB").save(buf, "PNG")
    wf = json.loads(json.dumps(template))
    find_node(wf, "SP_INPUT")["inputs"]["image"] = upload(server, "sprite_in.png", buf.getvalue())
    find_node(wf, "SP_POSITIVE")["inputs"]["text"] = prompt
    find_node(wf, "SP_SAMPLER")["inputs"]["seed"] = seed
    pid = json.loads(http(server, "/prompt", json.dumps({"prompt": wf, "client_id": uuid.uuid4().hex}).encode(),
                          {"Content-Type": "application/json"}))["prompt_id"]
    while True:
        hist = json.loads(http(server, "/history/" + pid))
        if pid in hist:
            break
        time.sleep(2)
    for out in hist[pid]["outputs"].values():
        for img in out.get("images", []):
            q = urllib.parse.urlencode({"filename": img["filename"], "subfolder": img.get("subfolder", ""), "type": img["type"]})
            result = Image.open(io.BytesIO(http(server, "/view?" + q))).convert("RGB")
            if result.size != sprite.size:
                result = result.resize(sprite.size, Image.LANCZOS)
            result = result.convert("RGBA")
            result.putalpha(sprite.getchannel("A"))  # 원본 누끼를 그대로
            return result
    sys.exit("결과 이미지가 없습니다. Save Image 노드를 확인하세요.")


def face_mask(neutral, other):
    """두 원본 표정이 다른 영역(얼굴)만 골라 넉넉히 넓히고 부드럽게 한다."""
    diff = ImageChops.difference(neutral.convert("RGB"), other.convert("RGB")).convert("L").point(lambda v: 255 if v > 12 else 0)
    box = diff.getbbox()
    mask = Image.new("L", neutral.size, 0)
    if box:
        x0, y0, x1, y1 = box
        pad = 18
        mask.paste(255, (max(0, x0 - pad), max(0, y0 - pad), x1 + pad, y1 + pad))
    return mask.filter(ImageFilter.GaussianBlur(8))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workflow", required=True, type=Path)
    ap.add_argument("--who", required=True, choices=sorted(PROMPT))
    ap.add_argument("--outfit", required=True)
    ap.add_argument("--poses", nargs="+", required=True)
    ap.add_argument("--src-version", required=True)
    ap.add_argument("--out-version", required=True)
    ap.add_argument("--folder", required=True, type=Path)
    ap.add_argument("--server", default="127.0.0.1:8188")
    ap.add_argument("--only-neutral", action="store_true")
    args = ap.parse_args()
    template = json.loads(args.workflow.read_text(encoding="utf-8"))
    prompt = PROMPT[args.who] + COMMON
    for pose in args.poses:
        stem = "%s_%s_%s" % (args.who, args.outfit, pose)
        files = sorted(args.folder.glob("%s_*_%s.png" % (stem, args.src_version)))
        neutral_path = args.folder / ("%s_neutral_%s.png" % (stem, args.src_version))
        if not neutral_path.exists():
            print("neutral 없음:", neutral_path.name)
            continue
        seed = zlib.crc32(stem.encode()) % (2 ** 32)
        neutral_src = Image.open(neutral_path).convert("RGBA")
        print("처리 중:", neutral_path.name, flush=True)
        neutral_out = run(args.server, template, neutral_src, prompt, seed)
        targets = [neutral_path] if args.only_neutral else files
        for path in targets:
            out_path = args.folder / path.name.replace("_" + args.src_version, "_" + args.out_version)
            if out_path.exists():
                print("건너뜀(이미 있음):", out_path.name)
                continue
            if path == neutral_path:
                neutral_out.save(out_path)
                continue
            print("처리 중:", path.name, flush=True)
            src = Image.open(path).convert("RGBA")
            styled = run(args.server, template, src, prompt, seed)
            merged = neutral_out.copy()
            merged.paste(styled, (0, 0), face_mask(neutral_src, src))  # 몸은 neutral 결과, 얼굴만 이 표정
            merged.putalpha(src.getchannel("A"))
            merged.save(out_path)
    print("완료")


if __name__ == "__main__":
    main()
