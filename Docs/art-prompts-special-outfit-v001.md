# R12 '특별한 날의 옷' 입상 프롬프트 v001

R12 데이트에서 히로인이 "너 만나려고 고른 옷"을 입고 나온다. 지금까지는 사복 입상이 나와서 대사와 화면이 맞지 않았다. 2026-11-23 사용자 결정으로 이 옷의 입상을 새로 만든다.

## 게임 연결 (이미 해 둠)
- 파일을 `Source/game/images/characters/<인물>/<인물>_special_pose01_<표정>.png`로 넣으면, R12 데이트(약속 장소부터 그날 밤까지) 동안 자동으로 이 입상이 나온다. 다음 날 아침에는 원래 옷으로 돌아간다.
- 그림이 없으면 예전처럼 사복이 나온다.
- 성인 이벤트 도입 CG 2·6·9·12번(`intimate-intro-cg-prompts-v002.md`)도 이 옷을 그린다. **입상을 먼저 만들고, 도입 CG는 그 입상을 참고해서 뽑는다.**
- 받은 그림은 검수와 사용자 승인 뒤에 런타임 크기(676×1014)로 넣는다.

## 옷 디자인 (대본 근거)

2026-11-23 사용자 요청으로 '현실적인 실제 데이트 룩'으로 바꾸고, 사용자가 가져온 레퍼런스 5장 중 4장을 인물에 맞췄다(레퍼런스 2: 검정 롱코트+파란 목도리+카디건·셔츠는 리아 겨울옷과 유진 사복에 겹쳐 쓰지 않음)(시기: 피칭 직전 11월 말~12월 초). 네 명 모두 기존 업무복·사복·생활복·겨울옷과 겹치는 옷이 없게 했다. 입상은 코트를 앞을 연 채로 입는다(약속 장소·길 장면). 도입 CG에서는 코트를 의자·옷걸이에 걸어 둔다.

| 인물 | 옷 | 대본 근거 |
|---|---|---|
| 리아 | 아이보리 테디 부클 스탠드카라 하프코트(앞 열림), 안에 연하늘 골지 니트 톱, 검정 플레어 미디스커트, 검정 롱부츠, 작은 검정 숄더백 | 사용자 레퍼런스 1. 밝고 귀여운 분위기, 파란 포인트. 크림 니트+데님 미니(사복), 베이지 코트+파란 목도리(겨울옷)와 겹치지 않음 |
| 지현 | 차콜 롱 울코트(앞 열림), 안에 크림 꽈배기 터틀넥 니트 미니 원피스, 크림 술 목도리, 검정 스타킹, 검정 롱부츠, 작은 갈색 핸드백 | 사용자 레퍼런스 4. 단정하고 우아한 연상. 니트 소매를 만지는 대사와 맞음. 카멜 트렌치+버건디 터틀넥+긴 스커트(사복)와 겹치지 않음 |
| 유진 | 아이보리 시어링 숏재킷(갈색 스웨이드 트림, 앞 열림), 안에 베이지 브이넥 니트, 갈색 글렌체크 A라인 미디스커트, 스타킹, 갈색 낮은 굽 앵클부츠, 안경·금색 머리핀 | 사용자 레퍼런스 3. 포근하고 수줍은 느낌. 원본의 주름 미니 대신 체크 미디로 바꿔 사복(갈색 주름 스커트)과 겹치지 않게 함 |
| 서윤 | 검정 오버사이즈 롱 테일러드 코트(앞 열림), 회색 후드티, 검정 가죽 스트레이트 팬츠, 검정 앵클부츠, 머리 위에 걸친 선글라스 | 사용자 레퍼런스 5. 힘 뺀 시크, 32세의 여유. 이날만 바지라 가터는 안 함. 라벤더 블라우스·회색 니트 원피스와 겹치지 않음 |

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
New outfit — her special date outfit: a ivory teddy-bouclé stand-collar half coat worn open with dark buttons, a light-blue fitted ribbed knit top underneath, black flared midi skirt, black knee-high boots, a small black shoulder bag. Neutral bright closed-mouth smile.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas.
```

**jihyun_special_pose01_neutral.png**
```text
Draw Baek Jihyun in the SAME standing pose, camera angle and proportions as jihyun_casual_pose01_neutral.png (one hand on her hip), same face and hair (very long straight crimson hair falling down her back, side-parted bangs, reddish-brown eyes, sharp eyeliner).
New outfit — her special date outfit: a charcoal long wool coat worn open, a cream cable-knit turtleneck sweater dress (mini length) underneath, cream fringe scarf, sheer black pantyhose, black knee-high boots, a small brown structured handbag. Composed, almost expressionless neutral face.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas.
```

**yujin_special_pose01_neutral.png**
```text
Draw Cha Yujin in the SAME standing pose, camera angle and proportions as yujin_casual_pose01_neutral.png, same face and hair (silver-white bob, one gold hairpin, thin round metal glasses, amber eyes, curvy adult figure).
New outfit — her special date outfit: a ivory shearling short jacket with brown suede trim worn open, a beige V-neck knit sweater with a thin brown line at the neckline, brown glen-check A-line midi skirt, sheer pantyhose, brown low-heel ankle boots. No bag. Slightly tense neutral face.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas.
```

**seoyun_special_pose01_neutral.png**
```text
Draw Han Seoyun in the SAME standing pose, camera angle and proportions as seoyun_casual_pose01_neutral.png (one finger near her lips), same face and hair (long wavy dark plum hair, half-lidded grey-lavender eyes, beauty mark under her LEFT eye).
New outfit — her special date outfit: a black oversized long tailored coat worn open, a grey hoodie, black leather straight-leg pants, black ankle boots, sunglasses pushed up on her head. Relaxed half-lidded neutral face.
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
- 아래가 프롬프트 본문이다(ChatGPT 대화용). Codex에 맡길 때는 [Codex 작업 지시](codex-art-tasks-v001.md)를 쓴다.

