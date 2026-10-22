from pathlib import Path
import json,re,shutil,zipfile,hashlib,statistics
P=Path(__file__).resolve().parents[1];S=P.parent;proof=P/'testing/balance-v1';H=S/'afterwork-balance-handoff-v1'
suites='opening_review,editorial_checks,jihyun04_checks,yujin_early_checks,seoyun_checks'.split(',');details=[]
for suite in suites:
 prefix='latest' if suite in ('opening_review','jihyun04_checks') else 'native'
 f=proof/(prefix+'-'+suite+'.log');t=f.read_text(encoding='utf-8-sig');assert '[rpytest] Status: PASSED' in t,f
 details.append({'suite':suite,'cases':int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),'assertions':int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])})
 shutil.copy2(f,H/'validation'/f.name)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'));contract=json.loads((proof/'source-contract.json').read_text(encoding='utf-8'))
clean=Path(pkg['clean_release']);validation=Path(pkg['validation'])
for name,sha in pkg['game_file_hashes'].items():assert hashlib.sha256((clean/'game'/name).read_bytes()).hexdigest()==sha
with zipfile.ZipFile(S/'afterwork-windows-builds/afterwork_script_prototype-0.23.0-route-balance-win.zip') as z:
 assert z.testzip() is None
 assert not any('/opening-traces/' in n or '/saves/' in n or n.endswith(('_tests.rpyc','testcases.rpyc','three_choice_cases.json')) for n in z.namelist())
oldroot=S/'afterwork-opening-handoff-v1/validation/opening-traces'
rows=[]
for f in sorted((validation/'opening-traces').glob('*.json')):
 new=json.loads(f.read_text(encoding='utf-8'));old=json.loads((oldroot/f.name).read_text(encoding='utf-8'))
 assert new['route']==old['route'] and new['variant']==old['variant']
 assert new['decisions']==old['decisions'],f.name
 assert new['dating'] and new['memory'].get(new['route']+'_confession_accepted')
 assert bool(new['memory'].get(new['route']+'_prepared_conversation'))==(new['variant']==2)
 def chars(d,personal):
  rs=[r for r in d['rows'] if (not r['chapter'].startswith('C') if personal else r['chapter'].startswith('C'))]
  if personal:rs += [r for group in d['messages'].values() for r in group]
  return sum(len(re.sub(r'\{[^}]*\}','',r['text'])) for r in rs)
 assert chars(new,False)==chars(old,False),f.name
 rows.append({'route':new['route'],'variant':new['variant'],'before_personal_characters':chars(old,True),'after_personal_characters':chars(new,True),'delta':chars(new,True)-chars(old,True),'common_characters':chars(new,False),'same_choices':True})
 (H/'validation/opening-traces').mkdir(parents=True,exist_ok=True);shutil.copy2(f,H/'validation/opening-traces'/f.name)
assert len(rows)==12
comparison={'scope':'R01-R04 including dialogue,narration,messages; common excluded; three matched paths each','human_reading_time_measured':False,'rows':rows}
(proof/'balance-comparison.json').write_text(json.dumps(comparison,ensure_ascii=False,indent=2),encoding='utf-8');shutil.copy2(proof/'balance-comparison.json',H/'validation/balance-comparison.json')
md='''# 히로인 초반 분량 수정 전후 — 0.22.0 → 0.23.0

2026-10-20. 공통 C01~C08을 제외한 개인 R01~R04의 실제 표시 대사·지문·메신저를 비교했다. 공백과 문장부호는 포함하고 이름·메뉴 UI·선택지 문구는 제외한다. 엔진의 확정 이력(adv)만 세어 현재 표시(current)와 중복 집계하지 않는다. 같은 네 인물×세 경로에서 선택 목록과 공통 분량이 이전과 같음을 대조했다. 서로 다른 선택을 임의로 골라 격차를 줄여 보인 표가 아니다.

| 인물 | 수정 전 | 수정 후 | 같은 세 경로의 평균 증감 |
|---|---:|---:|---:|
'''
names={'ria':'강리아','jihyun':'백지현','yujin':'차유진','seoyun':'한서윤'}
summaries=[]
for route,name in names.items():
 rs=[r for r in rows if r['route']==route];before=[r['before_personal_characters'] for r in rs];after=[r['after_personal_characters'] for r in rs];delta=round(statistics.mean(r['delta'] for r in rs))
 md+=f'| {name} | {min(before):,}~{max(before):,}자 | {min(after):,}~{max(after):,}자 | {delta:+,}자 |\n'
 summaries.append({'route':route,'before_range':[min(before),max(before)],'after_range':[min(after),max(after)],'mean_delta':delta,'before_mean':statistics.mean(before),'after_mean':statistics.mean(after)})
