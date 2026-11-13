label test_yujin08_entry:
    $ active_route = "yujin"
    $ dating = True
    $ cream_focus = "yujin"
    $ affinity = {"ria":0, "jihyun":0, "yujin":24, "seoyun":0}
    $ memory = {"yujin_next_date_plan":["dohyun_suggests","yujin_suggests","both_suggest"][yujin_fixture["case"] % 3], "yujin_r02_plan":["follow","window","linger"][yujin_fixture["case"] % 3]}
    call yujin_r05
    call yujin_r06
    call yujin_r07
    call yujin_r08
    $ remember("yujin08_test_done")
    menu:
        "검사 종료":
            pass
    return

testsuite yujin08_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase branches_and_real_memories:
        parameter case = list(range(12))
        $ yujin_fixture["case"] = case
        run Start("test_yujin08_entry")
        advance until screen "choice"
        assert eval cream_yujin_visible() == bool(renpy.loadable("images/characters/yujin/ui_temp_v001.png")) and not cream_ria_visible()
        if eval case == 0:
            screenshot "yujin-r05-portrait.png"
        click expression yujin_test_choice(case % 3)
        advance until screen "choice"
        click expression yujin_test_choice((case // 3) % 3)
        advance until screen "choice"
        assert eval memory["yujin_r05_layout"] == ["photo_first","text_first","spread"][case % 3]
        assert eval first_kiss == ((case // 3) % 3 == 0)
        click expression yujin_test_choice((case + 1) % 3)
        advance until screen "choice"
        click expression yujin_test_choice((case // 3 + 1) % 3)
        advance until screen "choice"
        assert eval memory["yujin_r06_expression"] == ["both_initiate","think_first","take_turns"][(case + 1) % 3]
        assert eval first_kiss == (((case // 3) % 3 == 0) or ((case // 3 + 1) % 3 == 0))
        if eval case == 0:
            screenshot "yujin-r07-night-portrait.png"
        click expression yujin_test_choice(case % 3)
        if eval case % 3 == 0:
            advance until screen "event_cut"
            assert eval phone_names(renpy.get_screen("event_cut").scope["event_id"].split("_")[0]) == "차유진"
            if eval case == 0:
                screenshot "yujin-r07-placeholder.png"
            if eval case == 9:
                click id "cut_skip"
            else:
                click id "cut_next" until not screen "event_cut"
        advance until screen "office_phone"
        assert eval memory["yujin_r07_pace"] == ["shared","deferred","talk"][case % 3]
        assert eval bool(memory.get("yujin_r08_morning_shared")) == (case % 3 == 0)
        assert eval not cream_yujin_visible()
        assert eval ("커튼" in phone_threads["yujin"][-1]["text"]) == (memory.get("yujin_r07_pace") == "shared")
        click id "phone_next" until eval phone_context == "yujin_r08_reply"
        assert eval ("생각해 보시고" in phone_threads["yujin"][-1]["text"]) == ((case + 1) % 3 == 1)
        if eval case == 0:
            run FileSave("28", confirm=False)
            click id "phone_reply_thu19"
            click id "phone_next" until not screen "office_phone"
            advance until eval memory.get("yujin08_test_done")
            assert eval memory["yujin_r08_availability"] == "thu19"
            run FileLoad("28", confirm=False)
        click id ("phone_reply_" + ["wed19","thu19","wed1930"][case % 3])
        click id "phone_next" until not screen "office_phone"
        advance until eval memory.get("yujin08_test_done")
        assert eval memory["yujin_r08_availability"] == ["wed19","thu19","wed1930"][case % 3]
        assert eval memory["yujin_r08_next_appointment"] == ["수요일 저녁 일곱 시, 회사 근처 카페","목요일 저녁 일곱 시, 회사 근처 카페","수요일 저녁 일곱 시 반, 회사 근처 카페"][case % 3]
        assert eval memory["yujin_r08_proposer"] == "yujin"
        assert eval affinity["yujin"] == 38
        assert eval memory["yujin_r08_complete"]
        assert eval all("yujin_R0" + str(i) in completed for i in range(5,9))
        assert eval not any(k.startswith("ria_") for k in memory)
        assert eval len({row["id"] for row in phone_threads["yujin"]}) == len(phone_threads["yujin"])

    teardown:
        exit
