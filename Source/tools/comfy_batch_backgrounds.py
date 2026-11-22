#!/usr/bin/env python3
"""ComfyUI로 배경 23장을 한 번에 그림체 통일(img2img)한다. 사용자 PC에서 실행한다.

준비 (ComfyUI 화면에서 한 번만)
  1. 마스터 워크플로에 Docs/backgrounds-title-plan-v001.md 4절대로 img2img·ControlNet·IP-Adapter를 붙인다.
  2. 아래 노드의 제목(Title)을 바꾼다. 우클릭 → Title.
       BG_INPUT     배경을 읽는 Load Image 노드
       BG_POSITIVE  긍정 프롬프트 CLIP Text Encode 노드
       BG_SAMPLER   KSampler 노드
  3. 사무실 1장으로 값이 마음에 들면 메뉴 Workflow → Export (API)로 저장한다. 예: bg_workflow_api.json

실행
  python comfy_batch_backgrounds.py --workflow bg_workflow_api.json \
      --input CharacterArt/candidates/bg-chatgpt-v001 --output CharacterArt/candidates/bg-chatgpt-v001

  --only bg_office 처럼 일부만 돌릴 수 있다. --denoise 로 노이즈 강도를 덮어쓸 수 있다.
  결과는 bg_<장소>_day_v003.png 로 저장된다. 기존 파일은 덮어쓰지 않는다.

이 스크립트는 표준 라이브러리만 쓰고, 로컬 ComfyUI(기본 127.0.0.1:8188)에만 접속한다.
"""
import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
import uuid
import zlib
from pathlib import Path

COMMON = ("anime visual novel background, scenery, no humans, clean thin lineart, cel shading, "
          "flat colors with soft two-tone shadows, muted colors, slightly desaturated, lived-in, ")

PLACES = {
    "bg_office": "small branding design office interior, white desks by the window, monitors, color swatches, shared work table, glass meeting room door",
    "bg_meeting": "office meeting room, long wooden table, gray chairs, glass wall, wall-mounted screen turned off, whiteboard",
    "bg_client_hall": "large corporate boardroom, long glossy table, leather chairs, big presentation screen, floor-to-ceiling windows, high-rise view",
    "bg_pantry": "office pantry, small sink, coffee machine, microwave, mug shelf, small round table with two chairs",
    "bg_corridor": "office corridor end, large window with low sill, elevator doors on the left, bulletin board",
    "bg_rooftop": "office building rooftop, low railing, metal fence, air conditioner units, old bench, city skyline",
    "bg_stairs": "office building emergency staircase landing, gray stairs, handrail, green exit light, small window",
    "bg_company_front": "sidewalk in front of a five-story office building, glass entrance, bus stop shelter with bench, street trees, crosswalk",
    "bg_popup": "pop-up store setup inside a shopping mall, half-built display stands, cardboard boxes, light stands, tape marks on floor",
    "bg_cafe": "cozy neighborhood cafe, wooden tables, window seats, counter with espresso machine, cup shelves",
    "bg_bookcafe": "neighborhood bookstore cafe, wall of wooden bookshelves, book display table, small tables by the window, warm lamps",
    "bg_restaurant": "old korean pojangmacha restaurant, stainless round tables, plastic stools, open kitchen counter with big pots, incandescent bulbs",
    "bg_park": "riverside park path, bench under trees, grass, river railing, apartments in the distance",
    "bg_street": "busy street in front of a subway station, subway entrance, shop fronts, street lamps, wide sidewalk",
    "bg_train": "empty subway car interior, long seats, hand straps, windows with above-ground view",
    "bg_gallery": "small independent gallery, white walls with framed abstract paintings, track lights, long bench",
    "bg_laundry": "neighborhood coin laundromat, rows of washers and dryers, folding table, plastic chairs, large glass window",
    "bg_ria_home": "small korean studio apartment, wooden floor, curtains, bright sofa with cushions, ring light, photo postcards on wall, small kitchen, slightly messy",
    "bg_jihyun_home": "tidy korean apartment living room, wooden floor, gray and burgundy tones, workbench with toolbox and parts, bookshelf, sofa",
    "bg_yujin_home": "small korean studio apartment, wooden floor, curtains, desk with drawing tablet, sketchbooks, cream rug, bed, warm lamp",
    "bg_seoyun_studio": "studio-apartment workspace, wooden floor, big wooden work table with documents and books, wall bookshelves, sofa bed, small kitchen, lavender curtains",
    "bg_dohyun_room": "simple korean one-room apartment, bed, desk with laptop, small clothes rack, window",
    "bg_motel": "business motel room, double bed, bedside lamp, small tv, curtained window",
}


