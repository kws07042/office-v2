# 히로인 속옷 시트 프롬프트 v001

[속옷·잠옷 취향 설정](../CharacterArt/character_art_09_INTIMATE_WEAR.md)을 그림으로 고정한다. 인물마다 평소·특별한 날·집 세 벌, 모두 12장이다. 도입 CG와 본 장면 CG를 뽑을 때 이 그림을 함께 넣으면 속옷이 장면마다 달라지지 않는다.
- 노출 한도: 속옷이 다 가리고 비치지 않는다. 나체와 노골적 자세는 없다.
- 저장: `CharacterArt/candidates/intimate-wear-v001/<인물>_lingerie_<everyday|special|home>.png`
- 후보 자산이다. 검수와 사용자 승인 전에는 게임에 연결하지 않는다.

## ChatGPT용 (그림 첨부: 마스터 4장)

```text
You will draw 12 full-body character reference sprites for an adult office-romance visual novel: 4 heroines x 3 underwear sets (everyday, special, home). These are design sheets that fix each heroine's underwear taste. ONE image per reply. Before each image, write its file name on one line. After each image, wait for me to say "next".

REFERENCES: I attached the 4 MASTER sprites (*_office_pose01_neutral_v001.png). If missing, use:
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/ria_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/jihyun_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/yujin_office_pose01_neutral_v001.png
https://raw.githubusercontent.com/kws07042/office-v2/main/CharacterArt/candidates/heroine-masters-v001/seoyun_office_pose01_neutral_v001.png

ABSOLUTE STYLE RULE: the MASTER sprites are the only allowed art style; every image must look like the same artist drew it.
- LINE ART: thin, clean, uniform dark-brown outlines, no sketchy, painterly or thick lines.
- EYES: large almond eyes, thick dark upper lash line with a small wing, iris gradient dark-to-light, one white crescent highlight plus small round highlights.
- FACE: small pointed chin, tiny nose shadow, small mouth, soft pink blush.
- SHADING: anime cel shading, one soft shadow tone, small crisp highlights, warm clean finish.
- HAIR: defined strand clumps with white glossy highlight bands.
- BODY: tall slim adult proportions, about 8 heads tall, same body shape and build as each master (Yujin curvier).
FORBIDDEN: realistic or semi-realistic rendering, 3D, painterly texture, thick outlines, a different anime style, redesigned faces, childlike proportions. If anything conflicts, the masters win.
Adult women aged 27–32. No earrings, necklaces or rings.

STEP 0 — text only first: which references you can see, and your description of the master style. Wait for my "ok".

EVERY IMAGE: full body from the top of the head to the feet, standing, centered, vertical 2:3 canvas, barefoot unless stated. TRANSPARENT background, PNG with alpha, clean cutout, no halo, no shadow, nothing else in the image (if transparency fails, use solid pure green #00FF00).
CONTENT LIMIT: underwear fully covers, opaque and not see-through except lace trim edges over fabric lining; no nudity, no nipples, no explicit pose. A tasteful lingerie design sheet that shows each heroine's personality through her choice of underwear, pose and expression.

1 ria_lingerie_everyday.png — KANG RIA (very long wavy blonde high ponytail, blue scrunchie, straight bangs, blue eyes). Cute and comfy: sky-blue cotton full-cup bra with thin white lace trim and a tiny bow at the center, matching sky-blue hipster briefs with a tiny bow, white ankle socks. Pose: playful V sign next to her cheek, weight on one leg. Expression: cheeky grin with pink ears, as if caught and laughing it off.
2 ria_lingerie_special.png — RIA. Her special-day set: white lace balconette bra with small blue satin ribbons, matching white lace briefs with blue ribbons. Pose: hands clasped behind her back, leaning forward slightly. Expression: proud but shy smile, deep blush, "you noticed, right?"
3 ria_lingerie_home.png — RIA, hair down with the blue scrunchie on her wrist. Navy sporty cotton bra and navy boy shorts with a white stripe band. Pose: stretching both arms up overhead. Expression: relaxed sleepy grin.
4 jihyun_lingerie_everyday.png — BAEK JIHYUN (very long straight crimson hair down her back, side-parted bangs, reddish-brown eyes, sharp eyeliner). Neat even where no one sees: deep burgundy satin plunge bra with restrained lace only at the edges, perfectly matching high-cut briefs, no bows or frills. Pose: arms loosely crossed under her chest, upright posture. Expression: composed, almost expressionless, faint blush only at the ears.
5 jihyun_lingerie_special.png — JIHYUN. Black lace balconette bra and matching black lace briefs, elegant and minimal. Pose: one hand on her hip, chin slightly raised. Expression: confident gaze that is just starting to break into embarrassment.
6 jihyun_lingerie_home.png — JIHYUN. Ivory silk bra and matching ivory silk shorts-style briefs. Pose: tucking her hair behind one ear, shoulders relaxed. Expression: gentle unguarded small smile.
7 yujin_lingerie_everyday.png — CHA YUJIN (silver-white bob, one gold hairpin, thin round metal glasses always on, amber eyes, curvy adult figure). Chooses by color and texture: soft peach cotton full-coverage bra with a tiny embroidered bow, matching peach briefs. Pose: both arms hugging herself loosely, knees together. Expression: very shy, looking up through her glasses, red ears.
8 yujin_lingerie_special.png — YUJIN. Her first lace set: sage-green lace full-cup bra over a soft lining and matching sage briefs. Pose: one hand holding her other elbow, then facing forward bravely. Expression: nervous but brave direct gaze, blush.
9 yujin_lingerie_home.png — YUJIN. Heather-grey modal bra and matching grey boy shorts. Pose: holding both hands loosely in front, slight tilt of the head. Expression: soft shy smile.
10 seoyun_lingerie_everyday.png — HAN SEOYUN (long wavy dark plum hair, half-lidded grey-lavender eyes, beauty mark under her LEFT eye). Wears what makes her feel good even if unseen: deep plum lace bra and briefs with lining, plum garter belt, black lace-band thigh-high stockings. Pose: one hand on her hip, other hand touching her lips with one finger. Expression: teasing half-lidded smile, "nowhere to look, right?"
11 seoyun_lingerie_special.png — SEOYUN. Black satin bra and briefs, black garter belt, black lace-band thigh-highs. Pose: weight on one leg, hand brushing her hair back. Expression: the teasing stops, a quiet sincere look.
12 seoyun_lingerie_home.png — SEOYUN. Lavender silk bra and matching silk briefs. Pose: stretching lazily with one arm above her head. Expression: the most relaxed open smile.

Start with STEP 0.
```

