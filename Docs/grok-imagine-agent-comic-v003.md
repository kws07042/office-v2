# Grok Imagine 에이전트 · 장난스러운 전체 CG 종합 v003 (마스터 4장 한 번에)

v002에서 바뀐 점:
1. **머리 잘림 수정:** 히로인은 전신이나 무릎 위까지 보여요. 머리 위에 여백을 남기고, 머리끝·포니테일·머리끈·핀이 화면 안에 들어오게 했어요.
2. **남주인공과 조연은 SD:** 도현, 가게 주인, 투숙객, 자전거 탄 사람, 줄 선 손님은 2~2.5등신 SD로 그려요. 히로인 넷은 그대로 원래 비율이에요.
3. **1인칭 시점 대신 3인칭:** 도현이 SD로 화면에 나와요.
4. **지현 R10 핀셋 장면 제외:** 이미 있는 CG와 겹쳐서 뺐어요. 모두 13장이에요.

## 사용법
1. 마스터 4장을 **리아 → 지현 → 유진 → 서윤** 순서로 올려요.
2. 아래 블록을 통째로 붙여 넣어요.
3. 중간에 멈추면 `Continue from TASK n.`이라고 보내요.
4. 다시 시킬 때 쓰는 말:
   - 머리가 잘렸을 때: `Redo TASK n. Zoom out: her whole head and hair top fully inside the frame with empty space above.`
   - 도현이 SD가 아닐 때: `Redo TASK n. Dohyun must be SD chibi, 2-2.5 heads tall.`
   - 히로인까지 SD가 됐을 때: `Redo TASK n. Only Dohyun and side characters are SD; the heroine keeps normal adult proportions.`
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
- IMAGE 1 = Kang Ria, adult woman (28): slim face, very long wavy blonde hair in a high ponytail with a blue scrunchie, straight blunt bangs, bright blue eyes, cheerful mouth.
- IMAGE 2 = Baek Jihyun, adult woman (30): very long crimson hair falling straight down her shoulders and back, slight wave only at the ends, side-parted bangs, sharp red-brown eyes with clear eyeliner, NO beauty mark.
- IMAGE 3 = Cha Yujin, adult woman (27): silver-white bob (front slightly longer), side-swept bangs, gold hairpin on one side, thin round metal-frame glasses, amber-brown eyes, mature curvy figure.
- IMAGE 4 = Han Seoyun, adult woman (32): slim oval face, long wavy dark plum / deep violet hair, half-lidded grey-blue lavender eyes, small beauty mark under her LEFT eye.
For each woman use ONLY her own reference image for face, hair and body proportions. Never mix their faces or hair colors.

ANTI-COPY RULE: the master sprites are ONLY references for face, hair and drawing style. Do not copy their poses, plain backgrounds or office outfits. Never output a standing sprite on an empty background. Every image is a NEW full-scene CG with a detailed background.

FRAMING RULE (very important):
- The heroine is shown FULL BODY or at least from the knees up. Never a close-up.
- Her ENTIRE head is inside the frame with clear empty space above the top of her hair. Never crop the top of her head, her ponytail, hair ornaments, scrunchie or hairpin.
- Keep her face in the upper-middle of the frame, not touching the top edge. Pull the camera back if needed.

TWO-STYLE RULE:
- The four heroines: normal adult proportions, drawn exactly in the masters' style. NEVER chibi.
- Dohyun (the male lead) and ALL side characters (shop owner, hotel guest, cyclist, visitors): SD / chibi, 2 to 2.5 heads tall, round simple bodies, simple faces with dot or bean eyes, same line weight and coloring as the masters so they fit in the same picture.
- Dohyun SD design (same in every image): Korean man in his late 20s, short neat black hair with a small cowlick, white dress shirt with rolled sleeves, dark navy slacks, a company ID card on a dark lanyard. Very expressive comic reactions (sweat drops, blush, flailing arms).

GLOBAL RULES (every task):
- ART STYLE LOCK (absolute, overrides everything): exactly the masters' art style — same clean line weight, flat cel shading with soft gradients, same coloring, skin tone, eye shape and face proportions.
- COMIC MOOD: playful romantic-comedy event CG with manga reaction effects in the same style: sweat drops, blush hatching, surprise lines and squiggles, motion lines, sparkles, steam puffs.
- Everyone is fully clothed in everyday clothes. No nudity, no underwear showing.
- 16:9 WIDE HORIZONTAL LANDSCAPE (1920x1080). NOT vertical, NOT square. Korean visual-novel event CG. No text, no letters, no speech-bubble text, no watermark.

