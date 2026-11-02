# Player-flow regression tests. Development only; excluded from game builds.
init python:
    flow_case = 0

label test_flow_yujin:
    scene bg plain
    $ active_route = "yujin"
    $ dating = True
    $ affinity = {n: 17 for n in ("ria", "jihyun", "yujin", "seoyun")}
    $ completed = []
    $ memory = {"yujin_r13_agreed_scope": True, "yujin_r13_support_plan": "slides", "yujin_support_action": "self_summary" if flow_case >= 3 else "materials", "yujin_support_overstep": flow_case >= 3}
    $ _history_list = []
    call yujin_r14
    menu:
        "흐름 검사 종료":
            pass
    return

label test_flow_seoyun:
    scene bg plain
    $ active_route = "seoyun"
    $ dating = True
    $ completed = []
    $ affinity = {n: 17 for n in ("ria", "jihyun", "yujin", "seoyun")}
    $ memory = {"seoyun_conflict": "resolved", "seoyun_marriage_state": "married_cohabiting", "seoyun_marriage_revealed": True, "seoyun_trust_status": "damaged_not_restored"}
    $ _history_list = []
    call seoyun_r15
    menu:
        "흐름 검사 종료":
            pass
    return

label test_flow_yujin_sketch:
    scene bg plain
    $ active_route = "yujin"
    $ dating = True
    $ completed = []
    $ affinity = {n: 17 for n in ("ria", "jihyun", "yujin", "seoyun")}
    $ memory = {}
    $ _history_list = []
    call yujin_o02_offer
    menu:
        "흐름 검사 종료":
            pass
    return

