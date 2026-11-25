# Grok Imagine 에이전트 · 장난스러운 전체 CG v001

참고 그림처럼 깜짝 놀라거나 들켜서 당황하는 순간을 보여 주는 전체 CG입니다.
전체 대사에서 실제로 그런 순간이 쓰여 있는 장면만 골랐어요. 새 장면은 만들지 않았어요.

- 노출 수위: 옷을 다 입은 상태. 거품이나 수건으로 맨몸을 가리는 구도는 넣지 않아요.
- 그림체: 마스터 그림체를 그대로 따르고, 땀방울·홍조 선·놀람 선 같은 만화 효과만 더해요. SD나 치비 체형은 쓰지 않아요.
- 시점: 주인공 얼굴은 나오지 않아요. 손, 소매, 무릎만 화면 가장자리에 나와요.
- 비율: 16:9 가로.

## 사용법
1. 히로인별로 블록이 하나씩 있어요. 에이전트 창에 그 히로인의 마스터 입상 한 장만 올리고 블록을 통째로 붙여 넣으세요.
2. 리아 블록의 TASK 2(고깃집)는 네 명이 다 나와요. 리아 마스터만 올려도 되고, 다른 세 명은 글로 적은 외모를 따라 그려요. 다른 사람 얼굴이 어긋나면 그 히로인 마스터를 올리고 그 번호만 다시 시키세요.
3. 표정이 약하게 나오면 이렇게 보내세요: `Redo TASK n with a bigger comic reaction: wide eyes, sweat drops, blush lines, motion lines, same art style.`
4. 입상처럼 나오면 이렇게 보내세요: `Redo TASK n as a full scene CG, not a sprite.`

## 장면 목록

| # | 파일 이름 | 장면 | 대사 속 순간 |
|---|---|---|---|
| R1 | comic_ria_r06_taxi.webp | 리아 R06 · 카페 밖 골목 (입맞춤 선택지) | 입 맞추려는 순간 택시가 상향등을 켜서 둘이 화들짝 떨어짐 |
| R2 | comic_ria_r09_bbq.webp | 리아 R09 · 고깃집 회식 | 서윤이 "너희 둘 뭐 있어?" 하고 캐묻고, 리아는 "고기 탄다!" 하며 집게를 듦. 테이블 아래에서는 리아 발이 도현 발목에 붙어 있음 |
| J1 | comic_jihyun_r06_shop.webp | 지현 R06 · 단골 부품 가게 | 주인이 "처음 데려오신 분"이라며 서비스 봉투를 건네서 지현 귀가 빨개짐 |
| J2 | comic_jihyun_r12_elevator.webp | 지현 R12 · 출장 숙소 복도 | 캔커피를 건네던 손끝이 겹친 순간 엘리베이터가 '띵' 열려서 둘이 동시에 물러남 |
| Y1 | comic_yujin_r05_bell.webp | 유진 R05 · 데이트 (키스 선택지) | 다가오던 유진이 자전거 벨 소리에 화들짝 물러남 |
| Y2 | comic_yujin_r07_fan.webp | 유진 R07 · 유진의 집 | 도현이 '창가' 그림을 휴대폰 배경으로 해 뒀다고 하자 유진이 얼굴을 가림 |
| S1 | comic_seoyun_c04_caught.webp | 공통 C04 · 첫날 사무실 | "첫날에 그걸 들켰네." 컵을 들고 일어나다 고개만 돌려 웃음 |
| S2 | comic_seoyun_r09_towel.webp | 서윤 R09 · 식당 창가 | "수건한테 자리 뺏긴 얘기였어?" 서윤이 웃음을 터뜨림. 말풍선 속에 수건 널린 창문 |

---

## 강리아 (리아 마스터 올리기)

