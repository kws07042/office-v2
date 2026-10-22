from pathlib import Path
import hashlib
import json
import re
import shutil

P=Path(__file__).resolve().parents[1]
S=P.parent
D=Path('C:/Users/user/Desktop/건/오피스 V2')
proof=P/'testing/couple-activity-v1'
H=S/'afterwork-couple-activity-handoff-v1'
c=json.loads((proof/'contract.json').read_text(encoding='utf-8'))
n=Path(c['native'])
version=c['version']
suites=['integrated_story_checks','jihyun_final_checks','yujin08_checks','yujin12_checks','seoyun_checks','ria16_flow']
results=[]
for suite in suites:
    text=(proof/('final-'+suite+'.log')).read_text(encoding='utf-8-sig')
    assert '[rpytest] Status: PASSED' in text,suite
    results.append({'suite':suite,'cases':int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',text)[1]),'assertions':int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',text)[1])})
for rel,h in c['runtime_sha256'].items():
    assert hashlib.sha256((n/'game'/rel).read_bytes()).hexdigest()==h,rel
for f,h in c['source_sha256'].items():
    assert hashlib.sha256((P/'game'/f).read_bytes()).hexdigest()==h,f
for folder in ['docs','source/game','runtime','validation/traces','validation/screenshots']:
    (H/folder).mkdir(parents=True,exist_ok=True)
for name in c['changed']:
    shutil.copy2(P/'game'/name,H/'source/game'/name)
    runtime=name.replace('.rpy','.rpyc')
    shutil.copy2(n/'game'/runtime,H/'runtime'/runtime)
for name in ['ria16_tests.rpy','three_choice_cases.json']:
    shutil.copy2(P/'game'/name,H/'source/game'/name)
for f in proof.iterdir():
    if f.is_file():shutil.copy2(f,H/'validation'/f.name)
