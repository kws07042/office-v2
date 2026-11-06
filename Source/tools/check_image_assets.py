#!/usr/bin/env python3
"""Read-only PNG/pinned-hash/planned-path audit. Requires Pillow.

Run from any directory: python3 Source/tools/check_image_assets.py [PATH ...]
Paths must stay inside this repository. JSON is printed to stdout; no files are
written. Decode/size/alpha checks do not establish visual quality or approval.
"""
import argparse
import ast
import hashlib
import json
import warnings
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]
Image.MAX_IMAGE_PIXELS = 40_000_000


def inspect(path, expected=None):
    result = {"path": path.relative_to(ROOT).as_posix()}
    try:
        resolved = path.resolve(strict=True)
        if not resolved.is_relative_to(ROOT):
            raise ValueError("symlink escapes repository")
        if resolved.stat().st_size > 64 * 1024 * 1024:
            raise ValueError("file exceeds 64 MiB input limit")
        data = resolved.read_bytes()
        result.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        with warnings.catch_warnings():
            warnings.simplefilter("error", Image.DecompressionBombWarning)
            with Image.open(resolved) as image:
                if image.format != "PNG":
                    raise ValueError("expected PNG format")
                image.verify()
            with Image.open(resolved) as image:
                image.load()
                rgba = image.convert("RGBA")
                counts = rgba.getchannel("A").histogram()
                result.update(width=image.width, height=image.height, mode=image.mode,
                              alpha_channel="A" in image.getbands() or "transparency" in image.info,
                              transparent_pixels=counts[0], partial_alpha_pixels=sum(counts[1:255]),
                              aspect_ratio=image.width / image.height)
        result["status"] = "PASS_TECHNICAL"
        if expected:
            result["baseline_match"] = result["sha256"] == expected
            if not result["baseline_match"]:
                result.update(status="FAIL", error="pinned SHA-256 differs")
    except (OSError, ValueError, Image.DecompressionBombError, Image.DecompressionBombWarning) as exc:
        result.update(status="FAIL", error=str(exc))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="repository-relative files or directories")
    args = parser.parse_args()
    roots = [ROOT / x for x in args.paths] or [ROOT / "CharacterArt/assets", ROOT / "Source/game/images"]
    paths = set()
    for p in roots:
        # A clean checkout omits directories left empty by the art reset.
        if not args.paths and not p.exists():
            continue
        if not p.resolve().is_relative_to(ROOT) or not p.exists():
            parser.error("input must exist inside repository: " + str(p))
        if p.is_file():
            if p.suffix.lower() != ".png":
                parser.error("file input must be PNG")
            paths.add(p)
        else:
            paths.update(x for x in p.rglob("*") if x.suffix.lower() == ".png" and x.is_file())
    manifest = json.loads((ROOT / "CharacterArt/CURRENT_ASSETS.json").read_text())
    baseline = {"CharacterArt/" + k: v for k, v in manifest["sha256"].items()}
    rows = [inspect(p, baseline.get(p.relative_to(ROOT).as_posix())) for p in sorted(paths)]
    hashes = {}
    for row in rows:
        if "sha256" in row:
            hashes.setdefault(row["sha256"], []).append(row["path"])
    plan = json.loads((ROOT / "Source/game/event_cg_plan.json").read_text())
    missing = []
    for s in plan["sets"]:
        for asset in [s["intro_cg"], s["intro_expression"]] + s["base_cg"]:
            target = (ROOT / "Source/game" / asset["planned_path"]).resolve()
            if not target.is_relative_to(ROOT / "Source/game") or not target.is_file():
                missing.append({"id": asset["id"], "planned_path": asset["planned_path"]})
    # Read only the literal media table, never import or execute game Python.
    phone_source = (ROOT / "Source/game/office_phone.rpy").read_text(encoding="utf-8")
    phone_table = next(line.strip().split("=", 1)[1].strip()
                       for line in phone_source.splitlines() if line.strip().startswith("PHONE_MEDIA ="))
    phone_media = ast.literal_eval(phone_table)
    missing_messages = []
    for media_id, media in phone_media.items():
        target = (ROOT / "Source/game" / media["path"]).resolve()
        if not target.is_relative_to(ROOT / "Source/game") or not target.is_file():
            missing_messages.append({"id": media_id, "planned_path": media["path"]})
    errors = sum(r["status"] == "FAIL" for r in rows)
    print(json.dumps(dict(files=rows, count=len(rows), errors=errors,
                         duplicate_sha256=[v for v in hashes.values() if len(v) > 1],
                         missing_planned_assets=missing,
                         missing_message_assets=missing_messages,
                         note="Missing planned assets are incomplete production, not PNG decode failures; visual QA and approval remain separate."),
                     ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
