# Internal native checks. The compiled file is excluded from distributions.
testsuite windows_smoke:
    testcase startup_and_save_restore:
        assert screen "main_menu" timeout 15.0
        assert eval not renpy.emscripten
        screenshot "windows-main-menu.png"
        click id "start_button" until not screen "main_menu"
        advance until screen "choice"
        screenshot "windows-c01-choice.png"
        click "표지를 조금 옮기고, 사람들이 어떻게 움직이는지 볼까요?" until not screen "choice"
        advance until screen "choice"
        click "조금 익숙해지면 놓을게요." until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith("C02")
        assert eval speech_informal is False
        assert eval affinity["ria"] == 10
        assert eval memory["c01_approach"] == "observe"
        assert eval "jihyun_intro" not in memory
        click "저장" until screen "save"
        run FileSave("4", confirm=False)
        screenshot "windows-save.png"
        click "돌아가기" until not screen "save"
        click "현장에서 본 근거부터 말한다." until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith("C03")
        assert eval memory["jihyun_intro"] == "evidence"
        run FileLoad("4", confirm=False)
        assert screen "choice" timeout 10.0
        assert eval chapter.startswith("C02")
        assert eval affinity["ria"] == 10
        assert eval "jihyun_intro" not in memory
        assert eval "C02" not in completed
        assert eval dating is False
        screenshot "windows-restored.png"
        $ import json
        $ native_result = {"suite": "windows_smoke", "passed": True, "native": not renpy.emscripten, "chapter": chapter, "speech_informal": speech_informal, "ria_affinity": affinity["ria"], "memory": dict(memory), "completed": list(completed), "dating": dating}
        $ open(config.basedir + "/native-smoke-success.json", "w", encoding="utf-8").write(json.dumps(native_result, ensure_ascii=False, indent=2))

    teardown:
        exit

# Focused fixture: no intro dialogue is claimed as covered by these matrix cases.
init python:
    romance_fixture_config = {}

label test_common_pair_entry:
    scene bg plain
    $ speech_informal = romance_fixture_config.get("informal", False)
    $ memory = {"booklet_known_ria": True, "booklet_known_jihyun": True, "booklet_known_yujin": True, "booklet_known_seoyun": True}
    $ affinity = {"ria": 0, "jihyun": 0, "yujin": 0, "seoyun": 0}
    $ completed = []
    $ dating = False
    $ active_route = None
    $ c06_person = None
    $ c06_topic = None
    $ _history_list = []
    call c06
    call c07
    call c08
    menu:
        "검증 구간 종료":
            pass
    return

label test_common_legacy_entry:
    scene bg plain
    $ c06_person = romance_fixture_config["person"]
    $ speech_informal = False
    $ memory = {"booklet_known_ria": True, "booklet_known_jihyun": True, "booklet_known_yujin": True, "booklet_known_seoyun": True}
    $ memory["c06_" + c06_person + "_weekend"] = True
    $ c06_topic = "weekend"
    $ affinity = {"ria": 0, "jihyun": 0, "yujin": 0, "seoyun": 0}
    $ completed = []
    $ dating = False
    $ active_route = None
    $ _history_list = []
    call c07
    call c08
    menu:
        "검증 구간 종료":
            pass
    return