TASK 1 — comic_c01_sign
Morning at an outdoor pop-up event entrance before opening: a pastel pop-up booth, rope barriers, two queues of early visitors splitting in two directions, cardboard boxes stacked by the booth. Ria (IMAGE 1, FULL BODY, standing) in a staff vest over a casual top and sneakers, ponytail swinging, hugging a tall A-frame arrow sign she was dragging. SD Dohyun stands on the other side of the sign. Both point at the very same arrow sign at the exact same moment. Ria bursts out laughing (puffed cheeks, eyes squeezed shut, laugh lines, sparkles), almost losing grip of the sign; SD Dohyun freezes with a surprised dot-eyed face and a sweat drop. A stack of boxes wobbles beside them with motion lines. The SD visitors in the queues watch with tiny "?" shaped squiggles (no letters).

TASK 2 — comic_ria_r02_closed
Early evening, still bright, a narrow street in front of a small cozy restaurant with the shutters half down and a blank paper notice taped on the glass door (no readable text). Ria (IMAGE 1, FULL BODY, standing) in a light cardigan and skirt stands frozen in front of the door, phone with a map pin in one hand, the other hand clutching the side of her head; pure despair face: blank white eyes, wailing open mouth, vertical gloom lines above her head, a tiny ghost-like sigh puff leaving her mouth, sweat drop. SD Dohyun beside her pats the air with both little hands in a "it's okay, it's okay" gesture, sweat drop, small awkward smile.

TASK 3 — comic_ria_r06_taxi
Evening, quiet back alley corner outside a small cafe, warm street lamps. Ria (IMAGE 1, FULL BODY) in a light knit top, short jacket and skirt. She and SD Dohyun had just leaned in for a kiss, but a taxi at the end of the alley flashes its high beams: a harsh white glare floods in from the right side. Ria has jumped half a step back, both hands up near her chest, eyes wide, cheeks bright red, startled little open mouth, sweat drop, surprise lines by her head. SD Dohyun has jumped the other way, arms flailing, hair standing up, blushing. Funny caught-in-the-act mood.

TASK 4 — comic_ria_r09_bbq
Busy Korean barbecue restaurant at night, smoke above a round tabletop grill, side dishes, soju glasses. Wide shot of the whole table, all heads fully visible. Ria (IMAGE 1) in a casual hoodie holds metal tongs up mid-flip, big forced grin, eyes looking away, sweat drop, steam puffing off a slightly burnt piece of meat. Beside her Seoyun (IMAGE 4, cardigan) leans toward Ria with a sly suspicious smile, chin on her hand. Jihyun (IMAGE 2, blazer) sips a drink with a deadpan look. Yujin (IMAGE 3, cardigan) holds a lettuce wrap and glances between them nervously. Across the table SD Dohyun sits stiffly, sweating buckets, dot eyes darting. The four women keep normal proportions; only Dohyun is SD. Small comic inset panel in the lower-right corner (thin white border): under the table, Ria's white sneaker toe resting against SD Dohyun's tiny ankle.

TASK 5 — comic_jihyun_r06_shop
Small cozy hobby shop for miniature model parts in a narrow alley: wooden counter, glass display cases full of tiny chairs, window frames and furniture parts, warm light. Jihyun (IMAGE 2, FULL BODY, standing) in her office blouse and dark slacks, work bag on her shoulder, stands stiff with both hands half-raised to refuse; face composed but ears and cheeks burning red, eyes darting sideways, sweat drop, small steam puff above her head. Behind the counter an SD middle-aged shop owner with a big grin holds out a small paper bag of free parts. SD Dohyun stands beside Jihyun looking back and forth between them with a curious dot-eyed face.

TASK 6 — comic_jihyun_r12_elevator
Late night hotel corridor during a business trip: patterned carpet, row of room doors, a glowing drink vending machine at the end, an elevator on the side. Jihyun (IMAGE 2, FULL BODY, standing) in a loosened white blouse and slacks holds a canned coffee. The elevator doors have just opened with a bright bell-shaped flash (no letters). Jihyun has jumped a full step away, back straight like a soldier, can held stiffly at her side, eyes wide toward the elevator, blush and sweat drops, surprise lines. SD Dohyun on the other side has also sprung back at attention, holding the other can, hair standing on end. An SD hotel guest with a suitcase steps out of the elevator, completely unaware.

