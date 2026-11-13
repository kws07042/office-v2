testcase badge_ui_smoke:
    $ renpy.screenshot(renpy.config.basedir + "/window-title.png")
    assert eval renpy.newest_slot(r"^(?:[0-9]+|quick|auto)-[0-9]+$") is None
    click id "badge_load"
    assert screen "load"
    $ renpy.screenshot(renpy.config.basedir + "/window-load.png")
    click "돌아가기"
    click "환경설정"
    assert screen "preferences"
    $ renpy.screenshot(renpy.config.basedir + "/window-settings.png")
    click id "settings_messenger"
    click id "settings_typing_off"
    assert eval persistent.phone_typing_enabled is False
    click id "settings_typing_on"
    assert eval persistent.phone_typing_enabled is True
    click id "settings_reading"
    click id "settings_instant"
    assert eval _preferences.text_cps == 0
    click id "settings_skip_seen"
    assert eval not _preferences.skip_unseen
    click "돌아가기"
    click id "badge_gallery"
    assert screen "progression_hub"
    assert eval renpy.get_screen("progression_hub").scope["tab"] == "gallery"
    click "이야기"
    assert eval renpy.get_screen("progression_hub").scope["tab"] == "story"
    click "결말"
    assert eval renpy.get_screen("progression_hub").scope["tab"] == "endings"
    click "관계"
    assert eval renpy.get_screen("progression_hub").scope["tab"] == "relations"
    click "CG · 회상"
    $ renpy.screenshot(renpy.config.basedir + "/window-gallery.png")
    click "돌아가기"
    run Start("office_phone_preview")
    advance until screen "office_phone"
    click id "phone_next" until eval renpy.get_screen("office_phone") and bool(renpy.get_screen("office_phone").scope.get("replies"))
    $ renpy.screenshot(renpy.config.basedir + "/window-phone.png")
    click id "phone_contact_jihyun"
    click "진행 중인 대화로 돌아가기"
    click id "phone_reply_miss"
    assert eval len(phone_threads["ria"]) > 2
    run MainMenu(confirm=False)
    run Start("cream_preview_start")
    assert screen "say"
    $ renpy.screenshot(renpy.config.basedir + "/window-dialogue.png")
    click id "badge_hide"
    pause 0.25
    assert eval _windows_hidden
    $ renpy.screenshot(renpy.config.basedir + "/window-hidden.png")
    keysym "hide_windows"
    pause until screen "say"
    run ShowMenu("history")
    assert screen "history"
    $ renpy.screenshot(renpy.config.basedir + "/window-history.png")
    click "돌아가기"
    run ShowMenu("save")
    assert screen "save"
    $ renpy.screenshot(renpy.config.basedir + "/window-save.png")
    click id "window_slot_1"
    assert eval FileLoadable("1")
    run ShowMenu("load")
    assert screen "load"
    click id "window_slot_1"
    assert screen "confirm"
    click "예"
    pause 0.4
    $ renpy.screenshot(renpy.config.basedir + "/window-after-load.png")
    pause until screen "say"
    assert screen "say"
    advance until screen "choice"
    $ renpy.screenshot(renpy.config.basedir + "/window-choices.png")
    click "조용한 카페에서 조금 더 이야기하자."
    assert eval cream_preview_reply == "cafe"
    run MainMenu(confirm=False)
    assert screen "main_menu"
    click id "badge_continue"
    pause until screen "say"
    assert screen "say"