```text
You will draw 32 full-body game sprites for an adult office-romance visual novel: 4 heroines x 8 expressions, in a "special date outfit". ONE image per reply. Before each image, write its file name on one line. After each image, wait for me to say "next".

REFERENCES: I attached 8 images — 4 MASTER sprites (office outfit, *_office_pose01_neutral_v001.png) and 4 casual sprites (*_casual_pose01_neutral.png). If any attachment is missing, use these public links:
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/ria_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/jihyun_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/yujin_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/seoyun_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/ria/ria_casual_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/jihyun/jihyun_casual_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/yujin/yujin_casual_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/seoyun/seoyun_casual_pose01_neutral.png

ABSOLUTE STYLE RULE: the MASTER sprites are the only allowed art style. Every image must look like the same artist drew it in the same session. Match these exact traits:
- LINE ART: thin, clean, uniform dark-brown outlines (slightly darker at the outer silhouette), no sketchy, painterly or thick lines.
- EYES: large almond eyes with a thick dark upper lash line ending in a small wing, thin lower lash line, iris gradient from dark at the top to lighter at the bottom, one bright white crescent highlight plus small round white highlights, same eye spacing and size as the masters.
- FACE: small pointed chin, tiny nose drawn with a faint shadow only, small mouth, soft pink blush on the cheeks.
- SHADING: anime cel shading — one soft shadow tone with gentle gradient edges, small crisp highlights; warm, clean, slightly glossy finish.
- HAIR: defined strand clumps with bright white glossy highlight bands near the crown, flowing tips.
- BODY: tall slim adult proportions, about 8 heads tall, long legs, same height and build as each master.
- COLOR: same saturation, warmth and skin tone as the masters.
FORBIDDEN: realistic or semi-realistic rendering, 3D, painterly or watercolor texture, thick outlines, flat vector style, chibi, a different anime style, glow or bloom, redesigned faces, childlike proportions. If anything conflicts, the master images win.
Characters are adult women aged 27–32. No earrings, necklaces or rings.

STEP 0 — before drawing, reply in text only: (a) which references you can see, (b) your description of the master style using the traits above, (c) each heroine's identifying features. Wait for my "ok".
STEP 1 — STYLE TEST: redraw ria_office_pose01_neutral_v001.png as exactly as possible (same outfit, pose and face, transparent background). Wait for my "ok". If I say "again", redraw until it matches the master.
STYLE CHECK: whenever I say "style check", put your last image side by side with the matching master in your mind, list what differs (eyes, lines, shading, proportions) and redraw it.

EVERY SPRITE: full body from the top of the head to the shoes, centered, vertical 2:3 canvas. TRANSPARENT background, PNG with alpha, crisp clean outline, no white halo, no gray edge, no drop shadow, no ground shadow, no floor line, nothing else in the image. (If transparency fails, use a solid pure green #00FF00 background with no shadows.)
EACH HEROINE: image 1 = base (same standing pose, camera angle and proportions as her casual sprite, same face and hair as her master, NEW outfit below, neutral face). Images 2–8 = use image 1 as the exact base and change ONLY the facial expression; keep pose, body, outfit, hair, head position and size, lines, colors and canvas pixel-identical.

HEROINE 1 — KANG RIA (very long wavy blonde high ponytail, blue scrunchie, straight bangs, blue eyes). Pose: one hand raised in a small wave.
Outfit: ivory teddy-bouclé stand-collar half coat worn open with dark buttons, a light-blue fitted ribbed knit top underneath, black flared midi skirt, black knee-high boots, a small black shoulder bag.
ria_special_pose01_neutral.png — bright closed-mouth smile
ria_special_pose01_smile.png — wide cheerful smile showing teeth
ria_special_pose01_blush.png — cheeks flushed, looking away shyly
ria_special_pose01_laugh.png — eyes closed, laughing playfully
ria_special_pose01_surprise.png — eyes wide, mouth open
ria_special_pose01_sad.png — drooping brows with a forced small smile
ria_special_pose01_serious.png — no smile, determined look
ria_special_pose01_pout.png — puffed cheeks, sulking

HEROINE 2 — BAEK JIHYUN (very long straight crimson hair falling down her back, side-parted bangs, reddish-brown eyes, sharp eyeliner). Pose: one hand on her hip.
Outfit: charcoal long wool coat worn open, a cream cable-knit turtleneck sweater dress (mini length) underneath, cream fringe scarf, sheer black pantyhose, black knee-high boots, a small brown structured handbag.
jihyun_special_pose01_neutral.png — composed, almost expressionless
jihyun_special_pose01_smile.png — only the corners of the mouth lifted slightly
jihyun_special_pose01_blush.png — ears turning red, frozen and stiff
jihyun_special_pose01_laugh.png — trying to hold back a laugh, lips pressed
jihyun_special_pose01_surprise.png — eyebrows raised, a brief pause
jihyun_special_pose01_sad.png — eyes lowered, mouth closed tight
jihyun_special_pose01_serious.png — firm, steady look
jihyun_special_pose01_pout.png — sideways look as if arms are crossed

HEROINE 3 — CHA YUJIN (silver-white bob, one gold hairpin, thin round metal glasses always on, amber eyes, curvy adult figure). Pose: same as her casual sprite, no bag.
Outfit: ivory shearling short jacket with brown suede trim worn open, a beige V-neck knit sweater with a thin brown line at the neckline, brown glen-check A-line midi skirt, sheer pantyhose, brown low-heel ankle boots.
yujin_special_pose01_neutral.png — slightly tense default look
yujin_special_pose01_smile.png — shy small smile
yujin_special_pose01_blush.png — eyes cast down, face bright red
yujin_special_pose01_laugh.png — laughing while covering her mouth with one hand
yujin_special_pose01_surprise.png — round eyes behind the glasses
yujin_special_pose01_sad.png — eyes glistening, just before tears
yujin_special_pose01_serious.png — brave, direct gaze
yujin_special_pose01_pout.png — lips pushed out a little

HEROINE 4 — HAN SEOYUN (long wavy dark plum hair, half-lidded grey-lavender eyes, beauty mark under her LEFT eye). Pose: one finger near her lips.
Outfit: black oversized long tailored coat worn open, a grey hoodie, black leather straight-leg pants, black ankle boots, sunglasses pushed up on her head.
seoyun_special_pose01_neutral.png — relaxed, eyes half-lidded
seoyun_special_pose01_smile.png — teasing playful smile
seoyun_special_pose01_blush.png — the teasing stops, a serious quiet blush
seoyun_special_pose01_laugh.png — mischievous laugh as if teasing someone
seoyun_special_pose01_surprise.png — eyes widen slightly
seoyun_special_pose01_sad.png — no smile, looking far away
seoyun_special_pose01_serious.png — no teasing, steady direct gaze
seoyun_special_pose01_pout.png — half-closed eyes giving a sidelong glare

Start with STEP 0.
```
