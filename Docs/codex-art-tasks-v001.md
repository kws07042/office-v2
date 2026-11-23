# Codex 그림 작업 지시 v001

ChatGPT 대화용 프롬프트를 Codex에 그대로 넣으면 "ok/next를 기다려라"에서 멈춘다. Codex는 대답을 기다리지 않고 혼자 끝까지 해야 하므로 아래 지시를 쓴다. 저장소를 직접 읽을 수 있어서 그림을 첨부할 필요는 없다.

**순서: 작업 1(데이트 옷 입상)이 끝난 뒤 작업 2(도입 CG)를 맡긴다.** 작업 2의 일부 장면이 작업 1의 입상 옷을 따라 그리기 때문이다.

---

## 작업 1 · R12 데이트 옷 입상 32장

```text
저장소 kws07042/office-v2의 claude/heroine-sprites 브랜치에서 시작해 새 브랜치 codex/special-outfit-v001을 만들어라.

할 일: Docs/art-prompts-special-outfit-v001.md 안의 "한 번에 끝내는 판 · 그림체 강화" 아래 text 블록(32장 입상 프롬프트)을 그대로 따라 그림 32장을 만든다.

대화형 지시는 이렇게 바꿔 적용한다.
- "ok", "next", "again"을 기다리지 말고 끝까지 혼자 진행한다.
- 참고 그림은 링크 대신 저장소 파일을 직접 연다:
  CharacterArt/candidates/heroine-masters-v001/*_office_pose01_neutral_v001.png (마스터, 그림체 최우선)
  Source/game/images/characters/<인물>/<인물>_casual_pose01_neutral.png (자세)
- STEP 0: 마스터 그림체 설명을 STYLE_NOTES.md로 적는다.
- STEP 1 시험 그림: 리아 마스터를 다시 그려 마스터와 비교한다. 눈 모양·하이라이트, 선 굵기·색, 명암, 비율이 다르면 다시 그린다. 통과한 시험 그림은 _style_test.png로 남긴다.
- 매 장마다 마스터와 비교해 다르면 다시 그린다(STYLE CHECK를 스스로 한다).
- 한 인물의 표정 7장은 그 인물의 neutral 그림을 바탕으로 표정만 바꾼다.

저장:
- CharacterArt/candidates/special-outfit-v001/ 에 프롬프트에 적힌 파일 이름 그대로 저장(투명 PNG, 세로 2:3, 머리~신발 전신).
- 같은 폴더에 INDEX.md: 파일 이름, 인물, 표정, 참고한 마스터 파일, 다시 그린 횟수, 남은 문제(있으면).

지키는 것:
- Source/game/ 아래는 건드리지 않는다. 게임 연결과 승인 등록은 하지 않는다(사용자 검수 뒤에 한다).
- 성인 여성(27~32세) 체형, 어려 보이는 비율 금지, 귀걸이·목걸이·반지 금지.
- 끝나면 커밋하고 브랜치를 올린 뒤, 다 못 만든 그림이 있으면 그 목록을 남긴다.
```

---

## 작업 2 · 성인 이벤트 도입 CG 25장

```text
저장소 kws07042/office-v2의 codex/special-outfit-v001 브랜치(작업 1 결과)에서 시작해 새 브랜치 codex/intro-cgs-v002를 만들어라. 작업 1 브랜치가 없으면 claude/heroine-sprites에서 시작한다.

할 일: Docs/intimate-intro-cg-prompts-v003.md 안의 text 블록(25장 도입 CG 프롬프트)을 그대로 따라 그림 25장을 만든다. 속옷 취향은 CharacterArt/character_art_09_INTIMATE_WEAR.md를 따른다.

대화형 지시는 이렇게 바꿔 적용한다.
- "ok", "next", "again"을 기다리지 말고 끝까지 혼자 진행한다.
- 참고 그림은 저장소 파일을 직접 연다:
  마스터 CharacterArt/candidates/heroine-masters-v001/*_office_pose01_neutral_v001.png (그림체 최우선)
  의상 Source/game/images/characters/<인물>/<인물>_<casual|home>_pose01_neutral.png
  데이트 옷 CharacterArt/candidates/special-outfit-v001/<인물>_special_pose01_neutral.png (2·6·9·12번)
- STEP 0: 그림체 설명을 STYLE_NOTES.md로 적는다.
- STEP 1 시험 그림: 리아 마스터를 다시 그려 비교하고, 다르면 다시 그린다. _style_test.png로 남긴다.
- 매 장마다 마스터와 비교하고(STYLE CHECK), 원근 규칙(카메라 눈높이 1.4m, 침대 높이가 무릎, 엉덩이·발 닿는 곳과 그림자, 다리를 카메라 쪽으로 뻗지 않기)을 확인한다. 어긋나면 다시 그린다.
- 같은 히로인의 방은 처음 그린 방을 계속 쓴다.

저장:
- CharacterArt/candidates/intro-cgs-v002/ 에 Docs/intimate-intro-cg-prompts-v002.md의 파일 이름 표대로 저장(01_ria_r07_casual_intro.png ~ 25_seoyun_r15_police_intro.png), 1920x1080 PNG.
- 같은 폴더에 INDEX.md: 번호, 파일, 장면, 참고 파일, 다시 그린 횟수, 남은 문제.

지키는 것:
- 노출 한도: 속옷은 다 가리고 비치지 않음. 나체·유두·성행위·노골적 자세 금지. 코스프레는 몸을 다 가리는 성인 의상, 학생풍 금지.
- Source/game/ 아래는 건드리지 않는다. 게임 연결과 승인 등록은 하지 않는다.
- 끝나면 커밋하고 브랜치를 올린 뒤, 못 만든 장면이 있으면 그 목록과 이유를 남긴다.
```
