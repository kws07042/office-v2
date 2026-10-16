init python:
    import json
    import ast
    import re
    with renpy.file("three_choice_cases.json") as choice_case_file:
        choice_cases = json.load(choice_case_file)
    choice_fixture = {}

    def choice_target_visible():
        screen = renpy.get_screen("choice")
        return screen and any(renpy.substitute(i.caption) == choice_case["new_option"][1:-2] for i in screen.scope["items"])

    def choice_first_caption():
        return renpy.substitute(renpy.get_screen("choice").scope["items"][0].caption)

    def choice_added_dialogue_was_read():
        for line in choice_case["new_dialogue"]:
            matched = re.fullmatch(r'\s*(?:d|r|j|y|s|msgd|msgr) (".*")', line)
            if matched:
                expected = renpy.substitute(ast.literal_eval(matched.group(1)))
                return any(h.what == expected for h in renpy.store._history_list)
        return False

label test_three_choice_entry:
    scene bg plain
    $ choice_case = choice_cases[choice_fixture["case"] // 2]
    $ speech_informal = bool(choice_fixture["case"] & 1)
    $ active_route = "ria"
    $ dating = choice_case["label"] != "ria_r04"
    $ affinity = {"ria": 0, "jihyun": 0, "yujin": 0, "seoyun": 0}
    $ completed = ["ria_R%02d" % i for i in range(1,17)]
    $ memory = {"ria_core_understanding": True, "ria_confession_accepted": True, "ria_conflict": "discussing" if choice_case["label"] == "ria_r14" else "resolved", "ria_r13_response": "cover", "ria_r15_future_agreed": True, "ria_route_completed": True, "ria_r12_next_appointment_status": "scheduled"}
    call expression choice_case["label"]
    $ remember("choice_test_returned")
    menu:
        "선택지 검사 종료":
            pass
    return

testsuite three_choice_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase every_new_choice_both_speech_styles:
        parameter case = [i for i in range(64) if i not in (28, 29)]
        $ choice_fixture["case"] = case
        run Start("test_three_choice_entry")
        advance until screen "choice"
        if not eval choice_target_visible():
            click expression choice_first_caption() until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
        if not eval choice_target_visible():
            click expression choice_first_caption() until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
        if not eval choice_target_visible():
            click expression choice_first_caption() until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
        if not eval choice_target_visible():
            click expression choice_first_caption() until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
        assert eval choice_target_visible()
        assert eval len(renpy.get_screen("choice").scope["items"]) == 3
        if eval case in (0, 16, 46):
            pause 0.1
            screenshot ("three-choice-" + str(case) + ".png")
        click expression choice_case["new_option"][1:-2] until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        assert eval memory.get("choice_third_" + choice_case["key"]) is True
        if not eval memory.get("choice_test_returned"):
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
            if not eval memory.get("choice_test_returned"):
                click expression choice_first_caption() until not screen "choice"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if not eval memory.get("choice_test_returned"):
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
            if not eval memory.get("choice_test_returned"):
                click expression choice_first_caption() until not screen "choice"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if not eval memory.get("choice_test_returned"):
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
            if not eval memory.get("choice_test_returned"):
                click expression choice_first_caption() until not screen "choice"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if not eval memory.get("choice_test_returned"):
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
            if not eval memory.get("choice_test_returned"):
                click expression choice_first_caption() until not screen "choice"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if not eval memory.get("choice_test_returned"):
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
            if not eval memory.get("choice_test_returned"):
                click expression choice_first_caption() until not screen "choice"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if not eval memory.get("choice_test_returned"):
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
            if not eval memory.get("choice_test_returned"):
                click expression choice_first_caption() until not screen "choice"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if not eval memory.get("choice_test_returned"):
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
            if not eval memory.get("choice_test_returned"):
                click expression choice_first_caption() until not screen "choice"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if not eval memory.get("choice_test_returned"):
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
            if not eval memory.get("choice_test_returned"):
                click expression choice_first_caption() until not screen "choice"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        assert eval memory.get("choice_test_returned") is True
        assert eval choice_added_dialogue_was_read()
        assert eval dating is True
        assert eval ending != "ria_relationship_closed"
        if eval choice_case["key"] in ("o01_offer", "o02_offer", "o03_offer"):
            assert eval memory["ria_" + choice_case["key"][:3] + "_status"] == "brief"
            assert eval "ria_" + choice_case["key"][:3].upper() not in completed
        if eval choice_case["key"] in ("r04_affection", "r06_affection"):
            assert eval first_kiss is False
        if eval choice_case["key"] in ("r07_pace", "r12_pace", "r15_pace"):
            assert eval memory["ria_" + choice_case["key"][:3] + "_intimacy"] == "deferred"
            assert eval event_presentations == {}
        if eval choice_case["key"] == "r14_relationship":
            assert eval memory["ria_conflict"] == "resolved"
            assert eval memory["ria_r14_action_confirmed"] is True

    teardown:
        exit
