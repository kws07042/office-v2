# 성인 이벤트 도입 CG 프롬프트 v001 (속옷 전신 장면)

성인 이벤트(`adult_event_cg_plan_v1.json`)마다 본 장면 바로 앞에 나오는 **도입 CG(intro_cg)** 용이다. 속옷만 입은 상태이고 노출·성행위는 없다. 배경은 [친밀 장면 브리프](intimate-scene-briefs-v001.md)의 직전 상황을 따른다.
- 등장인물: 리아 28, 유진 27, 지현 30, 서윤 32. 모두 성인 직장인이다.
- 결과물은 후보다. `vn-art-qa` 검수와 사용자 승인 전에는 게임에 연결하지 않는다.
- 저장 경로는 계획서의 `images/events/<who>/<id>_intro.png` 규칙을 따른다.

## 먼저 붙여 넣을 공통 블록 (대화 시작에 한 번)

```text
You will draw intro CGs for an adult office-romance visual novel. Reference repository: github.com/kws07042/office-v2

ART STYLE (absolute): match the master sprites exactly — CharacterArt/candidates/heroine-masters-v001/*.png. Same line weight, same cel shading, same eye rendering and highlights, same hair strand rendering, soft light. Do not reinterpret faces or hair.
CHARACTERS (all adult women, 27–32, office workers; mature adult proportions, never childlike):
- Kang Ria (28): very long wavy blonde hair in a high ponytail with a BLUE scrunchie, straight bangs, BLUE eyes, slim face. Ref: ria_office_pose01_neutral_v001.png
- Baek Jihyun (30): very long crimson hair falling straight down the back (not flared out), side-parted bangs, reddish-brown eyes with confident sharp eyeliner, no beauty mark. Ref: jihyun_office_pose01_neutral_v001.png
- Cha Yujin (27): silver-white bob (front slightly longer), side-swept bangs, ONE gold hairpin, thin round metal glasses (always on), amber-brown eyes, mature curvy figure. Ref: yujin_office_pose01_neutral_v001.png
- Han Seoyun (32): long wavy dark plum / deep purple hair, half-lidded grey-lavender eyes, beauty mark under her LEFT eye, slim oval face. Ref: seoyun_office_pose01_neutral_v001.png
No earrings, piercings, necklaces or rings unless stated.

FORMAT: 16:9 landscape, 1920x1080, full-body or knee-up of ONE heroine, the viewer is her boyfriend standing in front of her (no man visible). Background drawn in the same anime style as the game backgrounds (Source/game/images/bg/). No text, no logos, no watermark, no UI.
CONTENT LIMIT: she wears only a matching bra and panties that fully cover; tasteful, romantic, intimate mood right before an intimate scene. No nudity, no see-through fabric, no nipples, no sexual act, no explicit pose.
```

## 리아

### ria_R07_casual_intro · 비 오는 토요일 밤, 리아의 집 (첫 밤)
```text
Kang Ria, ria_R07_casual_intro. Her apartment at night, rain streaking the window, warm bedside lamp, background ref bg_ria_home.jpg. Her cream cable-knit sweater and denim mini skirt lie folded hastily on the chair. She wears a pastel sky-blue cotton bra and panties with thin white lace trim (matching her blue scrunchie). Pose: sitting on the edge of the bed, hugging a round cushion half against her stomach, knees together, toes touching. Expression: laughing nervously to hide her nerves, cheeks pink, eyes looking straight at the viewer. Mood: "no umbrella excuse anymore" — playful but shy first night.
```

### ria_R12_special_intro · 토요일 밤, 리아의 집 (일주일 쌓인 그리움)
```text
Kang Ria, ria_R12_special_intro. Her apartment, late evening, fairy string lights over the headboard, background ref bg_ria_home.jpg. The date outfit she chose for him is draped over the bed. She wears a white lace bra and panties with small blue satin ribbons. Pose: standing, hands clasped behind her back, leaning forward slightly at the waist, weight on one leg. Expression: teasing proud grin with a deep blush, as if asking "you noticed, right?", eyes slightly glossy with longing. Mood: missed him all week, hiding a worry behind the smile.
```

### ria_R15_home_intro · 일요일 저녁, 리아의 집 (화해 후 먼저 다가감)
```text
Kang Ria, ria_R15_home_intro. Her apartment on Sunday evening, dusky orange light through the curtains, her grey oversized hoodie dropped on the floor, background ref bg_ria_home.jpg. Hair down from the ponytail, blue scrunchie on her wrist. She wears a navy satin bra and panties. Pose: kneeling on the bed, one hand reaching out toward the viewer, palm open. Expression: no joke at all — soft serious smile, steady eye contact, a slight tremble at the lips. Mood: trust rebuilt after a fight; she moves first.
```

### ria_O04_intro · 포차 뒤 역 앞 모텔 (충동과 수줍음 반반)
```text
Kang Ria, ria_O04_intro. A small station-front motel room at night, pink-and-blue neon from the sign outside through the blinds, background ref bg_motel.jpg. She wears a simple black cotton bra and panties. Pose: standing just inside the door, back lightly against it, one arm crossed over her stomach, the other hand fiddling with her ponytail. Expression: half-tipsy flush, sidelong shy glance, embarrassed little laugh. Mood: she pointed at the sign first and now is suddenly shy.
```

## 지현

### jihyun_R07_casual_intro · 금요일 밤, 지현의 집 (싸운 다음 날의 화해)
```text
Baek Jihyun, jihyun_R07_casual_intro. Her tidy minimal apartment at night, the small wooden window-frame model they assembled sits on the side table, city lights through the window, background ref bg_jihyun_home.jpg. Her camel trench coat and burgundy turtleneck hang neatly on a chair. She wears a deep burgundy satin bra and panties. Pose: standing by the window, arms loosely crossed under her chest, weight on one hip, long crimson hair over one shoulder. Expression: direct, calm gaze at the viewer, faint blush, lips slightly parted — she just said she wanted him. Mood: tension after the argument melting into honesty.
```

