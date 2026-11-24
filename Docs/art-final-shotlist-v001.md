# 마지막 그림 목록 v001 — 성인 이벤트 제외 (2026-11-20)

이 문서 하나로 남은 그림을 전부 뽑는다. 성인 이벤트 CG는 뺐다.
장면 CG의 지문·장소·의상은 2026-11-20 대본에서 다시 뽑았다. 기존 `art-prompts-chatgpt-v002.md`의 A-5·B 목록을 대신한다.

## 0. 한눈에 보기

| 묶음 | 장수 | 도구 | 우선 |
|---|---:|---|:-:|
| 1. 입상 — 지현·유진 사복·생활복 두 번째 포즈 | 24 | ChatGPT | 1 |
| 2. 입상 — 울먹이는 표정 | 8 | ChatGPT | 1 |
| 3-1. 장면 CG P1 (프롤로그·고백·피칭·크리스마스·핵심 데이트) | 22 | ChatGPT | 1 |
| 3-2. 장면 CG P2 (1월·크리스마스 아침·특별 장면·이듬해 봄) | 18 | ChatGPT | 2 |
| 3-3. 장면 CG P3 (나머지 데이트·일상) | 21 | ChatGPT | 3 |
| 4. 타이틀 키 비주얼 | 1 | ChatGPT → ComfyUI | 1 |
| **ChatGPT 합계** | **94** | | |
| 5-1. 서윤 사복 v004 (그림체 통일) | 9 | ComfyUI | 1 |
| 5-2. 배경 23장 그림체 통일 | 23 | ComfyUI | 1 |
| 5-3. 배경 시간대 변환 (저녁·밤·겨울·크리스마스) | 31 | ComfyUI | 2 |
| 5-4. 위 ChatGPT 결과 전부 그림체 통일 | 94 | ComfyUI | 1 |

**뽑지 않는 것**
- 겨울옷 추가 표정: 히로인당 대사 8~18줄뿐이라 지금 3표정이면 된다.
- 오피스 밖 크게 웃음·삐짐: 거의 안 나온다.
- 서윤 생활복 추가: 대사 6줄.
- 새 배경: 266개 장소 문구가 23곳으로 다 묶인다. 화방은 한 줄이라 거리 배경을 쓴다.
- 주인공: 얼굴·전신 없이 손과 팔만 나온다.

**최소로 끝내려면** 우선 1(입상 32 + CG 22 + 타이틀 1 = 55장)만 해도 출시할 수 있다.

## 1. 쓰는 법

1. 새 대화를 연다. 같은 히로인은 한 대화 안에서 계속 만든다.
2. 첨부 두 장
   - 화풍 기준: `CharacterArt/candidates/heroine-masters-v001/final_2048x3072/ria_office_pose01_neutral_v001.png`
   - 인물·의상 기준: 각 블록에 적힌 입상(`Source/game/images/characters/<인물>/`).
     리아·서윤의 사복·생활복 `pose02`는 아직 게임 폴더에 없으니 `CharacterArt/candidates/chatgpt-v001/`의 최신 버전을 쓴다.
3. [화풍 고정 문단]을 먼저 붙이고, 그다음 블록을 붙인다.
4. 파일 이름대로 저장해서 아래 폴더에 넣는다.
   - 입상: `CharacterArt/candidates/chatgpt-v002/`
   - 장면 CG·타이틀: `CharacterArt/candidates/cg-chatgpt-v001/`
5. 손가락 수, 머리색·눈색, 안경(유진), 눈 밑 점(서윤)을 확인한다. 틀리면 다시 뽑는다.

### [화풍 고정 문단] — 모든 프롬프트 맨 앞

```
STYLE LOCK — this is the most important rule.
Copy the art style of the attached reference images EXACTLY, as if drawn by the same artist in the same session:
- same line art: thin, clean, uniform dark-brown/black outlines, no sketchy or painterly lines
- same eye rendering: same eye shape, iris gradient, highlight shapes and positions, eyelash style
- same coloring: flat cel shading with one soft shadow tone and small crisp highlights; same saturation and warmth
- same face proportions and nose/mouth drawing; same hair strand rendering and hair highlights
Do NOT reinterpret, stylize, beautify, modernize, add your own style, add gradients, glow, painterly texture, 3D, semi-realism or photo textures.
If anything conflicts, the reference images win.
```

### [누끼 문단] — 입상 프롬프트 맨 끝

