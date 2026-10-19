from pathlib import Path
import json, re, shutil
P=Path(__file__).resolve().parents[1]
S=P.parent
proof=P/'testing/yujin-r12-v1'
H=S/'afterwork-yujin-r12-handoff-v1'
def totals(prefix,expected):
    files=list(proof.glob(prefix+'-*.log'))
    assert len(files)==expected
    count=checks=0
    for f in files:
        t=f.read_text(encoding='utf-8-sig')
        assert '[rpytest] Status: PASSED' in t,f
        count+=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])
        checks+=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])
        shutil.copy2(f,H/'validation'/f.name)
    return count,checks
sc,sa=totals('source',5)
nc,na=totals('native',3)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'))
report=dict(version='0.15.0-yujin-r12',source_cases=sc,source_assertions=sa,native_cases=nc,native_assertions=na,source_status='passed',native_status='passed',package_files_verified=len(pkg['game_file_hashes']),character_assets_changed=0,rigging_changed=False,github_updated=False)
(H/'validation/final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for name in ('package-verification.json','unchanged-assets-and-ria.json'):
    shutil.copy2(proof/name,H/'validation'/name)
md=f'''# 유진 R09~R12 검증 결과 — 0.15.0-yujin-r12

- 소스 실행 {sc}개 사례 / {sa}개 확인 통과: 신규 구간 28사례, 초반·공통 연결 15사례, R05~R08 12사례, 메신저 17사례, UI 6사례.
- 최종 Windows 패키지 {nc}개 사례 / {na}개 확인 통과: 신규 28사례, 초반·공통→R12 15사례, UI 6사례. 소스 검사 뒤 보완한 귀가·산책 위치 표시도 이 패키지 검사에 포함된다.
- 실제 R08의 수/목·19시/19시30분 약속 회수, 세 지원 행동과 실제 동의·수습 상태, 기록집 3후보, 공개/보류와 실제 메시지 전달 시점, 음악 3경로, 목요일 재회 시간·장소 3개, 함께 머물기/귀가/산책 3개를 대표 조합으로 검사했다.
- R12 답장 전에 저장하고 시간 변경 뒤 불러와 다른 시간을 고르는 검사, 연출 건너뛰기, 잘못된 친밀 기억·자동 수습·중복 메시지·가짜 완주 업적 방지 조건을 확인했다. 모든 가능한 조합을 전수 검사한 것은 아니다.
- 패키지 {len(pkg['game_file_hashes'])}개 게임 파일을 현재 소스와 해시 대조했다. 테스트·소스·저장 파일은 실행 배포 폴더에서 제외했다. 검사는 별도 복사본에서만 실행했다.
- 기존 이미지와 리아 대사 모듈 해시는 직전 0.14.0 패키지와 동일하다. 메신저·이벤트 표시·크림 UI·리아 표정 엔진은 재컴파일 해시 일부가 달랐으나 소스가 설치된 이전 버전과 바이트 단위로 동일하다. 이 미수정 모듈들은 바탕화면 업데이트 대상에서 제외했다. 이번에 리아 전체 플레이 검사를 반복했다고 주장하지 않는다.
- 실제 게임 캡처에서 일반 대사·선택지·입상 겹침과 R12의 유진 이름·준비 중 표시를 확인했다. 한 장의 임시 표정·가짜 공용 배경은 최종 아트가 아니다. 실제 음악 재생·음성·CG·영상 품질은 검사 대상이 아니다.
- 처음 문법 검사에서 테스트 조건식 괄호 문제를 발견해 수정했고, 그 뒤 문법 검사와 위 실행 검사를 통과했다. 사용자 저장 파일을 삭제하거나 외부에 업로드하지 않았다.

다음 구현: 유진 R13~R16·선택 일상·후일담. 이미 존중한 경로에 새 잘못을 만들지 않고, 합의한 지원의 실제 실행을 확인한 뒤 다음 결말로 연결한다.
'''
(H/'docs/유진_R09-R12_검증결과_v1.md').write_text(md,encoding='utf-8')
(P/'story/yujin_R09-R12_review_v1.md').write_text(md,encoding='utf-8')
s=(S/'update_office_v2_yujin_r08.ps1').read_text(encoding='utf-8-sig')
s=s.replace('0.14.0-yujin-r08','0.15.0-yujin-r12').replace('yujin-r08','yujin-r12').replace('이전버전_0.13.0_유진R08적용전','이전버전_0.14.0_유진R12적용전')
s=s.replace('$validation.native_cases -ne 50',f'$validation.native_cases -ne {nc}')
start=s.index('$modules=@(')
end=s.index('\n',start)
s=s[:start]+"$modules=@('core.rpyc','screens.rpyc','options.rpyc','yujin_r01_r04.rpyc','yujin_r09_r12.rpyc','event_assets.json','event_story.json','event_cg_plan.json')"+s[end:]
s=s.replace("if($name -in @('yujin_r05_r08.rpyc','images/characters/yujin/ui_temp_v001.png'))", "if($name -eq 'yujin_r09_r12.rpyc')")
s=s.replace('유진R08_v1','유진R12_v1').replace('유진R08_업데이트확인.json','유진R12_업데이트확인.json')
s=s.replace('TemporaryPortraitAdded=1','CharacterAssetsChanged=0').replace('SourceCases=58;NativeCases=50',f'SourceCases={sc};NativeCases={nc}')
(S/'update_office_v2_yujin_r12.ps1').write_text(s,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
