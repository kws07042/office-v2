# 성인 이벤트 도입 CG 연결 검사. 배포 패키지에 넣지 않는다.
default event_art_case = "ria_r07"

label test_event_art_entry:
    scene bg plain
    if event_art_case == "jihyun_qipao":
        $ memory["jihyun_r15_costume"] = "qipao"
        call event_sequence("jihyun_r15", "cosplay")
    elif event_art_case == "seoyun_r07":
        call event_sequence("seoyun_r07", "casual")
    elif event_art_case == "yujin_r12":
        call event_sequence("yujin_r12", "special")
    else:
        call event_sequence("ria_r07", "casual")
    return

testsuite event_art_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase intro_full_screen:
        parameter case = ["ria_r07", "jihyun_qipao", "yujin_r12", "seoyun_r07"]
        $ event_art_case = case
        run Start("test_event_art_entry")
        advance until screen "event_cut" timeout 20.0
        pause 0.4
        assert eval renpy.get_screen("event_cut").scope["full_art"]
        screenshot ("event-art-" + case + ".png")
        click id "cut_skip"

    testcase costume_paths:
        $ memory["seoyun_r15_costume"] = "police"
        assert eval event_intro_asset("seoyun_r15", "cosplay")["path"] == "images/events/seoyun/r15_cosplay_police_intro.png"
        $ memory["seoyun_r15_costume"] = "bunny"
        assert eval event_intro_asset("seoyun_r15", "cosplay")["path"] == "images/events/seoyun/r15_cosplay_bunny_intro.png"
        assert eval event_intro_asset("ria_r07", "casual")["path"] == "images/events/ria/r07_casual_intro.png"
        assert eval renpy.loadable("images/cg/ria_o04.jpg")
        assert eval event_after_path("seoyun_r07", "casual") == "images/events/seoyun/r07_casual_after.png"
        $ memory["seoyun_r15_costume"] = "police"
        assert eval event_after_path("seoyun_r15", "cosplay") == "images/events/seoyun/r15_cosplay_police_after.png"
        assert eval event_intro_asset("seoyun_r15", "cosplay", True)["path"] == "images/events/seoyun/r15_cosplay_police_intro_shy.png"
        assert eval event_after_path("ria_r07", "casual") == "images/events/ria/r07_casual_after.png"
        assert eval event_after_path("yujin_r07", "casual") is None
        $ memory["ria_r15_costume"] = "cheer"
        assert eval event_after_path("ria_r15", "cosplay") is None

    teardown:
        exit

testsuite event_after_art_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase seoyun_after_page:
        $ event_art_case = "seoyun_r07"
        run Start("test_event_art_entry")
        advance until screen "event_cut" timeout 20.0
        click id "cut_next" until eval event_cut_cursor == 6
        pause 0.4
        assert eval renpy.get_screen("event_cut").scope["full_art"]
        assert eval renpy.get_screen("event_cut").scope["resolved"]["path"] == "images/events/seoyun/r07_casual_after.png"
        screenshot "event-art-seoyun-after.png"
        click id "cut_next"

    teardown:
        exit
