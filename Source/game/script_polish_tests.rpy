# Regression fixtures for the full script edit. Excluded from playable builds.
init python:
    polish_fixture = {}
    def polish_history():
        return "\n".join(renpy.substitute(h.what) for h in _history_list)

label test_polish_jihyun_game:
    scene bg plain
    $ active_route = "jihyun"
    $ dating = True
    $ memory = {"jihyun_publicity": "private"}
    $ completed = []
    $ affinity = {"ria": 17, "jihyun": 17, "yujin": 17, "seoyun": 17}
    $ _history_list = []
    call jihyun_r11
    menu:
        "후일담까지 확인":
            pass
    $ remember("jihyun_route_completed")
    $ remember("jihyun_booklet_subject", "계단 사진")
    $ _history_list = []
    call jihyun_e01
    menu:
        "퇴고 검사 종료":
            pass
    return

label test_polish_private:
    scene bg plain
    $ active_route = polish_fixture["route"]
    $ dating = True
    $ memory = {"jihyun_private_name": "지현 누나", "seoyun_marriage_state": "married_cohabiting"}
    $ completed = ["polish_prior"]
    $ affinity = {"ria": 17, "jihyun": 17, "yujin": 17, "seoyun": 17}
    $ polish_slot = polish_fixture["slot"]
    $ polish_outfit = {"r07": "casual", "r12": "special", "r15": "home"}[polish_slot]
    $ _history_list = []
    if active_route == "jihyun":
        call jihyun_private_evening(polish_slot, polish_outfit)
    else:
        call seoyun_private_evening(polish_slot, polish_outfit)
    menu:
        "퇴고 검사 종료":
            pass
    return

label test_polish_yujin_reconsider:
    scene bg plain
    $ active_route = "yujin"
    $ dating = True
    $ memory = {"yujin_r13_agreed_scope": True, "yujin_r13_support_plan": "slides", "yujin_support_action": "materials", "yujin_support_overstep": False}
    $ completed = []
    $ affinity = {"ria": 17, "jihyun": 17, "yujin": 17, "seoyun": 17}
    $ _history_list = []
    call yujin_r14
    menu:
        "다음 날의 만남까지":
            pass
    $ _history_list = []
    call yujin_r15
    menu:
        "퇴고 검사 종료":
            pass
    return

label test_polish_event_address:
    $ active_route = "jihyun"
    $ dating = True
    $ memory = {"jihyun_private_name": polish_fixture["name"]}
    call event_sequence("jihyun_r15", "home")
    menu:
        "퇴고 검사 종료":
            pass
    return

label test_polish_seoyun_thought:
    scene bg plain
    sn "말을 고르다 놓친 마음도 이번에는 적어 두기로 했다."
    menu:
        "퇴고 검사 종료":
            pass
    return

