from pathlib import Path
import hashlib, json, shutil, zipfile

P = Path(__file__).resolve().parents[1]
B = P.parent / 'afterwork-windows-builds'
release = 'afterwork_script_prototype-0.10.0-ria-expressions-win'
package = B / (release + '.zip')
destination = B / 'playable-ria-expressions-release'
validation = B / 'native-validation-ria-expressions'
assert not destination.exists() and not validation.exists()
with zipfile.ZipFile(package) as z:
    assert z.testzip() is None
    names = z.namelist()
    assert not any('/game/' in n and n.endswith('.rpy') for n in names)
    assert not any(n.endswith(('testcases.rpyc', '_tests.rpyc', 'three_choice_cases.json', '-success.json')) for n in names)
    assert not any(n.startswith(tuple(release+'/'+d for d in ('game/saves/', 'testing/', 'tests/', 'tools/', 'story/'))) for n in names)
    assert release+'/game/images/characters/ria/ui_master.png' not in names
    assert release+'/game/images/characters/ria/expressions/face_reference.png' not in names
    hashes, generated = {}, {}
    for name in names:
        prefix = release+'/game/'
        if not name.startswith(prefix) or name.endswith('/'):
            continue
        relative, data = name[len(prefix):], z.read(name)
        if relative.startswith('cache/') or relative == 'script_version.txt':
            generated[relative] = hashlib.sha256(data).hexdigest()
            continue
        assert (P/'game'/relative).read_bytes() == data, relative
        hashes[relative] = hashlib.sha256(data).hexdigest()
    assert 'ria_expressions.rpyc' in hashes
    canonical = P.parent/'character-art-kit-v1/assets/ria/master/ria_master_v001.png'
    master_hash = hashlib.sha256(canonical.read_bytes()).hexdigest()
    assert hashes['images/characters/ria/ui_master_v2.png'] == master_hash
    for mood in ('smile', 'shy', 'serious'):
        assert 'images/characters/ria/expressions/'+mood+'.png' in hashes
    for filename in ('README.md', 'WINDOWS-README.txt'):
        assert z.read(release+'/'+filename) == (P/filename).read_bytes()
    for name in names:
        assert (destination/name).resolve().is_relative_to(destination.resolve())
    z.extractall(destination)
clean = destination/release
shutil.copytree(clean, validation)
for name in ('ria_expression_tests.rpyc', 'cream_tests.rpyc', 'compat_tests.rpyc', 'three_choice_tests.rpyc', 'five_asset_tests.rpyc', 'ria16_tests.rpyc', 'three_choice_cases.json'):
    shutil.copy2(P/'game'/name, validation/'game'/name)
proof = P/'testing/ria-expressions'
fixture_dest = proof/'native-clear_compat_checks-saves'
fixture_dest.mkdir(exist_ok=True)
for suite, slot in [('cream_ui_checks', '9'), ('five_asset_checks', '8')]:
    sources = list((P/'testing/clear-ui'/('native-'+suite+'-saves')).glob('1-'+slot+'-*.save'))
    assert len(sources) == 1
    shutil.copy2(sources[0], fixture_dest/sources[0].name)
report = {'runtime_version':'0.10.0-ria-expressions', 'planning_revision':'2.80',
          'zip_bytes':package.stat().st_size, 'zip_sha256':hashlib.sha256(package.read_bytes()).hexdigest(),
          'crc':'passed', 'current_game_file_hashes':hashes, 'engine_generated_files':generated,
          'master_byte_identical':True, 'master_sha256':master_hash,
          'old_master_and_source_reference_excluded':True, 'source_tests_saves_excluded':True,
          'clean_release':str(clean), 'validation':str(validation)}
(proof/'package-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'files_verified':len(hashes), 'clean_release':str(clean), 'zip_bytes':report['zip_bytes']}, ensure_ascii=False))
