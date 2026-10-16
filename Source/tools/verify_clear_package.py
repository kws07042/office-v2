from pathlib import Path
import hashlib,json,shutil,zipfile
P=Path(__file__).resolve().parents[1];B=P.parent/'afterwork-windows-builds'
release='afterwork_script_prototype-0.9.1-clear-ui-win'
package=B/(release+'.zip');destination=B/'playable-clear-ui-release';validation=B/'native-validation-clear-ui'
assert not destination.exists() and not validation.exists()
with zipfile.ZipFile(package) as z:
    assert z.testzip() is None
    names=z.namelist()
    assert not any('/game/' in n and n.endswith('.rpy') for n in names)
    assert not any(n.endswith(('testcases.rpyc','_tests.rpyc','three_choice_cases.json','-success.json')) for n in names)
    assert not any(n.startswith(tuple(release+'/'+d for d in ('game/saves/','testing/','tests/','tools/','story/'))) for n in names)
    hashes={}
    generated={}
    for filename in names:
        prefix=release+'/game/'
        if filename.startswith(prefix) and not filename.endswith('/'):
            relative=filename[len(prefix):]
            data=z.read(filename)
            if relative.startswith('cache/') or relative == 'script_version.txt':
                generated[relative]=hashlib.sha256(data).hexdigest()
                if relative.endswith('.json'):
                    assert isinstance(json.loads(data),dict)
                else:
                    assert data
                continue
            assert (P/'game'/relative).is_file(),relative
            assert data==(P/'game'/relative).read_bytes(),relative
            hashes[relative]=hashlib.sha256(data).hexdigest()
    assert 'cream_ui.rpyc' in hashes
    provenance=json.loads((P/'story/ria_ui_asset_provenance_v1.json').read_text(encoding='utf-8'))
    assert hashes['images/characters/ria/ui_master.png']==provenance['sha256']
    assert hashlib.sha256(Path(provenance['source']).read_bytes()).hexdigest()==provenance['sha256']
    plan=json.loads(z.read(release+'/game/event_cg_plan.json'))
    assert all(release+'/game/'+a['planned_path'] not in names for s in plan['sets'] for a in s['base_cg']+[s['intro_cg'],s['intro_expression']])
    for filename in ('README.md','WINDOWS-README.txt'):
        assert z.read(release+'/'+filename)==(P/filename).read_bytes()
    for name in names:assert (destination/name).resolve().is_relative_to(destination.resolve())
    z.extractall(destination)
clean=destination/release
shutil.copytree(clean,validation)
for name in ('cream_tests.rpyc','three_choice_tests.rpyc','five_asset_tests.rpyc','ria16_tests.rpyc','compat_tests.rpyc','three_choice_cases.json'):
    shutil.copy2(P/'game'/name,validation/'game'/name)
report={'runtime_version':'0.9.1-clear-ui','planning_revision':'2.79','zip_bytes':package.stat().st_size,'zip_sha256':hashlib.sha256(package.read_bytes()).hexdigest(),'crc':'passed','current_game_file_hashes':hashes,'engine_generated_files':generated,'original_ria_unchanged':True,'new_character_generation':False,'final_event_art_absent':True,'source_tests_saves_excluded':True,'clean_release':str(clean),'validation':str(validation)}
(P/'testing/clear-ui/package-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'files_verified':len(hashes),'clean_release':str(clean),'zip_bytes':report['zip_bytes']},ensure_ascii=False))
