# ChatGPT 붙여 넣기 묶음 — 첨부 없음 v002 (2026-11-20)

그림 첨부 없이 글만 붙여 넣는 판이다. 얼굴·옷은 지금 게임 입상을 보고 글로 적었다.

**쓰는 법**
1. ChatGPT에서 새 대화를 연다.
2. 코드 상자 안의 글을 통째로 복사해서 보낸다. 1번 그림이 나온다.
3. 마음에 들면 `다음`, 다시 원하면 `다시`. 고칠 점은 한 줄로 적는다. 예: `손가락 다시, 머리색 더 진하게`
4. ChatGPT가 그림 아래 적어 준 파일 이름으로 저장한다.
5. 묶음 하나 = 대화 하나. 중간에 그림체가 흐려지면 새 대화에 같은 글을 보내고 `N번부터`라고 한다.

**알아 둘 점**: 첨부가 없으면 얼굴과 그림체가 기존 입상과 조금씩 달라진다. 받은 뒤 집에서 ComfyUI로 마스터 그림체에 맞춘다(`home-comfyui-checklist.md`). 울먹 표정은 기존 입상의 얼굴만 바꿀 수 없어서, 두 손을 가슴 앞에 모은 별도 자세로 뽑는다.

| 순서 | 묶음 | 장수 |
|---|---|---:|
| 1 | 백지현 입상 (두 번째 포즈 + 표정 + 울먹) | 14 |
| 2 | 차유진 입상 (두 번째 포즈 + 표정 + 울먹) | 14 |
| 3 | 리아·서윤 울먹 표정 | 4 |
| 4 | 강리아 장면 CG | 14 |
| 5 | 백지현 장면 CG | 14 |
| 6 | 차유진 장면 CG | 14 |
| 7 | 한서윤 장면 CG | 14 |
| 8 | 공통 CG·타이틀 | 6 |
| | **합계** | **94** |

## 1. 백지현 입상 (두 번째 포즈 + 표정 + 울먹) — 14장

````text
ART STYLE (keep identical in every image of this conversation):
Polished commercial Korean/Japanese anime visual-novel illustration. Clean thin uniform dark-brown lineart, no sketchy or painterly lines. Soft cel shading with one shadow tone and small crisp highlights. Large glossy anime eyes with gradient irises and bright catchlights. Warm, slightly pastel palette, light from the upper left. Mature, attractive adult women in their late 20s to early 30s with realistic adult proportions. Do NOT use semi-realism, 3D, photo textures, painterly brushwork, heavy glow or chibi proportions.

CHARACTER: Baek Jihyun — very long wavy crimson-red hair with side-swept bangs, red-brown eyes, cool composed face, team-leader presence

RULES FOR THIS CONVERSATION
- Make exactly ONE image per reply, in the numbered order below. Start with #1 now.
- Under each image write only its file name.
- When I say "다음", make the next number. "다시" = redo the same number. Any other short note = fix that and redo.
- Every image is a full-body game sprite from the top of the head to the shoes, centered on a vertical 2:3 canvas, head near the top, same scale in every image. Natural hands with five fingers. No text except the ID badge.
- Items marked "BASE = #n" must use image #n from THIS conversation as the exact base: change ONLY what is written, keep pose, body, outfit, hair, head position and size, line art, colors and canvas pixel-identical.
- End every image with: CUTOUT: TRANSPARENT background (PNG with alpha), or plain flat light-gray #C8C8C8 if transparency is unavailable. Crisp clean outline, no halo, no drop shadow, no ground shadow, no floor line. Nothing else in the image.

LIST

#1  jihyun_casual_pose02_neutral_v001.png
OUTFIT: beige belted trench coat over a burgundy cable-knit turtleneck, long dark plum A-line skirt, brown ankle boots
POSE: holding the strap of her shoulder bag with both hands in front of her, head tilted slightly
EXPRESSION: calm neutral, mouth closed.

#2  jihyun_casual_pose02_smile_v001.png
BASE = #1. Change ONLY the facial expression to: a gentle warm smile, mouth slightly curved, eyes soft.

#3  jihyun_casual_pose02_blush_v001.png
BASE = #1. Change ONLY the facial expression to: a shy smile with clear pink blush across both cheeks, eyes glancing slightly aside.

#4  jihyun_casual_pose02_serious_v001.png
BASE = #1. Change ONLY the facial expression to: a serious focused look, eyebrows slightly lowered, mouth in a straight line.

#5  jihyun_casual_pose02_sad_v001.png
BASE = #1. Change ONLY the facial expression to: a sad look, inner eyebrows raised, eyes lowered, small downturned mouth.

#6  jihyun_casual_pose02_surprise_v001.png
BASE = #1. Change ONLY the facial expression to: surprised, eyes wide open, eyebrows raised, small open mouth.

#7  jihyun_home_pose02_neutral_v001.png
OUTFIT: hair in a loose half-up bun, soft taupe-gray long cardigan over a cream top, matching wide lounge pants, cream slippers
POSE: holding a warm mug with both hands at chest height, shoulders relaxed
EXPRESSION: calm neutral, mouth closed.

#8  jihyun_home_pose02_smile_v001.png
BASE = #7. Change ONLY the facial expression to: a gentle warm smile, mouth slightly curved, eyes soft.

#9  jihyun_home_pose02_blush_v001.png
BASE = #7. Change ONLY the facial expression to: a shy smile with clear pink blush across both cheeks, eyes glancing slightly aside.

#10  jihyun_home_pose02_serious_v001.png
BASE = #7. Change ONLY the facial expression to: a serious focused look, eyebrows slightly lowered, mouth in a straight line.

#11  jihyun_home_pose02_sad_v001.png
BASE = #7. Change ONLY the facial expression to: a sad look, inner eyebrows raised, eyes lowered, small downturned mouth.

#12  jihyun_home_pose02_surprise_v001.png
BASE = #7. Change ONLY the facial expression to: surprised, eyes wide open, eyebrows raised, small open mouth.

#13  jihyun_casual_teary_v001.png
OUTFIT: beige belted trench coat over a burgundy cable-knit turtleneck, long dark plum A-line skirt, brown ankle boots
POSE: standing with both hands clasped loosely at her chest, shoulders slightly drawn in
EXPRESSION: teary-eyed, eyes glistening with tears that have not fallen yet, inner eyebrows raised, lips pressed together as if holding back crying, faint pink on the nose and cheeks.

