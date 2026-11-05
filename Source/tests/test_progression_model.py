"""Tests execute only the newly authored pure model, never repository RPY/EXE/save data."""
import ast
import copy
import importlib.util
import json
from pathlib import Path
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
GAME = ROOT / "game"
sys.path.insert(0, str(GAME))
import progression_model as pm


class RelationshipTests(unittest.TestCase):
    def test_bounds(self):
        for value, expected in [(-400, 0), (-1, 0), (0, 0), (42, 42), (100, 100), (900, 100)]:
            with self.subTest(value=value):
                self.assertEqual(pm.bounded(value), expected)

    def test_independent_deltas_and_idempotence(self):
        state, affinity = pm.initial_state(), dict.fromkeys(pm.HEROES, 50)
        untouched = copy.deepcopy((state, affinity))
        next_state, points = pm.apply_choice(state, affinity, "new-choice-1", "ria", -8, 12)
        self.assertEqual(points["ria"], 42)
        self.assertEqual(next_state["bonus"]["ria"], 12)
        self.assertEqual((state, affinity), untouched)
        self.assertEqual(pm.apply_choice(next_state, points, "new-choice-1", "ria", 90, 90), (next_state, points))
        self.assertEqual([points[w] for w in pm.HEROES[1:]], [50, 50, 50])

    def test_increase_decrease_all_heroines(self):
        for who in pm.HEROES:
            with self.subTest(who=who):
                state, points = pm.apply_choice(pm.initial_state(), {}, who + "-up", who, 150, 200)
                self.assertEqual(points[who], 100)
                self.assertEqual(pm.relation_value({}, state, who), 100)
                state, points = pm.apply_choice(state, points, who + "-down", who, -200, -300)
                self.assertEqual(points[who], 0)
                self.assertEqual(pm.relation_value({}, state, who), 0)

    def test_bad_hero_and_choice_ids(self):
        for who in ("unknown", "", None):
            with self.assertRaises(ValueError):
                pm.apply_choice(pm.initial_state(), {}, "one", who)
        with self.assertRaises(ValueError):
            pm.apply_choice(pm.initial_state(), {}, "", "ria")

    def test_ria_no_correct_rest_preference(self):
        for value in ("listen", "share", "choose_rest"):
            self.assertEqual(pm.relation_value({"ria_r06_response": value}, pm.initial_state(), "ria"), 12)

    def test_declining_intimacy_and_publicity_not_penalized(self):
        for who in pm.HEROES:
            for value in ("shared", "deferred", "talk", "private", "home", "cosplay"):
                memory = {who + "_r07_intimacy": value, who + "_publicity": value,
                          who + "_r15_outfit": value}
                self.assertEqual(pm.relation_value(memory, pm.initial_state(), who), 0)

    def test_ria_one_mistake_is_recoverable(self):
        flags = {"ria_core_understanding": True, "ria_r06_response": "listen",
                 "ria_contact_agreement": True, "ria_r09_support": "explain",
                 "ria_r13_response": "cover", "ria_r14_action_confirmed": True,
                 "ria_r15_future_agreed": True, "ria_private_teasing_mode": "stop"}
        self.assertEqual(pm.relation_value(flags, pm.initial_state(), "ria"), 80)

    def test_yujin_overstep_and_repair(self):
        state = pm.initial_state()
        bad = {"yujin_support_overstep": True}
        fixed = dict(bad, yujin_support_repair_status="resolved",
                     yujin_support_alignment_verified=True)
        self.assertLess(pm.relation_value(bad, state, "yujin"),
                        pm.relation_value(fixed, state, "yujin"))

    def test_seoyun_family_status_and_introduction_are_not_scored(self):
        state = pm.initial_state()
        before = {"seoyun_core_understanding": True, "seoyun_r02_response": "wait",
                  "seoyun_expression": "sincere_first", "seoyun_r09_support": "scope"}
        disclosed = dict(before, seoyun_family_disclosed=True,
                         seoyun_family_state="divorced_parent")
        continued = dict(disclosed, seoyun_continues_after_discussion=True,
                         seoyun_child_introduction_status="planned")
        self.assertEqual(pm.relation_value(disclosed, state, "seoyun"),
                         pm.relation_value(before, state, "seoyun"))
        self.assertEqual(pm.relation_value(disclosed, state, "seoyun"),
                         pm.relation_value(continued, state, "seoyun"))

    def test_seoyun_performed_agreement_counts_but_legacy_flags_do_not(self):
        state = pm.initial_state()
        old = {"seoyun_marriage_revealed": True,
               "seoyun_continues_after_disclosure": True,
               "seoyun_repair_performed": "old version discussion"}
        self.assertEqual(pm.relation_value(old, state, "seoyun"), 0)
        actual = dict(old, seoyun_mutual_plan_performed=True,
                      seoyun_future_boundary_confirmed=True)
        self.assertEqual(pm.relation_value(actual, state, "seoyun"), 35)

    def test_legacy_memory_and_unknown_types(self):
        self.assertEqual(pm.relation_value({"ria_r06_response": []}, pm.initial_state(), "ria"), 0)
        self.assertEqual(pm.migrate_state(None), pm.initial_state())
        self.assertEqual(pm.migrate_state({"schema": 0, "bonus": {"ria": 100}}), pm.initial_state())

    def test_json_state_roundtrip_and_branch_restore(self):
        initial, points = pm.initial_state(), {"ria": 10, "jihyun": 10}
        saved = json.dumps({"state": initial, "affinity": points, "memory": {"past": True}})
        future, future_points = pm.apply_choice(initial, points, "future", "ria", 50, 60)
        restored = json.loads(saved)
        self.assertNotIn("future", restored["state"]["ledger"])
        self.assertEqual(restored["affinity"]["ria"], 10)
        self.assertNotEqual(future, restored["state"])
        self.assertEqual(pm.migrate_state(future), future)
        # JSON roundtrip is a model test, not a claim of native Ren'Py save testing.

    def test_visits_are_immutable_and_unique(self):
        state = pm.initial_state()
        visited = pm.visit(state, "c01")
        self.assertEqual(state["visited"], [])
        self.assertEqual(pm.visit(visited, "c01")["visited"], ["c01"])


