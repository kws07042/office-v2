---
name: vn-continuity-check
description: Review this visual novel's current story text and proposed scene/art changes for chronology, character voice, relationship state, props, wardrobe, branch logic, and approved-canon conflicts. Use for scenario or CG continuity review; write proposals rather than silently changing story.
---

# Story and art continuity

## Canon and source order
Read `AGENTS.md`, `SECURITY.md`, `README.md`, and the relevant current character and validation docs. Use approved current docs plus executable `Source/game/*.rpy` as evidence. Older reports are historical unless explicitly reaffirmed. For appearance, use `CharacterArt/APPEARANCE_CURRENT.md` and the title v002 reference; previous CG manifests and individual masters may be archived. For Seoyun, consult `Docs/seoyun-divorced-parent-v002.md` and current scripts; do not revive archived marriage/ring continuity.

## Review procedure
1. Define scope: changed scene/event IDs, scripts, branches, candidate CGs, and the canonical revision/date. Read only relevant surrounding events and decisions, then trace calls/jumps/menus and state writes to downstream scenes.
2. Build a concise timeline for each affected route/branch: date/time, workday, location, travel, clothing, props, who knows what, relationship status, promises, and unresolved conflict. Cite script path plus label/line.
3. Compare alternatives and save/re-entry states. Check that choices have distinct, intentional consequences where promised; choices do not silently converge into contradictory memories; endings and later romance respect explicit closure; CG display conditions match the scene actually reached.
4. Check each character's established adult identity, job, voice, boundaries, emotional cause/effect, and relationship pace against current character docs and scene history. Check staging continuity: who holds/moves each prop, clothing transitions, time of day, positions, and whether the proposed image depicts actions the script supports.
5. Classify findings as **Blocker**, **Review**, or **Note**, with evidence and impact. Distinguish confirmed contradictions from ambiguity and subjective craft suggestions. Never treat lack of a detail as permission to invent it.
6. Produce proposed wording or targeted edits only when useful. Do not edit approved story, character facts, endings, CG manifests, or runtime logic without explicit user approval. Correct an obvious typo only if within the user's authorized scope, and record it.
7. Do not execute game files, bytecode, saves, or unreviewed tools to inspect them. Static reading and approved repository checks are sufficient for continuity findings. If runtime validation is needed, hand off its plan to `renpy-regression` and state what it can establish.

## Report
State reviewed revision and scope; findings with severity, event/branch, cited locations, and consequence; confirmed facts versus assumptions; proposed minimal resolution; affected downstream events/assets/tests; and explicitly unreviewed material. Separate narrative judgment from mechanically verified behavior.
