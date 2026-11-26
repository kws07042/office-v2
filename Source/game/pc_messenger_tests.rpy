# 사내 메신저(C08 선택) 검사. 배포 패키지에 넣지 않는다.
label test_pc_c08_entry:
    scene bg plain
    $ speech_informal = False
    call c08
    return

label test_pc_chat_entry:
    scene bg plain
    $ location = "월요일 오후 · 사무실"
    call pc_chat("seoyun", [("seoyun", "안 가?"), ("dohyun", "...가도 되는지 모르겠어서요."), ("seoyun", "가도 되는지 묻고 갈 거면 평생 못 가. 물이나 갖다 놔. 말은 안 해도 돼.")])
    $ pc_chat_done = True
    "끝."
    return

testsuite pc_messenger_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase pc_c08_pick_ria:
        run Start("test_pc_c08_entry")
        advance until screen "choice" timeout 30.0
        assert eval renpy.get_widget("choice", "pc_contact_ria") is not None
        pause 0.6
        screenshot "pc-messenger-1-c08.png"
        assert eval renpy.get_screen("choice").scope["pc"]
        click id "pc_pick_ria" until not screen "choice"
        advance until screen "office_phone" timeout 20.0
        assert eval active_route == "ria" and phone_threads["ria"] and phone_threads["ria"][-1]["sender"] == "dohyun"
        assert eval all(not phone_threads[k] for k in ("jihyun", "yujin", "seoyun"))
        screenshot "pc-messenger-2-phone.png"

    testcase pc_c08_preview_then_confirm:
        run Start("test_pc_c08_entry")
        advance until screen "choice" timeout 30.0
        click id "pc_contact_seoyun"
        assert screen "choice"
        click id "pc_contact_jihyun"
        assert eval renpy.get_widget("choice", "pc_pick_jihyun") is not None
        click id "pc_pick_jihyun"
        advance until screen "office_phone" timeout 20.0
        assert eval active_route == "jihyun"

    testcase pc_c08_colleague_uses_plain_menu:
        run Start("test_pc_c08_entry")
        advance until screen "choice" timeout 30.0
        click id "pc_extra_0"
        advance until screen "choice" timeout 10.0
        assert eval not renpy.get_screen("choice").scope.get("pc")

    testcase pc_chat_advances_line_by_line:
        $ pc_chat_done = False
        $ pc_chat_test_hold = True
        run Start("test_pc_chat_entry")
        advance until screen "pc_chat_screen" timeout 20.0
        assert eval pc_chat_n == 1
        keysym "dismiss"
        pause 0.2
        assert eval pc_chat_n == 2
        click id "pc_next"
        pause 0.4
        screenshot "pc-messenger-3-chat.png"
        assert eval pc_chat_n == 3
        advance until eval pc_chat_done timeout 10.0
        assert eval not renpy.get_screen("pc_chat_screen")
        $ pc_chat_test_hold = False

    testcase pc_chat_single_advance_in_tests:
        $ pc_chat_done = False
        $ pc_chat_test_hold = False
        run Start("test_pc_chat_entry")
        advance until screen "pc_chat_screen" timeout 20.0
        advance
        assert eval pc_chat_done

    teardown:
        exit
