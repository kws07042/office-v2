# Grok 이미지 프롬프트 v001 · 도입 CG 다시 그리기

`Docs/intimate-intro-cg-redo-v001.md`에서 다시 그리기로 한 도입 CG 15장을 Grok 이미지 생성(Grok Imagine)용으로 옮겼다.
- 옷이 물리적으로 말이 안 되는 장면: 05, 08, 11, 19
- 노출을 조금 더 하는 코스프레: 14~25
- 수위 기준: 성인, 속옷·가터·맨어깨·허벅지까지. 나체·성행위는 없다.

## 설정법

1. **어디서:** grok.com이나 Grok 앱에서 새 대화를 연다. 이미지 생성은 대화창에서 바로 하거나 Imagine 메뉴를 쓴다. 메뉴 이름과 위치는 바뀔 수 있다.
2. **참고 그림 두 장을 먼저 올린다.** 가장 중요한 단계다.
   - ① 지금 게임에 들어간 그 장면 그림: `Source/game/images/events/<히로인>/<파일>.png`. 방, 구도, 조명을 유지하는 기준이다.
   - ② 그 히로인의 마스터 입상: `CharacterArt/candidates/heroine-masters-v001/<이름>_office_pose01_neutral_v001.png`. 얼굴과 그림체의 기준이다.
   - 깃허브 웹에서 파일을 열고 Download로 받으면 된다.
3. **'새로 그려 줘'가 아니라 '이 그림을 고쳐 줘'로 시킨다.** 처음부터 새로 그리게 하면 그림체가 무너진다. 아래 프롬프트는 모두 고치는 방식으로 썼다.
4. **비율은 16:9 가로로 고른다.** 비율 선택이 없으면 프롬프트 첫 줄의 `16:9 landscape`가 대신한다.
5. 여러 장이 나오면 얼굴이 마스터와 가장 닮은 것을 고른다. 손이나 옷이 어색하면 그 그림을 다시 올리고 "fix only the hands"처럼 한 가지만 고치게 한다.
6. **받은 그림은 원래 파일 이름 그대로 저장해서 Claude에게 주면 된다.** 게임 연결은 Claude가 한다.
7. **Grok이 거절하거나 너무 벗기면:** 프롬프트 끝의 CONTENT 줄을 그대로 두고 다시 시도한다. 그래도 안 되면 그 장면은 ChatGPT나 Codex용 프롬프트(`intimate-intro-cg-redo-v001.md`)로 돌린다.

