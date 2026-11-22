## 요약
`claude/heroine-sprites`에 쌓인 대사·그림·미니게임·갤러리 작업을 main에 합친다. main은 이 브랜치의 조상이라 충돌 없이 합쳐진다. PR #22·#23·#24의 그림도 이 브랜치에 이미 들어 있어서, 이 PR을 합치면 그 PR들은 닫아도 된다.

## 대사
- 네 루트 본편·엔딩·공통 구간·메신저 말투 정리(히로인별 말버릇, 지현 결재 말투는 장면당 한 번)
- 시제 통일, 연속성 수정, 리아 반말 선택이 다른 루트에서도 유지되게 수정

## 그림 연결 (검수 통과한 GPT 원본)
- 배경 23곳: 장소 문구로 자동 선택, 저녁·밤은 색 보정
- 입상 184장(사복·생활복 두 번째 포즈, 서윤 회색 원피스, 지현 벨트 없는 코트, 울먹 표정)
- 장면 CG 61장을 대본 줄에 연결, 타이틀 키 비주얼
- 표정 자동 규칙: 갈등·이별 장면에서 '!'만으로 웃지 않음, 이별·사과는 슬픔 우선, 핵심 장면 8곳 울먹 고정

## 새 기능
- 미니게임 5종(안내판·빵차 카드·기록집 사진·한 줄로 줄이기·틀린 그림 찾기), 이야기 8곳 + 메인 화면 모음. 건너뛰기 가능, 테스트·스킵 중에는 나오지 않음
- 회상 갤러리: 본 장면 CG와 기록집 사진

## 확인
- 회귀 검사 통과: art, sprite, cream_ui, silk_ui, xmas, opening_review, player_flow, integrated_story, ria16, jihyun_final, yujin_final(재실행), seoyun, minigame, gallery
- ria_expression_checks: 지워진 옛 리아 상반신을 찾던 확인 한 줄을 고쳤고, 고친 뒤 다시 돌리지는 않았음
- 그림체 통일(ComfyUI)은 v002가 탈락해 들어가지 않음. v003 안내: `Docs/home-comfyui-v003.md`

## 남은 것
- ComfyUI v003 결과 검수·교체, 시간대 배경 그림, 성인 이벤트 연결, 출시 빌드·보안 점검표

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01Dnvp3arKhcQBC88sGG3zUd
