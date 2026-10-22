from pathlib import Path
import json, re, shutil, hashlib, difflib

P=Path(__file__).resolve().parents[1]
D=Path('C:/Users/user/Desktop/건/오피스 V2')
q=P/'testing/relationship-secrets-v1'
c=json.loads((q/'contract.json').read_text(encoding='utf-8'))
n=Path(c['native'])
H=P.parent/'afterwork-relationship-secrets-handoff-v1'
for rel in ['source/game','runtime','docs','validation']:(H/rel).mkdir(parents=True,exist_ok=True)
stats=[]
for suite in ['yujin08_checks','yujin12_checks','yujin_final_checks','seoyun_checks','marriage_disclosure_checks','integrated_story_checks']:
    t=(q/('final-'+suite+'.log')).read_text(encoding='utf-8-sig')
    assert '[rpytest] Status: PASSED' in t,suite
    stats.append({'suite':suite,'cases':int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),'assertions':int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])})
def digest(f):return hashlib.sha256(f.read_bytes()).hexdigest()
for name,h in c['runtime_sha256'].items():assert digest(n/'game'/name)==h,name
for name in c['changed']:
    old=(q/(name+'.before')).read_text(encoding='utf-8-sig')
    new=(P/'game'/name).read_text(encoding='utf-8-sig')
    (q/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=name+' 0.30',tofile=name+' 0.31')),encoding='utf-8')
    shutil.copy2(P/'game'/name,H/'source/game'/name)
    runtime=name[:-4]+'.rpyc' if name.endswith('.rpy') else name
    shutil.copy2(n/'game'/runtime,H/'runtime'/runtime)
for name in ['seoyun_tests.rpy','marriage_disclosure_tests.rpy']:
    shutil.copy2(P/'game'/name,H/'source/game'/name)
v={'version':c['version'],'native_status':'passed','native_cases':sum(x['cases'] for x in stats),'native_assertions':sum(x['assertions'] for x in stats),'suites':stats,'human_fun_measured':False,'production_matches_tested':True}
(q/'validation.json').write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
for f in q.iterdir():
    if f.is_file():shutil.copy2(f,H/'validation'/f.name)

