"""Pure data rules. No engine, filesystem, network, pickle or scenario execution."""
HEROES = ("ria", "jihyun", "yujin", "seoyun")
STAT_NAMES = {"ria": "편안함", "jihyun": "존중", "yujin": "신뢰", "seoyun": "진정성"}
SCHEMA = 1
# Existing choices with equal narrative legitimacy receive equal credit.
# Declining intimacy, clothing preference, publicity and message timing are not scored.
RELATION_RULES = {
    "ria": (
        ("ria_core_understanding", "present", {}, 15),
        ("ria_r06_response", "value", {"listen": 12, "share": 12, "choose_rest": 12}, 0),
        ("ria_contact_agreement", "present", {}, 10),
        ("ria_r09_support", "value", {"explain": 12, "organize": 12, "rehearse": 12}, 0),
        ("ria_r13_response", "value", {"honest": 8, "ask": 8, "cover": -8}, 0),
        ("ria_r14_action_confirmed", "present", {}, 25),
        ("ria_r15_future_agreed", "present", {}, 10),
        ("ria_private_teasing_mode", "value", {"comfortable": 4, "light": 4, "stop": 4}, 0),
    ),
    "jihyun": (
        ("jihyun_core_understanding", "present", {}, 15),
        ("jihyun_r03_response", "value", {"reason": 10, "share_check": 10, "attitude": 10}, 0),
        ("jihyun_affection_scope", "value", {"hand_and_check": 15, "private_place": 15, "say_each_time": 15}, 0),
        ("jihyun_r09_support", "value", {"evidence": 15, "share": 15, "reader": 15}, 0),
        ("jihyun_r13_response", "value", {"reasons": 10, "roles": 10, "pause_then_return": 10}, 0),
        ("jihyun_r14_performed", "present", {}, 25),
        ("jihyun_future_promise", "present", {}, 10),
    ),
    "yujin": (
        ("yujin_core_understanding", "present", {}, 15),
        ("yujin_r03_response", "value", {"intent": 10, "impression": 10, "compare": 10}, 0),
        ("yujin_r06_expression", "value", {"both_initiate": 15, "think_first": 15, "take_turns": 15}, 0),
        ("yujin_support_overstep", "value", {True: -15, False: 15}, 0),
        ("yujin_r13_agreed_scope", "present", {}, 10),
        ("yujin_support_alignment_verified", "present", {}, 25),
        ("yujin_support_repair_status", "value", {"resolved": 15}, 0),
        ("yujin_r15_future", "present", {}, 10),
    ),
    "seoyun": (
        ("seoyun_core_understanding", "present", {}, 15),
        ("seoyun_r02_response", "value", {"wait": 10, "my_interest": 10, "unfinished": 10}, 0),
        ("seoyun_expression", "value", {"sincere_first": 15, "quiet_public": 15, "say_each_time": 15}, 0),
        ("seoyun_r09_support", "value", {"scope": 10, "roles": 10, "reader": 10}, 0),
        # Being divorced or having a child never reduces relationship value.
        # Only conversations and performed agreements count, not introduction promises.
        ("seoyun_mutual_plan_performed", "present", {}, 25),
        ("seoyun_future_boundary_confirmed", "present", {}, 10),
    ),
}
PROPOSAL_LIMITS = {"romance": (30, 0), "first": (60, 30),
                   "special": (80, 70), "true_ending": (90, 85)}
ENDINGS = {"colleague": ("common", "좋은 동료로, 우리"),
           "ria_good": ("ria", "리아 · 본편 결말"),
           "jihyun_good": ("jihyun", "지현 · 본편 결말"),
           "yujin_good": ("yujin", "유진 · 본편 결말"),
           "seoyun_good": ("seoyun", "함께 고르는 다음")}
for _who in HEROES:
    ENDINGS[_who + "_relationship_closed"] = (_who, "관계를 여기서 마침")


def bounded(value):
    return max(0, min(100, int(value)))


def check_hero(who):
    if who not in HEROES:
        raise ValueError("Unknown heroine: " + str(who))


def initial_state():
    return {"schema": SCHEMA, "bonus": {who: 0 for who in HEROES},
            "ledger": [], "visited": [], "current": None}


def relation_evidence(memory, who):
    check_hero(who)
    rows = []
    for key, kind, values, amount in RELATION_RULES[who]:
        if key not in memory:
            continue
        value = memory[key]
        delta = amount if kind == "present" and bool(value) else 0
        if kind == "value":
            # Guard against arbitrary unhashable legacy values.
            delta = next((n for v, n in values.items()
                          if type(value) is type(v) and value == v), 0)
        if delta:
            rows.append((key, delta))
    return rows