```
CUTOUT: TRANSPARENT background, PNG with alpha. Crisp clean outline with no white halo, no fringe, no drop shadow, no ground shadow, no floor line. Nothing else in the image.
```
투명이 안 나오면 `solid pure green #00FF00 background, no shadows`로 바꿔 뽑는다. 초록은 Claude가 지운다.

## 2. 입상

### 2-1. 두 번째 포즈 — 지현·유진 사복·생활복 (24장)

리아·서윤은 사복·생활복 포즈가 둘인데, 지현·유진은 하나뿐이라 데이트 내내 같은 자세로 서 있다.

**1단계: 포즈 전신 (4장).** 해당 `pose01_neutral` 입상을 첨부한다.
```
Attached is the official game sprite of this character. Redraw THIS SAME CHARACTER in the SAME outfit, same face, same hair, same proportions and same canvas size and scale, but in a NEW standing pose: {POSE}.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas, head at the same height as the attached sprite. Neutral expression. Natural hands with five fingers.
```

| 파일 | 첨부 | `{POSE}` |
|---|---|---|
| `jihyun_casual_pose02_neutral_v001.png` | `jihyun_casual_pose01_neutral.png` | holding the strap of her shoulder bag with both hands in front of her, head tilted slightly |
| `jihyun_home_pose02_neutral_v001.png` | `jihyun_home_pose01_neutral.png` | holding a warm mug with both hands at chest height, shoulders relaxed |
| `yujin_casual_pose02_neutral_v001.png` | `yujin_casual_pose01_neutral.png` | holding a small sketchbook to her chest with both arms, body turned slightly to the side |
| `yujin_home_pose02_neutral_v001.png` | `yujin_home_pose01_neutral.png` | hugging a soft cushion in front of her, one foot slightly behind the other |

**2단계: 표정 5장씩 (20장).** 같은 대화에서 방금 만든 전신을 첨부한다.
```
Use the attached image as the exact base. Change ONLY the facial expression to: {EXPRESSION}.
Keep everything else pixel-identical: pose, body, outfit, hair, head position and size, line art, colors, canvas size and position.
```
그 뒤에 [누끼 문단].

| 표정 | `{EXPRESSION}` |
|---|---|
| smile | a gentle warm smile, mouth slightly curved, eyes soft |
| blush | a shy smile with clear pink blush across both cheeks, eyes glancing slightly aside |
| serious | a serious focused look, eyebrows slightly lowered, mouth in a straight line |
| sad | a sad look, inner eyebrows raised, eyes lowered, small downturned mouth |
| surprise | surprised, eyes wide open, eyebrows raised, small open mouth |

파일 이름 예: `jihyun_casual_pose02_smile_v001.png`.

### 2-2. 울먹이는 표정 (8장)

R13 갈등, 이별 대화, 고백 직전처럼 꼭 필요한 순간에 대본에서 직접 지정해서 쓴다.
2-1의 2단계 블록을 쓰고, `{EXPRESSION}`에 아래 문장을 넣는다.
```
teary-eyed, eyes glistening with tears that have not fallen yet, inner eyebrows raised, lips pressed together as if holding back crying, faint pink on the nose and cheeks
```

| 파일 | 첨부 |
|---|---|
| `ria_casual_pose02_teary_v001.png` | `ria_casual_pose02_neutral` |
| `jihyun_casual_pose01_teary_v001.png` | `jihyun_casual_pose01_neutral.png` |
| `yujin_casual_pose01_teary_v001.png` | `yujin_casual_pose01_neutral.png` |
| `seoyun_casual_pose02_teary_v003.png` | `seoyun_casual_pose02_neutral_v003.png` (v004 통일 때 같이 처리) |
| `ria_office_pose01_teary_v001.png` | `ria_office_pose01_neutral.png` |
| `jihyun_office_pose01_teary_v001.png` | `jihyun_office_pose01_neutral.png` |
| `yujin_office_pose01_teary_v001.png` | `yujin_office_pose01_neutral.png` |
| `seoyun_office_pose01_teary_v001.png` | `seoyun_office_pose01_neutral.png` |

## 3. 장면 CG

### [CG 블록] — 화풍 고정 문단 뒤에 붙인다

