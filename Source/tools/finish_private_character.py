from pathlib import Path
import difflib
import hashlib
import json
import re
import shutil

P=Path(__file__).resolve().parents[1]
D=Path('C:/Users/user/Desktop/건/오피스 V2')
q=P/'testing/private-character-v1'
c=json.loads((q/'contract.json').read_text(encoding='utf-8'))
n=Path(c['native'])
H=P.parent/'afterwork-private-character-handoff-v1'
for x in ['source/game','runtime','docs','validation/traces']:(H/x).mkdir(parents=True,exist_ok=True)
stats=[]
for suite in ['integrated_story_checks','jihyun_final_checks','ria08']:
    f=q/('final-'+suite+'.log');t=f.read_text(encoding='utf-8-sig')
    assert '[rpytest] Status: PASSED' in t,suite
    stats.append({'suite':suite,'cases':int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),'assertions':int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])})
for name,h in c['runtime_sha256'].items():assert hashlib.sha256((n/'game'/name).read_bytes()).hexdigest()==h,name
for name in c['changed']:
    old=(q/(name+'.before')).read_text(encoding='utf-8-sig')
    new=(P/'game'/name).read_text(encoding='utf-8-sig')
    def flow(t):return [l.strip() for l in t.splitlines() if l.strip().startswith(('$ remember(', '$ award_once(', 'if ', 'elif ', 'else:', 'call ', 'return', 'label ', 'menu:', '$ first_kiss'))]
    assert flow(old)==flow(new),name
    assert len(re.findall(r'^\s+".*":\s*$',old,re.M))==len(re.findall(r'^\s+".*":\s*$',new,re.M)),name
    (q/(name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile=name+' 0.29',tofile=name+' 0.30')),encoding='utf-8')
    shutil.copy2(P/'game'/name,H/'source/game'/name)
    shutil.copy2(n/'game'/name.replace('.rpy','.rpyc'),H/'runtime'/name.replace('.rpy','.rpyc'))
v={'version':c['version'],'native_status':'passed','native_cases':sum(x['cases'] for x in stats),'native_assertions':sum(x['assertions'] for x in stats),'suites':stats,'existing_state_and_choices_preserved':True,'human_fun_measured':False}
(q/'validation.json').write_text(json.dumps(v,ensure_ascii=False,indent=2),encoding='utf-8')
for f in q.iterdir():
    if f.is_file():shutil.copy2(f,H/'validation'/f.name)
for f in (n/'review-output/integrated-v1').glob('*.json'):
    t=json.loads(f.read_text(encoding='utf-8'));assert t['ending']==t['route']+'_good'
    shutil.copy2(f,H/'validation/traces'/f.name)
for who,names in {'강리아':['ria_r01.rpy','ria_r02_r04.rpy','ria_r05_r08.rpy','ria_r09_r12.rpy','ria_r13_e01.rpy'],'백지현':['jihyun_r01_r04.rpy','jihyun_r05_r12.rpy','jihyun_r13_e01.rpy','jihyun_optional.rpy']}.items():
    md=f'# {who} 검수 후 현행 대본 — {c["version"]}\n\n2026-10-21. 현재 실행 소스 추출. 친밀한 본장면의 기존 생략·자리 표시는 유지한다.\n'
    for name in names:md+='\n## '+name+'\n\n```renpy\n'+(P/'game'/name).read_text(encoding='utf-8-sig')+'\n```\n'
    if who=='강리아':md+='\n## 메신저 대화\n\n```renpy\nlabel ria_r08_phone_conversation:'+ (P/'game/office_phone.rpy').read_text(encoding='utf-8-sig').split('label ria_r08_phone_conversation:',1)[1]+'\n```\n'
    (H/'docs'/(who+'_검수후_현행대본.md')).write_text(md,encoding='utf-8')
