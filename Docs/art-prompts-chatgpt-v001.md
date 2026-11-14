# 챗지피티 이미지 제작 목록·프롬프트 v001

2026-11-14 기준 대본(`Source/game/*.rpy`의 `$ location` 179개 표기)과 현행 외형 기준(`CharacterArt/APPEARANCE_CURRENT.md`, 마스터 v001 네 장)으로 정리했다. **제작 계획이며 승인·연결된 원화가 아니다.** 결과물은 `CharacterArt/candidates/` 아래 후보로 넣고, QA(`.agents/skills/vn-art-qa`) 뒤 게임에 연결한다.

## 0. 방식 결정
- **입상 = 마스터 몸 + 표정 얼굴 교체.** 표정마다 전신을 새로 뽑지 않는다(`CharacterArt/character_art_08_LAYERS.md`). 챗지피티에는 *얼굴 표정 시트*만 받고, 얼굴을 마스터 몸에 맞춰 붙이는 작업은 따로 한다.
- **의상 변경(사복·생활복)만 전신을 새로 만든다.** 같은 자세·같은 얼굴로, 몸 전체가 바뀌는 단위이기 때문이다. 표정은 위의 얼굴 시트를 공유한다.
- **배경은 장소별 1장 + 필요한 시간대 변형.** 같은 장소를 대본 여러 곳에서 다시 쓴다.
- **CG는 핵심 장면만.** 일반 장면 CG는 아래 우선순위대로 만든다. 성인 이벤트 CG는 챗지피티 정책상 만들 수 없으니 별도 도구로 한다.
- 모든 그림은 마스터와 **같은 그림체**(셀 명암, 선 굵기, 색감)로 만든다. 실사 질감, 3D 렌더 느낌, 사진 배경은 쓰지 않는다.

## 0-1. 그림체 절대 고정 (2026-11-14 사용자 결정)
그림체는 마스터 v001 네 장과 화풍 기준 그림 `CharacterArt/candidates/user-uploads/강리아 마스터.png`에서 **바꾸지 않는다.** 어긋나면 수정하지 않고 버린다.

**가장 확실한 방법: 마스터를 만든 도구로 이어서 만든다.**
- 로컬 ComfyUI, Anima Turbo 1.1, 화풍 IP-Adapter에 `강리아 마스터.png`를 넣고, 마스터와 같은 2차 다듬기 단계를 거친다. seed는 리아 1002, 지현 1002, 서윤 1003, 유진 1103(`CharacterArt/candidates/heroine-masters-v001/README.md`).
- 표정은 마스터 얼굴을 고정한 채 얼굴 부분만 다시 그리는 방식(inpaint)으로 만든다. 몸과 그림체가 그대로 남는다.

**챗지피티로 할 때 지킬 것**
1. 새 대화를 열고 **마스터 PNG와 `강리아 마스터.png`를 둘 다 첨부**한다. 한 대화 안에서 같은 인물을 계속 만들고, 대화가 길어져 그림체가 흔들리면 새 대화로 다시 시작한다.
2. 아래 **화풍 고정 문단을 모든 프롬프트 맨 앞에** 붙인다.
3. 결과를 마스터 옆에 나란히 놓고 아래 체크리스트로 본다. 하나라도 어긋나면 버린다.

화풍 고정 문단(모든 프롬프트 앞에 그대로 붙임):
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

**그림체 체크리스트 (마스터와 나란히 비교)**
| 항목 | 통과 기준 |
|---|---|
| 선 | 굵기·색·깔끔함이 마스터와 같다. 스케치 선·붓 질감 없음 |
| 눈 | 눈매·홍채 그라데이션·하이라이트 모양과 위치가 같다 |
| 채색 | 셀 명암 단계 수와 그림자 색, 하이라이트 모양이 같다. 그라데이션·광택 과다 없음 |
| 얼굴 | 턱선·코·입 그리는 방식, 얼굴 비율이 같다 |
| 머리 | 머리 결 표현과 하이라이트 방식이 같다 |
| 색감 | 채도·따뜻함이 마스터 범위 안이다 |
| 배경 | 히로인 옆에 놓았을 때 배경만 사실적이거나 붓 터치가 보이지 않는다 |

