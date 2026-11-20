# PR #25 검수 결과와 다시 뽑기 프롬프트 (2026-11-20)

PR #25(입상 32장 + 장면 CG·타이틀 62장 = 94장)를 한 장씩 봤다. 크기·투명 배경·머리 높이는 모두 기준대로였다. 표정 세트 4묶음도 얼굴만 바뀌고 몸은 같아 문제없었다.

## 1. 결과

| 구분 | 장수 | 처리 |
|---|---:|---|
| 통과 | 75 | 그대로 쓴다. ComfyUI 그림체 통일만 한다 |
| Claude가 고침 | 6 | 유진 생활복 pose02 6장: 머리 주변 뿌연 반투명 테두리를 지워 `_v002`로 저장 |
| 다시 뽑기 | 13 | 아래 2절 |

### 다시 뽑을 것

| 파일 | 문제 |
|---|---|
| `jihyun_r10_scene_v001.png` | 미니어처 집 부품이 아니라 전자 회로 기판이 그려졌다 |
| `jihyun_r16b_scene_v001.png` | 일요일 저녁 카페 앞(사복)이어야 하는데 밤 사무실 복도(업무복)로 그려졌다. R16 엘리베이터 장면과 겹친다 |
| `yujin_r02_scene_v001.png` | 토요일 전시 데이트인데 업무복·사원증 차림이다 |
| `yujin_sp2_scene_v001.png` | 노트북 썸네일이 벗은 등처럼 보인다. 옷 입은 뒷모습 그림이어야 한다 |
| `yujin_x01_scene_v001.png` | 스케치북 뒷면(갈색 표지)이 이쪽을 향한다. 그림이 도현 쪽으로 보여야 한다 |
| `ria_r04_scene_v001.png` | 오른쪽 아래에서 뻗은 도현 팔이 지나치게 길고 뻣뻣하다 |
| `seoyun_x01b_scene_v001.png` | 의자 위 다리 자세가 부자연스럽다 |
| `title_keyvisual_v001.png` | 로고 자리(왼쪽 위 하늘)가 없다. 화면 전체가 인물·건물로 차 있다 |
| `ria_office_pose01_teary_v001.png` | 손 흔드는 밝은 자세에 우는 얼굴. 자세와 감정이 어긋난다 |
| `jihyun_office_pose01_teary_v001.png` | 허리에 손 얹은 당당한 자세에 우는 얼굴 |
| `seoyun_office_pose01_teary_v001.png` | 입술에 손가락 대는 장난스러운 자세에 우는 얼굴 |
| `jihyun_casual_pose01_teary_v001.png` | 허리에 손 얹은 자세에 우는 얼굴 |
| `ria_casual_pose02_teary_v001.png` | 눈물기가 없어 그냥 홍조처럼 보인다 |

참고만 하고 그대로 둔 것
- `ria_x01_scene`: 리아가 정면을 보는데 도현의 두 팔이 오른쪽에서 들어온다. 어색하지만 장면은 읽혀서 남겼다.
- `ria_sp1_scene`: 도현의 어깨·몸통이 보인다. 어깨에 기대는 장면이라 필요하다. 얼굴은 없다.

## 2. Codex에 붙여 넣을 글

