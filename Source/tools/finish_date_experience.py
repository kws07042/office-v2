from pathlib import Path
import json,re,shutil,hashlib
P=Path(__file__).resolve().parents[1];S=P.parent;proof=P/'testing/date-experience-v1';H=S/'afterwork-date-experience-handoff-v1'
suites='ria16_flow,jihyun_final_checks,yujin08_checks,yujin_final_checks,seoyun_checks,date_experience_checks'.split(',');details=[]
for suite in suites:
 f=proof/(('final-' if suite=='date_experience_checks' else 'native-')+suite+'.log');t=f.read_text(encoding='utf-8-sig');assert '[rpytest] Status: PASSED' in t,f
 details.append({'suite':suite,'cases':int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),'assertions':int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),'runtime':'packaged Windows exe'});shutil.copy2(f,H/'validation'/f.name)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'));contract=json.loads((proof/'source-contract.json').read_text(encoding='utf-8'));clean=Path(pkg['clean_release'])
for name,sha in pkg['game_file_hashes'].items():assert hashlib.sha256((clean/'game'/name).read_bytes()).hexdigest()==sha,name
report={'version':'0.24.0-date-experience','native_status':'passed','native_cases':sum(d['cases'] for d in details),'native_assertions':sum(d['assertions'] for d in details),'scene_blocks_rewritten':contract['changed_scene_blocks'],'control_flow_choices_flags_awards_unchanged':True,'game_files_verified':len(pkg['game_file_hashes']),'images_changed':0,'human_fun_tested':False,'github_updated':False,'suites':details}
(proof/'final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for n in ('final-validation.json','source-contract.json','changed-files.json','unchanged-assets.json','package-verification.json'):shutil.copy2(proof/n,H/'validation'/n)
md=f'''# 데이트 체험 편집 실행 검증 — 0.24.0
2026-10-20. Ren’Py 구문 검사 통과. 수정9개 장면에서 대사·지문 외 조건·선택 문구·기억·보상·호감도·호출의 동일성을 대조했다.

Windows 실행본의 관련 검사 {report['native_cases']}사례/{report['native_assertions']}확인 통과. 네 루트의 관련 구간과 결말·일상 선택·친밀한 장면 진행/미룸·관계 수습/종료와 유진 R06 초기 애정 표현 경로를 기존 검사로 확인했다. 추가15경로는 지현·서윤 O03의 각3선택과 유진 O03의3장소×3선택을 확인한다. 모든 선택의 데카르트 곱 전수 검사라는 뜻은 아니다.

6개 묶음 모두 패키지에서 추출한 별도 Windows 실행본에서 확인했다. 추가15경로의 검사 도구는 진단 사본에만 추가했고 제품 ZIP에서 제외했다. 처음 추가 검사에는 자동 종료 지시가 빠져 통과 후 창이 남았으므로 종료 지시를 넣고 해당15경로만 재실행했다. 중복 실행은 사례 수에 합산하지 않는다.

| 검사 | 사례 | 확인 |
|---|---:|---:|
'''+''.join(f"| {d['suite']} | {d['cases']} | {d['assertions']} |\n" for d in details)+f'''
실행 ZIP의 {len(pkg['game_file_hashes'])}게임 파일과 원본의 일치·CRC·안전한 경로·폰트 고지·원문/검사/저장/측정 로그 제외를 확인했다. 게임 자산은0.23.0과 같고 리깅·사용자 저장은 변경하지 않았다.

자동 검사는 상태와 실행을 확인한다. 실제 독자의 재미·읽기 시간·새 장난의 웃음 효과는 측정하지 않았다. ‘데이트체험_재미진단과수정_v1.md’의 편집 판단과 남은 약점을 별도로 본다.
'''
(H/'docs/데이트체험_실행검증_v1.md').write_text(md,encoding='utf-8');(P/'story/date_experience_validation_v1.md').write_text(md,encoding='utf-8')
# Small reproducible source pack, isolated from the production game.
shutil.copy2(P/'game/date_experience_tests.rpy',H/'source/game/date_experience_tests.rpy')
for name in ('run_revision_tests.ps1','prepare_date_experience.py','verify_date_experience.py'):
 (H/'validation/tools').mkdir(exist_ok=True);shutil.copy2(P/'tools'/name,H/'validation/tools'/name)
shutil.copy2(P/'.renpy-agent/logs/20261020T085637-a6e7ee47-lint.log',H/'validation/lint.log')
installer=(S/'update_office_v2_balance.ps1').read_text(encoding='utf-8-sig')
for a,b in [('0.23.0-route-balance','0.24.0-date-experience'),('playable-balance-final','playable-date-experience'),('afterwork-balance-handoff-v1','afterwork-date-experience-handoff-v1'),('balance-v1','date-experience-v1'),('이전버전_0.22.0_초반균형편집전','이전버전_0.23.0_데이트체험편집전'),('초반균형편집_v1','데이트체험편집_v1'),('초반균형편집_업데이트확인.json','데이트체험편집_업데이트확인.json')]:installer=installer.replace(a,b)
installer=installer.replace('-ne 95','-ne '+str(report['native_cases'])).replace('NativeCases=95','NativeCases='+str(report['native_cases']))
a=installer.index('$modules=@(');b=installer.index('\n',a)
installer=installer[:a]+'$modules=@('+','.join("'"+n[:-4]+".rpyc'" for n in contract['changed_files'])+')'+installer[b:]
(S/'update_office_v2_date_experience.ps1').write_text(installer,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