## 1. 수량 요약
| 구분 | 새로 만들 것 | 비고 |
|---|---|---|
| 표정 얼굴 시트 | 4장(히로인당 8표정 = 얼굴 32개) | 의상과 무관하게 공유 |
| 의상 전신 | 8장(4명 × 사복·생활복) | 업무복은 마스터 완료 |
| 배경 | 28장 + 시간대 변형 10장 = **38장** | 아래 표 |
| 일반 장면 CG | P1 8장, P2 14장, P3 12장 | `Docs/scene-cg-production-v001.csv`의 34장과 v003 신규 장면 |
| 합계(성인 CG 제외) | **약 84장** | 최소 출시용: 시트 4 + 의상 8 + 배경 P0 12장 + CG P1 8장 = 32장 |

## 2. 표정 8종 (히로인 공통 목록, 연기는 인물별)
| 키 | 표정 | 리아 | 지현 | 유진 | 서윤 |
|---|---|---|---|---|---|
| neutral | 기본 | 밝게 다문 미소 | 무표정에 가까운 단정함 | 살짝 긴장한 기본 | 여유 있는 반쯤 감은 눈 |
| smile | 미소 | 활짝 웃음 | 입꼬리만 살짝 | 수줍은 미소 | 장난스러운 미소 |
| laugh | 크게 웃음/장난 | 눈 감고 깔깔 | 웃음 참는 얼굴 | 손으로 입 가리고 웃음 | 놀리는 웃음 |
| blush | 홍조·설렘 | 볼 붉히며 시선 피함 | 귀까지 빨개져 굳음 | 눈 내리깔고 새빨개짐 | 장난이 멈춘 진지한 홍조 |
| surprise | 놀람 | 눈 크게, 입 벌림 | 눈썹 올리고 멈칫 | 안경 너머 동그란 눈 | 눈 살짝 커짐 |
| pout | 삐짐·토라짐 | 볼 부풀림 | 팔짱 낀 듯한 시선 | 입술 삐죽 | 반쯤 감은 눈으로 흘겨봄 |
| sad | 서운·미안 | 눈썹 처지고 억지 미소 | 시선 떨굼, 입 다묾 | 눈물 맺힘 직전 | 웃음 없이 먼 곳 봄 |
| serious | 진지·단호 | 웃음기 뺀 결심 | 업무 모드 단호 | 용기 낸 직구 | 장난 없는 정면 응시 |

## 3. 의상 전신 8장
| 인물 | 사복(데이트) | 생활복(집) |
|---|---|---|
| 강리아 | 밝은 니트+데님 스커트, 운동화. 파란 슈슈 유지 | 오버사이즈 후드 티+반바지, 머리 내림 |
| 백지현 | 베이지 트렌치+버건디 니트, 슬랙스 대신 롱스커트, 로퍼 아닌 앵클부츠 | 회색 카디건+긴 홈웨어 바지, 머리 반묶음 |
| 차유진 | 크림 블라우스+카디건 유지, 플리츠 스커트, 크로스백. 안경 유지 | 큰 셔츠+레깅스, 머리핀 |
| 한서윤 | 검정 슬립 원피스+얇은 니트 가디건, 펌프스 | 실크 셔츠 홈웨어 세트 |

> 사복·생활복 디자인은 이번 제안이다. 외형 기준 문서에 아직 없으니 결과를 보고 확정한다.

