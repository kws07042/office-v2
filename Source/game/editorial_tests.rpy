init python:
    editorial_fixture = {}

    def editorial_history():
        return "\n".join(renpy.substitute(h.what) for h in _history_list)

label test_editorial_entry:
    $ active_route = "ria"
    $ dating = True
    $ speech_informal = editorial_fixture.get("informal", True)
    $ memory = {"ria_conflict":"resolved", "ria_route_completed":True, "ria_confession_accepted":True, "ria_r15_future_agreed":True}
    $ completed = ["ria_R13", "ria_R14", "ria_R15", "ria_R16"]
    $ affinity = {"ria":60, "jihyun":0, "yujin":0, "seoyun":0}
    if editorial_fixture["scene"] == "r02":
        $ afterwork_preference = "quiet"
        call ria_r02
    elif editorial_fixture["scene"] == "r14":
        $ remember("ria_conflict", "discussing")
        $ remember("ria_r13_response", "notice")
        call ria_r14
    elif editorial_fixture["scene"] == "r15":
        $ remember("ria_r10_place", "park")
        call ria_r15
    else:
        if editorial_fixture.get("rest"):
            $ remember("ria_o03_status", "completed")
            $ remember("ria_o03_rest", editorial_fixture["rest"])
        call ria_e01
    $ remember("editorial_test_done")
    menu:
        "검사 종료":
            pass
    return

testsuite editorial_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase r02_join_keeps_selected_cafe:
        parameter case = list(range(6))
        $ editorial_fixture = {"scene":"r02", "informal":bool(case % 2)}
        run Start("test_editorial_entry")
        advance until screen "choice"
        if eval case < 2:
            click expression ri("문 앞 구경은 여기까지 하고, 대안 같이 찾아보자.", "문 앞 구경은 여기까지 하고, 대안 같이 찾아볼까요?")
        elif eval case < 4:
            click "가까운 데를 찾고, 다음 후보는 리아에게 맡긴다."
        else:
            click expression ri("여긴 다음에 다시 오자. 오늘은 잠깐만 같이 걷고.", "여긴 다음에 다시 와요. 오늘은 잠깐만 같이 걸을까요?")
        advance until screen "choice"
        assert eval r02_plan == ("rebook" if case >= 4 else "together")
        assert eval ("역으로 향하는 길" in editorial_history()) == (case >= 4)
        assert eval ("공동 명의면" in editorial_history()) == (case in (2,3))
        assert eval ("후보 하나는 찾았" in editorial_history()) == (case < 2)
        assert eval bool(memory.get("choice_third_r02_plan")) == (case in (2,3))
        screenshot "editorial-r02-join.png"

    testcase quiet_plan_has_distinct_payoff:
        parameter case = list(range(4))
        $ editorial_fixture = {"scene":"r14", "informal":bool(case % 2)}
        run Start("test_editorial_entry")
        advance until screen "choice"
        click "같이 바꿔 보자고 한다 — 교제를 계속한다."
        advance until screen "choice"
        if eval case < 2:
            click "네 시부터 다섯 시 반까지만 보자고 한다."
        else:
            click "네 시, 코스 없이 한 곳에서 쉬자고 한다."
        advance until screen "office_phone"
        click id "phone_next" until not screen "office_phone"
        advance until eval memory.get("editorial_test_done")
        assert eval memory["ria_conflict"] == "resolved"
        assert eval memory["ria_r14_appointment_kept"] is True
        assert eval bool(memory.get("ria_r14_quiet_plan_recalled")) == (case >= 2)
        assert eval ("옮길 준비는 안 해 왔" in editorial_history()) == (case >= 2)
        assert eval memory["ria_r14_plan"] == "fixed"

    testcase r15_deferred_has_no_invented_title:
        parameter informal = [False, True]
        $ editorial_fixture = {"scene":"r15", "informal":informal}
        run Start("test_editorial_entry")
        advance until screen "choice"
        click "일주일에 한 번, 짧게라도 만날 저녁을 함께 정한다."
        advance until screen "choice"
        click "얘기만 더 하고 잠은 각자 잔다."
        advance until eval memory.get("editorial_test_done")
        assert eval memory["ria_r15_intimacy"] == "deferred"
        assert eval memory["ria_r15_booklet_photo_taken"] is True
        assert eval "사진 얘기 더 듣고 싶었" in editorial_history()
        assert eval "사진 제목 얘기" not in editorial_history()
        assert not screen "event_cut"

    testcase epilogue_recalls_only_completed_choice:
        parameter case = list(range(8))
        $ editorial_fixture = {"scene":"e01", "informal":bool(case % 2), "rest":[None, "parallel", "share_page", "one_each"][case // 2]}
        run Start("test_editorial_entry")
        advance until screen "choice"
        assert eval bool(memory.get("ria_e01_one_each_recalled")) == (case >= 6)
        assert eval ("한 가지씩만 보여 주고 덮었" in editorial_history()) == (case >= 6)
        assert eval ("각자 다른 거 보면서" in editorial_history()) == (case in (2,3))
        assert eval ("한 줄씩 얘기했던" in editorial_history()) == (case in (4,5))
        assert eval memory["ria_booklet_state"] == "completed_two_copies"
        screenshot "editorial-epilogue-recall.png"

    teardown:
        exit
