from pathlib import Path
import json,shutil
source=Path(__file__).with_name('verify_immersion_package.py').read_text(encoding='utf-8')
source=source.replace('0.21.0-immersive-dialogue','0.22.0-opening-review').replace('playable-immers','playable-opening-final-v2').replace('native-immers','native-opening-final-v2').replace('testing/immersion-v1','testing/opening-v1').replace('testing/romance-lines-v1','testing/immersion-v1')
exec(compile(source,str(Path(__file__)),'exec'))
for f in (P/'game').glob('*_tests.rpy'):
 shutil.copy2(f,validation/'game'/f.name)
 shutil.copy2(f.with_suffix('.rpyc'),validation/'game'/f.with_suffix('.rpyc').name)
shutil.copy2(P/'game/testcases.rpy',validation/'game/testcases.rpy')
shutil.copy2(P/'game/testcases.rpyc',validation/'game/testcases.rpyc')
import zipfile
with zipfile.ZipFile(package) as z:
 assert not any('/opening-traces/' in n for n in z.namelist())
print('Final package excludes trace logs. Run final-package tests in this validation copy.')
