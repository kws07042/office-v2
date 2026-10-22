"""Install only reviewed script modules and current documentation; preserve user art."""
from pathlib import Path
import hashlib
import json
import shutil

P=Path(__file__).resolve().parents[1]
H=P.parent/'afterwork-dialogue-style-handoff-v1'
D=Path('C:/Users/user/Desktop/건/오피스 V2').resolve(strict=True)
assert str(D)==str(Path('C:/Users/user/Desktop/건/오피스 V2'))
proof=P/'testing/dialogue-style-v1'
c=json.loads((proof/'contract.json').read_text(encoding='utf-8'))
b=json.loads((proof/'baseline.json').read_text(encoding='utf-8'))
v=json.loads((proof/'validation.json').read_text(encoding='utf-8'))
assert v['native_status']=='passed' and v['native_cases']==8
def digest(f):return hashlib.sha256(f.read_bytes()).hexdigest()
for rel,h in c['runtime_sha256'].items():
    expected=b['runtime'].get(rel,h)
    assert digest(D/'game'/rel)==expected, 'Concurrent runtime edit: '+rel
for rel,h in b['source'].items():
    assert digest(D/'개발자료/source/game'/rel)==h,'Concurrent source edit: '+rel
for f in (H/'docs').iterdir():
    if f.name in b.get('docs',{}):
        assert digest(D/'개발자료/docs'/f.name)==b['docs'][f.name], 'Concurrent document edit: '+f.name
backup=D/'개발자료/이전버전_0.34.0_대사표시변경전'
assert backup.resolve().is_relative_to(D)
assert not backup.exists(),'Backup already exists'
writes=[]
for f in (H/'runtime').iterdir():
    assert f.suffix in ('.rpyc','.json') and f.name in b['runtime']
    assert digest(f)==c['runtime_sha256'][f.name]
    writes.append((f,Path('game')/f.name))
for f in (H/'source/game').iterdir():writes.append((f,Path('개발자료/source/game')/f.name))
for f in (H/'docs').iterdir():writes.append((f,Path('개발자료/docs')/f.name))
for f in H.rglob('*'):
    if f.is_file():writes.append((f,Path('개발자료/독백이름색표시_v1')/f.relative_to(H)))
for name in ['시작안내.txt','README.md','WINDOWS-README.txt']:
    writes.append((H/'시작안내.txt',Path(name)))
assert len({str(rel) for f,rel in writes})==len(writes)
for f,rel in writes:
    assert f.is_file() and (D/rel).resolve().is_relative_to(D)
backup.mkdir(parents=True)
for f,rel in writes:
    dest=D/rel
    if dest.is_file():
        old=backup/rel
        old.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(dest,old)
    dest.parent.mkdir(parents=True,exist_ok=True)
    shutil.copy2(f,dest)
    assert digest(f)==digest(dest),str(dest)
# Recheck the installed executable composition, including unchanged modules.
for rel,h in c['runtime_sha256'].items():assert digest(D/'game'/rel)==h,rel
report={'version':v['version'],'backup':str(backup),'verified_writes':len(writes),'native_cases':v['native_cases'],'assertions':v['native_assertions'],'runtime_matches_tested':True,'images_audio_rigging_changed':False,'saves_removed':0,'github_updated':False}
for path in [proof/'desktop-installation.json',D/'독백이름색_업데이트확인.json']:
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False))
