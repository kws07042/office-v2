# 리아 표정 차분 실제 생성 프롬프트

2026-10-15 / 내장 image_gen 사용. 모델명·시드 미제공. 각 표정은 같은 320×320 마스터 관찰용 크롭에서 독립 편집했다. 게임에서는 생성된 전신·헤어·의상을 사용하지 않고, 눈·눈썹·입 및 shy의 볼 홍조 영역만 별도 마스크로 표시한다. 원본 피부색을 넓게 덮지 않는다.

## smile

Use case: precise-object-edit / identity-preserve.
Edit target: supplied SQUARE HEAD-AND-SHOULDERS CROP of Kang Ria, a 28-year-old adult anime heroine. Produce the SAME CROPPED IMAGE, not full body or a sheet.
Expression variant: BRIGHT AMUSED SMILE during friendly banter. Keep her turquoise eyes open, add a subtle smiling lift of lower lids and cheeks, eyebrows gently relaxed, small naturally open smiling mouth with minimal visible teeth. Adult, playful and warm, not exaggerated laughing, not childlike.
Change ONLY eyebrows, eyelids/eye expression, cheeks and mouth. Absolutely keep exact head tilt, face proportions, nose position, eye centers, hair silhouette and hair strands, golden blonde highlights, scrunchie, ear and neck geometry, shoulder placement, navy ribbed neckline, lighting, scale, square crop framing and transparent pixels. She has no earrings.
This crop will be resized back to 320x320 and overlaid as a small facial layer on an UNCHANGED master body in a game engine. Precise spatial alignment is essential: do not enlarge the face, move the head or reframe. No body/hand changes, no extra hair ornaments. Preserve delicate original anime drawing and skin colors. Actual transparent background. No text, grid, labels or comparison.

## shy

Use case: precise-object-edit / identity-preserve.
Edit only this provided square head-and-shoulders crop of Kang Ria, a 28-year-old adult anime heroine. Output the same square cropped composition, not full body or a sheet.
Expression: SHY AFTER A DIRECT ROMANTIC COMPLIMENT. A small closed-mouth smile she is trying to contain, slightly stronger natural rosy cheeks, turquoise eyes glancing a little downward/aside while eye centers and head pose stay fixed, relaxed gently lifted inner brows. Warm and embarrassed, not frightened, crying, angry, erotic, or exaggerated.
Change only facial expression: eyebrows, eyelids, iris direction within the existing eyes, cheeks and mouth. Preserve identity, adult age, precise eye positions and size, nose position, face geometry, existing head tilt, golden blonde hair strands and highlights, ear, neck, navy ribbed collar, shoulders, lighting and original delicate anime linework. Keep reference hair/face scale and framing. No earrings or new ornaments. A face layer will be aligned to a fixed master body at 320x320 so no head enlargement, shifts or crop changes. Actual transparent background. No text or grid.

## serious

Use case: precise-object-edit / identity-preserve.
Edit only the supplied square head-and-shoulders crop of Kang Ria, adult age 28. Output the EXACT SAME square cropped framing, no full body, no sheet.
Expression: CALM ATTENTIVE SINCERITY while listening and speaking honestly. Her turquoise eyes stay open and focused on the person in front, eyebrows gently attentive with no angry frown, small relaxed closed mouth with the smile reduced to a subtle neutral line. Warm serious listening, not sad, hostile, seductive or expressionless.
Change only the expression in her eyes/eyelids, eyebrows and mouth. Absolutely preserve her facial identity, apparent age, nose location, eye centers, face outline, exact head tilt, hair strands and golden blonde highlights, ear, neck, navy ribbed collar, shoulders and canvas framing. No earrings.
Critical skin-color invariant: Match the input's facial skin hue, brightness, saturation and shading to its existing neck/shoulders. Do not whiten, tan or pink-tint the whole face; do not add blush or dramatic face highlights. This expression should have the SAME skin lighting as the master. No beautification filter.
This will be resized to 320x320 and masked as a facial layer onto an unchanged master. Spatial alignment is essential: no head enlargement/shift/reframing. Original delicate anime rendering. Genuine transparent background. No text/grid/labels.

