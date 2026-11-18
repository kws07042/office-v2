# 챗지피티 이미지 프롬프트 v002 — 바로 붙여 넣는 판

`Docs/art-prompts-chatgpt-v001.md`의 규칙을 그대로 따르고, 이번에 새로 생긴 장면까지 프롬프트를 채워 넣었다.

## 정해진 것 (2026-11-19)
- **마스터 그림은 게임 화면에 쓰지 않는 쪽으로 간다.** 챗지피티에 첨부하는 '참고용'으로만 쓴다. 그래서 게임에 들어갈 인물 그림은 **의상마다 전신 + 표정**을 새로 뽑는다(아래 A-0).
- **인물이 들어가는 그림은 전부 누끼(투명 배경)로 뽑는다.** 아래 [누끼 문단]을 인물 프롬프트 맨 끝에 붙인다.
- **차유진 겨울 외투**는 카멜 케이프 코트와 체크 머플러로 바꿨다(`art-prompts-winter-v001.md` 반영).

## 쓰는 법 (매번 똑같이)

1. 챗지피티에서 **새 대화**를 연다. 같은 히로인은 한 대화 안에서 계속 만든다.
2. 그림 두 장을 **첨부**한다.
   - 해당 히로인 마스터: `CharacterArt/candidates/heroine-masters-v001/final_2048x3072/`
   - 화풍 기준인 강리아 마스터: `ria_office_pose01_neutral_v001.png`
   - 배경만 만들 때도 강리아 마스터 한 장은 첨부한다.
3. 아래 **[화풍 고정 문단]**을 먼저 붙이고, 줄을 바꿔 원하는 프롬프트 블록을 붙인다.
4. 결과를 마스터 옆에 나란히 놓고 v001 문서 0-1의 체크리스트로 확인한다. 하나라도 어긋나면 버리고 다시 뽑는다.
5. 파일 이름은 각 블록 위에 적힌 대로 저장한다.

### [화풍 고정 문단] — 모든 프롬프트 맨 앞에

```
STYLE LOCK — this is the most important rule.
Copy the art style of the attached reference images EXACTLY, as if drawn by the same artist in the same session:
- same line art: thin, clean, uniform dark-brown/black outlines, no sketchy or painterly lines
- same eye rendering: same eye shape, iris gradient, highlight shapes and positions, eyelash style
- same coloring: flat cel shading with one soft shadow tone and small crisp highlights; same saturation and warmth
- same face proportions and nose/mouth drawing; same hair strand rendering and hair highlights
Do NOT reinterpret, stylize, beautify, modernize, add your own style, add gradients, glow, painterly texture, 3D, semi-realism or photo textures.
If anything conflicts, the reference images win.
```

### [누끼 문단] — 인물 단독 그림(전신·표정)의 맨 끝에

```
CUTOUT: TRANSPARENT background, PNG with alpha. Crisp clean outline with no white halo, no fringe, no anti-aliased gray edge, no drop shadow, no ground shadow, no floor line. Every hair strand and loose fabric edge cleanly separated from the background. Nothing else in the image.
```

투명이 안 나오면 `Use a solid pure green #00FF00 background with no shadows` 로 바꿔 뽑고, 초록을 지워 누끼를 딴다.

---

## A-0. 게임에 쓸 인물 그림 — 전신 × 표정 (마스터 대신)

의상 4벌(업무복·사복·생활복·겨울)마다 **기본 전신 1장**을 먼저 뽑는다. 그 그림을 첨부해서 **표정만 바꾼 7장**을 뽑는다.
- 인물당 4벌 × 8표정 = 32장, 4명이면 **128장**
- 출시 최소: 업무복 8표정 + 나머지 3벌 기본·미소·홍조 3표정 = 인물당 17장, 4명이면 **68장**

**1단계: 기본 전신 (의상마다 1장).** A-2의 의상 블록 + [누끼 문단]. 업무복은 아래 블록을 쓴다.
```
Attached is the official character reference. Redraw THIS SAME CHARACTER in the SAME standing pose, same camera angle, same proportions, same face and the SAME office outfit, as a clean new full-body game sprite. Neutral expression.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas.
```

