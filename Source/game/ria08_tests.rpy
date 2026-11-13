# Internal tests only; excluded from local delivery builds.
init python:
    ria08_fixture = {}

    def ria08_test_caption(route):
        items = renpy.get_screen("choice").scope["items"]
        if chapter.startswith("C08") and route == "colleague" and len(items) == 5:
            return renpy.substitute(items[-1].caption)
        if chapter.startswith("리아 R04") and route == "decline" and len(items) == 3:
            return renpy.substitute(items[-1].caption)
        return renpy.substitute(items[0].caption)

label test_ria08_entry:
    scene bg plain
    $ speech_informal = ria08_fixture["informal"]
    $ active_route = "ria"
    $ dating = True
    $ memory = {"ria_core_understanding": True, "ria_confession_accepted": True}
    $ first_kiss = ria08_fixture["prior_kiss"]
    if first_kiss:
        $ remember("ria_first_kiss", "R04")
    $ affinity = {"ria": 35, "jihyun": 0, "yujin": 0, "seoyun": 0}
    $ trust_ria = 2
    $ completed = ["ria_R04"]
    call ria_r05
    call ria_o01_offer
    call ria_r06
    call ria_r07
    call ria_r08
    menu:
        "검사 종료":
            pass
    return

label test_ria08_guard:
    $ active_route = "ria"
    $ dating = False
    call ria_r05
    call ria_o01_offer
    call ria_r06
    call ria_r07
    call ria_r08
    menu:
        "교제 전 검사 종료":
            pass
    return

testsuite ria08:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase branch_and_restore:
        parameter case = list(range(16))
        $ ria08_fixture["informal"] = bool(case & 1)
        $ ria08_fixture["prior_kiss"] = bool(case & 2)
        run Start("test_ria08_entry")
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        click expression ("사진 찍는 동안 메뉴를 맡긴다." if case & 1 else "골목을 걸으며 하나씩 고른다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        assert eval memory.get("ria_r05_record_time_kept") is True
        assert eval affinity["ria"] == 39
        assert eval "시각 미정" in memory["ria_r05_next_walk"]
        if eval case & 4:
            click "잠깐 만나기 — 점심 메뉴의 작은 내기 (선택 일상)" until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            click expression ("시원한 국수를 가리킨다." if case & 2 else "매콤한 덮밥을 가리킨다.") until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            assert eval memory["ria_o01_status"] == "completed"
        else:
            click "본편 계속 — 다음 만남으로" until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            assert eval memory["ria_o01_status"] == "skipped"
            assert eval "ria_o01_meal" not in memory
        assert eval chapter.startswith("리아 R06")
        click expression ("나도 같이 쉬고 싶다고 한다." if case & 2 else "어떨 때 그런지 더 묻는다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        click expression ("인사하기 전에 하나만 더 조른다." if case & 4 else "나란히 조금 더 걷는다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        assert eval chapter.startswith("리아 R07")
        assert eval first_kiss == bool(case & 6)
        assert eval memory.get("ria_first_kiss") == ("R04" if case & 2 else ("R06" if case & 4 else None))
        assert eval memory["ria_publicity"] == "private"
        assert eval memory["ria_r07_appointment"] == "토요일 오후 네 시"
        assert eval affinity["ria"] == 45 + (2 if case & 4 else 0)
        assert eval trust_ria == 3
        run FileSave("2", confirm=False)
        click expression ("같은 마음이라고 답한다 — 친밀한 장면으로 이어짐." if case & 8 else "차만 마시고 돌아간다.") until not screen "choice"
        advance until eval renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "office_phone"
        click id "phone_next" until eval phone_context == "r08_reply"
        assert eval chapter.startswith("리아 R08")
        assert eval memory["ria_r07_intimacy"] == ("shared" if case & 8 else "deferred")
        assert eval memory.get("ria_r08_breakfast_shared", False) == bool(case & 8)
        assert eval affinity["ria"] == 45 + (2 if case & 4 else 0)
        if eval case == 0:
            run FileLoad("2", confirm=False)
            assert screen "choice" timeout 10.0
            assert eval chapter.startswith("리아 R07")
            assert eval "ria_r07_intimacy" not in memory
            assert eval "ria_r08_breakfast_shared" not in memory
            assert eval "ria_R07" not in completed
            click "같은 마음이라고 답한다 — 친밀한 장면으로 이어짐." until not screen "choice"
            advance until eval renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "office_phone"
            assert eval memory["ria_r07_intimacy"] == "shared"
            run FileLoad("2", confirm=False)
            assert screen "choice" timeout 10.0
            assert eval "ria_r07_stayed" not in memory
            click "차만 마시고 돌아간다." until not screen "choice"
            advance until eval renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "office_phone"
        if not eval phone_context == "r08_reply":
            click id "phone_next" until eval phone_context == "r08_reply"
        click id ("phone_reply_evening" if case & 1 else "phone_reply_miss")
        click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        assert eval set(completed) == ({"ria_R04", "ria_R05", "ria_R06", "ria_R07", "ria_R08", "ria_O01"} if case & 4 else {"ria_R04", "ria_R05", "ria_R06", "ria_R07", "ria_R08"})
        assert eval affinity["ria"] == 49 + (2 if case & 4 else 0)
        assert eval dating is True
        assert eval speech_informal == bool(case & 1)
        assert eval memory.get("ria_r08_messages_received") is True
        assert eval any("지난번" in row["text"] and "국수" in row["text"] for row in phone_threads["ria"]) == bool(case & 4)
        assert eval not any("{ri" in h.what or "[ri(" in h.what for h in _history_list)
        if eval case == 15:
            click "기록" until screen "history"
            pause 0.2
            screenshot "ria08-history.png"
            click "돌아가기" until not screen "history"
        $ award_once("ria_R08", "ria", 4)
        assert eval affinity["ria"] == 49 + (2 if case & 4 else 0)

    testcase not_dating_guard:
        run Start("test_ria08_guard")
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until screen "choice"
        assert eval memory == {}
        assert eval completed == []
        assert eval sum(affinity.values()) == 0
        assert eval dating is False

    teardown:
        exit

# Complete start-to-ending coverage now lives in ria16_flow.
