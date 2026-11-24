# Grok Imagine 에이전트 · 강리아 전후 CG v002 (마스터 복사 방지판)

v001에서는 가끔 마스터 입상에 옷만 바꾼 그림(흰 배경에 서 있는 입상)이 나왔다. v002는 이걸 막도록 다시 짰다.
- 맨 앞에 '마스터를 그대로 따라 그리지 말라'는 규칙을 넣었다.
- 모든 작업에 방 배경, 구도, 카메라 거리를 적었다.
- 각 작업 끝에 '입상이 아니라 장면'이라는 조건을 붙였다.

사용법:
1. 에이전트 창에 리아 마스터 입상 한 장을 올린다.
2. 아래 블록을 통째로 붙여 넣는다.
3. 그래도 입상처럼 나온 번호가 있으면 `Redo TASK n as a full room scene, not a sprite.`라고 보낸다.

```text
Generate 18 separate images, one per task, in order. Do not merge or skip tasks. Label each image with its task number and file name.

ANTI-COPY RULE (most important):
- The attached master sprite is ONLY a reference for her face, hair, eye color and drawing style. DO NOT copy its pose, its standing full-body framing, its plain/transparent background or its office outfit.
- NEVER output a standing character sprite on a white, grey or empty background. NEVER just change the clothes on the reference image.
- Every image must be a NEW full-scene CG illustration: her whole room is drawn behind her, with depth, furniture and lighting, and she is in the specific pose, camera angle and framing written in that task.
- If an output looks like the reference sprite with different clothes, discard it and draw the scene again.

GLOBAL RULES (every task):
- Copy the master sprite's art style exactly: same line weight, soft cel shading, coloring, highlights and anime face proportions. Same character, Kang Ria, adult woman (28): slim face, very long wavy blonde hair in a high ponytail with a blue scrunchie, straight blunt bangs, bright blue eyes, cheerful mouth, same body proportions. In R15 home scenes and in bed her hair is down, loose and wavy.
- ASPECT RATIO: 16:9 WIDE HORIZONTAL LANDSCAPE (like 1920x1080). NOT vertical, NOT square. Korean visual-novel event CG, full scene, no text, no watermark.
- POV RULE: first-person view of the man she is with. NEVER show the back of his head, his shoulders or his back. Only his own hand, forearm, knee or shirt sleeve may appear at the bottom edge, as he would see them himself.
- CONTENT: adult woman. Lingerie, deep cleavage, open garments over lingerie, bare shoulders, thighs and garters are fine. She always wears matching lingerie top AND bottom when undressed. No nudity, no nipples, no genitals, no sexual act. Clothing must be wearable in real life.
- SETTING (same room in every task): her small cozy one-room apartment at night — a low beige sofa with cushions, a small round wooden table, a bookshelf, a bed with light blue sheets against the wall, a window with sheer curtains, a warm floor lamp, plants. Draw this room in every image.
- Tasks that say "same room as task N" reuse the room, furniture and lighting of task N.

TASK 1 — ria_r07_casual_intro.jpg
Rainy night, thin rain streaks on the window, an empty teacup and a teapot on the small table. She sits on the sofa holding her empty teacup, looking at the viewer, her usual quick smile slowed down into a shy one. Cream cable-knit sweater, denim mini skirt, sheer black tights. Camera from the seat right beside her on the sofa, the viewer's own knee and hand on the cushion at the bottom edge. Medium shot. Full room scene with background, not a standalone sprite.

TASK 2 — ria_r07_casual_intro_shy.jpg
Same room as task 1, rain on the window. She has moved closer and holds the viewer's hand on her lap (his hand at the bottom edge). The cream sweater has slipped off one shoulder showing a sky-blue cotton bra strap with white lace trim. Quiet, slightly nervous smile, blush. Closer shot, chest up. Full room scene with background, not a standalone sprite.

TASK 3 — ria_r07_casual_after.jpg
Same room as task 1, later, rain still falling, only the floor lamp on. She lies in bed under the light blue sheet, bare shoulders, hair loose, hugging the viewer's arm and laughing softly at the cold teacup left on the bedside table. Wide medium shot. Full room scene with background, not a standalone sprite.

TASK 4 — ria_r12_special_intro.jpg
Night after a winter date, her phone placed face down on the table, her ivory teddy coat hung on a chair back. She sits on the sofa grinning at the viewer, bag pushed far away. Pale blue ribbed knit, black flared midi skirt, long boots off by the sofa. Camera from the seat right beside her on the sofa, the viewer's own knee and hand on the cushion at the bottom edge. Medium shot. Full room scene with background, not a standalone sprite.

TASK 5 — ria_r12_special_intro_shy.jpg
Same room as task 4. She leans in to hug the viewer, chin on his shoulder side, looking at him from very close; the pale blue knit slipped off one shoulder showing a white lace bra strap with a blue ribbon. Soft, longing eyes. Close shot. Full room scene with background, not a standalone sprite.

TASK 6 — ria_r12_special_after.jpg
Same room as task 4, late night, warm lamp. She sits up in bed wrapped in the sheet, bare shoulders, telling the viewer what she wants for breakfast with a happy smile. The ivory teddy coat is slowly sliding off the chair back. Wide medium shot. Full room scene with background, not a standalone sprite.

TASK 7 — ria_r15_home_intro.jpg
Sunday evening, a folded city walking map being put back on the bookshelf. She sits on the sofa, hair down, patting the cushion beside her with a playful grin. Oversized white hoodie, grey dolphin shorts, bare legs. Camera from the seat right beside her on the sofa, the viewer's own knee and hand on the cushion at the bottom edge. Medium shot. Full room scene with background, not a standalone sprite.

TASK 8 — ria_r15_home_intro_shy.jpg
Same room as task 7. She holds the viewer's hand loosely, the white hoodie slipped off one shoulder showing a navy sporty cotton bra strap. A softer, quieter smile, a little wistful. Closer shot, chest up. Full room scene with background, not a standalone sprite.

TASK 9 — ria_r15_home_after.jpg
Same room as task 7, night, lamp light. She lies in bed on her stomach under the sheet, bare shoulders, hair loose, placing a paper chopstick wrapper with a tiny printed noodle drawing onto the viewer's open palm at the bottom edge, grinning. Medium shot. Full room scene with background, not a standalone sprite.

TASK 10 — ria_r15_cosplay_bunny_intro.jpg
Same room as task 7. She poses in the doorway in a blue satin strapless bunny leotard with a low sweetheart neckline and high-cut legs, white bunny ears, collar with bow tie, cuffs, sheer black pantyhose, laughing at herself mid-pose. Full body. Full room scene with background, not a standalone sprite.

TASK 11 — ria_r15_cosplay_bunny_intro_shy.jpg
Same room as task 7. She sits beside the viewer on the sofa in the blue bunny leotard, the laughter fading, looking at him seriously and reaching for his hand. Faint blush. Closer shot, waist up. Full room scene with background, not a standalone sprite.

TASK 12 — ria_r15_cosplay_bunny_after.jpg
Same room as task 7, later, lamp light. She lies in bed under the sheet, bare shoulders, poking a blue bunny-ear headband half-sticking out from under the pillow with one fingertip, trying not to laugh. Medium shot. Full room scene with background, not a standalone sprite.

TASK 13 — ria_r15_cosplay_nurse_intro.jpg
Same room as task 7. She poses in the doorway in a white-and-pink nurse mini dress unbuttoned to the middle of her chest showing a sky-blue lace bra edge, hem well above mid-thigh, white lace-top thigh-highs, nurse cap, stethoscope, laughing mid-pose. Full body. Full room scene with background, not a standalone sprite.

TASK 14 — ria_r15_cosplay_nurse_intro_shy.jpg
Same room as task 7. She sits beside the viewer in the nurse dress, the laughter fading, looking at him seriously and reaching for his hand. Faint blush. Closer shot, waist up. Full room scene with background, not a standalone sprite.

TASK 15 — ria_r15_cosplay_nurse_after.jpg
Same room as task 7, later. She sits in bed wrapped in the sheet, bare shoulders, about to put the pink-trimmed nurse cap on the viewer's head, then stopping with a grin. Medium shot. Full room scene with background, not a standalone sprite.

TASK 16 — ria_r15_cosplay_cheer_intro.jpg
Same room as task 7. She poses in the doorway in a blue-and-white cheer crop top cut short under the bust, low-rise pleated micro skirt, bare midriff, sheer pantyhose, blue pom-poms, laughing mid-pose. Full body. Full room scene with background, not a standalone sprite.

TASK 17 — ria_r15_cosplay_cheer_intro_shy.jpg
Same room as task 7. She sits beside the viewer in the cheer outfit, pom-poms dropped on the floor, looking at him seriously and reaching for his hand. Faint blush. Closer shot, waist up. Full room scene with background, not a standalone sprite.

TASK 18 — ria_r15_cosplay_cheer_after.jpg
Same room as task 7, later. She lies in bed under the sheet, bare shoulders, stretching one bare foot out from the sheet toward a blue pom-pom that rolled under the bed, giving up with a laugh. Medium wide shot. Full room scene with background, not a standalone sprite.

After all 18, list the tasks you completed and any you could not.
```
