# 제미나이 입상 태스크 · 업무복 16장 v003 · 포즈 3개 (마스터 그림체 절대 기준)

v002에서 바뀐 점: 포즈를 3개로 늘렸어요. 16장 구성은 아래와 같아요.
- 포즈1 × 표정 8개 = 8장
- 포즈2 × 표정 4개 = 4장
- 포즈3 × 표정 4개 = 4장

게임은 업무복 장면에서 포즈1을 절반, 포즈2와 포즈3을 4분의 1씩 써요. 그래서 포즈1에 표정을 다 넣고, 포즈2·3에는 많이 쓰는 표정 4개(보통, 웃음, 진지, 수줍)만 넣었어요. 포즈2·3에 없는 표정이 나오면 게임이 가장 가까운 표정으로 자동으로 바꿔요.

업무복만 만들고, 그림체는 마스터를 절대 기준으로 해요.

**표정 8개를 고른 기준**
대사를 세어 보면 업무복이 쓰이는 장면이 가장 많아요(히로인별 275~359줄). 표정은 많이 쓰이는 순서인 보통 → 웃음 → 진지 → 수줍 → 놀람 → 슬픔 6개를 공통으로 넣었어요. 나머지 2개는 성격에 맞춰 골랐어요.

| 히로인 | 성격에 맞춘 표정 2개 |
|---|---|
| 리아 | 크게 웃음, 삐짐 |
| 지현 | 삐짐(못마땅), 울먹 (R13 갈등 장면용) |
| 유진 | 작게 웃음, 울먹 |
| 서윤 | 웃음, 장난스러운 삐짐 |

## 사용법
1. 제미나이 설정은 **Pro 이미지 모델, 세로 2:3, 고해상도(2K가 되면 2K)**예요.
2. 그 히로인의 **마스터 입상 한 장만** 올려요. `CharacterArt/candidates/heroine-masters-v001/final_2048x3072/` 안에 있는 파일이에요.
3. 블록을 통째로 붙여 넣어요. 중간에 멈추면 `Continue with IMAGE n.`이라고 보내요.
4. 다 받으면 파일 이름 그대로 저장해서 올려 주세요. 초록 배경 빼기, 키 맞추기, WebP 변환, 게임 연결은 제가 해요.
5. 다시 시킬 때 쓰는 말:
   - 그림체가 달라졌을 때: `Redo IMAGE n. Copy the master's art style exactly: same line weight, shading, coloring and eye drawing.`
   - 얼굴이 달라졌을 때: `Redo IMAGE n. Her face must be identical to the attached master; only the expression changes.`
   - 크기나 위치가 다를 때: `Redo IMAGE n with exactly the same framing as IMAGE 1.`
   - 사원증에 글자가 생겼을 때: `Redo IMAGE n with a blank ID card, no letters.`
   - 배경이 초록 단색이 아닐 때: `Redo IMAGE n on a flat pure #00FF00 background.`

---

## 강리아 (마스터: `ria_office_pose01_neutral_v001.png`)

| # | 포즈 | 표정 | 파일 이름 |
|---|---|---|---|
| 1 | pose01 | 보통 | ria_office_pose01_neutral.png |
| 2 | pose01 | 웃음 | ria_office_pose01_smile.png |
| 3 | pose01 | 크게 웃음 | ria_office_pose01_laugh.png |
| 4 | pose01 | 진지 | ria_office_pose01_serious.png |
| 5 | pose01 | 수줍 | ria_office_pose01_blush.png |
| 6 | pose01 | 놀람 | ria_office_pose01_surprise.png |
| 7 | pose01 | 슬픔 | ria_office_pose01_sad.png |
| 8 | pose01 | 삐짐 | ria_office_pose01_pout.png |
| 9 | pose02 | 보통 | ria_office_pose02_neutral.png |
| 10 | pose02 | 웃음 | ria_office_pose02_smile.png |
| 11 | pose02 | 진지 | ria_office_pose02_serious.png |
| 12 | pose02 | 수줍 | ria_office_pose02_blush.png |
| 13 | pose03 | 보통 | ria_office_pose03_neutral.png |
| 14 | pose03 | 웃음 | ria_office_pose03_smile.png |
| 15 | pose03 | 진지 | ria_office_pose03_serious.png |
| 16 | pose03 | 수줍 | ria_office_pose03_blush.png |

