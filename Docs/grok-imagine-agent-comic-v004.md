# Grok Imagine 에이전트 · 장난스러운 SD CG 종합 v004 (마스터 4장 한 번에)

v003에서 바뀐 점:
1. **히로인:** SD로 그리고, 머리끝부터 신발까지 전신이 다 나와요. 얼굴, 머리색, 눈, 머리 장식은 마스터 그대로예요.
2. **도현과 조연:** 몸은 안 나오고 SD 손과 소매만 나와요. 가게 주인, 투숙객, 자전거 탄 사람도 손만 나와요.
3. 13장 구성은 그대로예요.

## 사용법
1. 마스터 4장을 **리아 → 지현 → 유진 → 서윤** 순서로 올려요.
2. 아래 블록을 통째로 붙여 넣어요.
3. 중간에 멈추면 `Continue from TASK n.`이라고 보내요.
4. 다시 시킬 때 쓰는 말:
   - 전신이 다 안 나올 때: `Redo TASK n. Zoom out: her whole SD body from the top of her hair to her shoes inside the frame.`
   - SD가 아닐 때: `Redo TASK n. Draw her as SD chibi, 2.5 heads tall, same face and hair as IMAGE k.`
   - 도현이나 조연의 몸이 나왔을 때: `Redo TASK n. Show only his SD hand and sleeve at the frame edge, no body or face.`
   - 얼굴이 섞였을 때: `Redo TASK n. Use only IMAGE k for her face and hair.`

## 장면 목록
| # | 누구 | 장면 | 순간 | 파일 이름 |
|---|---|---|---|---|
| 1 | 강리아 | 공통 C01 · 첫 출근 행사장 | 둘이 동시에 같은 표지를 가리키고 리아가 푸흡 웃음 | comic_c01_sign.webp |
| 2 | 강리아 | 리아 R02 · 문 닫힌 가게 앞 | 찜한 가게가 임시 휴무라 멘붕 | comic_ria_r02_closed.webp |
| 3 | 강리아 | 리아 R06 · 카페 밖 골목 (입맞춤 선택지) | 택시 상향등에 화들짝 | comic_ria_r06_taxi.webp |
| 4 | 강리아 | 리아 R09 · 고깃집 회식 | 서윤 추궁 + 고기 탄다! + 테이블 아래 발 | comic_ria_r09_bbq.webp |
| 5 | 백지현 | 지현 R06 · 부품 가게 | 서비스 봉투에 귀가 빨개짐 | comic_jihyun_r06_shop.webp |
| 6 | 백지현 | 지현 R12 · 출장 숙소 복도 | 엘리베이터 띵에 차렷 | comic_jihyun_r12_elevator.webp |
| 7 | 차유진 | 유진 R02 · 전시 데이트 | 제목을 손으로 가리며 힌트 금지, 도현의 해석에 놀람 | comic_yujin_r02_title.webp |
| 8 | 차유진 | 유진 R05 · 공원길 (키스 선택지) | 자전거 벨에 튕겨 나감 | comic_yujin_r05_bell.webp |
| 9 | 차유진 | 유진 R07 · 유진 집 | 폰 배경이 자기 그림이라 얼굴 가림 | comic_yujin_r07_fan.webp |
| 10 | 한서윤 | 공통 C04 · 첫날 사무실 | "첫날에 그걸 들켰네" | comic_seoyun_c04_caught.webp |
| 11 | 한서윤 | 서윤 R02 · 북카페 ("궁금해서 묻는 거라고 못 박는다" 선택지) | 놀리다 역으로 당해 책 뒤에 숨으려다 멈춤 | comic_seoyun_r02_reverse.webp |
| 12 | 한서윤 | 서윤 R09 · 식당 창가 | 수건 얘기에 웃음 터짐 | comic_seoyun_r09_towel.webp |
| 13 | 네 명 함께 | 공통 C05 · 회사 근처 카페 점심 | 기록집 제목 '퇴근도 기획 중'에 네 명이 각기 다른 반응 | comic_c05_title.webp |