**2단계: 표정 바꾸기 (같은 대화에서 방금 만든 전신을 첨부).**
```
Use the attached image as the exact base. Change ONLY the facial expression to: {EXPRESSION}.
Keep everything else pixel-identical: pose, body, outfit, hair, head position and size, line art, colors, canvas size and position.
TRANSPARENT background, clean cutout, no halo, no shadow.
```
`{EXPRESSION}` 자리에는 A-1의 표정 문장을 하나씩 넣는다. 파일 이름은 `{인물}_{의상}_{표정}_v001.png` 형식이다(예: `yujin_winter_blush_v001.png`).

> A-1 표정 시트는 이 방식으로 바꾸면서 '표정 문장 모음'으로만 쓴다. 시트 그림을 따로 뽑지 않아도 된다.

---

## A. 출시에 꼭 필요한 것

### A-1. 표정 얼굴 시트 — 4장

모든 시트 공통 블록이다. `{EXPRESSIONS}` 자리에 그 인물 칸을 붙인다.

```
Attached is the official character reference. Draw an EXPRESSION SHEET of this exact character's face only.
Keep identical: face shape, eye shape and color, hairstyle, hair color, bangs, art style, line weight, cel shading, lighting direction (soft light from the upper left).
Layout: 4 columns x 2 rows on a plain flat light-gray background, each cell a head-and-shoulders crop facing the viewer at the same slight 3/4 angle and the same scale, collar and ID-card lanyard visible at the bottom edge.
Expressions in order:
{EXPRESSIONS}
Adult woman (late 20s/early 30s office worker), no text, no labels, no extra accessories, no earrings.
```

**`ria_face_sheet_v001.png`**
```
1 neutral – bright closed-mouth smile
2 smile – wide cheerful smile showing teeth
3 laugh – eyes closed, laughing playfully
4 blushing – cheeks flushed, looking away shyly
5 surprised – eyes wide, mouth open
6 pouting – puffed cheeks, sulking
7 sad – drooping brows with a forced small smile
8 serious – no smile, determined look
```

**`jihyun_face_sheet_v001.png`**
```
1 neutral – composed, almost expressionless, neat
2 smile – only the corners of the mouth lifted slightly
3 laugh – trying to hold back a laugh, lips pressed
4 blushing – ears turning red, frozen and stiff
5 surprised – eyebrows raised, a brief pause
6 pouting – sideways look as if arms are crossed
7 sad – eyes lowered, mouth closed tight
8 serious – firm work-mode expression
```

**`yujin_face_sheet_v001.png`** (안경 유지)
```
1 neutral – slightly tense default look, glasses on
2 smile – shy small smile
3 laugh – laughing while covering her mouth with one hand
4 blushing – eyes cast down, face bright red
5 surprised – round eyes behind the glasses
6 pouting – lips pushed out a little
7 sad – eyes glistening, just before tears
8 serious – brave, direct gaze
```

**`seoyun_face_sheet_v001.png`**
```
1 neutral – relaxed, eyes half-lidded
2 smile – teasing playful smile
3 laugh – mischievous laugh as if teasing someone
4 blushing – the teasing stops, a serious quiet blush
5 surprised – eyes widen slightly
6 pouting – half-closed eyes giving a sidelong glare
7 sad – no smile, looking far away
8 serious – no teasing, steady direct gaze
```

### A-2. 의상 전신 — 사복·생활복 8장

```
Attached is the official character reference. Redraw THIS SAME CHARACTER in the SAME standing pose, same camera angle, same proportions and same face, but change only the outfit to: {OUTFIT}.
Keep: hairstyle and hair accessory, eye color, body proportions, art style, line weight, cel shading, light from the upper left.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas, transparent background (or plain white if transparency is unavailable).
Adult woman office worker in her late 20s/early 30s. No ID card for casual/home outfits. No earrings, no extra jewelry, no text.
CUTOUT: TRANSPARENT background, PNG with alpha, crisp clean outline, no white halo, no drop shadow, no ground shadow.
```

| 파일 | `{OUTFIT}` |
|---|---|
| `ria_casual_full_v001.png` | light knit sweater, denim A-line skirt, white sneakers; keep the blue scrunchie in her high ponytail |
| `ria_home_full_v001.png` | oversized hoodie and comfortable shorts, hair let down loosely |
| `jihyun_casual_full_v001.png` | beige trench coat over a burgundy knit, long skirt, ankle boots |
| `jihyun_home_full_v001.png` | soft gray cardigan and long lounge pants, hair half-up |
| `yujin_casual_full_v001.png` | cream blouse with her cardigan, pleated skirt, small crossbody bag; keep her glasses |
| `yujin_home_full_v001.png` | big loose shirt and leggings, a hairpin; keep her glasses |
| `seoyun_casual_full_v001.png` | black slip dress with a thin knit cardigan, simple pumps |
| `seoyun_home_full_v001.png` | silk shirt loungewear set |

