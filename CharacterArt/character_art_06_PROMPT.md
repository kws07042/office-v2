# 생성 요청·참조 기록 양식

2026년 10월 15일 최신 사용자 정정: 네 히로인 모두 기본 디자인은 귀걸이 없음. 스터드·고리·드롭·이어커프·귀 피어싱을 자동 추가하지 않는다. 이전 참조의 귀걸이보다 이번 지시를 우선하며 예외는 별도 지시 때만 둔다. 귀 주변 금속 조각·잔여 고리·후광이 없는지 검수한다. 작업 상태는 아래 최신 기록 및 파일별 QA를 따른다. 귀걸이 제외 원칙은 유지한다.

이 문서는 프롬프트 준비용이다. 강리아의 기준은 [확정 참조 마스터](assets/ria/master/ria_master_v001.png)다. 얼굴·헤어·의상을 따르고 손의 애매한 경계는 복제하지 않는다. 차유진은 [제공 예비 마스터](assets/yujin/reference_v001/yujin_reference_v001.png)를 기준으로 하며 이전 A안으로 재설계하지 않는다. 백지현·한서윤도 실제 채택 참조가 제공되면 미승인 A안보다 우선한다.

## 생성 전에 채울 것

| 항목 | 입력 |
|---|---|
| 캐릭터·나이 | 이름 / ID / 성인 나이 |
| 용도 | 마스터 후보 / 표정 차분 / 새 자세 / 일반 CG / 일반 메신저 사진 |
| 상태 | 외형 A안 / 채택 마스터 기반 / 사용자 제공 자산 검수 |
| 얼굴·의상 기준 | 실제 파일명, 버전, 경로 |
| 그림체 기준 | 실제 파일명, 버전, 무엇을 따라야 하는지 |
| 구도 참고 | 다른 캐릭터 얼굴·의상을 가져오지 않도록 용도 제한 |
| 바꿀 것 | 예: 입꼬리와 눈썹만 |
| 고정할 것 | 얼굴·헤어·체형·의상·장신구·캔버스·위치 |
| 산출 | 실제 생성 크기 / 목표 크기 / 투명 여부 |
| 대본·장면 | 해당 사건과 실제 등장 소품 |

참조가 없으면 ‘없음’이라고 기록한다. 과거 이미지를 참조가 제공된 것처럼 채우지 않는다. 참고만 한 외형과 채택한 마스터를 구분한다.

## 새 마스터 후보용

아래 대괄호는 실제 값으로 채우는 편집 자리다. 이미지에 글자로 출력할 내용이 아니다.

```text
Create one full-body character design candidate for an adult office-romance visual novel.
Character: [name], age [adult age], [profession].
Use the approved style reference for line quality, facial rendering, skin shading,
hair highlights and palette. If no approved style reference exists, label this output
as an exploratory candidate rather than a matched final asset.
Design: [approved design, or the explicitly selected new-master A proposal].
Expression: [one expression]. Pose: [one natural pose with a clear hand action].
Include the complete head, hair and shoes with comfortable margins.
For a sprite, use a genuine transparent background; do not paint a checkerboard.
Preserve anatomically coherent hands and nails, consistent clothing and accessories.
No earrings, ear piercings, ear cuffs or stray metallic fragments near the ears.
No text, watermark, UI, extra character, duplicate fingers, detached accessories or ghost outline.
```

마스터 후보를 확인한 뒤 필요한 차분으로 진행한다. 프롬프트만으로 참조 일치·손의 정상 형태·실제 투명도를 보장하지 않는다.

## 表情差分用

```text
Edit the supplied approved character master. Change only [specific facial expression].
Keep identity, apparent adult age, face proportions, eye color, hairstyle, body,
costume details, pose, lighting, framing, canvas and baseline consistent.
Use the approved earring-free design. No earrings, ear piercings or ear cuffs.
Preserve the existing transparent background. Produce one expression, not a sheet.
Avoid redesigning hands, clothing or ear anatomy while changing the face.
```

생성형 얼굴 편집은 변경 범위 밖에도 영향을 줄 수 있다. 가능하면 확정 몸통과 정렬된 얼굴 차분을 쓰고 실제 차이를 검수한다. 참조에 귀걸이가 남아 있으면 별도 최소 변경 항목으로 적는다. 리아의 기준 참조는 등록돼 있으며, 이미지별 생성·수정은 별도 요청 범위에 따른다.

## 일반 CG용

```text
Use the approved heroine master and approved visual style.
Scene: [existing event ID, place, time, actual props and emotion].
Camera: the player looks at the heroine. Show her face, body language and relevant props.
Do not depict Dohyun's face, body, back, hands, silhouette or reflection.
Use a complete scene background, with composition readable behind the game's dialogue area.
Keep the heroine's identity, adult age, costume and approved non-ear accessories consistent.
Use the earring-free design; no earrings, ear piercings or ear cuffs.
Do not render dialogue, UI or phone text into the illustration.
```

## 생성 후 기록

실제로 사용한 프롬프트, 도구가 제공한 모델명·설정만 기록한다. 출력 파일·원본 크기·알파 검사·직접 수정·확대 방식을 남긴다. 도구가 모델을 알려주지 않으면 추정하지 않는다. [QA 양식](character_art_07_QA.md)을 복사해 이미지 옆에 둔다. 한 번 생성됐다는 사실을 승인으로 처리하지 않는다.


## 현행 상태

강리아 참조 채택일은 2026년 10월 15일이다. 불필요한 리아 중간 이미지는 사용자 요청에 따라 삭제했다. 과거 텍스트 이력의 파일명은 현행 생성 참조가 아니다.
