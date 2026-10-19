from pathlib import Path
import json,re,shutil
P=Path(__file__).resolve().parents[1]; S=P.parent; H=S/'afterwork-seoyun-final-handoff-v1'; proof=P/'testing/seoyun-final-v1'
def totals(prefix,expected):
    logs=list(proof.glob(prefix+'-*.log')); assert len(logs)==expected,(prefix,len(logs))
    cases=checks=0
    for f in logs:
        t=f.read_text(encoding='utf-8-sig'); assert '[rpytest] Status: PASSED' in t,f
        cases+=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]); checks+=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])
        shutil.copy2(f,H/'validation'/f.name)
    return cases,checks
sc,sa=totals('source',3); nc,na=totals('native',7)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'))
report=dict(version='0.19.0-all-routes-text',source_cases=sc,source_assertions=sa,native_cases=nc,native_assertions=na,source_status='passed',native_status='passed',package_files_verified=len(pkg['game_file_hashes']),character_assets_changed=0,rigging_changed=False,github_updated=False,text_slots_connected=89,planned_work_mini_events_pending=6)
(H/'validation/final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for n in ('package-verification.json','unchanged-assets.json'): shutil.copy2(proof/n,H/'validation'/n)
native=Path(pkg['validation'])
for n in ('seoyun-main-menu.png','seoyun-future-conflict.png','seoyun-phone-three-replies.png','seoyun-epilogue-date.png'):
    f=native/'tests/screenshots'/n; assert f.exists(),f; shutil.copy2(f,H/'screenshots'/n)
md=f'''# 서윤 전체 대본·네 루트 연결 검증 — 0.19.0-all-routes-text

- 초기 소스 검사 {sc}사례 / {sa}확인 통과. 서윤26·기존16개 연출 세트의 두 말투와 건너뛰기34·UI6사례다. 이후 외근 중 메시지를 실제 기록으로 추가하고 최종 실행본에서 다시 확인했다.
- 최종 Windows 실행본 {nc}사례 / {na}확인 통과. 서윤26·연출34·UI6·리아 전체8·유진 초반/공통 연결17·지현 초반/공통 연결17·메신저17을 실행했다.
- 서윤의21개 대표 경로는 공통 기억 유무·초반 화제·약속 종류·실제 이행·포옹/손/말 인사·고백 준비·동료 확인/취소/다시 듣기·첫 입맞춤 미룸·호칭·표현·놀이 아닌 실제 산책·공개·세 번의 친밀한 전환과 미룸·복장·일상·갈등 수습·관계 종료/취소/행동 후 계속 만나겠다고 재확인·후일담 생략을 대표 조합으로 포함한다. 모든 조합 전수 검사는 아니다.
- 별도3개는 실제 처음부터 공통 C08→한서윤→R01~R16→후일담 읽기/생략/한마디 후 읽기를 검증했다. 나머지는 미수습 상태의 후반 해금 방지1·시작 화면 서윤 버튼 진입1이다.
- 메신저 답장 직전 저장→다른 답 전송→복원으로 이전 답과 후속 반응이 남지 않는지 확인했다. 보낸 답과 서윤 확인 답은 각각 한 번, R12 외근 메시지·도현 확인 답도 실제 기록에 남는다. 현실 답장 속도로 결과를 바꾸지 않는다.
- R14 약속 전 저장→실제 수요일 대화 이행→복원으로 아직 하지 않은 수습이 완료 값으로 남지 않는지 확인했다. 갈등 발생/대화/합의/행동을 구분한다. 동거의 확답을 하지 않았는데 약속을 어겼다고 쓰지 않는다. 관계 종료 확정에는 사적인 수요일 만남·후반·완주 해금이 없다.
- 모든 친밀한 전환을 미룬 경로도 본편을 완주했다. 실제 함께 머물지 않은 경로에는 다음 아침이 없다. 빈 자산을 실제 이미지 해금으로 세지 않고, 의상을 골라 갈아입은 것과 친밀한 장면 진행을 구분한다.
- 선택 일상 완료/생략/짧은 반응과 책 대목·농담·자리 변화의 실제 경험을 구분했다. 전권을 다 읽었다거나 아직 찍지 않은 사진을 완성했다고 회상하지 않는다. O02는 R10 끝의 밤 시점 전에 배치해 시간 역행을 피했다.
- 최초 검사1개는 ‘전부 미룸’이라고 적은 검사 경로가 R07에서 함께 머물기를 클릭해 실패했다. 검사 선택 번호를 바로잡아 재실행했고 게임은 실제 클릭한 선택에 맞게 작동했다. 최초 실패 로그도 로컬 증거 폴더에 보존했다.
- 최종 패키지 게임 파일 {len(pkg['game_file_hashes'])}개를 소스와 해시 대조했다. CRC·안전한 압축 경로·폰트 라이선스 포함·원문/테스트/저장 제외를 확인했다. 검사 도구는 별도 실행본 복사본에만 넣었다. 이전0.18 실행본과 인물 이미지가 동일하고 기존 리아·유진·지현 대본 소스도 동일하다.
- 시작 화면·R08 메신저·후반 갈등·후일담 화면을 직접 이미지로 확인했다. 확인한 화면에 잘림·겹침은 없었다. 스크롤 창 위로 이전 메시지 일부가 보이는 것은 정상적인 스크롤이며, 모든 해상도·모든 문장의 상품 품질을 승인한 것은 아니다.

현재 공통8·개인20×4·동료 결말1=89개 기본 텍스트 슬롯이다. 전체95계획의 업무 미니 사건6개, 빠른 새 회차·회상 등 미완 편의 기능, 네 루트 통합 읽기·달력·실제 길이 측정, 최종 UI·미술·영상·음성·음원·Steam 기능은 별도다. 텍스트 첫 연결이며 최종 재미·상용 품질·과거 모든 중간 저장 호환·게임 개발 완료 선언이 아니다. 이미지와 리깅은 생성·편집하지 않았고 외부 배포·GitHub 업로드도 하지 않았다.
'''
(H/'docs/서윤_전체대본_검증결과_v1.md').write_text(md,encoding='utf-8'); (P/'story/seoyun_final_review_v1.md').write_text(md,encoding='utf-8')
s=(S/'update_office_v2_jihyun_final.ps1').read_text(encoding='utf-8-sig')
s=s.replace('0.18.0-jihyun-complete-text','0.19.0-all-routes-text').replace('jihyun-final','seoyun-final').replace('playable-jfin-phone','playable-sfin')
s=s.replace('이전버전_0.17.0_지현전체대본적용전','이전버전_0.18.0_서윤전체대본적용전')
s=s.replace('$validation.native_cases -ne 119',f'$validation.native_cases -ne {nc}')
modules=['core.rpyc','cream_ui.rpyc','screens.rpyc','options.rpyc','seoyun_r01_r04.rpyc','seoyun_r05_r12.rpyc','seoyun_r13_e01.rpyc','seoyun_optional.rpyc','event_assets.json','event_story.json','event_cg_plan.json']
a=s.index('$modules=@('); b=s.index('\n',a)
s=s[:a]+"$modules=@("+','.join("'"+n+"'" for n in modules)+')'+s[b:]
s=s.replace("if($name -in @('jihyun_r05_r12.rpyc','jihyun_r13_e01.rpyc','jihyun_optional.rpyc'))", "if($name -in @('seoyun_r01_r04.rpyc','seoyun_r05_r12.rpyc','seoyun_r13_e01.rpyc','seoyun_optional.rpyc'))")
s=s.replace('지현전체대본_v1','서윤전체대본_v1').replace('지현전체대본_업데이트확인.json','서윤전체대본_업데이트확인.json')
s=s.replace('SourceCases=60;NativeCases=119',f'SourceCases={sc};NativeCases={nc}')
(S/'update_office_v2_seoyun_final.ps1').write_text(s,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
