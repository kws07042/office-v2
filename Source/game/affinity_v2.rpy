# 호감도 v2 — 마음과 신뢰 (Docs/affinity-v2-design.md)
# 기존 affinity(장마다 쌓이는 기본 점수)는 그대로 두고, 선택 기록(memory)에서 신뢰와 마음 보정을 계산한다.
# 하트 숫자 = 마음(기본 점수 + 보정), 하트 테두리 = 신뢰(금색 / 보통 / 흐린 점선).

init -1 python:
    BOND_TRUST_RULES = {
        "ria": [
            ("ria_r06_response", {"listen": 2, "choose_rest": 1}),
            ("ria_r09_support", {"rehearse": 2, "organize": -1}),
            ("ria_r13_response", {"honest": 2, "ask": -1, "cover": -2}),
            ("ria_r14_clarification", {"both": 2}),
        ],
        "jihyun": [
            ("jihyun_r03_response", {"reason": 1}),
            ("jihyun_next_date_plan", {"both_suggest": 1, "dohyun_suggests": -1}),
            ("x_jihyun_r08_hour", {"ask": 1}),
            ("jihyun_r09_support", {"evidence": 2, "reader": -1}),
            ("jihyun_r13_response", {"reasons": 2, "roles": 2}),
            ("jihyun_r14_choice", {"ready": 2, "repair_after_blunt": -2, "wait_for_action": -1, "reconsidered": -2}),
        ],
        "yujin": [
            ("yujin_r03_response", {"intent": 2}),
            ("yujin_r06_expression", {"think_first": 1}),
            ("yujin_support_action", {"agreed_summary": 2, "materials": 1, "self_summary": -2}),
            ("yujin_support_repair_status", {"resolved": 1, "open": -1}),
            ("yujin_r13_support_plan", {"slides": 2, "requested_summary": 1}),
            ("yujin_r14_readiness", {"reassured": 1}),
        ],
        "seoyun": [
            ("seoyun_r02_response", {"wait": 1}),
            ("seoyun_r03_meaning", {"meet_you": 1}),
            ("seoyun_expression", {"sincere_first": 2}),
            ("seoyun_r09_support", {"reader": 1}),
            ("seoyun_r13_response", {"unknown": 2, "weight": -1}),
            ("seoyun_r14_choice", {"ready": 2, "wait_action": -1, "reconsidered": -2}),
        ],
    }

    def bond_trust(who):
        mem = renpy.store.memory
        score = 0
        for key, table in BOND_TRUST_RULES.get(who, []):
            if key in mem:
                score += table.get(mem[key], 0)
        if who == "ria" and mem.get("ria_r14_relationship_choice") == "reconsidered":
            score -= 2
        return max(-10, min(12, score))

    def bond_mind_bonus(who):
        mem = renpy.store.memory
        score = 0
        for part in ("o01", "o02", "o03"):
            score += {"completed": 2, "brief": 1, "skipped": -1}.get(mem.get(who + "_" + part + "_status"), 0)
        score += sum(1 for n in (1, 2, 3) if mem.get("x_sched_%d" % n) == who)
        return score

    def bond_mind(who):
        return max(0, min(100, renpy.store.affinity.get(who, 0) + bond_mind_bonus(who)))

    def bond_trust_tier(who):
        t = bond_trust(who)
        return "gold" if t >= 6 else ("low" if t < 0 else "normal")

    def relation_stage(who):
        # 화면에 보이는 관계 단계. 기본 판단(cream_relation_name)을 존중하고 그 위에 세분화한다.
        base = cream_relation_name(who)
        if base in ("다시 마주 보는 중", "동료로 지내는 중"):
            return base
        t = bond_trust(who)
        if base == "교제 중":
            if t < 0:
                return "엇갈리는 중"
            if t >= 10 and (who + "_R15") in renpy.store.completed:
                return "미래를 말하는 사이"
            if t >= 6:
                return "서로 기대는 사이"
            return "교제 중"
        mind = bond_mind(who)
        if mind >= 40:
            return "설레는 사이"
        if mind >= 25:
            return "신경 쓰이는 사람"
        return base

    # 신뢰가 떨어지거나 크게 오르는 순간을 하트 연출로 알린다.
    def bond_watch():
        st = renpy.store
        who = getattr(st, "active_route", None) or getattr(st, "cream_focus", None)
        if who not in BOND_TRUST_RULES:
            return
        now = bond_trust(who)
        seen = dict(getattr(st, "bond_last_trust", None) or {})
        before = seen.get(who)
        seen[who] = now
        st.bond_last_trust = seen
        if before is None or renpy.is_in_test():
            return
        if now < before:
            renpy.show_screen("bond_flash", kind="drop", _tag="bond_flash")
        elif now >= before + 2:
            renpy.show_screen("bond_flash", kind="rise", _tag="bond_flash")

    config.start_interact_callbacks.append(bond_watch)

default bond_last_trust = {}

screen bond_flash(kind):
    timer 0.9 action Hide("bond_flash")

transform bond_shake:
    xoffset 0
    linear 0.06 xoffset -3
    linear 0.06 xoffset 3
    linear 0.06 xoffset -2
    linear 0.06 xoffset 2
    linear 0.06 xoffset 0
