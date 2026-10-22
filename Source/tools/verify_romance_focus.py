from pathlib import Path
import hashlib
import json
import shutil
import zipfile

P = Path(__file__).resolve().parents[1]
S = P.parent
B = S / "afterwork-windows-builds"
name = "afterwork_script_prototype-0.27.0-romance-focus-win"
package = B / (name + ".zip")
destination = B / "playable-romance-focus"
validation = B / "native-romance-focus"
proof = P / "testing/romance-focus-v1"
assert not destination.exists() and not validation.exists(), "Fresh verification destination required"
hashes = {}
with zipfile.ZipFile(package) as archive:
    assert archive.testzip() is None, "ZIP CRC failed"
    names = archive.namelist()
    assert not any(n.endswith(".rpy") and "/game/" in n for n in names)
    assert not any(n.endswith(("_tests.rpyc", "testcases.rpyc", "three_choice_cases.json")) for n in names)
    assert not any(
        n.startswith(tuple(name + "/" + d for d in
                           ("game/saves/", "testing/", "tests/", "tools/", "story/", "opening-traces/")))
        for n in names
    )
    for member in names:
        assert (destination / member).resolve().is_relative_to(destination.resolve()), member
        prefix = name + "/game/"
        if not member.startswith(prefix) or member.endswith("/"):
            continue
        relative = member[len(prefix):]
        if relative.startswith("cache/") or relative == "script_version.txt":
            continue
        data = archive.read(member)
        assert data == (P / "game" / relative).read_bytes(), relative
        hashes[relative] = hashlib.sha256(data).hexdigest()
    for required in (
        "ria_r13_e01.rpyc", "jihyun_r13_e01.rpyc", "yujin_r05_r08.rpyc",
        "yujin_r13_e01.rpyc", "seoyun_r01_r04.rpyc", "seoyun_r05_r12.rpyc",
        "seoyun_r13_e01.rpyc", "options.rpyc", "office_phone.rpyc",
        "fonts/GowunDodum-Regular.ttf", "fonts/GowunDodum-OFL.txt",
        "fonts/Pretendard-Regular.otf", "fonts/Pretendard-LICENSE.txt",
    ):
        assert required in hashes, required
    archive.extractall(destination)
clean = destination / name
shutil.copytree(clean, validation)
for file in (P / "game").glob("*_tests.rpy"):
    shutil.copy2(file, validation / "game" / file.name)
    shutil.copy2(file.with_suffix(".rpyc"), validation / "game" / file.with_suffix(".rpyc").name)
for file in ("testcases.rpy", "testcases.rpyc", "three_choice_cases.json"):
    shutil.copy2(P / "game" / file, validation / "game" / file)
previous = json.loads((P / "testing/finale-daily-v1/package-verification.json").read_text(encoding="utf-8"))
assert all(hashes[n] == previous["game_file_hashes"][n] for n in hashes if n.startswith("images/"))
report = {
    "version": "0.27.0-romance-focus",
    "crc": "passed",
    "zip_sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
    "zip_bytes": package.stat().st_size,
    "game_file_hashes": hashes,
    "source_tests_saves_excluded": True,
    "clean_release": str(clean),
    "validation": str(validation),
}
(proof / "package-verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
(proof / "unchanged-assets.json").write_text(
    json.dumps({"images_unchanged": True, "compared_to": "0.26.0-finale-daily", "rigging_changed": False}, indent=2),
    encoding="utf-8",
)
print(json.dumps({"files_verified": len(hashes), "zip_bytes": package.stat().st_size, "clean_release": str(clean)}, ensure_ascii=False))