class ConditionTests(unittest.TestCase):
    def check(self, **kwargs):
        params = dict(stage="first", affinity=60, relation=30, reached=True,
                      dating=True, consent=True, proposal=True)
        params.update(kwargs)
        return pm.evaluate(**params)["eligible"]

    def test_affection_only(self):
        self.assertFalse(self.check(affinity=100, relation=0))

    def test_relation_only(self):
        self.assertFalse(self.check(affinity=0, relation=100))

    def test_both_thresholds(self):
        self.assertTrue(self.check())

    def test_story_not_reached(self):
        self.assertFalse(self.check(reached=False))

    def test_no_dating(self):
        self.assertFalse(self.check(dating=False))

    def test_no_current_consent(self):
        self.assertFalse(self.check(consent=False))

    def test_missing_flags(self):
        self.assertFalse(self.check(required_flags=("key",), flags={}))
        self.assertTrue(self.check(required_flags=("key",), flags={"key": True}))

    def test_compatibility_does_not_add_numeric_gate(self):
        self.assertTrue(self.check(affinity=0, relation=0, proposal=False))

    def test_romance_does_not_need_dating_or_relation(self):
        self.assertTrue(self.check(stage="romance", affinity=30, relation=0, dating=False, consent=False))

    def test_no_invented_true_ending(self):
        self.assertFalse(self.check(stage="true_ending", affinity=100, relation=100))

    def test_full_threshold_grid(self):
        for stage, (min_a, min_b) in pm.PROPOSAL_LIMITS.items():
            for a in range(0, 101, 10):
                for b in range(0, 101, 10):
                    with self.subTest(stage=stage, affection=a, relation=b):
                        self.assertEqual(self.check(stage=stage, affinity=a, relation=b),
                                         stage != "true_ending" and a >= min_a and b >= min_b)


class CollectionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = pm.asset_catalog(json.loads((GAME / "event_cg_plan.json").read_text(encoding="utf-8")))

    def test_catalog_unique_and_preserves_plan(self):
        self.assertEqual(len(self.catalog), 80)
        self.assertEqual(len({row["id"] for row in self.catalog}), 80)
        self.assertEqual(sum(row["stage"] == "first" and row["category"] == "adult" for row in self.catalog), 12)
        self.assertEqual(sum(row["stage"] == "special" and row["category"] == "adult" for row in self.catalog), 36)

    def test_missing_images_never_unlock(self):
        row = self.catalog[0]
        self.assertEqual(pm.observed_asset([], self.catalog, row["id"], row["path"], False), [])

    def test_only_actual_displayed_path_unlocks(self):
        row = self.catalog[0]
        self.assertEqual(pm.observed_asset([], self.catalog, row["id"], "other.png", True), [])
        self.assertEqual(pm.observed_asset([], self.catalog, "invented", row["path"], True), [])
        self.assertEqual(pm.observed_asset([], self.catalog, row["id"], row["path"], True), [row["id"]])

    def test_replay_cannot_unlock(self):
        row = self.catalog[0]
        self.assertEqual(pm.observed_asset([], self.catalog, row["id"], row["path"], True, replay=True), [])

    def test_idempotent_unlock_and_persistent_union(self):
        row = self.catalog[0]
        seen = pm.observed_asset([], self.catalog, row["id"], row["path"], True)
        self.assertEqual(pm.observed_asset(seen, self.catalog, row["id"], row["path"], True), seen)
        self.assertEqual(pm.merge_unlocked(["a"], ["b"], ["a"]), ["a", "b"])

    def test_fallback_does_not_grant_expression(self):
        base, expression = self.catalog[:2]
        seen = pm.observed_asset([], self.catalog, base["id"], base["path"], True)
        self.assertNotIn(expression["id"], seen)

    def test_empty_and_available_collection(self):
        self.assertIsNone(pm.collection(self.catalog, [], [])["percent"])
        row = self.catalog[0]
        summary = pm.collection(self.catalog, [row["id"], "invented"], [row["id"]])
        self.assertEqual(summary["percent"], 100.0)
        self.assertEqual(summary["seen"], 1)
        self.assertEqual(summary["planned"], 80)

    def test_endings_preserve_existing_ids(self):
        self.assertEqual(len(pm.ENDINGS), 9)
        self.assertEqual(pm.ENDINGS["seoyun_good"][1], "함께 고르는 다음")
        self.assertFalse(any("true" in key for key in pm.ENDINGS))


class IntegrationStaticTests(unittest.TestCase):
    def test_catalog_nodes_unique(self):
        nodes = json.loads((GAME / "progression_nodes.json").read_text(encoding="utf-8"))
        self.assertEqual(len(nodes), len({n["id"] for n in nodes}))
        self.assertEqual(sum(n["kind"] == "event" for n in nodes), 96)
        for node in nodes:
            self.assertRegex(node["id"], r"^[a-zA-Z0-9_.-]+$")

    def test_python_blocks_parse_without_execution(self):
        lines = (GAME / "progression.rpy").read_text(encoding="utf-8").splitlines()
        blocks, current = [], None
        for line in lines + ["screen sentinel():"]:
            if re.match(r"init(?: -?\d+)? python:", line):
                current = []
                blocks.append(current)
            elif current is not None:
                if line and not line.startswith("    ") and not line.startswith("#"):
                    current = None
                else:
                    current.append(line[4:] if line.startswith("    ") else "")
        for block in blocks:
            ast.parse("\n".join(block))

    def test_native_save_and_replay_contracts(self):
        source = (GAME / "progression.rpy").read_text(encoding="utf-8")
        self.assertIn('renpy.save(slot', source)
        self.assertIn('slot=True', source)
        self.assertIn('confirm=True', source)
        self.assertIn('config.after_load_callbacks.append', source)
        self.assertIn('renpy.end_replay()', source)
        self.assertNotIn('pickle', source)
        self.assertNotIn('security_keys', source)
        self.assertNotIn('renpy.jump(', source)
        self.assertNotIn('Jump(', source)

    def test_asset_recording_follows_screen_interaction(self):
        source = (GAME / "event_sequence.rpy").read_text(encoding="utf-8")
        self.assertIn('call screen event_cut(event_id, variant, event_cut_cursor)\n        $ progression_observe_cut', source)

    def test_legacy_trust_and_proposed_gates_not_replaced(self):
        core = (GAME / "core.rpy").read_text(encoding="utf-8")
        self.assertIn('default trust_ria = 0', core)
        self.assertIn('trust_ria + trust', core)
        for path in GAME.glob("*.rpy"):
            if path.name != "progression.rpy":
                self.assertNotIn("pm.evaluate", path.read_text(encoding="utf-8"))

    def test_gallery_and_model_are_read_only_on_open(self):
        source = (GAME / "progression.rpy").read_text(encoding="utf-8")
        self.assertNotIn('on "show" action Function(progression_observe', source)
        self.assertNotIn('persistent.progression_seen_assets = pm.evaluate', source)

    def test_rules_reference_real_memory_keys(self):
        source = "\n".join(p.read_text(encoding="utf-8") for p in GAME.glob("*.rpy")
                           if p.name != "progression.rpy")
        for who, rules in pm.RELATION_RULES.items():
            for key, _, _, _ in rules:
                with self.subTest(who=who, key=key):
                    self.assertIn('remember("' + key + '"', source)

if __name__ == "__main__":
    unittest.main(verbosity=2)
