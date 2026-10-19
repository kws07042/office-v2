from pathlib import Path
import json,shutil
source=Path(__file__).with_name('verify_yujin_r04_package.py').read_text(encoding='utf-8')
source=source.replace('0.13.0-yujin-r04','0.17.0-review-jihyun-r04')
source=source.replace('playable-yujin-r04-release','playable-j04').replace('native-validation-yujin-r04','native-j04').replace('testing/yujin-r04-v1','testing/review-jihyun-r04-v1')
source=source.replace("'yujin_r01_r04.rpyc', 'fonts", "'yujin_r01_r04.rpyc', 'jihyun_r01_r04.rpyc', 'fonts")
source=source.replace("('yujin_tests.rpyc', 'office_phone_tests.rpyc', 'cream_tests.rpyc')", "('yujin_tests.rpyc','jihyun_tests.rpyc','review_continuity_tests.rpyc','ria16_tests.rpyc','three_choice_tests.rpyc','office_phone_tests.rpyc','cream_tests.rpyc')")
exec(compile(source,str(Path(__file__)),'exec'))
shutil.copy2(P/'game/three_choice_cases.json',validation/'game/three_choice_cases.json')
old=json.loads((P/'testing/yujin-final-v1/package-verification.json').read_text(encoding='utf-8'))
images=[name for name in hashes if name.startswith('images/')]
assert all(hashes[name]==old['game_file_hashes'][name] for name in images)
stable=['common.rpy','office_phone.rpy','event_sequence.rpy','event_cg_slots.rpy','ria_expressions.rpy','yujin_r01_r04.rpy','yujin_r05_r08.rpy','yujin_r09_r12.rpy','yujin_optional.rpy']
previous=Path('C:/Users/user/Desktop/건/오피스 V2/개발자료/source/game')
assert all((P/'game'/name).read_bytes()==(previous/name).read_bytes() for name in stable)
(proof/'unchanged-assets.json').write_text(json.dumps({'unchanged_image_files':images,'images_match_0_16_0':True,'other_sources_matching_previous_installed_version':stable,'rigging_changed':False},ensure_ascii=False,indent=2),encoding='utf-8')