```text
Create 16 separate character sprite images of the same woman in her office outfit, one image per item below, in order. Label each image with its number and file name. Do not merge them into a sheet. Do not skip any.

MASTER STYLE LOCK (absolute, highest priority, overrides everything else):
- The attached master sprite is the ONLY reference. Copy its art style EXACTLY: same line art thickness and color, same flat cel shading with soft gradients, same shadow shapes, same skin tone, same hair shading and highlights, same eye drawing (iris, highlights, lashes), same face shape, same body proportions and height.
- Every image must look like it was cut from the same sprite set as the master, drawn by the same artist on the same day. If a result looks like a different art style, a different artist, a 3D render, a painting or a photo, discard it and redraw.
- Only the pose and the facial expression change. Face, hair, outfit, accessories and body stay identical to the master.
- Do not make her younger, rounder, cuter or chibi. Adult proportions.

CHARACTER: Kang Ria, adult woman (28), cheerful event-planning team member. Slim face, very long wavy honey-blonde hair in a HIGH PONYTAIL tied with a BLUE SCRUNCHIE, straight blunt bangs, bright BLUE eyes, bright friendly mouth.

OFFICE OUTFIT (identical to the master in every image): opaque white cotton collared blouse with sleeves rolled up, black high-waist pencil skirt, sheer black pantyhose, black patent pumps, navy lanyard with a BLANK light plastic ID card holder (no text).

SPRITE FORMAT (identical in all 16 images):
- Portrait 2:3, high resolution (at least 1024x1536, 2K if available). Do NOT upscale or redraw afterwards.
- FULL BODY, head to shoes, standing, facing the viewer at a slight 3/4 angle like the master, camera at chest height, no perspective distortion.
- Same scale and position in every image as the master: the top of her hair about 4% below the top edge, the soles of her shoes about 3% above the bottom edge, body centered. Never crop the hair, ponytail, hair ornaments, hands or shoes.
- Background: flat solid pure chroma green #00FF00, completely uniform, no floor, no ground shadow, no gradient, no green light spill on her.
- No text, no letters, no logo, no watermark anywhere. The ID card is blank.
- Hands must not cover her face. Clean silhouette edges for easy background removal.

IMAGES (pose 01 = images 1-8, pose 02 = images 9-12, pose 03 = images 13-16; keep the pose identical within each group, change only the face):
IMAGE 1 — ria_office_pose01_neutral.png
Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: calm pleasant face, mouth softly closed.

IMAGE 2 — ria_office_pose01_smile.png
Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: big bright smile, eyes slightly curved.

IMAGE 3 — ria_office_pose01_laugh.png
Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: laughing openly, eyes squeezed into happy arcs, mouth wide open.

IMAGE 4 — ria_office_pose01_serious.png
Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: focused work face, small frown, lips pressed.

IMAGE 5 — ria_office_pose01_blush.png
Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: shy smile, cheeks clearly pink, eyes glancing aside.

IMAGE 6 — ria_office_pose01_surprise.png
Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: eyes wide, small round open mouth, eyebrows up.

IMAGE 7 — ria_office_pose01_sad.png
Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: eyebrows tilted up, eyes lowered, small sad mouth, no tears.

IMAGE 8 — ria_office_pose01_pout.png
Pose: hands lightly clasped in front of her skirt, weight on one leg, a small cheerful lean forward. Expression: playful pout, cheeks slightly puffed, eyes looking sideways.

IMAGE 9 — ria_office_pose02_neutral.png
Pose: one hand raised at shoulder height in a small friendly wave, the other hand holding a clipboard at her hip. Expression: calm pleasant face, mouth softly closed.

IMAGE 10 — ria_office_pose02_smile.png
Pose: one hand raised at shoulder height in a small friendly wave, the other hand holding a clipboard at her hip. Expression: big bright smile, eyes slightly curved.

IMAGE 11 — ria_office_pose02_serious.png
Pose: one hand raised at shoulder height in a small friendly wave, the other hand holding a clipboard at her hip. Expression: focused work face, small frown, lips pressed.

IMAGE 12 — ria_office_pose02_blush.png
Pose: one hand raised at shoulder height in a small friendly wave, the other hand holding a clipboard at her hip. Expression: shy smile, cheeks clearly pink, eyes glancing aside.

IMAGE 13 — ria_office_pose03_neutral.png
Pose: explaining at work: holding an open notebook in one hand and raising a pen in the other hand as if pointing at something, bright engaged posture. Expression: calm pleasant face, mouth softly closed.

IMAGE 14 — ria_office_pose03_smile.png
Pose: explaining at work: holding an open notebook in one hand and raising a pen in the other hand as if pointing at something, bright engaged posture. Expression: big bright smile, eyes slightly curved.

IMAGE 15 — ria_office_pose03_serious.png
Pose: explaining at work: holding an open notebook in one hand and raising a pen in the other hand as if pointing at something, bright engaged posture. Expression: focused work face, small frown, lips pressed.

IMAGE 16 — ria_office_pose03_blush.png
Pose: explaining at work: holding an open notebook in one hand and raising a pen in the other hand as if pointing at something, bright engaged posture. Expression: shy smile, cheeks clearly pink, eyes glancing aside.
```

