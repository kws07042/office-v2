testsuite desktop_title_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase desktop_title_menu:
        assert eval renpy.get_widget("main_menu", "desktop_start_button") is not None
        pause 1.2
        screenshot "desktop-title-1.png"
        click id "desktop_start_button"
        assert eval renpy.get_widget("main_menu", "desktop_start_menu") is not None
        pause 0.5
        screenshot "desktop-title-2-start.png"
        click id "desktop_start_button"
        click id "gallery_button"
        assert screen "gallery"
        click id "gallery_back"
        assert screen "main_menu"

    teardown:
        exit
