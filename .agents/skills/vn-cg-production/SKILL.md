---
name: vn-cg-production
description: Turn the project's current scenario and CG plans into traceable visual-asset briefs, priorities, and readiness decisions. Use when auditing, planning, or integrating VN CGs and sprites; only connect assets after explicit approval.
---

# CG production planning

## Read first
Read `AGENTS.md`, `SECURITY.md`, `CharacterArt/APPEARANCE_CURRENT.md`, `CharacterArt/CURRENT_ASSETS.json`, `CharacterArt/CG_CURRENT.md`, and the relevant approved story. Inspect `Source/game/event_cg_plan.json`, `Source/game/event_assets.json`, `Source/game/event_cg_slots.rpy`, `Docs/scene-cg-plan-v001.md`, `Docs/scene-cg-production-v001.csv`, `Docs/adult_event_cg_plan_v1.json`, `Docs/성인이벤트_CG3장_제작명세_v1.md`, and `Docs/성인이벤트_CG3장_자산목록_v1.csv` when present. Check dates and current-status notices before relying on historical plans.

## Procedure
Current reset policy: the user requested removal and recreation of previous character/CG/candidate art on 2026-11-06, retaining title v002 for reference. Consult `Docs/production-review-v001/REVIEW.md`, `NARRATIVE.md`, and `art-reset.json`; finished new art and approved legacy reuse are both zero. Do not restore removed assets from historical manifests automatically.

1. Establish the active revision from current approved docs and executable `Source/game/` scripts. Resolve conflicts in favor of newer explicit approvals and current scripts; mark unresolved conflicts REVIEW/HOLD. In particular, respect the current Seoyun divorced-parent story; archived marriage/ring art is not a current brief.
2. Inventory actual files, manifests, hashes, script references, CG slots, event IDs, unlock conditions, and tests. Distinguish planned slots, existing files, approved files, variants, expression/outfit deltas, and distinct compositions. Compute counts from parsed records and filesystem evidence; never infer delivery from a plan entry.
3. For each proposed asset, record heroine/event ID, source file and line/label, cast, location/time, depicted action and emotion, approved outfit/props, composition/crop, required variants, display/unlock condition, current asset/path/hash/approval, and rationale.
4. Mark **READY** only if story outcome, cast, location, action, outfit/props, display condition, and appearance reference are settled. **REVIEW** when a material choice, branch difference, plan conflict, prop, or composition needs a decision. **HOLD** when story/design/reference is unresolved enough that production risks rework. Readiness describes the brief, not finished art.
5. Assign a separate production priority P0/P1/P2 with rationale. Count composition masters separately from expression/outfit/effect variants and exported files. Prefer reuse only when identity, continuity, crop, and emotional purpose remain correct. Recommend Live2D only for poses with clear sustained motion value; static layered sprites or CGs are sufficient otherwise.
6. Draft prompts and composition briefs from approved evidence. Preserve the v002 title appearance reference and its explicit unknowns. Do not invent lore, measurements, wardrobe approvals, or character traits. Identify external tool/model terms and commercial-use limits for the user to verify; do not claim rights from a tool name alone.
7. Never bulk-generate, replace, rename, delete, or connect art without authorization. Before integration, require explicit approval, verified provenance/license, QA pass, stable asset ID/path, and a reviewed Ren'Py diff. Keep candidates outside production manifests until then.
8. Validate counts and references with read-only scripts where possible. Report the exact command, exit status, files inspected, and whether visual review was manual or metadata-only. No test or asset not actually checked may be called passed.

## Deliverable
Provide a concise per-asset table (ID, script location, brief, variants, existing/approved state, READY/REVIEW/HOLD, P0/P1/P2, display condition) and separate totals for base compositions, source variants, output files, existing approved reuse, new work, and unresolved decisions. Cite repository paths and distinguish recommendation from approved production scope.