## Codex용

```text
저장소 kws07042/office-v2의 claude/heroine-sprites 브랜치에서 시작해 새 브랜치 codex/intimate-wear-v001을 만들어라.

할 일: Docs/lingerie-sheet-prompts-v001.md의 "ChatGPT용" text 블록을 그대로 따라 12장을 만든다. 속옷 취향은 CharacterArt/character_art_09_INTIMATE_WEAR.md를 따른다.
- "ok", "next"를 기다리지 말고 끝까지 혼자 진행한다.
- 참고 그림은 저장소 파일을 직접 연다: CharacterArt/candidates/heroine-masters-v001/*_office_pose01_neutral_v001.png
- STEP 0 그림체 설명은 STYLE_NOTES.md로 적고, 매 장 마스터와 비교해 다르면 다시 그린다.
- 저장: CharacterArt/candidates/intimate-wear-v001/<블록에 적힌 파일 이름>, 투명 PNG 세로 2:3 전신. 같은 폴더에 INDEX.md(파일, 인물, 세트, 다시 그린 횟수, 남은 문제).
- 노출 한도를 지킨다. Source/game/ 아래는 건드리지 않는다. 게임 연결과 승인 등록은 하지 않는다.
- 끝나면 커밋하고 브랜치를 올린다.
```