#14  jihyun_office_teary_v001.png
OUTFIT: charcoal-black tailored blazer, burgundy shirt, black belt, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
POSE: standing with both hands clasped loosely at her chest, shoulders slightly drawn in
EXPRESSION: teary-eyed, eyes glistening with tears that have not fallen yet, inner eyebrows raised, lips pressed together as if holding back crying, faint pink on the nose and cheeks.
````

## 2. 차유진 입상 (두 번째 포즈 + 표정 + 울먹) — 14장

````text
ART STYLE (keep identical in every image of this conversation):
Polished commercial Korean/Japanese anime visual-novel illustration. Clean thin uniform dark-brown lineart, no sketchy or painterly lines. Soft cel shading with one shadow tone and small crisp highlights. Large glossy anime eyes with gradient irises and bright catchlights. Warm, slightly pastel palette, light from the upper left. Mature, attractive adult women in their late 20s to early 30s with realistic adult proportions. Do NOT use semi-realism, 3D, photo textures, painterly brushwork, heavy glow or chibi proportions.

CHARACTER: Cha Yujin — light silver-gray bob with a small gold hairpin, thin round metal glasses, warm amber eyes, shy gentle face

RULES FOR THIS CONVERSATION
- Make exactly ONE image per reply, in the numbered order below. Start with #1 now.
- Under each image write only its file name.
- When I say "다음", make the next number. "다시" = redo the same number. Any other short note = fix that and redo.
- Every image is a full-body game sprite from the top of the head to the shoes, centered on a vertical 2:3 canvas, head near the top, same scale in every image. Natural hands with five fingers. No text except the ID badge.
- Items marked "BASE = #n" must use image #n from THIS conversation as the exact base: change ONLY what is written, keep pose, body, outfit, hair, head position and size, line art, colors and canvas pixel-identical.
- End every image with: CUTOUT: TRANSPARENT background (PNG with alpha), or plain flat light-gray #C8C8C8 if transparency is unavailable. Crisp clean outline, no halo, no drop shadow, no ground shadow, no floor line. Nothing else in the image.

LIST

#1  yujin_casual_pose02_neutral_v001.png
OUTFIT: peach-cream cable-knit cardigan over a cream collared blouse, brown pleated mini skirt, small beige crossbody bag, brown pantyhose, black pumps
POSE: holding a small sketchbook to her chest with both arms, body turned slightly to the side
EXPRESSION: calm neutral, mouth closed.

#2  yujin_casual_pose02_smile_v001.png
BASE = #1. Change ONLY the facial expression to: a gentle warm smile, mouth slightly curved, eyes soft.

#3  yujin_casual_pose02_blush_v001.png
BASE = #1. Change ONLY the facial expression to: a shy smile with clear pink blush across both cheeks, eyes glancing slightly aside.

#4  yujin_casual_pose02_serious_v001.png
BASE = #1. Change ONLY the facial expression to: a serious focused look, eyebrows slightly lowered, mouth in a straight line.

#5  yujin_casual_pose02_sad_v001.png
BASE = #1. Change ONLY the facial expression to: a sad look, inner eyebrows raised, eyes lowered, small downturned mouth.

#6  yujin_casual_pose02_surprise_v001.png
BASE = #1. Change ONLY the facial expression to: surprised, eyes wide open, eyebrows raised, small open mouth.

#7  yujin_home_pose02_neutral_v001.png
OUTFIT: oversized white button-up shirt worn as loungewear, black leggings, cream slippers
POSE: hugging a soft cushion in front of her, one foot slightly behind the other
EXPRESSION: calm neutral, mouth closed.

#8  yujin_home_pose02_smile_v001.png
BASE = #7. Change ONLY the facial expression to: a gentle warm smile, mouth slightly curved, eyes soft.

#9  yujin_home_pose02_blush_v001.png
BASE = #7. Change ONLY the facial expression to: a shy smile with clear pink blush across both cheeks, eyes glancing slightly aside.

#10  yujin_home_pose02_serious_v001.png
BASE = #7. Change ONLY the facial expression to: a serious focused look, eyebrows slightly lowered, mouth in a straight line.

#11  yujin_home_pose02_sad_v001.png
BASE = #7. Change ONLY the facial expression to: a sad look, inner eyebrows raised, eyes lowered, small downturned mouth.

#12  yujin_home_pose02_surprise_v001.png
BASE = #7. Change ONLY the facial expression to: surprised, eyes wide open, eyebrows raised, small open mouth.

#13  yujin_casual_teary_v001.png
OUTFIT: peach-cream cable-knit cardigan over a cream collared blouse, brown pleated mini skirt, small beige crossbody bag, brown pantyhose, black pumps
POSE: standing with both hands clasped loosely at her chest, shoulders slightly drawn in
EXPRESSION: teary-eyed, eyes glistening with tears that have not fallen yet, inner eyebrows raised, lips pressed together as if holding back crying, faint pink on the nose and cheeks.

#14  yujin_office_teary_v001.png
OUTFIT: peach-cream cable-knit cardigan over a white blouse, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
POSE: standing with both hands clasped loosely at her chest, shoulders slightly drawn in
EXPRESSION: teary-eyed, eyes glistening with tears that have not fallen yet, inner eyebrows raised, lips pressed together as if holding back crying, faint pink on the nose and cheeks.
````

## 3. 리아·서윤 울먹 표정 — 4장

````text
ART STYLE (keep identical in every image of this conversation):
Polished commercial Korean/Japanese anime visual-novel illustration. Clean thin uniform dark-brown lineart, no sketchy or painterly lines. Soft cel shading with one shadow tone and small crisp highlights. Large glossy anime eyes with gradient irises and bright catchlights. Warm, slightly pastel palette, light from the upper left. Mature, attractive adult women in their late 20s to early 30s with realistic adult proportions. Do NOT use semi-realism, 3D, photo textures, painterly brushwork, heavy glow or chibi proportions.

RULES FOR THIS CONVERSATION
- Make exactly ONE image per reply, in the numbered order below. Start with #1 now.
- Under each image write only its file name.
- When I say "다음", make the next number. "다시" = redo the same number. Any other short note = fix that and redo.
- Every image is a full-body game sprite from the top of the head to the shoes, centered on a vertical 2:3 canvas, head near the top, same scale in every image. Natural hands with five fingers. No text except the ID badge.
- Items marked "BASE = #n" must use image #n from THIS conversation as the exact base: change ONLY what is written, keep pose, body, outfit, hair, head position and size, line art, colors and canvas pixel-identical.
- End every image with: CUTOUT: TRANSPARENT background (PNG with alpha), or plain flat light-gray #C8C8C8 if transparency is unavailable. Crisp clean outline, no halo, no drop shadow, no ground shadow, no floor line. Nothing else in the image.

