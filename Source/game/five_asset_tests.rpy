init python:
    layout_fixture = {}
    layout_variants = [("ria_r07", "casual"), ("ria_r12", "special"), ("ria_r15", "home"), ("ria_r15", "cosplay")]

label test_layout_entry:
    scene bg plain
    $ active_route = "ria"
    $ dating = True
    $ speech_informal = bool(layout_fixture.get("case", 0) & 1)
    $ layout_event, layout_variant = layout_variants[layout_fixture.get("case", 0) // 2]
    call event_sequence(layout_event, layout_variant)
    if not event_main_reached:
        "(장면 생략 · 시간이 흐릅니다.)"
        $ remember("layout_time_transition")
    menu:
        "화면 검사 종료":
            pass
    return

testsuite five_asset_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase four_sets_two_speech_styles:
        parameter case = list(range(8))
        $ layout_fixture["case"] = case
        run Start("test_layout_entry")
        advance until screen "event_cut"
        assert eval event_cut_cursor == 0
        assert eval event_intro_expression_ready is False
        assert eval [p["kind"] for p in event_pages(layout_event,layout_variant)] == ["intro"]*3 + ["main"]*3 + ["after"]
        assert eval len(event_cg_sets) == 16
        assert eval sum(s["runtime_connected"] for s in event_cg_sets.values()) == 4
        assert eval all(len(s["event_asset_order"]) == 5 and len(s["base_cg"]) == 3 and not s["expression_variants"] for s in event_cg_sets.values())
        click id "cut_next"
        click id "cut_next"
        pause 0.8
        assert eval event_cut_cursor == 2
        assert eval event_intro_expression_ready is True
        if eval case == 0:
            screenshot "intro-expression-placeholder.png"
        run FileSave("8", confirm=False)
        click id "cut_next"
        assert eval event_main_reached is True
        click id "cut_previous"
        assert eval event_cut_cursor == 2
        assert eval event_intro_expression_ready is True
        run FileLoad("8", confirm=False)
        assert screen "event_cut" timeout 10.0
        assert eval event_cut_cursor == 2
        assert eval event_intro_expression_ready is True
        assert eval event_main_reached is False
        click id "cut_next"
        assert eval event_cut_cursor == 3
        assert eval event_main_reached is True
        click id "cut_next"
        assert eval event_cut_cursor == 4
        click id "cut_next"
        assert eval event_cut_cursor == 5
        click id "cut_next"
        assert eval event_cut_cursor == 6
        assert eval renpy.get_screen("event_cut").scope["page"]["kind"] == "after"
        assert eval renpy.get_screen("event_cut").scope["expression"] is False
        click id "cut_next" until not screen "event_cut"
        advance until screen "choice"
        assert eval "layout_time_transition" not in memory
        assert eval event_presentations[layout_event+":"+layout_variant]["visited_slots"] == list(range(1,8))
        assert eval event_presentations[layout_event+":"+layout_variant]["main_frames_seen"] == [1,2,3]
        assert eval event_presentations[layout_event+":"+layout_variant]["loaded_asset_ids"] == []
        assert eval len(event_presentations[layout_event+":"+layout_variant]["missing_asset_ids"]) == 5
        assert eval event_presentations[layout_event+":"+layout_variant]["status"] == "completed"
        assert eval sum(affinity.values()) == 0
        assert eval first_kiss is False

    testcase skip_without_forced_wait:
        parameter reached = [False,True]
        $ layout_fixture["case"] = 0
        run Start("test_layout_entry")
        advance until screen "event_cut"
        if eval reached:
            click id "cut_next"
            click id "cut_next"
            click id "cut_next"
        click id "cut_skip" until not screen "event_cut"
        advance until screen "choice"
        assert eval ("layout_time_transition" in memory) == (not reached)
        assert eval event_presentations["ria_r07:casual"]["status"] == "skipped_presentation"

    teardown:
        exit

testsuite five_asset_fixture_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase synthetic_intro_and_three_main_images:
        $ layout_fixture["case"] = 0
        run Start("test_layout_entry")
        advance until screen "event_cut"
        assert eval event_intro_asset("ria_r07","casual")["path"] is not None
        click id "cut_next"
        click id "cut_next"
        pause 0.8
        assert eval event_intro_expression_ready is True
        assert eval event_intro_asset("ria_r07","casual",True)["fallback"] == (not renpy.loadable(event_cg_sets["ria_r07:casual"]["intro_expression"]["planned_path"]))
        screenshot "synthetic-intro-expression.png"
        click id "cut_next"
        assert eval event_resolve_cg("ria_r07","casual","ria_R07_casual_base01")["path"] is not None
        click id "cut_next"
        click id "cut_next"
        screenshot "synthetic-third-main.png"
        click id "cut_next" until not screen "event_cut"
        advance until screen "choice"
        assert eval event_presentations["ria_r07:casual"]["loaded_images"] == list(range(1,8))
        assert eval len(event_presentations["ria_r07:casual"]["loaded_asset_ids"]) == (5 if renpy.loadable(event_cg_sets["ria_r07:casual"]["intro_expression"]["planned_path"]) else 4)
        assert eval len(event_presentations["ria_r07:casual"]["missing_asset_ids"]) == (0 if renpy.loadable(event_cg_sets["ria_r07:casual"]["intro_expression"]["planned_path"]) else 1)
        assert eval first_kiss is False

    teardown:
        exit
