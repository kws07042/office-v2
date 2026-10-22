# Isolated review paths. Excluded from the Windows production package.
init python:
    date_review_fixture = {"case": 0}
    def date_review_finished():
        sc = renpy.get_screen("choice")
        return sc is not None and sc.scope["items"][0].caption == "데이트 검사 종료"
    def date_review_caption():
        return renpy.get_screen("choice").scope["items"][date_review_fixture["case"] % 3].caption

label test_date_optional_entry:
    $ dating = True
    $ first_kiss = False
    $ memory = {}
    $ completed = []
    $ affinity = {"ria": 0, "jihyun": 0, "yujin": 0, "seoyun": 0}
    $ active_route = "jihyun" if date_review_fixture["case"] < 3 else ("seoyun" if date_review_fixture["case"] < 6 else "yujin")
    $ cream_focus = active_route
    if active_route == "jihyun":
        call jihyun_o03
    elif active_route == "seoyun":
        call seoyun_o03
    else:
        $ memory["yujin_r10_page"] = ["entrance_bench", "one_sentence", "open_space"][(date_review_fixture["case"] - 6) // 3]
        call yujin_o03
    menu:
        "데이트 검사 종료":
            pass
    return

testsuite date_experience_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase all_optional_replies_and_yujin_places:
        parameter case = list(range(15))
        $ date_review_fixture["case"] = case
        run Start("test_date_optional_entry")
        advance until screen "choice"
        assert eval not date_review_finished()
        click expression date_review_caption()
        advance until eval date_review_finished()
        assert eval memory[active_route + "_o03_status"] == "completed"
        assert eval affinity[active_route] == 2
        assert eval completed == [active_route + "_O03"]
        if eval case < 3:
            assert eval memory["jihyun_o03_request"] == ["그늘 휴식 뒤 도현이 고른 빵집", "삼십 분 휴식 후 각자 귀가, 저녁 재회", "기록집 한 줄의 첫 감상 부탁"][case % 3]
        elif eval case < 6:
            assert eval memory["seoyun_o03_detail"] == ["옮겨진 작은 조명 아래 새 자리", "같은 책 선반 앞에서 오늘의 노트를 놓은 자리", "처음 고른 창가의 식물 그림자"][case % 3]
        else:
            assert eval memory["yujin_o03_action"] == ["photo", "sentence", "stay"][case % 3]
            assert eval bool(memory.get("yujin_o03_photo_taken")) == (case % 3 == 0)
            assert eval location == ["일요일 오후 · 전시 공간 입구의 긴 의자", "일요일 오후 · 조용한 동네 카페", "일요일 오후 · 동네 산책길"][(case - 6) // 3]
        assert eval dating and first_kiss == False

    teardown:
        exit
