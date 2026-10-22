from pathlib import Path
import json,re,shutil,hashlib,difflib
P=Path(__file__).resolve().parents[1];Q=P/'testing/early-couple-v1'
D=Path('C:/Users/user/Desktop/건/오피스 V2');H=P.parent/'afterwork-early-couple-handoff-v1'
c=json.loads((Q/'contract.json').read_text(encoding='utf-8'));N=Path(c['native'])
digest=lambda f:hashlib.sha256(f.read_bytes()).hexdigest()
stats=[]
for suite in ['ria08','yujin08_checks','jihyun_final_checks','seoyun_checks','integrated_story_checks','early_couple_talk_checks']:
    t=(Q/f'final-{suite}.log').read_text(encoding='utf-8-sig')
    assert '[rpytest] Status: PASSED' in t,suite
    stats.append(dict(suite=suite,cases=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),assertions=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])))
for name,h in c['runtime_sha256'].items():assert digest(N/'game'/name)==h,name
for sub in ['source/game','runtime','docs','validation/traces']:(H/sub).mkdir(parents=True,exist_ok=True)
edits=json.loads((Q/'edits.json').read_text(encoding='utf-8'))
for name in c['changed']:
    old=(Q/(name+'.before')).read_text(encoding='utf-8-sig');new=(P/'game'/name).read_text(encoding='utf-8-sig')
    (Q/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=name+' 0.33',tofile=name+' 0.34')),encoding='utf-8')
    shutil.copy2(P/'game'/name,H/'source/game'/name)
    shutil.copy2(N/'game'/name.replace('.rpy','.rpyc'),H/'runtime'/name.replace('.rpy','.rpyc'))
    if name!='options.rpy':
        for pat in [r'^label .+$',r'^\s*\$ remember\(.+$',r'^\s*\$ award_once\(.+$',r'^\s*call event_sequence\(.+$',r'^\s*menu:$']:
            assert re.findall(pat,old,re.M)==re.findall(pat,new,re.M),(name,pat)
# A changed test checks the same story truth rather than a removed exact phrase.
shutil.copy2(P/'game/yujin08_tests.rpy',H/'source/game/yujin08_tests.rpy')
b=json.loads((Q/'baseline.json').read_text(encoding='utf-8'))
b['source']['yujin08_tests.rpy']=digest(Q/'yujin08_tests.rpy.before')
assert digest(D/'개발자료/source/game/yujin08_tests.rpy')==b['source']['yujin08_tests.rpy']
(Q/'baseline.json').write_text(json.dumps(b,ensure_ascii=False,indent=2),encoding='utf-8')

traces=[]
for who in ['ria','jihyun','yujin','seoyun']:
    for variant in [0,1]:
        f=N/'review-output/integrated-v1'/f'{who}-{variant}.json'
        t=json.loads(f.read_text(encoding='utf-8'));assert t['route']==who and t['variant']==variant
        traces.append(t);shutil.copy2(f,H/'validation/traces'/f.name)
        shared=t['memory'].get('ria_r07_intimacy' if who=='ria' else who+'_r07_pace')=='shared'
        key={'ria':'ria_r08_breakfast_shared','jihyun':'jihyun_r08_shared_morning','yujin':'yujin_r08_morning_shared','seoyun':'seoyun_shared_morning'}[who]
        assert bool(t['memory'].get(key))==shared,(who,variant,key)
        if who=='seoyun':assert t['memory']['seoyun_marriage_state']=='married_cohabiting'
