# 서윤 성인 이벤트 전후 CG · Grok 후보 v001 (2026-11-24)

- 출처: 사용자가 Grok Imagine 에이전트로 생성해 업로드한 zip(SHA-256 앞자리 0c1d15f4feeef1dc), 1792×1008 JPEG 18장.
- 프롬프트: Docs/grok-imagine-agent-seoyun-v001.md. zip 안의 순서는 작업 역순이었다(image.jpg = TASK 18).
- 상태: 후보. 게임에는 아직 연결하지 않았다.

## 검수
| 판정 | 장면 |
|---|---|
| 통과 | R07 B·C, R12 B·C, R15 생활복 B·C, 바니걸 A·B·C, 간호사 B·C, 여경찰 B |
| 시점 수정 | R07 A, R12 A, R15 생활복 A, 간호사 A: 화면 아래 구석에 남자의 어깨·등이 뒤에서 본 모습으로 걸려 있어, 주인공 시점이 아니라 제3자가 보는 화면처럼 보인다 |
| 노출 추가(사용자 요청) | 간호사 A, 여경찰 A, 코스프레 C 세 장 |
| 소품 | 여경찰 C의 알록달록한 패치워크 담요가 작업실 톤과 맞지 않는다 |

## 추가본 반영 (2026-11-24, zip SHA-256 앞자리 a11f194af5a1786c)
| 파일 | 상태 |
|---|---|
| r15_cosplay_nurse_intro, r15_cosplay_police_intro, r15_cosplay_nurse_after | 교체·통과(노출 추가, 주인공 손만 보임) |
| r12_special_intro, r15_home_intro | 교체·통과(시점 수정). r15_home_intro_alt는 다른 안 |
| r15_cosplay_bunny_after | 교체·통과(바니수트+셔츠). _alt는 속옷 세트판 |
| r15_cosplay_police_after_pending | 보류: 하의 속옷이 그려지지 않음(수위 기준 밖), 무릎 위 경찰 모자 빠짐. 기존 police_after 유지 |
| r07_casual_intro | 아직 다시 그리지 않음(구석 어깨 문제 남음) |

## 최종 (2026-11-24)
- r07_casual_intro, r15_cosplay_police_after를 사용자가 올린 두 장으로 교체(시점 수정, 하의 속옷·무릎 위 모자 확인). 보류 파일 삭제.
- 18장 모두 통과. 사용자 요청 흐름(전부 모이면 게임 연결)에 따라 1280×720 PNG로 줄여 Source/game/images/events/seoyun/에 연결.
  A=도입(`*_intro.png`), B=도입 표정(`*_intro_shy.png`), C=이후 대화(`*_after.png`, 새 연결).
