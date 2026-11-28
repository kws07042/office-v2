# 제미나이 입상 태스크 · 히로인별 16장 v001

전체 대사에서 히로인이 말하는 줄을 모두 세었어요. 줄마다 게임이 고르는 의상(장소 기준)과 표정(대사 내용 기준)을 계산해서, 많이 쓰이는 조합부터 16장을 골랐어요.

| 히로인 | 대사 수 | 의상 / 표정 쓰임 (줄 수) |
|---|---|---|
| 강리아 | 612 | 업무복 305 · 사복 176 · 생활복 113 / 보통 274 · 웃음 246 · 진지 32 · 놀람 27 · 수줍 21 · 슬픔 9 |
| 백지현 | 582 | 업무복 359 · 생활복 123 · 사복 91 / 보통 394 · 진지 87 · 웃음 56 · 놀람 18 · 수줍 15 · 슬픔 9 |
| 차유진 | 510 | 업무복 275 · 사복 146 · 생활복 89 / 보통 307 · 웃음 107 · 진지 42 · 수줍 37 · 슬픔 13 · 놀람 2 |
| 한서윤 | 536 | 업무복 316 · 사복 206 · 생활복 6 / 보통 314 · 웃음 123 · 진지 38 · 놀람 24 · 수줍 24 · 슬픔 9 |

**16장으로 정한 구성**
- 업무복 8장: 기본 포즈 6표정, 두 번째 포즈 2표정
- 사복 5장
- 생활복 3장 (서윤은 생활복이 6줄뿐이라 사복 두 번째 포즈 3장으로 바꿈)

겨울옷(리아 18줄 등)과 R12 데이트 옷은 쓰임이 적어서 이번 16장에서 뺐어요. 필요하면 다음에 따로 뽑아요. 그 전까지는 지금 입상이 그대로 나와요.

## 사용법
1. 제미나이 설정은 **Pro 이미지 모델, 세로 2:3, 고해상도(2K가 되면 2K)**예요.
2. 그 히로인의 **마스터 입상 한 장**만 올려요. `CharacterArt/candidates/heroine-masters-v001/final_2048x3072/` 안에 있는 파일이에요.
3. 블록을 통째로 붙여 넣어요. 한 번에 다 안 나오면 `Continue with IMAGE n.`이라고 보내요.
4. 다 받으면 파일 이름 그대로 저장해서 올려 주세요. 초록 배경 빼기, 키 맞추기, WebP 변환, 게임 연결은 제가 해요.
5. 다시 시킬 때 쓰는 말:
   - 크기·위치가 다를 때: `Redo IMAGE n with exactly the same framing as IMAGE 1: same height, head top and shoe position.`
   - 얼굴이 달라졌을 때: `Redo IMAGE n. Her face must match the attached master exactly.`
   - 사원증에 글자가 생겼을 때: `Redo IMAGE n with a blank ID card, no letters.`
   - 배경이 초록 단색이 아닐 때: `Redo IMAGE n on a flat pure #00FF00 background.`

**규칙 요약**
- 배경은 크로마키 초록 단색이에요. 투명 배경을 만들기 쉽게 하려는 거라 초록 옷이나 초록 조명은 금지했어요.
- 16장 모두 같은 크기와 같은 위치예요. 머리끝 위와 신발 아래에 여백을 두었어요.
- 사원증은 글자 없는 빈 카드예요.
- 업스케일은 하지 말아요.

---

## 강리아 (마스터: `ria_office_pose01_neutral_v001.png`)

