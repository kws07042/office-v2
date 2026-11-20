# 집에서 ComfyUI로 할 일 (2026-11-20)

PC에서 저장소 폴더를 열고, 아래를 PC의 Claude Code(또는 Codex)에 그대로 붙여 넣으면 된다.

```text
kws07042/office-v2 저장소에서 아래 두 가지를 로컬 ComfyUI로 처리해 줘. 설치·삭제나 ComfyUI 설정 변경은 먼저 나에게 물어볼 것. 이미지는 외부에 올리지 말 것.

0. 준비
   git fetch origin claude/heroine-sprites codex/bg-batch-v001
   git checkout claude/heroine-sprites
   - ComfyUI가 127.0.0.1:8188에서 켜져 있는지 확인.
   - 마스터를 만든 Anima Turbo 1.1 체크포인트, ControlNet lineart(anime)·depth, IP-Adapter, comfyui_controlnet_aux, ComfyUI_IPAdapter_plus가 있는지 확인하고 파일 이름을 알려 줘. 없는 게 있으면 설치하지 말고 보고.
   - 샘플러·스텝·CFG는 마스터 제작 워크플로 값을 그대로 쓴다.

1. 한서윤 사복 입상 그림체 통일 (먼저)
   - 워크플로: img2img + ControlNet lineart 0.85(end 0.8) + depth 0.5 + IP-Adapter style transfer 0.55
     (참조: CharacterArt/candidates/heroine-masters-v001/seoyun_office_pose01_neutral_v001.png), denoise 0.30.
   - 노드 제목: SP_INPUT(Load Image) / SP_POSITIVE(긍정 프롬프트) / SP_SAMPLER(KSampler). API 형식으로 sprite_workflow_api.json 저장(저장소 밖).
   - 값 정하기:
     python Source/tools/comfy_sprite_style.py --workflow <경로>/sprite_workflow_api.json --who seoyun --outfit casual --poses pose01 pose02 --src-version v003 --out-version v004 --folder CharacterArt/candidates/chatgpt-v001 --only-neutral
   - 판정: v003과 겹쳐 옷·손·윤곽이 같고, 선이 진해지고 명암이 2~3단 셀 채색으로 바뀌었으면 성공. 아니면 denoise ±0.04 조정 후 v004 파일을 지우고 다시.
     나란히 비교 이미지(마스터 / v003 / v004)를 만들어 나에게 보여 주고, 좋다고 하면 다음 단계.
   - 전체: 같은 명령에서 --only-neutral 을 빼고 실행(표정 9장. 몸은 neutral 결과, 얼굴만 각 표정).

2. 배경 23장 그림체 통일
   - Docs/backgrounds-title-plan-v001.md 4절 값대로 워크플로를 만들고(노드 제목 BG_INPUT/BG_POSITIVE/BG_SAMPLER) bg_workflow_api.json 저장.
   - 배경 원본 받기: git checkout origin/codex/bg-batch-v001 -- CharacterArt/candidates/bg-chatgpt-v001
   - 사무실 1장 시험: python Source/tools/comfy_batch_backgrounds.py --workflow <경로>/bg_workflow_api.json --input CharacterArt/candidates/bg-chatgpt-v001 --output CharacterArt/candidates/bg-chatgpt-v001 --only bg_office
   - 내가 좋다고 하면 --only 를 빼고 23장 전체.

3. 올리기
   - INDEX.md(두 폴더)에 v004·v003 행 추가: 체크포인트, denoise, SHA-256.
   - claude/heroine-sprites 브랜치에 커밋·푸시. 워크플로 JSON과 ComfyUI 출력 폴더 임시 파일은 커밋하지 말 것. 원본 v001~v003은 지우지 말 것.
```

결과가 올라오면 클라우드 세션에서 검수하고 게임에 연결한다.
