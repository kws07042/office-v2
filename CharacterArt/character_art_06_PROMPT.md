# 생성 요청·참조 기록 양식

현행 기준일: **2026-11-04**. [통합 외형 기준](APPEARANCE_CURRENT.md)과 [타이틀 원본 v002](assets/title/title_escalator_jihyun_arm_lowered_v002.png)을 직접 참조한다. 이전 개별 마스터를 새 기본 외형으로 사용하지 않는다.

## 생성 전에 채울 것

| 항목 | 기록 |
|---|---|
| 인물·나이·직무 | 인물별 문서의 기존 성인 설정 |
| 기준 파일·버전·해시 | title_escalator_jihyun_arm_lowered_v002.png / 통합 문서의 SHA-256 |
| 인물 식별 | 화면 왼쪽부터 서윤·유진·지현·리아. 대상 인물의 위치를 명시 |
| 용도·장면 | 개별 입상 / 표정 / 포즈 / CG / 대본 사건·소품·감정 |
| 유지 | 얼굴·눈·헤어·성인 체형·현행 의상·사원증·공통 작화 |
| 변경 범위 | 표정·동작·장소 등 실제 요청한 항목 |
| 미확인 부분 | 사진 밖 신발·등판·하의 길이 등. 제작 제안과 확정값을 구분 |
| 출력 | 실제 생성 크기 / 목표 크기 / 알파 / 레이어 계획 |

참조를 도구에 직접 전달했는지 기록한다. 파일명만 적고 이미지 입력을 했다고 주장하지 않는다. 원본 또는 인물별 식별용 비재생성 크롭을 사용하며 변형된 후속 편집본으로 화풍 기준을 갈아타지 않는다.

## 인물 식별용 요약

- 서윤·왼쪽 앞: 플럼빛 긴 웨이브, 밝은 칼라 블라우스·접은 소매, 짙은 스커트·벨트. 과거 갈색 머리·베이지 원피스·점·시계를 자동 복원하지 않는다.
- 유진·가운데 위: 갈색 보브·머리 장식 없음, 흰 목 리본·분홍 긴소매 카디건·짙은 스커트. 다른 인물과 비교해 성인 체형을 작게 축소하지 않는다.
- 지현·오른쪽 위: 크림슨 긴 웨이브, 버건디 셔츠·차콜 재킷·짙은 바지·벨트. 스커트 복장으로 되돌리지 않는다.
- 리아·오른쪽 앞: 금발 높은 포니테일·큰 남색 리본, 녹색·청록 눈과 선명한 윗속눈썹, 연한 청회색 칼라 블라우스·짧은 소매·짙은 스커트.

네 명 모두 남색 사원증과 밝은 세로 홀더 한 개, 귀걸이·피어싱 없음. 상세는 각 인물 문서와 실제 사진을 함께 확인한다.

## 새 개별 입상 후보

대괄호는 요청에 맞춰 채우며 그림에 출력할 문구가 아니다. 현재 타이틀은 합쳐진 평면 이미지이므로 완성된 분리 입상으로 오인하지 않는다.

```text
Use the supplied approved escalator title v002 as the identity, outfit and 2D anime
rendering reference. Target: [name, adult age, profession], located [position].
Show only this adult heroine. Preserve her own face, eyes, hairstyle, body proportions,
current outfit and navy employee lanyard. Do not mix traits from the other three women.
Expression and pose: [requested expression and anatomically coherent standing pose].
Keep consistent linework, skin shading, hair highlights and rendering density.
Unseen costume details: [explicit proposal; do not claim these are visible in the reference].
For a full-body sprite, include head and shoes with margins and genuine transparency.
No earrings, piercings, added jewelry, text, watermark, UI or duplicate people.
```

입상 최종 납품은 [레이어 규격](character_art_08_LAYERS.md)을 따른다. 한 장의 생성 PNG를 완성된 파츠 세트로 표시하지 않는다.

## 표정 차분

```text
Edit the supplied approved individual sprite for [name].
Change only [eyes, brows, mouth and/or blush].
Preserve identity, adult proportions, hair, outfit, hands, pose, canvas and baseline.
Compare against the original title v002 for appearance and style consistency.
Keep the existing genuine transparency. Output one expression, not a sheet.
```

새 외형의 개별 입상이 먼저 검수되어야 한다. 타이틀의 네 사람을 한꺼번에 바꾸지 않는다. 가능하면 고정 몸통에 정렬된 얼굴 레이어를 사용하고 변경 범위 밖의 차이를 확인한다.

## 일반 CG

```text
Use the supplied original title v002 and identify each required heroine by name and position.
Scene: [existing event ID, location, time, props, emotion and action].
Preserve each heroine's current identity, adult proportions, hairstyle, outfit and accessories.
Use the same delicate 2D anime style for both characters and background.
Camera: the player's viewpoint. Dohyun's hands/forearms may appear if the interaction needs them;
do not add his face, full body, back, silhouette or reflection.
If the scene explicitly excludes the protagonist's body, exclude his hands/arms too.
Keep coherent joints, body rotation, weight-bearing feet and prop contacts.
Do not render dialogue, logo, UI or phone text into the illustration.
```

## 생성 후 기록

실제 입력 이미지·프롬프트·도구가 알려준 모델명과 설정·생성 원본·출력 크기·알파·직접 수정 범위·확대 방식을 남긴다. 제공되지 않은 모델명은 추정하지 않는다. 원본과 얼굴·손·옷·작화를 직접 비교하고 [QA 양식](character_art_07_QA.md)을 작성한다. 생성 성공·참조 지정·사용자 선호·인게임 검수 완료는 각각 구별한다.
