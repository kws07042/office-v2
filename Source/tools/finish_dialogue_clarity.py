from pathlib import Path
import json, re, hashlib, shutil, difflib

P=Path(__file__).resolve().parents[1];q=P/'testing/dialogue-clarity-v1'
c=json.loads((q/'contract.json').read_text(encoding='utf-8'));N=Path(c['native'])
D=Path('C:/Users/user/Desktop/건/오피스 V2')
H=P.parent/'afterwork-dialogue-clarity-handoff-v1'
for rel in ['source/game','runtime','docs','validation']:(H/rel).mkdir(parents=True,exist_ok=True)
stats=[]
for suite in ['opening_review','integrated_story_checks','five_asset_checks','marriage_disclosure_checks','review_continuity_checks','yujin_final_checks']:
    t=(q/('final-'+suite+'.log')).read_text(encoding='utf-8-sig');assert '[rpytest] Status: PASSED' in t,suite
    stats.append(dict(suite=suite,cases=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),assertions=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])))
def digest(f):return hashlib.sha256(f.read_bytes()).hexdigest()
for name,h in c['runtime_sha256'].items():assert digest(N/'game'/name)==h,name
edits=json.loads((q/'edits.json').read_text(encoding='utf-8'))
for name in c['changed']:
    old=(q/(name+'.before')).read_text(encoding='utf-8-sig');new=(P/'game'/name).read_text(encoding='utf-8-sig')
    (q/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=name+' 0.31',tofile=name+' 0.32')),encoding='utf-8')
    shutil.copy2(P/'game'/name,H/'source/game'/name)
    runtime=name.replace('.rpy','.rpyc');shutil.copy2(N/'game'/runtime,H/'runtime'/runtime)
v={'version':c['version'],'native_status':'passed','native_cases':sum(s['cases'] for s in stats),'native_assertions':sum(s['assertions'] for s in stats),'suites':stats,'state_and_choice_flow_unchanged':True,'human_fun_measured':False}
(q/'validation.json').write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')

