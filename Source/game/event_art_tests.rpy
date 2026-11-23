# 성인 이벤트 도입 CG 연결 검사. 배포 패키지에 넣지 않는다.
default event_art_case = "ria_r07"

label test_event_art_entry:
    scene bg plain
    if event_art_case == "jihyun_qipao":
        $ memory["jihyun_r15_costume"] = "qipao"
        call event_sequence("jihyun_r15", "cosplay")
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
        parameter case = ["ria_r07", "jihyun_qipao", "yujin_r12"]
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

    teardown:
        exit
