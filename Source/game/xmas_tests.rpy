init python:
    def phone_view_at_bottom():
        v = renpy.get_widget("office_phone", "phone_messages")
        if v is None:
            return False
        adj = v.yadjustment
        return adj.range <= 0 or adj.value >= adj.range - 1

    xmas_fixture = {"who": "ria", "high": True}

label test_xmas_entry:
    $ xwho = xmas_fixture["who"]
    $ active_route = xwho
    $ dating = True
    $ speech_informal = False
    $ affinity = {"ria": 90, "jihyun": 90, "yujin": 90, "seoyun": 90}
    $ memory = {}
    if xmas_fixture["high"]:
        $ remember(xwho + "_o01_status", "completed")
        $ remember(xwho + "_o02_status", "completed")
        $ remember(xwho + "_o03_status", "completed")
        $ xmas_rule = next(r for r in XMAS_HEART_RULES[xwho] if max(r[1].values()) == 2)
        $ remember(xmas_rule[0], max(xmas_rule[1], key=xmas_rule[1].get))
    else:
        $ remember(xwho + "_o01_status", "skipped")
        $ remember(xwho + "_o02_status", "brief")
    call expression (xwho + "_x01")
    menu:
        "검사 종료":
            pass
    return

label test_special_entry:
    $ xwho = xmas_fixture["who"]
    $ active_route = xwho
    $ dating = True
    $ speech_informal = False
    $ memory = {}
    if xmas_fixture["high"]:
        $ remember(xwho + "_o01_status", "completed")
        $ remember(xwho + "_o02_status", "completed")
        $ remember(xwho + "_o03_status", "brief")
    call special_scene(xwho, 1)
    call special_scene(xwho, 2)
    menu:
        "검사 종료":
            pass
    return

label test_breakup_entry:
    $ xwho = xmas_fixture["who"]
    $ active_route = xwho
    $ dating = True
    $ speech_informal = False
    $ memory = {}
    python:
        for key, table in BOND_TRUST_RULES[xwho]:
            worst = min(table, key=table.get)
            if table[worst] < 0:
                remember(key, worst)
    if dating and bond_trust(xwho) <= BOND_BREAKUP_TRUST:
        call bond_breakup(xwho)
    menu:
        "검사 종료":
            pass
    return

testsuite xmas_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase heart_decides_christmas:
        parameter case = list(range(8))
        $ xmas_fixture["who"] = ["ria", "jihyun", "yujin", "seoyun"][case // 2]
        $ xmas_fixture["high"] = case % 2 == 0
        run Start("test_xmas_entry")
        advance until screen "choice" timeout 30.0
        assert eval memory[xmas_fixture["who"] + "_x01_done"]
        assert eval memory[xmas_fixture["who"] + "_x01"] == ("night" if xmas_fixture["high"] else "evening")
        assert eval (xmas_heart(xmas_fixture["who"]) >= XMAS_TRUE_HEART) == xmas_fixture["high"]

    testcase spring_story_unlock_and_read:
        run SetField(persistent, "spring_story_seen", False)
        assert eval spring_story_unlocked() == all(getattr(persistent, "local_%s_ending" % w, False) for w in ("ria", "jihyun", "yujin", "seoyun"))
        run Start("spring_story")
        advance until screen "main_menu" timeout 60.0
        assert eval persistent.spring_story_seen

    testcase prologue_then_common:
        run SetField(persistent, "seen_prologue", False)
        run Start()
        advance until eval chapter.startswith("C01") timeout 30.0
        assert eval persistent.seen_prologue

    testcase special_scenes_follow_heart:
        parameter case = list(range(8))
        $ xmas_fixture["who"] = ["ria", "jihyun", "yujin", "seoyun"][case // 2]
        $ xmas_fixture["high"] = case % 2 == 0
        run Start("test_special_entry")
        advance until screen "choice" timeout 30.0
        assert eval bool(memory.get("x_special_" + xmas_fixture["who"] + "_1")) == xmas_fixture["high"]
        assert eval bool(memory.get("x_special_" + xmas_fixture["who"] + "_2")) == xmas_fixture["high"]

    testcase messenger_follows_latest:
        run SetField(persistent, "phone_typing_enabled", False)
        run Start("office_phone_preview")
        advance until screen "office_phone" timeout 30.0
        click id "phone_next"
        pause 0.5
        click id "phone_next"
        pause 0.5
        click id "phone_next"
        pause 0.5
        click id "phone_next"
        pause 0.5
        click id "phone_next"
        pause 0.5
        assert eval renpy.get_widget("office_phone", "phone_messages").yadjustment.range > 0
        assert eval phone_view_at_bottom()

    testcase breakup_when_trust_is_gone:
        parameter case = [0, 1, 2, 3]
        $ xmas_fixture["who"] = ["ria", "jihyun", "yujin", "seoyun"][case]
        run Start("test_breakup_entry")
        advance until screen "choice" timeout 40.0
        assert eval bond_trust(xmas_fixture["who"]) <= BOND_BREAKUP_TRUST
        assert eval not dating and memory.get(xmas_fixture["who"] + "_breakup_by_heroine")
        assert eval ending == xmas_fixture["who"] + "_relationship_closed"

    teardown:
        exit
