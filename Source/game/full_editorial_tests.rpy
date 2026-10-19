init python:
    full_edit_case = 0

label test_full_edit_jihyun_time:
    $ active_route = "jihyun"
    $ dating = True
    $ memory = {}
    $ completed = []
    call jihyun_r10
    call jihyun_o02_offer
    call jihyun_r10_after
    menu:
        "검사 종료":
            pass
    return

label test_full_edit_ria_brief:
    $ active_route = "ria"
    $ dating = True
    $ completed = ["ria_R15"]
    $ memory = {"ria_conflict":"resolved"}
    $ location = "다음 날 월요일 아침 · 각자의 출근길" if full_edit_case else "일요일 밤 · 리아의 집"
    call ria_o03_offer
    menu:
        "검사 종료":
            pass
    return

label test_full_edit_ria_close:
    $ active_route = "ria"
    $ dating = True
    $ completed = ["ria_R13"]
    $ memory = {"ria_conflict":"discussing","ria_r13_response":"honest"}
    call ria_r14
    menu:
        "검사 종료":
            pass
    return

testsuite full_editorial_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent,"phone_typing_enabled",False)

    testcase optional_before_departure:
        parameter case = list(range(9))
        run Start("test_full_edit_jihyun_time")
        advance until screen "choice"
        click expression yujin_test_choice(case % 3)
        advance until screen "choice"
        click expression yujin_test_choice(1)
        advance until screen "choice"
        assert eval location == "토요일 오후 · 지현의 집"
        assert eval not memory.get("jihyun_r10_after_completed")
        assert eval not phone_threads.get("jihyun")
        click expression yujin_test_choice(case // 3)
        if eval case // 3 == 0:
            advance until screen "choice"
            assert eval location == "같은 토요일 오후 · 조립품 앞"
            click expression yujin_test_choice(case % 3)
        advance until screen "office_phone"
        assert eval location == "같은 토요일 밤 · 지현의 집 — 지현 시점"
        assert eval phone_threads["jihyun"][-1]["moment"] == "같은 토요일 밤"
        click id "phone_next"
        advance until screen "choice"
        assert eval memory.get("jihyun_r10_after_completed")
        assert eval memory["jihyun_o02_status"] == ["completed","skipped","brief"][case // 3]
        assert eval sum(1 for x in phone_threads["jihyun"] if x["id"] == "jihyun_r10_after") == 1

    testcase short_contact_after_sunday_or_monday:
        parameter case = [0,1]
        $ full_edit_case = case
        run Start("test_full_edit_ria_brief")
        advance until screen "choice"
        click expression yujin_test_choice(2)
        advance until screen "office_phone"
        assert eval location.startswith("그다음 화요일 저녁")
        click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        assert eval memory["ria_o03_status"] == "brief"
        assert eval not memory.get("ria_o03_rest")

    testcase relationship_confirmation_and_reconsideration:
        parameter case = [0,1,2]
        run Start("test_full_edit_ria_close")
        advance until screen "choice"
        click expression yujin_test_choice(1)
        advance until screen "choice"
        assert eval dating and not memory.get("ria_relationship_closed")
        click expression yujin_test_choice(case)
        if eval case == 0:
            advance until screen "choice"
            assert eval not dating and memory.get("ria_relationship_closed")
            assert eval "ria_R14" not in completed
        else:
            advance until screen "choice"
            assert eval dating and not memory.get("ria_relationship_closed")
            click expression yujin_test_choice(0)
            advance until screen "office_phone"
            click id "phone_next" until not screen "office_phone"
            advance until screen "choice"
            assert eval memory["ria_conflict"] == "resolved"
            assert eval memory.get("ria_r14_continuation_reconfirmed",False) == (case == 2)

    teardown:
        exit
