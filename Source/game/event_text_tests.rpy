# 본장면 대사(event_main_text.json) 연결 검사. 배포 패키지에 넣지 않는다.
default event_text_case = "ria_cheer"

label test_event_text_entry:
    scene bg plain
    $ event_text_in_test = True
    $ mc_name = "민수"
    if event_text_case == "seoyun_r07":
        call event_sequence("seoyun_r07", "casual")
    else:
        $ memory["ria_r15_costume"] = "cheer"
        call event_sequence("ria_r15", "cosplay")
    $ event_text_in_test = False
    menu:
        "검사 종료":
            pass
    return

label test_event_text_motel:
    scene bg plain
    $ event_text_in_test = True
    $ event_play_text_scene("ria_o04:motel", r)
    $ event_text_in_test = False
    menu:
        "검사 종료":
            pass
    return

testsuite event_text_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase data_complete:
        assert eval len(event_main_text) == 25
        assert eval all(len(s["main"]) == 3 for s in event_main_text.values())
        assert eval all(not isinstance(v, str) and len(v) == 2 for s in event_main_text.values() if s["id"].startswith("ria") for cg in s["main"] for k, v in cg["lines"] if k != "narration")
        assert eval all(isinstance(v, str) for s in event_main_text.values() if not s["id"].startswith("ria") for cg in s["main"] for k, v in cg["lines"])
        assert eval not any("[" in event_line_text(v) or "{" in event_line_text(v) for s in event_main_text.values() for cg in s["main"] for k, v in cg["lines"])

    testcase main_lines_step:
        parameter case = ["ria_cheer", "seoyun_r07"]
        $ event_text_case = case
        run Start("test_event_text_entry")
        advance until screen "event_cut" timeout 20.0
        click id "cut_next"
        click id "cut_next"
        click id "cut_next"
        assert eval event_cut_cursor == 3 and event_line == 0
        assert eval len(renpy.get_screen("event_cut").scope["mlines"]) >= 7
        if eval case == "ria_cheer":
            screenshot "event-text-main.png"
        click id "cut_next"
        assert eval event_cut_cursor == 3 and event_line == 1
        click id "cut_previous"
        assert eval event_cut_cursor == 3 and event_line == 0
        click id "cut_next" until eval event_cut_cursor == 4
        assert eval event_line == 0
        click id "cut_next" until not screen "event_cut"
        advance until screen "choice"
        assert eval event_presentations[("ria_r15:cosplay" if case == "ria_cheer" else "seoyun_r07:casual")]["status"] == "completed"

    testcase player_name_in_lines:
        $ mc_name = "민수"
        assert eval "민수" in mc_apply("도현이 손을 잡는다.") and "도현" not in mc_apply(event_line_text(event_main_text["seoyun_r07:casual"]["main"][0]["lines"][0][1]))
        $ mc_name = "도현"

    testcase motel_dialogue:
        run Start("test_event_text_motel")
        advance until screen "choice" timeout 60.0

    teardown:
        exit
