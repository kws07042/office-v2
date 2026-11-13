# Prior 0.9.0 snapshots are copied only into this suite's isolated save folder.
testsuite clear_compat_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase previous_choice_save:
        run FileLoad("9", confirm=False)
        assert screen "choice" timeout 10.0
        assert eval cream_preview_active is True
        assert eval cream_stage_mode() == "night"
        assert eval len(renpy.get_screen("choice").scope["items"]) == 3
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        click "천천히 걷자. 목적지는 걸으면서 고르고." until not screen "choice"
        assert eval cream_preview_reply == "walk"

    testcase previous_event_save:
        run FileLoad("8", confirm=False)
        assert screen "event_cut" timeout 10.0
        assert eval event_cut_cursor == 2
        assert eval event_intro_expression_ready is True
        assert eval event_main_reached is False
        click id "cut_next"
        assert eval event_cut_cursor == 3
        assert eval event_main_reached is True

    teardown:
        exit
