testsuite gallery_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase gallery_browse:
        $ persistent.cg_seen = set(persistent.cg_seen or set()) | {"ria_r07", "ria_x01", "jihyun_r11"}
        click id "gallery_button"
        screenshot "gallery-1-ria.png"
        click id "gallery_cg_ria_r07"
        assert screen "gallery_view"
        click id "gallery_next"
        screenshot "gallery-2-view.png"
        click id "gallery_close"
        click id "gallery_tab_jihyun"
        assert eval gallery_count("jihyun")[0] >= 1
        click id "gallery_tab_album"
        screenshot "gallery-3-album.png"
        click id "gallery_back"
        assert screen "main_menu"

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
