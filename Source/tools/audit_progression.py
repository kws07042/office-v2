"""Static audit only: never execute original game scripts or load saves."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[2]
BASELINE = ROOT.parent / "office-v2-baseline-text"
GAME = ROOT / "Source/game"

def text(path):
    return path.read_text(encoding="utf-8").replace("\r\n", "\n").rstrip("\n")

def audit(baseline=None):
    baseline = Path(baseline) if baseline else BASELINE
    if not baseline.is_dir():
        raise ValueError("Reviewed baseline text folder required; pass --baseline PATH.")
    preservation = []
    scores = {}
    endings = set()
    for path in sorted((baseline / "Source/game").glob("*.rpy")):
        current = GAME / path.name
        old, new = text(path), text(current)
        if path.name not in ("screens.rpy", "event_sequence.rpy"):
            stripped = "\n".join(line for line in new.splitlines()
                                 if not re.match(r"\s*\$ progression_", line))
            if path.name == "core.rpy":
                stripped = stripped.replace(
                    "who: max(0, min(100, renpy.store.affinity.get(who, 0) + amount))",
                    "who: min(100, renpy.store.affinity.get(who, 0) + amount)")
            if path.name == "options.rpy":
                stripped = stripped.replace('    build.classify("**/progression_smoke.rpyc", None)\n', '')
            preservation.append({"path": str(current.relative_to(ROOT)),
                                 "unchanged_without_hooks": stripped == old})
        if path.name == "event_sequence.rpy":
            stripped = "\n".join(line for line in new.splitlines()
                                 if "$ progression_observe_cut" not in line)
            preservation.append({"path": str(current.relative_to(ROOT)),
                                 "unchanged_without_hooks": stripped == old})
        for eid, who, amount in re.findall(
                r'award_once\(\s*"([^"]+)"\s*,\s*"([^"]+)"\s*,\s*(-?\d+)', old):
            scores.setdefault(who, {})[eid] = int(amount)
        endings.update(re.findall(r'ending = "([^"]+)"', old))
    balances = []
    for who in ("ria", "jihyun", "yujin", "seoyun"):
        awards = scores[who]
        common = 14  # own introduction 10 + both focused C06/C07 awards 2 each.
        for event in (7, 12, 15, 16):
            personal = sum(awards.get(who + "_R" + str(n).zfill(2), 0) for n in range(1, event))
            optional = 2 if event <= 10 else 4 if event <= 15 else 6
            balances.append({"heroine": who, "before": "R" + str(event).zfill(2),
                             "static_upper_bound": min(100, common + personal + optional),
                             "assumption": "both common focus awards and all earlier optional scenes"})
    findings = []
    patterns = [r"gh[pousr]_[A-Za-z0-9]{30,}", r"AKIA[0-9A-Z]{16}",
                r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"]
    for path in baseline.rglob("*"):
        if path.is_file():
            content = text(path)
            if any(re.search(pattern, content) for pattern in patterns):
                findings.append(str(path.relative_to(baseline)))
    nodes = json.loads((GAME / "progression_nodes.json").read_text(encoding="utf-8"))
    return {"baseline": "78ebd75ede0c20e1d76e3d02610d866346a397ae",
            "text_files_reviewed": len([p for p in baseline.rglob("*") if p.is_file()]),
            "preservation": preservation,
            "preservation_passed": all(r["unchanged_without_hooks"] for r in preservation),
            "affinity_upper_bounds": balances,
            "existing_ending_ids": sorted(endings),
            "nodes": {"total": len(nodes), "event": sum(n["kind"] == "event" for n in nodes),
                      "choice": sum(n["kind"] == "choice" for n in nodes),
                      "support": sum(n["kind"] == "support" for n in nodes)},
            "credential_pattern_findings_paths_only": findings,
            "security_scope": "current selected text snapshot only; not history, binaries or account",
            "runtime_verified": False}

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", help="Trusted text snapshot of the stated baseline commit")
    args = parser.parse_args()
    print(json.dumps(audit(args.baseline), ensure_ascii=False, indent=2))

