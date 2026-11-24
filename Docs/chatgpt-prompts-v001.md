# 챗지피티 프롬프트 모음 v001 (글쓰기·로고)

쓰는 법: 각 코드 블록을 그대로 붙인다. 결과는 Claude에게 가져오면 맞는 것만 골라 게임에 넣는다.
'도현'이라는 이름은 바꾸지 않는다. 게임이 화면에 띄울 때 플레이어 이름으로 바꾼다.

---

## 1. 대사 검수 (대본 .rpy 파일 하나를 통째로 붙인 뒤)

```text
너는 한국어 연애 비주얼노벨 대본 교정자다. 아래는 Ren'Py 대본이다. 성인 남녀(27~32세)의 회사 연애물이고, 히로인 말투 기준은 다음과 같다.
- 리아(28, 현장 마케팅): 밝고 빠른 말끝, 장난, 물결(~)·느낌표. 반말/존댓말 두 벌이 ri('반말','존댓말')로 들어 있다.
- 지현(30, 팀장): 짧고 결론부터. 칭찬에 약해 말을 잃는다.
- 유진(27, 디자이너, 안경): 존댓말, 말끝을 흐리다 직구. 색·빛 비유.
- 서윤(32, 외주 실장): 여유로운 반말로 떠보다가 진심일 땐 장난을 멈춘다.
- 도현: 주인공. 다정하고 차분한 존댓말.

해야 할 일: 고칠 곳만 찾아서 표로 정리해라. 대본 전체를 다시 쓰지 마라.
찾을 것:
1) 인물 말투에 안 맞는 줄
2) 사람이 실제로 안 쓰는 딱딱한 문어체
3) 같은 장면 안에서 같은 표현 반복
4) 앞뒤 사실이 안 맞는 곳(시간, 장소, 옷, 호칭)
5) 맞춤법·띄어쓰기
6) AI가 쓴 티가 나는 문장(아래 3번 목록 참고)

표 형식: | 줄 내용(앞 20자) | 문제 | 고친 문장 |
'도현'이라는 이름은 바꾸지 마라. 코드(label, $, call, menu 등)는 건드리지 마라.
```

---

## 2. 스토어 페이지 문구

```text
한국어 성인 연애 비주얼노벨 〈퇴근 후, 우리〉의 스토어 페이지 문구를 써 줘.
설정: 브랜딩 회사 GY브랜딩 기획팀에 들어온 주인공(이름은 플레이어가 사원증에 직접 씀). 연말 피칭 TF에서 만난 네 명.
- 강리아(28): 현장 마케팅. 밝고 장난스럽지만 몰래 이직을 고민 중.
- 백지현(30): TF 팀장. 일에선 완벽주의, 칭찬엔 약함. 미니어처 집을 조립하는 취미.
- 차유진(27): 디자이너. 수줍지만 비밀 그림 계정 '창가'를 가진 직구파.
- 한서윤(32): 외주 카피 실장. 여유롭게 떠보는 연상, 이혼한 과거가 있음.
특징: 회사 PC 메신저와 휴대폰 문자로 이어지는 연애, 히로인별 데이트와 갈등과 화해, 네 개의 루트와 진엔딩, 18세 이상 성인 장면.
써 줄 것:
1) 한 줄 소개(40자 이내) 3안
2) 짧은 설명(300자) 1안
3) 긴 설명(문단 4개, 히로인 소개 포함) 1안
4) 특징 bullet 6개
5) 태그 15개
과장된 광고 말투나 '최고의', '역대급' 같은 말은 빼고, 담백하고 설레는 톤으로. 아래 3번의 'AI 티 나는 표현'도 쓰지 마.
```

---

## 3. AI 티 안 나는 대본 쓰기 (새 장면을 쓸 때)

'[장면 설명]' 자리에 쓰고 싶은 장면을 적는다. 예: "리아 R09 · 비 오는 퇴근길, 우산 하나로 역까지 걷는다".

