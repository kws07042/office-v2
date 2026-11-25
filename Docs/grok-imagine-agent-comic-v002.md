# Grok Imagine 에이전트 · 장난스러운 전체 CG 종합 v002 (마스터 4장 한 번에)

v001의 8장에 GPT가 제안한 6장을 대사에 맞게 고쳐 더했어요. 모두 14장이에요.

## GPT 제안을 대사와 맞춰 본 결과
| GPT 제안 | 실제 대사 | 반영 |
|---|---|---|
| 리아 · 첫 출근 물품 옮기다 당황 | C01에 물건 나르는 장면은 없어요. 리아가 화살표 표지를 옮기고, 둘이 동시에 같은 표지를 가리켜서 리아가 웃음을 터뜨려요 | 표지를 끌어안은 리아 + 동시에 가리키는 손가락 |
| 리아 R02 · 가게 휴무 멘붕 | 그대로 있어요 ('임시 휴무', "분명 어제는 열려 있었는데...!") | 그대로 |
| 지현 R10 · 조립품이 무너짐 | 무너지지는 않아요. 도현이 핀셋으로 집은 부품이 두 번 미끄러지고, 지현이 손바닥으로 받아요. 도현은 두 손을 들어요 | 무너짐 → 손바닥 받기 + 항복 |
| 유진 R02 · 작품 엉뚱한 해석 | 도현이 "의자가 비뚤어져서 누가 돌아올 것 같다"고 해요. 엉뚱하다기보다 다른 해석이에요. 유진은 제목을 손으로 가리고 "힌트 없이요~"라고 해요 | 제목 가리기 + 의자 해석에 놀람 |
| 서윤 R02 · 놀리다 역으로 당함 | 있어요. 단, "궁금해서 묻는 거라고 못 박는다" 선택지에서만 나와요 ("나 좋아하는 거 얼굴에 다 나왔지", 책 뒤에 숨을까 망설임) | 그대로 |
| 4명 · 퇴근 모임 실언 | C05 점심에서 도현이 기록집 제목을 '퇴근도 기획 중'이라고 하자 네 명이 다르게 반응해요 (지현 "퇴근하고도 기획해야 해?", 유진 "아직 집에 못 갈 것 같아요", 서윤 "첫 독자 네 명을 야근시켰네~", 리아 "좀 웃겼는데~") | 네 반응을 그대로 그림으로 |

## 사용법
1. 그록 이매진 에이전트에 마스터 입상 4장을 **이 순서로** 올리세요: 1 리아 → 2 지현 → 3 유진 → 4 서윤.
2. 아래 블록 하나를 통째로 붙여 넣으세요.
3. 한 번에 다 안 나오면 `Continue from TASK n.`이라고 보내세요.
4. 다시 시킬 때 쓰는 말:
   - 얼굴이 다른 사람과 섞였을 때: `Redo TASK n. Use only IMAGE k for her face and hair.`
   - 반응이 약할 때: `Redo TASK n with a bigger comic reaction, same art style.`
   - 입상처럼 나왔을 때: `Redo TASK n as a full scene CG, not a sprite.`

## 장면 목록
| # | 누구 | 장면 | 순간 | 파일 이름 |
|---|---|---|---|---|
| 1 | 강리아 | 공통 C01 · 첫 출근 행사장 | 둘이 동시에 같은 표지를 가리키고 리아가 푸흡 웃음 | comic_c01_sign.webp |
| 2 | 강리아 | 리아 R02 · 문 닫힌 가게 앞 | 찜한 가게가 임시 휴무라 멘붕 | comic_ria_r02_closed.webp |
| 3 | 강리아 | 리아 R06 · 카페 밖 골목 (입맞춤 선택지) | 택시 상향등에 화들짝 | comic_ria_r06_taxi.webp |
| 4 | 강리아 | 리아 R09 · 고깃집 회식 | 서윤 추궁 + 고기 탄다! + 테이블 아래 발 | comic_ria_r09_bbq.webp |
| 5 | 백지현 | 지현 R06 · 부품 가게 | 서비스 봉투에 귀가 빨개짐 | comic_jihyun_r06_shop.webp |
| 6 | 백지현 | 지현 R10 · 지현의 집 조립 | 핀셋 부품이 두 번 미끄러져 지현 손바닥에 떨어짐, 도현 항복 | comic_jihyun_r10_tweezers.webp |
| 7 | 백지현 | 지현 R12 · 출장 숙소 복도 | 엘리베이터 띵에 차렷 | comic_jihyun_r12_elevator.webp |
| 8 | 차유진 | 유진 R02 · 전시 데이트 | 제목을 손으로 가리며 힌트 금지, 도현의 의자 해석에 놀람 | comic_yujin_r02_title.webp |
| 9 | 차유진 | 유진 R05 · 공원길 (키스 선택지) | 자전거 벨에 튕겨 나감 | comic_yujin_r05_bell.webp |
| 10 | 차유진 | 유진 R07 · 유진 집 | 폰 배경이 자기 그림이라 얼굴 가림 | comic_yujin_r07_fan.webp |
| 11 | 한서윤 | 공통 C04 · 첫날 사무실 | "첫날에 그걸 들켰네" | comic_seoyun_c04_caught.webp |
| 12 | 한서윤 | 서윤 R02 · 북카페 ("궁금해서 묻는 거라고 못 박는다" 선택지) | 놀리다 역으로 당해 책 뒤에 숨으려다 멈춤 | comic_seoyun_r02_reverse.webp |
| 13 | 한서윤 | 서윤 R09 · 식당 창가 | 수건 얘기에 웃음 터짐 | comic_seoyun_r09_towel.webp |
| 14 | 네 명 함께 | 공통 C05 · 회사 근처 카페 점심 | 기록집 제목 "퇴근도 기획 중"에 네 명이 각기 다른 반응 | comic_c05_title.webp |

