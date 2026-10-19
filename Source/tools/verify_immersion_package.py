from pathlib import Path
import json,shutil
source=Path(__file__).with_name('verify_yujin_r04_package.py').read_text(encoding='utf-8')
source=source.replace('0.13.0-yujin-r04','0.21.0-immersive-dialogue').replace('playable-yujin-r04-release','playable-immers').replace('native-validation-yujin-r04','native-immers').replace('testing/yujin-r04-v1','testing/immersion-v1')
source=source.replace("('yujin_tests.rpyc', 'office_phone_tests.rpyc', 'cream_tests.rpyc')", "('full_editorial_tests.rpyc','review_continuity_tests.rpyc','testcases.rpyc','ria16_tests.rpyc','three_choice_tests.rpyc','yujin_tests.rpyc','yujin08_tests.rpyc','yujin12_tests.rpyc','yujin_final_tests.rpyc','jihyun_tests.rpyc','jihyun_final_tests.rpyc','seoyun_tests.rpyc','office_phone_tests.rpyc')")
exec(compile(source,str(Path(__file__)),'exec'))
shutil.copy2(P/'game/three_choice_cases.json',validation/'game/three_choice_cases.json')
old=json.loads((P/'testing/romance-lines-v1/package-verification.json').read_text(encoding='utf-8'))
images=[n for n in hashes if n.startswith('images/')]
assert all(hashes[n]==old['game_file_hashes'][n] for n in images)
(proof/'unchanged-assets.json').write_text(json.dumps(dict(images_unchanged=True,image_files=images,rigging_changed=False),ensure_ascii=False,indent=2),encoding='utf-8')