```
Visual novel event CG drawn in EXACTLY the art style of the attached references (same line art, eyes, cel shading and palette). 16:9 landscape, 1920x1080, full illustration with background (NOT transparent).
Character: {HEROINE}, exactly as in the attached sprite: same face, hair color, eye color, outfit ({OUTFIT}).
The male lead is the camera (first-person view). Never draw his face or full body. Only his hands or forearm may appear when the action needs it: {SLEEVE}.
Scene: {ACTION}
Place and time: {PLACE}.
Adults only. Natural hands with five fingers. No text, no logos, no watermark, no speech bubbles.
```
- `{SLEEVE}`: 업무복 장면 `dark navy suit sleeve, white shirt cuff`, 그 밖은 `plain gray knit sleeve`.
- `{ACTION}`·`{PLACE}`는 아래 표의 문장을 그대로 넣는다. 한국어 그대로 넣어도 된다.
- 첨부: 화풍 기준(리아 마스터) + 표의 '의상 첨부' 입상.

인물 고정 정보(첨부와 함께 `{HEROINE}` 자리에 넣는다)
- 강리아: Kang Ria, very long wavy blonde high ponytail with a blue scrunchie, straight bangs, blue eyes
- 백지현: Baek Jihyun, very long crimson hair with side-swept bangs, red-brown eyes
- 차유진: Cha Yujin, silver-white bob with a gold hairpin, thin round metal glasses, amber eyes
- 한서윤: Han Seoyun, long wavy dark plum hair with pink inner color, half-lidded blue eyes, a mole under her left eye


### 3-1. P1 — 22장

#### 프롤로그 — `prologue_hands_v001.png`
인물 고정 정보 없이 이 블록만 쓴다. 리아 마스터만 첨부한다.
```
Visual novel event CG in EXACTLY the art style of the attached reference. 16:9, 1920x1080.
Scene: under a long presentation table in a corporate meeting hall during a tense pitch. Close-up of two hands under the table: a woman's hand gently pressing once on the back of a man's hand that rests on his knee (dark navy suit sleeve). Above the table edge, blurred papers and a presentation screen.
Mood: tense silence, but the touch says "it's okay". Cool blue projector light from above, warm light on the hands.
No faces. No text, no watermark.
```

#### 고백·핵심 데이트·피칭·크리스마스 — 21장

