# R12 '특별한 날의 옷' 입상 프롬프트 v001

R12 데이트에서 히로인이 "너 만나려고 고른 옷"을 입고 나온다. 지금까지는 사복 입상이 나와서 대사와 화면이 맞지 않았다. 2026-11-23 사용자 결정으로 이 옷의 입상을 새로 만든다.

## 게임 연결 (이미 해 둠)
- 파일을 `Source/game/images/characters/<인물>/<인물>_special_pose01_<표정>.png`로 넣으면, R12 데이트(약속 장소부터 그날 밤까지) 동안 자동으로 이 입상이 나온다. 다음 날 아침에는 원래 옷으로 돌아간다.
- 그림이 없으면 예전처럼 사복이 나온다.
- 성인 이벤트 도입 CG 2·6·9·12번(`intimate-intro-cg-prompts-v002.md`)도 이 옷을 그린다. **입상을 먼저 만들고, 도입 CG는 그 입상을 참고해서 뽑는다.**
- 받은 그림은 검수와 사용자 승인 뒤에 런타임 크기(676×1014)로 넣는다.

## 옷 디자인 (대본 근거)

| 인물 | 옷 | 대본 근거 |
|---|---|---|
| 리아 | 하늘색 오프숄더 니트 미니 원피스(긴소매), 비치는 검정 스타킹, 흰 앵클부츠, 파란 슈슈 | "한 번 더 갈아입을 뻔했거든~" 파란색이 상징색 |
| 지현 | 짙은 와인색 긴소매 랩 미디 원피스(허리 끈), 비치는 검정 스타킹, 검정 앵클부츠, 머리는 내림 | 데이트 내내 소매를 만진다 |
| 유진 | 작은 리본 칼라가 달린 세이지그린 긴소매 니트 원피스(무릎 길이), 비치는 스타킹, 갈색 낮은 굽 앵클부츠, 안경·금색 머리핀 | "오늘 옷도 좀 오래 골랐어요", 옷소매를 내려다봄 |
| 서윤 | 검정 새틴 긴소매 블라우스, 라벤더 하이웨이스트 새틴 미디 스커트, 가터벨트와 검정 레이스 니삭스(치마 아래, 걸을 때 살짝 보임), 검정 펌프스 | "오늘 만나려고 꺼내 입었다는 옷의 소매를 정리했다" |

로퍼·교복풍 요소는 넣지 않는다(외형 기준: 어려 보이는 요소 금지).

## 쓰는 법
1. 새 대화에서 아래 **[0] 그림체 고정**을 붙인다. ChatGPT가 그림체 설명을 하면 "ok".
2. **[1] 기본 전신**을 인물 하나씩 붙인다. 같은 인물은 한 대화에서 계속 만든다.
3. 마음에 드는 기본 전신이 나오면 **[2] 표정 바꾸기**로 7장을 더 뽑는다.
4. 파일 이름: `ria_special_pose01_neutral.png` 처럼 `<인물>_special_pose01_<표정>.png`.

### [0] 그림체 고정
```text
STYLE LOCK — most important rule. Open these reference images first (public GitHub, no login):
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/ria_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/jihyun_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/yujin_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/seoyun_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/ria/ria_casual_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/jihyun/jihyun_casual_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/yujin/yujin_casual_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/seoyun/seoyun_casual_pose01_neutral.png
Reply in text first: could you open each image, and describe the art style (line weight and color, eye shape and highlights, shading, hair rendering). Wait for my "ok".
Then copy that style EXACTLY in every image: thin clean dark-brown outlines, same eye rendering, flat cel shading with one soft shadow tone and small crisp highlights, same face proportions, same hair strands. No reinterpretation, no painterly texture, no 3D, no semi-realism. If anything conflicts, the reference images win.
Adult women 27–32, mature proportions, never childlike. No earrings, necklaces or rings.
```

### [1] 기본 전신 (인물마다 1장)
공통 끝부분([누끼])을 각 블록 뒤에 붙인다.

**ria_special_pose01_neutral.png**
```text
Draw Kang Ria in the SAME standing pose, camera angle and proportions as ria_casual_pose01_neutral.png (one hand raised in a small wave), same face and hair (very long wavy blonde high ponytail, blue scrunchie, straight bangs, blue eyes).
New outfit — her special date outfit: a sky-blue off-shoulder knit mini dress with long sleeves, fitted at the waist, sheer black pantyhose, white ankle boots. Neutral bright closed-mouth smile.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas.
```

