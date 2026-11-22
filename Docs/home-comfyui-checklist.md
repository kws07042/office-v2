# 집에서 ComfyUI로 할 일 (2026-11-20 개정)

PC에서 저장소 폴더를 열고, 아래를 PC의 Claude Code(또는 Codex)에 그대로 붙여 넣는다.
예전 1·2단계(서윤 v004, 배경 v003 따로 돌리기)는 아래 한 번에 포함되어 없앴다.

```text
kws07042/office-v2 저장소의 ChatGPT 그림 273장을 로컬 ComfyUI로 마스터 그림체에 맞춰 줘.
설치·삭제나 ComfyUI 설정 변경은 먼저 나에게 물어볼 것. 이미지는 외부에 올리지 말 것.

1. 준비
   git fetch origin claude/heroine-sprites
   git checkout claude/heroine-sprites
   git pull
   - ComfyUI가 127.0.0.1:8188에서 켜져 있는지 확인.
   - 마스터를 만든 Anima Turbo 1.1 체크포인트, ControlNet lineart(anime)·depth 모델,
     IP-Adapter(PLUS), 커스텀 노드 comfyui_controlnet_aux·ComfyUI_IPAdapter_plus가 있는지 확인하고 파일 이름을 알려 줘.
     없는 게 있으면 설치하지 말고 보고. 체크포인트가 SDXL 계열이 아니면 IP-Adapter가 안 맞으니 실행하지 말고 알려 줘.

2. 워크플로
   - Source/tools/comfyui/master_style_api.json 을 ComfyUI에 불러온다.
   - CKPT·CN_LINEART·CN_DEPTH 노드의 CHANGE_ME 를 내 PC 모델 파일로 바꾸고,
     SAMPLER 노드의 steps·cfg·sampler·scheduler를 마스터 제작 워크플로 값으로 바꾼다(denoise·seed는 스크립트가 넣음).
   - Workflow → Export (API) 로 저장소 밖에 my_master_style_api.json 으로 저장.

3. 시험 (각 1장)
   python Source/tools/comfy_style_unify.py --workflow <경로>/my_master_style_api.json --files "CharacterArt/candidates/cg-chatgpt-v001/ria_r07_scene_v002.png" "CharacterArt/candidates/chatgpt-v002/jihyun_casual_pose02_neutral_v001.png" "CharacterArt/candidates/bg-chatgpt-v001/bg_office_day_v004.png" --out-dir CharacterArt/candidates/unified-v001 --out-version v101
   - 마스터(CharacterArt/candidates/heroine-masters-v001/final_2048x3072/ria_office_pose01_neutral_v001.png) / 원본 / 결과를 나란히 놓은 비교 이미지를 만들어 보여 줘.
   - 성공 기준: 구도·옷·얼굴·손은 원본 그대로, 선 굵기·눈 그리는 법·2단 셀 채색은 마스터와 같음.
   - 구도나 얼굴이 바뀌면 --denoise 를 0.04씩 낮추고, 그림체가 덜 바뀌면 --style-weight 를 0.95까지 올린다.
     다시 할 때는 unified-v001 안의 해당 결과 파일을 지우고 같은 명령. 정한 값을 알려 줘.
   - 내가 좋다고 하면 4단계.

4. 전체 273장
   python Source/tools/comfy_style_unify.py --workflow <경로>/my_master_style_api.json --list Docs/unify-list-v001.txt --out-dir CharacterArt/candidates/unified-v001 --out-version v101  (3단계에서 정한 --denoise·--style-weight 도 붙인다)
   - 입상 188장(투명 유지, 같은 포즈 표정은 neutral 몸 + 각 표정 얼굴), 장면 CG·타이틀 62장, 배경 23장.
   - 끊기면 같은 명령을 다시 실행(이미 만든 파일은 건너뜀).
   - 끝나면 폴더별 비교 사진(원본 / 결과) 한 장씩 만든다.

5. 올리기
   - CharacterArt/candidates/unified-v001/INDEX.md 에 파일, 원본 경로, 체크포인트 이름, denoise, style weight, SHA-256.
   - 새 브랜치 comfy/unified-v001 에 커밋·푸시하고 PR을 연다.
   - 워크플로 JSON, ComfyUI output 폴더 임시 파일은 커밋하지 않는다. 원본은 지우지 않는다.
```

결과 PR이 올라오면 클라우드 세션에서 검수하고 게임에 연결한다.