| 파일 | 인물 · 의상 | 의상 첨부 | `{ACTION}` | `{PLACE}` |
|---|---|---|---|---|
| `ria_r04_scene_v001.png` | 강리아 · 업무복 | `ria_office_pose01_neutral.png` | 고백 뒤 가까이 서서 부드럽게 웃는 순간 | 금요일 저녁 · 조명이 켜진 산책길 |
| `jihyun_r04_scene_v001.png` | 백지현 · 업무복 | `jihyun_office_pose01_neutral.png` | 지현은 바로 대답하려다 물컵에서 손을 뗐다. 이번에는 주인공을 보며 천천히 말했다. | 금요일 저녁 일곱 시 · 약속한 카페 |
| `yujin_r04_scene_v001.png` | 차유진 · 업무복 | `yujin_office_pose01_neutral.png` | 유진은 앞에 둔 메뉴판을 덮었다. 주인공이 앉자 인사보다 먼저 한 번 숨을 골랐다. | 금요일 저녁 일곱 시 · 약속한 카페 |
| `seoyun_r04_scene_v001.png` | 한서윤 · 업무복 | `seoyun_office_pose01_neutral.png` | 서윤은 컵을 내려놓고 주인공을 보았다. 웃으며 다음 화제로 넘기지 않았다. | 금요일 저녁 일곱 시 · 약속한 북카페 |
| `ria_r07_scene_v001.png` | 강리아 · 사복 | `ria_casual_pose02_neutral.png` | 카페를 나서며 리아가 우산을 펴려다 멈췄다. 문 위 차양에서 떨어진 물이 우산보다 먼저 신발에 닿았다. 주인공이 웃음을 참자 리아가 우산을 주인공 쪽으로 내밀었다. | 토요일 오후 · 비가 내리는 동네 카페 |
| `ria_r11_scene_v001.png` | 강리아 · 생활복 | `ria_home_pose02_neutral.png` | 리아가 면을 건지는 동안 주인공은 소스를 저었다. 각자 다른 작은 숟가락으로 맛을 보고 소금을 조금 더 넣었다. | 그 주 일요일 저녁 · 리아의 집 |
| `jihyun_r10_scene_v001.png` | 백지현 · 생활복 | `jihyun_home_pose01_neutral.png` | 주인공이 핀셋으로 집은 부품이 두 번 미끄러졌다. 세 번째에 지현이 손바닥을 아래에 받쳤다. | 토요일 오후 · 지현의 집 |
| `jihyun_r11_scene_v001.png` | 백지현 · 생활복 | `jihyun_home_pose01_neutral.png` | 저녁을 먹고 지현이 작은 카드 상자를 꺼냈다. 빵과 차 그림을 모으는 가벼운 게임이었다. | 일요일 저녁 · 지현의 집 |
| `yujin_r02_scene_v001.png` | 차유진 · 사복 | `yujin_casual_pose01_neutral.png` | 작은 전시실 안으로 들어갔다. 유진은 벽을 따라 걷다가 한 그림에서 멈췄다. | 토요일 오후 두 시 · 작은 전시 공간 |
| `yujin_o02_scene_v001.png` | 차유진 · 사복 | `yujin_casual_pose01_neutral.png` | 손을 옮기자 컵 안에 밝은 선이 다시 생겼다. 유진이 종이 위에 주인공의 손 그림자 끝을 짧게 그렸다. | 기록집을 함께 본 토요일 오후 · 같은 카페 |
| `seoyun_r02_scene_v001.png` | 한서윤 · 사복 | `seoyun_casual_pose02_neutral_v003.png` | 서윤이 좋아한다는 얇은 산문집 『느린 모퉁이』를 꺼냈다. 주인공은 표지만 보고 옆 선반의 엉뚱한 제목을 집었다. | 토요일 오후 두 시 · 단골 서점과 북카페 |
| `seoyun_r10_scene_v001.png` | 한서윤 · 사복 | `seoyun_casual_pose02_neutral_v003.png` | 서로 한 조각씩 덜어 줬다. 주인공은 레몬을 먹고 물을 찾았고, 서윤은 초콜릿을 먹고 자기 접시를 다시 봤다. | 토요일 오후 · 단골 북카페 |
| `seoyun_r13_scene_v001.png` | 한서윤 · 업무복 | `seoyun_office_pose01_neutral.png` | 서윤이 수첩을 접었다. 탁자 위에는 컵 두 개만 남았다. | 약속한 월요일 저녁 일곱 시 · 카페 |
| `ria_r16_scene_v001.png` | 강리아 · 업무복 | `ria_office_pose01_neutral.png` | 피칭에 이긴 날 해 질 무렵. 리아가 옥상 난간에 기대 길게 숨을 내쉬고, 돌아보며 크게 웃는다. "나 오늘 제일 잘했지? 솔직하게." 뒤로 노을 진 도시. | 피칭 당일 저녁 · 회사 옥상 |
| `jihyun_r16_scene_v001.png` | 백지현 · 업무복 | `jihyun_office_pose01_neutral.png` | 피칭 직후 비상계단. 지현이 한 칸 내려와 눈높이를 맞추고, 눈을 감고 다가온다. 초록 비상구 표시등. 입술이 닿기 직전 구도. | 피칭 당일 저녁 · 회사 비상계단 |
| `yujin_r16_scene_v001.png` | 차유진 · 업무복 | `yujin_office_pose01_neutral.png` | 클라이언트 앞 발표 화면 옆에 리모컨을 쥐고 선 유진. "비슷한 게 아니라, 제가 그렸어요." 떨리지만 고개를 든 얼굴. 주인공은 맨 앞줄 시점. | 피칭 당일 · 클라이언트사 대회의실 |
| `seoyun_r16_scene_v001.png` | 한서윤 · 업무복 | `seoyun_office_pose01_neutral.png` | 엘리베이터 앞. 서윤이 뒤에 선 남자(전남편, 흐릿한 뒷모습)를 등지고 돌아와 주인공의 팔짱을 낀다. "가자, 주인공아." 담담하고 홀가분한 얼굴. | 피칭 당일 저녁 · 클라이언트사 엘리베이터 앞 |
| `ria_x01_scene_v001.png` | 강리아 · 겨울 외투 | `ria_winter_pose01_neutral.png` | 반쯤 해체된 팝업 행사장, 불이 켜진 트리 하나 아래. 리아가 포장 상자에 등을 돌리고 앉아 있고, 주인공의 손이 포니테일에 새 파란 벨벳 슈슈를 서툴게 감는다. 붕어빵 봉투가 옆에. | 12월 24일 밤 · 철수 중인 팝업 행사장 |
| `jihyun_x01_scene_v001.png` | 백지현 · 생활복 | `jihyun_home_pose01_neutral.png` | 현관에서 회색 카디건 차림의 지현이 30분 단위로 칸을 나눈 일정표 한 장을 내민다. 21:00 칸만 비어 있다. 침착한 척하지만 귀가 빨갛다. | 12월 24일 오후 · 지현의 집 |
| `yujin_x01_scene_v001.png` | 차유진 · 생활복 | `yujin_home_pose01_neutral.png` | 창가 책상. 유진이 스케치북을 뒤집어 내민다. 처음으로 정면에서 그린 주인공의 얼굴, 오른쪽 아래에 '차유진' 서명. 낮은 겨울 해가 옆얼굴에 걸린다. | 12월 24일 오후 늦게 · 유진의 집 |
| `seoyun_x01_scene_v001.png` | 한서윤 · 사복 | `seoyun_casual_pose02_neutral_v003.png` | 난로가 켜진 작업실. 서윤이 작업대에 와인 잔 두 개를 나란히 놓고 천천히 닦는다. 의자에 걸린 주인공의 코트 위에 서윤의 가디건이 겹쳐 걸려 있다. | 12월 24일 저녁 · 서윤의 작업실 |