## 공통 문구 (매 프롬프트 맨 앞에 붙어 있음)

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
```

## 05 · 지현 R07

- 참고 그림 ①: `Source/game/images/events/jihyun/r07_casual_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/jihyun_office_pose01_neutral_v001.png`
- 저장할 이름: `jihyun_r07_casual_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: Her long dark skirt has a short side zipper from the waistband to the hip, half open, the skirt still fully covering both legs to mid-calf. Deep burgundy satin bra with lace only at the edges. Her fingertips rest on the viewer's shirt collar: draw the viewer's collar and shoulder edge at the right frame edge so her hand touches it.
```

## 08 · 유진 R07

- 참고 그림 ①: `Source/game/images/events/yujin/r07_casual_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/yujin_office_pose01_neutral_v001.png`
- 저장할 이름: `yujin_r07_casual_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: Her white blouse is unbuttoned and open in front, opaque cotton, so the pale peach cotton bra is seen in the opening, not through the fabric. Cream cardigan at her elbows.
```

## 11 · 서윤 R07

- 참고 그림 ①: `Source/game/images/events/seoyun/r07_casual_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/seoyun_office_pose01_neutral_v001.png`
- 저장할 이름: `seoyun_r07_casual_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: Her grey knit maxi dress is pulled down to her waist: the empty upper half and both sleeves hang and gather around her hips, the skirt part continues to her ankles with no slit. Dusty plum lace bra. One hand holds the gathered knit at her hip.
```

## 14 · 리아 바니걸

- 참고 그림 ①: `Source/game/images/events/ria/r15_cosplay_bunny_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/ria_office_pose01_neutral_v001.png`
- 저장할 이름: `ria_r15_cosplay_bunny_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: blue satin strapless bunny leotard with a lower sweetheart neckline and high-cut legs, white ears, collar with bow tie, cuffs, sheer black pantyhose. Keep the same playful doorway pose.
```

## 15 · 리아 간호사

- 참고 그림 ①: `Source/game/images/events/ria/r15_cosplay_nurse_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/ria_office_pose01_neutral_v001.png`
- 저장할 이름: `ria_r15_cosplay_nurse_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: white-and-pink nurse mini dress unbuttoned to the middle of her chest showing a sky-blue lace bra edge, hem well above mid-thigh, white thigh-highs with lace tops. Keep the keep the same pose with the stethoscope.
```

## 16 · 리아 치어리더

- 참고 그림 ①: `Source/game/images/events/ria/r15_cosplay_cheer_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/ria_office_pose01_neutral_v001.png`
- 저장할 이름: `ria_r15_cosplay_cheer_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: blue-and-white cheer crop top cut short under the bust, low-rise pleated micro skirt, bare midriff, sheer pantyhose. Keep the keep the same pose.
```

## 17 · 지현 바니걸

- 참고 그림 ①: `Source/game/images/events/jihyun/r15_cosplay_bunny_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/jihyun_office_pose01_neutral_v001.png`
- 저장할 이름: `jihyun_r15_cosplay_bunny_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: black satin bunny leotard with crimson trim, deeper plunging neckline, high-cut legs, fishnet pantyhose, cuffs and bow tie. Keep the keep the same pose.
```

## 18 · 지현 간호사

- 참고 그림 ①: `Source/game/images/events/jihyun/r15_cosplay_nurse_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/jihyun_office_pose01_neutral_v001.png`
- 저장할 이름: `jihyun_r15_cosplay_nurse_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: fitted white nurse dress with the top three buttons open showing a black lace bra edge, short hem, white garter stockings. Keep the keep the same pose with the clipboard.
```

## 19 · 지현 차이나드레스

- 참고 그림 ①: `Source/game/images/events/jihyun/r15_cosplay_qipao_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/jihyun_office_pose01_neutral_v001.png`
- 저장할 이름: `jihyun_r15_cosplay_qipao_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: deep crimson silk cheongsam with gold embroidery, sleeveless, a keyhole opening at the chest, and HIGH SLITS ON BOTH SIDES up to the hip. She sits on the bed edge with one leg crossed over the other: the front panel falls between her legs and drapes over the bed edge; her crossed leg comes out through the side slit; the back panel stays under her on the bed. Black pantyhose, heels. Face turned aside, shy blush.
```

## 20 · 유진 바니걸

- 참고 그림 ①: `Source/game/images/events/yujin/r15_cosplay_bunny_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/yujin_office_pose01_neutral_v001.png`
- 저장할 이름: `yujin_r15_cosplay_bunny_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: cream-white satin bunny leotard with gold trim, sweetheart neckline, high-cut legs, white ears, sheer pantyhose, glasses on. Keep the same shy pose.
```

## 21 · 유진 간호사

- 참고 그림 ①: `Source/game/images/events/yujin/r15_cosplay_nurse_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/yujin_office_pose01_neutral_v001.png`
- 저장할 이름: `yujin_r15_cosplay_nurse_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: pastel pink nurse mini dress, front buttons open to show a peach bra edge, short hem, white thigh-highs, glasses on. Keep the keep the same pose hugging the clipboard.
```

## 22 · 유진 메이드

- 참고 그림 ①: `Source/game/images/events/yujin/r15_cosplay_maid_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/yujin_office_pose01_neutral_v001.png`
- 저장할 이름: `yujin_r15_cosplay_maid_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: black-and-white maid dress with an off-shoulder neckline and cleavage window, short flared skirt with petticoat, frilled apron, black thigh-highs with garter straps, glasses on. Keep the same curtsy.
```

## 23 · 서윤 바니걸

- 참고 그림 ①: `Source/game/images/events/seoyun/r15_cosplay_bunny_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/seoyun_office_pose01_neutral_v001.png`
- 저장할 이름: `seoyun_r15_cosplay_bunny_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: deep purple satin bunny leotard, plunging neckline, high-cut legs, garter belt with black lace thigh-highs, cuffs and bow tie. Keep the keep the same pose against the bedpost.
```

## 24 · 서윤 간호사

- 참고 그림 ①: `Source/game/images/events/seoyun/r15_cosplay_nurse_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/seoyun_office_pose01_neutral_v001.png`
- 저장할 이름: `seoyun_r15_cosplay_nurse_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: white nurse dress with lavender trim unbuttoned to the waist over a plum lace bra, short hem, garter belt and black lace thigh-highs. Keep the keep the same pose patting the bed.
```

## 25 · 서윤 여경찰

- 참고 그림 ①: `Source/game/images/events/seoyun/r15_cosplay_police_intro.png`
- 참고 그림 ②: `CharacterArt/candidates/heroine-masters-v001/seoyun_office_pose01_neutral_v001.png`
- 저장할 이름: `seoyun_r15_cosplay_police_intro.png`

```text
Edit the FIRST attached image. 16:9 landscape. Keep its exact art style, room, furniture, lighting, camera angle and the character's pose unless told otherwise. Keep her face, hair and eye color identical to the SECOND attached image (the master sprite). Clean Korean visual-novel anime style, soft cel shading, same line weight as the originals. No text, no watermark.
CLOTHING PHYSICS: every garment must be wearable in real life; openings only where real garments have them; fabric is opaque; removed clothes are props on the chair or floor.
CONTENT: adult woman. Cleavage, bare shoulders, thighs, garters and visible underwear are fine. No nudity, no nipples, no genitals, no sexual act.
CHANGE ONLY THE OUTFIT: navy police-style jacket worn open over a black lace bra, no shirt, navy mini skirt, garter belt and black lace thigh-highs, peaked cap, toy handcuffs on one finger. Keep the keep the same pose.
```
