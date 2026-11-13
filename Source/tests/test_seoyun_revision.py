"""Read-only story contracts. RPY is parsed as text, never executed or imported."""
import ast
import csv
import json
import re
import textwrap
import unittest
from pathlib import Path

GAME = Path(__file__).resolve().parents[1] / "game"
FILES = ("seoyun_r01_r04.rpy", "seoyun_r05_r12.rpy",
         "seoyun_r13_e01.rpy", "seoyun_optional.rpy")


def labels(source):
    matches = list(re.finditer(r"^label (\w+)(?:\([^\n]*\))?:", source, re.M))
    return {m[1]: source[m.end():matches[i+1].start() if i+1 < len(matches) else len(source)]
            for i, m in enumerate(matches)}


class SeoyunRevisionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = {name: (GAME / name).read_text(encoding="utf-8") for name in FILES}
        cls.parts = {key: value for content in cls.files.values() for key, value in labels(content).items()}

    def test_disclosure_precedes_confession_and_is_not_assumed(self):
        self.assertIn("call seoyun_family_context", self.parts["seoyun_r02"])
        r04 = self.parts["seoyun_r04"]
        self.assertLess(r04.index("call seoyun_family_context"), r04.index('$ dating = True'))
        context = self.parts["seoyun_family_context"]
        self.assertIn('if not memory.get("seoyun_family_disclosed"):', context)
        self.assertIn("이혼했어. 삼 년 됐고", context)
        self.assertNotIn("아이", context)
        self.assertIn('remember("seoyun_family_state", "divorced")', context)

    def test_old_marriage_is_not_new_story_content(self):
        story = "\n".join(self.files.values())
        for obsolete in ("married_cohabiting", "seoyun_marriage_revealed",
                         "남편하고 같은 집", "반지 케이스", "알고도 고른 다음"):
            self.assertNotIn(obsolete, story)
        self.assertNotIn("seoyun_child_met", story)
        for obsolete in ("아이 아빠", "아이랑", "아이와", "아이를", "아이한테", "돌봄"):
            self.assertNotIn(obsolete, story)

    def test_existing_event_ids_and_affection_rewards_remain(self):
        events = [f"seoyun_r{i:02}" for i in range(1, 17)] + [f"seoyun_o{i:02}" for i in range(1, 4)] + ["seoyun_e01"]
        self.assertTrue(all(event in self.parts for event in events))
        found = re.findall(r'award_once\("(seoyun_[ROE]\d+)"\s*,\s*"seoyun"\s*,\s*(\d+)\)', "\n".join(self.files.values()))
        expected = dict(zip([f"seoyun_R{i:02}" for i in range(1,17)], [4,7,8,5,4,6,0,4,6,4,0,4,0,8,5,4]))
        expected.update({"seoyun_O01": 2, "seoyun_O02": 2, "seoyun_O03": 2, "seoyun_E01": 8})
        self.assertEqual(len(found), len(expected))
        self.assertEqual({key: int(value) for key, value in found}, expected)

    def test_both_breakup_exits_stop_before_later_romance(self):
        source = self.parts["seoyun_r14"]
        lines = source.splitlines()
        exits = []
        for i, line in enumerate(lines):
            if line.strip() == "$ dating = False":
                indent = len(line) - len(line.lstrip())
                block = []
                for following in lines[i+1:]:
                    if following.strip() and len(following)-len(following.lstrip()) < indent:
                        break
                    block.append(following.strip())
                exits.append(block)
        self.assertEqual(len(exits), 2)
        for block in exits:
            self.assertIn('$ ending = "seoyun_relationship_closed"', block)
            self.assertIn("return", block)
            self.assertFalse(any("award_once" in line for line in block))
        self.assertIn('memory.get("seoyun_conflict") != "resolved"', self.parts["seoyun_r15"])

    def test_actual_discussion_precedes_repair_and_no_forced_parent_role(self):
        source = self.parts["seoyun_r14"]
        self.assertLess(source.index('약속한 수요일'), source.index('remember("seoyun_repair_performed"'))
        self.assertIn('피칭은 피칭으로만', source)
        self.assertIn('다시 만나자는 연락', source)
        epilogue = self.parts["seoyun_e01"]
        for value in ("consider_introduction", "couple_time", "discuss_life"):
            self.assertIn('"' + value + '"', epilogue)
        self.assertIn("구체적 일정은 확인 전", epilogue)

    def test_private_evening_and_next_morning_keep_real_choices(self):
        evening = self.parts["seoyun_private_evening"]
        for value in ("shared", "deferred", "talk"):
            self.assertIn('"' + value + '"', evening)
        self.assertIn('if memory.get("seoyun_r07_pace") == "shared":', self.parts["seoyun_r08"])
        self.assertIn("오늘 저녁만은 비워 두겠다고", self.parts["seoyun_r07"])
        plan = json.loads((GAME / "event_cg_plan.json").read_text(encoding="utf-8"))
        self.assertEqual(len([row for row in plan["sets"] if row["heroine"] == "seoyun"]), 4)

    def test_calls_and_progression_titles_have_real_targets(self):
        all_sources = "\n".join(p.read_text(encoding="utf-8") for p in GAME.glob("*.rpy"))
        all_labels = set(re.findall(r"^label (\w+)", all_sources, re.M))
        for content in self.files.values():
            for target in re.findall(r"^\s*call (\w+)", content, re.M):
                self.assertTrue(target == "screen" or target in all_labels, target)
        nodes = json.loads((GAME / "progression_nodes.json").read_text(encoding="utf-8"))
        self.assertEqual(sum(n["kind"] == "event" for n in nodes), 96)
        self.assertEqual(len({n["id"] for n in nodes}), len(nodes))
        for node in nodes:
            if node["heroine"] == "seoyun" and node["kind"] == "event":
                match = re.search(r'chapter = "([^"]+)"', self.parts[node["id"]])
                if match:
                    self.assertEqual(node["title"], match[1])

    def test_python_statements_and_text_literals_parse_without_execution(self):
        for name, content in self.files.items():
            for line in content.splitlines():
                stripped = line.strip()
                if stripped.startswith("$ "):
                    ast.parse(stripped[2:], filename=name)
                elif re.match(r'^(?:s|d|sn|dn)?\s*"', stripped) and not stripped.endswith(":"):
                    quoted = stripped[stripped.index('"'):]
                    ast.parse(quoted, mode="eval", filename=name)
        for name in ("progression.rpy", "office_ui.rpy"):
            lines = (GAME / name).read_text(encoding="utf-8").splitlines()
            for i, line in enumerate(lines):
                if re.fullmatch(r"init(?: -?\d+)? python:", line):
                    block = []
                    for tail in lines[i+1:]:
                        if tail.strip() and not tail.startswith((" ", "\t")):
                            break
                        block.append(tail)
                    ast.parse(textwrap.dedent("\n".join(block)), filename=name)

    def test_production_list_has_34_real_script_references(self):
        root = GAME.parents[1]
        with (root / "Docs/scene-cg-production-v001.csv").open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(len(rows), 34)
        self.assertEqual(len({r["제안파일명"] for r in rows}), 34)
        for row in rows:
            content = (root / row["대본파일"]).read_text(encoding="utf-8").splitlines()
            self.assertEqual(content[int(row["줄"])-1].strip().strip('"'), row["대본지문"])
        seoyun = [r for r in rows if r["인물"] == "한서윤"]
        self.assertEqual(len(seoyun), 8)
        self.assertTrue(all("반지" not in r["장면"] for r in seoyun))


if __name__ == "__main__":
    unittest.main(verbosity=2)
