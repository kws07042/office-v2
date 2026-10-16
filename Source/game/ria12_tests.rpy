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

testsuite ria12:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase branch_and_restore:
        parameter case = list(range(32))
        $ ria12_fixture["case"] = case
        run Start("test_ria12_entry")
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        click expression ("리아와 함께 전후 사진·질문 기록을 짧게 정리한다." if case & 1 else "리아가 판단 근거를 직접 설명하도록 질문을 건넨다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        assert eval memory["ria_r09_competence_seen"] is True
        assert eval memory["ria_r09_support"] == ("organize" if case & 1 else "explain")
        assert eval "ria_r09_intimacy" not in memory
        assert eval "ria_r09_date_close" in memory
        assert eval affinity["ria"] == 55
        assert eval chapter.startswith("리아 R10")
        click expression ("빵집 옆 골목을 기록집 첫 장소 후보로 고른다." if case & 8 else "작은 공원의 긴 의자를 기록집 첫 장소 후보로 고른다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        assert eval memory["ria_r10_place"] == ("bakery" if case & 8 else "park")
        assert eval "아직" in memory["ria_r10_booklet_state"]
        run FileSave("3", confirm=False)
        click expression ("서윤 한 명에게 교제 사실을 알리기로 함께 합의한다." if case & 4 else "당분간 둘만 알고 지내고 싶다고 말한다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        assert eval memory["ria_publicity"] == ("agreed_seoyun" if case & 4 else "private")
        assert eval "ria_disclosure_done" not in memory
        assert eval "ria_known_colleagues" not in memory
        if eval case % 3 != 0:
            click "잠깐 만나기 — 지도에 없는 산책 (선택 일상)" until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            click expression ("가로등 아래 서서 ‘불 켜지는 모퉁이’라고 부른다." if case & 4 else "발견한 계단을 따라 ‘한 칸 더’라고 부른다.") until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            assert eval memory["ria_o02_status"] == "completed"
            assert eval memory["ria_o02_name"] == ("불 켜지는 모퉁이" if case & 4 else "한 칸 더")
        else:
            click "본편 계속 — 일요일 저녁으로" until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            assert eval memory["ria_o02_status"] == "skipped"
            assert eval "ria_o02_name" not in memory
            assert eval "ria_o02_visited" not in memory
        assert eval chapter.startswith("리아 R11")
        assert eval memory["ria_publicity"] == ("told_seoyun" if case & 4 else "private")
        assert eval memory.get("ria_known_colleagues", []) == (["seoyun"] if case & 4 else [])
        assert eval any("축하해~ 두 사람" in h.what for h in _history_list) == bool(case & 4)
        assert eval any("어제 한 칸 더" in h.what or "어제 불 켜지는 모퉁이" in h.what for h in _history_list) == (case % 3 != 0)
        if eval case == 0:
            run FileLoad("3", confirm=False)
            assert screen "choice" timeout 10.0
            assert eval "ria_known_colleagues" not in memory
            assert eval "ria_o02_status" not in memory
            assert eval "ria_R10" not in completed
            click "서윤 한 명에게 교제 사실을 알리기로 함께 합의한다." until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            click "본편 계속 — 일요일 저녁으로" until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            assert eval memory["ria_known_colleagues"] == ["seoyun"]
            run FileLoad("3", confirm=False)
            assert screen "choice" timeout 10.0
            assert eval "ria_known_colleagues" not in memory
            assert eval "ria_disclosure_done" not in memory
            click "당분간 둘만 알고 지내고 싶다고 말한다." until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            click "본편 계속 — 일요일 저녁으로" until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            assert eval memory["ria_publicity"] == "private"
        click expression ("도현이 제안한 덮밥을 함께 만들고 재료를 나눈다." if ((case >> 1) ^ (case >> 3)) & 1 else "리아 추천 파스타를 함께 만들고 소스 간을 맞춘다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        assert eval memory["ria_r11_menu"] == ("rice" if ((case >> 1) ^ (case >> 3)) & 1 else "pasta")
        assert eval "미정" in memory["ria_r11_contact_plan"]
        assert eval chapter.startswith("리아 R12")
        assert eval "ria_r11_intimacy" not in memory
        assert eval memory["ria_outfit_idea_discussed"] is True
        assert eval memory["ria_r12_gap_messages_received"] is True
        assert eval "일곱 시" in memory["ria_r12_appointment"]
        assert eval any("지난번 파스타" in h.what for h in _history_list) == (memory["ria_r11_menu"] == "pasta")
        assert eval any("지난번 덮밥" in h.what for h in _history_list) == (memory["ria_r11_menu"] == "rice")
        run FileSave("4", confirm=False)
        click expression ("나도 같은 마음이라고 답한다 — 친밀한 장면으로 이어짐." if case & 16 else "오늘은 돌아가고 내일 다시 만나고 싶다고 말한다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        assert eval memory["ria_r12_intimacy"] == ("shared" if case & 16 else "deferred")
        assert eval any("함께 아침을 먹고" in h.what for h in _history_list) == bool(case & 16)
        if eval case == 0:
            run FileLoad("4", confirm=False)
            assert screen "choice" timeout 10.0
            assert eval "ria_r12_intimacy" not in memory
            click "나도 같은 마음이라고 답한다 — 친밀한 장면으로 이어짐." until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            assert eval memory["ria_r12_intimacy"] == "shared"
            run FileLoad("4", confirm=False)
            assert screen "choice" timeout 10.0
            assert eval "ria_r12_intimacy" not in memory
            assert eval "ria_r12_next_appointment" not in memory
            click "오늘은 돌아가고 내일 다시 만나고 싶다고 말한다." until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
        click expression ("일찍 연락이 오면 좋겠다고 말하되 확정 시간은 네 시로 둔다." if case & 16 else "네 시 약속을 기준으로 내 일정을 잡겠다고 말한다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        assert eval affinity["ria"] == 63 + (2 if case % 3 != 0 else 0)
        assert eval trust_ria == 3
        assert eval dating is True
        assert eval speech_informal == bool(case & 1)
        assert eval memory["ria_r12_next_appointment_status"] == "scheduled"
        assert eval memory["ria_r12_next_appointment"] == "일요일 오후 네 시, 변경은 서로 다시 확인"
        assert eval memory["ria_r12_expectation"] == ("hope_early" if case & 16 else "fixed")
        assert eval set(completed) == ({"ria_R08", "ria_R09", "ria_R10", "ria_R11", "ria_R12", "ria_O02"} if case % 3 != 0 else {"ria_R08", "ria_R09", "ria_R10", "ria_R11", "ria_R12"})
        assert eval not any("[ri(" in h.what for h in _history_list)
        if eval case == 31:
            click "기록" until screen "history"
            pause 0.2
            screenshot "ria12-history.png"
            click "돌아가기" until not screen "history"
        $ award_once("ria_R12", "ria", 4)
        assert eval affinity["ria"] == 63 + (2 if case % 3 != 0 else 0)

    testcase guard:
        parameter case = [0, 1]
        $ ria12_fixture["case"] = case
        run Start("test_ria12_guard")
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        assert eval memory == {}
        assert eval completed == []
        assert eval sum(affinity.values()) == 0

    teardown:
        exit

# Complete start-to-ending coverage now lives in ria16_flow.
