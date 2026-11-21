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

    teardown:
        exit