### A-3. 의상 전신 — 겨울 외투 4장

`Docs/art-prompts-winter-v001.md`에 인물별 완성 프롬프트가 있다. 그대로 쓴다.

### A-4. 배경 P0 — 12장

```
Visual novel background art drawn in EXACTLY the art style of the attached character references (same line weight, same flat cel shading, same palette warmth), so a character from the reference can stand in it without looking pasted in. Not photorealistic, no 3D render look, no painterly texture.
Scene: {PLACE}, {TIME}.
Setting: contemporary Seoul, Korea; Korean signage only as unreadable shapes.
Camera: eye level (about 150 cm), slightly wide lens, clear empty floor area in the lower center where a standing character will be placed; keep the bottom 28% visually calm (a dialogue box will cover it).
No people, no characters, no text, no watermark. 16:9, 1920x1080.
```

| 파일 | `{PLACE}` | `{TIME}` |
|---|---|---|
| `bg_office_day_v001.png` | a bright open-plan office of a small branding agency, long shared desks with monitors and design proofs, plants, large windows | daytime, soft sunlight |
| `bg_office_evening_v001.png` | (same as above) | evening, golden hour, a few desk lamps on |
| `bg_meeting_day_v001.png` | a small glass-walled meeting room with a long table, wall screen, sticky notes | daytime, soft sunlight |
| `bg_cafe_day_v001.png` | a cozy neighborhood café with wooden tables, window seats, warm pendant lights | daytime, soft sunlight |
| `bg_bookcafe_day_v001.png` | a quiet book café inside a bookstore, tall shelves, reading tables, small bell over the door | daytime, soft sunlight |
| `bg_restaurant_evening_v001.png` | a small neighborhood Korean restaurant with a few tables, menu boards on the wall, steam from the kitchen | evening, warm interior lights |
| `bg_ria_home_night_v001.png` | a cheerful one-room apartment living area with a sofa, a city map pinned on the wall, small plants | night, warm interior lights |
| `bg_jihyun_home_night_v001.png` | a tidy minimalist living room with a shelf of miniature house models and a tea set on a low table | night, warm interior lights |
| `bg_yujin_home_day_v001.png` | an illustrator's apartment corner: desk by a large window, drawing tablet, small music player, art prints | daytime, soft sunlight |
| `bg_seoyun_studio_night_v001.png` | a private writing studio: bookshelves, a soft sofa, a small kitchenette, warm lamps | night, warm interior lights |
| `bg_dohyun_home_night_v001.png` | a modest studio apartment of a young office worker, single bed, desk with a notebook and camera, laundry rack | night, one desk lamp |
| `bg_office_front_evening_v001.png` | the street in front of an office building: crosswalk, bus stop, a bench, convenience store light | evening, golden hour |

### A-5. 장면 CG P1 — 약 17장

```
Visual novel event CG drawn in EXACTLY the art style of the attached references (same line art, eyes, cel shading and palette). 16:9, 1920x1080, full illustration with background.
Characters: {HEROINE} exactly as in the reference (same face, hair, outfit: {OUTFIT}). The male lead appears only as hands/arms or from behind, face never shown.
Scene: {ACTION}, at {PLACE}, {TIME}.
Emotion: {EMOTION}. Camera: {SHOT}.
Adults only. No text, no watermark.
```

#### 프롤로그 — `prologue_hands_v001.png`

인물을 특정하지 않는 그림이라 이 블록만 따로 쓴다. 강리아 마스터만 첨부한다.
```
Visual novel event CG in EXACTLY the art style of the attached reference. 16:9, 1920x1080.
Scene: under a long presentation table in a corporate meeting hall during a tense pitch. Close-up of two hands under the table: a woman's hand gently pressing once on the back of a man's hand that rests on his knee. Above the table edge, blurred papers and a projector glow. No faces visible at all, no sleeves that identify a specific person (plain dark office sleeves).
Mood: tense silence, but the touch says "it's okay". Cool blue projector light from above, warm light on the hands.
No text, no watermark.
```

#### 크리스마스 진엔딩 — 4장