| # | 의상·포즈 | 표정 | 파일 이름 |
|---|---|---|---|
| 1 | 업무복 pose01 | 보통 | ria_office_pose01_neutral.png |
| 2 | 업무복 pose01 | 웃음 | ria_office_pose01_smile.png |
| 3 | 업무복 pose01 | 진지 | ria_office_pose01_serious.png |
| 4 | 업무복 pose01 | 수줍 | ria_office_pose01_blush.png |
| 5 | 업무복 pose01 | 놀람 | ria_office_pose01_surprise.png |
| 6 | 업무복 pose01 | 슬픔 | ria_office_pose01_sad.png |
| 7 | 업무복 pose02 | 웃음 | ria_office_pose02_smile.png |
| 8 | 업무복 pose02 | 크게 웃음 | ria_office_pose02_laugh.png |
| 9 | 사복 pose01 | 보통 | ria_casual_pose01_neutral.png |
| 10 | 사복 pose01 | 웃음 | ria_casual_pose01_smile.png |
| 11 | 사복 pose01 | 수줍 | ria_casual_pose01_blush.png |
| 12 | 사복 pose01 | 놀람 | ria_casual_pose01_surprise.png |
| 13 | 사복 pose01 | 슬픔 | ria_casual_pose01_sad.png |
| 14 | 생활복 pose01 | 보통 | ria_home_pose01_neutral.png |
| 15 | 생활복 pose01 | 웃음 | ria_home_pose01_smile.png |
| 16 | 생활복 pose01 | 수줍 | ria_home_pose01_blush.png |

```text
Create 16 separate character sprite images of the same woman, one image per item below, in order. Label each image with its number and file name. Do not merge images into a sheet. Do not skip any.

REFERENCE: the attached master sprite is the ONLY reference for her face, hair, eye color, body proportions, height and drawing style. Every image must look like the same person drawn by the same artist.

CHARACTER: Kang Ria, adult woman (28), cheerful event-planning team member. Slim face, very long wavy honey-blonde hair in a HIGH PONYTAIL tied with a BLUE SCRUNCHIE, straight blunt bangs, bright BLUE eyes, bright friendly mouth. Same height, body proportions and face as the master.

ART STYLE LOCK (absolute): exactly the master's anime visual-novel style — same clean line weight, flat cel shading with soft gradients, same coloring and skin tone, same eye shape, same highlights. Do not make her younger, rounder or chibi. Adult proportions.

SPRITE FORMAT (identical in all 16 images):
- Portrait 2:3, high resolution (at least 1024x1536, 2K if available). Do NOT upscale or redraw afterwards.
- FULL BODY, head to shoes, standing, facing the viewer at a slight 3/4 angle, camera at chest height, no perspective distortion.
- Same scale and position in every image: the top of her hair about 4% below the top edge, the soles of her shoes about 3% above the bottom edge, body centered horizontally. Never crop the hair, ponytail, hair ornaments, hands or shoes.
- Background: flat solid pure chroma green #00FF00, completely uniform, no floor, no shadow on the ground, no gradient, no green light spill on her. Nothing she wears may be green.
- No text, no letters, no logo, no watermark anywhere. The ID card is blank.
- Arms and hands must not overlap her face. Clean, separated silhouette edges for easy background removal.

OUTFITS (keep exactly the same in every image that uses them):
- OFFICE: opaque white cotton collared blouse with sleeves rolled up, black high-waist pencil skirt, sheer black pantyhose, black patent pumps, navy lanyard with a BLANK light plastic ID card holder (no text).
- CASUAL: cream cable-knit cropped sweater, blue denim mini skirt, sheer black tights, white sneakers. Ponytail and blue scrunchie stay.
- HOME: oversized white hoodie, light grey lounge shorts, bare legs, grey fluffy slippers. Ponytail and blue scrunchie stay.

IMAGES:
IMAGE 1 — ria_office_pose01_neutral.png
Outfit: OFFICE. Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: calm pleasant face, mouth softly closed.

IMAGE 2 — ria_office_pose01_smile.png
Outfit: OFFICE. Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: big bright smile, eyes slightly curved.

IMAGE 3 — ria_office_pose01_serious.png
Outfit: OFFICE. Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: focused work face, small frown, lips pressed.

IMAGE 4 — ria_office_pose01_blush.png
Outfit: OFFICE. Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: shy smile, cheeks clearly pink, eyes glancing aside.

IMAGE 5 — ria_office_pose01_surprise.png
Outfit: OFFICE. Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: eyes wide, small round open mouth, eyebrows up.

IMAGE 6 — ria_office_pose01_sad.png
Outfit: OFFICE. Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: eyebrows tilted up, eyes lowered, small sad mouth, no tears.

IMAGE 7 — ria_office_pose02_smile.png
Outfit: OFFICE. Pose: one hand raised at shoulder height in a small friendly wave, the other hand holding a clipboard at her hip. Expression: big bright smile, eyes slightly curved.

IMAGE 8 — ria_office_pose02_laugh.png
Outfit: OFFICE. Pose: one hand raised at shoulder height in a small friendly wave, the other hand holding a clipboard at her hip. Expression: laughing openly, eyes squeezed into happy arcs, mouth wide open.

IMAGE 9 — ria_casual_pose01_neutral.png
Outfit: CASUAL. Pose: one hand raised beside her face in a small wave, the other relaxed at her side. Expression: calm pleasant face, mouth softly closed.

IMAGE 10 — ria_casual_pose01_smile.png
Outfit: CASUAL. Pose: one hand raised beside her face in a small wave, the other relaxed at her side. Expression: big bright smile, eyes slightly curved.

IMAGE 11 — ria_casual_pose01_blush.png
Outfit: CASUAL. Pose: one hand raised beside her face in a small wave, the other relaxed at her side. Expression: shy smile, cheeks clearly pink, eyes glancing aside.

IMAGE 12 — ria_casual_pose01_surprise.png
Outfit: CASUAL. Pose: one hand raised beside her face in a small wave, the other relaxed at her side. Expression: eyes wide, small round open mouth, eyebrows up.

IMAGE 13 — ria_casual_pose01_sad.png
Outfit: CASUAL. Pose: one hand raised beside her face in a small wave, the other relaxed at her side. Expression: eyebrows tilted up, eyes lowered, small sad mouth, no tears.

IMAGE 14 — ria_home_pose01_neutral.png
Outfit: HOME. Pose: hands tucked into the hoodie front pocket, relaxed stance. Expression: calm pleasant face, mouth softly closed.

IMAGE 15 — ria_home_pose01_smile.png
Outfit: HOME. Pose: hands tucked into the hoodie front pocket, relaxed stance. Expression: big bright smile, eyes slightly curved.

IMAGE 16 — ria_home_pose01_blush.png
Outfit: HOME. Pose: hands tucked into the hoodie front pocket, relaxed stance. Expression: shy smile, cheeks clearly pink, eyes glancing aside.
```

