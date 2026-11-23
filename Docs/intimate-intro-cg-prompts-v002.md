# 성인 이벤트 도입 CG 프롬프트 v002 (대사 흐름 기준, 전체 다시 뽑기)

v001 결과(`codex/intro-cgs-v001`)에서 원근이 깨진 그림(02·03·06·13)과 침대가 없는 그림(05·11·12)이 나와 전체를 다시 뽑는다. v001과 달라진 점은 아래와 같다.
- 의상: 속옷만 입히지 않는다. 장면 직전 대본에서 입고 있던 옷을 반쯤 벗은 상태로 그린다(대본의 사복·특별한 날의 옷·생활복). 노출과 성행위는 없다.
- 장소: 침실에서 침대가 보이게 한다. 서윤은 작업실 안쪽 작은 침실이다(가족 물건 없음).
- 원근: 한 장면으로 그리고, 카메라 높이와 몸이 닿는 곳을 고정한다. 같은 히로인의 방은 첫 장면의 방을 다시 쓴다.
- 손: 도현은 손과 소매만 화면 가장자리에 나올 수 있다.

'특별한 날의 옷'(R12)은 대본에 모양이 정해져 있지 않다. 이 문서에서 처음 정한다(지현·유진·서윤은 대본대로 소매가 있는 옷). 사용자 확인이 필요하다.

R15 코스프레는 2026-11-23 사용자 결정으로 바꿨다. 공통 두 벌(바니걸·간호사)과 히로인 전용 한 벌(리아 치어리더, 지현 차이나드레스, 유진 메이드, 서윤 여경찰) 중 하나를 고른다. 예전 탐정·마술사 재킷은 폐기한다. 각 장면의 대사는 대본의 의상 선택 대사를 그대로 쓴다.

결과는 후보다. 검수와 사용자 승인 전에는 게임에 연결하지 않는다.

## 0단계: 그림체 맞추기 (새 대화에서는 반드시 맨 앞에 붙인다)

새 ChatGPT 대화는 이전 그림을 기억하지 못해서 그림체가 무너진다. 아래 블록을 장면 프롬프트 **바로 앞에** 붙인다. 저장소는 공개라서 아래 주소는 로그인 없이 열린다(2026-11-23 확인). 그래도 ChatGPT가 그림을 열지 못한다고 하면, 마스터 그림 네 장을 직접 첨부하는 것이 가장 확실하다.

```text
STEP 0 — STYLE LOCK. Before drawing anything, open and look at these reference images (public GitHub, no login needed):
MASTER STYLE + FACES (highest priority):
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/ria_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/jihyun_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/yujin_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/seoyun_office_pose01_neutral_v001.png
OUTFITS (casual and home clothes):
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/ria/ria_casual_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/ria/ria_home_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/jihyun/jihyun_casual_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/jihyun/jihyun_home_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/yujin/yujin_casual_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/yujin/yujin_home_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/seoyun/seoyun_casual_pose01_neutral.png
https://raw.githubusercontent.com/kws07042/office-v2/main/Source/game/images/characters/seoyun/seoyun_home_pose01_neutral.png
APPROVED SCENE EXAMPLES (room, lighting and rendering level to match):
https://raw.githubusercontent.com/kws07042/office-v2/codex/intro-cgs-v001/CharacterArt/candidates/intro-cgs-v001/01_ria_rainy_night.png
https://raw.githubusercontent.com/kws07042/office-v2/codex/intro-cgs-v001/CharacterArt/candidates/intro-cgs-v001/07_jihyun_bedside.png
https://raw.githubusercontent.com/kws07042/office-v2/codex/intro-cgs-v001/CharacterArt/candidates/intro-cgs-v001/08_yujin_window.png

Then, BEFORE the first image, reply in text only: (a) whether you could open each image, (b) a short description of the art style you see — line weight and line color, how the eyes are drawn (shape, iris gradient, highlight shapes), shading type, skin and hair rendering, color temperature, (c) each heroine's identifying features. Wait for my "ok".
In every image afterwards: copy that exact style. Same face shape, same eye shape and highlights, same thin dark-brown line art, same soft two-tone cel shading with gentle gradients, same glossy hair strands, warm soft lighting. Do NOT switch to realistic, 3D, semi-real, thick-outline, flat-vector or a different anime style. Do not redesign faces. If I say "style check", compare your last image with the master images and redraw what differs.
If you cannot open the links, tell me and I will attach the images.
```

## 1단계: 장면 프롬프트 (0단계 바로 뒤에 붙인다)

