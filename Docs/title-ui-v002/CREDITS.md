# 제작 기록과 출처

- 제작일: 2026-11-03.
- 배경: 내장 imagegen으로 새로 생성. 참고 이미지는 프로젝트의 ria_r07_umbrella_v005 CG. 프롬프트는 Design/ai_prompts.json의 background 항목.
- 로고: 내장 imagegen으로 콘셉트 생성 후, 곡선·일몰·쉼표 장식과 정확한 제목을 별도 레이어로 제작. 프롬프트는 같은 파일의 logo_concept 항목. AI 콘셉트 원본은 Design/logo_ai_concept_v001.png.
- 제목·로고의 한글/영문: [Google Fonts 공식 나눔명조 배포](https://github.com/google/fonts/tree/main/ofl/nanummyeongjo). NanumMyeongjo-Regular.ttf 원본과 SIL Open Font License 1.1을 fonts에 함께 보관. 글꼴 파일은 수정하지 않음.
- 브라우저 일반 UI: 운영체제 로컬 글꼴. 원격 글꼴·CDN·분석 SDK·외부 JS 없음.
- 히로인 원화: [프로젝트 확정 CG 목록](https://github.com/kws07042/office-v2/blob/main/CharacterArt/CG_CURRENT.md)의 리아 우산 v005, 지현 미니어처 v005, 유진 스케치 v001, 서윤 독서 v003. 출처와 바이트 해시는 asset_manifest.json. 원본 파일의 저작권·사용 조건을 승계하며 새 라이선스를 부여하지 않음.
- 애니메이션: 생성 영상이 아닌 별도 레이어의 CSS/JavaScript 및 Ren’Py ATL 연출. 공유용 WebP도 같은 레이어를 조합해 제작. 배경과 히로인 원화 자체는 변형하지 않음.
- 구현 참고: [Ren’Py 화면 액션](https://www.renpy.org/doc/html/screen_actions.html), [ATL](https://www.renpy.org/doc/html/transforms.html), [시작 시 실행되는 splashscreen](https://www.renpy.org/doc/html/label.html#special-labels).
- 검증 SDK: [Ren’Py 공식 8.5.3 SDK](https://www.renpy.org/dl/8.5.3/renpy-8.5.3-sdk.zip), [공식 체크섬](https://www.renpy.org/dl/8.5.3/checksums.txt). SHA-256 ff57648f9c04f27e381c48af6d8e3ee3cdec296bed4d3831f47f09b0a71b505e. SDK는 배포 패키지에 포함하지 않으며 실행 검증은 승인 검토에서 차단됨.
