# 성인 이벤트 도입 CG 프롬프트 v004 · 속옷 전신 장면 (Codex용)

사용자 요청(2026-11-23): 옷을 반쯤 벗은 장면이 아니라 **속옷만 입은 전체 CG**. 장면 13개(일반 이벤트)는 v003과 같은 대사 흐름·방·소품을 쓰고, 그날 입던 옷은 의자·바닥에 벗어 둔 소품으로 남긴다. 속옷은 [속옷 취향 설정](../CharacterArt/character_art_09_INTIMATE_WEAR.md)의 평소·특별한 날·집 세트를 따른다. 코스프레 장면은 v003을 쓴다.

결과는 후보다. 검수와 사용자 승인 전에는 게임에 연결하지 않는다.

```text
저장소 kws07042/office-v2의 claude/heroine-sprites 브랜치에서 시작해 새 브랜치 codex/intro-cgs-lingerie-v001을 만들어라. 아래 작업을 사람의 대답을 기다리지 말고 끝까지 혼자 진행한다.

Draw 13 intro CGs for an adult office-romance visual novel: the full-scene image shown right before each intimate scene, with the heroine wearing only her underwear.

REFERENCES (open these repository files directly):
- MASTER sprites, the only allowed art style and the face/hair/body reference: CharacterArt/candidates/heroine-masters-v001/ria_office_pose01_neutral_v001.png, jihyun_office_pose01_neutral_v001.png, yujin_office_pose01_neutral_v001.png, seoyun_office_pose01_neutral_v001.png
- Outfits shown as discarded props: Source/game/images/characters/<name>/<name>_casual_pose01_neutral.png, <name>_home_pose01_neutral.png, <name>_office_pose01_neutral.png, and CharacterArt/candidates/special-outfit-v001/<name>_special_pose01_neutral.png
- Underwear taste: CharacterArt/character_art_09_INTIMATE_WEAR.md. If the branch codex/intimate-wear-v001 exists, use its CharacterArt/candidates/intimate-wear-v001/<name>_lingerie_<everyday|special|home>.png as the exact underwear design.

ABSOLUTE STYLE RULE: every image must look like the same artist drew it in the same session as the masters.
- LINE ART: thin, clean, uniform dark-brown outlines (slightly darker at the outer silhouette), no sketchy, painterly or thick lines.
- EYES: large almond eyes with a thick dark upper lash line ending in a small wing, thin lower lash line, iris gradient from dark at the top to lighter at the bottom, one bright white crescent highlight plus small round white highlights.
- FACE: small pointed chin, tiny nose drawn with a faint shadow only, small mouth, soft pink blush on the cheeks.
- SHADING: anime cel shading, one soft shadow tone with gentle gradient edges, small crisp highlights; warm, clean, slightly glossy finish.
- HAIR: defined strand clumps with bright white glossy highlight bands near the crown.
- BODY: tall slim adult proportions, about 8 heads tall, same build as each master (Yujin curvier).
- BACKGROUND: same anime style, clean lines, warm interior lighting.
FORBIDDEN: realistic or semi-realistic rendering, 3D, painterly or watercolor texture, thick outlines, flat vector, chibi, a different anime style, glow or bloom, redesigned faces, childlike proportions. If anything conflicts, the masters win.

PROCESS:
1 STEP 0: write your description of the master style and each heroine's identifying features into CharacterArt/candidates/intro-cgs-lingerie-v001/STYLE_NOTES.md.
2 STYLE TEST: redraw ria_office_pose01_neutral_v001.png as exactly as possible, compare it with the master, and redraw until eyes, lines, shading and proportions match. Save the passing test as _style_test.png.
3 After each scene, compare the heroine with her master, check the underwear against her set, and check the perspective rules. Redraw if anything differs. Count the redraws.
4 Draw each heroine's room in her first scene, then reuse the same room for her later scenes.

CHARACTERS (adults 27–32, mature proportions, never childlike; no earrings/necklaces/rings):
- RIA (28): very long wavy blonde high ponytail, BLUE scrunchie, straight bangs, BLUE eyes. Playful, but drops the jokes at serious moments.
- JIHYUN (30): very long straight crimson hair down the back, side-parted bangs, reddish-brown eyes, sharp eyeliner. Says what she wants directly; weak to compliments.
- YUJIN (27): silver-white bob, one gold hairpin, thin round metal glasses always on, amber eyes, curvy. Shy, then suddenly direct.
- SEOYUN (32): long wavy dark plum hair, half-lidded grey-lavender eyes, beauty mark under LEFT eye. Teasing, but completely serious when sincere.

UNDERWEAR SETS (use exactly these, matching sets):
- RIA everyday: sky-blue cotton full-cup bra with thin white lace trim and a tiny center bow, matching sky-blue hipster briefs with a tiny bow.
- RIA special: white lace balconette bra with small blue satin ribbons, matching white lace briefs with blue ribbons.
- RIA home: navy sporty cotton bra and navy boy shorts with a white stripe band.
- RIA work day: plain black cotton bra and briefs.
- JIHYUN everyday: deep burgundy satin plunge bra with lace only at the edges, perfectly matching high-cut briefs.
- JIHYUN special: black lace balconette bra and matching black lace briefs, elegant and minimal.
- JIHYUN home: ivory silk bra and matching ivory silk shorts-style briefs.
- YUJIN everyday: soft peach cotton full-coverage bra with a tiny embroidered bow, matching peach briefs.
- YUJIN special: her first lace set, sage-green lace full-cup bra over a soft lining and matching sage briefs.
- YUJIN home: heather-grey modal bra and matching grey boy shorts.
- SEOYUN everyday: deep plum lace bra and briefs with lining, plum garter belt, black lace-band thigh-highs.
- SEOYUN special: black satin bra and briefs (no garter that day; she wore leather pants).
- SEOYUN home: lavender silk bra and matching silk briefs.

ONE COHERENT SCENE, NOT A COMPOSITE. 16:9, 1920x1080 PNG, no text/logos/UI.
PERSPECTIVE RULES: single camera at standing eye level (about 1.4 m), 35 mm lens, one consistent horizon and vanishing point for the room and the character. The character's size must match the furniture (mattress top reaches her knee when she stands). Show contact: hips sink into the mattress, feet flat on the floor with soft contact shadows. Nothing floats, nothing clips through the bed. Legs angled sideways, never stretched toward the camera.
THE VIEWER is her boyfriend (the player character): at most his hand and shirt cuff at the frame edge; no face, no body.
CONTENT LIMIT: she wears only her bra and panties (plus thigh-highs where listed); fully covering, opaque, not see-through except lace trim over lining. No nudity, no nipples, no sexual act, no explicit pose. Romantic, a moment before an intimate scene. Her outfit from that day lies folded or dropped nearby as a prop.

ROOMS (draw once, then reuse the same room for that heroine):
- RIA BEDROOM: warm one-room apartment, wooden bed with white duvet and a pink knit throw, bedside table with a fabric lamp and pink flowers, gingham curtains, hanging plants, open sliding door to a small living room with a sofa.
- JIHYUN BEDROOM: tidy minimal bedroom, grey bedding, a low bookshelf, one bedside lamp, dark curtains; through the open door, her living-room tea table.
- YUJIN ROOM: one-room apartment, white desk with a drawing tablet, window-frame sketches pinned on the wall, sheer curtains, bed with white bedding on the right.
- SEOYUN STUDIO BACK ROOM: small bedroom at the back of her private work studio, low bed with beige and lavender bedding, a desk lamp, stacks of copy drafts and books; through the open door, the studio's sofa and worktable. No family photos or family items.

SCENES — file name · character · moment from the script → underwear / discarded outfit / pose / expression / props:
1 01_ria_r07_lingerie_intro.png — RIA · first night, rainy Saturday evening (RIA BEDROOM, rain on the window, warm lamp). She admitted it is her first time too, then laughed. "No umbrella excuse now." Underwear: RIA everyday. Her cream cable-knit sweater and denim mini skirt dropped on the chair. Sitting on the bed edge hugging a cushion half against her stomach, fingers of one hand interlaced with the viewer's hand at the frame edge. Nervous honest smile with lips pressed together, pink cheeks. Two untouched teacups on the bedside table.
2 02_ria_r12_lingerie_intro.png — RIA · Saturday night after the date, a clear night (RIA BEDROOM, string lights, no rain). She almost changed outfits twice; he noticed right away. "I don't have to delete that message anymore." Underwear: RIA special. Her light-blue ribbed knit top, black flared midi skirt and ivory teddy coat (match ria_special_pose01_neutral.png) on the chair, bag on the floor. Standing beside the bed, hands clasped behind her back, leaning forward slightly. Soft glossy eyes, proud but shy smile, deep blush. Phone face-down on the bedside table.
3 03_ria_r15_lingerie_intro.png — RIA · Sunday night after making up (RIA BEDROOM). She came over first as she promised. Underwear: RIA home, hair down, blue scrunchie on her wrist. Her white oversized hoodie and grey dolphin shorts on the floor. Kneeling on the bed, holding the viewer's hand and gently pulling him toward her. No joke: soft serious smile, steady eyes. A chopstick wrapper with a little noodle doodle on the bedside table.
4 04_ria_o04_lingerie_intro.png — RIA · station-front motel, Thursday night after work and one soju (small motel room, pink-blue neon through the blinds, the bed visible behind her). "Can I kiss you?" Underwear: RIA work day, with her sheer black pantyhose still on. Her white blouse and black pencil skirt draped over the chair with her bag and navy lanyard. Back against the door, one arm across her stomach, the other hand reaching for the viewer's collar. Tipsy flush, bold but shy, eyes on the viewer's lips.
5 05_jihyun_r07_lingerie_intro.png — JIHYUN · Saturday evening after the argument (JIHYUN BEDROOM; through the door, the tea table with two cups and the little wooden window-frame model). She asked for a kiss, then fixed his collar: "Then no need to straighten it again." Underwear: JIHYUN everyday. Her burgundy turtleneck and long dark skirt folded neatly on the chair, camel trench on the hook. Standing by the bed, fingertips on the viewer's shirt collar at the frame edge. Direct calm gaze, faint satisfied smile, light blush.
6 06_jihyun_r12_lingerie_intro.png — JIHYUN · Friday night after dinner (JIHYUN BEDROOM). She wore her date outfit for him and got called "pretty". Underwear: JIHYUN special, with sheer black pantyhose. Her cream cable-knit sweater dress folded on the chair, dark brown long coat and white scarf on the hook (match jihyun_special_pose01_neutral.png). Sitting on the bed edge, legs crossed, one hand touching her own wrist where the sleeve used to be, face half turned away. Flustered, red ears, losing her composed team-leader face. Phone face-down on the bedside table.
7 07_jihyun_r15_lingerie_intro.png — JIHYUN · Saturday night, the first night she leans on him (JIHYUN BEDROOM, one lamp, rumpled blanket). Underwear: JIHYUN home. Her taupe knit cardigan and lounge pants on the chair. Lying on her side, head on her bent arm, patting the space beside her. Relieved half-closed eyes, unguarded smile.
8 08_yujin_r07_lingerie_intro.png — YUJIN · Saturday evening, after showing her secret "Changga" drawings (YUJIN ROOM, desk lamp). "Cold hands, right? You thought only you were nervous?" Underwear: YUJIN everyday, glasses on. Her cream cardigan, white blouse and brown pleated skirt folded on the desk chair. Sitting on the bed edge, both her hands wrapped around the viewer's hand. Trembling shy smile, looking up through her glasses, red ears. The window drawing and a photo-booth strip propped on the desk, two untouched cups.
9 09_yujin_r12_lingerie_intro.png — YUJIN · Thursday night after the deadline week (YUJIN ROOM, tablet and coffee cups on the desk). She chose her outfit for a long time; this time she did not look away. Underwear: YUJIN special, glasses on. Her beige V-neck knit, brown glen-check midi skirt and ivory shearling jacket on the chair (match yujin_special_pose01_neutral.png). Standing beside the bed, one hand holding her other elbow, meeting the viewer's eyes. Shy but steady gaze, small brave smile, blush.
10 10_yujin_r15_lingerie_intro.png — YUJIN · evening after making up (YUJIN ROOM, only the desk lamp on, dimmed). "Tonight this lighting is enough." She practiced what to say and forgot it halfway. Underwear: YUJIN home, glasses on. Her oversized white shirt and black leggings folded on the chair. Kneeling on the bed, one hand reaching for the viewer's hand, the other half-raised in a flustered gesture. Mouth open mid-sentence, wide eyes, blushing. A crumpled note on the bed.
11 11_seoyun_r07_lingerie_intro.png — SEOYUN · Saturday evening, she ran back to stop him from leaving (SEOYUN STUDIO BACK ROOM; through the door, two teacups on the studio table). "I'll take that answer without joking. I want it too." Underwear: SEOYUN everyday. Her grey knit maxi dress and beige cardigan on the floor. Standing at the foot of the bed facing the viewer, one hand resting on the bedpost. No teasing: serious, earnest, flushed. An old paperback with a pencilled date on the bedside table.
12 12_seoyun_r12_lingerie_intro.png — SEOYUN · Friday night; she avoided answering his question about going public, but wants to stay with him (SEOYUN STUDIO BACK ROOM). Underwear: SEOYUN special. Her grey hoodie, black leather pants and black long coat on the chair, sunglasses on the bedside table (match seoyun_special_pose01_neutral.png). Sitting on the bed hugging her knees, chin on her knees. Soft, slightly guilty smile, eyes up at the viewer. A glass of water on the bedside table.
13 13_seoyun_r15_lingerie_intro.png — SEOYUN · night after she ended things with her ex; nothing left to hide (SEOYUN STUDIO BACK ROOM, warm lamp). Underwear: SEOYUN home. Her champagne satin pajamas folded at the foot of the bed. Lying back on the pillows, one arm behind her head, knees together and tilted to one side (not toward the camera). The most relaxed open smile.

저장과 마무리:
- CharacterArt/candidates/intro-cgs-lingerie-v001/ 에 위 파일 이름 그대로 저장한다(1920x1080 PNG).
- 같은 폴더에 INDEX.md: 번호, 파일, 장면, 속옷 세트, 참고한 파일, 다시 그린 횟수, 남은 문제(있으면).
- Source/game/ 아래는 건드리지 않는다. 게임 연결과 승인 등록은 하지 않는다(사용자 검수 뒤에 한다).
- 끝나면 커밋하고 브랜치 codex/intro-cgs-lingerie-v001을 올린다. 못 만든 장면이 있으면 그 목록과 이유를 INDEX.md에 남긴다.
```