```text
Draw intro CGs for an adult office-romance visual novel, ONE image per reply, in order. After each image wait for me to say "next". Reference repo: github.com/kws07042/office-v2

STYLE (absolute): copy the master sprites in CharacterArt/candidates/heroine-masters-v001/ — same line weight, cel shading, eye rendering, hair strands. Outfits: Source/game/images/characters/<name>/<name>_<casual|home>_pose01_neutral.png.
CHARACTERS (adults 27–32, mature proportions, never childlike; no earrings/necklaces/rings):
- RIA (28): very long wavy blonde high ponytail, BLUE scrunchie, straight bangs, BLUE eyes. Playful, but drops the jokes at serious moments.
- JIHYUN (30): very long straight crimson hair down the back, side-parted bangs, reddish-brown eyes, sharp eyeliner. Says what she wants directly; weak to compliments.
- YUJIN (27): silver-white bob, one gold hairpin, thin round metal glasses always on, amber eyes, curvy. Shy, then suddenly direct.
- SEOYUN (32): long wavy dark plum hair, half-lidded grey-lavender eyes, beauty mark under LEFT eye. Teasing, but completely serious when sincere.

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
1 RIA · first night, rainy Saturday evening (RIA BEDROOM, rain on the window, warm lamp). She admitted it is her first time too, then laughed. "No umbrella excuse now." Cream cable-knit sweater slipping off one shoulder showing a sky-blue bra strap, denim mini skirt, sheer pantyhose. Sitting on the bed edge, fingers interlaced with the viewer's hand at the frame edge, other hand gripping the sweater hem. Nervous honest smile with lips pressed together, pink cheeks. Two untouched teacups on the bedside table.
2 RIA · Saturday night after the date, a clear night (RIA BEDROOM, string lights, no rain). She almost changed outfits twice; he noticed right away. She just put her bag down: "I don't have to delete that message anymore." Special date outfit: sky-blue off-shoulder knit mini dress, back zipper half open, sliding off to show a white lace bra with blue ribbons. Standing beside the bed, holding the dress at her chest with both hands, bag dropped on the chair, phone face-down on the bedside table. Soft glossy eyes, small relieved smile, deep blush.
3 RIA · Sunday night after making up (RIA BEDROOM). In home clothes, she came over first as she promised. White oversized hoodie slipping off one shoulder showing a navy bra, grey dolphin shorts, hair down, blue scrunchie on her wrist. Kneeling on the bed, holding the viewer's hand and gently pulling him toward her. No joke: soft serious smile, steady eyes. A chopstick wrapper with a little noodle doodle on the bedside table.
4 RIA · station-front motel, Thursday night after work and one soju (small motel room, pink-blue neon through the blinds, the bed visible behind her). Bag hung on the chair; she leaned by the door: "Can I kiss you?" Office look: white blouse unbuttoned to the middle showing a black bra, black pencil skirt, sheer black pantyhose, navy lanyard hung on the chair with the bag. Back against the door, one hand on a blouse button, the other reaching for the viewer's collar. Tipsy flush, bold but shy, eyes on the viewer's lips.
5 JIHYUN · Saturday evening after the argument (JIHYUN BEDROOM; through the door, the tea table with two cups and the little wooden window-frame model). She asked for a kiss, then fixed his collar: "Then no need to straighten it again." Her burgundy turtleneck folded neatly on the chair, camel trench on the hook; deep burgundy lace bra and her long dark skirt with the side zipper open. Standing by the bed, fingertips still on the viewer's shirt collar at the frame edge. Direct calm gaze, faint satisfied smile, light blush.
6 JIHYUN · Friday night after dinner (JIHYUN BEDROOM). She wore this for him, kept touching her sleeve, then got called "pretty". Special outfit: deep wine-red long-sleeve wrap dress, tie undone, falling open over a black lace bra and panties. Sitting on the bed edge, legs crossed, one hand holding her sleeve cuff, face half turned away. Flustered, red ears, losing her composed team-leader face. Phone face-down on the bedside table.
7 JIHYUN · Saturday night, the first night she leans on him (JIHYUN BEDROOM, one lamp, rumpled blanket). She changed into home clothes and sat beside him without hesitation. Taupe knit cardigan slipping off her shoulders over an ivory silk bra, loose lounge pants. Lying on her side, head on her bent arm, patting the space beside her. Relieved half-closed eyes, unguarded smile.
8 YUJIN · Saturday evening, after showing her secret "Changga" drawings (YUJIN ROOM, desk lamp). She held his hand: "Cold hands, right? You thought only you were nervous?" Cream cardigan sliding down to her elbows, white blouse unbuttoned showing a pale peach bra, brown pleated skirt, sheer pantyhose. Sitting on the bed edge, both her hands wrapped around the viewer's hand. Trembling shy smile, looking up through her glasses, red ears. The window drawing and a photo-booth strip propped on the desk, two untouched cups.
9 YUJIN · Thursday night after the deadline week (YUJIN ROOM, tablet and coffee cups on the desk). She chose this outfit for a long time; this time she did not look away. Special outfit: sage-green long-sleeve knit dress with a small ribbon collar, pulled down off both shoulders to show a sage lace bra, one hand holding her sleeve. Standing beside the bed, bag dropped at her feet, meeting the viewer's eyes. Shy but steady gaze, small brave smile, blush.
10 YUJIN · evening after making up (YUJIN ROOM, only the desk lamp on, dimmed). "Tonight this lighting is enough." She practiced what to say and forgot it halfway. Her oversized white shirt only, top buttons undone, heather-grey cotton panties, black leggings folded on the chair, bare legs. Kneeling on the bed, one hand reaching for the viewer's hand, the other half-raised in a flustered gesture. Mouth open mid-sentence, wide eyes, blushing. A crumpled note on the bed.
11 SEOYUN · Saturday evening, she ran back to stop him from leaving (SEOYUN STUDIO BACK ROOM; through the door, two teacups on the studio table). "I'll take that answer without joking. I want it too." Beige cardigan dropped on the floor, grey knit maxi dress pulled down off both shoulders to her waist, showing a dusty plum lace bra. Standing at the foot of the bed facing the viewer, one hand holding the dress at her waist. No teasing: serious, earnest, flushed. An old paperback with a pencilled date on the bedside table.
12 SEOYUN · Friday night; she avoided answering his question about going public, but wants to stay with him (SEOYUN STUDIO BACK ROOM). Special outfit: black satin long-sleeve blouse fully unbuttoned over a black lace bra, lavender high-waist midi skirt, her garter belt and black lace-band thigh-highs visible at the hem. Sitting on the bed hugging her knees, chin on her knees. Soft, slightly guilty smile, eyes up at the viewer. A glass of water on the bedside table.
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

Start with scene 1.
```