LIST

#1  ria_casual_teary_v001.png
CHARACTER: Kang Ria — honey-blonde very long wavy hair in a high ponytail tied with a blue scrunchie, straight blunt bangs, bright blue eyes, cheerful energetic face
OUTFIT: cream cable-knit sweater, blue denim mini skirt, brown pantyhose, white sneakers
POSE: standing with both hands clasped loosely at her chest, shoulders slightly drawn in
EXPRESSION: teary-eyed, eyes glistening with tears that have not fallen yet, inner eyebrows raised, lips pressed together as if holding back crying, faint pink on the nose and cheeks.

#2  ria_office_teary_v001.png
CHARACTER: Kang Ria — honey-blonde very long wavy hair in a high ponytail tied with a blue scrunchie, straight blunt bangs, bright blue eyes, cheerful energetic face
OUTFIT: white button-up shirt with rolled sleeves, black pencil skirt, sheer black pantyhose, black pumps, company ID badge on a lanyard
POSE: standing with both hands clasped loosely at her chest, shoulders slightly drawn in
EXPRESSION: teary-eyed, eyes glistening with tears that have not fallen yet, inner eyebrows raised, lips pressed together as if holding back crying, faint pink on the nose and cheeks.

#3  seoyun_casual_teary_v001.png
CHARACTER: Han Seoyun — very long wavy dark plum-black hair with a pink inner color streak, half-lidded blue-violet eyes, small mole under her left eye, teasing confident face
OUTFIT: gray ribbed knit midi dress with a scoop neckline and side slit, long beige open cardigan, bare legs, white sneakers
POSE: standing with both hands clasped loosely at her chest, shoulders slightly drawn in
EXPRESSION: teary-eyed, eyes glistening with tears that have not fallen yet, inner eyebrows raised, lips pressed together as if holding back crying, faint pink on the nose and cheeks.

#4  seoyun_office_teary_v001.png
CHARACTER: Han Seoyun — very long wavy dark plum-black hair with a pink inner color streak, half-lidded blue-violet eyes, small mole under her left eye, teasing confident face
OUTFIT: lavender shirt with rolled sleeves, black belt, navy mini pencil skirt, black lace-top thigh-high stockings, black pumps, company ID badge on a lanyard
POSE: standing with both hands clasped loosely at her chest, shoulders slightly drawn in
EXPRESSION: teary-eyed, eyes glistening with tears that have not fallen yet, inner eyebrows raised, lips pressed together as if holding back crying, faint pink on the nose and cheeks.
````

## 4. 강리아 장면 CG — 14장

````text
ART STYLE (keep identical in every image of this conversation):
Polished commercial Korean/Japanese anime visual-novel illustration. Clean thin uniform dark-brown lineart, no sketchy or painterly lines. Soft cel shading with one shadow tone and small crisp highlights. Large glossy anime eyes with gradient irises and bright catchlights. Warm, slightly pastel palette, light from the upper left. Mature, attractive adult women in their late 20s to early 30s with realistic adult proportions. Do NOT use semi-realism, 3D, photo textures, painterly brushwork, heavy glow or chibi proportions.

CHARACTER: Kang Ria — honey-blonde very long wavy hair in a high ponytail tied with a blue scrunchie, straight blunt bangs, bright blue eyes, cheerful energetic face

RULES FOR THIS CONVERSATION
- Make exactly ONE image per reply, in the numbered order below. Start with #1 now.
- Under each image write only its file name.
- When I say "다음", make the next number. "다시" = redo the same number. Any other short note = fix that and redo.
- Every image: visual novel event CG, 16:9 landscape 1920x1080, full illustration WITH a detailed background.
- Keep the heroine's face, hair color, eye color and the given outfit exactly the same in every image.
- The male lead is the camera (first-person view). Never draw his face or full body. Only his hands or forearm may appear when the action needs it (sleeve given per item).
- Adults only. Natural hands with five fingers. No text, no logos, no watermark, no speech bubbles.
- Scene descriptions are in Korean; follow them literally.

LIST

#1  ria_r04_scene_v001.png
OUTFIT: white button-up shirt with rolled sleeves, black pencil skirt, sheer black pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 고백 뒤 가까이 서서 부드럽게 웃는 순간
PLACE/TIME: 금요일 저녁 · 조명이 켜진 산책길

#2  ria_r07_scene_v001.png
OUTFIT: cream cable-knit sweater, blue denim mini skirt, brown pantyhose, white sneakers
SLEEVE: plain gray knit sleeve
SCENE: 카페를 나서며 리아가 우산을 펴려다 멈췄다. 문 위 차양에서 떨어진 물이 우산보다 먼저 신발에 닿았다. 주인공이 웃음을 참자 리아가 우산을 주인공 쪽으로 내밀었다.
PLACE/TIME: 토요일 오후 · 비가 내리는 동네 카페

#3  ria_r11_scene_v001.png
OUTFIT: oversized white hoodie, gray dolphin shorts with white trim, bare legs, gray slippers
SLEEVE: plain gray knit sleeve
SCENE: 리아가 면을 건지는 동안 주인공은 소스를 저었다. 각자 다른 작은 숟가락으로 맛을 보고 소금을 조금 더 넣었다.
PLACE/TIME: 그 주 일요일 저녁 · 리아의 집

#4  ria_r16_scene_v001.png
OUTFIT: white button-up shirt with rolled sleeves, black pencil skirt, sheer black pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 피칭에 이긴 날 해 질 무렵. 리아가 옥상 난간에 기대 길게 숨을 내쉬고, 돌아보며 크게 웃는다. "나 오늘 제일 잘했지? 솔직하게." 뒤로 노을 진 도시.
PLACE/TIME: 피칭 당일 저녁 · 회사 옥상

#5  ria_x01_scene_v001.png
OUTFIT: cream wool short coat open over a white shirt, light-blue knit scarf, black pencil skirt, black pantyhose, black pumps
SLEEVE: plain gray knit sleeve
SCENE: 반쯤 해체된 팝업 행사장, 불이 켜진 트리 하나 아래. 리아가 포장 상자에 등을 돌리고 앉아 있고, 주인공의 손이 포니테일에 새 파란 벨벳 슈슈를 서툴게 감는다. 붕어빵 봉투가 옆에.
PLACE/TIME: 12월 24일 밤 · 철수 중인 팝업 행사장