## 4. 배경 목록 (우선순위·대본 사용처)
| ID | 장소 | 시간대 | 대본 사용 | 우선 |
|---|---|---|---|---|
| bg_office | 온빛브랜딩 오픈 오피스(공용 작업 공간·협업 테이블·디자인 작업 공간·창가) | 낮 / 저녁 | 15회+ | P0 |
| bg_meeting | 회사 회의실 | 낮 | 10회 | P0 |
| bg_cafe | 동네 카페(회사 근처·역 근처 공용) | 낮 / 밤 / 비 | 30회+ | P0 |
| bg_bookcafe | 서점 안쪽 북카페(서윤 단골) | 낮 | 10회 | P0 |
| bg_restaurant | 작은 동네 식당 | 저녁 | 10회 | P0 |
| bg_ria_home | 리아의 집 거실(지도·화분·소파) | 밤 | 10회 | P0 |
| bg_jihyun_home | 지현의 집 거실(조립 모형 선반·찻잔) | 밤 | 8회 | P0 |
| bg_yujin_home | 유진의 집(창가 작업 책상·음악 기기) | 낮 / 밤 | 9회 | P0 |
| bg_seoyun_studio | 서윤의 개인 작업실(책장·소파·작은 주방) | 밤 | 5회 | P0 |
| bg_dohyun_home | 도현의 원룸 | 밤 | 5회 | P0 |
| bg_office_front | 회사 앞 거리·횡단보도·벤치 | 저녁 | 8회 | P0 |
| bg_alley | 동네 골목·산책길 | 낮 / 저녁(가로등) | 8회 | P0 |
| bg_client_hall | 클라이언트사 대회의실(피칭) | 낮 | 5회 | P1 |
| bg_bbq | 고깃집 회식 테이블 | 밤 | 4회 | P1 |
| bg_rooftop | 회사 옥상 | 노을 | 1회(리아 R16) | P1 |
| bg_stairwell | 회사 비상계단 | 저녁 | 1회(지현 R16) | P1 |
| bg_elevator | 엘리베이터 안·복도 | 낮 | 3회 | P1 |
| bg_station | 역 앞·버스 정류장 | 밤 | 4회 | P1 |
| bg_popup | 팝업 행사장 입구 / 뒤편(가림막) | 낮 | 2회 | P1 |
| bg_gallery | 작은 전시 공간 | 낮 | 3회 | P1 |
| bg_teahouse | 조용한 찻집(지현) | 낮 | 2회 | P1 |
| bg_riverside | 강변·다리 | 낮 | 3회 | P1 |
| bg_pocha | 역 뒤 골목 포차 | 밤 | 1회(리아 O04) | P2 |
| bg_motel | 역 앞 모텔 방 | 밤 | 1회(리아 O04) | P2 |
| bg_hotel_hall | 출장 숙소 복도·자판기 | 밤 | 1회(지현 R12) | P2 |
| bg_parts_shop | 모형 부품 가게 | 저녁 | 1회(지현 R06) | P2 |
| bg_old_bookshop | 오래된 동네 헌책방 | 오후 | 1회(서윤 R07) | P2 |
| bg_client_lobby | 클라이언트사 로비·엘리베이터 앞 | 낮 | 2회 | P2 |

메신저 장면(약 40곳)은 휴대폰 화면이 덮으므로 배경을 따로 만들지 않는다.

## 5. 일반 장면 CG 우선순위 (v003 신규 장면 + 기존 CSV)
| 우선 | 장면 | 위치 |
|---|---|---|
| P1 | 피칭 당일 4장(리아 옥상 / 지현 비상계단 / 유진 '창가' 고백 / 서윤 팔짱) | 각 루트 R16 |
| P1 | 고백 4장(각 루트 R04) | `scene-cg-production-v001.csv` |
| P2 | TF 회식(루트 공통 구도) 1장, 지현 출장 복도 1장, 리아 가림막 1장 | R09, 지현 R12, 리아 R07 |
| P2 | 기존 CSV의 데이트 장면 11장 | 같은 CSV |
| P3 | 유진 벤치 스케치, 서윤 헌책방, 지현 부품 가게 등 일상 12장 | R06~R07, 선택 일상 |

---

## 6. 프롬프트

챗지피티 이미지 생성은 영어 프롬프트가 더 안정적이다. **항상 해당 히로인 마스터 PNG(`CharacterArt/candidates/heroine-masters-v001/final_2048x3072/`)와 화풍 기준 `CharacterArt/candidates/user-uploads/강리아 마스터.png`를 함께 첨부**하고, 0-1의 **화풍 고정 문단을 아래 각 프롬프트 맨 앞에 붙인다.** 배경과 CG도 마찬가지다.

### 6-1. 표정 얼굴 시트 (히로인당 1장)
```
Attached is the official character reference. Draw an EXPRESSION SHEET of this exact character's face only.
Keep identical: face shape, eye shape and color, hairstyle, hair color, bangs, art style, line weight, cel shading, lighting direction (soft light from the upper left).
Layout: 4 columns x 2 rows on a plain flat light-gray background, each cell a head-and-shoulders crop facing the viewer at the same slight 3/4 angle and the same scale, collar and ID-card lanyard visible at the bottom edge.
Expressions in order:
1 neutral – {NEUTRAL}
2 smile – {SMILE}
3 laugh – {LAUGH}
4 blushing – {BLUSH}
5 surprised – {SURPRISE}
6 pouting – {POUT}
7 sad – {SAD}
8 serious – {SERIOUS}
Adult woman (late 20s/early 30s office worker), no text, no labels, no extra accessories, no earrings.
```
`{…}`에는 2번 표의 해당 인물 칸을 영어로 넣는다. 예시는 리아:
```
1 neutral – bright closed-mouth smile
2 smile – wide cheerful smile showing teeth
3 laugh – eyes closed, laughing playfully
4 blushing – cheeks flushed, looking away shyly
5 surprised – eyes wide, mouth open
6 pouting – puffed cheeks, sulking
7 sad – drooping brows with a forced small smile
8 serious – no smile, determined look
```

