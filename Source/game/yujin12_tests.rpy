init python:
    yujin12_fixture = {"case":0}

label test_yujin12_entry:
    $ active_route = "yujin"
    $ dating = True
    $ affinity = {"ria":0,"jihyun":0,"yujin":38,"seoyun":0}
    $ memory = {}
    if yujin12_fixture["case"] < 27:
        $ remember("yujin_r08_availability", ["wed19","thu19","wed1930"][yujin12_fixture["case"] % 3])
        $ remember("yujin_r08_next_appointment", ["수요일 저녁 일곱 시, 회사 근처 카페","목요일 저녁 일곱 시, 회사 근처 카페","수요일 저녁 일곱 시 반, 회사 근처 카페"][yujin12_fixture["case"] % 3])
        $ remember("yujin_r02_plan", ["follow","window","linger"][yujin12_fixture["case"] % 3])
        $ remember("yujin_r05_layout", ["photo_first","text_first","spread"][yujin12_fixture["case"] % 3])
    call yujin_r09
    call yujin_r10
    call yujin_r11
    call yujin_r12
    $ remember("yujin12_done")
    menu:
        "검사 종료":
            pass
    return

testsuite yujin12_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase real_support_and_relationship:
        parameter case = list(range(28))
        $ yujin12_fixture["case"] = case
        run SetField(persistent, "local_yujin_ending", bool(case % 2))
        run Start("test_yujin12_entry")
        advance until screen "choice"
        assert eval cream_yujin_visible() and not cream_ria_visible()
        if eval case < 27:
            assert eval ("목요일" in location) == (case % 3 == 1)
        click expression yujin_test_choice(case % 3)
        advance until screen "choice"
        assert eval memory["yujin_support_action"] == ["materials","self_summary","agreed_summary"][case % 3]
        assert eval memory["yujin_support_overstep"] == (case % 3 == 1)
        assert eval memory["yujin_r09_explained_by"] == "yujin"
        if eval case < 27:
            assert eval memory["yujin_r09_kept_appointment"] == memory["yujin_r08_next_appointment"]
            assert eval location.startswith(memory["yujin_r08_next_appointment"])
        else:
            assert eval "새로 제안" in memory["yujin_r09_kept_appointment"]
        if eval case == 1:
            screenshot "yujin-r09-boundary-choice.png"
        click expression yujin_test_choice((case // 3) % 3)
        advance until screen "choice"
        assert eval memory["yujin_support_repair_status"] == ("open" if case % 3 == 1 and (case // 3) % 3 == 1 else ("agreed_pending_action" if case % 3 == 1 else "not_needed"))
        click expression yujin_test_choice((case + 1) % 3)
        advance until screen "choice"
        assert eval memory["yujin_r10_page"] == ["entrance_bench","one_sentence","open_space"][(case + 1) % 3]
        click expression yujin_test_choice((case // 3) % 3)
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
        if eval (case // 3) % 3 == 0:
            assert screen "office_phone"
            assert eval phone_active_contact == "jihyun"
            assert eval not memory.get("yujin_disclosed_to")
            click id "phone_next" until not screen "office_phone"
            advance until screen "choice"
            assert eval memory["yujin_disclosed_to"] == "jihyun"
            assert eval len(phone_threads["jihyun"]) == 3
        else:
            assert screen "choice"
            assert eval not memory.get("yujin_disclosed_to") and not phone_threads["jihyun"]
        if eval case == 0:
            screenshot "yujin-r11-music-choice.png"
        click expression yujin_test_choice((case // 9 + case) % 3)
        advance until screen "office_phone"
        assert eval memory["yujin_r11_music"] == ["yujin_calm","dohyun_bright","both"][(case // 9 + case) % 3]
        assert eval len(memory["yujin_r11_heard"]) == (2 if (case // 9 + case) % 3 == 2 else 1)
        assert eval "월요일" in location
        click id "phone_next" until eval phone_context == "yujin_r12_reunion_reply"
        assert eval not memory.get("yujin_r12_reunion_kept")
        if eval case == 0:
            run FileSave("32", confirm=False)
            click id "phone_reply_cafe19"
            click id "phone_next" until not screen "office_phone"
            advance until screen "choice"
            assert eval "일곱 시" in memory["yujin_r12_appointment"]
            run FileLoad("32", confirm=False)
        click id ("phone_reply_" + ["cafe1830","cafe19","bookshop1830"][case % 3])
        click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        assert eval location == memory["yujin_r12_appointment"]
        assert eval ("일곱 시" in location) == (case % 3 == 1)
        assert eval ("서점" in location) == (case % 3 == 2)
        click expression yujin_test_choice((case // 9) % 3)
        advance until screen "choice"
        assert eval not memory.get("yujin_support_repair_action_verified")
        assert eval memory["yujin_support_repair_status"] == ("open" if case % 3 == 1 and (case // 3) % 3 == 1 and (case // 9) % 3 == 1 else ("agreed_pending_action" if case % 3 == 1 else "not_needed"))
        click expression yujin_test_choice((case // 3 + case // 9) % 3)
        if eval (case // 3 + case // 9) % 3 == 0:
            advance until screen "event_cut"
            assert eval renpy.get_screen("event_cut").scope["event_id"] == "yujin_r12"
            if eval case == 0:
                screenshot "yujin-r12-placeholder.png"
            if eval case == 15:
                click id "cut_skip"
            else:
                click id "cut_next" until not screen "event_cut"
        advance until eval memory.get("yujin12_done")
        assert eval memory["yujin_r12_intimacy"] == ["shared","deferred","walk"][(case // 3 + case // 9) % 3]
        assert eval memory["yujin_r12_complete"]
        assert eval memory["yujin_r12_reunion_kept"] == memory["yujin_r12_appointment"]
        assert eval affinity["yujin"] == 52
        assert eval all("yujin_R" + str(i).zfill(2) in completed for i in range(9,13))
        assert eval not any(k.startswith("ria_") for k in memory)
        assert eval not phone_threads["ria"] and not phone_threads["seoyun"]
        assert eval len({row["id"] for row in phone_threads["yujin"]}) == len(phone_threads["yujin"])
        assert eval bool(persistent.local_yujin_ending) == bool(case % 2)

    teardown:
        exit
