# AI 제작 파이프라인 초기 진단 및 산출물 인덱스

> 후속 확인: [현재 검토 결과와 사건별 제작표](production-review-v001/REVIEW.md)를 우선한다. 이 초기 기록의 버전·95사건·검사기 기능·공식 가이드 미확인 상태는 후속 검토에서 정정/갱신했다.

작성일: 2026-11-06
범위: 저장소 지침·현행 외형 기준·CG 계획·자산 인덱스·기존 검증 자료와 네 프로젝트 스킬 작성. 전체 대본 95개 사건의 장면별 재독은 후속 검토가 필요하며 완료로 간주하지 않는다.

## 확인한 현행 기준

- 저장소 `README.md` 기준 Source는 `0.35.2-player-flow`, Windows 실행판은 `0.34.1-dialogue-style`이다. 두 버전을 혼용하지 않는다.
- [현행 외형 기준](../CharacterArt/APPEARANCE_CURRENT.md)의 canonical reference는 title v002, SHA-256 `8c6966a5dd2ae5da06cb1db17370baab5ae94049d00ebc7d8d441513a7c677a1`이다. 외형 기준은 확정됐지만 네 명의 새 개별 전신 마스터와 분리 입상은 완료되지 않았다.
- [이전 CG 목록](../CharacterArt/CG_CURRENT.md)과 `CG_CURRENT.json`은 2026-11-02 이전 외형의 보관 자산이다. 문서상 설치된 자산은 9개 기록이며 게임 적용 완료로 보지 않는다. Seoyun R13 반지 CG는 이전 서사의 보관 자산이다.
- 현행 `Source/game/event_cg_plan.json`은 planning revision 2.91, 히로인별 4세트, 총 16세트다: R07 casual, R12 special, R15 home/cosplay. 세트마다 도입, 도입 표정, 본장면 기본 슬롯 3개가 있어 계획 경로는 80개(16×5)다. 이는 80개 완성 파일이 있다는 뜻이 아니다. JSON의 이미지 상태는 미제공이며 최종 이미지 대기 상태다. 과거 `Docs/adult_event_cg_plan_v1.json` revision 2.79보다 현행 런타임 계획을 우선했다.
- 일반 장면 CG의 기존 제작 제안 `Docs/scene-cg-plan-v001.md`는 기본 구도 34개(히로인당 8, 공통 2), 선행 12개를 제안한다. 이는 제안 수량이며 승인된 제작 완료 수량이 아니다. 기존 성인이벤트 12세트 계획과 현행 16세트 계획은 범위/대안 구성이 다르므로 하나의 수치로 합산하지 않았다.
- `Source/game/progression_nodes.json`에는 275개 노드(96 event, 157 choice, 22 support)가 있다. 이 수치는 대본 사건 수나 CG 수와 동일하지 않다.

## 이미지 inventory

읽기 전용 검사기 `Source/tools/check_image_assets.py`가 `CharacterArt/assets`와 `Source/game/images`의 PNG 30개를 검사했다. PNG 시그니처, 청크 CRC, IHDR/IEND, 치수, 컬러 타입, SHA-256을 읽었다. 손상/비정상 파일 0개, SHA-256이 동일한 중복 그룹 1개였다. 알파 채널 유무는 PNG 형식 정보이며 실제 투명 픽셀 수를 분석한 결과가 아니다. 시각적 외형 QA도 수행하지 않았다.

실행: `python3 Source/tools/check_image_assets.py`
현재 결과 원본: `/tmp/image-audit.json` (세션 임시 파일; 보존 산출물 아님)

## 파이프라인 스킬

`.agents/skills/`에 `vn-art-qa`, `vn-cg-production`, `renpy-regression`, `vn-continuity-check`를 추가했다. 각각 자산 판정, CG 명세, 엔진 회귀, 대본/장면 연속성을 담당한다. 사용자 승인 없이 이미지·대본·게임 런타임 자산을 승격하거나 변경하지 않도록 경계를 두었다. 공식 skill-creator 패키지는 이 환경에서 제공되지 않아 자체 형식/링크 검사를 수행했다.

## 가능한 검증과 한계

- `python3 -m unittest discover -s Source/tests -p 'test_*.py' -v`: 48개 통과. 순수 모델/정적 소스 검증이며 Ren'Py 엔진 실행 검증은 아니다.
- `python3 Source/tests/player_flow_contract.py`: 현재 main에서 실패. 스크립트는 baseline `44ba86ad5aa7cef83d68abd0be261964df74a937`과 파일 동일성을 기대하지만 현행 `common.rpy`가 그 이후 변경되었다. 테스트 기대를 수정하지 않았다.
- 공식 SDK 8.5.3 다운로드는 `www.renpy.org` 네트워크 정책 거부(403)로 차단되어 SDK 린트·게임 suite·인게임 검수는 미실행이다. 환경 설정 초안에 해당 도메인 허용을 저장했다. 허용 적용 후 공식 SDK SHA-256 `eb0a9be7f0fb13632fe25ceade9a8bed5a1b4d6b6e83bd19eeeb29e1a1bb4a45`를 검증한 뒤 진행해야 한다.

## 아직 확정하지 않은 산출물/검토

1. 95개 사건 및 선택 분기의 대사 전체 재독 결과와 장면별 READY/REVIEW/HOLD 판정.
2. 히로인별 입상 기본 포즈, 표정/눈·입·눈썹 파츠, Live2D 후보 수량. 신규 개별 외형 기준 원화가 대기 중이며 현재 타이틀 합성 이미지로 정확한 파츠 수를 확정할 수 없다. 임시 계획치는 별도 승인 제안으로 산출해야 한다.
3. 34개 일반 장면 CG와 현행 16개 성인 이벤트 세트의 교차 검토, 줄/레이블 위치 갱신, 장면별 소품·의상·분기 재확인.
4. GPT/로컬 생성 방식의 실제 샘플 비교. 이 환경에서 허용·검증된 성인 이미지 생성 도구/모델 및 상업 사용 약관 확인 전에는 품질 비교를 완료로 주장하지 않는다.
5. 강리아 시범용 이미지 생성·인게임 연결은 이번 승인 범위(스킬/분석/명세 우선)에 포함하지 않았다.

## 변경 파일과 보안

신규 파일은 네 개의 SKILL.md, 이 보고서, `Source/tools/check_image_assets.py`이다. 기존 대본·이미지·잠금파일·런타임 코드는 수정하지 않았다. GitHub push/merge, 외부 스킬·모델 설치, 이미지 업로드, 대량 이미지 생성은 하지 않았다.