note='''# 히로인 설정 변경과 대사 수정 보고서

2026-10-21 · Windows 0.31.0-relationship-secrets · 현행 결정

## 무엇이 달라졌나

| 인물 | 현재 확정 설정 | 이번 작업 |
|---|---|---|
| 강리아 | 연애 경험은 있지만 첫 성적 경험 이전. 능숙한 척한 사실을 R07에서 밝힘 | 0.30 반영분 유지 |
| 백지현 | M 성향, 칭찬 선호, 사적으로 상대에게 주도권을 맡기고 싶은 마음 | 0.30 반영분 유지. 업무 갈등의 사과·처벌과는 별개 |
| 차유진 | 부드러운 존댓말과 적극성을 유지하되 관계 불안·독점욕이 있음 | R06·R08·R10·R12·R15·후일담 대사 수정 |
| 한서윤 | 법적으로 기혼이며 배우자와 현재 함께 살고 있음. 별거·이혼 진행 중이 아님 | 초반 복선, 사적 장소, R13 공개, R14 선택, 후반·후일담 수정 |

## 서윤: 진행 중인 불륜 관계로 변경

| 구간 | 실제 전개 |
|---|---|
| R01·R04 | 전화에 답하지 않는 행동과 비공개 이유에 대한 짧은 망설임. 초반에는 도현이 혼인 사실을 모름 |
| R07·R08·R12 | 둘만의 공간은 가족과 사는 집이 아닌 개인 작업실. R12의 동거 질문을 피함 |
| R13 | 반지 케이스를 계기로 현재 기혼·배우자 동거를 직접 밝힘. 별거나 이혼 절차가 진행 중이라는 핑계를 붙이지 않음 |
| R14 | 즉시 종료 또는 사실 확인. 확인한 다음에도 ‘알고 계속 만남 / 여기서 마침’을 명시적으로 선택 |
| R15·R16 | 계속 만나기로 고른 경로만 진행. 만남이나 친밀한 선택을 용서·신뢰 회복으로 처리하지 않음 |
| E01 | 반년 뒤에도 혼인·배우자 동거 지속. 도현과 동거를 준비하거나 이혼을 약속한 결말로 바뀌지 않음 |

R13 실제 대사: “아니. 나 지금도 결혼한 상태야. 남편하고 같은 집에서 살고 있어.”

R14 실제 선택: “혼인 사실을 안 상태로도, 지금은 계속 만나기로 한다.” / “사실을 들었지만 관계는 여기서 마치기로 한다.”

기존에는 미래 질문을 가볍게 넘긴 문제를 조율하고 동거 준비를 약속했다. 이제는 **중요한 사실을 숨긴 관계를 알고도 이어갈지**가 갈등의 중심이다. 종료하면 이후 연애·친밀 이벤트로 강제로 돌아가지 않는다. 내부 완료 ID `seoyun_good`은 호환을 위해 남겼지만 표시되는 결말은 ‘알고도 고른 다음’이다. 무조건적인 행복 결말이라는 뜻이 아니다.

## 유진: 조용한 독점욕이 실제 대화에 보이게

| 구간 | 표현 |
|---|---|
| R06 | 다른 사람에게도 같은 말을 하는지 묻고, 자신만의 말이었으면 하는 욕심을 드러냄 |
| R08 | 확인받고 싶은 메시지를 쓰다가 보내지 않고, 자기 시간을 보내는 모습 |
| R10 | 교제를 알리고 싶은 이유에 ‘여자친구라고 말해 보고 싶다’는 마음을 추가. 공개를 미뤄도 상대 선택을 받아들임 |
| R12 | ‘내 생각이 났다’는 답장을 두 번 읽었다고 털어놓음 |
| R15 | 옆자리를 다른 사람에게 내주고 싶지 않다고 먼저 말함 |
| E01 | 휴대폰을 보는 도현에게 다시 자신을 봐 달라고 장난. 기다리는 동안 자기 간식을 고름 |

R15 실제 대사: “오늘은 옆이 좋아요. ...다른 사람한테는 그 자리 안 내줄래요.”

단순히 수줍은 인물에서, 좋아하는 만큼 자기가 특별한지 확인하고 싶어 하는 인물로 바꿨다. 매번 불안을 해설하지 않고 메시지·자리·공개 욕심으로 나눴다. 임상 진단명은 붙이지 않았으며 감시·협박·답장 시간 벌점은 추가하지 않았다.

## 대표 수정 전후 — 실제 대사

**유진 R15**

- 이전: “그럼 제가 이겼네요. 오세요.”
- 현재: “오늘은 옆이 좋아요. ...다른 사람한테는 그 자리 안 내줄래요.”
- 단순한 부르기 장난에서 자신만의 자리를 만들고 싶은 욕심으로 바꿨다. 이어지는 도현의 예약 장난과 유진의 응수로 무게를 조절했다.

**서윤 E01**

- 이전: “우리, 같은 집에 들어가는 날도 있었으면 좋겠어. ...당장 집 보러 가자는 건 아니고. 네가 먼저 열쇠 돌리는 소리 같은 게 좀 궁금해졌어.”
- 현재: “걷고 싶어요. 오늘 같이 있고 싶은 건 사실이니까요. 그 뒤까지 약속하지는 않을게요.”
- 화자와 장면 구조까지 바꿨다. 동거를 준비하는 종착점에서, 도현이 현재의 만남만 선택하고 미래를 유보하는 결말로 바꾼 것이다.

## 보존한 것과 한계

- 새 그림·음성·본장면 묘사는 만들지 않았다. 기존 친밀한 본장면 생략·자리 표시와 CG 계획을 유지했다.
- 기존 사건 ID와 루트 완료 ID, 유진의 선택 기억은 유지했다. 서윤 R14에는 사실 확인 후 계속/종료하는 확인 선택을 추가했다. 독립 사건을 늘린 것은 아니다.
- 서윤의 새 갈등은 기존의 가벼운 연애보다 훨씬 무겁다. 반복적인 ‘괜찮지 않다’ 확인 대사가 후반 템포를 늦출 가능성은 실제 독서·플레이로 더 봐야 한다.
- 유진은 노골적인 집착보다 작은 불안·질투 수준이다. 기존 적극성과 다정함을 남긴 편집이다.
- 기존 저장 파일을 지우지 않는다. 다만 새 복선과 사실 공개를 자연스럽게 보려면 새 회차를 권장한다. 예전 중간 저장의 모든 조합에 대한 마이그레이션 검증은 하지 않았다.
- 자동 검사는 분기·기억·완주 안정성의 근거다. 재미나 구매 만족도를 입증하지는 않는다.
'''
report='히로인_설정변경과대사수정_보고서_v1.md'
(H/'docs'/report).write_text(note,encoding='utf-8')
(P/'story/relationship_secrets_current_v1.md').write_text(note,encoding='utf-8')
draft=P/'story/yujin_relationship_anxiety_draft_v1.md'
t=draft.read_text(encoding='utf-8').split('## 별도 결정 대기')[0]
draft.write_text('> 초안 기록. 확정 반영은 relationship_secrets_current_v1.md를 따른다.\n\n'+t+'## 추가 확정\n\n서윤은 배우자와 함께 거주하는 현재 기혼 관계로 확정했고 0.31에 반영했다.\n',encoding='utf-8')

