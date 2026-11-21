# 미니게임 5종을 끝까지 눌러 본다.
testsuite minigame_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase hub_and_sign:
        click id "minigame_button"
        screenshot "mg-0-hub.png"
        click id "hub_sign"
        click id "sign_slot_3"
        click id "sign_dir_2"
        click id "sign_place"
        screenshot "mg-1-sign-hint.png"
        click id "sign_slot_1"
        click id "sign_dir_2"
        click id "sign_place"
        click id "sign_slot_2"
        click id "sign_dir_4"
        click id "sign_place"
        click id "sign_slot_2"
        click id "sign_dir_0"
        click id "sign_place"
        advance until screen "main_menu" timeout 20.0
        assert eval persistent.minigame_best.get("sign") == 8

    testcase cards:
        run [SetField(persistent, "mg_pending", "cards"), Start("minigame_free")]
        click id "card_market_0"
        screenshot "mg-2-cards.png"
        click id "card_market_0"
        click id "card_market_0"
        click id "card_market_0"
        click id "card_market_0"
        click id "cards_done"
        advance until screen "main_menu" timeout 20.0
        assert eval "cards" in persistent.minigame_best

    testcase photo:
        run [SetField(persistent, "mg_pending", "photo"), Start("minigame_free")]
        click id "photo_cell_1_1"
        screenshot "mg-3-photo.png"
        click id "photo_shoot"
        click id "photo_keep"
        advance until screen "main_menu" timeout 20.0
        assert eval persistent.minigame_best.get("photo") == 3 and len(persistent.album) >= 1

    testcase trim:
        run [SetField(persistent, "mg_pending", "trim"), Start("minigame_free")]
        click id "trim_chip_0"
        click id "trim_submit"
        screenshot "mg-4-trim-keep.png"
        click id "trim_chip_0"
        click id "trim_chip_1"
        click id "trim_chip_3"
        click id "trim_chip_4"
        click id "trim_chip_6"
        click id "trim_submit"
        click id "trim_chip_0"
        click id "trim_chip_1"
        click id "trim_chip_4"
        click id "trim_submit"
        advance until screen "main_menu" timeout 20.0
        assert eval persistent.minigame_best.get("trim") == 3

    testcase spot:
        run [SetField(persistent, "mg_pending", "spot"), Start("minigame_free")]
        click id "spot_logo"
        click id "spot_head"
        screenshot "mg-5-spot.png"
        click id "spot_arrow"
        click id "spot_date"
        advance until screen "main_menu" timeout 20.0
        assert eval persistent.minigame_best.get("spot") == 3

    teardown:
        exit
