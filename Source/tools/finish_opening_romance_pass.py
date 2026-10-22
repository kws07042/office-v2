from pathlib import Path
import json, re, hashlib, shutil, difflib

P=Path(__file__).resolve().parents[1];q=P/'testing/opening-romance-pass-v1'
c=json.loads((q/'contract.json').read_text(encoding='utf-8'));N=Path(c['native'])
D=Path('C:/Users/user/Desktop/건/오피스 V2')
H=P.parent/'afterwork-opening-romance-pass-handoff-v1'
for rel in ['source/game','runtime','docs','validation']:(H/rel).mkdir(parents=True,exist_ok=True)
stats=[]
for suite in ['opening_review','integrated_story_checks']:
    t=(q/('final-'+suite+'.log')).read_text(encoding='utf-8-sig');assert '[rpytest] Status: PASSED' in t,suite
    stats.append(dict(suite=suite,cases=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),assertions=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])))
def digest(f):return hashlib.sha256(f.read_bytes()).hexdigest()
for name,h in c['runtime_sha256'].items():assert digest(N/'game'/name)==h,name
trace_dir=H/'validation/traces';trace_dir.mkdir(parents=True,exist_ok=True)
all_rows=[]
for who in ['ria','jihyun','yujin','seoyun']:
    for variant in range(3):
        f=N/'opening-traces'/f'{who}-{variant}.json'
        trace=json.loads(f.read_text(encoding='utf-8'))
        assert trace['route']==who and trace['variant']==variant and trace['dating']
        all_rows.extend(trace['rows']);shutil.copy2(f,trace_dir/f.name)
assert any('의견 내자마자 쫓겨나는 줄' in r['text'] for r in all_rows)
assert any('입에 거품 묻은 것도 모르고' in r['text'] for r in all_rows)
assert any('내 국수가 이겼지?' in r['text'] or '제 국수가 이겼죠?' in r['text'] for r in all_rows)
edits=json.loads((q/'edits.json').read_text(encoding='utf-8'))
for name in c['changed']:
    old=(q/(name+'.before')).read_text(encoding='utf-8-sig');new=(P/'game'/name).read_text(encoding='utf-8-sig')
    (q/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=name+' 0.31',tofile=name+' 0.32')),encoding='utf-8')
    shutil.copy2(P/'game'/name,H/'source/game'/name)
    runtime=name.replace('.rpy','.rpyc');shutil.copy2(N/'game'/runtime,H/'runtime'/runtime)
v={'version':c['version'],'native_status':'passed','native_cases':sum(s['cases'] for s in stats),'native_assertions':sum(s['assertions'] for s in stats),'suites':stats,'state_and_choice_flow_unchanged':True,'human_fun_measured':False}
(q/'validation.json').write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')

report=(P/'story/opening_romance_review_v1.md').read_text(encoding='utf-8')
(H/'docs/초반연애_흐름편집_보고서_v1.md').write_text(report,encoding='utf-8')
(P/'story/opening_romance_review_v1.md').write_text(report,encoding='utf-8')

groups={'공통':['common.rpy','core.rpy'],'강리아':['ria_r01.rpy','ria_r02_r04.rpy','ria_r05_r08.rpy','ria_r09_r12.rpy','ria_r13_e01.rpy'],'백지현':['jihyun_r01_r04.rpy','jihyun_r05_r12.rpy','jihyun_r13_e01.rpy','jihyun_optional.rpy'],'차유진':['yujin_r01_r04.rpy','yujin_r05_r08.rpy','yujin_r09_r12.rpy','yujin_r13_e01.rpy','yujin_optional.rpy'],'한서윤':['seoyun_r01_r04.rpy','seoyun_r05_r12.rpy','seoyun_r13_e01.rpy','seoyun_optional.rpy']}
prefix='''> 현행 갱신: 기획 v3.06 / Windows 0.33.0-opening-romance — 2026-10-21
> 공통의 반복 업무 문답을 압축하고 첫인상·선택 뒤 활동·고백의 감정 연결을 다듬었다. 초반연애_흐름편집_보고서_v1.md와 현행 실행 대본을 우선한다. 사건·선택 기억·인물 설정·자산 계획은 유지한다. 아래 이전 갱신은 이력이다.

'''
# Synchronize current script documents, leaving prior delivery folders and historical reports alone.
for f in (D/'개발자료/docs').glob('*.md'):
    if not any(s in f.name for s in ['현행대본','연결대본','초반대본과호감도']):continue
    old=f.read_text(encoding='utf-8-sig');t=old
    for e in edits:t=t.replace(e['old'],e['new'])
    if t!=old:(H/'docs'/f.name).write_text(prefix+t,encoding='utf-8')