---

## 백지현 (마스터: `jihyun_office_pose01_neutral_v001.png`)

| # | 포즈 | 표정 | 파일 이름 |
|---|---|---|---|
| 1 | pose01 | 보통 | jihyun_office_pose01_neutral.png |
| 2 | pose01 | 웃음 | jihyun_office_pose01_smile.png |
| 3 | pose01 | 진지 | jihyun_office_pose01_serious.png |
| 4 | pose01 | 수줍 | jihyun_office_pose01_blush.png |
| 5 | pose01 | 놀람 | jihyun_office_pose01_surprise.png |
| 6 | pose01 | 슬픔 | jihyun_office_pose01_sad.png |
| 7 | pose01 | 삐짐 | jihyun_office_pose01_pout.png |
| 8 | pose01 | 울먹 | jihyun_office_pose01_teary.png |
| 9 | pose02 | 보통 | jihyun_office_pose02_neutral.png |
| 10 | pose02 | 진지 | jihyun_office_pose02_serious.png |
| 11 | pose02 | 웃음 | jihyun_office_pose02_smile.png |
| 12 | pose02 | 수줍 | jihyun_office_pose02_blush.png |
| 13 | pose03 | 보통 | jihyun_office_pose03_neutral.png |
| 14 | pose03 | 진지 | jihyun_office_pose03_serious.png |
| 15 | pose03 | 웃음 | jihyun_office_pose03_smile.png |
| 16 | pose03 | 수줍 | jihyun_office_pose03_blush.png |

