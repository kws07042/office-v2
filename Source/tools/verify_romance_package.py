"""Verify and unpack this revision without touching existing releases."""
from pathlib import Path
import hashlib
import json
import zipfile

project = Path(__file__).resolve().parents[1]
stage = project.parent
builds = stage / "afterwork-windows-builds"
package = builds / "afterwork_script_prototype-0.2.2-romance-win.zip"
release = "afterwork_script_prototype-0.2.2-romance-win"
destination = builds / "playable-romance-final"
assert not destination.exists(), "Use a new extraction folder."
with zipfile.ZipFile(package) as archive:
    assert archive.testzip() is None
    names = archive.namelist()
    assert not any("/game/" in name and name.endswith(".rpy") for name in names)
    assert not any(name.endswith(("testcases.rpyc", "-success.json")) for name in names)
    assert not any(name.startswith(tuple(release + "/" + folder for folder in ("game/saves/", "testing/", "tests/"))) for name in names)
    compiled = {}
    for filename in ("common.rpyc", "ria_r01.rpyc", "ria_r02_r04.rpyc", "core.rpyc", "screens.rpyc", "options.rpyc"):
        source = (project / "game" / filename).read_bytes()
        packaged = archive.read(release + "/game/" + filename)
        assert source == packaged, filename + " differs from tested source"
        compiled[filename] = hashlib.sha256(packaged).hexdigest()
    assert any(name.endswith("/afterwork_script_prototype.exe") for name in names)
    for name in names:
        resolved = (destination / name).resolve()
        assert resolved.is_relative_to(destination.resolve()), "Unsafe archive path"
    archive.extractall(destination)
result = {
    "release": release,
    "zip_bytes": package.stat().st_size,
    "zip_sha256": hashlib.sha256(package.read_bytes()).hexdigest(),
    "archive_crc": "passed",
    "source_test_byte_match": compiled,
    "testcases_and_saves_excluded": True,
}
(project / "testing/romance-revision/package-verification.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
