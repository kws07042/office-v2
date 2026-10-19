from pathlib import Path
import json, hashlib
source=Path(__file__).with_name('verify_yujin_r04_package.py').read_text(encoding='utf-8')
source=source.replace('0.13.0-yujin-r04','0.15.0-yujin-r12').replace('yujin-r04','yujin-r12')
source=source.replace("'yujin_r01_r04.rpyc', 'fonts", "'yujin_r01_r04.rpyc', 'yujin_r09_r12.rpyc', 'images/characters/yujin/ui_temp_v001.png', 'fonts")
source=source.replace("('yujin_tests.rpyc', 'office_phone_tests.rpyc', 'cream_tests.rpyc')", "('yujin_tests.rpyc', 'yujin12_tests.rpyc', 'cream_tests.rpyc')")
P=Path(__file__).resolve().parents[1]
proof=P/'testing/yujin-r12-v1'
if not (proof/'package-verification.json').exists():
    exec(compile(source,str(Path(__file__)),'exec'))
else:
    hashes=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'))['game_file_hashes']
old=json.loads((P/'testing/yujin-r08-v1/package-verification.json').read_text(encoding='utf-8'))
stable=[name for name in hashes if name.startswith('images/') or (name.startswith('ria_') and name!='ria_expressions.rpyc')]
assert all(hashes[name]==old['game_file_hashes'][name] for name in stable)
source_stable=['cream_ui.rpy','event_cg_slots.rpy','event_sequence.rpy','office_phone.rpy','ria_expressions.rpy']
installed=Path('C:/Users/user/Desktop/건/오피스 V2/개발자료/source/game')
assert all((P/'game'/name).read_bytes()==(installed/name).read_bytes() for name in source_stable)
(proof/'unchanged-assets-and-ria.json').write_text(json.dumps({'unchanged_files':stable,'all_listed_hashes_match_0_14_0':True,'other_unchanged_source_files':source_stable,'source_matches_installed_previous_version':True,'compiled_python_blocks': 'Some bytecode hashes changed upon compilation although sources are identical. These unchanged modules are excluded from the desktop update.'},ensure_ascii=False,indent=2),encoding='utf-8')
