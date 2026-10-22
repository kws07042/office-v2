# Marriage disclosure choice regression. No production assets.
testsuite marriage_disclosure_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase choose_after_facts:
        parameter leave = [False, True]
        $ seoyun_fixture.update(case=0, common=False, decline_done=False, epilogue=0, after_reveal_exit=leave)
        run Start("test_seoyun_entry")
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval seoyun_test_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R12"):
                    assert eval not memory.get("seoyun_marriage_revealed")
                if eval renpy.get_screen("choice").scope["items"][0].caption.startswith("혼인 사실을 안 상태로"):
                    assert eval memory.get("seoyun_marriage_revealed") and memory.get("seoyun_marriage_state") == "married_cohabiting"
                    screenshot ("marriage-disclosure-" + ("exit" if leave else "continue") + ".png")
                click expression seoyun_test_caption()
        assert eval seoyun_test_done()
        assert eval memory.get("seoyun_marriage_revealed")
        assert eval memory.get("seoyun_marriage_state") == "married_cohabiting"
        if eval leave:
            assert eval ending == "seoyun_relationship_closed" and not dating
            assert eval "seoyun_R15" not in completed and not memory.get("seoyun_route_completed")
            assert eval not memory.get("seoyun_continues_after_disclosure")
        else:
            assert eval ending == "seoyun_good" and dating
            assert eval memory.get("seoyun_continues_after_disclosure")
            assert eval memory.get("seoyun_cohabitation_status") == "동거 약속 없음, 배우자와 동거 중인 기혼 관계 지속"
            assert eval memory.get("seoyun_trust_status") == "damaged_not_restored"

    teardown:
        exit
