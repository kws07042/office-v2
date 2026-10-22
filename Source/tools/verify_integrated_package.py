from pathlib import Path
import hashlib
import json
import shutil
import zipfile

P = Path(__file__).resolve().parents[1]
S = P.parent
D = Path('C:/Users/user/Desktop/건/오피스 V2')
proof = P / 'testing/integrated-review-v1'
version = '0.28.0-integrated-review'
name = 'afterwork_script_prototype-' + version + '-win'
package = S / 'afterwork-windows-builds' / (name + '.zip')
dest = S / 'afterwork-windows-builds/playable-integrated-final'
native = S / 'afterwork-windows-builds/native-integrated-final'
assert not dest.exists() and not native.exists(), 'Use fresh verification destinations'
changes = json.loads((proof / 'edits.json').read_text(encoding='utf-8'))
changed_runtime = {n.replace('.rpy', '.rpyc') for n in changes}
hashes = {}
with zipfile.ZipFile(package) as archive:
    assert archive.testzip() is None
    for member in archive.namelist():
        assert (dest / member).resolve().is_relative_to(dest.resolve()), member
        assert not (member.startswith(name + '/game/') and member.endswith(('.rpy', '_tests.rpyc', 'testcases.rpyc', 'three_choice_cases.json'))), member
        assert not member.startswith(tuple(name + '/' + folder + '/' for folder in ('game/saves', 'testing', 'tests', 'tools', 'review-output', 'opening-traces', 'story'))), member
        prefix = name + '/game/'
        if member.startswith(prefix) and not member.endswith('/'):
            rel = member[len(prefix):]
            if rel.startswith('cache/') or rel == 'script_version.txt':
                continue
            data = archive.read(member)
            assert data == (P / 'game' / rel).read_bytes(), rel
            hashes[rel] = hashlib.sha256(data).hexdigest()
    assert changed_runtime <= set(hashes)
    archive.extractall(dest)
clean = dest / name
shutil.copytree(clean, native)
mixed = {}
for rel in hashes:
    installed = D / 'game' / rel
    if rel not in changed_runtime and rel.endswith('.rpyc') and installed.exists():
        shutil.copy2(installed, native / 'game' / rel)
        mixed[rel] = hashlib.sha256(installed.read_bytes()).hexdigest()
for file in (P / 'game').glob('*_tests.rpy'):
    shutil.copy2(file, native / 'game' / file.name)
    shutil.copy2(file.with_suffix('.rpyc'), native / 'game' / file.with_suffix('.rpyc').name)
for filename in ('testcases.rpy', 'testcases.rpyc', 'three_choice_cases.json'):
    shutil.copy2(P / 'game' / filename, native / 'game' / filename)
previous = json.loads((P / 'testing/romance-focus-v1/package-verification.json').read_text(encoding='utf-8'))
assert all(hashes[n] == previous['game_file_hashes'][n] for n in hashes if n.startswith(('images/', 'fonts/')))
report = {'version': version, 'crc': 'passed', 'zip_sha256': hashlib.sha256(package.read_bytes()).hexdigest(), 'zip_bytes': package.stat().st_size, 'game_file_hashes': hashes, 'clean_release': str(clean), 'validation': str(native), 'installed_unchanged_modules': mixed, 'images_fonts_unchanged': True, 'source_tests_saves_excluded': True}
(proof / 'package-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'files': len(hashes), 'validation': str(native), 'installed_modules_retained_for_tests': len(mixed)}, ensure_ascii=False))