---

## 백지현 (마스터: `jihyun_office_pose01_neutral_v001.png`)

| # | 의상·포즈 | 표정 | 파일 이름 |
|---|---|---|---|
| 1 | 업무복 pose01 | 보통 | jihyun_office_pose01_neutral.png |
| 2 | 업무복 pose01 | 진지 | jihyun_office_pose01_serious.png |
| 3 | 업무복 pose01 | 웃음 | jihyun_office_pose01_smile.png |
| 4 | 업무복 pose01 | 수줍 | jihyun_office_pose01_blush.png |
| 5 | 업무복 pose01 | 놀람 | jihyun_office_pose01_surprise.png |
| 6 | 업무복 pose01 | 슬픔 | jihyun_office_pose01_sad.png |
| 7 | 업무복 pose02 | 보통 | jihyun_office_pose02_neutral.png |
| 8 | 업무복 pose02 | 진지 | jihyun_office_pose02_serious.png |
| 9 | 사복 pose01 | 보통 | jihyun_casual_pose01_neutral.png |
| 10 | 사복 pose01 | 웃음 | jihyun_casual_pose01_smile.png |
| 11 | 사복 pose01 | 수줍 | jihyun_casual_pose01_blush.png |
| 12 | 사복 pose01 | 진지 | jihyun_casual_pose01_serious.png |
| 13 | 사복 pose01 | 슬픔 | jihyun_casual_pose01_sad.png |
| 14 | 생활복 pose01 | 보통 | jihyun_home_pose01_neutral.png |
| 15 | 생활복 pose01 | 웃음 | jihyun_home_pose01_smile.png |
| 16 | 생활복 pose01 | 수줍 | jihyun_home_pose01_blush.png |