report='''# 뜻이 바로 들어오는 대사로 — 전체 대본 검수

2026-10-21 · Windows 0.32.0-dialogue-clarity

## 이번에 고친 기준

공통 C01~C08, 네 인물 R01~R16·후일담, 선택 일상, 메신저, 친밀 이벤트 전후 대사를 앞뒤 맥락과 함께 검토했다. 배타적인 선택의 반응은 각각 비교했다. 이 작업은 문장 이해와 대화 연결의 편집이며 모든 선택 조합을 사람이 플레이했다는 뜻은 아니다.

1. ‘그거·그쪽·다음·남겨 둔다’의 대상을 짐작해야 하는 문장은 구체적으로 쓴다.
2. 농담의 전제가 앞에 없거나 실제 행동과 다르면, 앞 대사와 응수를 함께 고친다.
3. 화자·물건·자리·이미 한 말이 바뀌지 않게 확인한다.
4. 바로 이해되는 장난과 짧은 직구는 남긴다. 모든 비유를 설명문으로 바꾸지는 않는다.

## 대표 수정

| 구간 | 이전 문제 | 현재 |
|---|---|---|
| 공통 C05, 첨부 장면 | ‘같은 페이지에서 안 잘 생각’이 책 위에서 자겠다는 말처럼 읽힘 | “난 읽던 책 마저 읽으려고. 어제는 두 장도 못 읽고 잠들었거든~” |
| 공통 C04, 서윤 첫 소개 | 누가 어려운 사람을 맡았는지 불명확하고, 도현이 서윤까지 포함한 적이 없음 | 짧게 쓰되 설명을 빼지 말라는 실제 요청을 먼저 보여 주고, 까다롭다는 말에 서윤이 장난을 건다. 선택 뒤의 커피 장난·답장 검토까지 연결 |
| 지현 R01 | 지현 한 사람을 ‘두 분’이라고 세는 농담이 불필요하게 헷갈림 | 메뉴를 몰래 보고 있던 행동을 도현이 알아채고, 함께 더 고르는 대화 |
| 지현 R10 | 작은 조립집에 머리를 넣고 작아지겠다는 장난 | 가까이서 구경하되 지붕은 건드리지 말라는 주의와 ‘손은 뒤로’라는 응수 |
| 유진 R03 | 도현이 직접 찍은 사진 속 사람을 도현이냐고 물음 | 비슷한 두 사진을 왜 다시 찍었는지 묻고, 지나가는 사람을 기다렸다는 답에 반응 |
| 리아 R06 | 세 번째 가게로 두 번째 돌아갔다는 말에서 숫자와 대상이 겹침 | “같은 가게 설명을 자꾸 다시 읽더라.” 반말·존댓말 모두 수정 |
| 리아 R11 | 플레이어가 메뉴를 골라도 리아가 자기가 정했다고 함 | “오늘은 내가 전부 준비할 필요가 없었네.” 함께 요리한 경험으로 마무리 |
| 유진 R15 | 도현에게 내준 빈자리에 자신이 다시 앉는 지문, 다 먹은 과자가 뒤에 남아 있음 | 자기 자리로 돌아옴. ‘과자를 나눠 먹은 뒤’로 수정 |
| 서윤 R10 | ‘초콜릿 세 입, 아직 네 번은 아님’이라는 의미 없는 횟수 장난 | 몇 입 먹었는지는 적지 말라는 생활 장난으로 정리 |
| 서윤 R13~후일담 | ‘네가 그리는 다음’, ‘끝날 때까지’, ‘나머지는 따로’가 핵심 사실을 흐림 | 같이 사는 미래·현재 배우자 동거·이혼·남은 불편함을 각각 명시 |
| 이벤트 전후 | 이미 예쁘다고 말했는데 아직 말하지 않은 것처럼 되풀이함. 음료를 주는 방향이 뒤집힌 문장 | 이미 한 칭찬을 인정하는 대사와 무엇을 마실지 고르는 질문으로 수정 |

## 남긴 장면

- 리아가 ‘오 분 동안 일정 생각 안 하기’를 정하자 도현이 그것도 일정이라고 받아치는 장면: 전제가 바로 앞에 있어 이해된다.
- 지현과 카드 그림으로 아침 메뉴를 고르고 잼을 양보하지 않는 장면: 소품과 행동이 농담을 받쳐 준다.
- 유진이 매운 떡볶이를 좋아한다는 발견: 손가락 숫자가 맵기라는 점만 명확히 했다.
- 서윤 O02의 실패한 농담: 인물이 그 자리에서 뜻을 다시 말하는 의도된 엇갈림이다. 설명 없이 플레이어만 알아맞혀야 하는 문장과 구분해 보존했다.

## 유지한 범위와 남은 점

사건 수·선택 개수·기억 변수·조건·보상·핵심 분기·CG 수는 바꾸지 않았다. 리아 반말/존댓말, 서윤 기혼·배우자 동거, 유진 관계 불안, 리아 첫 경험·지현 사적 성향도 유지했다. 새 그림·음성·본장면 묘사는 만들지 않았다.

문장 이해는 개선했지만, 책·사진·약속을 소재로 한 대화 비중 자체를 대규모로 줄인 작업은 아니다. 소재 반복이나 장면 재미까지 완전히 해결됐다고 판단하지 않는다. 실제 처음 읽는 사람의 반응 확인도 남아 있다. 이번 자동 검사는 진행·상태 오류를 확인하며 대사의 재미를 판정하지 않는다.
'''
(H/'docs/대사이해도_전체검수_보고서_v1.md').write_text(report,encoding='utf-8')
(P/'story/dialogue_clarity_review_v1.md').write_text(report,encoding='utf-8')