```text
Create 16 separate character sprite images of the same woman in her office outfit, one image per item below, in order. Label each image with its number and file name. Do not merge them into a sheet. Do not skip any.

MASTER STYLE LOCK (absolute, highest priority, overrides everything else):
- The attached master sprite is the ONLY reference. Copy its art style EXACTLY: same line art thickness and color, same flat cel shading with soft gradients, same shadow shapes, same skin tone, same hair shading and highlights, same eye drawing (iris, highlights, lashes), same face shape, same body proportions and height.
- Every image must look like it was cut from the same sprite set as the master, drawn by the same artist on the same day. If a result looks like a different art style, a different artist, a 3D render, a painting or a photo, discard it and redraw.
- Only the pose and the facial expression change. Face, hair, outfit, accessories and body stay identical to the master.
- Do not make her younger, rounder, cuter or chibi. Adult proportions.

CHARACTER: Baek Jihyun, adult woman (30), composed team leader. Very long CRIMSON hair falling straight down her shoulders and back (not spreading outward), slight wave only at the ends, glossy crown, side-parted bangs, sharp RED-BROWN eyes with clear eyeliner, confident gaze, NO beauty mark.

OFFICE OUTFIT (identical to the master in every image): burgundy shirt, charcoal tailored jacket, charcoal-black high-waist pencil skirt, sheer black pantyhose, black pumps, navy lanyard with a BLANK light plastic ID card holder (no text).

SPRITE FORMAT (identical in all 16 images):
- Portrait 2:3, high resolution (at least 1024x1536, 2K if available). Do NOT upscale or redraw afterwards.
- FULL BODY, head to shoes, standing, facing the viewer at a slight 3/4 angle like the master, camera at chest height, no perspective distortion.
- Same scale and position in every image as the master: the top of her hair about 4% below the top edge, the soles of her shoes about 3% above the bottom edge, body centered. Never crop the hair, ponytail, hair ornaments, hands or shoes.
- Background: flat solid pure chroma green #00FF00, completely uniform, no floor, no ground shadow, no gradient, no green light spill on her.
- No text, no letters, no logo, no watermark anywhere. The ID card is blank.
- Hands must not cover her face. Clean silhouette edges for easy background removal.

IMAGES (pose 01 = images 1-8, pose 02 = images 9-12, pose 03 = images 13-16; keep the pose identical within each group, change only the face):
IMAGE 1 — jihyun_office_pose01_neutral.png
Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: calm composed face, mouth closed.

IMAGE 2 — jihyun_office_pose01_smile.png
Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: small restrained smile, eyes softened.

IMAGE 3 — jihyun_office_pose01_serious.png
Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: stern focused face, eyebrows drawn together, lips pressed.

IMAGE 4 — jihyun_office_pose01_blush.png
Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: embarrassed face trying to stay composed, cheeks pink, eyes looking away.

IMAGE 5 — jihyun_office_pose01_surprise.png
Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: eyes widened, lips parted, eyebrows up.

IMAGE 6 — jihyun_office_pose01_sad.png
Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: tired sad face, eyes lowered, eyebrows tilted, no tears.

IMAGE 7 — jihyun_office_pose01_pout.png
Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: annoyed face, slight frown, lips pushed to one side, eyes looking away.

IMAGE 8 — jihyun_office_pose01_teary.png
Pose: standing straight, one hand on her hip, the other relaxed at her side, chin slightly up. Expression: holding back tears, eyes glossy with tears at the corners, lips pressed, still composed.

IMAGE 9 — jihyun_office_pose02_neutral.png
Pose: holding a tablet against her chest with one arm, the other hand lightly touching her jacket lapel. Expression: calm composed face, mouth closed.

IMAGE 10 — jihyun_office_pose02_serious.png
Pose: holding a tablet against her chest with one arm, the other hand lightly touching her jacket lapel. Expression: stern focused face, eyebrows drawn together, lips pressed.

IMAGE 11 — jihyun_office_pose02_smile.png
Pose: holding a tablet against her chest with one arm, the other hand lightly touching her jacket lapel. Expression: small restrained smile, eyes softened.

IMAGE 12 — jihyun_office_pose02_blush.png
Pose: holding a tablet against her chest with one arm, the other hand lightly touching her jacket lapel. Expression: embarrassed face trying to stay composed, cheeks pink, eyes looking away.

IMAGE 13 — jihyun_office_pose03_neutral.png
Pose: arms crossed over her chest, weight on one leg, evaluating look. Expression: calm composed face, mouth closed.

IMAGE 14 — jihyun_office_pose03_serious.png
Pose: arms crossed over her chest, weight on one leg, evaluating look. Expression: stern focused face, eyebrows drawn together, lips pressed.

IMAGE 15 — jihyun_office_pose03_smile.png
Pose: arms crossed over her chest, weight on one leg, evaluating look. Expression: small restrained smile, eyes softened.

IMAGE 16 — jihyun_office_pose03_blush.png
Pose: arms crossed over her chest, weight on one leg, evaluating look. Expression: embarrassed face trying to stay composed, cheeks pink, eyes looking away.
```

---

## 차유진 (마스터: `yujin_office_pose01_neutral_v001.png`)

