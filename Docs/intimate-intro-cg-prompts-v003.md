# 성인 이벤트 도입 CG 프롬프트 v003 (한 번에 끝내는 판)

v002와 장면은 같다. 아래 네 가지를 더했다.
- 그림체 강화: 마스터 그림을 첨부하고, 그림체 특징을 글로 적고, 시험 그림(리아 마스터 다시 그리기)을 먼저 그린다.
- 속옷 취향: [속옷·잠옷 취향 설정](../CharacterArt/character_art_09_INTIMATE_WEAR.md)을 프롬프트에 넣었다.
- 2·6·9·12번은 '특별한 날의 옷' 입상(`<인물>_special_pose01_neutral.png`)을 따른다. 입상을 먼저 만든다.
- 파일 이름 규칙은 v002와 같다(`CharacterArt/candidates/intro-cgs-v002/`).

첨부할 그림: 마스터 4장(`CharacterArt/candidates/heroine-masters-v001/*_office_pose01_neutral_v001.png`), 각 인물의 사복·생활복·데이트 옷 입상 neutral(있는 것만).

결과는 후보다. 검수와 사용자 승인 전에는 게임에 연결하지 않는다.

```text
Draw intro CGs for an adult office-romance visual novel, ONE image per reply, in order. Before each image write its file name on one line. After each image wait for me to say "next".

REFERENCES: I attached the 4 MASTER sprites (*_office_pose01_neutral_v001.png) plus casual, home and special-outfit sprites. If an attachment is missing, use the public repo github.com/kws07042/office-v2:
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/ria_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/jihyun_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/yujin_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/seoyun_office_pose01_neutral_v001.png
Outfit sprites: https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/<name>/<name>_<casual|home|special>_pose01_neutral.png

ABSOLUTE STYLE RULE: the MASTER sprites are the only allowed art style. Every image must look like the same artist drew it in the same session.
- LINE ART: thin, clean, uniform dark-brown outlines (slightly darker at the outer silhouette), no sketchy, painterly or thick lines.
- EYES: large almond eyes with a thick dark upper lash line ending in a small wing, thin lower lash line, iris gradient from dark at the top to lighter at the bottom, one bright white crescent highlight plus small round white highlights.
- FACE: small pointed chin, tiny nose drawn with a faint shadow only, small mouth, soft pink blush on the cheeks.
- SHADING: anime cel shading, one soft shadow tone with gentle gradient edges, small crisp highlights; warm, clean, slightly glossy finish.
- HAIR: defined strand clumps with bright white glossy highlight bands near the crown.
- BODY: tall slim adult proportions, about 8 heads tall, same build as each master.
- BACKGROUND: same anime style, clean lines, warm interior lighting.
FORBIDDEN: realistic or semi-realistic rendering, 3D, painterly or watercolor texture, thick outlines, flat vector, chibi, a different anime style, glow or bloom, redesigned faces, childlike proportions. If anything conflicts, the masters win.

STEP 0 — text only first: (a) which references you can see, (b) your description of the master style using the traits above, (c) each heroine's identifying features. Wait for my "ok".
STEP 1 — STYLE TEST: redraw ria_office_pose01_neutral_v001.png as exactly as possible on a plain background. Wait for my "ok"; if I say "again", redraw until it matches.
STYLE CHECK: whenever I say "style check", compare your last image with the matching master, list what differs and redraw it.

CHARACTERS (adults 27–32, mature proportions, never childlike; no earrings/necklaces/rings):
- RIA (28): very long wavy blonde high ponytail, BLUE scrunchie, straight bangs, BLUE eyes. Playful, but drops the jokes at serious moments.
- JIHYUN (30): very long straight crimson hair down the back, side-parted bangs, reddish-brown eyes, sharp eyeliner. Says what she wants directly; weak to compliments.
- YUJIN (27): silver-white bob, one gold hairpin, thin round metal glasses always on, amber eyes, curvy. Shy, then suddenly direct.
- SEOYUN (32): long wavy dark plum hair, half-lidded grey-lavender eyes, beauty mark under LEFT eye. Teasing, but completely serious when sincere.

UNDERWEAR TASTE (keep consistent in every scene):
- RIA: cute and bright, comfort first. Cotton sets with thin lace trim and small bows in sky blue, white, mint or navy; lace only on special days. Never black mesh, thongs or garters (except a plain black cotton set on work days).
- JIHYUN: neat even where no one sees. Always a perfectly matching set of plain satin or silk with restrained lace only at the edges, in burgundy, wine, black or ivory. No big bows, frills or prints.
- YUJIN: chooses by color and texture, too shy for flashy pieces. Soft cotton or modal full-coverage sets with a tiny embroidered accent, in peach, sage green, cream or heather grey; her first lace set is sage green.
- SEOYUN: wears what makes her feel good even if unseen. Lace and satin sets in deep plum, black or lavender, with a garter belt and lace-band thigh-highs as her everyday habit.

ONE COHERENT SCENE, NOT A COMPOSITE. 16:9, 1920x1080, no text/logos/UI.
PERSPECTIVE RULES: single camera at standing eye level (about 1.4 m), 35 mm lens, one consistent horizon and vanishing point for the room and the character. The character's size must match the furniture (mattress top reaches her knee when she stands). Show contact: hips sink into the mattress, feet flat on the floor with soft contact shadows. Nothing floats, nothing clips through the bed. Legs angled sideways, never stretched toward the camera.
THE VIEWER is her boyfriend Dohyun: at most his hand and shirt cuff at the frame edge; no face, no body.
CONTENT LIMIT (scenes 1–13): she is half-undressed from the outfit named in each scene, with her bra and panties visible and fully covering; not see-through. No nudity, no nipples, no sexual act, no explicit pose. Romantic, a moment before an intimate scene.

ROOMS (draw once, then reuse the same room for that heroine):
- RIA BEDROOM: warm one-room apartment, wooden bed with white duvet and a pink knit throw, bedside table with a fabric lamp and pink flowers, gingham curtains, hanging plants, open sliding door to a small living room with a sofa.
- JIHYUN BEDROOM: tidy minimal bedroom, grey bedding, a low bookshelf, one bedside lamp, dark curtains; through the open door, her living-room tea table.
- YUJIN ROOM: one-room apartment, white desk with a drawing tablet, window-frame sketches pinned on the wall, sheer curtains, bed with white bedding on the right.
- SEOYUN STUDIO BACK ROOM: small bedroom at the back of her private work studio, low bed with beige and lavender bedding, a desk lamp, stacks of copy drafts and books; through the open door, the studio's sofa and worktable. No family photos or family items.

SCENES — character · scene · moment from the script → outfit / pose / expression / props:
1 RIA · first night, rainy Saturday evening (RIA BEDROOM, rain on the window, warm lamp). She admitted it is her first time too, then laughed. "No umbrella excuse now." Cream cable-knit sweater slipping off one shoulder, showing her sky-blue cotton bra with thin white lace trim, denim mini skirt, sheer pantyhose. Sitting on the bed edge, fingers interlaced with the viewer's hand at the frame edge, other hand gripping the sweater hem. Nervous honest smile with lips pressed together, pink cheeks. Two untouched teacups on the bedside table.
2 RIA · Saturday night after the date, a clear night (RIA BEDROOM, string lights, no rain). She almost changed outfits twice; he noticed right away. She just put her bag down: "I don't have to delete that message anymore." Special date outfit (match ria_special_pose01_neutral.png): baby-blue puff-sleeve blouse unbuttoned and slipping off her shoulders over a white lace bra with blue ribbons, beige suede mini skirt, opaque black tights, her winter coat tossed on the chair. Standing beside the bed, holding the blouse closed at her chest with both hands, bag dropped on the chair, phone face-down on the bedside table. Soft glossy eyes, small relieved smile, deep blush.
3 RIA · Sunday night after making up (RIA BEDROOM). In home clothes, she came over first as she promised. White oversized hoodie slipping off one shoulder showing a navy sporty cotton bra, grey dolphin shorts, hair down, blue scrunchie on her wrist. Kneeling on the bed, holding the viewer's hand and gently pulling him toward her. No joke: soft serious smile, steady eyes. A chopstick wrapper with a little noodle doodle on the bedside table.
4 RIA · station-front motel, Thursday night after work and one soju (small motel room, pink-blue neon through the blinds, the bed visible behind her). Bag hung on the chair; she leaned by the door: "Can I kiss you?" Office look: white blouse unbuttoned to the middle showing a plain black cotton bra, black pencil skirt, sheer black pantyhose, navy lanyard hung on the chair with the bag. Back against the door, one hand on a blouse button, the other reaching for the viewer's collar. Tipsy flush, bold but shy, eyes on the viewer's lips.
5 JIHYUN · Saturday evening after the argument (JIHYUN BEDROOM; through the door, the tea table with two cups and the little wooden window-frame model). She asked for a kiss, then fixed his collar: "Then no need to straighten it again." Her burgundy turtleneck folded neatly on the chair, camel trench on the hook; deep burgundy satin bra with lace only at the edges (matching set) and her long dark skirt with the side zipper open. Standing by the bed, fingertips still on the viewer's shirt collar at the frame edge. Direct calm gaze, faint satisfied smile, light blush.
6 JIHYUN · Friday night after dinner (JIHYUN BEDROOM). She wore this for him, kept touching her sleeve, then got called "pretty". Special outfit (match jihyun_special_pose01_neutral.png): dark forest-green velvet midi dress, back zipper half open and slipping off one shoulder, showing a matching black lace bra, her coat hung neatly on the hook. Sitting on the bed edge, legs crossed, one hand holding her velvet sleeve cuff, face half turned away. Flustered, red ears, losing her composed team-leader face. Phone face-down on the bedside table.
7 JIHYUN · Saturday night, the first night she leans on him (JIHYUN BEDROOM, one lamp, rumpled blanket). She changed into home clothes and sat beside him without hesitation. Taupe knit cardigan slipping off her shoulders over an ivory silk bra, loose lounge pants. Lying on her side, head on her bent arm, patting the space beside her. Relieved half-closed eyes, unguarded smile.
8 YUJIN · Saturday evening, after showing her secret "Changga" drawings (YUJIN ROOM, desk lamp). She held his hand: "Cold hands, right? You thought only you were nervous?" Cream cardigan sliding down to her elbows, white blouse unbuttoned showing a pale peach cotton bra with a tiny embroidered bow, brown pleated skirt, sheer pantyhose. Sitting on the bed edge, both her hands wrapped around the viewer's hand. Trembling shy smile, looking up through her glasses, red ears. The window drawing and a photo-booth strip propped on the desk, two untouched cups.
9 YUJIN · Thursday night after the deadline week (YUJIN ROOM, tablet and coffee cups on the desk). She chose this outfit for a long time; this time she did not look away. Special outfit (match yujin_special_pose01_neutral.png): sage-green ribbed knit midi dress with a thin brown belt, belt undone and the dress pulled down off both shoulders to show a matching sage lace bra, one hand holding her sleeve. Standing beside the bed, bag dropped at her feet, meeting the viewer's eyes. Shy but steady gaze, small brave smile, blush.
10 YUJIN · evening after making up (YUJIN ROOM, only the desk lamp on, dimmed). "Tonight this lighting is enough." She practiced what to say and forgot it halfway. Her oversized white shirt only, top buttons undone, heather-grey cotton panties, black leggings folded on the chair, bare legs. Kneeling on the bed, one hand reaching for the viewer's hand, the other half-raised in a flustered gesture. Mouth open mid-sentence, wide eyes, blushing. A crumpled note on the bed.
11 SEOYUN · Saturday evening, she ran back to stop him from leaving (SEOYUN STUDIO BACK ROOM; through the door, two teacups on the studio table). "I'll take that answer without joking. I want it too." Beige cardigan dropped on the floor, grey knit maxi dress pulled down off both shoulders to her waist, showing a dusty plum lace bra. Standing at the foot of the bed facing the viewer, one hand holding the dress at her waist. No teasing: serious, earnest, flushed. An old paperback with a pencilled date on the bedside table.
12 SEOYUN · Friday night; she avoided answering his question about going public, but wants to stay with him (SEOYUN STUDIO BACK ROOM). Special outfit (match seoyun_special_pose01_neutral.png): black square-neck knit top pulled off one shoulder over a black satin bra, deep plum satin midi skirt, her garter belt and black lace-band thigh-highs showing where the skirt rides up, knee-high boots kicked off by the bed. Sitting on the bed hugging her knees, chin on her knees. Soft, slightly guilty smile, eyes up at the viewer. A glass of water on the bedside table.
13 SEOYUN · night after she ended things with her ex; nothing left to hide (SEOYUN STUDIO BACK ROOM, warm lamp). Home clothes she keeps at the studio: champagne satin pajama shirt unbuttoned over a lavender silk bra, matching satin shorts. Lying back on the pillows, one arm behind her head, knees together and tilted to one side (not toward the camera). The most relaxed open smile.
COSTUME SCENES (R15, after making up). Same room as that heroine's scene above. Each costume is a fully covering adult costume (leotard, dress or uniform), not see-through, no nudity. Professional-adult costume look, nothing school-like.
14 RIA · bunny girl (RIA BEDROOM). "I didn't pick the bunny ears... just kidding, I did." Blue satin bunny suit, white bunny ears, white wrist cuffs and bow tie, sheer black pantyhose. Standing in the bedroom doorway, one hand on the door frame, other hand making a little bunny-ear gesture. Playful grin, deep blush.
15 RIA · nurse (RIA BEDROOM). "You walked all day. I'll do the check-up." White-and-pink mini nurse dress, small nurse cap, white thigh-high stockings, toy stethoscope. Sitting on the bed edge, leaning toward the viewer holding the stethoscope out. Teasing smile.
16 RIA · cheerleader (RIA BEDROOM). "My uniform from the sports pop-up event! Tonight I'm only cheering for you." Blue-and-white pro-team style cheer crop top and pleated skirt, no logos, blue pom-poms, high ponytail with the blue scrunchie. Standing by the bed, one pom-pom raised. Big bright smile.
17 JIHYUN · bunny girl (JIHYUN BEDROOM). "I never even wore this at the event. Laugh and I change back right now." Black satin bunny suit with crimson trim, black bunny ears, sheer black pantyhose, cuffs and bow tie. Standing by the bed, arms crossed, chin up. Proud but blushing to the ears.
18 JIHYUN · nurse (JIHYUN BEDROOM). "You always refilled my water. Tonight I check on you. Results first." Classic white nurse dress, nurse cap, white stockings, clipboard and pen. Standing, clipboard against her hip, pen pointed at the viewer. Confident, faint smile.
19 JIHYUN · china dress (JIHYUN BEDROOM). "The slit is normally this high. ...I picked it for you to look at, so look." Deep crimson silk cheongsam with gold embroidery and a high side slit. Sitting on the bed edge, legs crossed so the slit shows her leg, face turned aside. Composed expression breaking into a shy blush.
20 YUJIN · bunny girl (YUJIN ROOM, dim desk lamp). "This was at the very bottom of the box... but you picked it." Cream-white satin bunny suit with gold trim, white ears, sheer pantyhose, glasses on. Standing by the bed, both hands clasped in front, knees together. Very embarrassed, looking up through her glasses.
21 YUJIN · nurse (YUJIN ROOM). "I can keep my glasses on, right? So I can see your face." Pastel pink nurse dress, nurse cap, white stockings, glasses on. Sitting on the bed, clipboard hugged to her chest. Shy small smile.
22 YUJIN · maid (YUJIN ROOM). "A uniform from the café collab. Y-your order... no, that's not it." Classic black-and-white maid dress with frilly apron and headdress, black thigh-highs, glasses on. Standing by the bed in a small curtsy, holding her skirt. Flustered, mouth open mid-word.
23 SEOYUN · bunny girl (SEOYUN STUDIO BACK ROOM). "Knew you'd pick this one. Laugh and I take it off again... you're laughing." Deep purple satin bunny suit, black ears, sheer black pantyhose, cuffs and bow tie. Leaning against the bedpost, one hand on her hip. Teasing half-lidded smile.
24 SEOYUN · nurse (SEOYUN STUDIO BACK ROOM). "Tell me where it hurts. Tonight I'll take care of you, no jokes." White nurse dress with lavender trim, nurse cap, her garter belt and black lace thigh-highs, stethoscope around her neck. Sitting on the bed, patting the space beside her. Gentle sincere smile.
25 SEOYUN · police (SEOYUN STUDIO BACK ROOM). "Dohyun, answer only what I ask. Did you miss me today?" Navy police-style uniform jacket and mini skirt, peaked cap, toy handcuffs dangling from one finger, black thigh-highs. Standing by the bed, weight on one hip. Smirking, eyes narrowed playfully.

Start with STEP 0.
```