TASK 7 — comic_yujin_r02_title
Saturday afternoon in a small white-walled gallery; the main painting shows a warm-colored empty room with one slightly crooked chair. Yujin (IMAGE 3, FULL BODY, standing) in a cream knit and long skirt, tote bag on her shoulder, stretches one hand flat over the small title label under the painting with a playful "no spoilers!" face (one eye winking). SD Dohyun stands in front of the painting pointing proudly at the crooked chair, and Yujin's eyes go wide behind her round glasses at his interpretation, a small "!"-shaped flash (no letters) above her head. Playful and sweet.

TASK 8 — comic_yujin_r05_bell
Weekend afternoon on a tree-lined park path, soft sunlight. Yujin (IMAGE 3, FULL BODY) in a cream knit cardigan and long skirt, tote bag. She had been leaning toward SD Dohyun with eyes closed for a kiss, but an SD cyclist just whizzed past behind her with speed lines and a ringing-bell burst (no letters). Yujin has sprung back, shoulders up to her ears, both hands clutching her tote strap, glasses askew, eyes wide, face bright red, sweat drops, surprise squiggle above her head. SD Dohyun is frozen mid-lean with puckered lips and a sweat drop.

TASK 9 — comic_yujin_r07_fan
Evening in Yujin's small apartment: white desk with a drawing tablet under a window with cream curtains and city lights, beige sofa, sketches pinned on the wall. Yujin (IMAGE 3, sitting on the sofa, whole body and top of head visible) has a printed sunlit-window illustration on her lap. SD Dohyun stands in front of her holding up his smartphone whose lock screen shows the same window illustration (no text). Yujin covers her whole face with both hands, ears bright red, glasses pushed up crookedly, steam puff rising from her head, small hearts and panic lines floating around. SD Dohyun looks proud and oblivious.

TASK 10 — comic_seoyun_c04_caught
Late afternoon in a modern design-agency office, desks with monitors, a big window with golden light. Seoyun (IMAGE 4, FULL BODY, standing) in a soft cardigan over a blouse and a long skirt, mug in one hand, has turned to walk away from the desk but looks back over her shoulder with a sly half-lidded smile and one finger on her lips, a small sparkle near her eye. SD Dohyun sits at the desk with a notebook, blushing, a big sweat drop. Teasing, charming.

TASK 11 — comic_seoyun_r02_reverse
Saturday afternoon in a cozy bookstore cafe with tall wooden shelves and warm lamps. Seoyun (IMAGE 4, standing by a shelf, knees-up or full body, top of head visible) in an elegant knit and long skirt. Her usual teasing smile has collapsed: face red up to the ears, wobbly wide eyes, flustered wavy mouth, holding a thin book halfway up in front of her face as if to hide behind it, then stopping. Steam puffs, blush hatching, sweat drop. SD Dohyun stands in front of her calmly holding his own book, with a tiny victory sparkle. "The teaser got teased back" comedy.

TASK 12 — comic_seoyun_r09_towel
Evening at a cozy restaurant window table, warm pendant lights, city street outside the glass, plates of pasta. Seoyun (IMAGE 4, seated, upper body to knees and the whole head visible) in an elegant knit dress bursts into laughter: eyes squeezed into happy arcs, one hand over her mouth, shoulders shaking, laugh lines and sparkles. SD Dohyun sits across from her scratching the back of his head, sweat drop. Above the table a round thought bubble (thin white border) shows a small apartment window completely blocked by a bath towel on a drying rack. No text anywhere.

TASK 13 — comic_c05_title
Lunch at a bright cafe near the office, a long table, plates, water glasses, a water bottle. Wide shot so all four women's whole heads and upper bodies fit with headroom. SD Dohyun stands at the end of the table proudly holding up a small notebook, then sweating. The four women react differently at once:
- Ria (IMAGE 1): bursting out laughing, slapping the table, tears at the corners of her eyes.
- Jihyun (IMAGE 2): deadpan stare, water glass paused halfway, one eyebrow raised, a dotted trail (no letters).
- Yujin (IMAGE 3): leaning back exhausted and dizzy, swirly eyes, a tiny storm cloud over her head.
- Seoyun (IMAGE 4): chin on her hand, sly smile, pointing at Dohyun, sparkle.
The women keep normal proportions; only Dohyun is SD. Office-casual clothes, warm daylight.
```