note='''# 리아·지현 사적 성향 반영 — 0.30.0

2026-10-21 사용자 결정 적용. 노골적인 본장면은 작성하지 않고 기존 생략·자리 표시를 유지한다.

## 확정 설정

- 강리아: 과거 연애 경험은 기존대로 있을 수 있지만, 성적 경험은 없다. 능숙한 장난과 경험을 혼동하지 않는다. 상대의 긴장을 덜어 주려는 마음과 자신이 잘 보이고 싶은 마음 때문에 아는 척했다가 R07에서 사실을 말한다. 순결을 가치 평가나 다른 인물과의 우열로 사용하지 않는다. 도현의 첫 연애 설정을 근거로 구체적인 성적 이력을 추가 확정하지 않는다.
- 백지현: M 성향을 명시한다. 칭찬 선호와 합의된 주도권 역전을 함께 유지하며, 일상·업무에서는 독립적이고 자기 의견이 있는 인물이다. 실제 잘못의 사과나 용서를 성적 역할로 대신하지 않는다. 세부 성행위·처벌·굴욕 대사는 작성하지 않는다. R06에서 사적으로 상대가 먼저 원하는 것을 말해 주길 바란다고 직접 밝힌다.
- 차유진: ‘살짝 멘헤라’는 검토 제안이다. 이번에는 확정하거나 대본에 반영하지 않았다. 관계 불안·작은 질투를 넣는 경우에도 임상 진단명처럼 쓰지 않고, 감시·협박·자해 위협을 호감 보상으로 사용하지 않는 방향을 권고했다. 사용자 결정 전 기존 설정이 우선한다.

## 실행 변경과 연결

리아 R07: 찻잔을 들었다 내려놓고 말 고르기 → 첫 경험임을 밝힘 → 서로 능숙한 척 상대만 보고 있었다고 웃음 → 기존 세 선택. 공개는 친밀한 선택보다 앞에 있으므로 모든 경로에서 들으며, 거절/미루기 경로에서는 이후 경험이 있었다고 쓰지 않는다. R07 이후의 shared/deferred 기억은 그대로다.

지현 R06: 이름을 불러 보고 싶은 기존 장면 뒤에, 상대의 바람을 먼저 듣고 싶은 마음을 덧붙임. 싫으면 싫다고 말하는 태도를 유지한다. R07이나 R12에서 실제 갈등을 벌로 수습하는 장면은 추가하지 않았다.

이전 데이트 활동 0.29는 유지한다. 새 그림·음성·이벤트·기억 변수는 없다. 이전 기획의 ‘칭찬과 부드러운 역전만, 강한 성향으로 통합하지 않음’은 이번 사용자의 M 성향 추가 결정에 맞춰 현행 문구를 갱신한다. 구체적 강도·행위는 미설계다. 앞서 제안한 지현의 숨긴 결정 반전은 여전히 미적용이다.
'''
(H/'docs/리아와지현_사적성향_현행명세_v1.md').write_text(note,encoding='utf-8')
(P/'story/private_character_revision_v1.md').write_text(note,encoding='utf-8')
prefix='''> 현행 갱신: 기획 v3.03 / Windows 0.30.0-private-character — 2026-10-21
> 리아는 과거 연애 유무와 별개로 첫 성적 경험 이전이며 R07에서 능숙한 척했음을 직접 밝힌다. 지현은 M 성향·칭찬 선호·합의된 주도권 역전으로 갱신한다. 전후 대화만 반영하며 본장면 자리 표시는 유지한다. ‘리아와지현_사적성향_현행명세_v1.md’와 현행 대본을 우선한다.
> 유진의 관계 불안·질투 성향은 제안이며 미적용. 이미지·음성·핵심 분기 변화 없음. 이전 갱신은 이력이다.

'''
for name in ['퇴근 후 우리_v2_통합 기획서.md','퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md','기획_질문및결정대장.md']:
    t=(D/'개발자료/docs'/name).read_text(encoding='utf-8-sig')
    t=t.replace('칭찬 페티시·부드러운 주도권 역전','M 성향·칭찬 선호·합의된 주도권 역전')
    t=t.replace('원안의 성적 취향 유지: M 성향·칭찬 선호·합의된 주도권 역전','현행 성향(사용자 추가 결정 반영): M 성향·칭찬 선호·합의된 주도권 역전')
    t=t.replace('강한 굴욕·복종 선호로 통합하지 않는다.','사적 성향을 업무상 복종이나 실제 잘못에 대한 벌로 확대하지 않는다. 구체적인 강도·행위는 아직 정하지 않았다.')
    t=t.replace('| 리아 | 연애 경험 있음. 횟수·기간·상대의 상세 이력은 기본 대본에 넣지 않음 |','| 리아 | 연애 경험은 있으나 성적 경험은 없음. 횟수·기간·상대의 상세 이력은 넣지 않음 |')
    (H/'docs'/name).write_text(prefix+t,encoding='utf-8')
md=f'# 사적 성향 적용 검증 — {c["version"]}\n\n구문 검사 통과. 현재 설치본의 변경 모듈 3개만 교체한 Windows 진단 사본에서 {v["native_cases"]}사례 / {v["native_assertions"]}확인 통과. 공통→후일담 8경로와 지현 후반·리아 초반의 관련 분기 포함. 선택 개수·조건·기억·보상·호출 흐름 동일. 실제 재미나 전체 선택 조합 전수 검사를 뜻하지 않는다.\n'
(H/'docs/사적성향_실행검증_v1.md').write_text(md,encoding='utf-8')
(H/'시작안내.txt').write_text('퇴근 후, 우리 — 대본 시험판 '+c['version']+'\n\nafterwork_script_prototype.exe로 실행합니다.\n리아 R07의 첫 경험 고백과 지현 R06의 사적인 바람을 반영했습니다. 이전 데이트 활동 편집도 유지합니다.\n이미지·음성·본장면 자산은 준비 중입니다. 이미 실행 중이면 종료 후 다시 실행해 주세요.\n상세: 개발자료/docs/리아와지현_사적성향_현행명세_v1.md\n',encoding='utf-8')
installer=(P/'tools/install_couple_activity.py').read_text(encoding='utf-8')
installer=installer.replace('afterwork-couple-activity-handoff-v1','afterwork-private-character-handoff-v1').replace('testing/couple-activity-v1','testing/private-character-v1').replace("v['native_cases']==99","v['native_cases']==42").replace('이전버전_0.28.0_데이트활동편집전','이전버전_0.29.0_사적성향반영전').replace('개발자료/데이트활동편집_v1','개발자료/사적성향반영_v1').replace('데이트활동편집_업데이트확인.json','사적성향_업데이트확인.json')
(P/'tools/install_private_character.py').write_text(installer,encoding='utf-8')
print(json.dumps(v,ensure_ascii=False))