| # | 포즈 | 표정 | 파일 이름 |
|---|---|---|---|
| 1 | pose01 | 보통 | yujin_office_pose01_neutral.png |
| 2 | pose01 | 웃음 | yujin_office_pose01_smile.png |
| 3 | pose01 | 크게 웃음 | yujin_office_pose01_laugh.png |
| 4 | pose01 | 진지 | yujin_office_pose01_serious.png |
| 5 | pose01 | 수줍 | yujin_office_pose01_blush.png |
| 6 | pose01 | 놀람 | yujin_office_pose01_surprise.png |
| 7 | pose01 | 슬픔 | yujin_office_pose01_sad.png |
| 8 | pose01 | 울먹 | yujin_office_pose01_teary.png |
| 9 | pose02 | 보통 | yujin_office_pose02_neutral.png |
| 10 | pose02 | 웃음 | yujin_office_pose02_smile.png |
| 11 | pose02 | 진지 | yujin_office_pose02_serious.png |
| 12 | pose02 | 수줍 | yujin_office_pose02_blush.png |
| 13 | pose03 | 보통 | yujin_office_pose03_neutral.png |
| 14 | pose03 | 웃음 | yujin_office_pose03_smile.png |
| 15 | pose03 | 진지 | yujin_office_pose03_serious.png |
| 16 | pose03 | 수줍 | yujin_office_pose03_blush.png |

```text
Create 16 separate character sprite images of the same woman in her office outfit, one image per item below, in order. Label each image with its number and file name. Do not merge them into a sheet. Do not skip any.

MASTER STYLE LOCK (absolute, highest priority, overrides everything else):
- The attached master sprite is the ONLY reference. Copy its art style EXACTLY: same line art thickness and color, same flat cel shading with soft gradients, same shadow shapes, same skin tone, same hair shading and highlights, same eye drawing (iris, highlights, lashes), same face shape, same body proportions and height.
- Every image must look like it was cut from the same sprite set as the master, drawn by the same artist on the same day. If a result looks like a different art style, a different artist, a 3D render, a painting or a photo, discard it and redraw.
- Only the pose and the facial expression change. Face, hair, outfit, accessories and body stay identical to the master.
- Do not make her younger, rounder, cuter or chibi. Adult proportions.

CHARACTER: Cha Yujin, adult woman (27), quiet brand designer. SILVER-WHITE bob (front slightly longer, straight), side-swept bangs, one GOLD HAIRPIN on one side, thin ROUND metal-frame GLASSES, amber-brown eyes, calm gentle face, mature curvy figure.

OFFICE OUTFIT (identical to the master in every image): cream cable-knit open cardigan, white collared blouse, charcoal grey high-waist pencil skirt, sheer black pantyhose, black pumps, navy lanyard with a BLANK light plastic ID card holder (no text).

SPRITE FORMAT (identical in all 16 images):
- Portrait 2:3, high resolution (at least 1024x1536, 2K if available). Do NOT upscale or redraw afterwards.
- FULL BODY, head to shoes, standing, facing the viewer at a slight 3/4 angle like the master, camera at chest height, no perspective distortion.
- Same scale and position in every image as the master: the top of her hair about 4% below the top edge, the soles of her shoes about 3% above the bottom edge, body centered. Never crop the hair, ponytail, hair ornaments, hands or shoes.
- Background: flat solid pure chroma green #00FF00, completely uniform, no floor, no ground shadow, no gradient, no green light spill on her.
- No text, no letters, no logo, no watermark anywhere. The ID card is blank.
- Hands must not cover her face. Clean silhouette edges for easy background removal.

IMAGES (pose 01 = images 1-8, pose 02 = images 9-12, pose 03 = images 13-16; keep the pose identical within each group, change only the face):
IMAGE 1 — yujin_office_pose01_neutral.png
Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: calm quiet face, mouth softly closed.

IMAGE 2 — yujin_office_pose01_smile.png
Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: gentle warm smile.

IMAGE 3 — yujin_office_pose01_laugh.png
Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: soft laugh, eyes closed in happy arcs, small open mouth.

IMAGE 4 — yujin_office_pose01_serious.png
Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: concentrating face, eyes focused, lips pressed.

IMAGE 5 — yujin_office_pose01_blush.png
Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: very shy face, cheeks and ears pink, eyes looking down.

IMAGE 6 — yujin_office_pose01_surprise.png
Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: eyes wide behind her glasses, small open mouth.

IMAGE 7 — yujin_office_pose01_sad.png
Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: downcast eyes, eyebrows tilted, small sad mouth, no tears.

IMAGE 8 — yujin_office_pose01_teary.png
Pose: holding a sketchbook in front of her waist with both hands, shoulders slightly drawn in. Expression: teary eyes behind her glasses, small tears at the corners, trembling lips.

IMAGE 9 — yujin_office_pose02_neutral.png
Pose: one hand pushing up her glasses at the bridge, the other hand holding a pencil at her side. Expression: calm quiet face, mouth softly closed.

IMAGE 10 — yujin_office_pose02_smile.png
Pose: one hand pushing up her glasses at the bridge, the other hand holding a pencil at her side. Expression: gentle warm smile.

IMAGE 11 — yujin_office_pose02_serious.png
Pose: one hand pushing up her glasses at the bridge, the other hand holding a pencil at her side. Expression: concentrating face, eyes focused, lips pressed.

IMAGE 12 — yujin_office_pose02_blush.png
Pose: one hand pushing up her glasses at the bridge, the other hand holding a pencil at her side. Expression: very shy face, cheeks and ears pink, eyes looking down.

IMAGE 13 — yujin_office_pose03_neutral.png
Pose: both hands clasped behind her back, leaning slightly forward, curious posture. Expression: calm quiet face, mouth softly closed.

IMAGE 14 — yujin_office_pose03_smile.png
Pose: both hands clasped behind her back, leaning slightly forward, curious posture. Expression: gentle warm smile.

IMAGE 15 — yujin_office_pose03_serious.png
Pose: both hands clasped behind her back, leaning slightly forward, curious posture. Expression: concentrating face, eyes focused, lips pressed.

IMAGE 16 — yujin_office_pose03_blush.png
Pose: both hands clasped behind her back, leaning slightly forward, curious posture. Expression: very shy face, cheeks and ears pink, eyes looking down.
```