노출은 없어요. 모두 옷을 다 입은 상태이고, 웃음은 표정과 상황으로만 만들어요.

```text
Generate 14 separate images, one per task, in order. Do not merge or skip tasks. Label each image with its task number and file name.

REFERENCE IMAGES (4 master sprites attached, in this order):
- IMAGE 1 = Kang Ria, adult woman (28): slim face, very long wavy blonde hair in a high ponytail with a blue scrunchie, straight blunt bangs, bright blue eyes, cheerful mouth.
- IMAGE 2 = Baek Jihyun, adult woman (30): very long crimson hair falling straight down her shoulders and back, slight wave only at the ends, side-parted bangs, sharp red-brown eyes with clear eyeliner, NO beauty mark.
- IMAGE 3 = Cha Yujin, adult woman (27): silver-white bob (front slightly longer), side-swept bangs, gold hairpin on one side, thin round metal-frame glasses, amber-brown eyes, mature curvy figure.
- IMAGE 4 = Han Seoyun, adult woman (32): slim oval face, long wavy dark plum / deep violet hair, half-lidded grey-blue lavender eyes, small beauty mark under her LEFT eye.
For each woman use ONLY her own reference image for face, hair and body proportions. Never mix their faces or hair colors.

ANTI-COPY RULE: the master sprites are ONLY references for face, hair and drawing style. Do not copy their poses, standing full-body framing, plain backgrounds or office outfits. Never output a standing sprite on an empty background. Never just change the clothes on a reference image. Every image is a NEW full-scene CG.

GLOBAL RULES (every task):
- ART STYLE LOCK (absolute, overrides everything): exactly the masters' art style — same clean line weight, flat cel shading with soft gradients, same coloring, skin tone, eye shape and face proportions. Normal adult body proportions, NOT chibi, NOT super-deformed.
- COMIC MOOD: playful romantic-comedy event CG. Add manga reaction effects drawn in the same style: sweat drops, blush hatching, small surprise lines and squiggles, motion lines, sparkles, steam puffs. Exaggerated but cute facial reactions.
- Everyone is fully clothed in everyday clothes. No nudity, no underwear showing.
- POV RULE: first-person view of the man with her. Never show his face, the back of his head, his shoulders or his back. Only his hand, forearm or shirt sleeve may appear at the frame edge.
- 16:9 WIDE HORIZONTAL LANDSCAPE (1920x1080). NOT vertical, NOT square. Korean visual-novel event CG. No text, no letters, no speech-bubble text, no watermark.

TASK 1 — comic_c01_sign
Morning at an outdoor pop-up event entrance before opening: a pastel pop-up booth, rope barriers, two queues of early visitors splitting in two directions, cardboard boxes of goods stacked by the booth. Ria (IMAGE 1) in a staff vest over a casual top, ponytail swinging, hugging a tall A-frame arrow sign she is in the middle of dragging. Ria and the viewer are pointing at the very same arrow sign at the exact same moment: her finger in the frame, the viewer's arm and finger entering from the bottom-left edge, both fingers aimed at the same sign. Ria bursts out laughing ("pfft" face: puffed cheeks, eyes squeezed, little laugh lines and sparkles), one hand nearly losing grip of the sign, a stack of boxes wobbling next to her with motion lines. First-day chaos, bright and funny.

TASK 2 — comic_ria_r02_closed
Early evening, still bright, a narrow street in front of a small cozy restaurant with the shutters half down and a paper notice taped on the glass door (blank paper, no readable text). Ria (IMAGE 1) in a cute going-out outfit (light cardigan, skirt) stands frozen in front of the door, holding her phone with a map pin on the screen in one hand, the other hand clutching her hair; her face is pure despair: white-ish blank eyes, open wailing mouth, a vertical gloom-lines effect above her head, a sweat drop, a tiny ghost-like sigh puff leaving her mouth. The viewer's hand at the bottom edge raised in a calming gesture, a small smile implied by a sparkle near the frame edge. Comedic "my plan just died" moment, but still cute.

TASK 3 — comic_ria_r06_taxi
Evening, quiet back alley corner outside a small cafe, warm street lamps. Ria in a light knit top and a short jacket. She had just leaned in close for a kiss, but a taxi at the end of the alley has flashed its high beams: a harsh white glare floods the frame from the right. Ria has jumped half a step back, both hands up near her chest, eyes wide, cheeks bright red, mouth in a startled little "eek", sweat drop, surprise lines by her head. The viewer's hand is at the bottom edge, still half-raised toward her. Funny, sweet, caught-in-the-act mood.

TASK 4 — comic_ria_r09_bbq
Busy Korean barbecue restaurant at night, smoke above a round tabletop grill, side dishes, soju glasses. Camera from the viewer's seat across from Ria. Ria in a casual hoodie holds metal tongs up in the air mid-flip, big forced grin, eyes looking away, sweat drop, steam puffing off a slightly burnt piece of meat. Beside her, Han Seoyun (32, long wavy dark plum hair, half-lidded grey-blue lavender eyes, small beauty mark under her LEFT eye, cardigan) leans in toward Ria with a sly, suspicious smile, chin on her hand. At the side of the table Baek Jihyun (30, long straight crimson hair, sharp red-brown eyes, blazer) sips a drink with a deadpan look, and Cha Yujin (27, silver-white bob, gold hairpin, thin round glasses, amber eyes, cardigan) holds a lettuce wrap and glances between them nervously. Small comic inset panel in the lower right corner: under the table, Ria's white sneaker toe resting against the viewer's ankle. The inset has a thin white border, same art style. No text.

TASK 5 — comic_jihyun_r06_shop
Small cozy hobby shop for miniature model parts in a narrow alley: wooden counter, glass display cases full of tiny chairs, window frames and furniture parts, warm light. Jihyun in her office blouse and dark slacks, a work bag on her shoulder. Behind the counter a friendly middle-aged shop owner (face simple, partly cropped at the frame edge) grins and holds out a small paper bag of free parts. Jihyun stands stiff, both hands awkwardly half-raised to refuse, face composed but ears and cheeks burning red, eyes darting sideways toward the viewer, sweat drop, little steam puff above her head. The viewer's hand at the bottom edge. Embarrassed-but-pleased comedy.

TASK 6 — comic_jihyun_r10_tweezers
Saturday afternoon in Jihyun's tidy apartment, a low wooden table covered with a cutting mat, a half-built miniature wooden house without its roof, tiny doorknobs and parts in a tray, glue, a cup of tea. Jihyun (IMAGE 2) in a soft house sweater, hair tied loosely, sits beside the viewer and has her palm held flat under the viewer's tweezers with a dry, unimpressed "I knew it" look (one eyebrow raised, half-lidded eyes), a tiny doorknob part landing in her palm with small motion lines and a "plink" sparkle. In the foreground the viewer's two hands are raised in surrender at the bottom edge, the tweezers dropped on the mat, a sweat drop beside them. Deadpan comedy, warm light.

TASK 7 — comic_jihyun_r12_elevator
Late night hotel corridor during a business trip: patterned carpet, row of room doors, a drink vending machine glowing at the end, an elevator on the side. Jihyun in a loosened white blouse and slacks, holding a canned coffee. The elevator doors have just opened with a bright "ding" glow (draw a small bell-shaped flash, no letters). Jihyun has jumped a full step back from the viewer, back straight like a soldier, can held stiffly at her side, eyes wide and darting to the elevator, blush and sweat drops, surprise lines. The viewer's hand at the bottom edge still holds the other can, frozen mid-reach. A stranger hotel guest with a suitcase steps out of the elevator in the background, small and unaware. Funny tension.

TASK 8 — comic_yujin_r02_title
Saturday afternoon in a small white-walled gallery with a few framed paintings; the main painting shows a warm-colored empty room with one slightly crooked chair. Yujin (IMAGE 3) in a cream knit and long skirt, tote bag on her shoulder, stands by the painting and stretches one hand out flat to cover the small title label under it, leaning in, with a playful "no spoilers!" face: one eye winking, tongue slightly out, a little sparkle. The viewer's hand enters from the bottom edge pointing at the crooked chair in the painting, while Yujin's eyes go wide behind her round glasses in surprise at his interpretation, a small "!" shaped flash (no letters) above her head. Playful, sweet.

TASK 9 — comic_yujin_r05_bell
Weekend afternoon on a tree-lined park path, soft sunlight. Yujin in a cream knit cardigan and long skirt, a folded empty snack bag peeking from her tote. She had been leaning in close with eyes half closed for a kiss, but a cyclist just whizzed past behind her: draw the bicycle as a blur with speed lines and a small ringing-bell burst (no letters). Yujin has sprung back, shoulders up to her ears, both hands clutching her tote strap, glasses slightly askew, eyes wide, face bright red, sweat drops, surprise squiggle above her head. The viewer's hand at the bottom edge, still reaching toward her. Sweet and funny.

TASK 10 — comic_yujin_r07_fan
Evening in Yujin's small apartment: white desk with a drawing tablet under a window with cream curtains and city lights, beige sofa, sketches pinned on the wall. Yujin sits on the sofa holding up a printed illustration of a sunlit window. The viewer's hand at the bottom edge holds out a smartphone whose lock screen shows the very same window illustration (no text on the screen). Yujin has just realized: she covers her whole face with both hands, ears bright red, glasses pushed up crookedly, a little steam puff rising from her head, small hearts and panic lines floating around. Overjoyed-embarrassed comedy.

TASK 11 — comic_seoyun_c04_caught
Late afternoon in a modern design-agency office, desks with monitors, a big window with golden light. Seoyun in a soft cardigan over a blouse, a mug in one hand, caught mid-motion as she stands up from the desk next to the viewer: her body already turned to leave, but she looks back over her shoulder with a sly half-lidded smile and one finger on her lips, a small sparkle near her eye, as if saying "you caught me". The viewer's hand at the bottom edge rests on a notebook, a sweat drop drawn beside it. Teasing, charming.

TASK 12 — comic_seoyun_r02_reverse
Saturday afternoon in a cozy bookstore cafe with tall wooden shelves and warm lamps. Seoyun (IMAGE 4) in an elegant knit and long skirt, sitting at a small table. Her usual teasing smile has collapsed: she is caught off guard, face fully red up to the ears, eyes wide and wobbling, mouth in a flustered wavy line, holding a thin hardcover book up halfway in front of her face as if about to hide behind it, then stopping. Steam puffs and blush hatching, a small sweat drop. The viewer's hand at the bottom edge rests calmly on the table next to his own book, a tiny sparkle of victory near it. "The teaser got teased back" comedy.

TASK 13 — comic_seoyun_r09_towel
Evening at a cozy restaurant window table, warm pendant lights, city street outside the glass, plates of pasta. Seoyun sits across from the viewer in an elegant knit dress, bursting into laughter: eyes squeezed into happy arcs, one hand covering her mouth, shoulders shaking, little laugh lines and sparkles around her. Above the table, a round comic thought bubble with a thin white border shows a small apartment window completely blocked by a hanging bath towel on a drying rack, drawn in the same style. The viewer's hand at the bottom edge scratches awkwardly near the table edge, sweat drop. No text anywhere.

TASK 14 — comic_c05_title
Lunch at a bright cafe near the office, a long table with four women and the viewer, plates, water glasses, a water bottle. Camera from the viewer's seat at the head of the table, his hand at the bottom edge holding up a small notebook he has just shown. The four women all react differently at once to his embarrassing project title, each with her own manga effect:
- Ria (IMAGE 1, blonde ponytail, blue scrunchie): bursting out laughing, hand slapping the table, tears at the corners of her eyes.
- Jihyun (IMAGE 2, long crimson hair, blazer): deadpan stare, water glass paused halfway, one eyebrow raised, a small dotted "..." trail (no letters).
- Yujin (IMAGE 3, silver bob, round glasses): leaning back looking exhausted and dizzy, swirly eyes, a tiny storm cloud over her head, as if she just got overtime.
- Seoyun (IMAGE 4, wavy plum hair, beauty mark under LEFT eye): chin on her hand, sly smile, one finger pointing at the viewer, sparkle.
A sweat drop on the viewer's side. Everyone fully clothed in office-casual clothes. Group comedy, warm daylight.
```
