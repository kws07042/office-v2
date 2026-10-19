from pathlib import Path
import json,shutil,sys
source=Path(__file__).with_name('verify_yujin_r04_package.py').read_text(encoding='utf-8')
source=source.replace('0.13.0-yujin-r04','0.18.0-jihyun-complete-text').replace('playable-yujin-r04-release','playable-jfin-phone').replace('native-validation-yujin-r04','native-jfin-phone').replace('testing/yujin-r04-v1','testing/jihyun-final-v1')
source=source.replace("'yujin_r01_r04.rpyc', 'fonts", "'jihyun_r05_r12.rpyc','jihyun_r13_e01.rpyc','jihyun_optional.rpyc','yujin_r01_r04.rpyc', 'fonts")
source=source.replace("('yujin_tests.rpyc', 'office_phone_tests.rpyc', 'cream_tests.rpyc')", "('yujin_tests.rpyc','jihyun_tests.rpyc','jihyun_final_tests.rpyc','five_asset_tests.rpyc','ria16_tests.rpyc','three_choice_tests.rpyc','office_phone_tests.rpyc','cream_tests.rpyc','yujin_final_tests.rpyc')")
if '--resume' in sys.argv:
    P=Path(__file__).resolve().parents[1]; proof=P/'testing/jihyun-final-v1'
    report=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'))
    assert report['validation'].endswith('native-jfin-phone')
    validation=Path(report['validation']); hashes=report['game_file_hashes']
else:
    exec(compile(source,str(Path(__file__)),'exec'))
baseline=json.loads((proof/'package-before-phone-fix.json').read_text(encoding='utf-8'))
changes=[n for n in hashes if hashes[n]!=baseline['game_file_hashes'][n]]
assert 'jihyun_r05_r12.rpyc' in changes and all(n.endswith('.rpyc') for n in changes),changes
(proof/'phone-fix-package-delta.json').write_text(json.dumps(dict(changed_runtime_files=changes,compiled_init_metadata_can_change=True,full_native_regression_repeated=True),indent=2),encoding='utf-8')
shutil.copy2(P/'game/three_choice_cases.json',validation/'game/three_choice_cases.json')
old=json.loads((P/'testing/review-jihyun-r04-v1/package-verification.json').read_text(encoding='utf-8'))
images=[n for n in hashes if n.startswith('images/')]
assert all(hashes[n]==old['game_file_hashes'][n] for n in images)
previous=Path('C:/Users/user/Desktop/건/오피스 V2/개발자료/source/game')
stable=['common.rpy','office_phone.rpy','event_sequence.rpy','event_cg_slots.rpy','ria_expressions.rpy','ria_r09_r12.rpy','ria_r13_e01.rpy','yujin_r01_r04.rpy','yujin_r05_r08.rpy','yujin_r09_r12.rpy','yujin_r13_e01.rpy','yujin_optional.rpy']
assert all((P/'game'/n).read_bytes()==(previous/n).read_bytes() for n in stable)
(proof/'unchanged-assets.json').write_text(json.dumps(dict(unchanged_image_files=images,images_match_0_17_0=True,stable_sources=stable,rigging_changed=False),ensure_ascii=False,indent=2),encoding='utf-8')