#6  ria_x02_scene_v001.png
OUTFIT: cream wool short coat open over a white shirt, light-blue knit scarf, black pencil skirt, black pantyhose, black pumps
SLEEVE: plain gray knit sleeve
SCENE: 파란불로 바뀌는 횡단보도 앞, 리아가 반 발짝 앞에서 돌아보며 주인공의 손을 잡아끈다. 새 파란 슈슈를 한 포니테일이 흔들린다.
PLACE/TIME: 1월 평일 저녁 · 퇴근길 횡단보도

#7  ria_x01b_scene_v001.png
OUTFIT: oversized white hoodie, gray dolphin shorts with white trim, bare legs, gray slippers
SLEEVE: plain gray knit sleeve
SCENE: 크리스마스 다음 날 아침. 리아가 창가에서 머그를 들고 졸린 얼굴로 돌아보며 웃는다. 삐뚤게 감긴 파란 슈슈.
PLACE/TIME: 12월 25일 아침 · 리아의 집

#8  ria_sp1_scene_v001.png
OUTFIT: cream cable-knit sweater, blue denim mini skirt, brown pantyhose, white sneakers
SLEEVE: plain gray knit sleeve
SCENE: 코인 세탁방 플라스틱 의자에 나란히 앉아, 리아가 주인공의 어깨에 머리를 기댄다. 돌아가는 세탁기 창, 주인공 손바닥 위에 리아의 휴대폰.
PLACE/TIME: 일요일 오후 · 동네 코인 세탁방

#9  ria_sp2_scene_v001.png
OUTFIT: white button-up shirt with rolled sleeves, black pencil skirt, sheer black pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 야근 뒤 옥상. 리아가 따지 않은 캔커피를 쥔 채, 억지로 웃으며 '만약에' 질문을 던진다. 웃음이 한 박자 늦다.
PLACE/TIME: 목요일 밤 · 회사 옥상

#10  ria_r02_scene_v001.png
OUTFIT: white button-up shirt with rolled sleeves, black pencil skirt, sheer black pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 리아가 내민 손을 잡고 걸음을 맞췄다. 정면을 보다가 옆을 보고, 다시 앞을 봤다.
PLACE/TIME: 다음 만남 · 아직 밝은 퇴근길

#11  ria_r08_scene_v001.png
OUTFIT: oversized white hoodie, gray dolphin shorts with white trim, bare legs, gray slippers
SLEEVE: plain gray knit sleeve
SCENE: 아침에 식탁을 정리하던 리아가 빵 두 조각을 접시에 놓았다.
PLACE/TIME: 일요일 아침 · 리아의 집

#12  ria_r10_scene_v001.png
OUTFIT: oversized white hoodie, gray dolphin shorts with white trim, bare legs, gray slippers
SLEEVE: plain gray knit sleeve
SCENE: 리아가 동네 지도를 펼치자 접힌 모서리가 자꾸 들렸다. 주인공이 노트로 한쪽을 누르고, 리아는 컵을 올리려다 둘의 팔이 겹친 걸 보고 멈췄다.
PLACE/TIME: 그 주 토요일 오후 · 리아의 집

#13  ria_r15_scene_v001.png
OUTFIT: cream cable-knit sweater, blue denim mini skirt, brown pantyhose, white sneakers
SLEEVE: plain gray knit sleeve
SCENE: 지도에서 골랐던 작은 공원에 갔다. 주인공은 긴 의자의 빈자리와 길게 드리운 빛을 찍고, 리아 옆에 앉아 짧은 글을 적었다.
PLACE/TIME: 그 주 일요일 오후 · 동네 산책길

#14  ria_e01_scene_v001.png
OUTFIT: oversized white hoodie, gray dolphin shorts with white trim, bare legs, gray slippers
SLEEVE: plain gray knit sleeve
SCENE: 주인공이 한 부를 리아 쪽으로 밀었다. 리아는 바로 펼치지 않고 표지를 손바닥으로 한 번 쓸어 봤다.
PLACE/TIME: 약 반년 뒤, 초여름의 휴일 · 리아의 집
````

## 5. 백지현 장면 CG — 14장

````text
ART STYLE (keep identical in every image of this conversation):
Polished commercial Korean/Japanese anime visual-novel illustration. Clean thin uniform dark-brown lineart, no sketchy or painterly lines. Soft cel shading with one shadow tone and small crisp highlights. Large glossy anime eyes with gradient irises and bright catchlights. Warm, slightly pastel palette, light from the upper left. Mature, attractive adult women in their late 20s to early 30s with realistic adult proportions. Do NOT use semi-realism, 3D, photo textures, painterly brushwork, heavy glow or chibi proportions.

CHARACTER: Baek Jihyun — very long wavy crimson-red hair with side-swept bangs, red-brown eyes, cool composed face, team-leader presence

RULES FOR THIS CONVERSATION
- Make exactly ONE image per reply, in the numbered order below. Start with #1 now.
- Under each image write only its file name.
- When I say "다음", make the next number. "다시" = redo the same number. Any other short note = fix that and redo.
- Every image: visual novel event CG, 16:9 landscape 1920x1080, full illustration WITH a detailed background.
- Keep the heroine's face, hair color, eye color and the given outfit exactly the same in every image.
- The male lead is the camera (first-person view). Never draw his face or full body. Only his hands or forearm may appear when the action needs it (sleeve given per item).
- Adults only. Natural hands with five fingers. No text, no logos, no watermark, no speech bubbles.
- Scene descriptions are in Korean; follow them literally.

LIST

#1  jihyun_r04_scene_v001.png
OUTFIT: charcoal-black tailored blazer, burgundy shirt, black belt, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 지현은 바로 대답하려다 물컵에서 손을 뗐다. 이번에는 주인공을 보며 천천히 말했다.
PLACE/TIME: 금요일 저녁 일곱 시 · 약속한 카페

#2  jihyun_r10_scene_v001.png
OUTFIT: hair in a loose half-up bun, soft taupe-gray long cardigan over a cream top, matching wide lounge pants, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 주인공이 핀셋으로 집은 부품이 두 번 미끄러졌다. 세 번째에 지현이 손바닥을 아래에 받쳤다.
PLACE/TIME: 토요일 오후 · 지현의 집

