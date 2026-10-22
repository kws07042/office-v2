from pathlib import Path
import json,re,shutil,zipfile,hashlib,math
P=Path(__file__).resolve().parents[1];S=P.parent;proof=P/'testing/opening-v1';H=S/'afterwork-opening-handoff-v1'
suites='opening_review,common_romance,jihyun04_checks,yujin_early_checks,seoyun_checks,ria16_flow,editorial_checks'.split(',')
details=[]
for suite in suites:
 prefix='latest' if suite in ('opening_review','common_romance') else 'final'
 f=proof/(prefix+'-'+suite+'.log');t=f.read_text(encoding='utf-8-sig');assert '[rpytest] Status: PASSED' in t,f
 details.append({'suite':suite,'cases':int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),'assertions':int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])})
 shutil.copy2(f,H/'validation'/f.name)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'));contract=json.loads((proof/'source-contract.json').read_text(encoding='utf-8'))
clean=Path(pkg['clean_release']);validation=Path(pkg['validation'])
with zipfile.ZipFile(S/'afterwork-windows-builds/afterwork_script_prototype-0.22.0-opening-review-win.zip') as z:
 assert z.testzip() is None
 assert not any('/opening-traces/' in n or '/saves/' in n or n.endswith(('_tests.rpyc','testcases.rpyc','three_choice_cases.json')) for n in z.namelist())
for n,sha in pkg['game_file_hashes'].items():assert hashlib.sha256((clean/'game'/n).read_bytes()).hexdigest()==sha,n
traces=[]
for f in sorted((validation/'opening-traces').glob('*.json')):
 d=json.loads(f.read_text(encoding='utf-8'));assert d['dating'] and d['memory'].get(d['route']+'_confession_accepted')
 assert bool(d['memory'].get(d['route']+'_prepared_conversation')) == (d['variant']==2)
 rows=d['rows'];pre=[r for r in rows if not re.search(r'R04\b',r['chapter'])]
 common=[r for r in rows if r['chapter'].startswith('C')]
 messages=[r for group in d['messages'].values() for r in group]
 count=lambda rs:sum(len(re.sub(r'\{[^}]*\}','',r['text'])) for r in rs)
 chars=count(pre)+count(messages);units=len(pre)+len(messages);decisions=sum(not re.search(r'R04\b',r['chapter']) for r in d['decisions'])
 # Explicit sensitivity model, not measured player reading speed.
 low=chars/500+units/60+decisions*8/60
 high=chars/300+units*2/60+decisions*15/60
 traces.append({'route':d['route'],'variant':d['variant'],'common_characters':count(common),'before_r04_characters_including_messages':chars,'before_r04_dialogue_units_including_messages':units,'before_r04_choices':decisions,'to_r04_end_characters_including_messages':count(rows)+count(messages),'reading_model_minutes':[round(low,1),round(high,1)]})
 (H/'validation/opening-traces').mkdir(parents=True,exist_ok=True);shutil.copy2(f,H/'validation/opening-traces'/f.name)
