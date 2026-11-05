---
name: vn-art-qa
description: Review proposed visual-novel character art and sprite assets against the current approved appearance reference, provenance, technical requirements, and project QA records. Use when inspecting, accepting, revising, or rejecting supplied or generated art; never promote a candidate or overwrite an original automatically.
---

# Visual asset QA

## Read first
- `AGENTS.md` and `SECURITY.md`.
- `CharacterArt/APPEARANCE_CURRENT.md` and `CharacterArt/CURRENT_ASSETS.json`.
- `CharacterArt/character_art_07_QA.md`; for layered sprites also read `CharacterArt/character_art_08_LAYERS.md`.
- The relevant character guide and asset-local QA/provenance record.

The shared canonical appearance is `CharacterArt/assets/title/title_escalator_jihyun_arm_lowered_v002.png`, SHA-256 `8c6966a5dd2ae5da06cb1db17370baab5ae94049d00ebc7d8d441513a7c677a1`. It is a composite reference, not evidence that individual current-appearance masters or sprites exist. Check the manifest and current docs; filenames such as `master` and `current` do not establish approval. Preserve superseded art as history.

## Procedure
1. Identify each input, its source, intended character/event/use, approval state, expected dimensions/color mode/alpha, and destination. Do not upload private art to external services.
2. Run the read-only `python3 Source/tools/check_image_assets.py [repository-relative paths]` (Pillow required) to report PNG decode, alpha pixels, SHA-256, pinned baseline mismatches, duplicates, and missing planned event assets. A technical pass does not approve art. Inspect image metadata, dimensions, alpha, file integrity, and SHA-256 using local tools. Never execute embedded scripts or untrusted project files. Distinguish technical checks from visual judgments.
3. Compare visible traits to the canonical reference and character guide: face, eyes, hair, silhouette/proportions, approved clothing, badge/props, hands, linework, coloring, and shading. Respect the documented unknowns; do not invent exact measurements or details hidden in the reference. Evaluate poses in scene context and avoid treating a one-scene gesture as a permanent trait.
4. Check for unauthorized accessories, stale designs, changed story facts, cropping/occlusion, unusable transparent edges, and sprite layer/anchor/size mismatches. For adult art, confirm depicted characters are adults and follow the approved brief and applicable image-generation rules.
5. Assign exactly one result per file: **Pass** (all required checks supported and provenance/approval clear), **Fix** (specific correctable defects), or **Reject** (wrong identity/version, unsafe provenance, or fundamental conflict). Unknown evidence is not a pass; state what remains unverified.
6. Write a review record only where requested or repository convention calls for one. Include file/hash, source and approval state, tool/check versions, observations, findings by severity, status, and explicit unresolved checks. Never overwrite an original, alter an asset index, or promote a candidate without user approval.

## Report
For each asset: path and hash; intended use; approval/provenance; technical facts; visual findings tied to reference; Pass/Fix/Reject; exact proposed corrections; unresolved checks. Summarize totals without implying a human visual review occurred when only metadata was checked.
