# 도입 CG 다시 그리기 v001 (codex/intro-cgs-v002 검수 결과)

## 검수 (2026-11-23)
| 번호 | 문제 | 판정 |
|---|---|---|
| 19 지현 치파오 | 옆트임이 한쪽인데 꼰 두 다리가 모두 앞으로 다 나와 있음. 통으로 된 원피스라 불가능 | 다시 |
| 11 서윤 R07 | '허리까지 내린 니트 원피스'가 트임 있는 랩스커트로 그려짐. 상체·소매 부분이 사라짐 | 다시 |
| 05 지현 R07 | 지퍼가 엉덩이부터 밑단까지 이어짐(치마 지퍼는 엉덩이까지). 보이지 않는 옷깃을 잡으려 허공에 손을 뻗음 | 다시 |
| 08 유진 R07 | 흰 블라우스 너머로 브래지어가 비침 | 다시 |
| 04 리아 모텔 | 옷깃 대신 문손잡이 쪽으로 손을 뻗음 | 그대로 둬도 됨 |
| 14~25 코스프레 | 사용자 요청: 노출을 조금 더(나체 없이) | 다시 |
그 밖의 장면은 그림체·얼굴·소품·원근이 통과.

## Codex 지시
```text
저장소 kws07042/office-v2의 codex/intro-cgs-v002 브랜치에서 시작해 새 브랜치 codex/intro-cgs-v003을 만들어라. 사람의 대답을 기다리지 말고 끝까지 혼자 진행한다.

Redraw 16 intro CGs from CharacterArt/candidates/intro-cgs-v002/: scenes 05, 08, 11, 19 (physically impossible clothing) and the costume scenes 14–25 (a bit more revealing). Keep everything else from the v002 images: art style, faces, rooms, props, lighting, camera. Use the same file names, saved in CharacterArt/candidates/intro-cgs-v003/.

REFERENCES (repository files): the v002 image of the same scene (layout, room, props), the MASTER sprites CharacterArt/candidates/heroine-masters-v001/<name>_office_pose01_neutral_v001.png (art style and face, highest priority), CharacterArt/character_art_09_INTIMATE_WEAR.md (underwear), CharacterArt/candidates/intimate-wear-v001/ (underwear designs, if present). Keep the ABSOLUTE STYLE RULE of Docs/intimate-intro-cg-prompts-v003.md.

CLOTHING PHYSICS (new rule for every image):
- Every garment must be wearable in real life: seams, slits, zippers and openings only where a real garment has them.
- A one-piece dress is a closed tube: a leg can only come out through a slit, and the fabric stays continuous around the other side.
- Skirt zippers run from the waistband to the hip only.
- A garment pulled down or off bunches realistically: sleeves and the upper part hang or gather at the waist or arms; it never turns into a different garment.
- Removed garments become props on the chair or floor.
- Fabric is opaque. Nothing shows through a blouse or shirt.
- If her hand touches the viewer, draw the viewer's hand or shirt cuff at the frame edge so she is not reaching into empty air.
After each image, check these rules and redraw if any fails.

CONTENT LIMIT: adult women 27–32. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act, no explicit pose.

REDO — physics fixes:
05 05_jihyun_r07_casual_intro.png — same scene as v002. Her long dark skirt has a short side zipper from the waistband to the hip, half open, the skirt still fully covering both legs to mid-calf. Deep burgundy satin bra with lace only at the edges. Her fingertips rest on the viewer's shirt collar: draw the viewer's collar and shoulder edge at the right frame edge so her hand touches it.
08 08_yujin_r07_casual_intro.png — same scene as v002. Her white blouse is unbuttoned and open in front, opaque cotton, so the pale peach cotton bra is seen in the opening, not through the fabric. Cream cardigan at her elbows.
11 11_seoyun_r07_casual_intro.png — same scene as v002. Her grey knit maxi dress is pulled down to her waist: the empty upper half and both sleeves hang and gather around her hips, the skirt part continues to her ankles with no slit. Dusty plum lace bra. One hand holds the gathered knit at her hip.
19 19_jihyun_r15_qipao_intro.png — see costume 19 below.

COSTUMES (R15, more revealing; same room, pose and expression as v002 unless noted):
14 RIA bunny — blue satin strapless bunny leotard with a lower sweetheart neckline and high-cut legs, white ears, collar with bow tie, cuffs, sheer black pantyhose. Same playful doorway pose.
15 RIA nurse — white-and-pink nurse mini dress unbuttoned to the middle of her chest showing a sky-blue lace bra edge, hem well above mid-thigh, white thigh-highs with lace tops. Same pose with the stethoscope.
16 RIA cheer — blue-and-white cheer crop top cut short under the bust, low-rise pleated micro skirt, bare midriff, sheer pantyhose. Same pose.
17 JIHYUN bunny — black satin bunny leotard with crimson trim, deeper plunging neckline, high-cut legs, fishnet pantyhose, cuffs and bow tie. Same pose.
18 JIHYUN nurse — fitted white nurse dress with the top three buttons open showing a black lace bra edge, short hem, white garter stockings. Same pose with the clipboard.
19 JIHYUN china dress — deep crimson silk cheongsam with gold embroidery, sleeveless, a keyhole opening at the chest, and HIGH SLITS ON BOTH SIDES up to the hip. She sits on the bed edge with one leg crossed over the other: the front panel falls between her legs and drapes over the bed edge; her crossed leg comes out through the side slit; the back panel stays under her on the bed. Black pantyhose, heels. Face turned aside, shy blush.
20 YUJIN bunny — cream-white satin bunny leotard with gold trim, sweetheart neckline, high-cut legs, white ears, sheer pantyhose, glasses on. Same shy pose.
21 YUJIN nurse — pastel pink nurse mini dress, front buttons open to show a peach bra edge, short hem, white thigh-highs, glasses on. Same pose hugging the clipboard.
22 YUJIN maid — black-and-white maid dress with an off-shoulder neckline and cleavage window, short flared skirt with petticoat, frilled apron, black thigh-highs with garter straps, glasses on. Same curtsy.
23 SEOYUN bunny — deep purple satin bunny leotard, plunging neckline, high-cut legs, garter belt with black lace thigh-highs, cuffs and bow tie. Same pose against the bedpost.
24 SEOYUN nurse — white nurse dress with lavender trim unbuttoned to the waist over a plum lace bra, short hem, garter belt and black lace thigh-highs. Same pose patting the bed.
25 SEOYUN police — navy police-style jacket worn open over a black lace bra, no shirt, navy mini skirt, garter belt and black lace thigh-highs, peaked cap, toy handcuffs on one finger. Same pose.

저장과 마무리:
- CharacterArt/candidates/intro-cgs-v003/ 에 같은 파일 이름으로 저장(1920x1080 PNG). 다시 그리지 않은 장면은 넣지 않는다.
- INDEX.md: 번호, 파일, 고친 점, 옷 물리 규칙 확인 결과, 다시 그린 횟수, 남은 문제.
- Source/game/ 아래는 건드리지 않는다. 게임 연결·승인 등록은 하지 않는다.
- 끝나면 커밋하고 브랜치 codex/intro-cgs-v003을 올린다.
```