## 파일 이름 (올릴 때)
`CharacterArt/candidates/intro-cgs-v002/` 폴더에 장면 번호로 저장한다.

| 번호 | 파일 | 이벤트 |
|---|---|---|
| 01 | `01_ria_r07_casual_intro.png` | ria_r07 |
| 02 | `02_ria_r12_special_intro.png` | ria_r12 |
| 03 | `03_ria_r15_home_intro.png` | ria_r15 home |
| 04 | `04_ria_o04_motel_intro.png` | ria_o04 |
| 05 | `05_jihyun_r07_casual_intro.png` | jihyun_r07 |
| 06 | `06_jihyun_r12_special_intro.png` | jihyun_r12 |
| 07 | `07_jihyun_r15_home_intro.png` | jihyun_r15 home |
| 08 | `08_yujin_r07_casual_intro.png` | yujin_r07 |
| 09 | `09_yujin_r12_special_intro.png` | yujin_r12 |
| 10 | `10_yujin_r15_home_intro.png` | yujin_r15 home |
| 11 | `11_seoyun_r07_casual_intro.png` | seoyun_r07 |
| 12 | `12_seoyun_r12_special_intro.png` | seoyun_r12 |
| 13 | `13_seoyun_r15_home_intro.png` | seoyun_r15 home |
| 14 | `14_ria_r15_bunny_intro.png` | ria_r15 cosplay · bunny |
| 15 | `15_ria_r15_nurse_intro.png` | ria_r15 cosplay · nurse |
| 16 | `16_ria_r15_cheer_intro.png` | ria_r15 cosplay · cheer |
| 17 | `17_jihyun_r15_bunny_intro.png` | jihyun_r15 cosplay · bunny |
| 18 | `18_jihyun_r15_nurse_intro.png` | jihyun_r15 cosplay · nurse |
| 19 | `19_jihyun_r15_qipao_intro.png` | jihyun_r15 cosplay · qipao |
| 20 | `20_yujin_r15_bunny_intro.png` | yujin_r15 cosplay · bunny |
| 21 | `21_yujin_r15_nurse_intro.png` | yujin_r15 cosplay · nurse |
| 22 | `22_yujin_r15_maid_intro.png` | yujin_r15 cosplay · maid |
| 23 | `23_seoyun_r15_bunny_intro.png` | seoyun_r15 cosplay · bunny |
| 24 | `24_seoyun_r15_nurse_intro.png` | seoyun_r15 cosplay · nurse |
| 25 | `25_seoyun_r15_police_intro.png` | seoyun_r15 cosplay · police |
