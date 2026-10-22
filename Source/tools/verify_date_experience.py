from pathlib import Path
import shutil,json,zipfile
source=Path(__file__).with_name('verify_yujin_r04_package.py').read_text(encoding='utf-8')
for a,b in [('0.13.0-yujin-r04','0.24.0-date-experience'),('playable-yujin-r04-release','playable-date-experience'),('native-validation-yujin-r04','native-date-experience'),('testing/yujin-r04-v1','testing/date-experience-v1')]:source=source.replace(a,b)
exec(compile(source,str(Path(__file__)),'exec'))
for f in (P/'game').glob('*_tests.rpy'):
 shutil.copy2(f,validation/'game'/f.name);shutil.copy2(f.with_suffix('.rpyc'),validation/'game'/f.with_suffix('.rpyc').name)
for name in ('testcases.rpy','testcases.rpyc','three_choice_cases.json'):shutil.copy2(P/'game'/name,validation/'game'/name)
with zipfile.ZipFile(package) as z:assert not any('/opening-traces/' in n for n in z.namelist())
old=json.loads((P/'testing/balance-v1/package-verification.json').read_text(encoding='utf-8'))
assert all(hashes[n]==old['game_file_hashes'][n] for n in hashes if n.startswith('images/'))
(proof/'unchanged-assets.json').write_text(json.dumps({'images_unchanged':True,'compared_to':'0.23.0-route-balance','rigging_changed':False},indent=2),encoding='utf-8')
print('Production excludes tests/saves/trace logs; art unchanged.')