def pick_source(folder, name):
    """가장 높은 버전의 낮판을 고른다(v003 출력은 입력에서 뺀다)."""
    found = sorted(folder.glob(name + "_day_v00[12].png"))
    return found[-1] if found else None


def find_node(workflow, title):
    for node_id, node in workflow.items():
        if node.get("_meta", {}).get("title") == title:
            return node_id, node
    sys.exit("워크플로에서 제목이 '%s'인 노드를 찾지 못했습니다. README 순서 2를 확인하세요." % title)


def http(server, path, data=None, headers=None):
    req = urllib.request.Request("http://%s%s" % (server, path), data=data, headers=headers or {})
    with urllib.request.urlopen(req, timeout=600) as resp:
        return resp.read()


def upload(server, path):
    boundary = uuid.uuid4().hex
    body = (("--%s\r\nContent-Disposition: form-data; name=\"image\"; filename=\"%s\"\r\n"
             "Content-Type: image/png\r\n\r\n" % (boundary, path.name)).encode()
            + path.read_bytes()
            + ("\r\n--%s\r\nContent-Disposition: form-data; name=\"overwrite\"\r\n\r\ntrue\r\n--%s--\r\n" % (boundary, boundary)).encode())
    result = json.loads(http(server, "/upload/image", body, {"Content-Type": "multipart/form-data; boundary=" + boundary}))
    return result["name"]


def run_one(server, template, name, source, denoise):
    workflow = json.loads(json.dumps(template))
    _, load = find_node(workflow, "BG_INPUT")
    _, positive = find_node(workflow, "BG_POSITIVE")
    _, sampler = find_node(workflow, "BG_SAMPLER")
    load["inputs"]["image"] = upload(server, source)
    positive["inputs"]["text"] = COMMON + PLACES[name]
    sampler["inputs"]["seed"] = zlib.crc32(name.encode()) % (2 ** 32)  # 장소마다 고정 시드
    if denoise is not None:
        sampler["inputs"]["denoise"] = denoise
    client = uuid.uuid4().hex
    prompt_id = json.loads(http(server, "/prompt", json.dumps({"prompt": workflow, "client_id": client}).encode(),
                                {"Content-Type": "application/json"}))["prompt_id"]
    while True:
        history = json.loads(http(server, "/history/" + prompt_id))
        if prompt_id in history:
            break
        time.sleep(2)
    for output in history[prompt_id]["outputs"].values():
        for image in output.get("images", []):
            query = urllib.parse.urlencode({"filename": image["filename"], "subfolder": image.get("subfolder", ""), "type": image["type"]})
            return http(server, "/view?" + query)
    sys.exit("%s: 결과 이미지가 없습니다. Save Image 노드를 확인하세요." % name)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--workflow", required=True, type=Path)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--server", default="127.0.0.1:8188")
    parser.add_argument("--only", nargs="*")
    parser.add_argument("--denoise", type=float)
    args = parser.parse_args()
    template = json.loads(args.workflow.read_text(encoding="utf-8"))
    args.output.mkdir(parents=True, exist_ok=True)
    names = args.only or list(PLACES)
    for name in names:
        if name not in PLACES:
            sys.exit("모르는 장소: %s" % name)
        target = args.output / (name + "_day_v003.png")
        if target.exists():
            print("건너뜀(이미 있음):", target.name)
            continue
        source = pick_source(args.input, name)
        if source is None:
            print("입력 없음:", name)
            continue
        print("처리 중:", source.name, "->", target.name, flush=True)
        target.write_bytes(run_one(args.server, template, name, source, args.denoise))
    print("완료")


if __name__ == "__main__":
    main()