testsuite player_flow_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase relationship_decision_waits_until_after_work:
        parameter case = list(range(6))
        $ flow_case = case
        run Start("test_flow_yujin")
        advance until screen "choice"
        assert eval "검토 직전" in location
        assert eval not any("연애를 마치" in renpy.substitute(i.caption) for i in renpy.get_screen("choice").scope["items"])
        assert eval "끝내자는 말" not in polish_history()
        click expression yujin_test_choice(2)
        advance until screen "choice"
        assert eval "퇴근 후" in location
        assert eval dating and not memory.get("yujin_relationship_closed")
        assert eval "첫 질문이 나왔다" in polish_history()
        assert eval "시안 아래에는 유진의 이름이 남았다" in polish_history()
        assert eval not memory.get("yujin_support_alignment_verified")
        click expression yujin_test_choice(case % 3)
        advance until screen "choice"
        assert eval dating == (case % 3 != 0)
        assert eval memory.get("yujin_relationship_closed", False) == (case % 3 == 0)
        assert eval ("yujin_R14" in completed) == (case % 3 != 0)
        assert eval affinity["yujin"] == (17 if case % 3 == 0 else 25)
        assert eval all(affinity[n] == 17 for n in ("ria", "jihyun", "seoyun"))
        if eval case % 3 == 0:
            assert eval ending == "yujin_relationship_closed"
            assert eval not memory.get("yujin_r14_complete")
            assert eval not memory.get("yujin_support_repair_action_verified")
        else:
            assert eval memory.get("yujin_r14_complete") and memory.get("yujin_r14_relationship_talk_completed")
            assert eval memory["yujin_r14_readiness"] == ("reassured" if case % 3 == 1 else "talk_after")
            assert eval bool(memory.get("yujin_support_repair_action_verified")) == (case >= 3)
            assert eval ("전에 제가 먼저 설명했던 일" in polish_history()) == (case == 5)
            assert eval ("보여 드릴 게 있어야 만나자고" in polish_history()) == (case == 2)
            assert eval "끝이라고 했다가 바꾸시면" not in polish_history()
        if eval case == 1:
            screenshot "flow-yujin-affection.png"

    testcase load_restores_work_and_relationship_decisions:
        $ flow_case = 0
        run Start("test_flow_yujin")
        advance until screen "choice"
        run FileSave("flow-before-r14", confirm=False)
        click expression yujin_test_choice(2)
        advance until screen "choice"
        run FileSave("flow-after-work", confirm=False)
        click expression yujin_test_choice(0)
        advance until screen "choice"
        assert eval not dating and affinity["yujin"] == 17
        run FileLoad("flow-after-work", confirm=False)
        assert screen "choice" timeout 10.0
        assert eval dating and not memory.get("yujin_relationship_closed")
        assert eval "퇴근 후" in location
        click expression yujin_test_choice(1)
        advance until screen "choice"
        assert eval dating and affinity["yujin"] == 25
        assert eval completed.count("yujin_R14") == 1
        run FileLoad("flow-before-r14", confirm=False)
        assert screen "choice" timeout 10.0
        assert eval dating and affinity["yujin"] == 17 and not completed
        assert eval "검토 직전" in location
        click expression yujin_test_choice(0)
        advance until screen "choice"
        assert eval memory["yujin_r14_readiness"] == "ready"
        assert eval "버스 한 대는 놓치셔야겠어요" not in polish_history()
        assert eval completed.count("yujin_R14") == 1 and affinity["yujin"] == 25

    testcase disclosure_stays_true_across_all_private_paces:
        parameter case = list(range(3))
        $ flow_case = case
        run Start("test_flow_seoyun")
        advance until screen "choice"
        assert eval "오는 길엔 몇 번 돌아갈까" in polish_history()
        assert eval "한 입을 덜었다" in polish_history()
        assert eval "한 입 바꿀래" in polish_history()
        assert eval "교환 조건이 생겼네" not in polish_history()
        click expression yujin_test_choice(case)
        advance until screen "choice"
        click expression yujin_test_choice(case)
        advance until screen "choice"
        assert eval memory["seoyun_r15_outfit"] == ("cosplay" if case == 1 else "home")
        assert eval "오늘 저녁 내내 불편하기만 했던 건 아니에요" in polish_history()
        if eval case == 0:
            screenshot "flow-seoyun-still-uncertain.png"
        click expression yujin_test_choice(case)
        if eval case == 0:
            advance until screen "event_cut"
            assert eval renpy.get_screen("event_cut").scope["event_id"] == "seoyun_r15"
            click id "cut_skip" until not screen "event_cut"
        advance until screen "choice"
        assert eval dating and memory["seoyun_marriage_state"] == "married_cohabiting"
        assert eval memory["seoyun_r15_pace"] == ["shared", "deferred", "talk"][case]
        assert eval completed.count("seoyun_R15") == 1
        assert eval memory["seoyun_marriage_revealed"] and memory["seoyun_trust_status"] == "damaged_not_restored"

    testcase optional_sketch_actions_keep_their_own_memory:
        parameter case = list(range(3))
        run Start("test_flow_yujin_sketch")
        advance until screen "choice"
        click expression yujin_test_choice(0)
        advance until screen "choice"
        click expression yujin_test_choice(case)
        advance until screen "choice"
        assert eval memory["yujin_o02_impression"] == ["overlapping_light", "stopped_before_drinking", "drawing_and_photo"][case]
        assert eval memory["yujin_o02_subject"] == "창가 빛이 겹친 작은 컵"
        assert eval memory["yujin_o02_status"] == "completed" and completed == ["yujin_O02"]
        assert eval affinity["yujin"] == 19
        assert eval ("그림도 밤 됐어요" in polish_history()) == (case == 0)
        assert eval ("오리 같은데요" in polish_history()) == (case == 1)
        assert eval ("손잡이가 더 잘생겼어요" in polish_history()) == (case == 2)
        if eval case == 1:
            screenshot "flow-yujin-duck-cup.png"

    testcase skipping_sketch_does_not_invent_a_drawing:
        run Start("test_flow_yujin_sketch")
        advance until screen "choice"
        click expression yujin_test_choice(1)
        advance until screen "choice"
        assert eval memory["yujin_o02_status"] == "skipped"
        assert eval "yujin_o02_impression" not in memory and "yujin_o02_subject" not in memory
        assert eval not completed and affinity["yujin"] == 17
        assert eval "오리 같은데요" not in polish_history()

    teardown:
        exit