### 6-2. 의상 전신 (인물·의상당 1장)
```
Attached is the official character reference. Redraw THIS SAME CHARACTER in the SAME standing pose, same camera angle, same proportions and same face, but change only the outfit to: {OUTFIT}.
Keep: hairstyle and hair accessory, eye color, body proportions, art style, line weight, cel shading, light from the upper left.
Full body from the top of the head to the shoes, centered, vertical 2:3 canvas, transparent background (or plain white if transparency is unavailable).
Adult woman office worker in her late 20s/early 30s. No ID card for casual/home outfits. No earrings, no extra jewelry, no text.
```
예: 리아 사복 → `{OUTFIT}` = `light knit sweater, denim A-line skirt, white sneakers; keep the blue scrunchie in her high ponytail`

### 6-3. 배경 (장소당 1장)
```
Visual novel background art drawn in EXACTLY the art style of the attached character references (same line weight, same flat cel shading, same palette warmth), so a character from the reference can stand in it without looking pasted in. Not photorealistic, no 3D render look, no painterly texture.
Scene: {PLACE}, {TIME}.
Setting: contemporary Seoul, Korea; Korean signage only as unreadable shapes.
Camera: eye level (about 150 cm), slightly wide lens, clear empty floor area in the lower center where a standing character will be placed; keep the bottom 28% visually calm (a dialogue box will cover it).
No people, no characters, no text, no watermark. 16:9, 1920x1080.
```
장소 문장 예시:
| ID | `{PLACE}` |
|---|---|
| bg_office | a bright open-plan office of a small branding agency, long shared desks with monitors and design proofs, plants, large windows |
| bg_meeting | a small glass-walled meeting room with a long table, wall screen, sticky notes |
| bg_cafe | a cozy neighborhood café with wooden tables, window seats, warm pendant lights |
| bg_bookcafe | a quiet book café inside a bookstore, tall shelves, reading tables, small bell over the door |
| bg_ria_home | a cheerful one-room apartment living area with a sofa, a city map pinned on the wall, small plants |
| bg_jihyun_home | a tidy minimalist living room with a shelf of miniature house models and a tea set on a low table |
| bg_yujin_home | an illustrator's apartment corner: desk by a large window, drawing tablet, small music player, art prints |
| bg_seoyun_studio | a private writing studio: bookshelves, a soft sofa, a small kitchenette, warm lamps |
| bg_client_hall | a large corporate presentation hall with a projector screen and a long judging table |
| bg_rooftop | an office building rooftop with a railing and city skyline |
| bg_stairwell | an office emergency stairwell, concrete steps, handrail, green exit sign |
| bg_bbq | a Korean barbecue restaurant table with a grill, side dishes, busy warm atmosphere |

`{TIME}`: `daytime, soft sunlight` / `evening, golden hour` / `night, warm interior lights` / `rainy afternoon, rain on the windows`

### 6-4. 장면 CG
```
Visual novel event CG drawn in EXACTLY the art style of the attached references (same line art, eyes, cel shading and palette). 16:9, 1920x1080, full illustration with background.
Characters: {HEROINE} exactly as in the reference (same face, hair, outfit: {OUTFIT}). The male lead appears only as hands/arms or from behind, face never shown.
Scene: {ACTION}, at {PLACE}, {TIME}.
Emotion: {EMOTION}. Camera: {SHOT}.
Adults only. No text, no watermark.
```
예: 유진 피칭 고백 → `{ACTION}` = `standing at a presentation screen holding a remote, nervously admitting in front of clients that she is the artist behind a popular anonymous illustration account`, `{SHOT}` = `medium shot from the audience side, the lead's back visible in the foreground nodding to her`

## 7. 넘겨줄 때
- 파일 이름: `{인물}_{종류}_{키}_v001.png` 예) `ria_face_sheet_v001.png`, `ria_casual_full_v001.png`, `bg_cafe_night_v001.png`
- `CharacterArt/candidates/chatgpt-v001/` 폴더에 올리거나 채팅에 첨부. 표정 시트는 얼굴 잘라 맞추기·색 보정·누끼를 거쳐 입상 레이어로 만든다.
- 챗지피티 이미지의 상업적 이용 조건은 사용 전에 직접 확인한다.
