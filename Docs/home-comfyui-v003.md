# 집에서 ComfyUI v003 다시 돌리기 (2026-11-22)

v002(PR #33)는 기술 검사는 통과했지만 선이 마스터보다 옅어지고, 입·코가 반실사로, CG 배경이 뭉개져 게임에 넣지 않았다(`Docs/unified-v002-review.md`).
아래를 PC의 Claude Code에 그대로 붙여 넣는다.

```text
kws07042/office-v2 저장소에서 ComfyUI 그림체 통일을 v003으로 다시 해 줘. 지난번(unified-v002)에 쓴 저장소 밖 스크립트(Documents/ComfyStyleUnify/unify_v2.py, unify_cg.py)를 고쳐 쓴다.
설치·삭제나 ComfyUI 설정 변경은 먼저 나에게 물어볼 것. 이미지는 외부에 올리지 말 것.

0. 준비
   git fetch origin claude/heroine-sprites && git checkout claude/heroine-sprites && git pull
   읽을 것: Docs/unified-v002-review.md (왜 탈락했는지)

1. 바꿀 설정
   입상
   - 1차 강도(denoise) 0.50 → 0.34 (뾰로통 0.30). 선화 고정 1.0 유지.
   - 마스터 IP-Adapter 0.55 → 0.75.
   - 2차 얼굴: 강도 0.45 → 0.32, 원본 선화 0.8 → 1.0(끝 80%까지).
   - negative에 추가: realistic lips, lip shading, nose shadow, semi-realistic, soft lineart, faded lines, blurry
   - positive에 추가: thick dark lineart, bold eyelashes, simple line mouth
   장면 CG
   - 인물만 다시 그린다. 인물 마스크(사람 분할 모델, 머리카락 포함, 12px 넓히고 8px 흐림)로 결과 인물과 원본 배경을 합친다. 배경은 원본 픽셀 그대로.
   - 인물 강도 0.45 → 0.34, 얼굴 2차는 입상과 같은 값.
   - 메뉴판·화면·스케치북·서류 속 그림은 원본에서 되붙인다(지난번 Fix 6장 원인).
   공통
   - 서윤 눈 밑 점은 화면 오른쪽 눈 아래 하나만. 결과에 반대쪽 점이 생기면 원본 얼굴 그 부분을 되붙인다.

2. 시험 6장 (unified-v003 폴더, 결과 이름 _v301.png)
   - chatgpt-v001/ria_office_pose01_neutral_v003.png, chatgpt-v001/yujin_casual_pose01_neutral_v003.png,
     chatgpt-v001/jihyun_home_pose01_neutral_v003.png, chatgpt-v001/seoyun_casual_pose01_neutral_v003.png,
     cg-chatgpt-v001/ria_x01_scene_v004.png, cg-chatgpt-v001/seoyun_r16_scene_v002.png
     (각 폴더의 최신 버전 기준. 원본 경로는 Docs/unify-list-v001.txt 와 같은 규칙)
   - INDEX.md를 v002와 같은 형식(| `결과` | `원본` | ...)으로 적고 검사:
     python Source/tools/unify_postcheck.py check --index CharacterArt/candidates/unified-v003/INDEX.md
     6장 모두 PASS여야 한다. FAIL이면 강도를 0.04 더 낮추거나, 선 되얹기를 쓴다:
     python Source/tools/unify_postcheck.py lines --index CharacterArt/candidates/unified-v003/INDEX.md --strength 0.8
     (결과 옆에 _lines.png가 생긴다. 이걸 쓰기로 하면 그 파일을 _v301.png로 바꾼다.)
   - 마스터(heroine-masters-v001/final_2048x3072/<인물>_office_pose01_neutral_v001.png) / 원본 / 결과를 나란히 놓은 비교 이미지와
     얼굴 확대 비교 이미지를 만들어 보여 줘. 기준: 속눈썹·윤곽선이 마스터만큼 진하고, 입은 선 하나, 코는 점이나 짧은 선, CG 배경은 원본과 같음.
   - 내가 좋다고 하면 3단계.

3. 전체 250장
   Docs/unify-list-v001.txt 에서 bg-chatgpt-v001(배경 23장)만 빼고 전부. 결과는 unified-v003/<원래 폴더>/<이름>_v301.png.
   같은 포즈 표정은 neutral 몸 + 표정 얼굴(지난번과 같음). 끝나면 check 를 다시 돌려 FAIL 0장이어야 한다.
   폴더별 비교 사진(원본 / 결과) 한 장씩.

4. 올리기
   unified-v003/INDEX.md(파일, 원본, 강도, 판정, SHA-256), 새 브랜치 art/unified-v003 에 커밋·푸시하고 PR.
   워크플로 JSON·임시 파일은 커밋하지 않는다. 원본과 unified-v002는 지우지 않는다.
```

결과 PR이 올라오면 클라우드 세션에서 같은 기준(선 비율, 얼굴 확대, CG 배경)으로 검수하고 통과분을 게임에 교체한다.
