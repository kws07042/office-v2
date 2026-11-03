init python:
    yujin_fixture = {"case":0}

    def yujin_test_choice(index=0):
        return renpy.substitute(renpy.get_screen("choice").scope["items"][index].caption)

    def yujin_test_menu_end():
        view = renpy.get_screen("choice")
        return bool(view and any("수록 구간을 마쳤습니다" in x.caption for x in view.scope["items"]))

    def yujin_test_common_choice():
        captions = [renpy.substitute(x.caption) for x in renpy.get_screen("choice").scope["items"]]
        if chapter.startswith("C08"):
            return next(x for x in captions if x.startswith("차유진과"))
        return captions[0]

label test_yujin_entry:
    $ active_route = "yujin"
    $ speech_informal = bool(yujin_fixture["case"] % 2)
    $ affinity = {"ria":0, "jihyun":0, "yujin":0, "seoyun":0}
    $ memory = {}
    if yujin_fixture["case"] // 3 < 3:
        $ remember("yujin_intro", ["flow", "message", "process"][yujin_fixture["case"] // 3])
    call yujin_early_route
    $ remember("yujin_test_done")
    menu:
        "검사 종료":
            pass
    return

testsuite yujin_early_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase representative_branches:
        parameter case = list(range(12))
        $ yujin_fixture["case"] = case
        run Start("test_yujin_entry")
        advance until screen "office_phone"
        assert eval phone_active_contact == "yujin"
        click id "phone_next" until eval phone_context == "yujin_r01_reply"
        click id ("phone_reply_" + ["interest", "time", "reason"][case % 3])
        click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        assert eval memory["yujin_r01_reply"] == ["interest", "time", "reason"][case % 3]
        assert eval memory["yujin_r01_appointment"] == "토요일 오후 두 시, 작은 전시 공간 입구"
        click expression yujin_test_choice(case % 3)
        advance until screen "choice"
        click expression yujin_test_choice((case // 3) % 3)
        advance until screen "office_phone"
        assert eval memory["yujin_r02_touch"] == ["hand", "later", "talk"][(case // 3) % 3]
        assert eval ("손 놓을 때까지" in phone_threads["yujin"][-1]["text"]) == ((case // 3) % 3 == 0)
        assert eval not cream_ria_visible()
        if eval case == 0:
            screenshot "yujin-r03-hand-memory.png"
        click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        click expression yujin_test_choice((case + 1) % 3)
        advance until screen "choice"
        assert eval memory["yujin_core_understanding"] is True
        assert eval not dating
        if eval case == 0:
            screenshot "yujin-confession-choice.png"
        if eval case % 4 == 0:
            click "마음은 있지만 더 이야기하고 싶다고 말한다."
            advance until screen "choice"
            assert eval yujin_prepared and memory["yujin_prepared_conversation"]
            assert eval not dating
        if eval case % 4 in (1,2):
            click "이번 회차는 연애를 시작하지 않고 동료로 지낸다 — 동료 결말로 이어짐."
            advance until screen "choice"
            if eval case % 4 == 1:
                click "동료로 지내겠다는 뜻을 확인한다."
            else:
                click "결정을 다시 고른다."
                advance until screen "choice"
        if eval case % 4 != 1:
            click "나도 유진과 연인으로 만나고 싶다고 답한다."
            advance until screen "choice"
            assert eval dating and memory["yujin_confession_accepted"]
            assert eval affinity["yujin"] == 24
            click expression yujin_test_choice(case % 3)
        advance until eval memory.get("yujin_test_done")
        assert eval memory.get("yujin_r04_complete", False) == (case % 4 != 1)
        assert eval dating == (case % 4 != 1)
        assert eval ending == ("colleague" if case % 4 == 1 else "yujin_early_segment_complete")
        assert eval all(not phone_threads[k] for k in ("ria", "jihyun", "seoyun"))
        assert eval len({row["id"] for row in phone_threads["yujin"]}) == len(phone_threads["yujin"])
        assert eval not any(x.startswith("ria_") for x in memory)
        assert eval first_kiss is False
        run Show("office_phone_archive")
        assert "차유진"
        screenshot "yujin-message-history.png"
        click id "phone_archive_close"

    testcase save_load_changes_real_touch_memory:
        $ yujin_fixture["case"] = 0
        run Start("test_yujin_entry")
        advance until screen "office_phone"
        click id "phone_next" until eval phone_context == "yujin_r01_reply"
        run FileSave("18", confirm=False)
        click id "phone_reply_interest"
        run FileLoad("18", confirm=False)
        click id "phone_reply_time"
        click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        assert eval memory["yujin_r01_reply"] == "time"
        click expression yujin_test_choice(0)
        advance until screen "choice"
        run FileSave("19", confirm=False)
        click expression yujin_test_choice(0)
        advance until screen "office_phone"
        assert eval memory["yujin_r02_touch"] == "hand"
        assert eval "손 놓을 때까지" in phone_threads["yujin"][-1]["text"]
        run FileLoad("19", confirm=False)
        click expression yujin_test_choice(1)
        advance until screen "office_phone"
        assert eval memory["yujin_r02_touch"] == "later"
        assert eval "손 놓을 때까지" not in phone_threads["yujin"][-1]["text"]
        assert eval len({row["id"] for row in phone_threads["yujin"]}) == len(phone_threads["yujin"])
        run Show("office_phone_archive")
        click id "phone_contact_ria"
        assert "아직 주고받은 메시지가 없어요."
        click id "phone_archive_close"

    testcase main_menu_preview:
        run ShowMenu("office_dev_menu")
        click id "yujin_preview_button"
        advance until screen "office_phone"
        assert eval active_route == "yujin" and phone_active_contact == "yujin"
        assert eval memory.get("yujin_intro") is None
        screenshot "yujin-preview-entry.png"

    testcase common_to_yujin_route:
        run Start()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
            if not eval yujin_test_menu_end():
                click expression yujin_test_common_choice()
        assert eval yujin_test_menu_end()
        assert eval active_route == "yujin"
        assert eval memory.get("yujin_r04_complete")
        assert eval memory.get("yujin_intro") == "flow"
        assert eval "yujin_R04" in completed and "ria_R01" not in completed
        assert eval dating
        assert eval ending == "yujin_early_segment_complete"

    teardown:
        exit