#3  jihyun_r11_scene_v001.png
OUTFIT: hair in a loose half-up bun, soft taupe-gray long cardigan over a cream top, matching wide lounge pants, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 저녁을 먹고 지현이 작은 카드 상자를 꺼냈다. 빵과 차 그림을 모으는 가벼운 게임이었다.
PLACE/TIME: 일요일 저녁 · 지현의 집

#4  jihyun_r16_scene_v001.png
OUTFIT: charcoal-black tailored blazer, burgundy shirt, black belt, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 피칭 직후 비상계단. 지현이 한 칸 내려와 눈높이를 맞추고, 눈을 감고 다가온다. 초록 비상구 표시등. 입술이 닿기 직전 구도.
PLACE/TIME: 피칭 당일 저녁 · 회사 비상계단

#5  jihyun_x01_scene_v001.png
OUTFIT: hair in a loose half-up bun, soft taupe-gray long cardigan over a cream top, matching wide lounge pants, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 현관에서 회색 카디건 차림의 지현이 30분 단위로 칸을 나눈 일정표 한 장을 내민다. 21:00 칸만 비어 있다. 침착한 척하지만 귀가 빨갛다.
PLACE/TIME: 12월 24일 오후 · 지현의 집

#6  jihyun_x02_scene_v001.png
OUTFIT: long black wool coat worn open over her office outfit (burgundy shirt, gray pencil skirt), long gray scarf hanging loose
SLEEVE: plain gray knit sleeve
SCENE: 버스 정류장 의자에 나란히 앉아, 지현이 장갑 낀 손으로 주인공의 손등을 한 번 누른다. 정류장 불빛, 다가오는 버스.
PLACE/TIME: 1월 평일 저녁 · 회사 앞 버스 정류장

#7  jihyun_x01b_scene_v001.png
OUTFIT: hair in a loose half-up bun, soft taupe-gray long cardigan over a cream top, matching wide lounge pants, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 크리스마스 다음 날 아침. 꺼진 휴대폰을 옆에 둔 채 지현이 머그를 들고 주인공 쪽으로 몸을 돌린다. 편안한 얼굴.
PLACE/TIME: 12월 25일 아침 · 지현의 집

#8  jihyun_sp1_scene_v001.png
OUTFIT: hair in a loose half-up bun, soft taupe-gray long cardigan over a cream top, matching wide lounge pants, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 조립 중인 작은 집의 계단 난간. 본드가 조금 번진 자리로 지현이 손을 뻗었다가 멈추고, 부드럽게 웃는다. 주인공의 손에 핀셋.
PLACE/TIME: 토요일 오후 · 지현의 집

#9  jihyun_sp2_scene_v001.png
OUTFIT: hair in a loose half-up bun, soft taupe-gray long cardigan over a cream top, matching wide lounge pants, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 소파에 기대 잠든 지현. 평온한 얼굴. 주인공의 손에 지현의 휴대폰(알람 화면). 스탠드 불빛.
PLACE/TIME: 화요일 저녁 · 지현의 집

#10  jihyun_r05_scene_v001.png
OUTFIT: beige belted trench coat over a burgundy cable-knit turtleneck, long dark plum A-line skirt, brown ankle boots
SLEEVE: plain gray knit sleeve
SCENE: 음료 옆에 놓인 종이 냅킨을 지현이 두 번 접었다. 주인공은 그 위에 빈 설탕 봉지를 세웠다.
PLACE/TIME: 고백 다음 날 토요일 오후 · 강변 카페

#11  jihyun_r08_scene_v001.png
OUTFIT: hair in a loose half-up bun, soft taupe-gray long cardigan over a cream top, matching wide lounge pants, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 각자 빵에 잼을 발랐다. 주인공의 빵을 보던 지현이 자기 것에도 잼을 더 얹었다.
PLACE/TIME: 일요일 아침 · 지현의 집

#12  jihyun_r14_scene_v001.png
OUTFIT: charcoal-black tailored blazer, burgundy shirt, black belt, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 지현이 펜을 들었다가 내려놓았다. 주인공이 질문에 끝까지 답한 뒤에야 자기 자료를 펼쳤다.
PLACE/TIME: 수요일 오전 · 비교 검토 직전

#13  jihyun_r16b_scene_v001.png
OUTFIT: charcoal-black tailored blazer, burgundy shirt, black belt, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 엘리베이터를 기다리는 동안 지현이 먼저 주인공의 손을 잡았다. 사무실 복도에서는 처음이었다.
PLACE/TIME: 피칭 전날 밤 · 사무실

#14  jihyun_e01_scene_v001.png
OUTFIT: hair in a loose half-up bun, soft taupe-gray long cardigan over a cream top, matching wide lounge pants, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 지현이 게임 카드를 펼치려다 조립집을 옮겼다. 둘이 나란히 앉을 자리를 만들고도 손을 떼지 못했다.
PLACE/TIME: 약 반년 뒤, 쉬는 날 오후 · 지현의 집
````

## 6. 차유진 장면 CG — 14장

````text
ART STYLE (keep identical in every image of this conversation):
Polished commercial Korean/Japanese anime visual-novel illustration. Clean thin uniform dark-brown lineart, no sketchy or painterly lines. Soft cel shading with one shadow tone and small crisp highlights. Large glossy anime eyes with gradient irises and bright catchlights. Warm, slightly pastel palette, light from the upper left. Mature, attractive adult women in their late 20s to early 30s with realistic adult proportions. Do NOT use semi-realism, 3D, photo textures, painterly brushwork, heavy glow or chibi proportions.

CHARACTER: Cha Yujin — light silver-gray bob with a small gold hairpin, thin round metal glasses, warm amber eyes, shy gentle face

RULES FOR THIS CONVERSATION
- Make exactly ONE image per reply, in the numbered order below. Start with #1 now.
- Under each image write only its file name.
- When I say "다음", make the next number. "다시" = redo the same number. Any other short note = fix that and redo.
- Every image: visual novel event CG, 16:9 landscape 1920x1080, full illustration WITH a detailed background.
- Keep the heroine's face, hair color, eye color and the given outfit exactly the same in every image.
- The male lead is the camera (first-person view). Never draw his face or full body. Only his hands or forearm may appear when the action needs it (sleeve given per item).
- Adults only. Natural hands with five fingers. No text, no logos, no watermark, no speech bubbles.
- Scene descriptions are in Korean; follow them literally.

LIST

