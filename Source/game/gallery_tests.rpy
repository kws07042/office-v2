testsuite gallery_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase gallery_browse:
        $ persistent.cg_seen = {"ria_r07", "ria_x01", "jihyun_r11"}
        $ persistent.diary_recent = {}
        click id "gallery_button"
        screenshot "gallery-1-ria.png"
        click id "gallery_cg_ria_r07"
        click id "gallery_expand"
        assert screen "gallery_view"
        keysym "K_RIGHT"
        screenshot "gallery-2-view.png"
        keysym "K_ESCAPE"
        click id "gallery_tab_jihyun"
        assert eval gallery_count("jihyun")[0] >= 1
        click id "gallery_tab_album"
        screenshot "gallery-3-album.png"
        click id "gallery_back"
        assert screen "main_menu"

    testcase diary_album_roundtrip:
        $ persistent.cg_seen = set(persistent.cg_seen or set()) | {"ria_sp1", "jihyun_r04"}
        run ShowMenu("progression_hub")
        assert screen "progression_hub"
        click id "diary_tab_jihyun"
        click id "diary_photo"
        assert screen "gallery"
        assert eval renpy.get_screen("gallery").scope["tab"] == "jihyun"
        click id "gallery_expand"
        assert screen "gallery_view"
        keysym "K_ESCAPE"
        click id "gallery_tab_album"
        click id "gallery_back"

    testcase diary_empty_and_legacy:
        $ persistent.cg_seen = set()
        $ persistent.diary_recent = {}
        $ persistent.diary_lines = {}
        run ShowMenu("progression_hub", initial_person="yujin")
        assert eval renpy.get_widget("progression_hub", "diary_photo") is None
        click id "diary_album"
        assert eval renpy.get_widget("gallery", "gallery_expand") is None
        click id "gallery_back"
        $ persistent.cg_seen = {"ria_sp1", "ria_r04"}
        run ShowMenu("progression_hub", initial_person="ria")
        assert eval renpy.get_widget("progression_hub", "diary_photo") is not None
        click id "diary_photo"
        click id "gallery_cg_ria_r04"
        click id "gallery_expand"
        keysym "K_RIGHT"
        assert eval persistent.diary_recent.get("ria") == "ria_sp1"
        keysym "K_ESCAPE"
        assert screen "gallery"
        click id "gallery_back"

    testcase diary_current_save:
        run Start("test_diary_save_entry")
        pause 0.5
        run FileSave("diary-test", confirm=False, slot=True)
        $ dating = False
        run FileLoad("diary-test", confirm=False, slot=True)
        pause 0.5
        assert eval dating and active_route == "ria"
        run ShowMenu("progression_hub")
        assert eval renpy.get_screen("progression_hub").scope["person"] == "ria"
        screenshot "applied-diary.png"
        click id "diary_album"
        screenshot "applied-album.png"
        click id "gallery_back"

    testcase sd_cut_restore:
        $ location = "며칠 뒤 · 회사 근처 카페"
        $ cg("common_c05")
        $ sd_cut("common_sd_c05")
        assert eval art_cg_path() == "images/cg/common_sd_c05.jpg" and "common_sd_c05" in persistent.cg_seen
        $ sd_cut_end()
        assert eval art_cg_path() == "images/cg/common_c05.jpg"
        $ cg()
        $ sd_cut("ria_sd_r02")
        $ sd_cut_end()
        assert eval art_cg_path() is None
        assert eval all(renpy.loadable(gallery_path(n)) for n in GALLERY_ORDER if "_sd_" in n) and len([n for n in GALLERY_ORDER if "_sd_" in n]) == 13
        assert eval gallery_label("ria_sd_r02") == "세 번 읽은 임시 휴무" and gallery_owner("common_sd_c05") == "common"

    teardown:
        exit

label test_diary_save_entry:
    $ active_route = "ria"
    $ dating = True
    $ location = "일요일 오후 · 동네 코인 세탁방"
    $ cg("ria_sp1")
    $ persistent.special_ria_1 = True
    $ persistent.diary_lines["ria"] = "사십 분 생각보다 짧다."
    "다이어리 검사"
    return