---

## 한서윤 (마스터: `seoyun_office_pose01_neutral_v001.png`)

| # | 포즈 | 표정 | 파일 이름 |
|---|---|---|---|
| 1 | pose01 | 보통 | seoyun_office_pose01_neutral.png |
| 2 | pose01 | 웃음 | seoyun_office_pose01_smile.png |
| 3 | pose01 | 크게 웃음 | seoyun_office_pose01_laugh.png |
| 4 | pose01 | 진지 | seoyun_office_pose01_serious.png |
| 5 | pose01 | 수줍 | seoyun_office_pose01_blush.png |
| 6 | pose01 | 놀람 | seoyun_office_pose01_surprise.png |
| 7 | pose01 | 슬픔 | seoyun_office_pose01_sad.png |
| 8 | pose01 | 삐짐 | seoyun_office_pose01_pout.png |
| 9 | pose02 | 보통 | seoyun_office_pose02_neutral.png |
| 10 | pose02 | 웃음 | seoyun_office_pose02_smile.png |
| 11 | pose02 | 진지 | seoyun_office_pose02_serious.png |
| 12 | pose02 | 수줍 | seoyun_office_pose02_blush.png |
| 13 | pose03 | 보통 | seoyun_office_pose03_neutral.png |
| 14 | pose03 | 웃음 | seoyun_office_pose03_smile.png |
| 15 | pose03 | 진지 | seoyun_office_pose03_serious.png |
| 16 | pose03 | 수줍 | seoyun_office_pose03_blush.png |