| 파일 | `{HEROINE}` / `{OUTFIT}` | `{ACTION}` | `{PLACE}`, `{TIME}` | `{EMOTION}` | `{SHOT}` |
|---|---|---|---|---|---|
| `ria_x01_scene_v001.png` | Kang Ria / work jumper over her casual outfit, blue scrunchie | sitting on a packing box under the only lit Christmas tree, her back turned while the lead's hands tie a new blue velvet scrunchie in her ponytail | a half-dismantled pop-up store, night | quiet happiness, shoulders relaxing | medium shot from behind and slightly to the side, tree lights bokeh |
| `jihyun_x01_scene_v001.png` | Baek Jihyun / home outfit | holding out a desk calendar where every evening slot of next week is left empty, a small wrapped gift on the table | her tidy living room with the miniature house shelf, late afternoon | shy, trying to stay composed, ears red | medium shot across the low table |
| `yujin_x01_scene_v001.png` | Cha Yujin / home outfit, glasses | showing a drawing of the lead seen from the FRONT for the first time, signed with her real name, holding the sketchbook up | her window-side desk, late afternoon winter light | nervous pride, blushing | over-the-shoulder from the lead, sketchbook in focus |
| `seoyun_x01_scene_v001.png` | Han Seoyun / casual outfit with cardigan | setting two wine glasses side by side on her work table, one of them just taken out of a drawer after three years | her writing studio with a small heater on, evening | soft smile without teasing | medium shot, two glasses in the foreground |

#### 피칭 당일 — 4장

| 파일 | `{HEROINE}` / `{OUTFIT}` | `{ACTION}` | `{PLACE}`, `{TIME}` | `{EMOTION}` | `{SHOT}` |
|---|---|---|---|---|---|
| `ria_r16_scene_v001.png` | Kang Ria / office outfit | asking excitedly "I did best today, right?" with a big grin | an office rooftop at dusk after winning the pitch | proud and happy | medium shot, city skyline behind |
| `jihyun_r16_scene_v001.png` | Baek Jihyun / office outfit | stepping one stair down to meet the lead's eye level and kissing him first | an office emergency stairwell, evening | brave, flustered | side view at stair level, green exit sign |
| `yujin_r16_scene_v001.png` | Cha Yujin / office outfit, glasses | standing at a presentation screen holding a remote, admitting in front of clients that she is the artist behind a popular anonymous illustration account | a corporate presentation hall, daytime | scared but determined | medium shot from the audience side, the lead's back visible nodding |
| `seoyun_r16_scene_v001.png` | Han Seoyun / office outfit | linking her arm with the lead's in front of the elevators after the pitch, not hiding anymore | client company elevator lobby, evening | calm, free | full shot from a slight distance |

#### 고백 (각 R04) — 4장

| 파일 | `{HEROINE}` / `{OUTFIT}` | `{ACTION}` | `{PLACE}`, `{TIME}` | `{EMOTION}` | `{SHOT}` |
|---|---|---|---|---|---|
| `ria_r04_scene_v001.png` | Kang Ria / casual | standing close on a quiet street after the confession, smiling softly | quiet residential street, evening | relieved, warm | medium two-shot, lead from behind |
| `jihyun_r04_scene_v001.png` | Baek Jihyun / casual | letting go of her water cup to answer the confession seriously, looking straight at him | small café near the office, evening | serious, sincere | across-the-table shot |
| `yujin_r04_scene_v001.png` | Cha Yujin / casual, glasses | closing the menu and taking a breath before confessing first | café, evening | nervous courage | across-the-table, slightly low angle |
| `seoyun_r04_scene_v001.png` | Han Seoyun / casual | putting her cup down and looking at him without any joke | book café, evening | quiet, earnest | close medium shot |

#### 기존 CSV의 P1 중 남은 것

`Docs/scene-cg-production-v001.csv`에서 P1이면서 위에 없는 장면들이다. 하나씩 `{ACTION}`에 CSV의 '대본지문'을 영어로 옮겨 넣는다.
- 리아 R07 우산, R11 요리
- 지현 R10 부품 받치기, R11 카드게임
- 유진 R02 전시, O02 스케치
- 서윤 R02 북카페, R10 케이크, R13 수첩

---

## B. 다음 단계 (P2) — 이번에 새로 생긴 장면 22장

A-5와 같은 CG 블록을 쓴다.

### 진엔딩 1월 장면 X02 — 4장