v={'version':c['version'],'native_status':'passed','native_cases':sum(x['cases'] for x in stats),'native_assertions':sum(x['assertions'] for x in stats),'suites':stats,'state_and_choice_flow_unchanged':True,'representative_traces':8,'human_fun_measured':False,'initial_failure':'Old exact phrase assertion in Yujin shared-morning message; updated to compare curtain reference against shared memory; rerun passed'}
v['revision_note']=c['validation_revision_note']
(Q/'validation.json').write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
prefix='''> 現行 갱신: 기획 v3.07 / Windows 0.34.0-early-couple — 2026-10-21
> R05~R08의 교제 변화를 실제 식사·호칭·취향·장난으로 편집했다. R07의 동기와 R08의 실제 선택 기억을 연결한다. 교제초반_편집보고서_v1.md와 실행 소스를 우선한다. 사건 수·핵심 분기·기억·CG 계획·인물 설정은 유지한다. 아래 구버전 갱신은 이력이다.

'''.replace('現行','현행')
rule='''## 교제 초반 현행 기준

- 리아: 새 호칭과 물 따르기 장난, 실제 식사. R07 첫 경험 고백은 모든 세 선택보다 앞에 유지. 반말·존댓말 모두 작성. 공유 아침의 빵과 각자 아침 사진을 구분.
- 지현: 취미를 보여 주며 받고 싶은 칭찬, 도현의 작은 오판, 사적인 접근을 기다리는 마음. 실제 잘못의 벌과 성향을 연결하지 않음. R07 전용 호칭 대화가 R12·R15에 나오지 않도록 슬롯 조건 사용.
- 유진: 매운맛을 따로 주문한 두 접시, 자신에게 한 말을 기억하려는 작은 독점욕. 반복 확인은 줄이고 먼저 제안. 함께 아침을 보낸 경우에만 커튼과 앉았던 자리 회상. 응답 지연·다른 동료 대화·취향 선택은 벌점 없음.
- 서윤: 과자 양보와 메뉴판 너머의 작은 직구. R07은 후식 메뉴를 다시 펴는 도현의 아쉬움에서 개인 작업실의 만남으로 이어짐. 법적 기혼·배우자 동거·R13 공개를 유지하며 별거/이혼 중으로 바꾸지 않음.
- 초대는 본장면에 대한 동의가 아니다. 기존 함께/귀가/대화 뒤 귀가의 선택과 생략·자리 표시를 유지한다. 세 선택의 즉각 반응은 달라도 정답 점수나 새 장기 분기는 없다.
- R04의 상호 교제 확인, O01의 완료/생략 및 실제 기억, R09의 약속 날짜·시각·업무 갈등은 유지한다. 행동 지문은 새 자산이나 애니메이션 구현을 뜻하지 않는다.

'''
groups={'공통':['common.rpy','core.rpy'],'강리아':['ria_r01.rpy','ria_r02_r04.rpy','ria_r05_r08.rpy','ria_r09_r12.rpy','ria_r13_e01.rpy'],'백지현':['jihyun_r01_r04.rpy','jihyun_r05_r12.rpy','jihyun_r13_e01.rpy','jihyun_optional.rpy'],'차유진':['yujin_r01_r04.rpy','yujin_r05_r08.rpy','yujin_r09_r12.rpy','yujin_r13_e01.rpy','yujin_optional.rpy'],'한서윤':['seoyun_r01_r04.rpy','seoyun_r05_r12.rpy','seoyun_r13_e01.rpy','seoyun_optional.rpy']}
for f in (D/'개발자료/docs').glob('*.md'):
    if any(x in f.name for x in ['현행대본','연결대본','초반대본과호감도']):
        old=f.read_text(encoding='utf-8-sig');t=old
        for e in edits:t=t.replace(e['old'],e['new'])
        if t!=old:(H/'docs'/f.name).write_text(prefix+t,encoding='utf-8')
for who,names in groups.items():
    t=f'# {who} 현행 대본 — {c["version"]}\n\n2026-10-21. 실행 소스 추출. 배타적인 선택은 서로 다른 회차의 경로다.\n'
    for name in names:t+='\n## '+name+'\n\n```renpy\n'+(P/'game'/name).read_text(encoding='utf-8-sig')+'\n```\n'
    if who=='강리아':t+='\n## 메신저 대화\n\n```renpy\nlabel ria_r08_phone_conversation:'+(P/'game/office_phone.rpy').read_text(encoding='utf-8-sig').split('label ria_r08_phone_conversation:',1)[1]+'\n```\n'
    (H/'docs'/(who+'_검수후_현행대본.md')).write_text(t,encoding='utf-8')
