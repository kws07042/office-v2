from pathlib import Path
import json,re,shutil,hashlib
P=Path(__file__).resolve().parents[1];S=P.parent;proof=P/'testing/finale-daily-v1';H=S/'afterwork-finale-daily-handoff-v1'
suites='ria16_flow,jihyun_final_checks,yujin_final_checks,seoyun_checks'.split(',');details=[]
for suite in suites:
 f=proof/('native-'+suite+'.log');t=f.read_text(encoding='utf-8-sig');assert '[rpytest] Status: PASSED' in t,f
 details.append({'suite':suite,'cases':int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),'assertions':int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])});shutil.copy2(f,H/'validation'/f.name)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'));contract=json.loads((proof/'source-contract.json').read_text(encoding='utf-8'));clean=Path(pkg['clean_release'])
for n,sha in pkg['game_file_hashes'].items():assert hashlib.sha256((clean/'game'/n).read_bytes()).hexdigest()==sha,n
report={'version':'0.26.0-finale-daily','native_status':'passed','native_cases':sum(d['cases'] for d in details),'native_assertions':sum(d['assertions'] for d in details),'scene_blocks_rewritten':12,'control_flow_choices_flags_awards_unchanged':True,'game_files_verified':len(pkg['game_file_hashes']),'images_changed':0,'human_fun_tested':False,'github_updated':False,'suites':details}
(proof/'final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for n in ('final-validation.json','source-contract.json','changed-files.json','unchanged-assets.json','package-verification.json'):shutil.copy2(proof/n,H/'validation'/n)
md=f'''# R15~후일담 편집 실행 검증 — 0.26.0

Ren’Py 구문 검사 통과. 네 인물 R15/R16/E01 총12개 장면에서 대사·지문만 편집하고 조건·선택 문구·기억·교제·보상·호감도·호출이0.25.0과 같음을 대조했다.

별도 저장을 쓰는 실제 Windows 진단 사본에서 {report['native_cases']}사례/{report['native_assertions']}확인 통과. 친밀한 장면의 진행/미룸·복장 선택, 관계 유지/종료, 본편 완료/미완료 가드, 후일담의 세 계획과 실제 선택 일상/음악 회상 조건을 기존 검사로 확인했다. 전체 선택 조합의 전수 검사는 아니다.

| 검사 | 사례 | 확인 |
|---|---:|---:|
'''+''.join(f"| {d['suite']} | {d['cases']} | {d['assertions']} |\n" for d in details)+f'''
실행 ZIP CRC·경로·원문/검사/저장/측정 로그 제외·폰트 고지와 {len(pkg['game_file_hashes'])}게임 파일의 원본 일치를 확인했다. 진단 사본과 깨끗한 설치본은 구분했다. 이미지·리깅·사용자 저장은 수정하지 않았다.

지현 동거 제안·서윤 다음 대화 선택의 실제 화면에서 새 대사의 잘림이 없는지 확인했다. 기존 긴 선택 문구의 줄바꿈은 남아 있고 선택 문구 자체는 이번에 바꾸지 않았다. 두 인물의 최종 입상·배경 아트 완성 판정은 아니다.

자동 검사는 실행과 상태를 검증한다. 대사에 대한 편집 판단, 실제 독자의 재미·독서 시간은 다른 항목이다. ‘후반과후일담_일상중심편집_v1.md’에 수정 전후와 남긴 날짜·계획을 적었다. 실제 독자 반응은 측정하지 않았다.
'''
(H/'docs/후반과후일담_실행검증_v1.md').write_text(md,encoding='utf-8');(P/'story/finale_daily_validation_v1.md').write_text(md,encoding='utf-8')
shutil.copy2(P/'.renpy-agent/logs/20261020T101610-4d330129-lint.log',H/'validation/lint.log')
(H/'validation/tools').mkdir(exist_ok=True)
for n in ('run_revision_tests.ps1','prepare_finale_daily.py','verify_finale_daily.py','finish_finale_daily.py'):shutil.copy2(P/'tools'/n,H/'validation/tools'/n)
for n in ('ria16_tests.rpy','jihyun_final_tests.rpy','yujin_final_tests.rpy','seoyun_tests.rpy'):shutil.copy2(P/'game'/n,H/'source/game'/n)
for n in ('jihyun-epilogue-cohabitation-choice.png','seoyun-epilogue-date.png'):
 f=Path(pkg['validation'])/'tests/screenshots'/n
 if f.exists():
  (H/'screenshots').mkdir(exist_ok=True);shutil.copy2(f,H/'screenshots'/n)
installer=(S/'update_office_v2_click_interest.ps1').read_text(encoding='utf-8-sig')
for a,b in [('0.25.0-click-interest','0.26.0-finale-daily'),('playable-click-interest','playable-finale-daily'),('afterwork-click-interest-handoff-v1','afterwork-finale-daily-handoff-v1'),('click-interest-v1','finale-daily-v1'),('이전버전_0.24.0_흥미편집전','이전버전_0.25.0_후일담편집전'),('흥미편집_v1','후일담편집_v1'),('흥미편집_업데이트확인.json','후일담편집_업데이트확인.json')]:installer=installer.replace(a,b)
installer=installer.replace('-ne 107','-ne '+str(report['native_cases'])).replace('NativeCases=107','NativeCases='+str(report['native_cases']))
a=installer.index('$modules=@(');b=installer.index('\n',a)
installer=installer[:a]+'$modules=@('+','.join("'"+n[:-4]+".rpyc'" for n in contract['changed_files'])+')'+installer[b:]
(S/'update_office_v2_finale_daily.ps1').write_text(installer,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