```text
너는 한국 연애 비주얼노벨 작가다. 〈퇴근 후, 우리〉의 장면 하나를 Ren'Py 대본 형식으로 써라.

[장면 설명]

인물과 말투:
- 도현(d): 주인공, 28, 기획팀. 다정하고 차분한 존댓말. 속마음은 dn "..." 으로, 짧고 솔직하게.
- 리아(r): 28, 현장 마케팅. 밝고 빠른 말끝, 장난. 대사는 r "[ri('반말','존댓말')]" 처럼 반말·존댓말 두 벌.
- 지현(j): 30, 팀장. 짧고 결론부터. 칭찬엔 말을 잃는다.
- 유진(y): 27, 디자이너, 안경. 존댓말, 말끝을 흐리다 직구. 색·빛 이야기.
- 서윤(s): 32, 외주 실장. 여유로운 반말로 떠보다 진심일 땐 장난을 멈춘다.
- 지문은 따옴표만 쓴 줄 "..." 로, 1~2문장.

반드시 지킬 것(사람이 쓴 것처럼):
1. 대사는 실제 사람이 말하는 길이와 리듬으로. 한 줄에 한 가지 말만. 말을 끊고, 되묻고, 딴소리하고, 대답을 피하기도 한다.
2. 감정을 이름으로 말하지 마라. '설렜다', '마음이 따뜻해졌다', '가슴이 두근거렸다' 대신 손, 물건, 행동, 침묵으로 보여 줘라.
3. 구체적인 사물 하나를 장면 내내 붙잡아라. 예: 젖은 우산 손잡이, 식은 커피 뚜껑, 사원증 줄.
4. 결론을 대사로 정리하지 마라. 장면은 작은 행동이나 애매한 한마디로 끝내라.
5. 인물끼리 서로를 설명해 주는 대사 금지("너는 늘 그렇게 배려하잖아" 같은 것).
6. 같은 단어나 어미를 세 줄 안에 반복하지 마라.

쓰지 말 것(AI 티 나는 표현):
'~하는 것 같아', '왠지 모르게', '문득', '살며시', '조심스럽게', '어느새', '그 순간', '마치 ~처럼'(한 장면에 한 번 넘으면 안 됨), '진심으로', '소중한', '특별한', '고마워, 정말로', '우리 앞으로도', '함께라서', '미소를 지었다'(한 장면에 한 번까지), 줄표(—)로 문장 잇기, 세 개씩 나열하는 문장.

분량: 대사와 지문 합쳐 30~45줄. 선택지가 필요하면 menu: 로 두세 개, 각 선택지는 짧은 말로.
성적인 장면은 쓰지 마라(키스나 손잡기까지).
```

---

## 4. 일상 장면 아이디어 40개

```text
〈퇴근 후, 우리〉 설정(브랜딩 회사 GY브랜딩, 연말 피칭 TF, 히로인 리아·지현·유진·서윤)으로, 히로인마다 '사귀기 전'과 '사귄 뒤'에 넣을 짧은 일상 장면 아이디어를 각 5개씩 줘(총 40개).
조건:
- 회사 안팎의 현실적인 상황(야근, 회식, 비 오는 퇴근길, 점심, 출장 등)
- 장면마다 한 줄 상황 + 그 히로인만 할 법한 대사 한 줄 + 끝에 남는 작은 소품이나 감정
- 성적인 내용은 빼고 설렘 위주
- 같은 상황을 두 히로인에게 반복하지 말 것
- 3번의 'AI 티 나는 표현' 금지
표 형식: | 히로인 | 시점 | 상황 | 대표 대사 | 남는 것 |
```

---

## 5. 타이틀 로고 (챗지피티 이미지 생성)

이미지 생성이지만 한글 글자는 챗지피티가 가장 잘 쓴다. 먼저 A안을 뽑아 보고, 마음에 안 들면 B안을 뽑는다. 결과는 투명 PNG로 받는다.

**A안 · 손글씨 리본형**
```text
Create a game title logo for a Korean romance visual novel.
Title text exactly: "퇴근 후, 우리"  (Korean, keep every character, the comma, and the spacing exactly)
Small subtitle under it: "AFTER WORK, US"
Style: elegant, warm and a little playful. Rounded handwritten-style Korean lettering with smooth brush-pen strokes, deep wine red (#B3123F) letters with a thin dark plum (#2B0F1E) outline and a soft cream (#FFF6EE) inner highlight. A thin silk ribbon line loops from the last letter and ends in a tiny heart. Subtitle in small spaced serif capitals in dark plum.
Composition: horizontal logo, centered, wide aspect around 3:1, generous padding.
Background: fully TRANSPARENT (PNG with alpha). No background color, no frame, no characters, no extra words, no watermark.
Clean vector-like edges so it stays sharp when scaled down to 600 px wide on a dark or light screen.
```

**B안 · 사무실 소품형**
```text
Create a game title logo for a Korean office romance visual novel.
Title text exactly: "퇴근 후, 우리"  (Korean, exact characters, comma and spacing)
Small subtitle: "AFTER WORK, US"
Style: modern and clean. Bold rounded Korean sans lettering in deep wine red (#B3123F) with a cream (#FFF6EE) offset shadow. A small employee ID card with a navy lanyard hangs from the "ㅌ" of 퇴, tilted slightly; a tiny chat bubble with a heart floats near "우리". Subtitle in small spaced sans capitals, dark plum (#2B0F1E).
Composition: horizontal logo, centered, around 3:1, generous padding.
Background: fully TRANSPARENT (PNG with alpha). No background, no characters, no extra text, no watermark. Sharp clean edges, readable at 600 px wide on both dark and light backgrounds.
```

받은 로고는 Claude가 타이틀 화면(바탕화면 타이틀과 실크 타이틀)에 크기와 위치를 맞춰 넣는다.