**jihyun_special_pose01_neutral.png**
```text
Draw Baek Jihyun in the SAME standing pose, camera angle and proportions as jihyun_casual_pose01_neutral.png (one hand on her hip), same face and hair (very long straight crimson hair falling down her back, side-parted bangs, reddish-brown eyes, sharp eyeliner).
New outfit — her special date outfit: a deep wine-red long-sleeve wrap midi dress tied at the waist, sheer black pantyhose, black heeled ankle boots. Composed, almost expressionless neutral face.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas.
```

**yujin_special_pose01_neutral.png**
```text
Draw Cha Yujin in the SAME standing pose, camera angle and proportions as yujin_casual_pose01_neutral.png, same face and hair (silver-white bob, one gold hairpin, thin round metal glasses, amber eyes, curvy adult figure).
New outfit — her special date outfit: a sage-green knee-length long-sleeve knit dress with a small ribbon collar, sheer pantyhose, brown low-heel ankle boots. No bag. Slightly tense neutral face.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas.
```

**seoyun_special_pose01_neutral.png**
```text
Draw Han Seoyun in the SAME standing pose, camera angle and proportions as seoyun_casual_pose01_neutral.png (one finger near her lips), same face and hair (long wavy dark plum hair, half-lidded grey-lavender eyes, beauty mark under her LEFT eye).
New outfit — her special date outfit: a black satin long-sleeve blouse tucked into a lavender high-waist satin midi skirt, black lace-band thigh-highs with a garter just peeking below the hem, black pumps. Relaxed half-lidded neutral face.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas.
```

**[누끼] — 위 블록 끝에 붙인다**
```text
CUTOUT: TRANSPARENT background, PNG with alpha. Crisp clean outline with no white halo, no fringe, no gray edge, no drop shadow, no ground shadow, no floor line. Every hair strand and loose fabric edge cleanly separated. Nothing else in the image.
```
투명이 안 나오면 `Use a solid pure green #00FF00 background with no shadows`로 바꿔 뽑는다.

### [2] 표정 바꾸기 (방금 만든 기본 전신을 첨부)
```text
Use the attached image as the exact base. Change ONLY the facial expression to: {EXPRESSION}.
Keep everything else pixel-identical: pose, body, outfit, hair, head position and size, line art, colors, canvas size and position.
TRANSPARENT background, clean cutout, no halo, no shadow.
```

| 파일 끝 | 리아 | 지현 | 유진 (안경 유지) | 서윤 |
|---|---|---|---|---|
| `_smile` | wide cheerful smile showing teeth | only the corners of the mouth lifted slightly | shy small smile | teasing playful smile |
| `_laugh` | eyes closed, laughing playfully | trying to hold back a laugh, lips pressed | laughing while covering her mouth with one hand | mischievous laugh as if teasing someone |
| `_blush` | cheeks flushed, looking away shyly | ears turning red, frozen and stiff | eyes cast down, face bright red | the teasing stops, a serious quiet blush |
| `_surprise` | eyes wide, mouth open | eyebrows raised, a brief pause | round eyes behind the glasses | eyes widen slightly |
| `_sad` | drooping brows with a forced small smile | eyes lowered, mouth closed tight | eyes glistening, just before tears | no smile, looking far away |
| `_serious` | no smile, determined look | firm, steady look | brave, direct gaze | no teasing, steady direct gaze |
| `_pout` | puffed cheeks, sulking | sideways look as if arms are crossed | lips pushed out a little | half-closed eyes giving a sidelong glare |

출시 최소: 기본·미소·홍조 3장(인물당). 전부 뽑으면 인물당 8장, 4명 32장.

## 한 번에 끝내는 판 · 그림체 강화 (2026-11-23)

새 대화에서 그림체가 무너지는 문제 때문에 만든 판이다.
- 마스터 4장과 사복 입상 4장을 **직접 첨부**한다. 링크는 예비용이다.
- 첫 그림으로 리아 마스터를 그대로 다시 그리게 해서 그림체를 먼저 맞춘다.
- 그림체 특징을 글로 구체적으로 적었다.
- 프롬프트 본문은 채팅으로 전달했다. 장면·의상 내용은 위의 [1]·[2]와 같다.