| 파일 | `{HEROINE}` / `{OUTFIT}` | `{ACTION}` | `{PLACE}`, `{TIME}` | `{SHOT}` |
|---|---|---|---|---|
| `ria_x02_scene_v001.png` | Ria / winter coat | taking the lead's hand openly at a crosswalk as the light turns green | street, winter evening | from behind, both walking |
| `jihyun_x02_scene_v001.png` | Jihyun / winter coat | pressing the lead's hand once under the bus-stop light as the bus arrives | bus stop, winter night | side medium shot |
| `yujin_x02_scene_v001.png` | Yujin / office outfit, glasses | showing a sketch of two hands overlapping under a table, titled in pencil | office corridor end window, winter dusk | over-the-shoulder |
| `seoyun_x02_scene_v001.png` | Seoyun / winter coat | looking straight at the lead across two lattes, not joking | café by the window, winter evening | across-the-table |

### 크리스마스 아침 — 4장

`{ACTION}` 하나를 네 명 모두에게 쓴다. 장소만 각자의 집으로 바꾼다.
```
morning after Christmas Eve, sitting at the window with a warm mug, sleepy relaxed smile toward the lead
```

### 특별 장면 — 8장

| 파일 | `{ACTION}` | `{PLACE}`, `{TIME}` |
|---|---|---|
| `ria_sp1_v001.png` | leaning her head on the lead's shoulder on plastic chairs while laundry spins | coin laundromat, afternoon |
| `ria_sp2_v001.png` | holding an unopened coffee can, asking a "what if" question with a forced smile | office rooftop, night |
| `jihyun_sp1_v001.png` | looking through a loupe at a small glue smudge on a miniature railing, smiling softly | her living room desk, afternoon |
| `jihyun_sp2_v001.png` | asleep on the sofa, face peaceful, the lead holding her phone | her living room, evening lamp |
| `yujin_sp1_v001.png` | sketching the lead's hand resting on a bench back | park bench, afternoon |
| `yujin_sp2_v001.png` | showing a laptop folder full of drawings of the same man's back, nervous | her desk, night |
| `seoyun_sp1_v001.png` | reading a thin book aloud into her phone in bed, lamp on | her bedroom corner, midnight |
| `seoyun_sp2_v001.png` | folding shirts into a small suitcase, laughing at her own joke | her studio, late night |

### 숨은 이야기 "이듬해 봄" — 2장

네 마스터를 모두 첨부한다.

| 파일 | `{ACTION}` | `{PLACE}`, `{TIME}` |
|---|---|---|
| `spring_rooftop_v001.png` | all four heroines and the lead (from behind) on the rooftop, everyone tapping the shoulder of the person next to them, laughing | office rooftop, spring evening |
| `spring_pitch_v001.png` | a presentation screen showing six names in the same size, the four heroines standing in a row in front of it | presentation hall, spring daytime |

### 새 배경 — 7장

A-4의 배경 블록을 쓴다.

| 파일 | `{PLACE}` | `{TIME}` |
|---|---|---|
| `bg_train_day_v001.png` | inside a Korean intercity train car, aisle between two seat rows | daytime |
| `bg_subway_night_v001.png` | inside a Seoul subway car with hand straps and a route map | night |
| `bg_laundromat_v001.png` | small neighborhood coin laundromat, front-loading machines, plastic chairs | afternoon |
| `bg_stair_landing_v001.png` | office stairwell landing with a tall window, light falling across three steps | noon |
| `bg_corridor_window_v001.png` | end of an office corridor with a large window, long sunbeam on the floor | late afternoon / winter dusk |
| `bg_art_store_v001.png` | old art supply store in an alley, paper racks, pencils, brushes | evening |
| `bg_bookfair_v001.png` | small indie zine fair, folding-table booths with postcards | daytime |

---

## C. 나중에 (P3)

나머지 배경과 일상 CG는 v001 문서 4장과 5장 목록, CSV의 P2·P3를 같은 블록으로 만든다. 일반 엔딩 1월 장면(N02)은 배경과 입상으로 대신해도 된다.

## 받은 뒤

- `CharacterArt/candidates/chatgpt-v001/`에 파일 이름 그대로 넣는다.
- 다음 세션에서 Claude에게 "그림 연결해 줘"라고 하면 게임에 넣는다.
- 챗지피티 이미지의 상업적 이용 조건은 사용 전에 직접 확인한다.
