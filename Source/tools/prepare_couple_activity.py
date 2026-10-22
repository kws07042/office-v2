from pathlib import Path
import difflib
import hashlib
import json
import re
import shutil

P = Path(__file__).resolve().parents[1]
S = P.parent
D = Path('C:/Users/user/Desktop/건/오피스 V2')
proof = P/'testing/couple-activity-v1'
native = S/'afterwork-windows-builds/native-couple-activity-v1'
assert not native.exists(), 'Use a new diagnostic directory'
old = S/'afterwork-windows-builds/native-integrated-final'
shutil.copytree(old, native, ignore=shutil.ignore_patterns('game', 'review-output', 'tests', 'log.txt'))
shutil.copytree(D/'game', native/'game', ignore=shutil.ignore_patterns('saves', 'cache', 'script_version.txt'))
contract = json.loads((proof/'contract.json').read_text(encoding='utf-8'))
for n in contract['changed']:
    old_text = (proof/(n+'.before')).read_text(encoding='utf-8')
    new = (P/'game'/n).read_text(encoding='utf-8')
    (proof/(n+'.diff')).write_text(''.join(difflib.unified_diff(old_text.splitlines(True),new.splitlines(True),fromfile=n+' 0.28',tofile=n+' 0.29')),encoding='utf-8')
    assert [l.strip() for l in old_text.splitlines() if l.strip().startswith(('$ remember(', '$ award_once(', 'call ', 'if ', 'elif ', 'else:', 'label ', 'return'))] == [l.strip() for l in new.splitlines() if l.strip().startswith(('$ remember(', '$ award_once(', 'call ', 'if ', 'elif ', 'else:', 'label ', 'return'))],n
    shutil.copy2((P/'game'/n).with_suffix('.rpyc'),(native/'game'/n).with_suffix('.rpyc'))
for f in (P/'game').glob('*_tests.rpy'):
    shutil.copy2(f,native/'game'/f.name)
    shutil.copy2(f.with_suffix('.rpyc'),native/'game'/f.with_suffix('.rpyc').name)
for n in ('testcases.rpy','testcases.rpyc','three_choice_cases.json'):
    shutil.copy2(P/'game'/n,native/'game'/n)
contract['native'] = str(native)
contract['runtime_sha256'] = {f.name:hashlib.sha256(f.read_bytes()).hexdigest() for f in (native/'game').iterdir() if f.suffix in ('.rpyc','.json') and not f.name.endswith('_tests.rpyc') and f.name not in ('testcases.rpyc','three_choice_cases.json')}
contract['source_sha256'] = {n:hashlib.sha256((P/'game'/n).read_bytes()).hexdigest() for n in contract['changed']}
(proof/'contract.json').write_text(json.dumps(contract,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'native':str(native),'changed_runtime':len(contract['changed']),'state_contract':'unchanged'},ensure_ascii=False))
