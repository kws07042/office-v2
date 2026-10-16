from pathlib import Path
import hashlib, json, shutil, zipfile

P = Path(__file__).resolve().parents[1]
B = P.parent / 'afterwork-windows-builds'
name = 'afterwork_script_prototype-0.11.0-office-phone-win'
package = B / (name + '.zip')
destination = B / 'playable-office-phone-release'
validation = B / 'native-validation-office-phone'
proof = P / 'testing/phone-v1'
assert not destination.exists() and not validation.exists(), 'Use a fresh verification destination'
hashes = {}
with zipfile.ZipFile(package) as z:
    assert z.testzip() is None
    names = z.namelist()
    assert not any('/game/' in n and n.endswith('.rpy') for n in names)
    assert not any(n.endswith(('_tests.rpyc', 'testcases.rpyc', 'three_choice_cases.json')) for n in names)
    assert not any(n.startswith(tuple(name + '/' + d for d in ('game/saves/', 'testing/', 'tests/', 'tools/', 'story/'))) for n in names)
    for n in names:
        assert (destination / n).resolve().is_relative_to(destination.resolve())
        prefix = name + '/game/'
        if not n.startswith(prefix) or n.endswith('/'):
            continue
        relative = n[len(prefix):]
        if relative.startswith('cache/') or relative == 'script_version.txt':
            continue
        data = z.read(n)
        assert data == (P / 'game' / relative).read_bytes(), relative
        hashes[relative] = hashlib.sha256(data).hexdigest()
    for required in ('office_phone.rpyc', 'ria_r05_r08.rpyc', 'screens.rpyc', 'options.rpyc'):
        assert required in hashes
    z.extractall(destination)
clean = destination / name
shutil.copytree(clean, validation)
for f in ('office_phone_tests.rpyc', 'cream_tests.rpyc', 'compat_tests.rpyc'):
    shutil.copy2(P / 'game' / f, validation / 'game' / f)
fixtures = proof / 'native-clear_compat_checks-saves'
fixtures.mkdir(exist_ok=True)
for suite, slot in [('cream_ui_checks', '9'), ('five_asset_checks', '8')]:
    saves = list((P / 'testing/clear-ui' / ('native-' + suite + '-saves')).glob('1-' + slot + '-*.save'))
    assert len(saves) == 1
    shutil.copy2(saves[0], fixtures / saves[0].name)
report = {'version': '0.11.0-office-phone', 'crc': 'passed', 'zip_sha256': hashlib.sha256(package.read_bytes()).hexdigest(), 'zip_bytes': package.stat().st_size, 'game_file_hashes': hashes, 'source_tests_saves_excluded': True, 'clean_release': str(clean), 'validation': str(validation)}
(proof / 'package-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'files_verified': len(hashes), 'zip_bytes': package.stat().st_size, 'clean_release': str(clean)}, ensure_ascii=False))