for who,names in groups.items():
    t=f'# {who} 현행 대본 — {c["version"]}\n\n2026-10-21. 실행 소스에서 추출. 배타적인 선택은 별도 경로다.\n'
    for name in names:t+='\n## '+name+'\n\n```renpy\n'+(P/'game'/name).read_text(encoding='utf-8-sig')+'\n```\n'
    if who=='강리아':t+='\n## 메신저 대화\n\n```renpy\nlabel ria_r08_phone_conversation:'+(P/'game/office_phone.rpy').read_text(encoding='utf-8-sig').split('label ria_r08_phone_conversation:',1)[1]+'\n```\n'
    (H/'docs'/(who+'_검수후_현행대본.md')).write_text(t,encoding='utf-8')
for name in ['퇴근 후 우리_v2_통합 기획서.md','퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md','기획_질문및결정대장.md']:
    t=(D/'개발자료/docs'/name).read_text(encoding='utf-8-sig')
    rule='''## 현행 초반 편집 규칙 — 2026-10-21

업무 설명은 인물의 태도를 보여 주는 데 필요한 만큼 남긴다. 식사·작은 내기처럼 예고한 행동은 선택 뒤 실제로 보여 준다. 고백은 해당 경로에서 함께 겪은 일에 근거를 둔다. 없는 기억을 덧붙이지 않으며 세 선택의 행동 차이와 동의·거절은 보존한다.

'''
    (H/'docs'/name).write_text(prefix+rule+t,encoding='utf-8')
validation=f'# 초반 연애 흐름 편집 실행 검증\n\n{v["version"]}. 구문 검사 통과. Windows {v["native_cases"]}사례 / {v["native_assertions"]}확인 통과.\n\n| 검사 | 사례 | 확인 |\n|---|---:|---:|\n'
for s in stats:validation+=f'| {s["suite"]} | {s["cases"]} | {s["assertions"]} |\n'
validation+='\n대본의 조건·호출·기억·보상·메뉴 수는 수정 전후 동일함을 비교했다. 이벤트 JSON은 수정하지 않았다. 마지막으로 정리한 공통 C03 응수 두 문장은 최종 초반 검사로 재확인했다. 자동 검사와 편집자의 문장 판단은 별개이며, 전수 조합 검증이나 독자 재미 측정은 아니다.\n'
(H/'docs/초반연애_실행검증_v1.md').write_text(validation,encoding='utf-8')
(H/'시작안내.txt').write_text('퇴근 후, 우리 — 대본 시험판 '+c['version']+'\n\nafterwork_script_prototype.exe로 실행합니다.\n초반의 업무 반복을 줄이고 데이트 선택과 고백의 감정 연결을 다듬었습니다.\n실행 중인 게임은 종료 후 다시 실행해 주세요.\n상세: 개발자료/docs/초반연애_흐름편집_보고서_v1.md\n',encoding='utf-8')
for f in q.iterdir():
    if f.is_file():shutil.copy2(f,H/'validation'/f.name)
installer=(P/'tools/install_relationship_secrets.py').read_text(encoding='utf-8')
installer=installer.replace('afterwork-relationship-secrets-handoff-v1','afterwork-opening-romance-pass-handoff-v1').replace('testing/relationship-secrets-v1','testing/opening-romance-pass-v1').replace("v['native_cases']==104",f"v['native_cases']=={v['native_cases']}").replace('이전버전_0.30.0_관계반전편집전','이전버전_0.32.0_초반연애편집전').replace('개발자료/관계반전반영_v1','개발자료/초반연애편집_v1').replace('관계반전_업데이트확인.json','초반연애_업데이트확인.json')
(P/'tools/install_opening_romance_pass.py').write_text(installer,encoding='utf-8')
print(json.dumps(v,ensure_ascii=False))