```text
Generate 2 separate images, one per task, in order. Label each image with its task number and file name.

ANTI-COPY RULE: the attached master sprite is ONLY a reference for her face, hair and drawing style. Do not copy its pose, framing, plain background or outfit. Never output a standing sprite on an empty background. Every image is a NEW full-scene CG.

GLOBAL RULES:
- ART STYLE LOCK (absolute): exactly the master sprite's style — same line weight, flat cel shading with soft gradients, same coloring, eye shape and face proportions. Normal adult body proportions, NOT chibi, NOT super-deformed.
- COMIC MOOD: playful romantic-comedy event CG. Add manga reaction effects drawn in the same style: sweat drops, blush hatching on cheeks, small surprise lines and squiggles near the head, motion lines. Exaggerated but cute facial reactions.
- Kang Ria, adult woman (28): slim face, very long wavy blonde hair in a high ponytail with a blue scrunchie, straight blunt bangs, bright blue eyes, cheerful mouth, same body proportions. Fully clothed in everyday clothes.
- POV RULE: first-person view of the man with her. Never show his face, the back of his head or his back. Only his hand, forearm or shirt sleeve may appear at the frame edge.
- 16:9 WIDE HORIZONTAL LANDSCAPE (1920x1080). Korean visual-novel event CG. No text, no speech-bubble text, no watermark.

TASK 1 — comic_ria_r06_taxi
Evening, quiet back alley corner outside a small cafe, warm street lamps. Ria in a light knit top and a short jacket. She had just leaned in close for a kiss, but a taxi at the end of the alley has flashed its high beams: a harsh white glare floods the frame from the right. Ria has jumped half a step back, both hands up near her chest, eyes wide, cheeks bright red, mouth in a startled little "eek", sweat drop, surprise lines by her head. The viewer's hand is at the bottom edge, still half-raised toward her. Funny, sweet, caught-in-the-act mood.

TASK 2 — comic_ria_r09_bbq
Busy Korean barbecue restaurant at night, smoke above a round tabletop grill, side dishes, soju glasses. Camera from the viewer's seat across from Ria. Ria in a casual hoodie holds metal tongs up in the air mid-flip, big forced grin, eyes looking away, sweat drop, steam puffing off a slightly burnt piece of meat. Beside her, Han Seoyun (32, long wavy dark plum hair, half-lidded grey-blue lavender eyes, small beauty mark under her LEFT eye, cardigan) leans in toward Ria with a sly, suspicious smile, chin on her hand. At the side of the table Baek Jihyun (30, long straight crimson hair, sharp red-brown eyes, blazer) sips a drink with a deadpan look, and Cha Yujin (27, silver-white bob, gold hairpin, thin round glasses, amber eyes, cardigan) holds a lettuce wrap and glances between them nervously. Small comic inset panel in the lower right corner: under the table, Ria's white sneaker toe resting against the viewer's ankle. The inset has a thin white border, same art style. No text.
```

## 백지현 (지현 마스터 올리기)

```text
Generate 2 separate images, one per task, in order. Label each image with its task number and file name.

ANTI-COPY RULE: the attached master sprite is ONLY a reference for her face, hair and drawing style. Do not copy its pose, framing, plain background or outfit. Never output a standing sprite on an empty background. Every image is a NEW full-scene CG.

GLOBAL RULES:
- ART STYLE LOCK (absolute): exactly the master sprite's style — same line weight, flat cel shading with soft gradients, same coloring, eye shape and face proportions. Normal adult body proportions, NOT chibi, NOT super-deformed.
- COMIC MOOD: playful romantic-comedy event CG. Add manga reaction effects drawn in the same style: sweat drops, blush hatching on cheeks and ears, small surprise lines, motion lines. Exaggerated but cute reactions on a normally composed, serious woman.
- Baek Jihyun, adult woman (30): very long crimson hair falling straight down her shoulders and back, slight wave only at the ends, side-parted bangs, sharp red-brown eyes with clear eyeliner, NO beauty mark, same body proportions. Fully clothed.
- POV RULE: first-person view of the man with her. Never show his face, the back of his head or his back. Only his hand, forearm or shirt sleeve may appear at the frame edge.
- 16:9 WIDE HORIZONTAL LANDSCAPE (1920x1080). Korean visual-novel event CG. No text, no watermark.

TASK 1 — comic_jihyun_r06_shop
Small cozy hobby shop for miniature model parts in a narrow alley: wooden counter, glass display cases full of tiny chairs, window frames and furniture parts, warm light. Jihyun in her office blouse and dark slacks, a work bag on her shoulder. Behind the counter a friendly middle-aged shop owner (face simple, partly cropped at the frame edge) grins and holds out a small paper bag of free parts. Jihyun stands stiff, both hands awkwardly half-raised to refuse, face composed but ears and cheeks burning red, eyes darting sideways toward the viewer, sweat drop, little steam puff above her head. The viewer's hand at the bottom edge. Embarrassed-but-pleased comedy.

TASK 2 — comic_jihyun_r12_elevator
Late night hotel corridor during a business trip: patterned carpet, row of room doors, a drink vending machine glowing at the end, an elevator on the side. Jihyun in a loosened white blouse and slacks, holding a canned coffee. The elevator doors have just opened with a bright "ding" glow (draw a small bell-shaped flash, no letters). Jihyun has jumped a full step back from the viewer, back straight like a soldier, can held stiffly at her side, eyes wide and darting to the elevator, blush and sweat drops, surprise lines. The viewer's hand at the bottom edge still holds the other can, frozen mid-reach. A stranger hotel guest with a suitcase steps out of the elevator in the background, small and unaware. Funny tension.
```

## 차유진 (유진 마스터 올리기)