### 3-2. P2 — 18장

| 파일 | 인물 · 의상 | 의상 첨부 | `{ACTION}` | `{PLACE}` |
|---|---|---|---|---|
| `ria_x02_scene_v001.png` | 강리아 · 겨울 외투 | `ria_winter_pose01_neutral.png` | 파란불로 바뀌는 횡단보도 앞, 리아가 반 발짝 앞에서 돌아보며 주인공의 손을 잡아끈다. 새 파란 슈슈를 한 포니테일이 흔들린다. | 1월 평일 저녁 · 퇴근길 횡단보도 |
| `jihyun_x02_scene_v001.png` | 백지현 · 겨울 외투 | `jihyun_winter_pose01_neutral.png` | 버스 정류장 의자에 나란히 앉아, 지현이 장갑 낀 손으로 주인공의 손등을 한 번 누른다. 정류장 불빛, 다가오는 버스. | 1월 평일 저녁 · 회사 앞 버스 정류장 |
| `yujin_x02_scene_v001.png` | 차유진 · 업무복 | `yujin_office_pose01_neutral.png` | 3층 복도 끝 창틀에 스케치북을 올려 보여 주는 유진. 회의실 책상 아래 겹쳐진 두 손 그림, 연필 제목 '석 달 뒤에도'. 짧은 겨울 노을. | 1월 평일 저녁 · 회사 3층 복도 끝 창문 |
| `seoyun_x02_scene_v001.png` | 한서윤 · 겨울 외투 | `seoyun_winter_pose01_neutral.png` | 창가 자리, 라테 두 잔 너머로 서윤이 농담 없이 주인공을 똑바로 본다. 창밖에 클라이언트사 건물. | 1월 평일 저녁 · 회사 앞 카페 |
| `ria_x01b_scene_v001.png` | 강리아 · 생활복 | `ria_home_pose02_neutral.png` | 크리스마스 다음 날 아침. 리아가 창가에서 머그를 들고 졸린 얼굴로 돌아보며 웃는다. 삐뚤게 감긴 파란 슈슈. | 12월 25일 아침 · 리아의 집 |
| `jihyun_x01b_scene_v001.png` | 백지현 · 생활복 | `jihyun_home_pose01_neutral.png` | 크리스마스 다음 날 아침. 꺼진 휴대폰을 옆에 둔 채 지현이 머그를 들고 주인공 쪽으로 몸을 돌린다. 편안한 얼굴. | 12월 25일 아침 · 지현의 집 |
| `yujin_x01b_scene_v001.png` | 차유진 · 생활복 | `yujin_home_pose01_neutral.png` | 크리스마스 다음 날 아침. 유진이 '이 방은 아침 빛이 제일 예쁘다'던 창가에 머그를 들고 앉아 있다. 안경에 아침 햇살. | 12월 25일 아침 · 유진의 집 |
| `seoyun_x01b_scene_v001.png` | 한서윤 · 생활복 | `seoyun_home_pose02_neutral.png` | 크리스마스 다음 날 아침. 작업실 창가에서 서윤이 머그를 들고 졸린 눈으로 웃는다. 작업대 위에 빈 와인 잔 두 개. | 12월 25일 아침 · 서윤의 작업실 |
| `ria_sp1_scene_v001.png` | 강리아 · 사복 | `ria_casual_pose02_neutral.png` | 코인 세탁방 플라스틱 의자에 나란히 앉아, 리아가 주인공의 어깨에 머리를 기댄다. 돌아가는 세탁기 창, 주인공 손바닥 위에 리아의 휴대폰. | 일요일 오후 · 동네 코인 세탁방 |
| `ria_sp2_scene_v001.png` | 강리아 · 업무복 | `ria_office_pose01_neutral.png` | 야근 뒤 옥상. 리아가 따지 않은 캔커피를 쥔 채, 억지로 웃으며 '만약에' 질문을 던진다. 웃음이 한 박자 늦다. | 목요일 밤 · 회사 옥상 |
| `jihyun_sp1_scene_v001.png` | 백지현 · 생활복 | `jihyun_home_pose01_neutral.png` | 조립 중인 작은 집의 계단 난간. 본드가 조금 번진 자리로 지현이 손을 뻗었다가 멈추고, 부드럽게 웃는다. 주인공의 손에 핀셋. | 토요일 오후 · 지현의 집 |
| `jihyun_sp2_scene_v001.png` | 백지현 · 생활복 | `jihyun_home_pose01_neutral.png` | 소파에 기대 잠든 지현. 평온한 얼굴. 주인공의 손에 지현의 휴대폰(알람 화면). 스탠드 불빛. | 화요일 저녁 · 지현의 집 |
| `yujin_sp1_scene_v001.png` | 차유진 · 사복 | `yujin_casual_pose01_neutral.png` | 공원 벤치. 유진이 무릎 위 스케치북에 벤치 등받이에 놓인 주인공의 손을 그린다. 집중한 옆얼굴. | 토요일 오후 · 공원 벤치 |
| `yujin_sp2_scene_v001.png` | 차유진 · 생활복 | `yujin_home_pose01_neutral.png` | 유진이 노트북을 주인공 쪽으로 민다. 화면에 같은 남자의 뒷모습 그림 서른 장이 썸네일로. 긴장해서 소매를 쥔 손. | 일요일 밤 · 유진의 집 |
| `seoyun_sp1_scene_v001.png` | 한서윤 · 생활복 | `seoyun_home_pose02_neutral.png` | 자정. 침대 옆 스탠드 아래 서윤이 얇은 책 『느린 모퉁이』를 펼치고 휴대폰에 대고 낮게 읽는다. 처음 보는 차분한 얼굴. (주인공 없음, 전화 너머) | 평일 밤 · 서윤의 작업실, 전화 |
| `seoyun_sp2_scene_v001.png` | 한서윤 · 사복 | `seoyun_casual_pose02_neutral_v003.png` | 밤 열한 시 작업실. 작은 캐리어에 셔츠를 개어 넣으며 서윤이 자기 농담에 웃는다. 주인공의 손이 셔츠 하나를 건넨다. | 일요일 밤 · 서윤의 작업실 |