```text
Create 16 separate character sprite images of the same woman, one image per item below, in order. Label each image with its number and file name. Do not merge images into a sheet. Do not skip any.

REFERENCE: the attached master sprite is the ONLY reference for her face, hair, eye color, body proportions, height and drawing style. Every image must look like the same person drawn by the same artist.

CHARACTER: Baek Jihyun, adult woman (30), composed team leader. Very long CRIMSON hair falling straight down her shoulders and back (not spreading outward), slight wave only at the ends, glossy crown, side-parted bangs, sharp RED-BROWN eyes with clear eyeliner, confident gaze, NO beauty mark. Same height, body proportions and face as the master.

ART STYLE LOCK (absolute): exactly the master's anime visual-novel style — same clean line weight, flat cel shading with soft gradients, same coloring and skin tone, same eye shape, same highlights. Do not make her younger, rounder or chibi. Adult proportions.

SPRITE FORMAT (identical in all 16 images):
- Portrait 2:3, high resolution (at least 1024x1536, 2K if available). Do NOT upscale or redraw afterwards.
- FULL BODY, head to shoes, standing, facing the viewer at a slight 3/4 angle, camera at chest height, no perspective distortion.
- Same scale and position in every image: the top of her hair about 4% below the top edge, the soles of her shoes about 3% above the bottom edge, body centered horizontally. Never crop the hair, ponytail, hair ornaments, hands or shoes.
- Background: flat solid pure chroma green #00FF00, completely uniform, no floor, no shadow on the ground, no gradient, no green light spill on her. Nothing she wears may be green.
- No text, no letters, no logo, no watermark anywhere. The ID card is blank.
- Arms and hands must not overlap her face. Clean, separated silhouette edges for easy background removal.

OUTFITS (keep exactly the same in every image that uses them):
- OFFICE: burgundy shirt, charcoal tailored jacket, charcoal-black high-waist pencil skirt, sheer black pantyhose, black pumps, navy lanyard with a BLANK light plastic ID card holder (no text).
- CASUAL: long camel trench coat open over a burgundy turtleneck knit, long dark plum maxi skirt, brown lace-up ankle boots.
- HOME: soft grey-mauve knit cardigan over a light top, matching wide lounge pants, cream slippers, hair loosely tied half-up.

IMAGES:
IMAGE 1 — jihyun_office_pose01_neutral.png
Outfit: OFFICE. Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: calm composed face, mouth closed.

IMAGE 2 — jihyun_office_pose01_serious.png
Outfit: OFFICE. Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: stern focused face, eyebrows drawn together, lips pressed.

IMAGE 3 — jihyun_office_pose01_smile.png
Outfit: OFFICE. Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: small restrained smile, eyes softened.

IMAGE 4 — jihyun_office_pose01_blush.png
Outfit: OFFICE. Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: embarrassed face trying to stay composed, cheeks pink, eyes looking away.

IMAGE 5 — jihyun_office_pose01_surprise.png
Outfit: OFFICE. Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: eyes widened, lips parted, eyebrows up.

IMAGE 6 — jihyun_office_pose01_sad.png
Outfit: OFFICE. Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: tired sad face, eyes lowered, eyebrows tilted, no tears.

IMAGE 7 — jihyun_office_pose02_neutral.png
Outfit: OFFICE. Pose: holding a tablet against her chest with one arm, the other hand lightly touching her jacket lapel. Expression: calm composed face, mouth closed.

IMAGE 8 — jihyun_office_pose02_serious.png
Outfit: OFFICE. Pose: holding a tablet against her chest with one arm, the other hand lightly touching her jacket lapel. Expression: stern focused face, eyebrows drawn together, lips pressed.

IMAGE 9 — jihyun_casual_pose01_neutral.png
Outfit: CASUAL. Pose: one hand in the trench coat pocket, the other holding the strap of a small leather bag. Expression: calm composed face, mouth closed.

IMAGE 10 — jihyun_casual_pose01_smile.png
Outfit: CASUAL. Pose: one hand in the trench coat pocket, the other holding the strap of a small leather bag. Expression: small restrained smile, eyes softened.

IMAGE 11 — jihyun_casual_pose01_blush.png
Outfit: CASUAL. Pose: one hand in the trench coat pocket, the other holding the strap of a small leather bag. Expression: embarrassed face trying to stay composed, cheeks pink, eyes looking away.

IMAGE 12 — jihyun_casual_pose01_serious.png
Outfit: CASUAL. Pose: one hand in the trench coat pocket, the other holding the strap of a small leather bag. Expression: stern focused face, eyebrows drawn together, lips pressed.

IMAGE 13 — jihyun_casual_pose01_sad.png
Outfit: CASUAL. Pose: one hand in the trench coat pocket, the other holding the strap of a small leather bag. Expression: tired sad face, eyes lowered, eyebrows tilted, no tears.

IMAGE 14 — jihyun_home_pose01_neutral.png
Outfit: HOME. Pose: arms loosely folded over the cardigan, relaxed weight on one leg. Expression: calm composed face, mouth closed.

IMAGE 15 — jihyun_home_pose01_smile.png
Outfit: HOME. Pose: arms loosely folded over the cardigan, relaxed weight on one leg. Expression: small restrained smile, eyes softened.

IMAGE 16 — jihyun_home_pose01_blush.png
Outfit: HOME. Pose: arms loosely folded over the cardigan, relaxed weight on one leg. Expression: embarrassed face trying to stay composed, cheeks pink, eyes looking away.
```