testsuite common_romance:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase pair_memory:
        parameter (person, topic, second, method, informal) = [("ria", "today", "ria", "verify", True), ("ria", "weekend", "ria", "coordinate", False), ("ria", "place", "ria", "try", True), ("jihyun", "today", "jihyun", "verify", False), ("jihyun", "weekend", "jihyun", "coordinate", False), ("jihyun", "place", "jihyun", "try", False), ("yujin", "today", "yujin", "verify", False), ("yujin", "weekend", "yujin", "coordinate", False), ("yujin", "place", "yujin", "try", False), ("seoyun", "today", "seoyun", "verify", False), ("seoyun", "weekend", "seoyun", "coordinate", False), ("seoyun", "place", "seoyun", "try", False), ("ria", "today", "jihyun", "try", False), ("jihyun", "weekend", "yujin", "verify", False), ("yujin", "place", "seoyun", "coordinate", False), ("seoyun", "today", "ria", "try", True)]
        $ romance_fixture_config["informal"] = informal
        run Start("test_common_pair_entry")
        advance until screen "choice"
        click expression {"ria": "리아에게 말을 건다.", "jihyun": "지현에게 말을 건다.", "yujin": "유진에게 말을 건다.", "seoyun": "서윤에게 말을 건다."}[person] until not screen "choice"
        advance until screen "choice"
        click expression {"today": "오늘 있었던 일을 묻는다.", "weekend": "쉬는 날의 취향을 묻는다.", "place": "퇴근 후 들르는 장소를 묻는다."}[topic] until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith("C07")
        assert eval speech_informal == informal
        assert eval memory.get("c06_" + person + "_" + topic + "_personal_moment") is True
        assert eval len([k for k in memory if k.endswith("_personal_moment")]) == 1
        assert eval affinity[person] == 2
        assert eval sum(affinity.values()) == 2
        click expression {"ria": "리아와 확인한다.", "jihyun": "지현과 확인한다.", "yujin": "유진과 확인한다.", "seoyun": "서윤과 확인한다."}[second] until not screen "choice"
        advance until screen "choice"
        click expression {"verify": "직접 떨어져서 읽고 확인한다.", "coordinate": "각자 볼 부분을 나누고 결과를 맞춘다.", "try": "작게 바꾼 시안 하나를 만들어 비교한다."}[method] until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith("C08")
        assert eval memory.get("c07_" + second + "_method") == method
        assert eval memory.get("c07_" + second + "_afterwork_moment") is True
        assert eval len([k for k in memory if k.endswith("_afterwork_moment")]) == 1
        assert eval sum(affinity.values()) == 4
        assert eval affinity[second] == (4 if person == second else 2)
        assert eval dating is False
        assert eval set(completed) == {"C06", "C07"}
        click "강리아와 다음 약속 잡기 — 친구 같은 동갑, 장난 속에서 특별해지는 연애." until not screen "choice"
        advance until screen "choice"
        assert eval active_route == "ria"
        assert eval memory["c08_route"] == "ria"
        assert eval dating is False

    testcase legacy_does_not_invent_personal_memory:
        parameter person = ["ria", "jihyun", "yujin", "seoyun"]
        $ romance_fixture_config["person"] = person
        run Start("test_common_legacy_entry")
        advance until screen "choice"
        click expression {"ria": "리아와 확인한다.", "jihyun": "지현과 확인한다.", "yujin": "유진과 확인한다.", "seoyun": "서윤과 확인한다."}[person] until not screen "choice"
        advance until screen "choice"
        click "직접 떨어져서 읽고 확인한다." until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith("C08")
        assert eval not any(k.endswith("_personal_moment") for k in memory)
        assert eval len(_history_list) > 10
        assert eval not any(any(marker in h.what for marker in ("일정 안 생각하는 연습", "설명서 똑바로", "다른 제목 골랐", "그 책갈피")) for h in _history_list)
        assert eval memory.get("c07_" + person + "_afterwork_moment") is True
        assert eval dating is False

    testcase complete_common_and_save_restore:
        assert screen "main_menu" timeout 10.0
        click id "start_button" until not screen "main_menu"
        advance until screen "choice"
        click "표지를 조금 옮기고, 사람들이 어떻게 움직이는지 볼까요?" until not screen "choice"
        advance until screen "choice"
        click "조금 익숙해지면 놓을게요." until not screen "choice"
        advance until screen "choice"
        click "더 확인할 시간을 요청한다." until not screen "choice"
        advance until screen "choice"
        click "사람들이 움직이는 방향을 묻는다." until not screen "choice"
        advance until screen "choice"
        click "농담을 받아친 뒤 요청을 확인한다." until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith("C05")
        assert eval memory.get("jihyun_followup_delivered") is True
        click "오늘은 쉬는 쪽이 좋아요." until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith("C06")
        assert eval memory.get("c05_shared_table") is True
        assert eval all(memory.get("booklet_known_" + k) for k in ("ria", "jihyun", "yujin", "seoyun"))
        click "리아에게 말을 건다." until not screen "choice"
        advance until screen "choice"
        click "퇴근 후 들르는 장소를 묻는다." until not screen "choice"
        advance until screen "choice"
        click "리아와 확인한다." until not screen "choice"
        advance until screen "choice"
        click "각자 볼 부분을 나누고 결과를 맞춘다." until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith("C08")
        assert eval affinity["ria"] == 14
        assert eval dating is False
        assert eval any("창밖 볼 시간 남겨" in h.what for h in _history_list)
        screenshot "romance-c08-choice.png"
        click "기록" until screen "history"
        assert eval len(_history_list) > 10
        pause 0.2
        $ history_vp = renpy.get_displayable("history", "history_viewport")
        assert eval history_vp.xadjustment.page > 1000
        screenshot "romance-c07-history.png"
        click "돌아가기" until not screen "history"
        run FileSave("3", confirm=False)
        click "강리아와 다음 약속 잡기 — 친구 같은 동갑, 장난 속에서 특별해지는 연애." until not screen "choice"
        advance until screen "choice"
        assert eval chapter.startswith("W_COORD01")
        assert eval work_style == "coordinate"
        click "각자 처음 보는 사람이 무엇을 알아야 하는지 묻는다." until not screen "choice"
        advance until screen "choice"
        assert eval memory.get("work_stage_1") == "W_COORD01"
        assert eval chapter.startswith("리아 R01")
        assert eval active_route == "ria"
        assert eval dating is False
        run FileLoad("3", confirm=False)
        assert screen "choice" timeout 10.0
        assert eval chapter.startswith("C08")
        assert eval active_route is None
        assert eval "work_stage_1" not in memory
        assert eval work_style == "coordinate"
        assert eval memory.get("c06_ria_place_personal_moment") is True
        assert eval memory.get("c07_ria_afterwork_moment") is True
        assert eval affinity["ria"] == 14
        assert eval dating is False
        $ import json
        $ open(config.basedir + "/common-romance-success.json", "w", encoding="utf-8").write(json.dumps({"chapter": chapter, "dating": dating, "memory": dict(memory), "affinity": dict(affinity)}, ensure_ascii=False, indent=2))

    teardown:
        exit
