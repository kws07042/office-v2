# Fresh CI saves only. Excluded from production by the existing *_tests rule.
init python:
    work_fixture = {}
    WORK_TEST_CHOICES = {
        "verify": (
            ("두 자료의 조사 시간부터 나란히 적는다.", "자료를 모은 담당자에게 물어볼 질문을 적는다.", "원본을 함께 펴고 비어 있는 칸을 확인한다."),
            ("언제 판단이 바뀌는지 한 줄로 적는다.", "확인할 사람과 시점을 붙인다.", "회의에서 확인된 것과 추정한 것을 따로 읽는다."),
        ),
        "coordinate": (
            ("각자 처음 보는 사람이 무엇을 알아야 하는지 묻는다.", "서로의 요청을 한 번씩 대신 말해 보고 확인받는다.", "각자 가장 빼기 싫은 한 부분에 표시하게 한다."),
            ("바꾸려는 예문 하나를 나란히 놓는다.", "처음 읽는 사람이 어떻게 받아들이는지 확인한다.", "이번에 바꾸지 않을 부분부터 적는다."),
        ),
        "try": (
            ("안내문의 위치만 바꾸고 발걸음을 본다.", "첫 줄 문구만 바꾸고 무엇을 읽었는지 묻는다.", "안내하는 사람의 서 있는 자리만 바꿔 본다."),
            ("예상과 실제 결과를 나란히 보여 준다.", "바꾼 부분 하나만 되돌려 짧게 다시 본다.", "다음 시험에서 볼 질문 하나를 정한다."),
        ),
    }
    WORK_TEST_VALUES = {
        "verify": (("conditions", "question", "original"), ("boundary", "owner", "say")),
        "coordinate": (("reader", "relay", "keep"), ("example", "reader", "scope")),
        "try": (("position", "headline", "guide"), ("show", "isolate", "next")),
    }

    def work_test_caption(stage, variant):
        return WORK_TEST_CHOICES[work_style][stage - 1][variant]

    def work_test_key(stage):
        return work_mini_id(work_style, stage).lower().replace("w_", "work_") + "_choice"

label test_work_pair:
    scene bg plain
    $ work_style = work_fixture["style"]
    $ c07_method = work_style
    $ active_route = work_fixture.get("route", "ria")
    $ speech_informal = work_fixture.get("informal", False)
    $ dating = False
    $ first_kiss = False
    $ prepared = False
    $ trust_ria = 1
    $ affinity = {"ria": 17, "jihyun": 17, "yujin": 17, "seoyun": 17}
    $ completed = ["fixture_prior"]
    $ memory = {"fixture_prior": True}
    $ _history_list = []
    call work_mini_first
    $ work_fixture["first_history_count"] = len(_history_list)
    call work_mini_first
    $ work_fixture["first_replay_history_count"] = len(_history_list)
    menu:
        "다음 업무 사건으로":
            pass
    $ dating = active_route != "colleague"
    call work_mini_second
    $ work_fixture["second_history_count"] = len(_history_list)
    call work_mini_second
    $ work_fixture["second_replay_history_count"] = len(_history_list)
    menu:
        "업무 검사 종료":
            pass
    return

label test_work_legacy:
    scene bg plain
    $ work_style = None
    $ c07_method = work_fixture["style"]
    $ active_route = "colleague"
    $ dating = False
    $ memory = {"fixture_prior": True}
    $ affinity = {"ria": 17, "jihyun": 17, "yujin": 17, "seoyun": 17}
    $ completed = ["fixture_prior"]
    $ _history_list = []
    call work_mini_second
    menu:
        "업무 검사 종료":
            pass
    return

label test_work_no_context:
    $ work_style = None
    $ c07_method = None
    $ active_route = "ria"
    $ memory = {"fixture_prior": True}
    $ _history_list = []
    call work_mini_first
    call work_mini_second
    menu:
        "업무 검사 종료":
            pass
    return

label test_work_colleague_ending:
    scene bg plain
    $ work_style = work_fixture["style"]
    $ c07_method = work_style
    $ active_route = "colleague"
    $ dating = False
    $ memory = {}
    $ affinity = {"ria": 17, "jihyun": 17, "yujin": 17, "seoyun": 17}
    $ completed = ["fixture_prior"]
    call work_mini_first
    call end_common
    menu:
        "동료 결말 검사 종료":
            pass
    return

