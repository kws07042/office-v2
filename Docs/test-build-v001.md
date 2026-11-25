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

## test6 (main 병합 후 · 서윤·지현·리아 전후 CG)

| 항목 | 값 |
|---|---|
| 게임 버전 | 0.40.0-test6 (main 06ff7d7 + 버전 표기 1c606cb) |
| 결과 | afterwork_script_prototype-0.40.0-test6-win.zip, 204,130,423바이트, SHA-256 e3025f65691bfa1ba6cab7524a2267e2b3c7beb0da8f5bb07d93f18c03b29cb1 |
| 제외 확인 | 게임 .rpy 원본, *_tests.rpyc, tools, saves 없음 |
| 검사 | 8.6.2 lint 통과. 이벤트 그림, 이후 대화 그림, 본장면 대사, 그림 연결, 서윤 전체, 지현 최종, 리아 R16 통과(Linux). Windows 실제 실행은 못 함 |

## test7 (사원증 이름 입력 커서 위치)

| 항목 | 값 |
|---|---|
| 게임 버전 | 0.40.1-test7 (0239fbe) |
| 결과 | afterwork_script_prototype-0.40.1-test7-win.zip, 204,111,686바이트, SHA-256 b0fd526bfd212a72edb92603792f7abb008f07f6c72ed83d56a561d28736e56f |
| 검사 | 8.6.2 lint 통과, 사원증 이름 검사 통과(Linux). 배포 제외 확인. Windows 실제 실행은 못 함 |

## test8 (대사 1,071줄 교정 · 본장면 흐린 배경 · 갤러리 · 입상 키 · WebP)

| 항목 | 값 |
|---|---|
| 게임 버전 | 0.41.0-test8 (4c3afcd) |
| 결과 | afterwork_script_prototype-0.41.0-test8-win.zip, 143,067,573바이트(test6 204MB에서 줄어듦), SHA-256 93a89949055d7169bd2788bc6682f51b8806c2b0f4eba3925282490953b420e3 |
| 제외 확인 | 게임 .rpy 원본, *_tests.rpyc, tools, saves 없음. 이벤트 그림 WebP 59장 포함 |
| 검사 | 8.6.2 lint 통과. 통합 스토리·오프닝·플레이 흐름·리아 R16·서윤·지현 최종·유진 최종·문자 2종·이벤트 그림·이후 그림·본장면 대사·그림 연결·갤러리·입상·실크 UI·데이트복 통과(Linux). Windows 실제 실행은 못 함 |

## test9 (리아 반말 고정 · 유진 R09 이후 도현 반말 · 리아 문자 반말 복구)

| 항목 | 값 |
|---|---|
| 게임 버전 | 0.42.0-test9 (afe4b5f) |
| 결과 | afterwork_script_prototype-0.42.0-test9-win.zip, 143,070,373바이트, SHA-256 227a2c3267c72a2dc461562590237b083f04941e1eec40b6556f0dee62f1b8f9 |
| 검사 | 8.6.2 lint 통과. 통합 스토리·오프닝·플레이 흐름·리아 R16·유진 최종·유진 R08·유진 R12·문자·본장면 대사 통과(Linux, 유진 R12는 단독 재실행에서 통과). 배포 제외 확인. Windows 실제 실행은 못 함 |

## test10 (성인 장면 표현 순화 · 새틴/테두리 제거 · 대사 618줄 수정 반영)

| 항목 | 값 |
|---|---|
| 게임 버전 | 0.43.0-test10 (4d8cdf0) |
| 결과 | afterwork_script_prototype-0.43.0-test10-win.zip, 143,094,288바이트, SHA-256 c67a92467bf9fd35197288b492178f13165a7c34b034015ec3f79d66e8ef2367 |
| 검사 | 8.6.2 lint 통과. 통합 스토리·오프닝·플레이 흐름·리아 R16/R08/R12·서윤·지현 최종/R04·유진 최종/R08/R12·문자 2종·PC 메신저·본장면 대사·업무 미니게임 통과(Linux). three_choice 10건 실패는 main(06ff7d7)에서도 똑같아서 원래 있던 문제. 배포 제외 확인. Windows 실제 실행은 못 함 |

## test11 (SD 코믹 컷 13장 · 리아 첫날 책상 대사 삭제 · 부를 때 성 빼기)

| 항목 | 값 |
|---|---|
| 게임 버전 | 0.44.0-test11 (2a6a5bb) |
| 결과 | afterwork_script_prototype-0.44.0-test11-win.zip, 146,895,206바이트, SHA-256 222b885534113d77f0cea5e2b2cd24fe032e599e4a3ce38824ea23d41bb84b97 |
| 그림 | main의 sd-comic-masterlook-v001 13장을 1280x720 JPEG로 바꿔 images/cg/*_sd_*.jpg로 넣음(사용자 지시). 출처·해시는 ART_RUNTIME.json |
| 검사 | 8.6.2 lint 통과. 갤러리(SD 컷 복귀 포함)·그림·통합 스토리·오프닝·리아 R16·이름 호칭·본장면 대사 통과(Linux). 배포 제외 확인. Windows 실제 실행은 못 함 |
