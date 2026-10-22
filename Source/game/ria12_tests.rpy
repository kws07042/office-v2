# Internal native tests; excluded from local delivery builds.
init python:
    ria12_fixture = {}

label test_ria12_entry:
    scene bg plain
    $ speech_informal = bool(ria12_fixture["case"] & 1)
    $ active_route = "ria"
    $ dating = True
    $ afterwork_preference = ["quiet", "meal", "suggestion", None][ria12_fixture["case"] % 4]
    $ memory = {"ria_publicity": "private", "ria_contact_agreement": "평소 답장은 여유 있게, 약속 변경은 알게 된 때 연락"}
    if ria12_fixture["case"] % 4 != 3:
        $ remember("ria_r05_booklet_subject", "화분과 그림자" if ria12_fixture["case"] & 1 else "골목의 긴 그림자")
    $ affinity = {"ria": 49, "jihyun": 0, "yujin": 0, "seoyun": 0}
    $ trust_ria = 3
    $ completed = ["ria_R08"]
    call ria_r09
    call ria_r10
    call ria_o02_offer
    call ria_r11
    call ria_r12
    menu:
        "검사 종료":
            pass
    return

label test_ria12_guard:
    $ active_route = "ria" if ria12_fixture["case"] == 0 else "jihyun"
    $ dating = bool(ria12_fixture["case"])
    call ria_r09
    call ria_r10
    call ria_o02_offer
    call ria_o02
    call ria_r11
    call ria_r12
    menu:
        "진입 조건 검사 종료":
            pass
    return

init python:
    def ria12_done():
        sc = renpy.get_screen("choice")
        return bool(sc and sc.scope["items"][0].caption == "검사 종료")
    def ria12_current_caption():
        caps = [renpy.substitute(i.caption) for i in renpy.get_screen("choice").scope["items"]]
        case = ria12_fixture["case"]
        if chapter.startswith("리아 R09"):
            return caps[case & 1]
        if chapter.startswith("리아 R10") and "ria_r10_place" not in memory:
            return caps[1 if case & 8 else 0]
        if chapter.startswith("리아 R10") and "(선택 일상)" not in caps[0]:
            return caps[0 if case & 4 or case == 0 and not ria12_fixture.get("public_restored") else 1]
        if "(선택 일상)" in caps[0]:
            return caps[0 if case % 3 else 1]
        if chapter.startswith("리아 O02"):
            return caps[1 if case & 4 else 0]
        if chapter.startswith("리아 R11"):
            return caps[1 if ((case >> 1) ^ (case >> 3)) & 1 else 0]
        if chapter.startswith("리아 R12"):
            if any("친밀한 장면" in x for x in caps):
                return caps[0 if case & 16 or case == 0 and not ria12_fixture.get("intimacy_restored") else 1]
            return caps[1 if case & 16 else 0]
        return caps[0]

testsuite ria12:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase branch_and_restore:
        parameter case = list(range(32))
        $ ria12_fixture.clear()
        $ ria12_fixture["case"] = case
        run Start("test_ria12_entry")
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        if not eval ria12_done():
            advance until eval ria12_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    assert eval memory["ria_r12_intimacy"] == "deferred"
                    click id "phone_reply_fixed"
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval ria12_done():
                if eval case == 0 and chapter.startswith("리아 R10") and memory.get("ria_r10_place") and not ria12_fixture.get("public_saved") and "(선택 일상)" not in renpy.get_screen("choice").scope["items"][0].caption:
                    run FileSave("3", confirm=False)
                    $ ria12_fixture["public_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R11") and not ria12_fixture.get("public_restored"):
                    assert eval memory["ria_publicity"] == "told_seoyun"
                    assert eval any(r["id"] == "ria_disclosure_2" for r in phone_threads["seoyun"])
                    run FileLoad("3", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_disclosure_done" not in memory and "ria_o02_status" not in memory
                    assert eval phone_threads["seoyun"] == []
                    $ ria12_fixture["public_restored"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and any("친밀한 장면" in i.caption for i in renpy.get_screen("choice").scope["items"]) and not ria12_fixture.get("intimacy_saved"):
                    run FileSave("4", confirm=False)
                    $ ria12_fixture["intimacy_saved"] = True
                if eval case == 0 and chapter.startswith("리아 R12") and memory.get("ria_r12_intimacy") == "shared" and not ria12_fixture.get("intimacy_restored"):
                    run FileLoad("4", confirm=False)
                    assert screen "choice" timeout 10.0
                    assert eval "ria_r12_intimacy" not in memory and "ria_r12_next_appointment" not in memory
                    assert eval not event_presentations
                    $ ria12_fixture["intimacy_restored"] = True
                click expression ria12_current_caption()
        assert eval ria12_done()
        assert eval memory["ria_r09_competence_seen"] and memory["ria_r09_support"] == ("organize" if case & 1 else "explain")
        assert eval memory["ria_r10_place"] == ("bakery" if case & 8 else "park")
        assert eval "아직" in memory["ria_r10_booklet_state"]
        assert eval memory["ria_publicity"] == ("told_seoyun" if case & 4 else "private")
        assert eval memory.get("ria_known_colleagues", []) == (["seoyun"] if case & 4 else [])
        assert eval any(r["id"] == "ria_disclosure_2" and r["sender"] == "seoyun" for r in phone_threads["seoyun"]) == bool(case & 4)
        assert eval memory["ria_o02_status"] == ("completed" if case % 3 else "skipped")
        assert eval bool(memory.get("ria_o02_name")) == bool(case % 3)
        assert eval memory["ria_r11_menu"] == ("rice" if ((case >> 1) ^ (case >> 3)) & 1 else "pasta")
        assert eval memory["ria_r12_intimacy"] == ("shared" if case & 16 else "deferred")
        assert eval memory["ria_r12_expectation"] == ("hope_early" if case & 16 else "fixed")
        assert eval memory["ria_r12_next_appointment_status"] == "scheduled"
        assert eval memory["ria_r12_next_appointment"] == "일요일 오후 네 시, 변경은 서로 다시 확인"
        assert eval affinity["ria"] == 63 + (2 if case % 3 else 0)
        assert eval dating and trust_ria == 3 and speech_informal == bool(case & 1)
        if eval case == 0:
            assert eval ria12_fixture["public_restored"] and ria12_fixture["intimacy_restored"]
        $ award_once("ria_R12", "ria", 4)
        assert eval affinity["ria"] == 63 + (2 if case % 3 else 0)

    testcase guard:
        parameter case = [0, 1]
        $ ria12_fixture["case"] = case
        run Start("test_ria12_guard")
        advance until screen "choice"
        assert eval memory == {} and completed == [] and sum(affinity.values()) == 0

    teardown:
        exit