stats={'version':version,'native_status':'passed','native_cases':sum(r['cases'] for r in results),'native_assertions':sum(r['assertions'] for r in results),'suites':results,'complete_routes':8,'images_audio_rigging_changed':False,'human_fun_measured':False,'github_updated':False}
(proof/'validation.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(proof/'validation.json',H/'validation/validation.json')
for f in (n/'review-output/integrated-v1').glob('*.json'):
    t=json.loads(f.read_text(encoding='utf-8'))
    assert t['ending']==t['route']+'_good'
    shutil.copy2(f,H/'validation/traces'/f.name)
for f in (n/'tests/screenshots').glob('integrated-*.png'):
    shutil.copy2(f,H/'validation/screenshots'/f.name)
groups={'공통':['common.rpy','core.rpy'],'강리아':['ria_r01.rpy','ria_r02_r04.rpy','ria_r05_r08.rpy','ria_r09_r12.rpy','ria_r13_e01.rpy'],'백지현':['jihyun_r01_r04.rpy','jihyun_r05_r12.rpy','jihyun_r13_e01.rpy','jihyun_optional.rpy'],'차유진':['yujin_r01_r04.rpy','yujin_r05_r08.rpy','yujin_r09_r12.rpy','yujin_r13_e01.rpy','yujin_optional.rpy'],'한서윤':['seoyun_r01_r04.rpy','seoyun_r05_r12.rpy','seoyun_r13_e01.rpy','seoyun_optional.rpy']}
for who,names in groups.items():
    md=f'# {who} 검수 후 현행 대본 — {version}\n\n2026-10-21. 현재 실행 소스에서 추출. 조건·선택·기억을 보존한다. 네 데이트 장면의 공동 활동을 편집했다. 본장면은 기존 자리 표시다.\n'
    for name in names:
        md+='\n## '+name+'\n\n```renpy\n'+(P/'game'/name).read_text(encoding='utf-8-sig')+'\n```\n'
    if who in ('공통','강리아'):
        md+='\n## office_phone.rpy의 메신저 대화\n\n```renpy\n'+(P/'game/office_phone.rpy').read_text(encoding='utf-8-sig').split('label ria_r08_phone_conversation:',1)[-1]+'\n```\n'
    (H/'docs'/(who+'_검수후_현행대본.md')).write_text(md,encoding='utf-8')
review='''# 교제 후 네 데이트 활동 편집 — 0.29.0

2026-10-21. 전체 루트 재집필이 아니라, 앞선 평가에서 우선 고른 네 장면을 실제 공동 활동으로 바꾸는 첫 적용이다. 신규 이미지·음성·미니게임은 만들지 않았다. 지문은 실제 동작 애니메이션 구현을 뜻하지 않는다.

| 장면 | 이전 중심 | 현행 경험 | 보존한 연결 |
|---|---|---|---|
| 유진 R05 | 기록집 첫 장 구성 감상 | 서점 요리책에서 매운맛 취향 발견 → 공원 과자 나누기 → 마지막 바삭한 조각은 자기 몫 → 먼저 애정 표현 | 사진/글/나란히 세 구성은 짧게 실제로 보고 기존 layout 기억 유지. 입맞춤·손잡기·걷기 선택 보존 |
| 지현 R11 | 카드 결과 요약과 칭찬 | 상대 손 읽기, 한 점 차이 승부, 협동에서 자기 칭찬도 받고 싶음, 점수 없는 경로의 잼 욕심 | competitive/cooperative/picture_talk 및 결과값 그대로. 이후 한 점 차이·잼 회상과 충돌하지 않음 |
| 서윤 R10 | 추천 책 해설과 기록집 감상 | 케이크 취향을 틀려 접시 교환, 마지막 조각을 나누며 반응 역전 | R10 ID와 세 문장·독자 반응 기억, 공개 선택 유지. 장 제목은 ‘단골도 틀리는 취향’ |
| 리아 R15 | 가게 찾기 뒤 미래 일정 합의 | 가게 찾기 → 실제 두 메뉴 식사·교환 → 다음 메뉴를 탐내거나 배달 자랑 | weekly_evening/plan_together/rest_balance 모두 실제 대사로 약속한 뜻을 유지. 후일담 달력과 충돌하지 않음 |

리아 반말/존댓말 모두 편집했다. 리아 R15의 젓가락 포장지는 식당에서 챙기는 행동을 먼저 보여 주므로 거절 경로의 포장지 그림 찾기와 연결된다. 친밀 전환·거절·생활복/코스프레·회상·호감도·사건 슬롯 수는 유지했다. 지현의 대결 결과를 역전하지 않은 것은 R12와 후일담의 한 점 차이 회상을 보존하기 위해서다. 다음 승부는 예고이며 이 장면에서 이미 재대결했다고 쓰지 않는다.

## 남은 약점

R06의 애정 표현 조율, R09의 업무 지원, R12의 약속 확인, R13~R14의 갈등, R16·후일담은 이번 네 장면 편집만으로 해결되지 않는다. 모든 루트가 완전히 다른 구조가 됐다고 주장하지 않는다. 실제 독자 재미와 체감 시간은 아직 측정하지 않았다.

## 반전 검토의 범위

현재 적용한 유진의 예상 밖 매운맛 취향, 서윤의 취향 예측 실패 등은 작은 기대 뒤집기다. 결혼 여부·퇴사·숨은 과거 같은 전체 서사 반전은 아니다. 서윤 기혼/별거, 리아의 정해진 출국, 유진의 사전 만남, 지현의 숨겨진 결정은 대화 중 제안했을 뿐 현행 설정이 아니다. 선택되지 않은 제안을 실제 설정이나 회상으로 사용하지 않는다. 큰 비밀은 인물 설정과 기존 교제 동기를 바꾸므로 별도 결정이 필요하다.
'''
(H/'docs/교제후_네데이트활동_편집_v1.md').write_text(review,encoding='utf-8')
(P/'story/couple_activity_revision_v1.md').write_text(review,encoding='utf-8')
prefix='''> 현행 갱신: 기획 v3.02 / Windows 0.29.0-couple-activity — 2026-10-21
> 유진 R05·지현 R11·서윤 R10·리아 R15를 실제 공동 활동·작은 욕심·즉각 반응 중심으로 편집했다. 세 선택과 기존 기억·핵심 분기·CG 계획은 유지한다. 기준은 ‘교제후_네데이트활동_편집_v1.md’와 인물별 ‘검수후_현행대본.md’다.
> 전체 후반 구조 재집필은 아직 아니다. 큰 비밀/기혼 등의 반전 예시는 미채택이며 현행 설정이 아니다. 새 그림·음성은 만들지 않았다. 이전 갱신은 이력이다.

'''
for name in ['퇴근 후 우리_v2_통합 기획서.md','퇴근 후 우리_95개 사건 명세_v1.md','기획_질문및결정대장.md','게임개발_완료까지_전체작업계획_v1.md','퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md']:
    text=(D/'개발자료/docs'/name).read_text(encoding='utf-8-sig')
    details=''
    if '캐릭터 보강' in name:
        details='''## 0.29 생활 취향의 실행 근거

- 유진 R05: 매운 떡볶이 조리법에 관심이 있고, 나눠 먹은 과자의 바삭한 끝 조각은 자기 몫으로 챙긴다. 수줍은 말투와 취향의 강도는 별개다. 도현도 매운맛을 똑같이 좋아한다고 쓰지 않는다.
- 지현 R11: 대결 경로는 기존대로 지현이 한 점 차이 승리. 협동에서도 자기 기여를 인정받고 싶어 한다. 점수 없는 놀이에서는 딸기잼을 양보하지 않고 살구 카드는 나눌 수 있다. 모든 경로에서 대결했다고 회상하지 않는다.
- 서윤 R10: 초콜릿 케이크를 더 좋아해 처음 고른 레몬 접시를 바꾼다. 단골이라 상대 취향까지 다 아는 것은 아니다. 기존 위스키 취향은 유지한다.
- 리아 R15: 함께 찾은 식당에서 메뉴를 바꿔 맛보고 상대 메뉴를 탐내며 다음 저녁을 제안한다. 한 가지 음식만 좋아하는 고정 공식으로 만들지 않는다.

'''
    (H/'docs'/name).write_text(prefix+details+text,encoding='utf-8')
validation=f'''# 교제 후 활동 편집 검증 — {version}

Ren’Py 구문 검사 통과. 현재 바탕화면 게임의 나머지 실행 파일을 그대로 둔 진단 사본에서 변경 모듈 5개를 교체하고 검증했다. {stats['native_cases']}사례 / {stats['native_assertions']}확인 통과. 공통에서 후일담까지 네 루트×두 경로의 진행 기록 8개를 보존했다. 친밀 전환을 미룬 경로도 포함한다. 모든 선택 조합의 전수 검사는 아니다.

| 검사 | 사례 | 확인 |
|---|---:|---:|
'''+''.join(f"| {r['suite']} | {r['cases']} | {r['assertions']} |\n" for r in results)+'''

기존 조건·기억 쓰기·호감도 보상·장면 호출은 수정 전과 동일함을 별도로 대조했다. 변경은 텍스트와 서윤 R10의 표시 제목이다. 새 게임 자산은 없다. 구문·분기 통과는 재미나 독자 몰입의 실측 근거가 아니다. 실행 중인 사용자 게임을 종료하지 않고 저장 파일과 그림·리깅 파일을 유지한다. GitHub에는 이번 업데이트를 올리지 않는다.
'''
(H/'docs/교제후_활동편집_실행검증_v1.md').write_text(validation,encoding='utf-8')
(P/'story/couple_activity_validation_v1.md').write_text(validation,encoding='utf-8')
guide=f'''퇴근 후, 우리 — 대본 시험판 {version}

afterwork_script_prototype.exe로 실행합니다.
이번 변경: 유진 R05의 서점·과자, 지현 R11의 카드놀이, 서윤 R10의 케이크 취향, 리아 R15의 식사 장난.
새 대사는 해당 장면을 다시 진행해 확인할 수 있습니다. 현재 켜져 있는 게임은 종료 후 다시 실행해야 새 파일을 읽습니다.
최종 그림·음성·영상과 친밀한 본장면 자산은 아직 준비 전입니다. 현재 장면은 대본 개발판입니다.
세부 변경·검증: 개발자료/docs/교제후_네데이트활동_편집_v1.md 및 교제후_활동편집_실행검증_v1.md
'''
(H/'시작안내.txt').write_text(guide,encoding='utf-8')
print(json.dumps(stats,ensure_ascii=False))