---

## 차유진 (마스터: `yujin_office_pose01_neutral_v001.png`)

| # | 의상·포즈 | 표정 | 파일 이름 |
|---|---|---|---|
| 1 | 업무복 pose01 | 보통 | yujin_office_pose01_neutral.png |
| 2 | 업무복 pose01 | 웃음 | yujin_office_pose01_smile.png |
| 3 | 업무복 pose01 | 진지 | yujin_office_pose01_serious.png |
| 4 | 업무복 pose01 | 수줍 | yujin_office_pose01_blush.png |
| 5 | 업무복 pose01 | 슬픔 | yujin_office_pose01_sad.png |
| 6 | 업무복 pose01 | 놀람 | yujin_office_pose01_surprise.png |
| 7 | 업무복 pose02 | 보통 | yujin_office_pose02_neutral.png |
| 8 | 업무복 pose02 | 진지 | yujin_office_pose02_serious.png |
| 9 | 사복 pose01 | 보통 | yujin_casual_pose01_neutral.png |
| 10 | 사복 pose01 | 웃음 | yujin_casual_pose01_smile.png |
| 11 | 사복 pose01 | 수줍 | yujin_casual_pose01_blush.png |
| 12 | 사복 pose01 | 슬픔 | yujin_casual_pose01_sad.png |
| 13 | 사복 pose01 | 진지 | yujin_casual_pose01_serious.png |
| 14 | 생활복 pose01 | 보통 | yujin_home_pose01_neutral.png |
| 15 | 생활복 pose01 | 웃음 | yujin_home_pose01_smile.png |
| 16 | 생활복 pose01 | 수줍 | yujin_home_pose01_blush.png |