#### 이듬해 봄 — 2장 (네 명의 업무복 입상을 모두 첨부)
| 파일 | `{ACTION}` | `{PLACE}` |
|---|---|---|
| `spring_rooftop_scene_v001.png` | 리허설 뒤 옥상. 네 히로인과 신입(짧은 머리 20대 남자, 정장, 뒷모습 위주)이 웃음을 터뜨리며 옆 사람 어깨를 툭 친다. 주인공 시점. | 3월 피칭 전날 저녁 · 회사 옥상 |
| `spring_pitch_scene_v001.png` | 발표 화면에 여섯 이름이 같은 크기로 떠 있고, 그 앞에 네 히로인이 나란히 선다. | 3월 피칭 당일 · 클라이언트사 대회의실 |

### 3-3. P3 — 21장

| 파일 | 인물 · 의상 | 의상 첨부 | `{ACTION}` | `{PLACE}` |
|---|---|---|---|---|
| `ria_r02_scene_v001.png` | 강리아 · 업무복 | `ria_office_pose01_neutral.png` | 리아가 내민 손을 잡고 걸음을 맞췄다. 정면을 보다가 옆을 보고, 다시 앞을 봤다. | 다음 만남 · 아직 밝은 퇴근길 |
| `ria_r08_scene_v001.png` | 강리아 · 생활복 | `ria_home_pose02_neutral.png` | 아침에 식탁을 정리하던 리아가 빵 두 조각을 접시에 놓았다. | 일요일 아침 · 리아의 집 |
| `ria_r10_scene_v001.png` | 강리아 · 생활복 | `ria_home_pose02_neutral.png` | 리아가 동네 지도를 펼치자 접힌 모서리가 자꾸 들렸다. 주인공이 노트로 한쪽을 누르고, 리아는 컵을 올리려다 둘의 팔이 겹친 걸 보고 멈췄다. | 그 주 토요일 오후 · 리아의 집 |
| `ria_r15_scene_v001.png` | 강리아 · 사복 | `ria_casual_pose02_neutral.png` | 지도에서 골랐던 작은 공원에 갔다. 주인공은 긴 의자의 빈자리와 길게 드리운 빛을 찍고, 리아 옆에 앉아 짧은 글을 적었다. | 그 주 일요일 오후 · 동네 산책길 |
| `ria_e01_scene_v001.png` | 강리아 · 생활복 | `ria_home_pose02_neutral.png` | 주인공이 한 부를 리아 쪽으로 밀었다. 리아는 바로 펼치지 않고 표지를 손바닥으로 한 번 쓸어 봤다. | 약 반년 뒤, 초여름의 휴일 · 리아의 집 |
| `jihyun_r05_scene_v001.png` | 백지현 · 사복 | `jihyun_casual_pose01_neutral.png` | 음료 옆에 놓인 종이 냅킨을 지현이 두 번 접었다. 주인공은 그 위에 빈 설탕 봉지를 세웠다. | 고백 다음 날 토요일 오후 · 강변 카페 |
| `jihyun_r08_scene_v001.png` | 백지현 · 생활복 | `jihyun_home_pose01_neutral.png` | 각자 빵에 잼을 발랐다. 주인공의 빵을 보던 지현이 자기 것에도 잼을 더 얹었다. | 일요일 아침 · 지현의 집 |
| `jihyun_r14_scene_v001.png` | 백지현 · 업무복 | `jihyun_office_pose01_neutral.png` | 지현이 펜을 들었다가 내려놓았다. 주인공이 질문에 끝까지 답한 뒤에야 자기 자료를 펼쳤다. | 수요일 오전 · 비교 검토 직전 |
| `jihyun_r16b_scene_v001.png` | 백지현 · 업무복 | `jihyun_office_pose01_neutral.png` | 엘리베이터를 기다리는 동안 지현이 먼저 주인공의 손을 잡았다. 사무실 복도에서는 처음이었다. | 피칭 전날 밤 · 사무실 |
| `jihyun_e01_scene_v001.png` | 백지현 · 생활복 | `jihyun_home_pose01_neutral.png` | 지현이 게임 카드를 펼치려다 조립집을 옮겼다. 둘이 나란히 앉을 자리를 만들고도 손을 떼지 못했다. | 약 반년 뒤, 쉬는 날 오후 · 지현의 집 |
| `yujin_r07_scene_v001.png` | 차유진 · 사복 | `yujin_casual_pose01_neutral.png` | 노트는 서점에서 넣고 나왔다. 저녁에는 같은 떡볶이를 순한 맛과 매운맛으로 따로 주문했다. 유진이 주인공 앞에 물잔을 밀자 주인공은 아직 첫입도 안 먹었다며 웃었다. | 토요일 오후 세 시 · 동네 서점 |
| `yujin_r08_scene_v001.png` | 차유진 · 생활복 | `yujin_home_pose01_neutral.png` | 유진이 커튼을 조금 열었다. 주인공도 일어나 반대쪽 커튼을 조금 걷었다. 어제 그림에서 봤던 그림자가 창가에 비쳤다. | 다음 날 일요일 아침 · 유진의 집 |
| `yujin_r10_scene_v001.png` | 차유진 · 사복 | `yujin_casual_pose01_neutral.png` | 유진이 개인 노트를 펼쳤다. 안쪽 주머니에서 지난 전시 티켓이 나왔다. | 같은 주 토요일 오후 · 동네 카페 |
| `yujin_r11_scene_v001.png` | 차유진 · 생활복 | `yujin_home_pose01_neutral.png` | 유진이 작은 음악 기기 옆을 비우고 컵 두 개를 가져왔다. 주인공은 골라 온 곡 이름을 적었다. | 다음 날 일요일 저녁 · 유진의 집 |
| `yujin_e01_scene_v001.png` | 차유진 · 생활복 | `yujin_home_pose01_neutral.png` | 주인공도 직접 찍은 사진과 짧은 글을 모아 완성한 작은 기록집을 건넸다. 유진은 예전에 봤던 접지 초안 옆에 나란히 놓고 차이를 한눈에 봤다. | 약 반년 뒤 초여름의 휴일 오후 · 유진의 집 |
| `seoyun_r05_scene_v001.png` | 한서윤 · 사복 | `seoyun_casual_pose02_neutral_v003.png` | 반으로 가르자 한쪽이 훨씬 커졌다. 서윤이 큰 쪽을 집으려다 멈췄다. | 고백 다음 날 토요일 오후 두 시 · 약속한 장소 |
| `seoyun_r08_scene_v001.png` | 한서윤 · 생활복 | `seoyun_home_pose02_neutral.png` | 작업실의 작은 주방에서 아침을 준비했다. 서윤이 주인공의 접시로 잘 구워진 빵을 밀어 주자, 주인공은 자기 것을 반으로 갈라 다시 건넸다. | 다음 날 일요일 아침 · 서윤의 작업실 |
| `seoyun_r11_scene_v001.png` | 한서윤 · 사복 | `seoyun_casual_pose02_neutral_v003.png` | 주인공이 고른 다리 아래로 걸었다. 난간 사이로 바람이 들어와 둘은 잠깐 멈췄다. | 일요일 저녁 여섯 시 반 · 서점 앞 |
| `seoyun_e01_scene_v001.png` | 한서윤 · 사복 | `seoyun_casual_pose02_neutral_v003.png` | 서윤이 표지를 손바닥으로 쓸었다. 첫 장을 읽고 나서는 자기 컵보다 책을 먼저 주인공 쪽으로 밀었다. | 약 반년 뒤, 쉬는 날 오후 · 단골 북카페 |

