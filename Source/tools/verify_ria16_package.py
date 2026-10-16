"""Verify this local release and extract to a new, private validation folder."""
from pathlib import Path
import hashlib
import json
import zipfile

project = Path(__file__).resolve().parents[1]
builds = project.parent / 'afterwork-windows-builds'
release = 'afterwork_script_prototype-0.5.0-ria-route-win'
package = builds / (release + '.zip')
destination = builds / 'playable-ria16-release'
assert not destination.exists(), 'Use a fresh extraction folder.'
with zipfile.ZipFile(package) as archive:
    assert archive.testzip() is None
    names = archive.namelist()
    assert not any('/game/' in n and n.endswith('.rpy') for n in names)
    assert not any(n.endswith(('testcases.rpyc', '_tests.rpyc', '-success.json')) for n in names)
    assert not any(n.startswith(tuple(release + '/' + d for d in ('game/saves/', 'testing/', 'tests/'))) for n in names)
    compiled = {}
    for filename in ('common.rpyc', 'ria_r01.rpyc', 'ria_r02_r04.rpyc', 'ria_r05_r08.rpyc', 'ria_r09_r12.rpyc', 'ria_r13_e01.rpyc', 'core.rpyc', 'screens.rpyc', 'options.rpyc'):
        data = archive.read(release + '/game/' + filename)
        assert data == (project / 'game' / filename).read_bytes(), filename
        compiled[filename] = hashlib.sha256(data).hexdigest()
    assert release + '/afterwork_script_prototype.exe' in names
    for name in names:
        assert (destination / name).resolve().is_relative_to(destination.resolve()), name
    archive.extractall(destination)
result = {
    'release': release,
    'zip_bytes': package.stat().st_size,
    'zip_sha256': hashlib.sha256(package.read_bytes()).hexdigest(),
    'archive_crc': 'passed',
    'tested_source_byte_match': compiled,
    'testcases_and_saves_excluded': True,
}
(project / 'testing/ria16/package-verification.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps(result, indent=2))
