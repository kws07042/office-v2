from pathlib import Path
import re,json,shutil
P=Path(__file__).resolve().parents[1]
S=P.parent
H=S/'afterwork-review-jihyun-r04-handoff-v1'
proof=P/'testing/review-jihyun-r04-v1'
def totals(prefix,expected):
    logs=list(proof.glob(prefix+'-*.log'))
    assert len(logs)==expected
    cases=checks=0
    for f in logs:
        t=f.read_text(encoding='utf-8-sig')
        assert '[rpytest] Status: PASSED' in t,f
        cases+=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])
        checks+=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])
        shutil.copy2(f,H/'validation'/f.name)
    return cases,checks
ac,aa=totals('audit',11)
sc,sa=totals('source',3)
nc,na=totals('native',5)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'))
report=dict(version='0.17.0-review-jihyun-r04',audit_cases=ac,audit_assertions=aa,source_cases=sc,source_assertions=sa,native_cases=nc,native_assertions=na,audit_status='passed',source_status='passed',native_status='passed',package_files_verified=len(pkg['game_file_hashes']),character_assets_changed=0,rigging_changed=False,github_updated=False)
(H/'validation/final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for name in ('package-verification.json','unchanged-assets.json'):
    shutil.copy2(proof/name,H/'validation'/name)
md=f'''# 전체 검수 후 지현 초반 연결 — 최종 검증

- 지현 착수 전 기존 구현 감사: {ac}개 사례 / {aa}개 확인 통과. ‘전체대본_검수및수정_20261019.md’의 범위와 남은 제작 과제를 따른다.
- 지현 추가 후 소스 검사: {sc}개 사례 / {sa}개 확인 통과. 지현15개 대표 조합·직접 확인 진입·공통 C08 연결, UI6, 이번 회상 대사 수정9개다.
- 최종 Windows 패키지: {nc}개 사례 / {na}개 확인 통과. 지현17, UI6, 이번 수정9, 리아 전체8, 유진 초반·전체 연결17을 다시 실행했다. 마지막 두 기존 루트 검사는 지현 추가 뒤에도 완주·거절·관계 종료·후일담 등이 유지되는지 확인하는 회귀 검사다.
- 지현은 공통 C02의 근거/실제 후속 제출/미제출/비교/기억 없는 경로, 화제3개·데이트 계획3개·고백 전 준비·동료 확정/취소/마음 다시 듣기·다음 데이트3개를 대표 조합으로 검사했다. R02 저장 후 선택을 바꾸고 복원하는 사례도 포함했다. 전 조합을 전수 검사한 것은 아니다.
- 지현 검사의 첫 실행에서는 첫 메시지를 읽기 전에 후속 답변 완료 값을 검사하고, 동료 결말의 실제 합동 장면에도 다른 히로인 입상이 없어야 한다고 잘못 가정한 검사문을 수정했다. 게임에서는 메시지를 읽은 뒤 상태를 기록하며, 지현 단독 장면에 다른 입상을 대신 쓰지 않는다.
- 실행본 {len(pkg['game_file_hashes'])}개 게임 파일을 소스와 해시 대조했다. 실행 배포본에는 테스트·소스·저장 파일을 제외했고, 검사 도구는 별도 복사본에만 넣었다. 기존 이미지가 이전 실행본과 동일함을 확인했다.
- 시작 화면의 별도 지현 확인 버튼·고백 화면·메신저 기록을 실제 캡처로 확인했다. 지현은 그림 미제공 상태이고, 빈 배경의 대본 화면은 최종 미술 승인 결과가 아니다.
- 새 초반 구간 완료는 전체 지현 엔딩·Steam 업적이 아니다. 다른 회차에서 얻은 로컬 완주 값이 있으면 초반 진행이 이를 새로 얻거나 지우지 않는다. 저장 호환성을 모든 중간 위치에서 검증했다는 뜻도 아니다.

다음 구현은 지현 R05~R08이다. R02의 맡긴 범위·실제 활동과 R04의 다음 데이트 방식을 회수하고, R05에서 첫 입맞춤을 선택 가능하게 한다. 이미지·영상·음성 제작은 기존 계획대로 뒤로 둔다.
'''
(H/'docs/지현_R01-R04_검증결과_v1.md').write_text(md,encoding='utf-8')
(P/'story/jihyun_R01-R04_review_v1.md').write_text(md,encoding='utf-8')
s=(S/'update_office_v2_yujin_final.ps1').read_text(encoding='utf-8-sig')
s=s.replace('0.16.0-yujin-complete-text','0.17.0-review-jihyun-r04').replace('yujin-final','review-jihyun-r04')
s=s.replace('playable-review-jihyun-r04-release','playable-j04')
s=s.replace('이전버전_0.15.0_유진전체대본적용전','이전버전_0.16.0_전체검수_지현초반적용전')
s=s.replace('$validation.native_cases -ne 51',f'$validation.native_cases -ne {nc}')
a=s.index('$modules=@(');b=s.index('\n',a)
s=s[:a]+"$modules=@('core.rpyc','cream_ui.rpyc','screens.rpyc','options.rpyc','ria_r09_r12.rpyc','ria_r13_e01.rpyc','yujin_r13_e01.rpyc','jihyun_r01_r04.rpyc')"+s[b:]
s=s.replace("if($name -in @('yujin_r13_e01.rpyc','yujin_optional.rpyc'))", "if($name -eq 'jihyun_r01_r04.rpyc')")
s=s.replace('유진전체대본_v1','전체검수_지현초반_v1').replace('유진전체대본_업데이트확인.json','전체검수_지현초반_업데이트확인.json')
s=s.replace('SourceCases=79;NativeCases=51',f'AuditCases={ac};SourceCases={sc};NativeCases={nc}')
(S/'update_office_v2_review_jihyun_r04.ps1').write_text(s,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