prefix='''> 현행 갱신: 기획 v3.04 / Windows 0.31.0-relationship-secrets — 2026-10-21
> 서윤은 법적 기혼·배우자와 동거 중이며 별거/이혼 절차 중이 아니다. 사적 만남은 개인 작업실. R13 공개→R14 사실 확인 후 계속/종료 선택→후일담에도 혼인 지속. 기존 동거 준비 결말은 폐기한다.
> 유진의 관계 불안·독점욕은 제안 단계가 아니라 현행 대사에 반영했다. 리아 첫 경험·지현 M 성향은 0.30대로 유지한다.
> 자세한 현행 기준은 히로인_설정변경과대사수정_보고서_v1.md와 현재 실행 대본이다. 아래 이전 갱신 문구 중 상충하는 내용은 이력으로만 읽는다.

'''
names=['퇴근 후 우리_v2_통합 기획서.md','퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md','퇴근 후 우리_95개 사건 명세_v1.md','기획_질문및결정대장.md','게임개발_완료까지_전체작업계획_v1.md','서윤_전체대본_현행명세_v1.md','유진_후반과선택일상_현행명세_v1.md','리아와지현_사적성향_현행명세_v1.md']
for name in names:
    t=(D/'개발자료/docs'/name).read_text(encoding='utf-8-sig')
    t=t.replace('| 서윤 | 함께 살 준비를 하기로 합의한 장래 약속 | 기존 책·일정 소품으로 필요한 준비와 결정 날짜를 구체적으로 정함. 실제 이사·새집 장면은 추가하지 않음 | 농담으로 넘기던 미래를 행동 가능한 약속으로 바꿈 |','| 서윤 | 기혼·배우자 동거 지속을 알고 선택한 관계 | 반년 뒤에도 서로 다른 집으로 돌아감. 동거·이혼 확약 없이 지금의 만남과 한계를 확인 | 알고도 계속 만나는 선택의 미해결된 무게를 남김 |')
    if name=='리아와지현_사적성향_현행명세_v1.md':
        t=t.replace('차유진: ‘살짝 멘헤라’는 검토 제안이다. 이번에는 확정하거나 대본에 반영하지 않았다.','차유진: 0.31에서 관계 불안·독점욕을 확정하고 대본에 반영했다. 이전 0.30의 미적용 상태를 대체한다.')
        t=t.replace('사용자 결정 전 기존 설정이 우선한다.','현행 관계 불안·독점욕 명세를 우선한다.')
    (H/'docs'/name).write_text(prefix+t,encoding='utf-8')