```text
Generate 2 separate images, one per task, in order. Label each image with its task number and file name.

ANTI-COPY RULE: the attached master sprite is ONLY a reference for her face, hair, glasses and drawing style. Do not copy its pose, framing, plain background or outfit. Never output a standing sprite on an empty background. Every image is a NEW full-scene CG.

GLOBAL RULES:
- ART STYLE LOCK (absolute): exactly the master sprite's style — same line weight, flat cel shading with soft gradients, same coloring, eye shape and face proportions. Normal adult body proportions, NOT chibi, NOT super-deformed.
- COMIC MOOD: playful romantic-comedy event CG. Add manga reaction effects drawn in the same style: sweat drops, blush hatching, small surprise lines and squiggles, motion lines. Shy, flustered, cute reactions.
- Cha Yujin, adult woman (27): slim adult face, silver-white bob (front slightly longer), side-swept bangs, a gold hairpin on one side, thin round metal-frame glasses, amber-brown eyes, mature curvy figure, same body proportions. Fully clothed.
- POV RULE: first-person view of the man with her. Never show his face, the back of his head or his back. Only his hand, forearm or shirt sleeve may appear at the frame edge.
- 16:9 WIDE HORIZONTAL LANDSCAPE (1920x1080). Korean visual-novel event CG. No text, no watermark.

TASK 1 — comic_yujin_r05_bell
Weekend afternoon on a tree-lined park path, soft sunlight. Yujin in a cream knit cardigan and long skirt, a folded empty snack bag peeking from her tote. She had been leaning in close with eyes half closed for a kiss, but a cyclist just whizzed past behind her: draw the bicycle as a blur with speed lines and a small ringing-bell burst (no letters). Yujin has sprung back, shoulders up to her ears, both hands clutching her tote strap, glasses slightly askew, eyes wide, face bright red, sweat drops, surprise squiggle above her head. The viewer's hand at the bottom edge, still reaching toward her. Sweet and funny.

TASK 2 — comic_yujin_r07_fan
Evening in Yujin's small apartment: white desk with a drawing tablet under a window with cream curtains and city lights, beige sofa, sketches pinned on the wall. Yujin sits on the sofa holding up a printed illustration of a sunlit window. The viewer's hand at the bottom edge holds out a smartphone whose lock screen shows the very same window illustration (no text on the screen). Yujin has just realized: she covers her whole face with both hands, ears bright red, glasses pushed up crookedly, a little steam puff rising from her head, small hearts and panic lines floating around. Overjoyed-embarrassed comedy.
```

## 한서윤 (서윤 마스터 올리기)

```text
Generate 2 separate images, one per task, in order. Label each image with its task number and file name.

ANTI-COPY RULE: the attached master sprite is ONLY a reference for her face, hair and drawing style. Do not copy its pose, framing, plain background or outfit. Never output a standing sprite on an empty background. Every image is a NEW full-scene CG.

GLOBAL RULES:
- ART STYLE LOCK (absolute): exactly the master sprite's style — same line weight, flat cel shading with soft gradients, same coloring, eye shape and face proportions. Normal adult body proportions, NOT chibi, NOT super-deformed.
- COMIC MOOD: playful romantic-comedy event CG. Seoyun is the teaser, so the comedy comes from her mischievous expressions. Manga effects drawn in the same style: sparkles, little laugh lines, sweat drop on the viewer's side, blush hatching.
- Han Seoyun, adult woman (32): slim oval face, long wavy dark plum / deep violet hair, half-lidded grey-blue lavender eyes, small beauty mark under her LEFT eye, same body proportions. Fully clothed.
- POV RULE: first-person view of the man with her. Never show his face, the back of his head or his back. Only his hand, forearm or shirt sleeve may appear at the frame edge.
- 16:9 WIDE HORIZONTAL LANDSCAPE (1920x1080). Korean visual-novel event CG. No text, no watermark.

TASK 1 — comic_seoyun_c04_caught
Late afternoon in a modern design-agency office, desks with monitors, a big window with golden light. Seoyun in a soft cardigan over a blouse, a mug in one hand, caught mid-motion as she stands up from the desk next to the viewer: her body already turned to leave, but she looks back over her shoulder with a sly half-lidded smile and one finger on her lips, a small sparkle near her eye, as if saying "you caught me". The viewer's hand at the bottom edge rests on a notebook, a sweat drop drawn beside it. Teasing, charming.

TASK 2 — comic_seoyun_r09_towel
Evening at a cozy restaurant window table, warm pendant lights, city street outside the glass, plates of pasta. Seoyun sits across from the viewer in an elegant knit dress, bursting into laughter: eyes squeezed into happy arcs, one hand covering her mouth, shoulders shaking, little laugh lines and sparkles around her. Above the table, a round comic thought bubble with a thin white border shows a small apartment window completely blocked by a hanging bath towel on a drying rack, drawn in the same style. The viewer's hand at the bottom edge scratches awkwardly near the table edge, sweat drop. No text anywhere.
```
