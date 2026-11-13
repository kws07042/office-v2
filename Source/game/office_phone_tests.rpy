init python:
    phone_fixture = {"case": 0}

    def phone_message(mid):
        return next((row for row in phone_threads["ria"] if row["id"] == mid), None)

label test_phone_r08:
    $ active_route = "ria"
    $ dating = True
    $ speech_informal = bool(phone_fixture["case"] % 2)
    $ affinity = {"ria":58, "jihyun":0, "yujin":0, "seoyun":0}
    $ memory = {"ria_r07_intimacy": "shared" if phone_fixture["case"] >= 6 else "deferred"}
    if phone_fixture["case"] >= 6:
        $ remember("ria_o01_status", "completed")
    call ria_r08
    $ remember("phone_test_done")
    menu:
        "메신저 검사 종료":
            pass
    return

testsuite office_phone_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0
        run SetField(persistent, "phone_typing_enabled", True)

    testcase branches_and_speech_styles:
        parameter case = list(range(12))
        $ phone_fixture["case"] = case
        run Start("test_phone_r08")
        advance until screen "office_phone"
        click id "phone_next" until eval phone_context == "r08_reply"
        assert eval len(phone_threads["ria"]) == (3 if case >= 6 else 6)
        assert eval (phone_message("r08_morning_1") is not None) == (case < 6)
        assert eval all(not phone_threads[key] for key in ("jihyun", "yujin", "seoyun"))
        if eval case == 1:
            pause 0.2
            screenshot "phone-three-replies.png"
        click id ("phone_reply_" + ["miss", "evening", "small_memory"][(case // 2) % 3])
        click id "phone_next" until not screen "office_phone"
        advance until eval memory.get("phone_test_done")
        assert eval memory["ria_r08_reply"] == ["miss", "evening", "small_memory"][(case // 2) % 3]
        assert eval bool(memory.get("choice_third_r08_reply")) == ((case // 2) % 3 == 2)
        assert eval memory["ria_r08_messages_received"] is True
        assert eval affinity["ria"] == 62
        assert eval completed.count("ria_R08") == 1
        assert eval len({row["id"] for row in phone_threads["ria"]}) == len(phone_threads["ria"])
        assert eval phone_unread("ria") == 0
        assert eval phone_photo_opened == []
        assert eval memory.get("ria_r08_breakfast_shared", False) == (case >= 6)
        run Show("office_phone_archive")
        assert screen "office_phone_archive"
        if eval case == 1:
            screenshot "phone-history.png"
        click id "phone_archive_close"

    testcase save_load_and_photo_placeholder:
        $ phone_fixture["case"] = 1
        run Start("test_phone_r08")
        advance until screen "office_phone"
        click id "phone_next" until eval phone_context == "r08_reply"
        click id "phone_photo_ria_r08_breakfast"
        assert screen "office_phone_photo"
        assert eval "ria_r08_breakfast" in phone_photo_previews
        assert eval phone_photo_opened == []
        pause 0.2
        screenshot "phone-photo-placeholder.png"
        click id "phone_photo_close"
        click "저장" until screen "save"
        assert screen "save"
        screenshot "phone-save-menu.png"
        run FileSave("14", confirm=False)
        click "돌아가기" until not screen "save"
        click id "phone_reply_small_memory"
        assert eval memory["ria_r08_reply"] == "small_memory"
        run FileLoad("14", confirm=False)
        assert screen "office_phone" timeout 10.0
        assert eval phone_context == "r08_reply"
        assert eval "ria_r08_reply" not in memory
        assert eval phone_message("r08_reply") is None
        click id "phone_reply_evening"
        click id "phone_next" until not screen "office_phone"
        advance until eval memory.get("phone_test_done")
        assert eval memory["ria_r08_reply"] == "evening"
        assert eval "기록 좀 정리" in phone_message("r08_reply")["text"]
        assert eval not memory.get("choice_third_r08_reply")
        assert eval len(phone_threads["ria"]) == 11
        run Show("office_phone_archive")
        assert screen "office_phone_archive"
        click id "phone_contact_yujin"
        assert "아직 주고받은 메시지가 없어요."
        screenshot "phone-empty-contact.png"
        click id "phone_contact_ria"
        click id "phone_archive_photo"
        assert screen "office_phone_photo"
        click id "phone_photo_close"
        click id "phone_archive_close"

    testcase rollback_replaces_reply:
        $ phone_fixture["case"] = 1
        run Start("test_phone_r08")
        advance until screen "office_phone"
        click id "phone_next" until eval phone_context == "r08_reply"
        click id "phone_reply_miss"
        assert eval memory["ria_r08_reply"] == "miss"
        run Rollback()
        assert eval phone_context == "r08_reply"
        assert eval "ria_r08_reply" not in memory
        click id "phone_reply_small_memory"
        click id "phone_next" until not screen "office_phone"
        advance until eval memory.get("phone_test_done")
        assert eval memory["ria_r08_reply"] == "small_memory"
        assert eval "어제 나란히" in phone_message("r08_reply")["text"]
        assert eval affinity["ria"] == 62

    testcase typing_and_disabled_option:
        $ phone_fixture["case"] = 1
        run Start("test_phone_r08")
        advance until screen "office_phone"
        click id "phone_next" until eval phone_context == "r08_reply"
        click id "phone_reply_miss"
        click id "phone_next"
        assert eval renpy.get_screen("office_phone").scope.get("waiting") is True
        screenshot "phone-typing.png"
        run FileSave("15", confirm=False)
        click id "phone_next"
        assert eval phone_message("r08_answer") is not None
        run FileLoad("15", confirm=False)
        assert screen "office_phone"
        assert eval phone_message("r08_answer") is None
        click id "phone_next"
        assert eval phone_message("r08_answer") is not None
        run SetField(persistent, "phone_typing_enabled", False)
        click id "phone_next"
        click id "phone_next"
        assert eval phone_message("r08_answer_2") is not None
        assert eval not renpy.get_screen("office_phone").scope.get("waiting")
        run MainMenu(confirm=False)
        run Start("test_phone_r08")
        advance until screen "office_phone"
        assert eval persistent.phone_typing_enabled is False
        click id "phone_next" until eval phone_context == "r08_reply"
        click id "phone_reply_miss"
        click id "phone_next"
        assert eval phone_message("r08_answer") is not None
        assert eval not renpy.get_screen("office_phone").scope.get("waiting")

    testcase actual_photo_loader:
        $ phone_fixture["case"] = 1
        run Start("test_phone_r08")
        advance until screen "office_phone"
        # Existing master is an isolated loader fixture, never a story photo.
        $ PHONE_MEDIA["qa_fixture"] = {"path": RIA_MASTER_V2, "title": "QA image fixture"}
        run Function(phone_note_photo, "qa_fixture")
        run Show("office_phone_photo", media="qa_fixture")
        assert screen "office_phone_photo"
        assert eval phone_photo_opened == (["qa_fixture"] if renpy.loadable(RIA_MASTER_V2) else [])
        assert eval phone_media_ready("qa_fixture") == bool(renpy.loadable(RIA_MASTER_V2))
        screenshot "phone-real-image-loader-fixture.png"
        click id "phone_photo_close"

    testcase main_menu_preview_and_archive:
        click id "preview_toggle"
        click id "phone_preview_button" until not screen "main_menu"
        advance until screen "office_phone"
        assert eval dating is True and active_route == "ria"
        assert eval phone_message("r08_morning_1") is not None
        screenshot "phone-preview.png"

    teardown:
        exit
