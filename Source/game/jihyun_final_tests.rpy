init python:
    jihyun_final_fixture = {"case":0}
    def jihyun_final_finished():
        s=renpy.get_screen("choice")
        return s is not None and s.scope["items"][0].caption == "검사 종료"
    def jihyun_final_caption():
        captions=[renpy.substitute(i.caption) for i in renpy.get_screen("choice").scope["items"]]
        c=jihyun_final_fixture["case"]
        if captions[0].startswith("관계 종료를 확정"):
            i=c-9
        elif captions[0].startswith("후일담 읽기"):
            i=1 if c==13 else (2 if c==14 else 0)
        elif "(선택 일상)" in captions[0]:
            i=1 if c==12 else c%3
        elif chapter.startswith("지현 R05"):
            i=c%3 if "jihyun_personal_slot" not in memory else (c//3)%3
        elif chapter.startswith("지현 R06"):
            i=c%3 if "jihyun_private_name" not in memory else (c//3)%3
        elif chapter.startswith("지현 R10"):
            i=c%3 if "jihyun_booklet_subject" not in memory else (c//3)%3
        elif chapter.startswith("지현 R14"):
            i=2 if c in (9,10,11) else c%2
        elif chapter.startswith("지현 R15"):
            if "같이 산책하되, 오전은 각자 쉰다." in captions[0]:
                i=c%3
            elif "생활복" in captions[0]:
                i=(c//3)%3
            else:
                i=(c+2)%3
        elif chapter.startswith("지현 R12"):
            i=(c+1)%3
        else:
            i=c%3
        return captions[i]

label test_jihyun_full_entry:
    $ active_route = "jihyun"
    $ cream_focus = "jihyun"
    $ dating = True
    $ affinity = {"ria":0,"jihyun":24,"yujin":0,"seoyun":0}
    $ memory = {"jihyun_r04_complete":True,"jihyun_next_date_plan":["dohyun_suggests","own_and_shared","both_suggest"][jihyun_final_fixture["case"]%3],"jihyun_publicity":"private"}
    $ completed = ["jihyun_R01","jihyun_R02","jihyun_R03","jihyun_R04"]
    call jihyun_r05
    call jihyun_o01_offer
    call jihyun_r06
    call jihyun_r07
    call jihyun_r08
    call jihyun_r09
    call jihyun_r10
    call jihyun_o02_offer
    call jihyun_r10_after
    call jihyun_r11
    call jihyun_r12
    call jihyun_r13
    call jihyun_r14
    call jihyun_r15
    call jihyun_o03_offer
    call jihyun_r16
    if memory.get("jihyun_route_completed"):
        menu:
            "후일담 읽기":
                call jihyun_e01
            "후일담은 생략":
                $ remember("jihyun_epilogue_skipped")
            "한마디 나누고 후일담 읽기":
                $ remember("jihyun_epilogue_bridge")
                call jihyun_e01
    $ remember("jihyun_final_test_done")
    menu:
        "검사 종료":
            pass
    return

label test_jihyun_guards_entry:
    $ active_route = "jihyun"
    $ dating = True
    $ memory = {}
    call jihyun_r14
    call jihyun_r15
    call jihyun_r16
    call jihyun_e01
    $ remember("jihyun_guard_done")
    menu:
        "검사 종료":
            pass
    return

testsuite jihyun_final_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)
        run SetField(persistent, "local_jihyun_ending", False)

    testcase full_route_choices_and_actual_memories:
        parameter case = list(range(16))
        $ jihyun_final_fixture["case"] = case
        run Start("test_jihyun_full_entry")
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        if not eval jihyun_final_finished():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case == 0:
                        screenshot "jihyun-r08-phone-replies.png"
                    click id ("phone_reply_" + ["restaurant","menu","affection"][case%3])
            elif screen "event_cut":
                if eval case == 1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval jihyun_final_finished():
                if eval case == 0 and chapter.startswith("지현 E01"):
                    screenshot "jihyun-epilogue-cohabitation-choice.png"
                if eval chapter.startswith("지현 R13"):
                    assert eval memory["jihyun_conflict"] == "open" and not memory.get("jihyun_r14_performed")
                    assert eval cream_relation_name("jihyun") == "약속 조율 중"
                    assert eval not persistent.local_jihyun_ending
                    if eval case == 0:
                        screenshot "jihyun-r13-conflict.png"
                        run FileSave("61",confirm=False)
                        click expression jihyun_test_choice(1)
                        advance until screen "choice"
                        assert eval memory["jihyun_r13_response"] == "roles"
                        run FileLoad("61",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["jihyun_conflict"] == "open" and "jihyun_r13_response" not in memory
                click expression jihyun_final_caption()
        assert eval jihyun_final_finished() and memory.get("jihyun_final_test_done")
        assert eval memory["jihyun_first_shared_slot_kept"] == memory["jihyun_shared_slot"]
        assert eval memory["jihyun_r08_reply"] == ["restaurant","menu","affection"][case%3]
        assert eval len([row for row in phone_threads["jihyun"] if row["id"] == "jihyun_r08_reply" and row["sender"]=="dohyun"]) == 1
        assert eval len([row for row in phone_threads["jihyun"] if row["id"] == "jihyun_r08_confirm" and row["sender"]=="jihyun"]) == 1
        assert eval phone_context is None
        assert eval first_kiss == ((case//3)%3 == 0)
        assert eval ("jihyun_r08_shared_morning" in memory) == (case%3 == 0)
        assert eval memory["jihyun_r07_pace"] == ["shared","deferred","talk"][case%3]
        assert eval memory["jihyun_r12_pace"] == ["shared","deferred","talk"][(case+1)%3]
        assert eval bool(memory.get("jihyun_disclosure_delivered")) == ((case//3)%3 == 0)
        assert eval memory["jihyun_conflict"] == "resolved" and memory["jihyun_r14_performed"]
        assert eval not cream_ria_visible() and not cream_yujin_visible()
        assert eval not any(k.startswith("yujin_r") or k.startswith("ria_r") for k in memory)
        if eval case == 9:
            assert eval cream_relation_name("jihyun") == "동료로 지내는 중"
            assert eval not dating and ending == "jihyun_relationship_closed"
            assert eval not memory.get("jihyun_route_completed") and not persistent.local_jihyun_ending
            assert eval "jihyun_R15" not in completed and "jihyun_E01" not in completed
        else:
            assert eval cream_relation_name("jihyun") == "교제 중"
            assert eval dating and ending == "jihyun_good" and persistent.local_jihyun_ending
            assert eval memory["jihyun_route_completed"] and "jihyun_R16" in completed
            assert eval memory["jihyun_r15_pace"] == ["shared","deferred","talk"][(case+2)%3]
            assert eval memory["jihyun_r15_outfit"] == ("cosplay" if (case//3)%3==1 else "home")
            assert eval len(event_presentations) == int(case%3==0)+int((case+1)%3==0)+int((case+2)%3==0)
            assert eval all(not v["loaded_asset_ids"] for v in event_presentations.values())
            assert eval bool(memory.get("jihyun_epilogue_completed")) == (case!=13)
            assert eval ("jihyun_cohabitation_status" in memory) == (case!=13)
            if eval case != 13:
                assert eval memory["jihyun_cohabitation_status"] == "동거 논의 시작, 계약·입주·동거 완료 아님"
                assert eval memory["jihyun_booklet_state"] == "이후 직접 촬영·글 정리를 마친 인쇄 기록집 완성"
            if eval case==11:
                assert eval memory["jihyun_continuation_reconfirmed"]
            assert eval affinity["jihyun"] == 69 + (0 if case==13 else 8) + (6 if case%3==0 and case!=12 else 0)
            assert eval all(memory["jihyun_o0"+str(n)+"_status"] == ("skipped" if case==12 else ["completed","skipped","brief"][case%3]) for n in range(1,4))
            if eval case==0:
                screenshot "jihyun-epilogue-cohabitation.png"
            $ jihyun_score_before = affinity["jihyun"]
            $ award_once("jihyun_R16","jihyun",4)
            assert eval affinity["jihyun"] == jihyun_score_before

    testcase no_unearned_finale:
        run Start("test_jihyun_guards_entry")
        advance until screen "choice"
        assert eval memory.get("jihyun_guard_done")
        assert eval not memory.get("jihyun_conflict") and not memory.get("jihyun_route_completed")
        assert eval not persistent.local_jihyun_ending and not completed

    teardown:
        exit
