from pathlib import Path
import shutil,json,hashlib
base=Path(__file__).with_name('verify_yujin_r04_package.py').read_text(encoding='utf-8')
base=base.replace('0.13.0-yujin-r04','0.20.0-dialogue-review').replace('playable-yujin-r04-release','playable-edit').replace('native-validation-yujin-r04','native-edit').replace('testing/yujin-r04-v1','testing/full-editorial-v1')
base=base.replace("('yujin_tests.rpyc', 'office_phone_tests.rpyc', 'cream_tests.rpyc')", "('full_editorial_tests.rpyc','testcases.rpyc','ria16_tests.rpyc','three_choice_tests.rpyc','yujin_tests.rpyc','yujin08_tests.rpyc','yujin12_tests.rpyc','yujin_final_tests.rpyc','jihyun_tests.rpyc','jihyun_final_tests.rpyc','seoyun_tests.rpyc','five_asset_tests.rpyc','office_phone_tests.rpyc','cream_tests.rpyc')")
exec(compile(base,str(Path(__file__)),'exec'))
shutil.copy2(P/'game/three_choice_cases.json',validation/'game/three_choice_cases.json')
previous=json.loads((P/'testing/seoyun-final-v1/package-verification.json').read_text(encoding='utf-8'))
images=[n for n in hashes if n.startswith('images/')]
assert all(hashes[n]==previous['game_file_hashes'][n] for n in images)
(proof/'unchanged-assets.json').write_text(json.dumps(dict(images_unchanged=True,image_files=images,rigging_changed=False),ensure_ascii=False,indent=2),encoding='utf-8')