testsuite script_polish_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase game_mode_survives_main_and_epilogue:
        parameter mode = list(range(3))
        run Start("test_polish_jihyun_game")
        advance until screen "choice"
        click expression yujin_test_choice(mode)
        advance until screen "choice"
        assert eval memory["jihyun_game_mode"] == ["competitive", "cooperative", "picture_talk"][mode]
        assert eval ("공부까지 해 오려고" in polish_history()) == (mode == 0)
        assert eval ("다음엔 내가 빵 고를게" in polish_history()) == (mode == 1)
        assert eval ("카드에서만 찾으면 아침 굶겠네" in polish_history()) == (mode == 2)
        assert eval "jihyun_R11" in completed and affinity["jihyun"] == 17
        click "후일담까지 확인" until not screen "choice"
        advance until screen "choice"
        click expression yujin_test_choice(0)
        advance until screen "choice"
        assert eval memory.get("jihyun_epilogue_completed")
        assert eval ("제가 이길 때까지" in polish_history()) == (mode == 0)
        assert eval ("이번엔 제가 차 맞출게요" in polish_history()) == (mode == 1)
        assert eval ("이번엔 제 잼도 제가 고를래요" in polish_history()) == (mode == 2)
        assert eval len(completed) == len(set(completed))

    testcase loading_before_game_removes_the_old_callback:
        run Start("test_polish_jihyun_game")
        advance until screen "choice"
        run FileSave("polish-before-game", confirm=False)
        click expression yujin_test_choice(0)
        advance until screen "choice"
        assert eval "공부까지 해 오려고" in polish_history()
        run FileLoad("polish-before-game", confirm=False)
        assert screen "choice" timeout 10.0
        assert eval "jihyun_game_mode" not in memory
        click expression yujin_test_choice(1)
        advance until screen "choice"
        assert eval memory["jihyun_game_mode"] == "cooperative"
        assert eval "공부까지 해 오려고" not in polish_history()
        assert eval "다음엔 내가 빵 고를게" in polish_history()
        assert eval completed.count("jihyun_R11") == 1
        assert eval affinity["jihyun"] == 17

    testcase bookends_follow_slot_and_keep_relationship_state:
        parameter case = list(range(12))
        $ polish_fixture.update(route="jihyun" if case < 6 else "seoyun", slot=["r07", "r12", "r15"][(case % 6) // 2])
        run Start("test_polish_private")
        advance until screen "choice"
        click expression yujin_test_choice(0 if case % 2 == 0 else 2)
        if eval case % 2 == 0:
            advance until screen "event_cut"
            assert eval renpy.get_screen("event_cut").scope["event_id"] == active_route + "_" + polish_fixture["slot"]
            click id "cut_skip" until not screen "event_cut"
        advance until screen "choice"
        assert eval memory[active_route + "_" + polish_fixture["slot"] + "_pace"] == ("shared" if case % 2 == 0 else "talk")
        assert eval dating is True and completed == ["polish_prior"]
        assert eval all(n == 17 for n in affinity.values())
        assert eval memory["seoyun_marriage_state"] == "married_cohabiting"
        assert eval memory["jihyun_private_name"] == "지현 누나"
        if eval active_route == "jihyun" and case % 2 == 0:
            assert eval ("핑계 안 찾아도 되네" in polish_history()) == (polish_fixture["slot"] == "r07")
            assert eval ("칭찬 기다리셨다는 것도" in polish_history()) == (polish_fixture["slot"] == "r12")
            assert eval ("말로는 조금 늦게 했네요" in polish_history()) == (polish_fixture["slot"] == "r15")
        elif eval active_route == "jihyun":
            assert eval ("수요일에 물 따라 달라고" in polish_history()) == (polish_fixture["slot"] == "r07")
            assert eval ("옷 고르면서는 칭찬" in polish_history()) == (polish_fixture["slot"] == "r12")
            assert eval ("산책길 후보는 두 군데" in polish_history()) == (polish_fixture["slot"] == "r15")
        elif eval case % 2 == 0:
            assert eval ("후식 메뉴 그렇게 볼 때" in polish_history()) == (polish_fixture["slot"] == "r07")
            assert eval ("말 잘하려는 것보다" in polish_history()) == (polish_fixture["slot"] == "r12")
            assert eval ("앞으로도 기다려야 하는 건 아니고" in polish_history()) == (polish_fixture["slot"] == "r15")
        else:
            assert eval ("후식 메뉴 또 펼쳤을 때" in polish_history()) == (polish_fixture["slot"] == "r07")
            assert eval ("오늘 대답을 재촉하지는 않고요" in polish_history()) == (polish_fixture["slot"] == "r12")
            assert eval ("아직 어려운 마음도" in polish_history()) == (polish_fixture["slot"] == "r15")

    testcase reconsidered_relationship_has_its_own_recovery:
        parameter decision = list(range(3))
        run Start("test_polish_yujin_reconsider")
        advance until screen "choice"
        if eval decision == 0:
            click expression yujin_test_choice(0)
        else:
            click expression yujin_test_choice(2)
            advance until screen "choice"
            click expression yujin_test_choice(decision)
        advance until screen "choice"
        assert eval dating and memory.get("yujin_support_alignment_verified")
        assert eval memory["yujin_r14_readiness"] == ["ready", "reconsidered", "talk_after"][decision]
        assert eval ("아직 웃으면서 넘기기는 어려워요" in polish_history()) == (decision != 0)
        assert eval ("그럼 다시 기다릴까요" in polish_history()) == (decision == 0)
        click "다음 날의 만남까지" until not screen "choice"
        advance until screen "choice"
        assert eval ("어제 얘기가 다 끝났다고 생각하진 않아요" in polish_history()) == (decision != 0)
        click expression yujin_test_choice(0)
        advance until screen "choice"
        click expression yujin_test_choice(1)
        advance until screen "choice"
        assert eval memory.get("yujin_r15_complete") and dating
        assert eval "yujin_relationship_closed" not in memory
        assert eval all(affinity[n] == 17 for n in ("ria", "jihyun", "seoyun"))

    testcase event_text_respects_each_selected_private_address:
        parameter name = ["지현 씨", "지현 누나", "팀장님"]
        $ polish_fixture["name"] = name
        run Start("test_polish_event_address")
        advance until screen "event_cut"
        click id "cut_next"
        pause 0.1
        assert eval renpy.get_screen("event_cut").scope["cursor"] == 1
        $ spoken = renpy.get_screen("event_cut").scope["beat"]["dohyun"][0]
        assert eval all(form not in spoken or form == name for form in ("지현 씨", "지현 누나", "팀장님"))
        assert eval "[memory" not in spoken
        assert eval memory["jihyun_private_name"] == name
        if eval name == "지현 누나":
            screenshot "polish-jihyun-event-address.png"
        click id "cut_skip" until not screen "event_cut"
        advance until screen "choice"

    testcase seoyun_thought_uses_the_shared_display_rule:
        run Start("test_polish_seoyun_thought")
        assert eval sn.name == s.name
        assert eval sn.what_prefix == dn.what_prefix and sn.what_suffix == dn.what_suffix
        assert eval cream_focus == "seoyun"
        screenshot "polish-seoyun-thought.png"
        advance until screen "choice"

    teardown:
        exit
