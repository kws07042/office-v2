# 사내 메신저(C08 선택) 검사. 배포 패키지에 넣지 않는다.
label test_pc_c08_entry:
    scene bg plain
    $ speech_informal = False
    call c08
    return

testsuite pc_messenger_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase pc_c08_pick_jihyun:
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

    testcase pc_c08_caption_click_still_works:
        run Start("test_pc_c08_entry")
        advance until screen "choice" timeout 30.0
        click "백지현과 다음 약속 잡기 — 단정한 연상과 의견을 주고받으며 가까워지는 연애."
        advance until screen "office_phone" timeout 20.0
        assert eval active_route == "jihyun"

    testcase pc_c08_colleague_uses_plain_menu:
        run Start("test_pc_c08_entry")
        advance until screen "choice" timeout 30.0
        click id "pc_extra_0"
        advance until screen "choice" timeout 10.0
        assert eval not renpy.get_screen("choice").scope.get("pc")

    teardown:
        exit