```text
Create 16 separate character sprite images of the same woman, one image per item below, in order. Label each image with its number and file name. Do not merge images into a sheet. Do not skip any.

REFERENCE: the attached master sprite is the ONLY reference for her face, hair, eye color, body proportions, height and drawing style. Every image must look like the same person drawn by the same artist.

CHARACTER: Cha Yujin, adult woman (27), quiet brand designer. SILVER-WHITE bob (front slightly longer, straight), side-swept bangs, one GOLD HAIRPIN on one side, thin ROUND metal-frame GLASSES, amber-brown eyes, calm gentle face, mature curvy figure. Same height, body proportions and face as the master.

ART STYLE LOCK (absolute): exactly the master's anime visual-novel style — same clean line weight, flat cel shading with soft gradients, same coloring and skin tone, same eye shape, same highlights. Do not make her younger, rounder or chibi. Adult proportions.

SPRITE FORMAT (identical in all 16 images):
- Portrait 2:3, high resolution (at least 1024x1536, 2K if available). Do NOT upscale or redraw afterwards.
- FULL BODY, head to shoes, standing, facing the viewer at a slight 3/4 angle, camera at chest height, no perspective distortion.
- Same scale and position in every image: the top of her hair about 4% below the top edge, the soles of her shoes about 3% above the bottom edge, body centered horizontally. Never crop the hair, ponytail, hair ornaments, hands or shoes.
- Background: flat solid pure chroma green #00FF00, completely uniform, no floor, no shadow on the ground, no gradient, no green light spill on her. Nothing she wears may be green.
- No text, no letters, no logo, no watermark anywhere. The ID card is blank.
- Arms and hands must not overlap her face. Clean, separated silhouette edges for easy background removal.

OUTFITS (keep exactly the same in every image that uses them):
- OFFICE: cream cable-knit open cardigan, white collared blouse, charcoal grey high-waist pencil skirt, sheer black pantyhose, black pumps, navy lanyard with a BLANK light plastic ID card holder (no text).
- CASUAL: cream cable-knit sweater over a white collar, brown pleated knee skirt, small beige crossbody bag, sheer black tights, black flats.
- HOME: oversized white button-up shirt, black leggings, cream slippers. Glasses and hairpin stay.

IMAGES:
IMAGE 1 — yujin_office_pose01_neutral.png
Outfit: OFFICE. Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: calm quiet face, mouth softly closed.

IMAGE 2 — yujin_office_pose01_smile.png
Outfit: OFFICE. Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: gentle warm smile.

IMAGE 3 — yujin_office_pose01_serious.png
Outfit: OFFICE. Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: concentrating face, eyes focused, lips pressed.

IMAGE 4 — yujin_office_pose01_blush.png
Outfit: OFFICE. Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: very shy face, cheeks and ears pink, eyes looking down.

IMAGE 5 — yujin_office_pose01_sad.png
Outfit: OFFICE. Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: downcast eyes, eyebrows tilted, small sad mouth, no tears.

IMAGE 6 — yujin_office_pose01_surprise.png
Outfit: OFFICE. Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: eyes wide behind her glasses, small open mouth.

IMAGE 7 — yujin_office_pose02_neutral.png
Outfit: OFFICE. Pose: one hand pushing up her glasses at the bridge, the other hand holding a pencil at her side. Expression: calm quiet face, mouth softly closed.

IMAGE 8 — yujin_office_pose02_serious.png
Outfit: OFFICE. Pose: one hand pushing up her glasses at the bridge, the other hand holding a pencil at her side. Expression: concentrating face, eyes focused, lips pressed.

IMAGE 9 — yujin_casual_pose01_neutral.png
Outfit: CASUAL. Pose: both hands holding the strap of her crossbody bag, feet together. Expression: calm quiet face, mouth softly closed.

IMAGE 10 — yujin_casual_pose01_smile.png
Outfit: CASUAL. Pose: both hands holding the strap of her crossbody bag, feet together. Expression: gentle warm smile.

IMAGE 11 — yujin_casual_pose01_blush.png
Outfit: CASUAL. Pose: both hands holding the strap of her crossbody bag, feet together. Expression: very shy face, cheeks and ears pink, eyes looking down.

IMAGE 12 — yujin_casual_pose01_sad.png
Outfit: CASUAL. Pose: both hands holding the strap of her crossbody bag, feet together. Expression: downcast eyes, eyebrows tilted, small sad mouth, no tears.

IMAGE 13 — yujin_casual_pose01_serious.png
Outfit: CASUAL. Pose: both hands holding the strap of her crossbody bag, feet together. Expression: concentrating face, eyes focused, lips pressed.

IMAGE 14 — yujin_home_pose01_neutral.png
Outfit: HOME. Pose: one hand holding a mug at chest height, the other tugging the long shirt sleeve. Expression: calm quiet face, mouth softly closed.

IMAGE 15 — yujin_home_pose01_smile.png
Outfit: HOME. Pose: one hand holding a mug at chest height, the other tugging the long shirt sleeve. Expression: gentle warm smile.

IMAGE 16 — yujin_home_pose01_blush.png
Outfit: HOME. Pose: one hand holding a mug at chest height, the other tugging the long shirt sleeve. Expression: very shy face, cheeks and ears pink, eyes looking down.
```

