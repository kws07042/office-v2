from pathlib import Path
import json,re,hashlib,shutil,runpy

P=Path(__file__).resolve().parents[1]; proof=P/'testing/immersion-v1'
proof.mkdir(parents=True,exist_ok=True)
assert not (proof/'changes.json').exists(), 'Already applied'
sources={p.name:p.read_text(encoding='utf-8') for p in (P/'game').glob('*.rpy') if '_tests' not in p.name and p.name!='testcases.rpy'}
original=dict(sources); edits=[]
def q(label,old,new):
    name=next(n for n,t in sources.items() if re.search(r'^label '+re.escape(label)+r'(?:\(|:)',t,re.M))
    t=sources[name]; start=re.search(r'^label '+re.escape(label)+r'(?:\(|:)',t,re.M).start(); end=t.find('\nlabel ',start+1); end=len(t) if end<0 else end
    body=t[start:end]; assert body.count(old)==1,(label,old,body.count(old))
    pos=body.index(old); indent=body[body.rfind('\n',0,pos)+1:pos]; assert not indent.strip(),(label,old)
    new=new.replace('\n','\n'+indent)
    sources[name]=t[:start]+body.replace(old,new,1)+t[end:]
    edits.append(dict(file=name,label=label,before=old,after=new))
def ri(label,speaker,old_i,old_f,new_i,new_f):
    q(label,f'{speaker} "[ri(\'{old_i}\', \'{old_f}\')]"',f'{speaker} "[ri(\'{new_i}\', \'{new_f}\')]"')

for script in ('rewrite_immersion_common.py','rewrite_immersion_ria.py','rewrite_immersion_jihyun.py','rewrite_immersion_yujin.py','rewrite_immersion_seoyun.py'):
    exec(compile((P/'tools'/script).read_text(encoding='utf-8'),script,'exec'))

# Dialogue-only edits must preserve all menus, branches, flags and awards.
def structure(t):
    return [x.rstrip() for x in t.splitlines() if x.strip() and not re.match(r'^\s*(?:[a-z]+\s+)?"',x)]
for n in sources:
    assert structure(sources[n])==structure(original[n]), 'Control-flow drift: '+n
    assert re.findall(r'^\s*".*":\s*$',sources[n],re.M)==re.findall(r'^\s*".*":\s*$',original[n],re.M), 'Choice drift: '+n
sources['options.rpy']=sources['options.rpy'].replace('0.20.1-romance-lines','0.21.0-immersive-dialogue')
target=Path('C:/Users/user/Desktop/건/오피스 V2/game')
(proof/'previous-runtime-hashes.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in target.iterdir() if p.is_file()},indent=2),encoding='utf-8')
changed=[]
for n,t in sources.items():
    if t!=original[n]:
        (proof/(n+'.before')).write_text(original[n],encoding='utf-8')
        (P/'game'/n).write_text(t,encoding='utf-8'); changed.append(n)
(proof/'changes.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2),encoding='utf-8')
(proof/'changed-files.json').write_text(json.dumps(changed,indent=2),encoding='utf-8')
print(json.dumps(dict(edited_passages=len(edits),scenes=len({e['label'] for e in edits}),files=changed,control_flow_unchanged=True),ensure_ascii=False))