#1  yujin_r04_scene_v001.png
OUTFIT: peach-cream cable-knit cardigan over a white blouse, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 유진은 앞에 둔 메뉴판을 덮었다. 주인공이 앉자 인사보다 먼저 한 번 숨을 골랐다.
PLACE/TIME: 금요일 저녁 일곱 시 · 약속한 카페

#2  yujin_r02_scene_v001.png
OUTFIT: peach-cream cable-knit cardigan over a cream collared blouse, brown pleated mini skirt, small beige crossbody bag, brown pantyhose, black pumps
SLEEVE: plain gray knit sleeve
SCENE: 작은 전시실 안으로 들어갔다. 유진은 벽을 따라 걷다가 한 그림에서 멈췄다.
PLACE/TIME: 토요일 오후 두 시 · 작은 전시 공간

#3  yujin_o02_scene_v001.png
OUTFIT: peach-cream cable-knit cardigan over a cream collared blouse, brown pleated mini skirt, small beige crossbody bag, brown pantyhose, black pumps
SLEEVE: plain gray knit sleeve
SCENE: 손을 옮기자 컵 안에 밝은 선이 다시 생겼다. 유진이 종이 위에 주인공의 손 그림자 끝을 짧게 그렸다.
PLACE/TIME: 기록집을 함께 본 토요일 오후 · 같은 카페

#4  yujin_r16_scene_v001.png
OUTFIT: peach-cream cable-knit cardigan over a white blouse, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 클라이언트 앞 발표 화면 옆에 리모컨을 쥐고 선 유진. "비슷한 게 아니라, 제가 그렸어요." 떨리지만 고개를 든 얼굴. 주인공은 맨 앞줄 시점.
PLACE/TIME: 피칭 당일 · 클라이언트사 대회의실

#5  yujin_x01_scene_v001.png
OUTFIT: oversized white button-up shirt worn as loungewear, black leggings, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 창가 책상. 유진이 스케치북을 뒤집어 내민다. 처음으로 정면에서 그린 주인공의 얼굴, 오른쪽 아래에 '차유진' 서명. 낮은 겨울 해가 옆얼굴에 걸린다.
PLACE/TIME: 12월 24일 오후 늦게 · 유진의 집

#6  yujin_x02_scene_v001.png
OUTFIT: peach-cream cable-knit cardigan over a white blouse, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 3층 복도 끝 창틀에 스케치북을 올려 보여 주는 유진. 회의실 책상 아래 겹쳐진 두 손 그림, 연필 제목 '석 달 뒤에도'. 짧은 겨울 노을.
PLACE/TIME: 1월 평일 저녁 · 회사 3층 복도 끝 창문

#7  yujin_x01b_scene_v001.png
OUTFIT: oversized white button-up shirt worn as loungewear, black leggings, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 크리스마스 다음 날 아침. 유진이 '이 방은 아침 빛이 제일 예쁘다'던 창가에 머그를 들고 앉아 있다. 안경에 아침 햇살.
PLACE/TIME: 12월 25일 아침 · 유진의 집

#8  yujin_sp1_scene_v001.png
OUTFIT: peach-cream cable-knit cardigan over a cream collared blouse, brown pleated mini skirt, small beige crossbody bag, brown pantyhose, black pumps
SLEEVE: plain gray knit sleeve
SCENE: 공원 벤치. 유진이 무릎 위 스케치북에 벤치 등받이에 놓인 주인공의 손을 그린다. 집중한 옆얼굴.
PLACE/TIME: 토요일 오후 · 공원 벤치

#9  yujin_sp2_scene_v001.png
OUTFIT: oversized white button-up shirt worn as loungewear, black leggings, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 유진이 노트북을 주인공 쪽으로 민다. 화면에 같은 남자의 뒷모습 그림 서른 장이 썸네일로. 긴장해서 소매를 쥔 손.
PLACE/TIME: 일요일 밤 · 유진의 집

#10  yujin_r07_scene_v001.png
OUTFIT: peach-cream cable-knit cardigan over a cream collared blouse, brown pleated mini skirt, small beige crossbody bag, brown pantyhose, black pumps
SLEEVE: plain gray knit sleeve
SCENE: 노트는 서점에서 넣고 나왔다. 저녁에는 같은 떡볶이를 순한 맛과 매운맛으로 따로 주문했다. 유진이 주인공 앞에 물잔을 밀자 주인공은 아직 첫입도 안 먹었다며 웃었다.
PLACE/TIME: 토요일 오후 세 시 · 동네 서점

#11  yujin_r08_scene_v001.png
OUTFIT: oversized white button-up shirt worn as loungewear, black leggings, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 유진이 커튼을 조금 열었다. 주인공도 일어나 반대쪽 커튼을 조금 걷었다. 어제 그림에서 봤던 그림자가 창가에 비쳤다.
PLACE/TIME: 다음 날 일요일 아침 · 유진의 집

#12  yujin_r10_scene_v001.png
OUTFIT: peach-cream cable-knit cardigan over a cream collared blouse, brown pleated mini skirt, small beige crossbody bag, brown pantyhose, black pumps
SLEEVE: plain gray knit sleeve
SCENE: 유진이 개인 노트를 펼쳤다. 안쪽 주머니에서 지난 전시 티켓이 나왔다.
PLACE/TIME: 같은 주 토요일 오후 · 동네 카페

#13  yujin_r11_scene_v001.png
OUTFIT: oversized white button-up shirt worn as loungewear, black leggings, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 유진이 작은 음악 기기 옆을 비우고 컵 두 개를 가져왔다. 주인공은 골라 온 곡 이름을 적었다.
PLACE/TIME: 다음 날 일요일 저녁 · 유진의 집

#14  yujin_e01_scene_v001.png
OUTFIT: oversized white button-up shirt worn as loungewear, black leggings, cream slippers
SLEEVE: plain gray knit sleeve
SCENE: 주인공도 직접 찍은 사진과 짧은 글을 모아 완성한 작은 기록집을 건넸다. 유진은 예전에 봤던 접지 초안 옆에 나란히 놓고 차이를 한눈에 봤다.
PLACE/TIME: 약 반년 뒤 초여름의 휴일 오후 · 유진의 집
````

## 7. 한서윤 장면 CG — 14장

````text
ART STYLE (keep identical in every image of this conversation):
Polished commercial Korean/Japanese anime visual-novel illustration. Clean thin uniform dark-brown lineart, no sketchy or painterly lines. Soft cel shading with one shadow tone and small crisp highlights. Large glossy anime eyes with gradient irises and bright catchlights. Warm, slightly pastel palette, light from the upper left. Mature, attractive adult women in their late 20s to early 30s with realistic adult proportions. Do NOT use semi-realism, 3D, photo textures, painterly brushwork, heavy glow or chibi proportions.

