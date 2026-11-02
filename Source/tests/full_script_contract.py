"""Read-only story contract check. Never imports or executes the game."""
import ast
from collections import Counter
import hashlib
import json
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = "7d04db1e7f04ae089951ad3db8aba3e84a5712be"

def baseline(path):
    return subprocess.check_output(["git", "show", BASE + ":" + path], cwd=ROOT).decode("utf-8").replace("\r\n", "\n")

def current(path):
    return (ROOT / path).read_text(encoding="utf-8").replace("\r\n", "\n")

def contract(text):
    rows = text.splitlines()
    state = [l.strip() for l in rows if l.lstrip().startswith("$ ") and not re.match(r"\s*\$ (?:location|chapter)\s*=", l)]
    calls = []
    for row in rows:
        line = row.strip()
        if line.startswith("call phone_deliver("):
            node = ast.parse(line.removeprefix("call "), mode="eval")
            assert isinstance(node.body, ast.Call) and len(node.body.args) >= 3
            node.body.args[2] = ast.Constant(value="<dialogue>")
            calls.append(ast.dump(node, include_attributes=False))
        elif line.startswith(("call ", "jump ", "return", "while ", "label ", "default ")):
            calls.append(line)
    choices = [l.strip() for l in rows if l.lstrip().startswith('"') and l.rstrip().endswith(":")]
    definitions = [l.strip() for l in rows if l.lstrip().startswith("define ") and not l.lstrip().startswith(("define sn =", "define config.version ="))]
    conditions = [l.strip() for l in rows if l.lstrip().startswith(("if ", "elif "))]
    return state, calls, choices, definitions, conditions

runtime = []
changed = []
slot_labels = []
for file in sorted((ROOT / "Source/game").glob("*.rpy")):
    if file.name.endswith("_tests.rpy") or file.name == "testcases.rpy":
        continue
    path = file.relative_to(ROOT).as_posix()
    before, after = baseline(path), current(path)
    bc, ac = contract(before), contract(after)
    assert bc[:4] == ac[:4], "State/call/menu/definition contract changed: " + path
    cursor = iter(ac[4])
    assert all(any(x == wanted for x in cursor) for wanted in bc[4]), "Existing condition removed: " + path
    assert before.count("(거사 — 장면 생략)") == after.count("(거사 — 장면 생략)"), "Reserved scene changed: " + path
    if file.name == "options.rpy":
        assert after.replace("0.35.1-full-script-edit", "<VERSION>") == before.replace("0.35.0-work-minis", "<VERSION>")
    remaining = Counter(bc[4])
    lines = after.splitlines()
    for index, row in enumerate(lines):
        condition = row.strip()
        if not condition.startswith(("if ", "elif ")):
            continue
        if remaining[condition]:
            remaining[condition] -= 1
            continue
        indent = len(row) - len(row.lstrip())
        for child in lines[index + 1:]:
            if not child.strip():
                continue
            if len(child) - len(child.lstrip()) <= indent:
                break
            assert not child.lstrip().startswith(("$ ", "call ", "jump ", "return", "menu:", "while ")), "New condition gates an effect: " + path
    runtime.append(path)
    if before != after:
        changed.append(path)
    slot_labels += re.findall(r"^label ((?:c\d\d|(?:ria|jihyun|yujin|seoyun)_(?:r\d\d|o\d\d|e01)|work_(?:verify|coord|test)\d\d|end_common))(?=[:(])", after, re.M)
assert len(slot_labels) == len(set(slot_labels)) == 95

before_event = json.loads(baseline("Source/game/event_story.json"))
after_event = json.loads(current("Source/game/event_story.json"))
allowed = {
    ("yujin_r12", "special", 3, "heroine"),
    ("jihyun_r15", "home", 1, "heroine"),
    ("jihyun_r15", "home", 1, "dohyun"),
    ("seoyun_r12", "special", 3, "heroine"),
}
event_edits = set()
assert before_event.keys() == after_event.keys()
for event, variants in before_event.items():
    assert variants.keys() == after_event[event].keys()
    for variant, beats in variants.items():
        fresh = after_event[event][variant]
        assert len(beats) == len(fresh) == 4
        for index, (before, after) in enumerate(zip(beats, fresh)):
            assert before.keys() == after.keys()
            for key, value in before.items():
                if value != after[key]:
                    entry = (event, variant, index, key)
                    assert entry in allowed, "Unreviewed event change: " + repr(entry)
                    event_edits.add(entry)
assert event_edits == allowed

asset_files = ["Source/game/event_assets.json", "Source/game/event_cg_plan.json"]
for path in asset_files:
    assert json.loads(baseline(path)) == json.loads(current(path)), "Asset plan changed: " + path

result = {
    "baseline": BASE,
    "runtime_files_compared": len(runtime),
    "changed_runtime_files": changed,
    "slots": len(slot_labels),
    "state_writes_rewards_calls_menu_choices_preserved": True,
    "existing_condition_texts_preserved": True,
    "new_conditions_only_select_dialogue": True,
    "event_ids": len(after_event),
    "event_variants": sum(len(x) for x in after_event.values()),
    "event_beats": sum(len(bs) for vs in after_event.values() for bs in vs.values()),
    "event_fields_changed": [list(x) for x in sorted(event_edits)],
    "reserved_main_placeholders_preserved": True,
    "asset_plans_preserved": True,
    "source_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in changed + ["Source/game/event_story.json"]},
    "limits": "Text/structure comparison plus targeted native tests; not a proof of every branch combination.",
}
out = ROOT / "Source/testing/full-script-edit"
out.mkdir(parents=True, exist_ok=True)
(out / "contract.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, ensure_ascii=False))