groups={'공통':['common.rpy','core.rpy'],'강리아':['ria_r01.rpy','ria_r02_r04.rpy','ria_r05_r08.rpy','ria_r09_r12.rpy','ria_r13_e01.rpy'],'백지현':['jihyun_r01_r04.rpy','jihyun_r05_r12.rpy','jihyun_r13_e01.rpy','jihyun_optional.rpy'],'차유진':['yujin_r01_r04.rpy','yujin_r05_r08.rpy','yujin_r09_r12.rpy','yujin_r13_e01.rpy','yujin_optional.rpy'],'한서윤':['seoyun_r01_r04.rpy','seoyun_r05_r12.rpy','seoyun_r13_e01.rpy','seoyun_optional.rpy']}
for who,files in groups.items():
    md=f'# {who} 현행 대본 — {c["version"]}\n\n2026-10-21. 실행 소스 추출. 배타적인 선택 경로를 함께 수록한 자료이며 한 회차의 경험을 뜻하지 않는다. 메신저의 공통 표시 로직은 office_phone.rpy, 이벤트 자리 표시는 event_story.json에 있다.\n'
    for name in files:md+='\n## '+name+'\n\n```renpy\n'+(P/'game'/name).read_text(encoding='utf-8-sig')+'\n```\n'
    if who=='강리아':md+='\n## 메신저 대화\n\n```renpy\nlabel ria_r08_phone_conversation:'+ (P/'game/office_phone.rpy').read_text(encoding='utf-8-sig').split('label ria_r08_phone_conversation:',1)[1]+'\n```\n'
    (H/'docs'/(who+'_검수후_현행대본.md')).write_text(md,encoding='utf-8')

validation=f'# 관계 반전 실행 검증 — {c["version"]}\n\n구문 검사 통과. Windows 진단 사본에서 총 {v["native_cases"]}사례 / {v["native_assertions"]}개 확인 통과.\n\n| 검사 | 사례 | 확인 |\n|---|---:|---:|\n'
for s in stats:validation+=f'| {s["suite"]} | {s["cases"]} | {s["assertions"]} |\n'
validation+='\n공통부터 후일담까지 8경로, 유진 전·중·후반, 서윤의 기존 선택 조합 및 사실 확인 뒤 계속/종료를 포함한다. 기존 검사는 R14 첫 선택 직후 이미 수습 완료라고 가정해 실패했다. 새 사실 확인 선택의 전후 상태로 검사를 수정한 뒤 재실행했다. 최초 그래픽 초기화 정체는 gl2 렌더러 지정 후 해결했다. 실패 기록도 보관한다.\n\n서윤의 conflict=resolved는 다음 사건 진행 플래그일 뿐 신뢰 회복이 아니다. trust_status=damaged_not_restored를 별도로 확인한다. 옛 저장 전체 조합·모든 배타적 선택의 전수 검사나 실제 플레이어 재미 검증은 아니다.\n'
(H/'docs/관계반전_실행검증_v1.md').write_text(validation,encoding='utf-8')
(H/'시작안내.txt').write_text('퇴근 후, 우리 — 대본 시험판 '+c['version']+'\n\nafterwork_script_prototype.exe로 실행합니다.\n서윤의 현재 기혼·배우자 동거와 유진의 관계 불안·독점욕을 반영했습니다.\n새 전개를 보려면 새 회차를 권장합니다. 실행 중인 게임은 종료 후 다시 실행해 주세요.\n상세: 개발자료/docs/'+report+'\n',encoding='utf-8')
installer=(P/'tools/install_private_character.py').read_text(encoding='utf-8')
installer=installer.replace('afterwork-private-character-handoff-v1','afterwork-relationship-secrets-handoff-v1').replace('testing/private-character-v1','testing/relationship-secrets-v1').replace("v['native_cases']==42",f"v['native_cases']=={v['native_cases']}").replace('이전버전_0.29.0_사적성향반영전','이전버전_0.30.0_관계반전편집전').replace('개발자료/사적성향반영_v1','개발자료/관계반전반영_v1').replace('사적성향_업데이트확인.json','관계반전_업데이트확인.json').replace("f.suffix=='.rpyc' and f.name in b['runtime']","f.suffix in ('.rpyc','.json') and f.name in b['runtime']")
(P/'tools/install_relationship_secrets.py').write_text(installer,encoding='utf-8')
print(json.dumps(v,ensure_ascii=False))