CHARACTER: Han Seoyun — very long wavy dark plum-black hair with a pink inner color streak, half-lidded blue-violet eyes, small mole under her left eye, teasing confident face

RULES FOR THIS CONVERSATION
- Make exactly ONE image per reply, in the numbered order below. Start with #1 now.
- Under each image write only its file name.
- When I say "다음", make the next number. "다시" = redo the same number. Any other short note = fix that and redo.
- Every image: visual novel event CG, 16:9 landscape 1920x1080, full illustration WITH a detailed background.
- Keep the heroine's face, hair color, eye color and the given outfit exactly the same in every image.
- The male lead is the camera (first-person view). Never draw his face or full body. Only his hands or forearm may appear when the action needs it (sleeve given per item).
- Adults only. Natural hands with five fingers. No text, no logos, no watermark, no speech bubbles.
- Scene descriptions are in Korean; follow them literally.

LIST

#1  seoyun_r04_scene_v001.png
OUTFIT: lavender shirt with rolled sleeves, black belt, navy mini pencil skirt, black lace-top thigh-high stockings, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 서윤은 컵을 내려놓고 주인공을 보았다. 웃으며 다음 화제로 넘기지 않았다.
PLACE/TIME: 금요일 저녁 일곱 시 · 약속한 북카페

#2  seoyun_r02_scene_v001.png
OUTFIT: gray ribbed knit midi dress with a scoop neckline and side slit, long beige open cardigan, bare legs, white sneakers
SLEEVE: plain gray knit sleeve
SCENE: 서윤이 좋아한다는 얇은 산문집 『느린 모퉁이』를 꺼냈다. 주인공은 표지만 보고 옆 선반의 엉뚱한 제목을 집었다.
PLACE/TIME: 토요일 오후 두 시 · 단골 서점과 북카페

#3  seoyun_r10_scene_v001.png
OUTFIT: gray ribbed knit midi dress with a scoop neckline and side slit, long beige open cardigan, bare legs, white sneakers
SLEEVE: plain gray knit sleeve
SCENE: 서로 한 조각씩 덜어 줬다. 주인공은 레몬을 먹고 물을 찾았고, 서윤은 초콜릿을 먹고 자기 접시를 다시 봤다.
PLACE/TIME: 토요일 오후 · 단골 북카페

#4  seoyun_r13_scene_v001.png
OUTFIT: lavender shirt with rolled sleeves, black belt, navy mini pencil skirt, black lace-top thigh-high stockings, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 서윤이 수첩을 접었다. 탁자 위에는 컵 두 개만 남았다.
PLACE/TIME: 약속한 월요일 저녁 일곱 시 · 카페

#5  seoyun_r16_scene_v001.png
OUTFIT: lavender shirt with rolled sleeves, black belt, navy mini pencil skirt, black lace-top thigh-high stockings, black pumps, company ID badge on a lanyard
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 엘리베이터 앞. 서윤이 뒤에 선 남자(전남편, 흐릿한 뒷모습)를 등지고 돌아와 주인공의 팔짱을 낀다. "가자, 주인공아." 담담하고 홀가분한 얼굴.
PLACE/TIME: 피칭 당일 저녁 · 클라이언트사 엘리베이터 앞

#6  seoyun_x01_scene_v001.png
OUTFIT: gray ribbed knit midi dress with a scoop neckline and side slit, long beige open cardigan, bare legs, white sneakers
SLEEVE: plain gray knit sleeve
SCENE: 난로가 켜진 작업실. 서윤이 작업대에 와인 잔 두 개를 나란히 놓고 천천히 닦는다. 의자에 걸린 주인공의 코트 위에 서윤의 가디건이 겹쳐 걸려 있다.
PLACE/TIME: 12월 24일 저녁 · 서윤의 작업실

#7  seoyun_x02_scene_v001.png
OUTFIT: long navy wool coat worn open over her office outfit, lavender scarf
SLEEVE: plain gray knit sleeve
SCENE: 창가 자리, 라테 두 잔 너머로 서윤이 농담 없이 주인공을 똑바로 본다. 창밖에 클라이언트사 건물.
PLACE/TIME: 1월 평일 저녁 · 회사 앞 카페

#8  seoyun_x01b_scene_v001.png
OUTFIT: pale pink satin pajama shirt and shorts, satin slippers
SLEEVE: plain gray knit sleeve
SCENE: 크리스마스 다음 날 아침. 작업실 창가에서 서윤이 머그를 들고 졸린 눈으로 웃는다. 작업대 위에 빈 와인 잔 두 개.
PLACE/TIME: 12월 25일 아침 · 서윤의 작업실

#9  seoyun_sp1_scene_v001.png
OUTFIT: pale pink satin pajama shirt and shorts, satin slippers
SLEEVE: plain gray knit sleeve
SCENE: 자정. 침대 옆 스탠드 아래 서윤이 얇은 책 『느린 모퉁이』를 펼치고 휴대폰에 대고 낮게 읽는다. 처음 보는 차분한 얼굴. (주인공 없음, 전화 너머)
PLACE/TIME: 평일 밤 · 서윤의 작업실, 전화

#10  seoyun_sp2_scene_v001.png
OUTFIT: gray ribbed knit midi dress with a scoop neckline and side slit, long beige open cardigan, bare legs, white sneakers
SLEEVE: plain gray knit sleeve
SCENE: 밤 열한 시 작업실. 작은 캐리어에 셔츠를 개어 넣으며 서윤이 자기 농담에 웃는다. 주인공의 손이 셔츠 하나를 건넨다.
PLACE/TIME: 일요일 밤 · 서윤의 작업실

#11  seoyun_r05_scene_v001.png
OUTFIT: gray ribbed knit midi dress with a scoop neckline and side slit, long beige open cardigan, bare legs, white sneakers
SLEEVE: plain gray knit sleeve
SCENE: 반으로 가르자 한쪽이 훨씬 커졌다. 서윤이 큰 쪽을 집으려다 멈췄다.
PLACE/TIME: 고백 다음 날 토요일 오후 두 시 · 약속한 장소

