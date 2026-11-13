init python:
    route_phone_fixture = {"case": 0}

label test_route_phone_entry:
    $ route_phone_case = route_phone_fixture["case"]
    $ active_route = "ria"
    $ dating = route_phone_case >= 4
    $ speech_informal = bool(route_phone_case % 2)
    $ affinity = {"ria":58, "jihyun":0, "yujin":0, "seoyun":0}
    $ memory = {"ria_r12_next_appointment_status":"scheduled", "ria_r12_expectation":"hope_early" if route_phone_case % 2 else "fixed"}
    $ completed = ["ria_R12"]
    if route_phone_case % 2:
        $ remember("ria_cafe_visited")
    if route_phone_case % 4 == 0:
        $ remember("ria_o02_status", "completed")
        $ remember("ria_o02_name", "불 켜지는 모퉁이")
    elif route_phone_case % 4 == 1:
        $ remember("ria_r10_place", "park")
    elif route_phone_case % 4 == 2:
        $ remember("ria_r10_place", "bakery")
    if route_phone_case < 4:
        call ria_r03
    elif route_phone_case < 8:
        call ria_r12
    else:
        call ria_r13
    $ remember("route_phone_test_done")
    "검사 종료"
    return

label test_route_phone_disclosure:
    $ active_route = "ria"
    $ dating = True
    $ location = "일요일 저녁 · 리아의 집"
    call ria_disclosure_phone
    $ remember("test_disclosure_done")
    menu:
        "검사 종료":
            return

testsuite route_phone_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase migrated_story_messages:
        parameter case = list(range(12))
        $ route_phone_fixture["case"] = case
        run Start("test_route_phone_entry")
        advance until screen "office_phone"
        click id "phone_next" until not screen "office_phone"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
        if screen "office_phone":
            click id "phone_next" until not screen "office_phone"
            advance until screen "choice"
        assert eval all(row.get("moment") for row in phone_threads["ria"])
        assert eval len({row["id"] for row in phone_threads["ria"]}) == len(phone_threads["ria"])
        assert eval phone_threads["seoyun"] == []
        assert eval phone_photo_opened == []
        if eval case < 4:
            assert eval memory.get("ria_r03_messages_received") is True
            assert eval len(phone_threads["ria"]) == 2
            assert eval ("그 카페 앞" in phone_threads["ria"][-1]["text"]) == bool(case % 2)
            screenshot "route-phone-r03.png"
        elif eval case < 8:
            assert eval memory.get("ria_r12_appointment") == "토요일 오후 일곱 시 역 앞"
            assert eval len(phone_threads["ria"]) == (7 if case == 7 else 8)
            assert eval {row["moment"] for row in phone_threads["ria"]} == {"화요일 밤", "수요일 밤", "목요일 밤", "금요일 저녁"}
            if eval case == 4:
                assert eval "불 켜지는 모퉁이" in phone_message("ria_r12_place_memory")["text"]
            elif eval case == 5:
                assert eval "작은 공원" in phone_message("ria_r12_place_memory")["text"]
            elif eval case == 6:
                assert eval "빵집 옆 골목" in phone_message("ria_r12_place_memory")["text"]
            else:
                assert eval phone_message("ria_r12_place_memory") is None
            run Show("office_phone_archive")
            screenshot "route-phone-weekly-history.png"
            click id "phone_archive_close"
        else:
            assert eval memory.get("ria_conflict") == "open"
            assert eval len(phone_threads["ria"]) == 6
            assert eval "다섯 시 십 분" in phone_message("ria_r13_arrival")["text"]
            run Show("office_phone_archive")
            screenshot "route-phone-delay-history.png"
            click id "phone_archive_close"

    testcase save_load_and_deduplication:
        $ route_phone_fixture["case"] = 4
        run Start("test_route_phone_entry")
        advance until screen "office_phone"
        assert eval len(phone_threads["ria"]) == 1
        run FileSave("16", confirm=False)
        click id "phone_next"
        assert eval len(phone_threads["ria"]) == 2
        run FileLoad("16", confirm=False)
        assert eval len(phone_threads["ria"]) == 1
        click id "phone_next"
        assert eval len(phone_threads["ria"]) == 2
        run Function(phone_add, "ria_r12_01", "ria", "duplicate")
        assert eval len(phone_threads["ria"]) == 2
        assert eval phone_threads["ria"][0]["text"] != "duplicate"

    testcase next_morning_reply_paths:
        parameter answer = ["fixed", "hope_early", "clarify"]
        $ route_phone_fixture["case"] = 7
        run Start("test_route_phone_entry")
        advance until screen "office_phone"
        click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        click "오늘은 가고 내일 다시 보자고 한다."
        advance until screen "office_phone"
        click id "phone_next" until eval phone_context == "r12_expectation"
        assert eval len(renpy.get_screen("office_phone").scope["replies"]) == 3
        run FileSave("17", confirm=False)
        click id ("phone_reply_" + answer)
        assert eval phone_context is None
        run FileLoad("17", confirm=False)
        assert eval phone_context == "r12_expectation"
        click id ("phone_reply_" + answer)
        click id "phone_next" until not screen "office_phone"
        advance until eval memory.get("route_phone_test_done")
        assert eval memory["ria_r12_expectation"] == ("hope_early" if answer == "hope_early" else "fixed")
        assert eval bool(memory.get("choice_third_r12_expectation")) == (answer == "clarify")
        assert eval memory["ria_r12_next_appointment_status"] == "scheduled"
        assert eval len({row["id"] for row in phone_threads["ria"]}) == len(phone_threads["ria"])
        assert eval phone_message("ria_r12_plan_01") is not None
        run Show("office_phone_archive")
        screenshot "route-phone-next-morning-plan.png"
        click id "phone_archive_close"

    testcase shared_disclosure_has_own_contact:
        run Start("test_route_phone_disclosure")
        advance until screen "office_phone"
        assert eval phone_active_contact == "seoyun"
        assert eval phone_threads["seoyun"][0]["sender"] == "ria_shared"
        screenshot "route-phone-shared-disclosure.png"
        click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        assert eval memory.get("test_disclosure_done")
        assert eval len(phone_threads["seoyun"]) == 4
        assert eval phone_threads["ria"] == []
        assert eval phone_active_contact == "ria"
        run Show("office_phone_archive")
        click id "phone_contact_seoyun"
        assert "서윤 씨, 감사합니다. 오늘은 저녁만 같이 만들려고요."
        screenshot "route-phone-seoyun-history.png"
        click id "phone_archive_close"

    teardown:
        exit
