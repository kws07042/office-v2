init python:
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

    teardown:
        exit
