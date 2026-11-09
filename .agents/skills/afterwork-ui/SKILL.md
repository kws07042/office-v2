---
name: afterwork-ui
description: Design or review the title menu, dialogue, choices, and tablet messenger for the Korean Ren'Py visual novel 〈퇴근 후, 우리〉. Use for UI mockups and screen styling in this project.
---

# 〈퇴근 후, 우리〉 UI

Read the relevant existing screens and the latest user-approved visual reference before changing layout. Use the game's Korean copy and approved art when they are available. Label temporary assets and sample dialogue outside the playable frame. Read `AGENTS.md` and `SECURITY.md` before touching the game source.

## Screen direction

- **Title:** Give the key visual the full frame. Use the left wall or equivalent quiet area for the Korean wordmark and a short vertical menu. Keep faces clear. Use one motif drawn from the office setting, such as a window mullion or an evening reflection. Keep decorative text and effects subordinate to the title.
- **Dialogue:** Lead with speaker and line. Anchor them near the bottom over the scene. Give the text enough contrast over both light and dark art and keep the portrait's face clear. Put secondary controls in a compact, consistent order.
- **Choices:** Center the stack horizontally, above the dialogue. Keep the text inside the rows left-aligned for scanning. Distinguish hover, focus, and selection through shape or contrast. Check long Korean lines, wrapping, and dense choice lists.
- **Messenger:** Treat it as a physical tablet viewed by the player. Keep a slim bezel and show the scene behind a dim, translucent overlay. Put time, signal, and battery in the tablet's status bar. Use KakaoTalk-like yellow for outgoing messages, white for incoming, and a soft cool chat background. Show the sender name and a circular empty profile slot at the start of incoming groups until approved portraits exist. Keep timestamps, read state, and reply options distinct from chat text.

Use a coherent Korean type scale and repeat spacing values. Reserve strong accents for actions or meaningful states. Inspect whether each gradient, outline, shadow, badge, and label helps the player. A decorative pattern that could sit on any generic dashboard is a cue to cut it.

## Preview and integration

Show mockups at the project's 16:9 game ratio with representative art and real-length Korean text. Compare dialogue, choices, and messenger in the same scene when useful. Keep browser prototypes offline and use existing local assets. For visual review, check the rendered frame at native and smaller window sizes for collisions, clipped copy, and legibility. Check keyboard focus and the longest supplied choices or replies.

When applying an approved design to Ren'Py, start from the existing screen actions and IDs in `screens.rpy`, `office_phone.rpy`, and related styles. Preserve story state and branch behavior through the visual changes. Report browser mockup review separately from actual Ren'Py validation.
