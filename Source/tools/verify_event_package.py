"""Verify the current local Windows package, then extract to a fresh folder."""
from pathlib import Path
import hashlib, json, shutil, zipfile

P=Path(__file__).resolve().parents[1]
B=P.parent/'afterwork-windows-builds'
release='afterwork_script_prototype-0.8.0-three-choices-win'
package=B/(release+'.zip')
destination=B/'playable-three-choices-release'
validation=B/'native-validation-three-choices'
assert not destination.exists() and not validation.exists(), 'Use fresh extraction and validation folders.'
with zipfile.ZipFile(package) as z:
    assert z.testzip() is None
    names=z.namelist()
    assert not any('/game/' in n and n.endswith('.rpy') for n in names)
    assert not any(n.endswith(('testcases.rpyc','_tests.rpyc','-success.json')) for n in names)
    assert not any(n.startswith(tuple(release+'/'+d for d in ('game/saves/','testing/','tests/','tools/','story/'))) for n in names)
    hashes={}
    for filename in ('common.rpyc','ria_r01.rpyc','ria_r02_r04.rpyc','ria_r05_r08.rpyc','ria_r09_r12.rpyc','ria_r13_e01.rpyc','core.rpyc','screens.rpyc','options.rpyc','event_sequence.rpyc','event_assets.json','event_story.json','event_cg_slots.rpyc','event_cg_plan.json'):
        data=z.read(release+'/game/'+filename)
        assert data==(P/'game'/filename).read_bytes(),filename
        hashes[filename]=hashlib.sha256(data).hexdigest()
    for filename in ('README.md','WINDOWS-README.txt'):
        assert z.read(release+'/'+filename)==(P/filename).read_bytes(),filename
    assert release+'/afterwork_script_prototype.exe' in names
    plan=json.loads(z.read(release+'/game/event_cg_plan.json'))
    assert all(release+'/game/'+a['planned_path'] not in names for s in plan['sets'] for a in s['base_cg']+[s['intro_cg'],s['intro_expression']])
    assert release+'/game/three_choice_cases.json' not in names
    for name in names:assert (destination/name).resolve().is_relative_to(destination.resolve())
    z.extractall(destination)
clean=destination/release
shutil.copytree(clean,validation)
for name in ('ria16_tests.rpyc','three_choice_tests.rpyc','five_asset_tests.rpyc','three_choice_cases.json'):
    shutil.copy2(P/'game'/name,validation/'game'/name)
report={'version':'0.8.0-three-choices','zip_bytes':package.stat().st_size,'zip_sha256':hashlib.sha256(package.read_bytes()).hexdigest(),'crc':'passed','current_game_file_hashes':hashes,'source_tests_saves_excluded':True,'production_art_absent':True,'clean_release':str(clean),'validation':str(validation)}
(P/'testing/revision08/package-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