```text
Create 16 separate character sprite images of the same woman in her office outfit, one image per item below, in order. Label each image with its number and file name. Do not merge them into a sheet. Do not skip any.

MASTER STYLE LOCK (absolute, highest priority, overrides everything else):
- The attached master sprite is the ONLY reference. Copy its art style EXACTLY: same line art thickness and color, same flat cel shading with soft gradients, same shadow shapes, same skin tone, same hair shading and highlights, same eye drawing (iris, highlights, lashes), same face shape, same body proportions and height.
- Every image must look like it was cut from the same sprite set as the master, drawn by the same artist on the same day. If a result looks like a different art style, a different artist, a 3D render, a painting or a photo, discard it and redraw.
- Only the pose and the facial expression change. Face, hair, outfit, accessories and body stay identical to the master.
- Do not make her younger, rounder, cuter or chibi. Adult proportions.

CHARACTER: Han Seoyun, adult woman (32), teasing senior copywriter. Slim oval face, long wavy dark plum / deep violet hair, half-lidded grey-blue lavender eyes, small BEAUTY MARK under her LEFT eye, no earrings.

OFFICE OUTFIT (identical to the master in every image): pale lavender collared blouse with rolled sleeves and the top button undone, navy high-waist pencil skirt with a black belt, garter belt with black lace-band thigh-high stockings, black pumps, navy lanyard with a BLANK light plastic ID card holder (no text).

SPRITE FORMAT (identical in all 16 images):
- Portrait 2:3, high resolution (at least 1024x1536, 2K if available). Do NOT upscale or redraw afterwards.
- FULL BODY, head to shoes, standing, facing the viewer at a slight 3/4 angle like the master, camera at chest height, no perspective distortion.
- Same scale and position in every image as the master: the top of her hair about 4% below the top edge, the soles of her shoes about 3% above the bottom edge, body centered. Never crop the hair, ponytail, hair ornaments, hands or shoes.
- Background: flat solid pure chroma green #00FF00, completely uniform, no floor, no ground shadow, no gradient, no green light spill on her.
- No text, no letters, no logo, no watermark anywhere. The ID card is blank.
- Hands must not cover her face. Clean silhouette edges for easy background removal.

IMAGES (pose 01 = images 1-8, pose 02 = images 9-12, pose 03 = images 13-16; keep the pose identical within each group, change only the face):
IMAGE 1 — seoyun_office_pose01_neutral.png
Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: relaxed half-lidded face, faint smile at the corner of her mouth.

IMAGE 2 — seoyun_office_pose01_smile.png
Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: teasing confident smile.

IMAGE 3 — seoyun_office_pose01_laugh.png
Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: laughing, eyes closed in happy arcs, one corner of the mouth higher.

IMAGE 4 — seoyun_office_pose01_serious.png
Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: serious face without any smile, steady eyes.

IMAGE 5 — seoyun_office_pose01_blush.png
Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: caught-off-guard face, cheeks pink, eyes wavering.

IMAGE 6 — seoyun_office_pose01_surprise.png
Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: eyes opened wide (not half-lidded), lips parted.

IMAGE 7 — seoyun_office_pose01_sad.png
Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: quiet sad face, eyes lowered, no tears.

IMAGE 8 — seoyun_office_pose01_pout.png
Pose: one hand holding a coffee mug at chest height, the other relaxed at her side, head slightly tilted. Expression: mock-sulky face, lips pushed out, eyes narrowed playfully.

IMAGE 9 — seoyun_office_pose02_neutral.png
Pose: arms loosely crossed under her chest, weight on one leg, teasing posture. Expression: relaxed half-lidded face, faint smile at the corner of her mouth.

IMAGE 10 — seoyun_office_pose02_smile.png
Pose: arms loosely crossed under her chest, weight on one leg, teasing posture. Expression: teasing confident smile.

IMAGE 11 — seoyun_office_pose02_serious.png
Pose: arms loosely crossed under her chest, weight on one leg, teasing posture. Expression: serious face without any smile, steady eyes.

IMAGE 12 — seoyun_office_pose02_blush.png
Pose: arms loosely crossed under her chest, weight on one leg, teasing posture. Expression: caught-off-guard face, cheeks pink, eyes wavering.

IMAGE 13 — seoyun_office_pose03_neutral.png
Pose: one hand on her hip, the other holding a pen near her lips, thinking posture. Expression: relaxed half-lidded face, faint smile at the corner of her mouth.

IMAGE 14 — seoyun_office_pose03_smile.png
Pose: one hand on her hip, the other holding a pen near her lips, thinking posture. Expression: teasing confident smile.

IMAGE 15 — seoyun_office_pose03_serious.png
Pose: one hand on her hip, the other holding a pen near her lips, thinking posture. Expression: serious face without any smile, steady eyes.

IMAGE 16 — seoyun_office_pose03_blush.png
Pose: one hand on her hip, the other holding a pen near her lips, thinking posture. Expression: caught-off-guard face, cheeks pink, eyes wavering.
```