```text
Generate 13 separate images, one per task, in order. Do not merge or skip tasks. Label each image with its task number and file name.

REFERENCE IMAGES (4 master sprites attached, in this order):
- IMAGE 1 = Kang Ria: very long wavy blonde hair in a high ponytail with a blue scrunchie, straight blunt bangs, bright blue eyes, cheerful mouth.
- IMAGE 2 = Baek Jihyun: very long straight crimson hair down her back, slight wave at the ends, side-parted bangs, sharp red-brown eyes with eyeliner, NO beauty mark.
- IMAGE 3 = Cha Yujin: silver-white bob, side-swept bangs, gold hairpin on one side, thin round metal-frame glasses, amber-brown eyes.
- IMAGE 4 = Han Seoyun: long wavy dark plum / deep violet hair, half-lidded grey-blue lavender eyes, small beauty mark under her LEFT eye.
All four are adult women. For each woman use ONLY her own reference image for face, hair, eye color and hair ornaments. Never mix them.

SD STYLE RULE (every image):
- Every heroine is drawn as an SD / chibi version of her master: about 2.5 heads tall, big head, small rounded body, short limbs, big expressive eyes. Keep her exact hair style, hair color, eye color, eye shape, glasses, hair ornaments and beauty mark from her reference.
- Keep the masters' line quality and coloring (clean lines, soft cel shading, same palette), only the proportions change to SD.
- Backgrounds are detailed and in normal scale, like an SD event illustration in a Korean visual novel.

FULL BODY RULE (very important):
- Each SD heroine is shown FULL BODY: from the top of her hair (including ponytail, scrunchie, hairpin) down to her shoes, all inside the frame.
- Leave clear empty space above her head and below her feet. Never crop her head, hair or feet. Pull the camera back if needed.

HANDS-ONLY RULE (Dohyun and all side characters):
- Dohyun (the male lead) and every side character (shop owner, hotel guest, cyclist, etc.) NEVER appear with a body or face.
- Show only their SD hand and a bit of sleeve entering from the frame edge, drawn in the same SD style (small round hand).
- Dohyun's sleeve is always a white dress shirt sleeve rolled up once.

GLOBAL RULES:
- COMIC MOOD: playful romantic-comedy with manga effects drawn in the same style: sweat drops, blush hatching, surprise lines and squiggles, motion lines, sparkles, steam puffs.
- Everyone is fully clothed in everyday clothes. No nudity, no underwear showing.
- 16:9 WIDE HORIZONTAL LANDSCAPE (1920x1080). NOT vertical, NOT square. No text, no letters, no speech-bubble text, no watermark.
- Never output a plain standing sprite on an empty background; every image is a full scene.

TASK 1 — comic_c01_sign
Morning at an outdoor pop-up event entrance before opening: a pastel pop-up booth, rope barriers, cardboard boxes stacked by the booth, two lines of footprints/queue stanchions splitting in two directions. SD Ria (IMAGE 1, full body head to shoes) in a staff vest over a casual top and sneakers, ponytail swinging, hugs a tall A-frame arrow sign she was dragging. Dohyun's SD hand and sleeve enter from the bottom-left edge, pointing at the very same arrow sign at the exact same moment as Ria's finger. Ria bursts out laughing (puffed cheeks, eyes squeezed shut, laugh lines, sparkles), almost losing grip of the sign. A stack of boxes wobbles beside her with motion lines.

TASK 2 — comic_ria_r02_closed
Early evening, still bright, a narrow street in front of a small cozy restaurant with the shutters half down and a blank paper notice taped on the glass door (no readable text). SD Ria (IMAGE 1, full body) in a light cardigan and skirt stands frozen at the door, phone with a map pin in one hand, the other hand clutching her head; pure despair: blank white eyes, wailing open mouth, vertical gloom lines over her head, a tiny ghost-like sigh puff, sweat drop. Dohyun's SD hand enters from the bottom edge patting the air in a "it's okay" gesture, with a small sweat drop beside it.

TASK 3 — comic_ria_r06_taxi
Evening, quiet back alley corner outside a small cafe, warm street lamps. SD Ria (IMAGE 1, full body) in a light knit top, short jacket and skirt. She had just leaned in for a kiss, but a taxi at the end of the alley flashes its high beams: a harsh white glare floods in from the right. Ria has jumped back, little feet off the ground, both hands up near her chest, eyes wide, cheeks bright red, sweat drop, surprise lines. Dohyun's SD hand at the bottom edge is still half-raised toward her, frozen, with a sweat drop.

TASK 4 — comic_ria_r09_bbq
Busy Korean barbecue restaurant at night, smoke above a round tabletop grill, side dishes, soju glasses. Camera from Dohyun's seat across the table, slightly high and pulled back so all four SD women are fully visible. SD Ria (IMAGE 1) in a hoodie holds metal tongs up mid-flip, big forced grin, eyes looking away, sweat drop, steam off a burnt piece of meat. SD Seoyun (IMAGE 4, cardigan) leans toward Ria with a sly suspicious smile, chin on hand. SD Jihyun (IMAGE 2, blazer) sips a drink deadpan. SD Yujin (IMAGE 3, cardigan) holds a lettuce wrap, glancing nervously. Dohyun's SD hands at the bottom edge grip his chopsticks, trembling, sweat drops. Small comic inset in the lower-right corner (thin white border): under the table, SD Ria's white sneaker toe resting against Dohyun's ankle.

TASK 5 — comic_jihyun_r06_shop
Small cozy hobby shop for miniature model parts in a narrow alley: wooden counter, glass display cases full of tiny chairs and window frames, warm light. SD Jihyun (IMAGE 2, full body) in an office blouse and dark slacks, work bag on her shoulder, stands stiff with both hands half-raised to refuse; face composed but ears and cheeks burning red, eyes darting sideways, sweat drop, steam puff over her head. From behind the counter on the right, only the shop owner's SD hand and sleeve reach in, holding out a small paper bag of free parts. Dohyun's SD hand at the bottom-left edge, half-raised in surprise.

TASK 6 — comic_jihyun_r12_elevator
Late night hotel corridor during a business trip: patterned carpet, room doors, a glowing vending machine at the end, an elevator on the side. SD Jihyun (IMAGE 2, full body) in a loosened white blouse and slacks holds a canned coffee. The elevator doors have just opened with a bright bell-shaped flash (no letters); from the elevator only an unknown guest's SD hand pulling a suitcase handle is visible. Jihyun has jumped a full step away, standing at attention like a soldier, can held stiffly at her side, eyes wide toward the elevator, blush, sweat drops, surprise lines. Dohyun's SD hand at the bottom edge holds the other can, frozen mid-reach.

TASK 7 — comic_yujin_r02_title
Saturday afternoon in a small white-walled gallery; a framed painting shows a warm-colored empty room with one slightly crooked chair. SD Yujin (IMAGE 3, full body) in a cream knit and long skirt, tote bag, stretches one little hand flat over the title label under the painting with a playful "no spoilers!" wink. Dohyun's SD hand enters from the bottom edge pointing at the crooked chair, and Yujin's eyes go wide behind her round glasses at his interpretation, a "!"-shaped flash (no letters) above her head.

TASK 8 — comic_yujin_r05_bell
Weekend afternoon on a tree-lined park path, soft sunlight. SD Yujin (IMAGE 3, full body) in a cream knit cardigan and long skirt, tote bag. She had been leaning in with eyes closed for a kiss, but a bicycle just whizzed past behind her (show only the blurred bicycle wheel and the rider's SD hand ringing the bell, speed lines, a bell burst with no letters). Yujin has sprung back, shoulders to her ears, clutching her tote strap, glasses askew, eyes wide, face bright red, sweat drops. Dohyun's SD hand at the bottom edge is still reaching toward her.

TASK 9 — comic_yujin_r07_fan
Evening in Yujin's small apartment: white desk with a drawing tablet under a window with cream curtains and city lights, beige sofa, sketches pinned on the wall. SD Yujin (IMAGE 3, full body, sitting on the sofa, feet visible) has a printed sunlit-window illustration on her lap. Dohyun's SD hand at the bottom edge holds up a smartphone whose lock screen shows the same window illustration (no text). Yujin covers her whole face with both little hands, ears bright red, glasses pushed up crookedly, steam rising from her head, small hearts and panic lines floating around.

TASK 10 — comic_seoyun_c04_caught
Late afternoon in a modern design-agency office, desks with monitors, a big window with golden light. SD Seoyun (IMAGE 4, full body) in a soft cardigan, blouse and long skirt, mug in one hand, has turned to walk away but looks back over her shoulder with a sly half-lidded smile and one finger on her lips, sparkle near her eye. Dohyun's SD hand at the bottom edge rests on a notebook on the desk, a big sweat drop beside it.

TASK 11 — comic_seoyun_r02_reverse
Saturday afternoon in a cozy bookstore cafe with tall wooden shelves and warm lamps. SD Seoyun (IMAGE 4, full body, standing by a shelf) in an elegant knit and long skirt. Her teasing smile has collapsed: face red to the ears, wobbly wide eyes, flustered wavy mouth, holding a thin book halfway up as if to hide behind it, then stopping. Steam puffs, blush hatching, sweat drop. Dohyun's SD hand at the bottom edge calmly holds his own book, a tiny victory sparkle beside it.

TASK 12 — comic_seoyun_r09_towel
Evening at a cozy restaurant window table, warm pendant lights, city street outside, plates of pasta. SD Seoyun (IMAGE 4, full body visible on her chair, feet included) in an elegant knit dress bursts into laughter: eyes in happy arcs, hand over her mouth, shoulders shaking, laugh lines and sparkles. Dohyun's SD hand at the bottom edge scratches awkwardly near his fork, sweat drop. Above the table a round thought bubble (thin white border) shows a small apartment window completely blocked by a bath towel on a drying rack. No text.

TASK 13 — comic_c05_title
Lunch at a bright cafe near the office, a long table, plates, water glasses, a water bottle. Camera from Dohyun's seat at the end of the table, pulled back so all four SD women are fully visible. Dohyun's SD hand at the bottom edge holds up a small notebook, a sweat drop beside it. The four SD women react differently at once:
- Ria (IMAGE 1): bursting out laughing, slapping the table, tears at her eye corners.
- Jihyun (IMAGE 2): deadpan stare, water glass paused halfway, one eyebrow raised, dotted trail (no letters).
- Yujin (IMAGE 3): leaning back exhausted, swirly eyes, a tiny storm cloud over her head.
- Seoyun (IMAGE 4): chin on her hand, sly smile, pointing at the notebook, sparkle.
Office-casual clothes, warm daylight.
```