for name in ['퇴근 후 우리_v2_통합 기획서.md','퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md','기획_질문및결정대장.md','리아와지현_사적성향_현행명세_v1.md','지현_전체대본_현행명세_v1.md','서윤_전체대본_현행명세_v1.md','유진_R05-R08_현행명세_v1.md']:
    t=(D/'개발자료/docs'/name).read_text(encoding='utf-8-sig')
    if name=='서윤_전체대본_현행명세_v1.md':
        t=t.replace('평소 사복·독서 자리를 보여 준 뒤 농담 없이 함께 밤을 보내고 싶다고 제안','평소 사복·개인 작업실. 후식 메뉴를 다시 보는 도현의 아쉬움과 차를 마시는 자리에서 밤을 함께하고 싶은 마음을 제안')
    if name=='유진_R05-R08_현행명세_v1.md':
        t=t.replace('# 차유진 R05~R08 현행 명세 — 기획 v2.86 / 0.14.0-yujin-r08','# 차유진 R05~R08 현행 명세 — 기획 v3.07 / 0.34.0-early-couple')
        t=t.replace('Yujin R07만 기존 이벤트 화면에 연결했다.','R07·R12·R15가 기존 이벤트 화면에 연결되어 있다.')
        t=t.replace('R12·R15는 아직 연결하지 않았다.','R15는 기존 생활복/코스프레 선택을 유지한다. 이번에는 R07 전후 대화만 편집했다.')
        t=t.replace('이후 R09~R16·O01~O03·E01을 이어 쓰고, 최종 사진·CG·영상은 그 뒤 제작한다.','현재 R09~R16·O01~O03·E01도 연결되어 있다. 최종 사진·CG·영상 제작은 여전히 이후 작업이다.')
    (H/'docs'/name).write_text(prefix+rule+t,encoding='utf-8')