groups={'공통':['common.rpy','core.rpy'],'강리아':['ria_r01.rpy','ria_r02_r04.rpy','ria_r05_r08.rpy','ria_r09_r12.rpy','ria_r13_e01.rpy'],'백지현':['jihyun_r01_r04.rpy','jihyun_r05_r12.rpy','jihyun_r13_e01.rpy','jihyun_optional.rpy'],'차유진':['yujin_r01_r04.rpy','yujin_r05_r08.rpy','yujin_r09_r12.rpy','yujin_r13_e01.rpy','yujin_optional.rpy'],'한서윤':['seoyun_r01_r04.rpy','seoyun_r05_r12.rpy','seoyun_r13_e01.rpy','seoyun_optional.rpy']}
prefix='''> 현행 갱신: 기획 v3.05 / Windows 0.32.0-dialogue-clarity — 2026-10-21
> 뜻을 짐작해야 하는 농담·혼합 비유·대답의 연결·화자와 소품 불일치를 정리했다. 대사이해도_전체검수_보고서_v1.md와 현행 실행 대본을 우선한다. 사건·선택 기억·인물 설정·자산 계획은 유지한다. 아래 이전 갱신은 이력이다.

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
    rule='''## 현행 대사 검수 규칙 — 2026-10-21

독자가 첫 독서에서 뜻을 알아들을 수 있도록, 농담의 전제와 지시 대상을 앞에 둔다. 책·페이지·지도·빈칸을 연애 감정의 비유로 쓸 때도 실제로 무엇을 말하는지 드러나야 한다. 이미 한 말·화자·메뉴를 고른 사람·컵과 빈자리의 주인이 바뀌지 않는지 확인한다. 수정할 때 앞뒤 응수도 함께 읽고 선택과 기억은 보존한다. 실패한 농담을 인물들이 즉시 풀어 말하는 연출은 유지할 수 있다.

'''
    (H/'docs'/name).write_text(prefix+rule+t,encoding='utf-8')
validation=f'# 대사 이해도 편집 실행 검증\n\n{v["version"]}. 구문 검사 통과. Windows {v["native_cases"]}사례 / {v["native_assertions"]}확인 통과.\n\n| 검사 | 사례 | 확인 |\n|---|---:|---:|\n'
for s in stats:validation+=f'| {s["suite"]} | {s["cases"]} | {s["assertions"]} |\n'
validation+='\n대본의 조건·호출·기억·보상·메뉴 수는 수정 전후 동일함을 비교했다. 이벤트 JSON의 키·배열 구조도 동일하다. 검수 후 유진 O01 응수 두 문장을 한 번 더 다듬어 해당 선택 일상을 별도로 재검사했다. 자동 검사와 편집자의 문장 판단은 별개이며, 전수 조합 검증이나 독자 재미 측정은 아니다.\n'
(H/'docs/대사이해도_실행검증_v1.md').write_text(validation,encoding='utf-8')
(H/'시작안내.txt').write_text('퇴근 후, 우리 — 대본 시험판 '+c['version']+'\n\nafterwork_script_prototype.exe로 실행합니다.\n전체 대본의 이해하기 어려운 농담·비유와 대화 연결을 정리했습니다.\n실행 중인 게임은 종료 후 다시 실행해 주세요.\n상세: 개발자료/docs/대사이해도_전체검수_보고서_v1.md\n',encoding='utf-8')
for f in q.iterdir():
    if f.is_file():shutil.copy2(f,H/'validation'/f.name)
installer=(P/'tools/install_relationship_secrets.py').read_text(encoding='utf-8')
installer=installer.replace('afterwork-relationship-secrets-handoff-v1','afterwork-dialogue-clarity-handoff-v1').replace('testing/relationship-secrets-v1','testing/dialogue-clarity-v1').replace("v['native_cases']==104",f"v['native_cases']=={v['native_cases']}").replace('이전버전_0.30.0_관계반전편집전','이전버전_0.31.0_대사이해도편집전').replace('개발자료/관계반전반영_v1','개발자료/대사이해도편집_v1').replace('관계반전_업데이트확인.json','대사이해도_업데이트확인.json')
(P/'tools/install_dialogue_clarity.py').write_text(installer,encoding='utf-8')
print(json.dumps(v,ensure_ascii=False))