assert len(traces)==12
(proof/'reading-profile.json').write_text(json.dumps({'model':'300–500 displayed characters/minute, 1–2 sec/unit, 8–15 sec/choice; not human measurements','paths':traces},ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(proof/'reading-profile.json',H/'validation/reading-profile.json')
pace='''# 초반 분량·읽기 시간 검토 — 0.22.0

2026-10-20. 실제 Windows 검사에서 C01~C08→개인 R01~R04 네 루트×세 경로의 표시된 대사·지문을 수집했다. 세 경로는 업무/취향 선택, 공통 두 번째 만남 상대, 말투, 애정 표현과 준비 대화의 대표 조합이다. 모든 조합을 전수 실행한 것은 아니다. variant2에서 네 인물 모두 ‘마음을 더 이야기’ 경로를 실제로 읽은 상태도 확인했다.

**사람이 읽어 잰 플레이 시간이 아니다.** 아래 분량은 실제 표시 로그에서 집계한 값이고, 시간은 가정을 바꿔 보는 모델이다. 자동 실행의 수십 초를 독서 시간으로 적지 않았다. 확정 이력(adv)만 기록해 화면 표시 중(current)과 두 번 세지 않았다. 메신저 본문은 ID로 저장된 실제 대화를 한 번씩 포함했다. 공백·문장부호를 포함하고 이름·선택지 전체 문구·메뉴 UI는 문자 수에서 제외했다.

시간 가정: 빠른 쪽은500자/분+대사/메시지당1초+선택당8초, 느린 쪽은300자/분+대사/메시지당2초+선택당15초다. 한국어 독자의 보편적 속도라는 주장이나 조사 결과가 아니다. CG·음성·연출이 없는 현행판에 대한 민감도 계산이며, 최종 연출 시간은 더해 넣지 않았다. 기준 구간은 C01 시작부터 R04 첫 대사 직전이다. R04의 고백 후 대화까지 포함한 분량은 별도 열이다.

| 경로 | C08까지 문자 | R04 직전까지 문자 | 대사·메시지 수 | 선택 수 | 가정상 분 | R04 끝까지 문자 |
|---|---:|---:|---:|---:|---:|---:|
'''
names={'ria':'리아','jihyun':'지현','yujin':'유진','seoyun':'서윤'}
for d in traces:
 pace+=f"| {names[d['route']]} {d['variant']+1} | {d['common_characters']:,} | {d['before_r04_characters_including_messages']:,} | {d['before_r04_dialogue_units_including_messages']} | {d['before_r04_choices']} | {d['reading_model_minutes'][0]}~{d['reading_model_minutes'][1]} | {d['to_r04_end_characters_including_messages']:,} |\n"
pace+='''
## 편집 판단

이 가정에서는 고백까지60~90분보다 짧게 나오는 경로가 있다. 따라서 기존 목표 달성을 확인했다고 적을 수 없다. 리아의 개인 초반이 다른 인물보다 길다는 차이도 남아 있다. 시간을 맞추려고 중복 대사·필수 대기·강제 입력 중을 추가하지 않았다. 현재 작업은 분량을 근거로 초반 압축과 빈 문답 보강을 결정한 것이며, 실제 독자 평가를 대체하지 않는다.

다음 외부 첫 독자 검증에서는 처음 시작/C08 진입/R04 첫 대사 시각, 중단·저장·메뉴 체류 시간을 따로 기록한다. ‘빨리 고르고 싶었다/아직 상대를 몰라 망설였다/고백이 급했다’의 구체적 이유도 받는다. 읽기 목표 자체를 바꾸거나 새 사건을 늘리는 결정은 이 결과 이후에 한다. 지금60~90분을 확정 성과로 바꾸지 않는다.
'''
(H/'docs/초반_분량과읽기시간_검토_v1.md').write_text(pace,encoding='utf-8');(P/'story/opening_reading_profile_v1.md').write_text(pace,encoding='utf-8')
total=sum(d['cases'] for d in details);checks=sum(d['assertions'] for d in details)
report={'version':'0.22.0-opening-review','native_status':'passed','native_cases':total,'native_assertions':checks,'suites':details,'connected_paths':12,'rest_prop_cases':3,'scene_blocks_rewritten':contract['changed_scene_blocks'],'game_files_verified':len(pkg['game_file_hashes']),'images_changed':0,'rigging_changed':False,'human_reading_time_measured':False,'github_updated':False,'source_contract':contract}
(proof/'final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');shutil.copy2(proof/'final-validation.json',H/'validation/final-validation.json')
for n in ('package-verification.json','unchanged-assets.json','source-contract.json','changed-files.json','first-attempt-opening_review.log'):
 if (proof/n).exists():shutil.copy2(proof/n,H/'validation'/n)
for n in ('opening_tests.rpy','editorial_tests.rpy','three_choice_cases.json'):shutil.copy2(P/'game'/n,H/'source/game'/n)
for f in (validation/'tests/screenshots').glob('opening-*.png'):shutil.copy2(f,H/'screenshots'/f.name)
md=f'''# 초반 연속 편집판 실행 검증 — 0.22.0

- 최종 Windows 게임 검사 {total}사례 / {checks}확인 통과. 구문 검사도 통과했다.
- 공통부터 네 루트 R04까지12대표 연결 경로, 준비 대화 실제 선택, 손잡기·입맞춤 선택/미룸, 리아 반말·존댓말, C06과 다른 C07 상대, 미확인 업무 자료, 교제 수락/거절·취소, 선택 복원과 후속 기억을 관련 검사로 확인했다. 서윤 휴식 경로의 허구 메모 회귀3개도 통과했다. 전 조합 전수 검사는 아니다.
- 최초 새 검사에서 C05에도 점수 보상이 있다고 잘못 가정한 실패12개가 있었다. 실제 C05는 대화 기억만 남기는 설계라, 실제 보상 장면6개와 C05/C08 기억을 따로 확인하도록 고쳤다. 최초 실패 로그를 보존했다. 측정 기록의 current/adv 이중 집계도 adv만 세도록 수정했다.
- 검사 선택 함수를 엔진이 여러 번 평가해 준비 대화가 건너뛰어질 수 있음을 발견했다. 함수 안에서 선택 여부를 먼저 바꾸지 않고 실제 게임의 prepared 상태를 읽게 고쳤고, 마지막 검사에서는 네 루트 모두 준비 대화를 실제로 읽었다는 상태를 추가로 확인했다. 게임 교제 조건을 완화한 것은 아니다.
- 내부 측정 로그 폴더를 실행 ZIP에서 제외하고 다시 빌드했다. 최종 패키지의54게임 파일·CRC·경로·원문/검사/저장/측정 로그 제외·폰트 고지를 확인했다. 빌드 로그 제외 후 관련7묶음을 실행했고, 마지막 C01 방향 응수 한 줄 교정 뒤 최종 패키지에서 초반12경로와 공통 선택 기억을 다시 검사했다. 나머지5묶음과 마지막 재검사 수를 중복 합산하지 않았다. 검사 원문은 진단 사본에만 있으며 깨끗한 실행판에는 없다.
- 그림·리깅·음성은 변경하지 않았다. 기존 사용자 저장은 삭제하지 않았다. 실제 재미와 독자 읽기 시간의 실측 결과는 아니며, 편집 판단·시간 모델은 별도 문서로 구분한다.

| 검사 | 사례 | 확인 |
|---|---:|---:|
'''+''.join(f"| {d['suite']} | {d['cases']} | {d['assertions']} |\n" for d in details)
(H/'docs/초반_연속검수_실행검증_v1.md').write_text(md,encoding='utf-8');(P/'story/opening_validation_v1.md').write_text(md,encoding='utf-8')
installer=(S/'update_office_v2_immersion.ps1').read_text(encoding='utf-8-sig')
for a,b in [('0.21.0-immersive-dialogue','0.22.0-opening-review'),('playable-immers','playable-opening-final-v2'),('afterwork-immersion-handoff-v1','afterwork-opening-handoff-v1'),('immersion-v1','opening-v1'),('이전버전_0.20.1_몰입재집필적용전','이전버전_0.21.0_초반연속편집전'),('몰입재집필_v1','초반연속편집_v1'),('몰입재집필_업데이트확인.json','초반연속편집_업데이트확인.json')]:installer=installer.replace(a,b)
installer=installer.replace('214',str(total))
extra="$writes.Add(@{Source=(Join-Path $handoff '시작안내.txt');Relative='WINDOWS-README.txt'})"
installer=installer.replace("New-Item -ItemType Directory -Path $backup | Out-Null",extra+"\nNew-Item -ItemType Directory -Path $backup | Out-Null")
a=installer.index('$modules=@(');b=installer.index('\n',a)
installer=installer[:a]+'$modules=@('+','.join("'"+n[:-4]+".rpyc'" for n in contract['changed_files'])+')'+installer[b:]
(S/'update_office_v2_opening.ps1').write_text(installer,encoding='utf-8-sig')
print(json.dumps({k:v for k,v in report.items() if k not in ('suites','source_contract')},ensure_ascii=False))