---

## 한서윤 (마스터: `seoyun_office_pose01_neutral_v001.png`)

| # | 의상·포즈 | 표정 | 파일 이름 |
|---|---|---|---|
| 1 | 업무복 pose01 | 보통 | seoyun_office_pose01_neutral.png |
| 2 | 업무복 pose01 | 웃음 | seoyun_office_pose01_smile.png |
| 3 | 업무복 pose01 | 진지 | seoyun_office_pose01_serious.png |
| 4 | 업무복 pose01 | 수줍 | seoyun_office_pose01_blush.png |
| 5 | 업무복 pose01 | 놀람 | seoyun_office_pose01_surprise.png |
| 6 | 업무복 pose01 | 슬픔 | seoyun_office_pose01_sad.png |
| 7 | 업무복 pose02 | 보통 | seoyun_office_pose02_neutral.png |
| 8 | 업무복 pose02 | 웃음 | seoyun_office_pose02_smile.png |
| 9 | 사복 pose01 | 보통 | seoyun_casual_pose01_neutral.png |
| 10 | 사복 pose01 | 웃음 | seoyun_casual_pose01_smile.png |
| 11 | 사복 pose01 | 수줍 | seoyun_casual_pose01_blush.png |
| 12 | 사복 pose01 | 놀람 | seoyun_casual_pose01_surprise.png |
| 13 | 사복 pose01 | 슬픔 | seoyun_casual_pose01_sad.png |
| 14 | 사복 pose02 | 보통 | seoyun_casual_pose02_neutral.png |
| 15 | 사복 pose02 | 웃음 | seoyun_casual_pose02_smile.png |
| 16 | 사복 pose02 | 진지 | seoyun_casual_pose02_serious.png |