before_ratio=max(r['before_mean'] for r in summaries)/min(r['before_mean'] for r in summaries);after_ratio=max(r['after_mean'] for r in summaries)/min(r['after_mean'] for r in summaries)
ria=next(r for r in summaries if r['route']=='ria');seo=next(r for r in summaries if r['route']=='seoyun')
md+=f'''\n세 경로 평균에서 가장 긴 인물/짧은 인물의 비율은 약{before_ratio:.2f}배에서{after_ratio:.2f}배로 줄었다. 리아/서윤 평균 비율은 약{ria['before_mean']/seo['before_mean']:.2f}배에서{ria['after_mean']/seo['after_mean']:.2f}배다. 여전히 리아가 가장 길고, 정확히 같은 분량으로 맞추지 않았다.

이 수치는 글자 수이지 플레이 시간이나 재미 점수가 아니다. 리아의 빠른 짧은 응수와 다른 인물의 긴 한 문장을 같은 ‘한 번 클릭’으로 세는 데도 차이가 있다. 실제 독자가 느낄 길이는 그림·호흡·선택 숙고에 따라 달라진다. 현재 범위 밖인 R05~E01까지 전체 루트 길이가 균등해졌다고 주장하지 않는다.

이번 편집 판단은 ‘서윤이 바로 다음 약속으로 넘어가던 구간에 지금 같이 하는 경험이 생기고, 리아의 일부 설명 반복이 줄었다’다. 리아의 매력을 깎아 글자 수를 맞추거나 다른 인물에 같은 대사를 복제하지 않았다. 후반 반복 소재와 실제 독자의 반응은 별도 검토가 남아 있다.

## 경로별 원자료

| 인물·경로 | 이전 | 이후 | 차이 |
|---|---:|---:|---:|
'''+''.join(f"| {names[r['route']]} {r['variant']+1} | {r['before_personal_characters']:,} | {r['after_personal_characters']:,} | {r['delta']:+,} |\n" for r in rows)
(H/'docs/히로인_초반분량_수정전후_v1.md').write_text(md,encoding='utf-8');(P/'story/early_route_balance_comparison_v1.md').write_text(md,encoding='utf-8')
total=sum(d['cases'] for d in details);assertions=sum(d['assertions'] for d in details)
report={'version':'0.23.0-route-balance','native_status':'passed','native_cases':total,'native_assertions':assertions,'scene_blocks_rewritten':contract['changed_scene_blocks'],'matched_paths':12,'game_files_verified':len(pkg['game_file_hashes']),'images_changed':0,'rigging_changed':False,'human_reading_time_measured':False,'suites':details,'summaries':summaries,'before_mean_ratio':before_ratio,'after_mean_ratio':after_ratio,'github_updated':False}
(proof/'final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');shutil.copy2(proof/'final-validation.json',H/'validation/final-validation.json')
for n in ('package-verification.json','source-contract.json','unchanged-assets.json','changed-files.json','baseline-reading-profile.json'):shutil.copy2(proof/n,H/'validation'/n)
for f in (validation/'tests/screenshots').glob('opening-*.png'):shutil.copy2(f,H/'screenshots'/f.name)
shutil.copy2(P/'game/opening_tests.rpy',H/'source/game/opening_tests.rpy')
validation_md=f'''# 초반 균형 편집판 검증 — 0.23.0

- Ren’Py 구문 검사 통과. 변경7개 장면의 제어 흐름·조건·선택·기억·보상·호감도 갱신이0.22.0과 같음을 대조했다. 변경은 대사·지문과 버전명이다.
- 관련 검사 {total}사례/{assertions}확인 통과. 네 루트 초반12연결 경로, 준비 대화, 선택한 애정 표현/미룸, 실제 자료의 제출 여부, 리아 말투와 카페 합류, 서윤 휴식 경로의 소품·인사와 후속 경로를 확인했다. 전체 선택 조합의 전수 검사는 아니다.
- 지현 서점의 마지막 지문 한 줄을 설명 문장에서 행동으로 다시 다듬은 뒤, 최종 패키지에서12연결 경로와 지현 초반17사례를 재검사했다. 다른 관련 검사와 재검사 횟수를 중복 합산하지 않았다.
- 실행 ZIP의54게임 파일·CRC·경로·원문/검사/저장/측정 로그 제외 및 폰트 고지를 확인했다. 깨끗한 게임과 별도 진단 사본을 구분했다. 아트는0.22.0과 같다.
- 같은12경로의 실제 표시 기록에서 공통 분량과 선택 목록을 대조해 분량 표를 만들었다. 사람의 실제 독서 시간이나 재미의 실측 결과는 아니다. 게임 그림·리깅·사용자 저장은 변경/삭제하지 않았다.

| 검사 | 사례 | 확인 |
|---|---:|---:|
'''+''.join(f"| {d['suite']} | {d['cases']} | {d['assertions']} |\n" for d in details)
(H/'docs/히로인_초반균형_실행검증_v1.md').write_text(validation_md,encoding='utf-8');(P/'story/early_route_balance_validation_v1.md').write_text(validation_md,encoding='utf-8')
installer=(S/'update_office_v2_opening.ps1').read_text(encoding='utf-8-sig')
for a,b in [('0.22.0-opening-review','0.23.0-route-balance'),('playable-opening-final-v2','playable-balance-final'),('afterwork-opening-handoff-v1','afterwork-balance-handoff-v1'),('opening-v1','balance-v1'),('이전버전_0.21.0_초반연속편집전','이전버전_0.22.0_초반균형편집전'),('초반연속편집_v1','초반균형편집_v1'),('초반연속편집_업데이트확인.json','초반균형편집_업데이트확인.json')]:installer=installer.replace(a,b)
installer=installer.replace('124',str(total))
a=installer.index('$modules=@(');b=installer.index('\n',a)
installer=installer[:a]+'$modules=@('+','.join("'"+n[:-4]+".rpyc'" for n in contract['changed_files'])+')'+installer[b:]
(S/'update_office_v2_balance.ps1').write_text(installer,encoding='utf-8-sig')
print(json.dumps({k:v for k,v in report.items() if k not in ('suites','summaries')},ensure_ascii=False));print(json.dumps(summaries,ensure_ascii=False))
