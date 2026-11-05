---
name: renpy-regression
description: Run or design safe Ren'Py source validation for this project, including official SDK lint and existing route, state, gallery, save/load, rollback, and packaging checks. Use when changing or validating game behavior; never treat static/model tests as proof of engine behavior.
---

# Ren'Py regression validation

## Safety and setup
Read `AGENTS.md`, `SECURITY.md`, and `Docs/progression-runtime-checklist-v001.md`. Treat Ren'Py scripts, compiled `.rpyc`/`.pyc`, EXE/DLL, saves, and persistent data as executable or sensitive. Never load untrusted saves/persistent, execute Windows artifacts for inspection, or run `Source/tools` before statically reviewing its code, targets, inputs, and writes. Do not read or copy signing keys or personal saves.

Use a clean task-local save directory and the checkout at `Source/`; do not mix `Windows/game` with current source. Obtain the official Ren'Py SDK from the documented official source and verify the repository-pinned SHA-256 (currently 8.5.3, `eb0a9be7f0fb13632fe25ceade9a8bed5a1b4d6b6e83bd19eeeb29e1a1bb4a45`) before extraction/use. Preserve proxy, TLS, and checksum verification. If blocked, report it and run independent static checks; never fetch an unverified substitute.

## Procedure
1. Record branch, commit, working-tree state, SDK version/hash, platform, and scope. Preserve user changes. Review changed RPY/Python and test sources before executing them, following repository policy.
2. Run relevant pure Python tests first: `python3 -m unittest discover -s Source/tests -p 'test_*.py' -v`. Existing useful checks include `test_progression_model.py` and `test_seoyun_revision.py`. These do not execute Ren'Py and do not establish engine behavior.
3. Run current contract checks only when their baseline applies. `Source/tests/player_flow_contract.py` pins historical base `44ba86ad5aa7cef83d68abd0be261964df74a937`; if current source has since changed, record the baseline mismatch as a stale check. Do not edit assertions or claim current story failure solely from this mismatch. Use `full_script_contract.py` only with its required base objects available and confirm its stated baseline matches scope.
4. With verified official SDK and reviewed current source, run `xvfb-run -a "$SDK/renpy.sh" "$PWD/Source" lint --error-code`. Capture output while preserving exit status.
5. Select existing named suites by changed behavior. Candidate existing suites include `player_flow_checks`, `script_polish_checks`, `work_mini_checks`, `common_romance`, `review_continuity_checks`, `full_editorial_checks`, `yujin_final_checks`, `integrated_story_checks`, and `marriage_disclosure_checks`. First compare fixture/expected story states with current source. `player_flow_checks` and `marriage_disclosure_checks` still contain Seoyun married/cohabiting expectations and must be reported as stale until reviewed for the divorced-parent story; do not silently use their historical pass counts. Run compatible suites with a fresh task-local `--savedir`, `--overwrite-screenshots`, and `--report-detailed`. Inspect logs and reports; require a nonzero executed case count and completed final summary. Do not imply all suites ran when only selected suites ran.
6. For stateful changes, test actual engine save/load, rollback/rollforward, alternate branches, route boundaries, gallery lock/unlock, replay, and persistent behavior as relevant. Model JSON roundtrips and source assertions are not substitutes. Keep task-generated saves isolated; never import personal saves.
7. Build a clean package only when requested/relevant, using the verified official SDK and current `Source/`. Check contents against `SECURITY.md`; exclude tests, bridge, source scripts, saves, signing material, and development tools as appropriate. Do not run the resulting executable as a security check.
8. Inspect `git status --short`; identify generated caches/reports. Remove only files created by this run when safe. Never modify application code merely to make validation pass during an onboarding/check task.

## Report
List each exact command/suite, SDK source/version/hash, pass/fail/skipped/unrun case counts, exit status, generated artifacts, and scope limits. Separate environment blockers, stale baselines, source failures, and untested behavior. Never call lint, a zero-test run, or model-only tests a full regression pass.