```text
kws07042/office-v2 저장소에서 PR #25 그림 중 13장을 다시 만들어 줘.

준비
- git fetch origin claude/heroine-sprites 후 그 브랜치에서 새 브랜치 codex/art-fix-v001 을 만든다.
- 검수 결과와 이유: Docs/art-fix-prompts-v001.md 1절.

공통 규칙
- 화풍 기준: CharacterArt/candidates/heroine-masters-v001/final_2048x3072/ria_office_pose01_neutral_v001.png 를 매번 참고 이미지로 넣는다.
- 인물·의상 기준: Source/game/images/characters/<인물>/ 의 해당 의상 pose01_neutral (리아·서윤 사복 pose02는 CharacterArt/candidates/chatgpt-v001/ 의 최신 버전).
- 장면 CG: 1920x1080, 배경 포함. 도현은 1인칭 시점이고 얼굴·전신은 그리지 않는다. 손·팔만 필요할 때.
- 입상: 1024x1536 투명 PNG. 기준 입상과 캔버스·머리 높이를 똑같이 맞춘다.
- 원본 v001은 지우지 않는다. 새 파일은 _v002, 기존 입상을 기준으로 바꾼 울먹 입상은 아래 이름 그대로.
- 각 폴더 INDEX.md에 파일, 고친 이유, 참고 그림, SHA-256을 적고 비교 사진(원본 v001 / 새 v002) 한 장을 올린다.
- 커밋·푸시하고 PR을 연다.

장면 CG (CharacterArt/candidates/cg-chatgpt-v001/)

1. jihyun_r10_scene_v002.png — 지현 생활복(회색 카디건, 반묶음 머리)
   토요일 오후 지현의 집 거실 탁자. 손바닥만 한 '미니어처 집' 조립 키트(나무 벽판, 작은 창틀, 계단 난간 부품, 본드, 핀셋, 부품 트레이)가 놓여 있다.
   도현의 핀셋에서 작은 나무 부품이 미끄러져 떨어지고, 지현이 그 아래에 손바닥을 받친다. 전자 회로·기판은 절대 넣지 않는다.

2. jihyun_r16b_scene_v002.png — 지현 사복(베이지 트렌치코트, 버건디 니트, 긴 치마)
   일요일 저녁 동네 카페 문 앞 보도. 카페 창 불빛이 따뜻하다. 카페를 막 나와 나란히 선 순간, 지현이 먼저 손을 반쯤 내밀다가 도현의 눈을 본다.
   사무실·엘리베이터·업무복·사원증은 넣지 않는다.

3. yujin_r02_scene_v002.png — 유진 사복(크림 꽈배기 카디건, 칼라 블라우스, 갈색 주름치마, 작은 크로스백, 안경)
   토요일 오후 작은 전시 공간. 유진이 벽의 그림 하나 앞에서 멈춰 서서 손끝으로 그림의 한 부분을 가리키며 도현 쪽을 돌아본다. 사원증은 없다.

4. yujin_sp2_scene_v002.png — 유진 생활복(큰 흰 셔츠, 검은 레깅스)
   일요일 밤 유진의 책상. 유진이 노트북을 도현 쪽으로 민다. 화면에는 연필·수채 스케치 썸네일 여러 장. 전부 '옷을 입은' 한 남자의 뒷모습이다: 셔츠 어깨선, 손목시계 찬 손목, 창가에 앉은 실루엣.
   맨살 등이나 벗은 몸은 하나도 없다. 유진은 긴장해서 셔츠 소매를 쥐고 있다.

5. yujin_x01_scene_v002.png — 유진 생활복
   크리스마스이브 오후 유진의 집 창가. 유진이 스케치북을 두 손으로 들어 '그림 면'을 도현 쪽으로 보여 준다. 그림은 창가 의자에 앉은 남자를 정면에서 그린 연필 스케치(얼굴은 연한 선으로 간략히), 오른쪽 아래에 작은 서명. 낮은 겨울 해가 유진의 옆얼굴에 걸린다. 스케치북 뒷면이 보이면 안 된다.

6. ria_r04_scene_v002.png — 리아 업무복(흰 셔츠, 검은 펜슬 스커트, 사원증)
   금요일 저녁 조명이 켜진 강변 산책길. 고백 직후 리아가 반 걸음 가까이 다가와 고개를 살짝 숙인 채 부드럽게 웃는다. 볼에 홍조.
   도현의 팔·손은 화면에 넣지 않는다.

7. seoyun_x01b_scene_v002.png — 서윤 생활복(연분홍 새틴 파자마)
   크리스마스 다음 날 아침 서윤의 작업실 창가. 서윤이 작업 의자에 옆으로 앉아 두 다리를 가지런히 모아 의자 위로 접어 올리고, 크리스마스 머그를 두 손으로 감싼 채 졸린 눈으로 웃는다. 작업대에 빈 와인 잔 두 개. 자연스러운 앉은 자세.

8. title_keyvisual_v002.png — 네 명 업무복
   v001과 같은 인물 배치(지현 왼쪽 팔짱, 리아 가운데 손 흔들기, 유진 오른쪽 스케치북, 서윤 뒤쪽)를 유지하되 네 명을 화면 오른쪽 2/3 안에 모은다.
   왼쪽 위 1/3은 블루아워 하늘과 먼 도시 불빛만 있는 빈 공간으로 둔다(로고 자리). 글자·로고는 그리지 않는다.

입상 (CharacterArt/candidates/chatgpt-v002/) — 표정은 아래 문장 그대로
TEARY = teary-eyed with clearly visible tears welling along the lower eyelids and a glossy shine in the eyes, inner eyebrows raised, lips pressed together as if holding back crying, faint pink on the nose and cheeks. No tears running down yet.

9.  ria_office_pose03_teary_v001.png — 기준: Source/game/images/characters/ria/ria_office_pose03_neutral.png. 얼굴만 TEARY로.
10. jihyun_office_pose03_teary_v001.png — 기준: Source/game/images/characters/jihyun/jihyun_office_pose03_neutral.png. 얼굴만 TEARY로.
11. seoyun_office_pose03_teary_v001.png — 기준: Source/game/images/characters/seoyun/seoyun_office_pose03_neutral.png. 얼굴만 TEARY로.
12. jihyun_casual_pose02_teary_v001.png — 기준: CharacterArt/candidates/chatgpt-v002/jihyun_casual_pose02_neutral_v001.png. 얼굴만 TEARY로.
13. ria_casual_pose02_teary_v002.png — 기준: CharacterArt/candidates/chatgpt-v001/ria_casual_pose02_neutral 최신 버전. 얼굴만 TEARY로(v001보다 눈물이 분명히 보이게).
    9~13은 기준 입상과 픽셀 단위로 같은 몸·옷·머리·캔버스여야 한다. 얼굴 외에는 아무것도 바꾸지 않는다.
```

## 3. 받은 뒤

- Claude가 다시 검수한다.
- 통과하면 94장 전체를 ComfyUI로 마스터 그림체에 맞춘다(`home-comfyui-checklist.md` 3절).