### jihyun_R12_special_intro · 금요일 밤, 지현의 집 (참았던 것의 해소)
```text
Baek Jihyun, jihyun_R12_special_intro. Her apartment, warm low lamp light, the date outfit she asked him to notice lies on the sofa, background ref bg_jihyun_home.jpg. She wears a black lace bra and panties. Pose: sitting on the arm of the sofa, legs crossed, one hand gripping the edge of the cushion, face turned half away. Expression: flustered after a compliment — red ears, eyes darting aside, trying to keep her composed team-leader face and failing. Mood: "Friday, not the hallway" — finally alone.
```

### jihyun_R15_home_intro · 지현의 집 (처음으로 기대는 밤)
```text
Baek Jihyun, jihyun_R15_home_intro. Her bedroom late at night, one bedside lamp, rumpled blanket, background ref bg_jihyun_home.jpg. She wears an ivory silk bra and panties. Pose: lying on her side on the bed, head resting on her bent arm, other hand lightly patting the empty space beside her. Expression: relieved, gentle half-closed eyes, small unguarded smile — the first time she lets herself lean on someone. Mood: quiet, warm, exhausted relief.
```

## 유진

### yujin_R07_casual_intro · 토요일 밤, 유진의 집 (비밀을 보여 준 첫 밤)
```text
Cha Yujin, yujin_R07_casual_intro. Her small apartment at night, sketchbooks and the "창가" (window) drawings pinned on the wall, thin curtains, desk lamp, background ref bg_yujin_home.jpg. Her cream cardigan and brown pleated skirt are folded on the desk chair. She wears a pale peach cotton bra and panties with tiny lace edges, glasses on, gold hairpin in. Pose: standing near the curtained window, both hands clasped at her chest, shoulders slightly raised. Expression: trembling shy smile, looking up at the viewer through her glasses, deep blush. Mood: "my hands are cold, right?" — nervous first night with the one person who knows her secret.
```

### yujin_R12_special_intro · 목요일 밤, 유진의 집 (메시지가 아니라 진짜)
```text
Cha Yujin, yujin_R12_special_intro. Her apartment late at night after the deadline week, empty coffee cups and a tablet on the desk, background ref bg_yujin_home.jpg. The new outfit she spent a long time choosing is laid on the bed. She wears a sage-green lace bra and panties, glasses on. Pose: sitting on a floor cushion, legs folded to one side, her phone held against her chest with both hands. Expression: relieved happy smile with slightly teary eyes, looking up at the viewer. Mood: real presence instead of messages.
```

### yujin_R15_home_intro · 유진의 집 (연습한 말을 잊음)
```text
Cha Yujin, yujin_R15_home_intro. Her apartment in the evening, soft window light fading to blue, a note with her practiced words crumpled on the desk, background ref bg_yujin_home.jpg. She wears a soft heather-grey cotton bra and panties, glasses on. Pose: taking one step toward the viewer, one hand reaching forward, the other hand half-raised in a flustered gesture. Expression: mouth open mid-sentence, eyes wide, blushing — she tried to lead and forgot her lines halfway. Mood: cute, earnest, a little comedic.
```

## 서윤

### seoyun_R07_casual_intro · 토요일 밤, 서윤의 개인 작업실 (장난이 멈춘 서윤)
```text
Han Seoyun, seoyun_R07_casual_intro. Her private work studio at night (not a family home), a large worktable with copy drafts and a desk lamp, bookshelves, background ref bg_seoyun_studio.jpg. Her grey knit dress and beige cardigan hang over the chair. She wears a dusty plum lace bra and panties. Pose: leaning back against the worktable edge, both hands on the table, one knee slightly bent. Expression: no teasing at all — serious, earnest, unsmiling gaze straight at the viewer, cheeks faintly flushed. Mood: she ran to catch him; wants to overwrite the past.
```

### seoyun_R12_special_intro · 금요일 밤, 작업실 (대답 못 한 채 곁에 있고 싶음)
```text
Han Seoyun, seoyun_R12_special_intro. Her studio late at night, rain-free city lights through a tall window, a low daybed with a throw blanket, background ref bg_seoyun_studio.jpg. She wears a black satin bra and panties with her signature garter belt and black lace-band thigh-high socks. Pose: sitting on the daybed hugging her knees, chin resting on them. Expression: a soft, slightly guilty smile, eyes looking up at the viewer from under her lashes. Mood: she couldn't answer his question yet, but wants to be beside him tonight.
```

### seoyun_R15_home_intro · 작업실 (숨길 게 없어진 첫 밤)
```text
Han Seoyun, seoyun_R15_home_intro. Her studio at night in warm lamp light, papers put away, the space tidy and calm, background ref bg_seoyun_studio.jpg. She wears a lavender silk bra and panties. Pose: lying back on the daybed, one arm above her head, long plum hair spread across the cushion, knees drawn up and tilted to one side. Expression: the most relaxed open smile in the game, eyes gentle, calling him "도현아" with her look. Mood: nothing left to hide; completely at ease.
```

## 검수 메모 (받은 뒤)
- 얼굴·머리·눈 색·매력점·안경·머리핀이 마스터와 같은지 확인한다.
- 속옷이 비치지 않는지, 손가락 수, 어려 보이는 비율이 없는지 확인한다.
- 배경 소품이 직전 대본과 맞는지 확인한다: 리아 R07 비, 지현 R07 창틀 조립품, 유진 R07 '창가' 그림, 서윤은 가족 물건 없음.
