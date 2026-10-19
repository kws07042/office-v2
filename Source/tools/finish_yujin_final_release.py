from pathlib import Path
import re,json,shutil
P=Path(__file__).resolve().parents[1]
S=P.parent
H=S/'afterwork-yujin-final-handoff-v1'
proof=P/'testing/yujin-final-v1'
def totals(prefix,expected):
    files=list(proof.glob(prefix+'-*.log'))
    assert len(files)==expected
    cases=checks=0
    for f in files:
        t=f.read_text(encoding='utf-8-sig')
        assert '[rpytest] Status: PASSED' in t,f
        cases+=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])
        checks+=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])
        shutil.copy2(f,H/'validation'/f.name)
    return cases,checks
sc,sa=totals('source',4)
nc,na=totals('native',3)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'))
report=dict(version='0.16.0-yujin-complete-text',source_cases=sc,source_assertions=sa,native_cases=nc,native_assertions=na,source_status='passed',native_status='passed',package_files_verified=len(pkg['game_file_hashes']),character_assets_changed=0,rigging_changed=False,steam_achievements_connected=False,github_updated=False)
(H/'validation/final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for name in ('package-verification.json','unchanged-assets-and-ria.json'):
    shutil.copy2(proof/name,H/'validation'/name)
md=f'''# 유진 전체 대본 연결 검증 — 0.16.0-yujin-complete-text

- 소스 실행 {sc}개 사례 / {sa}개 확인 통과. 후반·일상·종료 28사례, 초반·공통→본편·후일담 선택 17사례, 중반 28사례, UI 6사례다.
- 최종 Windows 패키지 {nc}개 사례 / {na}개 확인 통과. 후반·일상·종료 28사례와 초반·공통 연결 17사례, UI 6사례를 검사했다. 최종 한 줄 대사 수정은 패키지에 포함했다.
- 미해결/기존 합의/존중/기억 누락/이미 행동 수습된 경로를 포함했다. R13 합의만으로 수습 완료되지 않고 R14의 실제 이행 뒤 기록되는지, 하지 않은 잘못을 사과하지 않는 경로를 확인했다.
- R13에서 저장한 뒤 지원 계획을 바꾸고 다시 불러와 다른 계획을 고르는 검사, 관계 종료 확정·취소·보류, R15 복장·미룸·연출 건너뛰기, 일상 완료·생략·짧은 반응, 실제 촬영과 후일담 회수를 대표 조합으로 확인했다.
- 공통 구간부터 R16까지 진행하고 E01 읽기/생략/짧은 연결 뒤 읽기 세 경우를 확인했다. R16 이전 새 완주 해금 방지와 관계 종료 시 후반 진행 방지를 확인했다. 기존 회차에서 얻은 완주 기록은 새 회차의 부분 진행으로 지워지지 않는다.
- 초기 중반 회귀 검사는 이미 해금된 완주 기록까지 무조건 false여야 한다고 가정해 실패했다. 기존 기록 유무를 각각 초기 조건으로 주고, 부분 진행이 그 값을 새로 얻거나 지우지 않는 검사로 고쳐 통과했다. 게임에서 기존 해금을 취소하는 변경은 하지 않았다.
- 패키지 {len(pkg['game_file_hashes'])}개 게임 파일을 소스와 대조했다. 테스트·소스 대본·저장 파일은 실행 배포본에서 제외했다. 격리된 복사본에서 패키지 검사를 실행했다.
- 기존 이미지와 리아 대사 모듈은 직전 패키지와 해시가 같다. 메신저·표정·UI·이벤트 표시 및 유진 중반 소스는 설치된 이전 버전과 같으며 이번 바탕화면 업데이트에서 제외한다. 리아 전체 플레이를 새로 반복했다고 주장하지 않는다.
- 게임 캡처로 R13 선택·R15 특별 의상 준비 중 자리·E01 선택지와 임시 입상 배치를 확인했다. 모든 선택 조합의 전수 검증이나 실제 CG·영상·음성·음원 품질 검증은 아니다.

유진은 대본이 연결된 개발 단계다. 한 장의 임시 표정·공용 배경·준비 중 CG가 최종 미술은 아니다. 다음 단계는 대사 전체 읽기와 지현·서윤 대본 구현이며 외부 배포·Steam 출시 완료와 구분한다.
'''
(H/'docs/유진_전체대본_검증결과_v1.md').write_text(md,encoding='utf-8')
(P/'story/yujin_final_review_v1.md').write_text(md,encoding='utf-8')
s=(S/'update_office_v2_yujin_r12.ps1').read_text(encoding='utf-8-sig')
s=s.replace('0.15.0-yujin-r12','0.16.0-yujin-complete-text').replace('yujin-r12','yujin-final').replace('이전버전_0.14.0_유진R12적용전','이전버전_0.15.0_유진전체대본적용전')
s=s.replace('$validation.native_cases -ne 49',f'$validation.native_cases -ne {nc}')
a=s.index('$modules=@(');b=s.index('\n',a)
s=s[:a]+"$modules=@('core.rpyc','screens.rpyc','options.rpyc','yujin_r01_r04.rpyc','yujin_r13_e01.rpyc','yujin_optional.rpyc','event_assets.json','event_story.json','event_cg_plan.json')"+s[b:]
s=s.replace("if($name -eq 'yujin_r09_r12.rpyc')", "if($name -in @('yujin_r13_e01.rpyc','yujin_optional.rpyc'))")
s=s.replace('유진R12_v1','유진전체대본_v1').replace('유진R12_업데이트확인.json','유진전체대본_업데이트확인.json')
s=s.replace('SourceCases=78;NativeCases=49',f'SourceCases={sc};NativeCases={nc}')
(S/'update_office_v2_yujin_final.ps1').write_text(s,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