report=(P/'story/early_couple_review_v1.md').read_text(encoding='utf-8')
(H/'docs/교제초반_편집보고서_v1.md').write_text(report,encoding='utf-8')
t=f'# 교제 초반 실행 검증\n\n{c["version"]} · 2026-10-21\n\n구문 검사 통과. Windows 자동 실행 {v["native_cases"]}사례 / {v["native_assertions"]}확인 통과.\n\n| 검사 | 사례 | 확인 |\n|---|---:|---:|\n'
for x in stats:t+=f'| {x["suite"]} | {x["cases"]} | {x["assertions"]} |\n'
t+='''
리아: 반말/존댓말, 이전 입맞춤 여부, O01 진행/생략, 함께 머무름/귀가, R07 직전 저장→서로 다른 선택으로 불러오기, 아침 기억·호감도·중복 보상 검증.

추가 리아 검사: 대화 뒤 귀가하는 세 번째 경로에서 반말/존댓말 × 메신저 세 답장, 6경로를 최종 구성으로 실행했다. 밤을 보냈다는 기억과 공유 아침이 생기지 않는지, 선택 답장·메시지 중복·접촉·호감도 상태를 검사했다.

유진: 세 친밀 선택과 약속 시간 세 가지, 저장→시간 변경→불러오기, 제안 주체·아침 기억·메시지 ID 중복·호감도 검증. 초기에는 ‘아침에 커튼’이라는 옛 문구를 찾는 검사 4건이 실패했다. 문구 대신 실제 shared 상태와 커튼 회상의 일치 조건을 확인하도록 갱신하여 12사례 전체가 통과했다. 기준을 삭제하지 않았다.

지현·서윤: R05 이후 선택과 전체 루트, 미룸·관계 종료·후일담의 흐름을 기존 전체 검사로 실행. R07 전용 추가 대화가 공용 R12·R15 흐름을 깨뜨리지 않는지 포함한다.

통합: 공통 시작→R04→R05~R08→R09→후일담의 루트별 2경로, 총 8경로를 실제 실행하고 대사·선택·메시지·기억을 별도 JSON으로 기록. 공유 아침 플래그가 해당 회차의 R07 실제 선택과 일치함도 대조했다. 이 8경로는 대본 전수 조합 검사가 아니다.

정적 비교: 라벨·메뉴 수·기억 기록·보상·이벤트 호출은 편집 전후 동일. 새 상태 변수를 만들지 않았다. 기존 기억과 슬롯을 읽는 표시 조건만 추가했다. 이미지·음성·리깅·이벤트 JSON은 변경하지 않았다.

검사 수는 최종 통과 결과를 합산하며 실패 뒤 재실행을 이중 가산하지 않는다. 실제 독자의 재미, 읽는 속도, 모든 과거 버전 저장의 호환성은 미검증이다. 대표 경로의 독서는 실행 기록을 통한 검토이며, 사람이 원래 속도로 전편을 플레이한 결과가 아니다.

검사 순서: 개별 분기·저장 검사 통과 뒤 실행 기록을 읽다가 리아의 식사→사진 순서 한 지문, 지현의 잼 응수, 유진의 질문 전제를 마지막으로 다듬었다. 이 문구 수정은 상태·선택·기억 구조를 바꾸지 않았다. 그 뒤 최종 컴파일 구성에서 통합 8경로를 다시 실행했다. 개별 전체 검사를 모두 두 번 반복한 것으로 보고하지 않는다.

화면 확인: Windows에서 생성한 지현 R08 메신저 세 답장 화면, 유진 R05 일반 대화·선택 화면을 열어 읽었다. 글자와 버튼 잘림은 이 화면들에서 보이지 않았다. 전 해상도·모든 대사 길이 검증은 아니다. 유진의 기존 한 장짜리 수줍은 임시 표정은 그대로이며 최종 연기가 아니다.
'''
(H/'docs/교제초반_실행검증_v1.md').write_text(t,encoding='utf-8')
(H/'시작안내.txt').write_text('퇴근 후, 우리 — 대본 시험판 '+c['version']+'\n\nafterwork_script_prototype.exe로 실행합니다.\nR05~R08의 교제 초반 행동·장난·다음 날 연락을 편집했습니다.\n실행 중인 게임은 종료 후 다시 실행해 주세요.\n상세: 개발자료/docs/교제초반_편집보고서_v1.md\n',encoding='utf-8')
for f in Q.iterdir():
    if f.is_file():shutil.copy2(f,H/'validation'/f.name)
installer=(P/'tools/install_relationship_secrets.py').read_text(encoding='utf-8')
installer=installer.replace('afterwork-relationship-secrets-handoff-v1','afterwork-early-couple-handoff-v1').replace('testing/relationship-secrets-v1','testing/early-couple-v1').replace("v['native_cases']==104",f"v['native_cases']=={v['native_cases']}").replace('이전버전_0.30.0_관계반전편집전','이전버전_0.33.0_교제초반편집전').replace('개발자료/관계반전반영_v1','개발자료/교제초반편집_v1').replace('관계반전_업데이트확인.json','교제초반_업데이트확인.json')
installer=installer.replace("backup=D/'개발자료/이전버전_0.33.0_교제초반편집전'", "for f in (H/'docs').iterdir():\n    if f.name in b.get('docs',{}):\n        assert digest(D/'개발자료/docs'/f.name)==b['docs'][f.name], 'Concurrent document edit: '+f.name\nbackup=D/'개발자료/이전버전_0.33.0_교제초반편집전'")
(P/'tools/install_early_couple.py').write_text(installer,encoding='utf-8')
print(json.dumps(v,ensure_ascii=False))
