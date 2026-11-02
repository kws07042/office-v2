"""Static story/state comparison; never imports or executes the game."""
import ast
from collections import Counter
import hashlib
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = "44ba86ad5aa7cef83d68abd0be261964df74a937"
LOCAL = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8")) if len(sys.argv) == 2 else None

def baseline(path):
    if LOCAL is not None:
        return LOCAL[path].replace("\r\n", "\n")
    return subprocess.check_output(["git", "show", BASE + ":" + path], cwd=ROOT).decode("utf-8").replace("\r\n", "\n")

def current(path):
    return (ROOT / path).read_text(encoding="utf-8").replace("\r\n", "\n")

def signature(text):
    state, calls, menus, conditions, definitions = [], [], [], [], []
    for row in text.splitlines():
        line = row.strip()
        if line.startswith("$ ") and not re.match(r"\$ (?:location|chapter)\s*=", line):
            state.append(line)
        if line.startswith("call phone_deliver("):
            node = ast.parse(line.removeprefix("call "), mode="eval")
            node.body.args[2] = ast.Constant(value="<dialogue>")
            calls.append(ast.dump(node, include_attributes=False))
        elif line.startswith(("call ", "jump ", "return", "while ", "label ", "default ")):
            calls.append(line)
        if line.startswith('"') and line.endswith(":"):
            menus.append(line)
        if line.startswith(("if ", "elif ")):
            conditions.append(line)
        if line.startswith("define "):
            definitions.append(line)
    return state, calls, menus, conditions, definitions

allowed = {
    "Source/game/yujin_r13_e01.rpy",
    "Source/game/seoyun_r13_e01.rpy",
    "Source/game/jihyun_r05_r12.rpy",
    "Source/game/jihyun_r13_e01.rpy",
    "Source/game/ria_r13_e01.rpy",
    "Source/game/yujin_optional.rpy",
    "Source/game/options.rpy",
}
runtime, changed, labels = [], [], []
for f in sorted((ROOT / "Source/game").glob("*.rpy")):
    if f.name.endswith("_tests.rpy") or f.name == "testcases.rpy":
        continue
    path = f.relative_to(ROOT).as_posix()
    before, after = baseline(path), current(path)
    if before != after:
        assert path in allowed, "Unreviewed runtime file: " + path
        changed.append(path)
    b, a = signature(before), signature(after)
    if path.endswith("options.rpy"):
        assert after.replace("0.35.2-player-flow", "<VERSION>") == before.replace("0.35.1-full-script-edit", "<VERSION>")
    elif path.endswith("yujin_r13_e01.rpy"):
        for label in ("yujin_r13", "yujin_r15", "yujin_r16", "yujin_e01"):
            pattern = r"(?ms)^label " + label + r":.*?(?=^label |\Z)"
            assert re.search(pattern, before).group() == re.search(pattern, after).group(), label
        expected = Counter(b[0])
        expected['$ remember("yujin_r14_readiness", "reconsidered")'] -= 1
        expected['$ remember("yujin_r14_readiness", "relationship_talk")'] += 1
        expected['$ remember("yujin_r14_readiness", "reassured")'] += 1
        assert +expected == Counter(a[0]), "Unexpected relationship state/reward change"
        assert Counter(b[1]) == Counter(a[1]), "Call/jump/return changed"
        assert b[4] == a[4]
        r14 = r"(?ms)^label yujin_r14:.*?(?=^label |\\Z)"
        assert signature(re.search(r14, before).group())[3][0] == signature(re.search(r14, after).group())[3][0], "R14 route guard changed"
        assert after.count("    menu:") == before.count("    menu:")
    else:
        assert b[0] == a[0], "State/reward writes changed: " + path
        assert b[1] == a[1], "Calls changed: " + path
        assert b[3:] == a[3:], "Conditions/definitions changed: " + path
        if path.endswith("yujin_optional.rpy"):
            for label in ("yujin_o01_offer", "yujin_o01", "yujin_o02_offer", "yujin_o03_offer", "yujin_o03"):
                pattern = r"(?ms)^label " + label + r":.*?(?=^label |\Z)"
                assert re.search(pattern, before).group() == re.search(pattern, after).group(), label
            assert len(b[2]) == len(a[2])
        else:
            assert b[2] == a[2], "Unreviewed menu change: " + path
    assert before.count("(거사 — 장면 생략)") == after.count("(거사 — 장면 생략)")
    old_labels = re.findall(r"(?m)^label (\w+)", before)
    new_labels = re.findall(r"(?m)^label (\w+)", after)
    assert old_labels == new_labels, "Save jump label changed: " + path
    labels += re.findall(r"^label ((?:c\d\d|(?:ria|jihyun|yujin|seoyun)_(?:r\d\d|o\d\d|e01)|work_(?:verify|coord|test)\d\d|end_common))(?=[:(])", after, re.M)
    runtime.append(path)
assert set(changed) == allowed
assert len(labels) == len(set(labels)) == 95
for path in ("Source/game/event_story.json", "Source/game/event_assets.json", "Source/game/event_cg_plan.json"):
    assert json.loads(baseline(path)) == json.loads(current(path)), path

print(json.dumps({
    "baseline": BASE,
    "runtime_files": len(runtime),
    "changed_runtime_files": changed,
    "slots": len(labels),
    "labels_and_route_guards_preserved": True,
    "non_yujin_state_writes_and_rewards_preserved": True,
    "yujin_r14_state_delta": "Adds relationship_talk/reassured readiness; removes newly-produced reconsidered. Closure and continuation rewards unchanged.",
    "yujin_r14_control_flow": "Reviewed change: relationship choice moves after work. Native tests verify order, both histories, closure/continuation and save/load.",
    "reserved_scene_text_and_assets_unchanged": True,
    "source_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in changed},
    "limits": "Structure/state checks do not measure entertainment or prove every combination. Existing saves inside rewritten statements need platform play verification.",
}, ensure_ascii=False))
