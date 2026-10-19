from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]
proof=P/'testing/yujin-final-v1'
source=Path(__file__).with_name('verify_yujin_r04_package.py').read_text(encoding='utf-8')
source=source.replace('0.13.0-yujin-r04','0.16.0-yujin-complete-text').replace('yujin-r04','yujin-final')
source=source.replace("'yujin_r01_r04.rpyc', 'fonts", "'yujin_r01_r04.rpyc', 'yujin_r13_e01.rpyc', 'yujin_optional.rpyc', 'images/characters/yujin/ui_temp_v001.png', 'fonts")
source=source.replace("('yujin_tests.rpyc', 'office_phone_tests.rpyc', 'cream_tests.rpyc')", "('yujin_tests.rpyc', 'yujin_final_tests.rpyc', 'cream_tests.rpyc')")
exec(compile(source,str(Path(__file__)),'exec'))
old=json.loads((P/'testing/yujin-r12-v1/package-verification.json').read_text(encoding='utf-8'))
stable=[name for name in hashes if name.startswith('images/') or (name.startswith('ria_') and name!='ria_expressions.rpyc')]
assert all(hashes[name]==old['game_file_hashes'][name] for name in stable)
installed=Path('C:/Users/user/Desktop/건/오피스 V2/개발자료/source/game')
source_stable=['cream_ui.rpy','office_phone.rpy','event_sequence.rpy','event_cg_slots.rpy','ria_expressions.rpy','yujin_r05_r08.rpy','yujin_r09_r12.rpy']
assert all((P/'game'/name).read_bytes()==(installed/name).read_bytes() for name in source_stable)
(proof/'unchanged-assets-and-ria.json').write_text(json.dumps({'unchanged_image_and_ria_module_files':stable,'all_listed_hashes_match_0_15_0':True,'unchanged_sources_matching_previous_installed_version':source_stable,'unmodified_modules_excluded_from_desktop_update':True},ensure_ascii=False,indent=2),encoding='utf-8')
