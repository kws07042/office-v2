from pathlib import Path
import json,re,shutil,hashlib
P=Path(__file__).resolve().parents[1];S=P.parent;proof=P/'testing/click-interest-v1';H=S/'afterwork-click-interest-handoff-v1'
suites='ria16_flow,jihyun_final_checks,yujin12_checks,yujin_final_checks,seoyun_checks'.split(',');details=[]
for suite in suites:
 f=proof/('native-'+suite+'.log');t=f.read_text(encoding='utf-8-sig');assert '[rpytest] Status: PASSED' in t,f
 details.append({'suite':suite,'cases':int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),'assertions':int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])});shutil.copy2(f,H/'validation'/f.name)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'));contract=json.loads((proof/'source-contract.json').read_text(encoding='utf-8'));clean=Path(pkg['clean_release'])
for n,sha in pkg['game_file_hashes'].items():assert hashlib.sha256((clean/'game'/n).read_bytes()).hexdigest()==sha,n
report={'version':'0.25.0-click-interest','native_status':'passed','native_cases':sum(d['cases'] for d in details),'native_assertions':sum(d['assertions'] for d in details),'scene_blocks_rewritten':11,'control_flow_choices_flags_awards_unchanged':True,'game_files_verified':len(pkg['game_file_hashes']),'images_changed':0,'human_fun_tested':False,'github_updated':False,'suites':details}
(proof/'final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for n in ('final-validation.json','source-contract.json','changed-files.json','unchanged-assets.json','package-verification.json'):shutil.copy2(proof/n,H/'validation'/n)
md=f'''# 흥미 편집 실행 검증 — 0.25.0

Ren’Py 구문 검사 통과. 변경11개 장면은 대사·지문만 수정하고 제어 흐름·선택 문구·기억·교제·보상·호감도·호출이0.24.0과 같음을 대조했다.

별도 저장을 쓰는 실제 Windows 진단 사본에서 {report['native_cases']}사례/{report['native_assertions']}확인 통과. 리아 수습·다음 약속, 지현의 기록집/갈등/관계 종료, 유진 R09~R12 선택 기억과R13이후 지원·종료 경로, 서윤의 기록집·미래 대화·수습 경로를 검사했다. 모든 선택 조합을 전수 검사한 것은 아니다.

| 검사 | 사례 | 확인 |
|---|---:|---:|
'''+''.join(f"| {d['suite']} | {d['cases']} | {d['assertions']} |\n" for d in details)+f'''
ZIP CRC·경로·원문/검사/저장/측정 로그 제외·폰트 고지와 {len(pkg['game_file_hashes'])}게임 파일의 원본 일치를 확인했다. 실행 진단과 깨끗한 설치본은 별도다. 이미지·리깅·사용자 저장은 이번 작업에서 변경하지 않았다.

자동 검사는 실행과 상태를 확인한다. 실제 독자의 웃음·설렘·독서 시간은 측정하지 않았다. 편집 판단과 남은 약점은 ‘다음대사_흥미편집과남은약점_v1.md’를 본다.
'''
(H/'docs/흥미편집_실행검증_v1.md').write_text(md,encoding='utf-8');(P/'story/click_interest_validation_v1.md').write_text(md,encoding='utf-8')
shutil.copy2(P/'.renpy-agent/logs/20261020T095616-58aeeb4b-lint.log',H/'validation/lint.log')
(H/'validation/tools').mkdir(exist_ok=True)
for n in ('run_revision_tests.ps1','prepare_click_interest.py','verify_click_interest.py','finish_click_interest.py'):shutil.copy2(P/'tools'/n,H/'validation/tools'/n)
for n in ('ria16_tests.rpy','jihyun_final_tests.rpy','yujin12_tests.rpy','yujin_final_tests.rpy','seoyun_tests.rpy'):
 if (P/'game'/n).exists():shutil.copy2(P/'game'/n,H/'source/game'/n)
for n in ('jihyun-r13-conflict.png','seoyun-future-conflict.png'):
 f=Path(pkg['validation'])/'tests/screenshots'/n
 if f.exists():
  (H/'screenshots').mkdir(exist_ok=True);shutil.copy2(f,H/'screenshots'/n)
installer=(S/'update_office_v2_date_experience.ps1').read_text(encoding='utf-8-sig')
for a,b in [('0.24.0-date-experience','0.25.0-click-interest'),('playable-date-experience','playable-click-interest'),('afterwork-date-experience-handoff-v1','afterwork-click-interest-handoff-v1'),('date-experience-v1','click-interest-v1'),('이전버전_0.23.0_데이트체험편집전','이전버전_0.24.0_흥미편집전'),('데이트체험편집_v1','흥미편집_v1'),('데이트체험편집_업데이트확인.json','흥미편집_업데이트확인.json')]:installer=installer.replace(a,b)
installer=installer.replace('-ne 106','-ne '+str(report['native_cases'])).replace('NativeCases=106','NativeCases='+str(report['native_cases']))
a=installer.index('$modules=@(');b=installer.index('\n',a)
installer=installer[:a]+'$modules=@('+','.join("'"+n[:-4]+".rpyc'" for n in contract['changed_files'])+')'+installer[b:]
(S/'update_office_v2_click_interest.ps1').write_text(installer,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
