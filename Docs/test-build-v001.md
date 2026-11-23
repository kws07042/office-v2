# 테스트 빌드 v001 (2026-11-23)

사용자가 직접 플레이해 보기 위한 Windows 테스트 빌드. 출시용이 아니며 SECURITY.md 출시 점검표는 하지 않았다.

| 항목 | 값 |
|---|---|
| 게임 소스 | claude/heroine-sprites a2125fc (git archive로 깨끗한 사본에서 빌드) |
| 엔진 | 공식 Ren'Py 8.6.2 SDK (renpy.org/dl/8.6.2, 2026-11-18 공개), renpy-8.6.2-sdk.tar.bz2 SHA-256 07fcb871961af83a8564723a1ad7e8524f42479e75c998d4649dda08187e2e18. 배포 측 서명(.sums)은 이 환경에서 검증하지 못했고, HTTPS로 받은 파일의 해시만 기록했다 |
| 빌드 | launcher distribute --package win |
| 결과 | afterwork_script_prototype-0.35.3-seoyun-parent-review-win.zip, 134,784,223바이트, SHA-256 7449dfd5af13f773b1ca2bb53bc5e6005cd64920f4419aa1b3802376daa759c4 |
| 제외 확인 | 게임 .rpy 원본, *_tests.rpyc, tools, tests, saves, review-output, opening-traces, story, art 없음 |
| 확인한 것 | 8.6.2 lint 통과, 8.6.2로 타이틀·R12 데이트복 화면 검사 통과(Linux 렌더러). Windows 실제 실행은 이 환경에서 못 함 |

## test2 (같은 날, main 병합 후)

첫 빌드는 main의 PR #34~#41(이름표·대화창·입상 배치·상업용 UI)이 빠진 작업 브랜치에서 만들어 최신이 아니었다. main을 병합하고 리아 R01 장소·배경을 고친 뒤 다시 빌드했다.

| 항목 | 값 |
|---|---|
| 게임 버전 | 0.36.0-test2 (88c8af7 + 버전 표기) |
| 결과 | afterwork_script_prototype-0.36.0-test2-win.zip, 134,797,155바이트, SHA-256 bb3b748f55db3ac83ae6633e6850f9e66a56f310785bdc975596805c07853fbc |
| 검사 | lint 통과. 타이틀·사내 메신저·데이트복(화면/전환)·입상·그림 연결·실크 UI·크림 UI·미니게임·갤러리 10개, 리아 R16·리아 R16 흐름·오프닝·플레이 흐름·통합 플레이 5개 통과(8.6.0 비공식 엔진, Linux). Windows 실제 실행은 못 함 |

## test3 (주인공 이름·사원증·GY브랜딩)

| 항목 | 값 |
|---|---|
| 게임 버전 | 0.37.0-test3 |
| 결과 | afterwork_script_prototype-0.37.0-test3-win.zip, 134,801,459바이트, SHA-256 e483b417f8fa2a8d398b8355cc242e0ce1df250a483664c26f9965f093d2651a |
| 검사 | lint 통과. 이름·타이틀·사내 메신저·휴대폰·실크 UI·크림 UI·데이트복 화면·오프닝·리아 R16·통합 플레이·플레이 흐름 11개 통과(8.6.0 비공식 엔진, Linux). Windows 실제 실행은 못 함 |

## test4 (R12 데이트복 입상·인트로 CG 25장 연결)

| 항목 | 값 |
|---|---|
| 게임 버전 | 0.38.0-test4 (5af35a0) |
| 결과 | afterwork_script_prototype-0.38.0-test4-win.zip, 167,605,858바이트, SHA-256 854f956059849ade1e9f41d5e4ab864ed4214d9f1f44cd0ab886f54d7ffc92ac |
| 제외 확인 | 게임 .rpy 원본, *_tests.rpyc, tools, saves 없음(.rpy는 엔진 renpy/common만). 인트로 CG 24장 + 모텔 CG, 데이트복 입상 32장 포함 |
| 검사 | 인트로 CG 연결 뒤 five_asset·갤러리·리아 R16 통과. 지현·유진·서윤 최종 검사는 다시 돌리는 중. Windows 실제 실행은 못 함 |

## test5 (성인 이벤트 본장면 대사 연결)

| 항목 | 값 |
|---|---|
| 게임 버전 | 0.39.0-test5 (d994b95) |
| 결과 | afterwork_script_prototype-0.39.0-test5-win.zip, 167,612,908바이트, SHA-256 87d45d04e366463b3c5f226f11a6dc9fb74de32dad0b87600b56e88dfae21f92 |
| 내용 | event_main_text.json(25장면, Docs/adult/grok-adult-scenes-v003b.json 복사)을 본장면 CG1~3에 한 줄씩 표시. 리아 모텔은 대사창으로 재생 |
| 제외 확인 | 게임 .rpy 원본, *_tests.rpyc, tools, saves 없음(.rpy는 엔진 renpy/common만) |
| 검사 | 8.6.2 lint 통과. 본장면 대사(데이터·한 줄 이동·이름 치환·모텔), 그림 연결, 도입 CG 검사 통과(Linux). Windows 실제 실행은 못 함 |