def relation_value(memory, state, who):
    return bounded(sum(row[1] for row in relation_evidence(memory, who))
                   + state.get("bonus", {}).get(who, 0))


def relation_phase(value):
    value = bounded(value)
    if value < 25:
        return "조심스럽게 알아 가는 중"
    if value < 50:
        return "마음을 표현하는 중"
    if value < 75:
        return "서로를 이해하는 중"
    return "차곡차곡 깊어지는 중"


def apply_choice(state, affinity, choice_id, who, affection_delta=0, relation_delta=0):
    """One authored effect per choice ID; rollback must restore BOTH returned roots."""
    check_hero(who)
    if not isinstance(choice_id, str) or not choice_id:
        raise ValueError("Stable nonempty choice ID required")
    if choice_id in state.get("ledger", []):
        return state, affinity
    result = dict(state)
    result["bonus"] = dict(state.get("bonus", {}))
    result["bonus"][who] = max(-100, min(100, result["bonus"].get(who, 0) + int(relation_delta)))
    result["ledger"] = list(state.get("ledger", [])) + [choice_id]
    points = dict(affinity)
    points[who] = bounded(points.get(who, 0) + affection_delta)
    return result, points


def visit(state, node_id):
    result = dict(state)
    result["current"] = node_id
    result["visited"] = list(dict.fromkeys(list(state.get("visited", [])) + [node_id]))
    return result


def evaluate(stage, affinity, relation, reached=False, dating=False, consent=False,
             required_flags=(), flags=None, proposal=False):
    """Eligibility is not an unlock. Proposed numeric limits are diagnostic only."""
    if stage not in PROPOSAL_LIMITS:
        raise ValueError("Unknown stage")
    reasons = []
    if not reached:
        reasons.append("이야기 진행 필요")
    if stage != "romance" and not dating:
        reasons.append("교제 확인 필요")
    if stage in ("first", "special") and not consent:
        reasons.append("이번 장면의 진행 선택 필요")
    for flag in required_flags:
        if not (flags or {}).get(flag):
            reasons.append("주요 선택 확인 필요: " + flag)
    if proposal:
        a, b = PROPOSAL_LIMITS[stage]
        if affinity < a:
            reasons.append("호감도 기준 미충족")
        if relation < b:
            reasons.append("관계 수치 기준 미충족")
    # No new true ending exists in the approved script.
    if stage == "true_ending":
        reasons.append("진엔딩 대본·CG 미제작")
    return {"eligible": not reasons, "reasons": reasons, "proposal": bool(proposal)}


def asset_catalog(plan):
    rows = []
    for group in plan["sets"]:
        event_id = group["heroine"] + "_" + group["event"].lower()
        for asset in [group["intro_cg"], group["intro_expression"]] + group["base_cg"]:
            category = "romance" if asset["id"] in (group["intro_cg"]["id"], group["intro_expression"]["id"]) else "adult"
            rows.append({"id": asset["id"], "heroine": group["heroine"],
                         "event_id": event_id, "outfit": group["outfit"],
                         "category": category, "path": asset["planned_path"],
                         "stage": "first" if group["event"] == "R07" else "special"})
    return rows


def observed_asset(seen, catalog, asset_id, displayed_path, ready, replay=False):
    """Call after the displayed screen was acknowledged; never on eligibility."""
    item = next((row for row in catalog if row["id"] == asset_id), None)
    if replay or not ready or not item or displayed_path != item["path"]:
        return list(seen)
    return list(dict.fromkeys(list(seen) + [asset_id]))


def collection(catalog, seen, ready_ids):
    available = {row["id"] for row in catalog if row["id"] in ready_ids}
    earned = available.intersection(seen)
    return {"seen": len(earned), "available": len(available), "planned": len(catalog),
            "percent": round(100.0 * len(earned) / len(available), 1) if available else None}


def migrate_state(state):
    """Old saves start with no invented choices, CG or endings; preserve valid v1."""
    if not isinstance(state, dict) or state.get("schema") != SCHEMA:
        return initial_state()
    result = initial_state()
    result["bonus"] = {who: max(-100, min(100, int(state.get("bonus", {}).get(who, 0)))) for who in HEROES}
    result["ledger"] = list(state.get("ledger", []))
    result["visited"] = list(state.get("visited", []))
    result["current"] = state.get("current")
    return result


def merge_unlocked(old, new, current):
    return sorted(set(old or []).union(new or [], current or []))

