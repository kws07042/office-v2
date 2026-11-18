# 남은 작업 넘겨주기 v001 (2026-11-19)

〈퇴근 후, 우리〉에서 Claude 다음으로 넘길 일을 한곳에 모은 목록이다. 대본·시스템은 main에 모두 들어가 있다(PR #20 합침).

---

## 0. 지금 바로 할 것 — 브랜치 정리 (PC 터미널)

프로젝트 폴더에서 아래 명령을 한 번 실행한다. main만 남고 23개가 지워진다.

```bash
git push origin --delete claude/appearance-update-v003 claude/art-prompts claude/design-polish claude/heroine-masters-final claude/heroine-masters-v001 claude/jihyun-chatgpt-hair claude/jihyun-revert-hands claude/remove-old-heroine-art claude/ria-dialogue-pass claude/silk-motion-v2 claude/silk-ui claude/silk-ui-on-main claude/sound-v1 claude/yujin-designer claude/yujin-silver codex/afterwork-ui-skill codex/commercial-badge-ui codex/title-menu-v002 codex/window-ui-full story/full-script-edit story/player-flow-polish story/ria-event-dialogue-v0357 story/work-mini-scenes && git fetch --prune && git checkout main && git pull
```

- `story/ria-event-dialogue-v0357`에는 예전 리아 친밀 장면 원고가 있다. 비교용으로 남기려면 지우기 전에 그 브랜치의 `Source/game/ria_event_dialogue.json`을 따로 받아 둔다.
- 그다음 GitHub 저장소 **Settings → General → "Automatically delete head branches"**를 켠다.

---

## 1. 챗지피티 — 그림 (총 약 120장)

그림체 기준, 프롬프트 형식, 넘겨줄 때의 규칙은 모두 `Docs/art-prompts-chatgpt-v001.md`를 따른다. 히로인 마스터 PNG를 **매번 첨부**한다. 겨울 외투는 `Docs/art-prompts-winter-v001.md`를 따른다.

### 1-1. 수량 표

| 구분 | 장수 | 세부 | 우선 |
|---|---|---|---|
| 게임용 인물 전신 (의상 × 포즈 3종 × 표정) | 약 100 | `art-prompts-chatgpt-v002.md` A-0, A-0-2. 마스터는 참고용으로만 씀 | P0 |
| 의상 전신 — 사복·생활복 | 8 | 4명 × 2벌 | P0 |
| 의상 전신 — 겨울 외투 | 4 | 4명 × 1벌 (`art-prompts-winter-v001.md`) | P0 |
| 배경 — 기존 목록 | 38 | `art-prompts-chatgpt-v001.md` 4장 (28곳 + 시간대 10) | P0 12 / 나머지 P1~P2 |
| 배경 — 이번에 새로 생긴 장소 | 7 | 아래 1-2 | P1~P2 |
| 장면 CG — 기존 목록 | 34 | `Docs/scene-cg-production-v001.csv` | P1 8 / P2 14 / P3 12 |
| 장면 CG — 이번에 새로 생긴 장면 | 25 | 아래 1-3 | P1~P2 |
| **합계** | **약 220** | 성인 CG 제외 | 최소 출시: 인물 전신 약 100 + 배경 P0 12 + CG P1 약 17 = **약 130장** |

### 1-2. 새 배경 7곳

| ID | 장소 | 시간대 | 쓰는 곳 |
|---|---|---|---|
| bg_train | 기차·지하철 객실 안 | 낮 / 밤 | 지현 R12 기차, 서윤 R07·일정 선택·N02 지하철 |
| bg_laundromat | 동네 코인 세탁방 | 오후 | 리아 특별 장면 1 |
| bg_stair_landing | 회사 계단참 창가 | 낮 12시 반 | 유진 일정 선택(점심), 숨은 이야기 |
| bg_corridor_window | 회사 3층 복도 끝 창문 | 오후 4시 10분 / 겨울 저녁 | 유진 R01, 유진 X02·N02 |
| bg_art_store | 골목 안 오래된 화방 | 저녁 | 유진 R10 |
| bg_bookfair | 독립출판 행사장 부스 | 낮 | 유진 R12 |
| bg_popup_xmas | 철수 중인 팝업 행사장 + 트리 | 밤 | 리아 X01 (기존 bg_popup의 겨울 밤 변형) |

### 1-3. 새 장면 CG 25장

| 우선 | 장면 | 장수 | 위치 |
|---|---|---|---|
| P1 | 프롤로그: 피칭 회의실, 책상 아래 겹친 두 손(얼굴 안 보이게) | 1 | `prologue.rpy` |
| P1 | 크리스마스 진엔딩 대표 장면 (리아 트리 아래 슈슈 / 지현 집 / 유진 첫 정면 그림 / 서윤 두 잔) | 4 | `xmas_scenes.rpy` |
| P2 | 크리스마스 아침(25일) | 4 | 같은 파일 |
| P2 | 진엔딩 1월 장면 X02 (손을 누른 이유를 말하는 장면) | 4 | `xmas_after.rpy` |
| P2 | 특별 장면 | 8 | `special_scenes.rpy` |
| P2 | 숨은 이야기 "이듬해 봄": 옥상 다섯 사람 / 피칭 첫 장 여섯 이름 | 2 | `spring_story.rpy` |
| P3 | 일반 엔딩 1월 장면 N02 | 4 | `xmas_after.rpy` — 배경과 입상으로 대신해도 됨 |
| — | 일정 선택 12장면 | 0 | 배경과 입상으로 처리 |

특별 장면 8장의 내용은 다음과 같다.
- 리아: 코인 세탁방에서 어깨에 기댐 / 밤 옥상의 캔커피
- 지현: 루페로 번진 본드 보기 / 소파에서 잠든 20분
- 유진: 벤치에서 손 스케치 / 노트북 속 뒷모습 그림들
- 서윤: 한밤의 책 읽어 주는 전화 / 휴대폰 맡기기

### 1-4. 그림을 받은 뒤

1. 파일명은 `{인물}_{종류}_{장면}_v001.png` 형식으로 맞춘다.
2. 마스터 옆에 나란히 놓고 `art-prompts-chatgpt-v001.md` 0-1의 통과 기준표로 확인한다.
3. 통과한 그림만 Claude에게 넘겨 게임에 연결한다(이미지 정의, CG 카탈로그, 표정 연결).

---

## 2. Grok — 성인 장면 본문 13곳

대본에는 `(장면 생략 · 시간이 흐릅니다.)`만 들어 있다. 장면별 분위기와 지켜야 할 선은 `Docs/intimate-scene-briefs-v001.md`에 있다.

| 루트 | 파일 | 곳 |
|---|---|---|
| 리아 | `ria_r05_r08.rpy`, `ria_r09_r12.rpy`, `ria_r13_e01.rpy` | 3 |
| 지현 | `jihyun_r05_r12.rpy` | 1 |
| 유진 | `yujin_r05_r08.rpy`, `yujin_r09_r12.rpy`, `yujin_r13_e01.rpy` | 3 |
| 서윤 | `seoyun_r05_r12.rpy` | 1 |
| 크리스마스 진엔딩 | `xmas_scenes.rpy` | 5 |

- 받은 본문은 기존 대본과 같은 형식으로 붙인다(`r "..."`, 리아 대사는 `ri('반말','존댓말')` 두 벌).
- 예전 리아 원고 `ria_event_dialogue.json`(위 0번)은 참고용으로만 쓴다. 지금 루트 흐름과 맞지 않는 부분이 있다.

---

## 3. 작곡가 또는 음원 서비스 — 음악 8곡 + 효과음 8개

지금 들어 있는 소리는 프로그램으로 합성한 임시 음원이다(`Source/tools/make_audio.py`). 판매 전에 바꾸는 것을 권장한다. **파일명만 같으면 코드는 고치지 않아도 된다.**

| 파일 (`Source/game/audio/bgm/`) | 쓰는 곳 | 분위기 |
|---|---|---|
| title.ogg | 타이틀 | 따뜻한 피아노, 퇴근길 노을 |
| office.ogg | 사무실 | 가벼운 업무 리듬 |
| cafe.ogg | 카페·서점·식당 | 어쿠스틱, 잔잔함 |
| evening.ogg | 퇴근길·옥상 | 설렘, 노을 |
| night.ogg | 밤·회식·숙소 | 낮은 템포, 두근거림 |
| home.ogg | 집·작업실 | 포근함 |
| pitch.ogg | 피칭 당일 | 긴장, 상승 |
| ending.ogg | 결말 | 여운 |

효과음(`Source/game/audio/sfx/`)은 hover, click, pick, phone, heart, whoosh, menu, ending 8개다.

- 모두 반복 재생되므로 루프가 이어지게 만든다.
- 음량은 약 −20 LUFS에 맞춘다.
- 형식은 OGG(Vorbis)다.

---

## 4. 직접 할 것 — 출시 준비

1. **마지막 테스트 플레이:** 프롤로그 → 일정 선택 3번 → 루트 하나 → 크리스마스 → 후일담 순서로 한 번, 마음 점수를 일부러 낮게 해서 일반 엔딩으로 한 번 플레이한다. 네 루트를 다 보면 타이틀에 "이듬해 봄"이 생기는지도 확인한다.
2. **진엔딩 난이도:** 너무 쉽거나 어려우면 `xmas_scenes.rpy`의 `XMAS_TRUE_HEART = 8`을 바꾼다. 특별 장면 기준은 `special_scenes.rpy`의 `SPECIAL_HEART`다.
3. **포장 문구** (`Docs/commercial-roadmap-v001.md` 6단계):
   - 부제 후보: 〈퇴근 후, 우리 — 비밀 많은 사무실 연애〉 / 〈퇴근 후, 우리: 연말 피칭까지 60일〉
   - 한 줄 소개: "팀의 운명이 걸린 연말 피칭까지 60일. 그 사이, 네 사람의 비밀과 한 번의 연애."
   - 상점 소개 요점 4개는 로드맵 문서에 있다.
4. **버전 정리:** 게임 이름과 버전 문자열을 1.0.0으로 맞춘다(`options.rpy`).
5. **배포 빌드:** `Docs/Windows_시험판_빌드와검증_v1.md` 절차를 따른다. 검사·도구·생성 기록 파일이 배포판에서 빠지는지 확인한다.

---

## 5. 다음에 Claude에게 맡길 것 (한도가 돌아오면)

- 받은 그림을 게임에 연결하기(입상 표정, 배경, CG 카탈로그, 갤러리)
- Grok 본문을 대본 형식으로 붙이고 검사하기
- 이벤트 장면 화면 실크 디자인(로드맵 6단계)
- 전체 검사 다시 돌리기. 아직 다시 확인하지 않은 것: `three_choice`는 이전부터 10건 실패, `clear_compat`·`ria_expression`은 그림이 들어온 뒤 다시 봐야 함