testsuite work_mini_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase all_styles_choices_routes_and_speech:
        parameter case = list(range(18))
        $ work_fixture.update(style=("verify", "coordinate", "try")[case // 6], route=("ria", "jihyun", "yujin", "seoyun", "colleague")[case % 5], informal=bool((case // 3) % 2))
        run Start("test_work_pair")
        advance until screen "choice"
        assert eval chapter.startswith(work_mini_id(work_style, 1))
        assert eval len(renpy.get_screen("choice").scope["items"]) == 3
        click expression work_test_caption(1, case % 3) until not screen "choice"
        advance until screen "choice"
        assert eval memory.get("work_stage_1") == work_mini_id(work_style, 1)
        assert eval memory.get(work_test_key(1)) == WORK_TEST_VALUES[work_style][0][case % 3]
        assert eval "work_stage_2" not in memory
        assert eval work_fixture["first_history_count"] == work_fixture["first_replay_history_count"]
        assert eval dating is False
        assert eval first_kiss is False
        assert eval prepared is False
        assert eval trust_ria == 1
        assert eval completed == ["fixture_prior"]
        assert eval all(value == 17 for value in affinity.values())
        click "다음 업무 사건으로" until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith(work_mini_id(work_style, 2))
        click expression work_test_caption(2, (case + 1) % 3) until not screen "choice"
        advance until screen "choice"
        assert eval memory.get("work_stage_2") == work_mini_id(work_style, 2)
        assert eval memory.get(work_test_key(2)) == WORK_TEST_VALUES[work_style][1][(case + 1) % 3]
        assert eval len([key for key in memory if key.startswith("work_") and key.endswith("_complete")]) == 2
        assert eval work_fixture["second_history_count"] == work_fixture["second_replay_history_count"]
        assert eval dating == (active_route != "colleague")
        assert eval first_kiss is False and prepared is False and trust_ria == 1
        assert eval completed == ["fixture_prior"]
        assert eval all(value == 17 for value in affinity.values())

    testcase save_load_restores_first_and_replaces_second_choice:
        parameter style = ["verify", "coordinate", "try"]
        $ work_fixture.update(style=style, route="ria", informal=True)
        run Start("test_work_pair")
        advance until screen "choice"
        click expression work_test_caption(1, 0) until not screen "choice"
        advance until screen "choice"
        run FileSave("work-mini-boundary", confirm=False)
        click "다음 업무 사건으로" until not screen "choice"
        advance until screen "choice"
        click expression work_test_caption(2, 0) until not screen "choice"
        advance until screen "choice"
        assert eval memory.get("work_stage_2") == work_mini_id(work_style, 2)
        run FileLoad("work-mini-boundary", confirm=False)
        assert screen "choice" timeout 10.0
        assert eval memory.get("work_stage_1") == work_mini_id(work_style, 1)
        assert eval "work_stage_2" not in memory
        assert eval memory.get(work_test_key(1)) == WORK_TEST_VALUES[work_style][0][0]
        assert eval dating is False
        click "다음 업무 사건으로" until not screen "choice"
        advance until screen "choice"
        click expression work_test_caption(2, 2) until not screen "choice"
        advance until screen "choice"
        assert eval memory.get(work_test_key(2)) == WORK_TEST_VALUES[work_style][1][2]
        assert eval completed == ["fixture_prior"]
        assert eval all(value == 17 for value in affinity.values())

    testcase legacy_method_does_not_invent_first_event:
        parameter style = ["verify", "coordinate", "try"]
        $ work_fixture["style"] = style
        run Start("test_work_legacy")
        advance until screen "choice"
        assert eval work_style == style
        click expression work_test_caption(2, 0) until not screen "choice"
        advance until screen "choice"
        assert eval memory.get("work_stage_2") == work_mini_id(style, 2)
        assert eval "work_stage_1" not in memory
        assert eval not any(key.endswith("01_complete") for key in memory)
        assert eval not any(any(marker in h.what for marker in ("지난번", "첫 방문객 역할", "숨은 종이")) for h in _history_list)
        assert eval dating is False
        assert eval completed == ["fixture_prior"]

    testcase colleague_wrapper_runs_both_events:
        parameter style = ["verify", "coordinate", "try"]
        $ work_fixture["style"] = style
        run Start("test_work_colleague_ending")
        advance until screen "choice"
        click expression work_test_caption(1, 0) until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith(work_mini_id(style, 2))
        click expression work_test_caption(2, 0) until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith("END_COMMON")
        assert eval ending == "colleague" and dating is False
        assert eval memory.get("work_stage_1") == work_mini_id(style, 1)
        assert eval memory.get("work_stage_2") == work_mini_id(style, 2)
        assert eval completed == ["fixture_prior"]
        assert eval all(value == 17 for value in affinity.values())

    testcase standalone_preview_without_prologue_stays_unchanged:
        run Start("test_work_no_context")
        advance until screen "choice"
        assert eval memory == {"fixture_prior": True}
        assert eval work_style is None
        assert eval len(_history_list) == 0

    teardown:
        exit