공통 2장은 네 명의 업무복 입상을 모두 첨부한다.
| 파일 | `{ACTION}` | `{PLACE}` |
|---|---|---|
| `common_c05_scene_v001.png` | 카페 테이블에 네 히로인이 모여 식사한다. 유진이 짧게 웃으며 메뉴 한 줄을 가리키고, 지현은 컵 사이 물병으로 물을 나눈다. 리아는 웃으며 수저를 돌리고, 서윤은 턱을 괴고 본다. | 회사 근처 카페 · 점심 |
| `common_colleague_ending_scene_v001.png` | 협업 회의가 끝난 회의실. 네 명이 각자 자리를 정리한다. 누군가는 노트북을 덮고, 누군가는 먼저 손을 흔들며 나간다. | GY브랜딩 회의실 · 퇴근 무렵 |

## 4. 타이틀 키 비주얼 — `title_keyvisual_v001.png`

네 명의 업무복 `pose01_neutral` 입상과 리아 마스터를 첨부한다.
```
Visual novel TITLE KEY VISUAL in EXACTLY the art style of the attached references. 16:9, 1920x1080.
The four heroines from the attached sprites stand together on an office building rooftop just after work, at blue hour: city lights turning on, a few office windows still lit behind them.
Composition: Kang Ria front-center leaning forward with a bright wave; Baek Jihyun to the left with arms loosely crossed, a small smile; Cha Yujin to the right holding a sketchbook to her chest, glasses catching the light; Han Seoyun slightly behind, hair moving in the wind, teasing half-smile.
Leave the upper-left third calm (sky) for the game logo. Do NOT draw any text or logo.
Warm sunset rim light on the characters, cool blue sky. Same faces, hair and eye colors as the references. Adults only. No watermark.
```
받은 뒤 ComfyUI 3-2(타이틀) 설정으로 그림체를 맞춘다.

## 5. ComfyUI로 할 것 (집 PC)

순서와 명령은 `Docs/home-comfyui-checklist.md`를 따른다.
1. 서윤 사복 v004 9장 (+ 2-2의 서윤 울먹 1장)
2. 배경 23장 그림체 통일
3. **배경 시간대 변환 31장** — `backgrounds-title-plan-v001.md` 1절 표의 저녁·밤·기타 칸, 3-1절 설정
4. 이 문서의 ChatGPT 결과 94장을 같은 IP-Adapter 설정(입상은 `comfy_sprite_style.py`, CG·타이틀은 배경 워크플로)으로 통일

## 6. 받은 뒤

- 위 폴더에 올리고 Claude에게 "검수해 줘"라고 하면 해상도·손·얼굴·색을 확인한다.
- 통과한 것만 승인받고 게임에 연결한다. 울먹 표정은 장면마다 `face("ria", "teary")`로 지정한다.
- ChatGPT 이미지의 상업적 이용 조건은 출시 전에 직접 확인한다.