```text
Create 16 separate character sprite images of the same woman, one image per item below, in order. Label each image with its number and file name. Do not merge images into a sheet. Do not skip any.

REFERENCE: the attached master sprite is the ONLY reference for her face, hair, eye color, body proportions, height and drawing style. Every image must look like the same person drawn by the same artist.

CHARACTER: Han Seoyun, adult woman (32), teasing senior copywriter. Slim oval face, long wavy dark plum / deep violet hair, half-lidded grey-blue lavender eyes, small BEAUTY MARK under her LEFT eye, no earrings. Same height, body proportions and face as the master.

ART STYLE LOCK (absolute): exactly the master's anime visual-novel style — same clean line weight, flat cel shading with soft gradients, same coloring and skin tone, same eye shape, same highlights. Do not make her younger, rounder or chibi. Adult proportions.

SPRITE FORMAT (identical in all 16 images):
- Portrait 2:3, high resolution (at least 1024x1536, 2K if available). Do NOT upscale or redraw afterwards.
- FULL BODY, head to shoes, standing, facing the viewer at a slight 3/4 angle, camera at chest height, no perspective distortion.
- Same scale and position in every image: the top of her hair about 4% below the top edge, the soles of her shoes about 3% above the bottom edge, body centered horizontally. Never crop the hair, ponytail, hair ornaments, hands or shoes.
- Background: flat solid pure chroma green #00FF00, completely uniform, no floor, no shadow on the ground, no gradient, no green light spill on her. Nothing she wears may be green.
- No text, no letters, no logo, no watermark anywhere. The ID card is blank.
- Arms and hands must not overlap her face. Clean, separated silhouette edges for easy background removal.

OUTFITS (keep exactly the same in every image that uses them):
- OFFICE: pale lavender collared blouse with rolled sleeves and the top button undone, navy high-waist pencil skirt with a black belt, garter belt with black lace-band thigh-high stockings, black pumps, navy lanyard with a BLANK light plastic ID card holder (no text).
- CASUAL: long beige knit cardigan over a grey ribbed midi dress with a side slit, white sneakers.

IMAGES:
IMAGE 1 — seoyun_office_pose01_neutral.png
Outfit: OFFICE. Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: relaxed half-lidded face, faint smile at the corner of her mouth.

IMAGE 2 — seoyun_office_pose01_smile.png
Outfit: OFFICE. Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: teasing confident smile.

IMAGE 3 — seoyun_office_pose01_serious.png
Outfit: OFFICE. Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: serious face without any smile, steady eyes.

IMAGE 4 — seoyun_office_pose01_blush.png
Outfit: OFFICE. Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: caught-off-guard face, cheeks pink, eyes wavering.

IMAGE 5 — seoyun_office_pose01_surprise.png
Outfit: OFFICE. Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: eyes opened wide (not half-lidded), lips parted.

IMAGE 6 — seoyun_office_pose01_sad.png
Outfit: OFFICE. Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: quiet sad face, eyes lowered, no tears.

IMAGE 7 — seoyun_office_pose02_neutral.png
Outfit: OFFICE. Pose: arms loosely crossed under her chest, weight on one leg, teasing posture. Expression: relaxed half-lidded face, faint smile at the corner of her mouth.

IMAGE 8 — seoyun_office_pose02_smile.png
Outfit: OFFICE. Pose: arms loosely crossed under her chest, weight on one leg, teasing posture. Expression: teasing confident smile.

IMAGE 9 — seoyun_casual_pose01_neutral.png
Outfit: CASUAL. Pose: one hand touching her hair behind her ear, the other holding the cardigan edge. Expression: relaxed half-lidded face, faint smile at the corner of her mouth.

IMAGE 10 — seoyun_casual_pose01_smile.png
Outfit: CASUAL. Pose: one hand touching her hair behind her ear, the other holding the cardigan edge. Expression: teasing confident smile.

IMAGE 11 — seoyun_casual_pose01_blush.png
Outfit: CASUAL. Pose: one hand touching her hair behind her ear, the other holding the cardigan edge. Expression: caught-off-guard face, cheeks pink, eyes wavering.

IMAGE 12 — seoyun_casual_pose01_surprise.png
Outfit: CASUAL. Pose: one hand touching her hair behind her ear, the other holding the cardigan edge. Expression: eyes opened wide (not half-lidded), lips parted.

IMAGE 13 — seoyun_casual_pose01_sad.png
Outfit: CASUAL. Pose: one hand touching her hair behind her ear, the other holding the cardigan edge. Expression: quiet sad face, eyes lowered, no tears.

IMAGE 14 — seoyun_casual_pose02_neutral.png
Outfit: CASUAL. Pose: arms loosely crossed, head tilted, playful stance. Expression: relaxed half-lidded face, faint smile at the corner of her mouth.

IMAGE 15 — seoyun_casual_pose02_smile.png
Outfit: CASUAL. Pose: arms loosely crossed, head tilted, playful stance. Expression: teasing confident smile.

IMAGE 16 — seoyun_casual_pose02_serious.png
Outfit: CASUAL. Pose: arms loosely crossed, head tilted, playful stance. Expression: serious face without any smile, steady eyes.
```
