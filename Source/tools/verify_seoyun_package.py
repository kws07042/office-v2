from pathlib import Path
import json,shutil
source=Path(__file__).with_name('verify_yujin_r04_package.py').read_text(encoding='utf-8')
source=source.replace('0.13.0-yujin-r04','0.19.0-all-routes-text').replace('playable-yujin-r04-release','playable-sfin').replace('native-validation-yujin-r04','native-sfin').replace('testing/yujin-r04-v1','testing/seoyun-final-v1')
source=source.replace("'yujin_r01_r04.rpyc', 'fonts", "'seoyun_r01_r04.rpyc','seoyun_r05_r12.rpyc','seoyun_r13_e01.rpyc','seoyun_optional.rpyc','yujin_r01_r04.rpyc', 'fonts")
source=source.replace("('yujin_tests.rpyc', 'office_phone_tests.rpyc', 'cream_tests.rpyc')", "('seoyun_tests.rpyc','five_asset_tests.rpyc','yujin_tests.rpyc','jihyun_tests.rpyc','office_phone_tests.rpyc','cream_tests.rpyc','ria16_tests.rpyc','three_choice_tests.rpyc')")
exec(compile(source,str(Path(__file__)),'exec'))
shutil.copy2(P/'game/three_choice_cases.json',validation/'game/three_choice_cases.json')
old=json.loads((P/'testing/jihyun-final-v1/package-verification.json').read_text(encoding='utf-8'))
images=[n for n in hashes if n.startswith('images/')]
assert all(hashes[n]==old['game_file_hashes'][n] for n in images)
previous=Path('C:/Users/user/Desktop/건/오피스 V2/개발자료/source/game')
stable=['common.rpy','office_phone.rpy','event_sequence.rpy','event_cg_slots.rpy','ria_expressions.rpy','ria_r09_r12.rpy','ria_r13_e01.rpy','yujin_r01_r04.rpy','yujin_r05_r08.rpy','yujin_r09_r12.rpy','yujin_r13_e01.rpy','yujin_optional.rpy','jihyun_r01_r04.rpy','jihyun_r05_r12.rpy','jihyun_r13_e01.rpy','jihyun_optional.rpy']
assert all((P/'game'/n).read_bytes()==(previous/n).read_bytes() for n in stable)
(proof/'unchanged-assets.json').write_text(json.dumps(dict(unchanged_image_files=images,images_match_0_18_0=True,stable_sources=stable,rigging_changed=False),ensure_ascii=False,indent=2),encoding='utf-8')