#12  seoyun_r08_scene_v001.png
OUTFIT: pale pink satin pajama shirt and shorts, satin slippers
SLEEVE: plain gray knit sleeve
SCENE: 작업실의 작은 주방에서 아침을 준비했다. 서윤이 주인공의 접시로 잘 구워진 빵을 밀어 주자, 주인공은 자기 것을 반으로 갈라 다시 건넸다.
PLACE/TIME: 다음 날 일요일 아침 · 서윤의 작업실

#13  seoyun_r11_scene_v001.png
OUTFIT: gray ribbed knit midi dress with a scoop neckline and side slit, long beige open cardigan, bare legs, white sneakers
SLEEVE: plain gray knit sleeve
SCENE: 주인공이 고른 다리 아래로 걸었다. 난간 사이로 바람이 들어와 둘은 잠깐 멈췄다.
PLACE/TIME: 일요일 저녁 여섯 시 반 · 서점 앞

#14  seoyun_e01_scene_v001.png
OUTFIT: gray ribbed knit midi dress with a scoop neckline and side slit, long beige open cardigan, bare legs, white sneakers
SLEEVE: plain gray knit sleeve
SCENE: 서윤이 표지를 손바닥으로 쓸었다. 첫 장을 읽고 나서는 자기 컵보다 책을 먼저 주인공 쪽으로 밀었다.
PLACE/TIME: 약 반년 뒤, 쉬는 날 오후 · 단골 북카페
````

## 8. 공통 CG·타이틀 — 6장

````text
ART STYLE (keep identical in every image of this conversation):
Polished commercial Korean/Japanese anime visual-novel illustration. Clean thin uniform dark-brown lineart, no sketchy or painterly lines. Soft cel shading with one shadow tone and small crisp highlights. Large glossy anime eyes with gradient irises and bright catchlights. Warm, slightly pastel palette, light from the upper left. Mature, attractive adult women in their late 20s to early 30s with realistic adult proportions. Do NOT use semi-realism, 3D, photo textures, painterly brushwork, heavy glow or chibi proportions.

CHARACTERS:
- Kang Ria — honey-blonde very long wavy hair in a high ponytail tied with a blue scrunchie, straight blunt bangs, bright blue eyes, cheerful energetic face; office outfit: white button-up shirt with rolled sleeves, black pencil skirt, sheer black pantyhose, black pumps, company ID badge on a lanyard
- Baek Jihyun — very long wavy crimson-red hair with side-swept bangs, red-brown eyes, cool composed face, team-leader presence; office outfit: charcoal-black tailored blazer, burgundy shirt, black belt, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
- Cha Yujin — light silver-gray bob with a small gold hairpin, thin round metal glasses, warm amber eyes, shy gentle face; office outfit: peach-cream cable-knit cardigan over a white blouse, dark gray pencil skirt, brown pantyhose, black pumps, company ID badge on a lanyard
- Han Seoyun — very long wavy dark plum-black hair with a pink inner color streak, half-lidded blue-violet eyes, small mole under her left eye, teasing confident face; office outfit: lavender shirt with rolled sleeves, black belt, navy mini pencil skirt, black lace-top thigh-high stockings, black pumps, company ID badge on a lanyard

RULES FOR THIS CONVERSATION
- Make exactly ONE image per reply, in the numbered order below. Start with #1 now.
- Under each image write only its file name.
- When I say "다음", make the next number. "다시" = redo the same number. Any other short note = fix that and redo.
- Every image: visual novel event CG, 16:9 landscape 1920x1080, full illustration WITH a detailed background.
- Keep the heroine's face, hair color, eye color and the given outfit exactly the same in every image.
- The male lead is the camera (first-person view). Never draw his face or full body. Only his hands or forearm may appear when the action needs it (sleeve given per item).
- Adults only. Natural hands with five fingers. No text, no logos, no watermark, no speech bubbles.
- Scene descriptions are in Korean; follow them literally.

LIST

#1  prologue_hands_v001.png
(No heroine face in this one.)
Scene: under a long presentation table in a corporate meeting hall during a tense pitch. Close-up of two hands under the table: a woman's hand gently pressing once on the back of a man's hand that rests on his knee (dark navy suit sleeve). Above the table edge, blurred papers and a presentation screen.
Mood: tense silence, but the touch says "it's okay". Cool blue projector light from above, warm light on the hands.
No faces. No text, no watermark.

#2  spring_rooftop_scene_v001.png
CHARACTERS: all four heroines in their office outfits.
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 리허설 뒤 옥상. 네 히로인과 신입(짧은 머리 20대 남자, 정장, 뒷모습 위주)이 웃음을 터뜨리며 옆 사람 어깨를 툭 친다. 주인공 시점.
PLACE/TIME: 3월 피칭 전날 저녁 · 회사 옥상

#3  spring_pitch_scene_v001.png
CHARACTERS: all four heroines in their office outfits.
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 발표 화면에 여섯 이름이 같은 크기로 떠 있고, 그 앞에 네 히로인이 나란히 선다.
PLACE/TIME: 3월 피칭 당일 · 클라이언트사 대회의실

#4  common_c05_scene_v001.png
CHARACTERS: all four heroines in their office outfits.
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 카페 테이블에 네 히로인이 모여 식사한다. 유진이 짧게 웃으며 메뉴 한 줄을 가리키고, 지현은 컵 사이 물병으로 물을 나눈다. 리아는 웃으며 수저를 돌리고, 서윤은 턱을 괴고 본다.
PLACE/TIME: 회사 근처 카페 · 점심

#5  common_colleague_ending_scene_v001.png
CHARACTERS: all four heroines in their office outfits.
SLEEVE: dark navy suit sleeve with a white shirt cuff
SCENE: 협업 회의가 끝난 회의실. 네 명이 각자 자리를 정리한다. 누군가는 노트북을 덮고, 누군가는 먼저 손을 흔들며 나간다.
PLACE/TIME: GY브랜딩 회의실 · 퇴근 무렵

#6  title_keyvisual_v001.png
The four heroines stand together on an office building rooftop just after work, at blue hour: city lights turning on, a few office windows still lit behind them.
Composition: Kang Ria front-center leaning forward with a bright wave; Baek Jihyun to the left with arms loosely crossed, a small smile; Cha Yujin to the right holding a sketchbook to her chest, glasses catching the light; Han Seoyun slightly behind, hair moving in the wind, teasing half-smile.
Leave the upper-left third calm (sky) for the game logo. Do NOT draw any text or logo.
Warm sunset rim light on the characters, cool blue sky. Adults only. No watermark.
````
