init python:
    review_fixture = {"case":0}
    def review_history():
        return "\n".join(h.what for h in _history_list)

label test_review_ria09:
    $ active_route = "ria"
    $ dating = True
    $ speech_informal = bool(review_fixture["case"] % 2)
    call ria_r09
    $ remember("review_done")
    menu:
        "검사 종료":
            pass
    return

label test_review_yujin13:
    $ active_route = "yujin"
    $ dating = True
    $ memory = {"yujin_support_action":"materials","yujin_support_overstep":False}
    call yujin_r13
    $ remember("review_done")
    menu:
        "검사 종료":
            pass
    return

testsuite review_continuity_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase ria_actual_support_recalled:
        parameter case = list(range(6))
        $ review_fixture["case"] = case
        run Start("test_review_ria09")
        advance until screen "choice"
        click expression yujin_test_choice(case // 2)
        advance until eval memory.get("review_done")
        assert eval memory["ria_r09_support"] == ["explain","organize","rehearse"][case // 2]
        assert eval ("변경 이유는 직접 쓰시겠다고" in review_history() or "변경 이유는 네가 쓰겠다고" in review_history()) == (case // 2 == 1)
        assert eval ("직접 설명하신 거요" in review_history() or "네가 직접 설명한 거" in review_history()) == (case // 2 != 1)

    testcase yujin_selected_role_recalled:
        parameter plan = list(range(3))
        run Start("test_review_yujin13")
        advance until screen "choice"
        click expression yujin_test_choice(plan)
        advance until eval memory.get("review_done")
        assert eval ("자료 넘기는 데 집중" in review_history()) == (plan == 0)
        assert eval ("질문 순서랑 시간 메모에 집중" in review_history()) == (plan == 1)
        assert eval ("부탁하실 때까지 기다릴게요" in review_history()) == (plan == 2)
        assert eval not memory.get("yujin_support_repair_action_verified")

    teardown:
        exit
