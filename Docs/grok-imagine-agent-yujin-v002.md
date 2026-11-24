# Grok Imagine 에이전트 · 차유진 전후 CG v002 (마스터 복사 방지 + 방 구조 고정)

리아 v002와 같은 장치를 넣었다.
- 마스터를 그대로 따라 그리지 말라는 규칙
- 마스터 그림체 절대 유지
- 각 작업 끝에 '입상이 아니라 장면'이라는 조건

여기에 **방 구조 고정**을 더했다. 가구와 위치, 색, 카메라 방향을 정해 두어서 18장이 같은 방으로 나오게 했다.
- 왼쪽: 창과 책상
- 가운데: 소파
- 오른쪽: 침대와 협탁

사용법:
1. 에이전트 창에 유진 마스터 입상 한 장을 올린다.
2. 아래 블록을 통째로 붙여 넣는다.
3. 방이 달라진 번호가 있으면 `Redo TASK n in the exact room layout from the ROOM LAYOUT LOCK.`라고 보낸다.

```text
Generate 18 separate images, one per task, in order. Do not merge or skip tasks. Label each image with its task number and file name.

ANTI-COPY RULE (most important):
- The attached master sprite is ONLY a reference for her face, hair, glasses, eye color and drawing style. DO NOT copy its pose, its standing full-body framing, its plain/transparent background or its office outfit.
- NEVER output a standing character sprite on a white, grey or empty background. NEVER just change the clothes on the reference image.
- Every image must be a NEW full-scene CG illustration in the room described below, with the specific pose, camera angle and framing written in that task.
- If an output looks like the reference sprite with different clothes, discard it and draw the scene again.

ROOM LAYOUT LOCK (identical in all 18 images — same furniture, same positions, same colors):
- LEFT WALL: one large window with long cream linen curtains, city night lights outside. Under the window: a white desk with a drawing tablet, a pen cup, a small stack of sketchbooks and a black desk lamp.
- CENTER: a light beige two-seat fabric sofa facing the camera, two sage-green cushions. A small round light-wood side table to the sofa's right with a white mug.
- RIGHT SIDE: a single bed with white sheets and a light grey blanket, headboard against the right wall, a light-wood nightstand beside it with a small round warm lamp.
- BACK WALL: a tall white bookshelf with art books and a few framed pencil sketches pinned above the sofa.
- FLOOR: light oak wood with a round cream rug in front of the sofa.
- LIGHT: warm desk lamp and bedside lamp, cool city light from the window.
- CAMERA: sofa scenes look at the sofa from the front or from the seat beside her (window on the left of the frame, bed on the right). Bed scenes look at the bed from its side, nightstand and lamp visible, window on the left of the frame.
Never move, add or remove these pieces of furniture. Never change the room into a different apartment.

GLOBAL RULES (every task):
- ART STYLE LOCK (absolute, overrides everything else): draw in EXACTLY the master sprite's art style — same clean line weight, same flat cel shading with soft gradients, same coloring and skin tone, same eye shape, iris highlights and face proportions, same hair rendering. No semi-realistic, 3D, painterly, thick-paint or different anime style. Only her pose, outfit, camera and background change; the drawing style never changes.
- Same character, Cha Yujin, adult woman (27): slim adult face, silver-white bob (front slightly longer), side-swept bangs, a gold hairpin on one side, thin round metal-frame glasses (off only when the task says so), amber-brown eyes, calm smile, mature curvy figure, same body proportions.
- ASPECT RATIO: 16:9 WIDE HORIZONTAL LANDSCAPE (like 1920x1080). NOT vertical, NOT square. Korean visual-novel event CG, full scene, no text, no watermark.
- POV RULE: first-person view of the man she is with. NEVER show the back of his head, his shoulders or his back. Only his own hand, forearm, knee or shirt sleeve may appear at the bottom edge, as he would see them himself.
- CONTENT: adult woman. Lingerie, deep cleavage, open garments over lingerie, bare shoulders, thighs and garters are fine. She always wears matching lingerie top AND bottom when undressed. No nudity, no nipples, no genitals, no sexual act. Clothing must be wearable in real life.

TASK 1 — yujin_r07_casual_intro.jpg
Evening, a teacup on the small side table. She sits beside the viewer on the sofa, hands on her knees, looking at him with a blush but not turning away. Cream cable-knit cardigan, white blouse, brown pleated skirt, glasses on. Camera from the seat right beside her on the sofa, the viewer's own knee and hand on the cushion at the bottom edge. Medium shot. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 2 — yujin_r07_casual_intro_shy.jpg
She has moved closer and holds the viewer's hand (at the bottom edge). Her cardigan has slipped to her elbows and her white blouse is unbuttoned and open in front — opaque cotton — showing a pale peach cotton bra with a small embroidered ribbon in the opening. Shy, earnest eyes behind her glasses. Closer shot, chest up. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 3 — yujin_r07_casual_after.jpg
Same room as task 1, late night, lights off. A thin line of streetlight comes through the curtain gap and catches the lenses of her glasses on the nightstand. She lies in bed under the white sheet, bare shoulders, without glasses, looking at the window with a quiet smile. Medium shot. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 4 — yujin_r12_special_intro.jpg
Night after a date, her shearling jacket on the desk chair, her bag set down. She sits on the sofa turned toward the viewer, adjusting her sleeve, smiling and waiting for his reaction. Beige V-neck knit, brown check midi skirt, glasses on. Camera from the seat right beside her on the sofa, the viewer's own knee and hand on the cushion at the bottom edge. Medium shot. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 5 — yujin_r12_special_intro_shy.jpg
She sits pressed close beside the viewer, the beige V-neck knit pulled down below one shoulder showing a sage-green lace bra strap, glasses slightly crooked, happy shy smile. Closer shot, chest up. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 6 — yujin_r12_special_after.jpg
Same room as task 4, late night. She lies in bed under the sheet, bare shoulders, listening to the quiet room with the viewer. Her phone lies on the floor beside the bed, its screen lighting up once. Neither of them looks at it. Wide medium shot. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 7 — yujin_r15_home_intro.jpg
Weekend night. She sits beside the viewer on the sofa in an oversized white shirt and grey leggings, glasses on, looking at his face first with a small smile. Camera from the seat right beside her on the sofa, the viewer's own knee and hand on the cushion at the bottom edge. Medium shot. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 8 — yujin_r15_home_intro_shy.jpg
The oversized white shirt is unbuttoned halfway, showing a heather-grey cotton bra; her leggings are folded on the sofa arm, bare legs. She leans in close, quiet and content. Closer shot, chest up. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 9 — yujin_r15_home_after.jpg
Same room as task 7, later. She sits in bed wrapped in the white sheet, bare shoulders, picking up a small white shirt button from the blanket and holding it tight in her palm, smiling at the viewer. Medium shot. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 10 — yujin_r15_cosplay_bunny_intro.jpg
She stands shyly by the sofa in a cream-white satin bunny leotard with gold trim, sweetheart neckline, high-cut legs, white bunny ears, sheer pantyhose, glasses on, fiddling with a cuff and asking with her eyes to hear 'it suits you' again. Full body. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 11 — yujin_r15_cosplay_bunny_intro_shy.jpg
She sits close beside the viewer in the bunny leotard, quiet, shoulder almost touching his. Faint blush behind her glasses. Closer shot, waist up. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 12 — yujin_r15_cosplay_bunny_after.jpg
Same room as task 7, later, lamp light. The cream bunny ears lie side by side with her glasses on the nightstand. She lies in bed under the sheet, bare shoulders, without glasses, smiling at the viewer. Medium shot. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 13 — yujin_r15_cosplay_nurse_intro.jpg
She stands hugging a clipboard in a pastel pink nurse mini dress with the front buttons open to show a peach lace bra edge, short hem, white thigh-highs, nurse cap, glasses on, blushing. Full body. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 14 — yujin_r15_cosplay_nurse_intro_shy.jpg
She sits close beside the viewer in the nurse dress, clipboard set aside, quiet. Faint blush. Closer shot, waist up. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 15 — yujin_r15_cosplay_nurse_after.jpg
Same room as task 7, later. The pastel pink nurse dress hangs half off a chair, her folded glasses resting on it. She sits in bed wrapped in the sheet, bare shoulders, without glasses, smiling. Medium shot. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 16 — yujin_r15_cosplay_maid_intro.jpg
She curtsies in a black-and-white maid dress with an off-shoulder neckline and a cleavage window, short flared skirt with petticoat, frilled apron, black thigh-highs with garter straps, frilled headband, glasses on, flustered smile. Full body. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 17 — yujin_r15_cosplay_maid_intro_shy.jpg
She sits close beside the viewer in the maid dress, quiet, hands in her lap. Faint blush behind her glasses. Closer shot, waist up. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

TASK 18 — yujin_r15_cosplay_maid_after.jpg
Same room as task 7, later. She lies in bed under the sheet, bare shoulders, laughing as her black-and-white lace headband slips off the viewer's wrist (his hand at the bottom edge) and falls onto the pillow. Medium shot. Draw the full room from the ROOM LAYOUT LOCK behind her. Full scene, not a standalone sprite.

After all 18, list the tasks you completed and any you could not.
```
