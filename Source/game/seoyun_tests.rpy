init python:
    seoyun_fixture = {"case":0,"decline_done":False,"common":False,"epilogue":0}
    def seoyun_test_done():
        v=renpy.get_screen("choice")
        return bool(v and any(x.caption=="검사 종료" or "수록 구간을 마쳤습니다" in x.caption for x in v.scope["items"]))
    def seoyun_test_caption():
        caps=[renpy.substitute(x.caption) for x in renpy.get_screen("choice").scope["items"]]
        c=seoyun_fixture["case"]
        if caps[0].startswith("피칭이 끝날 때까지 기다리지 않고"):
            return caps[1 if seoyun_fixture.get("after_discussion_exit") else 0]
        if chapter.startswith("C"):
            if chapter.startswith("C08"):
                return next(x for x in caps if x.startswith("한서윤과"))
            if any(x.startswith("서윤에게") for x in caps):
                return next(x for x in caps if x.startswith("서윤에게"))
            if any(x.startswith("서윤과 확인") for x in caps):
                return next(x for x in caps if x.startswith("서윤과 확인"))
            return caps[0]
        if caps[0].startswith("후일담 읽기"):
            i=seoyun_fixture["epilogue"] if seoyun_fixture["common"] else (1 if c==13 else (2 if c==14 else 0))
        elif "(선택 일상)" in caps[0]:
            i=1 if c==12 else c%3
        elif chapter.startswith("서윤 R04"):
            if caps[0].startswith("동료로 지내겠다는"):
                seoyun_fixture["decline_done"]=True
                i=c-15
            elif caps[0].startswith("나도 좋아하며"):
                i=2 if c in (15,16,17) and not seoyun_fixture["decline_done"] else (1 if c in (18,19) and not seoyun_prepared else 0)
            else:
                i=2 if c==12 else (c//3)%3
        elif chapter.startswith("서윤 R06"):
            i=c%3 if "seoyun_private_name" not in memory else (c//3)%3
        elif chapter.startswith("서윤 R10"):
            i=c%3 if "seoyun_booklet_sentence" not in memory else (c//3)%3
        elif chapter.startswith("서윤 R14"):
            i=c-9 if caps[0].startswith("관계 종료를 확정") else (2 if c in (9,10,11) else c%2)
        elif chapter.startswith("서윤 R15"):
            if caps[0].startswith("보고 싶다는 마음"):
                i=c%3
            elif "생활복" in caps[0]:
                i=(c//3)%3
            else:
                i=1 if c==12 else (c+2)%3
        elif chapter.startswith("서윤 R07"):
            i=1 if c==12 else c%3
        elif chapter.startswith("서윤 R12"):
            i=1 if c==12 else (c+1)%3
        elif chapter.startswith("서윤 R02"):
            i=(c//3)%3 if "seoyun_r02_response" not in memory else c%3
        else:
            i=c%3
        return caps[i]

label test_seoyun_entry:
    $ memory = {}
    $ affinity = {"ria":0,"jihyun":0,"yujin":0,"seoyun":0}
    $ speech_informal = bool(seoyun_fixture["case"]%2)
    if seoyun_fixture["case"]%4 < 3:
        $ remember("seoyun_intro",["humor","clarify","draft"][seoyun_fixture["case"]%4])
        $ c06_person = "seoyun"
        $ c06_topic = ["today","weekend","place"][seoyun_fixture["case"]%3]
    if seoyun_fixture["case"]%2==0:
        $ remember("booklet_known_seoyun")
    if seoyun_fixture["case"]%3==0:
        $ remember("c07_seoyun_next_question")
    call seoyun_route
    $ remember("seoyun_test_complete")
    menu:
        "검사 종료":
            pass
    return

label test_seoyun_guards:
    $ active_route = "seoyun"
    $ dating = True
    call seoyun_r04
    call seoyun_r14
    call seoyun_r15
    call seoyun_r16
    call seoyun_e01
    $ remember("seoyun_guard_done")
    menu:
        "검사 종료":
            pass
    return

label test_seoyun_late_exit:
    $ active_route = "seoyun"
    $ dating = True
    $ memory = {"seoyun_family_disclosed": True, "seoyun_family_state": "divorced", "seoyun_conflict": "discussing"}
    $ affinity = {"ria": 0, "jihyun": 0, "yujin": 0, "seoyun": 0}
    call seoyun_r14
    $ remember("seoyun_late_exit_test_complete")
    menu:
        "검사 종료":
            pass
    return

testsuite seoyun_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent,"phone_typing_enabled",False)
        run SetField(persistent,"local_seoyun_ending",False)
        $ seoyun_fixture.update(common=False,decline_done=False,after_discussion_exit=False)

    testcase full_choices_and_relationships:
        parameter case = list(range(21))
        $ seoyun_fixture["case"] = case
        run Start("test_seoyun_entry")
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    if eval case==0:
                        screenshot "seoyun-phone-three-replies.png"
                        run FileSave("71",confirm=False)
                        click id "phone_reply_invite"
                        advance until screen "choice"
                        assert eval memory["seoyun_r08_reply"] == "invite"
                        run FileLoad("71",confirm=False)
                        assert screen "office_phone" timeout 10.0
                        assert eval phone_context == "seoyun_r08_reply" and "seoyun_r08_reply" not in memory
                    click id ("phone_reply_"+["miss","story","invite"][case%3])
            elif screen "event_cut":
                if eval case==1:
                    click id "cut_skip"
                else:
                    click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                if eval chapter.startswith("서윤 R04") and not dating:
                    assert eval affinity["seoyun"]==19
                if eval chapter.startswith("서윤 R13"):
                    assert eval memory["seoyun_conflict"]=="open" and not memory.get("seoyun_repair_performed")
                    assert eval cream_relation_name("seoyun")=="약속 조율 중"
                    if eval case==0:
                        screenshot "seoyun-future-conflict.png"
                if eval chapter.startswith("서윤 R14") and not memory.get("seoyun_repair_performed"):
                    assert eval not memory.get("seoyun_repair_performed")
                    if eval case==0:
                        run FileSave("72",confirm=False)
                        click expression seoyun_test_caption()
                        advance until screen "choice"
                        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and memory["seoyun_repair_performed"] and not memory.get("seoyun_continues_after_discussion")
                        run FileLoad("72",confirm=False)
                        assert screen "choice" timeout 10.0
                        assert eval memory["seoyun_conflict"]=="discussing" and "seoyun_repair_performed" not in memory
                if eval case==0 and chapter.startswith("서윤 E01"):
                    screenshot "seoyun-epilogue-date.png"
                click expression seoyun_test_caption()
        assert eval memory.get("seoyun_test_complete") and seoyun_test_done()
        assert eval memory["seoyun_r01_appointment"] == "수요일 저녁 일곱 시, 회사 앞 카페"
        assert eval memory["seoyun_promise"] == ["photo","sound","rest"][case%3]
        assert eval bool(memory.get("seoyun_booklet_introduced")) == bool(case%2)
        assert eval not any(k.startswith("ria_r") or k.startswith("yujin_r") or k.startswith("jihyun_r") for k in memory)
        if eval case==15:
            assert eval ending=="colleague" and not dating and not memory.get("seoyun_r04_complete")
            assert eval not memory.get("seoyun_route_completed") and not persistent.local_seoyun_ending
            assert eval "seoyun_R05" not in completed and not event_presentations
        else:
            assert eval memory["seoyun_r04_complete"]
            assert eval first_kiss == (case!=12 and (case//3)%3==0)
            assert eval memory["seoyun_r08_reply"] == ["miss","story","invite"][case%3]
            assert eval bool(memory.get("seoyun_shared_morning")) == (case%3==0 and case!=12)
            assert eval memory["seoyun_publicity"] == ("told_yujin" if (case//3)%3==0 else ["agreed_yujin","private","discuss_later"][(case//3)%3])
            assert eval bool(memory.get("seoyun_disclosure_delivered")) == ((case//3)%3==0)
            assert eval len([r for r in phone_threads["seoyun"] if r["id"]=="seoyun_r08_reply" and r["sender"]=="dohyun"])==1
            assert eval len([r for r in phone_threads["seoyun"] if r["id"]=="seoyun_r08_confirm"])==1
            assert eval len([r for r in phone_threads["seoyun"] if r["id"] in ("seoyun_r12_tuesday","seoyun_r12_thursday","seoyun_r12_reply")])==3
            assert eval phone_context is None and not cream_ria_visible() and not cream_yujin_visible()
            assert eval memory["seoyun_r07_pace"] == ("deferred" if case==12 else ["shared","deferred","talk"][case%3])
            assert eval memory["seoyun_r12_pace"] == ("deferred" if case==12 else ["shared","deferred","talk"][(case+1)%3])
            if eval case==9:
                assert eval ending=="seoyun_relationship_closed" and not dating
                assert eval cream_relation_name("seoyun")=="동료로 지내는 중"
                assert eval not memory.get("seoyun_repair_performed") and not memory.get("seoyun_route_completed") and not persistent.local_seoyun_ending
                assert eval "seoyun_R15" not in completed and "seoyun_E01" not in completed
            else:
                assert eval ending=="seoyun_good" and dating and persistent.local_seoyun_ending
                assert eval memory.get("seoyun_family_disclosed") and memory.get("seoyun_family_state")=="divorced"
                assert eval memory.get("seoyun_continues_after_discussion") and memory.get("seoyun_trust_status")=="mutual_answers_confirmed"
                assert eval memory["seoyun_route_completed"] and memory["seoyun_conflict"]=="resolved" and memory["seoyun_repair_performed"]
                assert eval cream_relation_name("seoyun")=="교제 중"
                assert eval memory["seoyun_r15_pace"] == ("deferred" if case==12 else ["shared","deferred","talk"][(case+2)%3])
                assert eval memory["seoyun_r15_outfit"] == ("cosplay" if (case//3)%3==1 else "home")
                assert eval len(event_presentations)==(0 if case==12 else 1)
                assert eval all(not v["loaded_asset_ids"] for v in event_presentations.values())
                assert eval bool(memory.get("seoyun_epilogue_completed"))==(case!=13)
                if eval case!=13:
                    assert eval memory["seoyun_cohabitation_status"]=="결혼·동거 확약 없음, 주변 공개는 둘이 정한 때에"
                assert eval affinity["seoyun"]==69+(0 if case==13 else 8)+(6 if case%3==0 and case!=12 else 0)
                assert eval all(memory["seoyun_o0"+str(n)+"_status"]==("skipped" if case==12 else ["completed","skipped","brief"][case%3]) for n in range(1,4))
                if eval case==11:
                    assert eval memory["seoyun_continuation_reconfirmed"]
                if eval case in (18,19):
                    assert eval memory["seoyun_prepared_conversation"]
                $ seoyun_score_before=affinity["seoyun"]
                $ award_once("seoyun_R16","seoyun",4)
                assert eval affinity["seoyun"]==seoyun_score_before

    testcase exit_after_actual_discussion:
        run Start("test_seoyun_late_exit")
        advance until screen "choice"
        assert eval not memory.get("seoyun_repair_performed")
        click "수요일에 서로 원하는 만남부터 이야기하자고 한다."
        advance until screen "choice"
        assert eval memory.get("seoyun_repair_performed") and memory.get("seoyun_future_boundary_confirmed")
        assert eval memory["seoyun_conflict"]=="agreed_pending_action" and not memory.get("seoyun_continues_after_discussion")
        click "이야기를 들었지만 연애는 여기서 마치기로 한다."
        advance until screen "choice"
        assert eval seoyun_test_done() and not dating and ending=="seoyun_relationship_closed"
        assert eval memory.get("seoyun_late_exit_test_complete") and not memory.get("seoyun_route_completed")
        assert eval not persistent.local_seoyun_ending

    testcase no_unearned_finale:
        run Start("test_seoyun_guards")
        advance until screen "choice"
        assert eval memory.get("seoyun_guard_done") and not completed
        assert eval not memory.get("seoyun_route_completed") and not persistent.local_seoyun_ending

    testcase preview_entry:
        screenshot "seoyun-main-menu.png"
        click id "seoyun_preview_button"
        advance until screen "office_phone"
        assert eval active_route=="seoyun" and phone_active_contact=="seoyun" and not memory.get("seoyun_intro")

    testcase common_to_seoyun:
        parameter epilogue=[0,1,2]
        $ seoyun_fixture.update(case=0,common=True,epilogue=epilogue)
        run Start()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        if not eval seoyun_test_done():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id "phone_reply_miss"
            elif screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif not eval seoyun_test_done():
                click expression seoyun_test_caption()
        assert eval seoyun_test_done() and active_route=="seoyun" and ending=="seoyun_good"
        assert eval memory["seoyun_intro"]=="humor" and memory["seoyun_route_completed"]
        assert eval c06_person=="seoyun" and memory["c07_seoyun_next_question"]
        assert eval bool(memory.get("seoyun_epilogue_completed"))==(epilogue!=1)
        assert eval bool(memory.get("seoyun_epilogue_bridge"))==(epilogue==2)
        assert eval bool(memory.get("seoyun_epilogue_skipped"))==(epilogue==1)

    teardown:
        exit
