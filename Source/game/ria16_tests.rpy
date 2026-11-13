# Internal authored tests. Excluded from Windows delivery.
init python:
    ria16_fixture = {}

    def route_phone_test_reply():
        replies = renpy.get_screen("office_phone").scope["replies"]
        value = replies[-1][0] if phone_fixture.get("preferred_reply") == "small_memory" else replies[0][0]
        return "phone_reply_" + value


    def ria16_final_menu():
        screen = renpy.get_screen("choice")
        return bool(screen and any("수록 구간을 마쳤습니다" in i.caption for i in screen.scope["items"]))

    def ria16_flow_caption(route):
        items = renpy.get_screen("choice").scope["items"]
        captions = [renpy.substitute(i.caption) for i in items]
        if chapter.startswith("C08") and route == "colleague" and len(items) == 5:
            return captions[-1]
        if chapter.startswith("리아 R04") and route == "decline" and len(items) == 3:
            return captions[-1]
        if route == "close" and chapter.startswith("리아 R14") and any("연애를 마치자고 한다 — 관계 종료 대화로 이어짐." in c for c in captions):
            return next(c for c in captions if "연애를 마치자고 한다 — 관계 종료 대화로 이어짐." in c)
        if route == "no_epilogue" and any("후일담 읽기" in c for c in captions):
            return captions[-1]
        if route == "cosplay" and any("코스프레 의상을" in c for c in captions):
            return next(c for c in captions if "코스프레 의상을" in c)
        if route == "third":
            new_options = {c["new_option"][1:-2] for c in choice_cases}
            for caption in captions:
                if caption in new_options:
                    return caption
        if route == "deferred":
            if chapter.startswith("C01") and "조금 익숙해지면 놓을게요." in captions:
                return "조금 익숙해지면 놓을게요."
            if chapter.startswith("C08"):
                return captions[0]
            if any("친밀한 장면" in c or "입맞춤" in c for c in captions):
                return captions[-1]
            if any("본편 계속" in c for c in captions):
                return next(c for c in captions if "본편 계속" in c)
            if any("당분간 둘만" in c for c in captions):
                return next(c for c in captions if "당분간 둘만" in c)
            if chapter.startswith("리아 R13"):
                return captions[-1]
        return captions[0]

label test_ria16_entry:
    scene bg plain
    $ speech_informal = bool(ria16_fixture["variant"] & 1)
    $ active_route = "ria"
    $ dating = True
    $ memory = {"ria_confession_accepted": True, "ria_core_understanding": True, "ria_r12_next_appointment_status": "scheduled", "ria_r12_expectation": "hope_early" if ria16_fixture["variant"] & 2 else "fixed"}
    if ria16_fixture["variant"] % 4 != 3:
        $ remember("ria_r10_place", "park" if ria16_fixture["variant"] & 1 else "bakery")
        $ remember("ria_r09_support", "organize" if ria16_fixture["variant"] & 1 else "explain")
    if ria16_fixture["variant"] & 8:
        $ remember("ria_r07_intimacy", "shared")
    if ria16_fixture["variant"] % 4 == 1:
        $ remember("ria_o02_status", "completed")
        $ remember("ria_o02_name", "한 칸 더")
    if ria16_fixture["variant"] % 4 == 2:
        $ remember("ria_private_teasing_mode", "stop")
    $ affinity = {"ria": 63, "jihyun": 0, "yujin": 0, "seoyun": 0}
    $ trust_ria = 3
    $ completed = ["ria_R12"]
    call ria_r13
    call ria_r14
    if dating:
        call ria_r15
        call ria_o03_offer
        call ria_r16
        call ria_e01
    menu:
        "검사 종료":
            pass
    return

label test_ria16_guard:
    $ active_route = "ria" if ria16_fixture["guard"] != 1 else "jihyun"
    $ dating = ria16_fixture["guard"] != 0
    call ria_r13
    call ria_r14
    call ria_r15
    call ria_o03_offer
    call ria_o03
    call ria_r16
    call ria_e01
    menu:
        "진입 조건 검사 종료":
            pass
    return

testsuite ria16:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase recovery_and_memories:
        parameter case = list(range(48))
        $ ria16_fixture["variant"] = case // 3
        $ ria16_fixture["reply"] = case % 3
        run Start("test_ria16_entry")
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
        if screen "office_phone":
            click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
            if screen "office_phone":
                click id route_phone_test_reply()
                click id "phone_next" until not screen "office_phone"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
        assert eval memory["ria_conflict"] == "open"
        if eval case == 0:
            screenshot "ria16-conflict-choice.png"
        click expression ["서운했다고 솔직히 말한다.", "두 시에 알았잖아, 하고 따진다.", "다음 데이트로 갚으라며 웃어넘긴다."][case % 3] until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
        if screen "office_phone":
            click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
            if screen "office_phone":
                click id route_phone_test_reply()
                click id "phone_next" until not screen "office_phone"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
        assert eval trust_ria == 2
        assert eval affinity["ria"] == 63
        assert eval memory["ria_r12_next_appointment_status"] == "changed_late_notice"
        assert eval memory["ria_conflict"] == "discussing"
        if eval case % 3 == 2:
            assert eval "ria_r14_understanding_confirmed" not in memory
            click expression ("보상 말고 연락이 필요하다고 고친다." if (case // 3) & 1 else "괜찮은 척했던 걸 털어놓는다.") until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            assert eval "ria_r14_clarification" in memory
        else:
            assert eval "ria_r14_clarification" not in memory
        assert eval memory["ria_r14_understanding_confirmed"] is True
        if eval case == 0:
            screenshot "ria16-repair-choice.png"
        run FileSave("5", confirm=False)
        click "같이 바꿔 보자고 한다 — 교제를 계속한다." until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
        if screen "office_phone":
            click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
            if screen "office_phone":
                click id route_phone_test_reply()
                click id "phone_next" until not screen "office_phone"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
        assert eval memory["ria_conflict"] == "discussing"
        click expression ("금요일에 시각부터 확정하자고 한다." if (case // 3) & 2 else "네 시부터 다섯 시 반까지만 보자고 한다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
        if screen "office_phone":
            click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
            if screen "office_phone":
                click id route_phone_test_reply()
                click id "phone_next" until not screen "office_phone"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
        assert eval chapter.startswith("리아 R15")
        assert eval memory["ria_conflict"] == "resolved"
        assert eval memory["ria_r14_delegation_done"] is True
        assert eval memory["ria_r14_appointment_kept"] is True
        assert eval trust_ria == 3
        assert eval affinity["ria"] == 71
        assert eval memory["ria_r15_booklet_photo_taken"] is True
        assert eval ("오늘 처음" in memory["ria_r15_booklet_photo"]) == ((case // 3) % 4 == 3)
        click expression ("다음 주 저녁, 날은 나중에 정하자고 한다." if (case // 3) & 4 else "다음 주에도 여기 오자고 한다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
        if screen "office_phone":
            click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
            if screen "office_phone":
                click id route_phone_test_reply()
                click id "phone_next" until not screen "office_phone"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
        assert eval memory["ria_r15_future_agreed"] is True
        assert eval memory["ria_r15_future_plan"] == ("plan_together" if (case // 3) & 4 else "weekly_evening")
        click expression ("나도 함께 있고 싶다고 답한다 — 친밀한 장면으로 이어짐." if (case // 3) & 4 else "오늘은 집에 가서 쉰다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
        if screen "office_phone":
            click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
            if screen "office_phone":
                click id route_phone_test_reply()
                click id "phone_next" until not screen "office_phone"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
        if eval (case // 3) & 4:
            click expression ("코스프레 의상을 같이 고르자고 한다." if (case // 3) & 1 else "지금의 편한 생활복이 좋다고 말한다.") until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            assert eval memory["ria_r15_outfit"] == ("cosplay" if (case // 3) & 1 else "home")
        else:
            assert eval "ria_r15_outfit" not in memory
        assert eval affinity["ria"] == 76
        assert eval memory["ria_r15_intimacy"] == ("shared" if (case // 3) & 4 else "deferred")
        if eval (case // 3) % 3 == 2:
            click "본편 계속 — 프로젝트 마무리로" until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            assert eval memory["ria_o03_status"] == "skipped"
            assert eval "ria_o03_rest" not in memory
        else:
            click "잠깐 만나기 — 쉬는 날의 준비물 (선택 일상)" until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            click expression ("노트 한 장에 감상을 한 줄씩 붙인다." if (case // 3) & 1 else "각자 할 일 하며 나란히 뒹군다.") until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if eval ((case // 3) & 12) and (case // 3) % 4 != 2:
                assert eval chapter.startswith("리아 O03")
                click expression ["노트보다 리아가 더 궁금하다고 받아친다.", "웃으며 다음 장을 넘긴다.", "그 장난은 아직 민망하다고 한다."][case % 3] until not screen "choice"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
                if screen "event_cut":
                    click id "cut_next" until not screen "event_cut"
                    advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                    if screen "office_phone":
                        click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                        if screen "office_phone":
                            click id route_phone_test_reply()
                            click id "phone_next" until not screen "office_phone"
                        advance until screen "choice"
                assert eval memory["ria_o03_teasing_seen"] is True
                assert eval memory["ria_private_teasing_mode"] == ["comfortable", "light", "stop"][case % 3]
            else:
                assert eval "ria_o03_teasing_seen" not in memory
            assert eval memory["ria_o03_status"] == "completed"
        assert eval chapter.startswith("리아 R16")
        assert eval "ria_route_completed" not in memory
        assert eval ending == ""
        assert eval affinity["ria"] == 76 + (0 if (case // 3) % 3 == 2 else 2)
        click expression ("각자 일을 지키며 오래 보자고 한다." if (case // 3) & 1 else "빈손인 날에도 보고 싶다고 한다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
        if screen "office_phone":
            click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
            if screen "office_phone":
                click id route_phone_test_reply()
                click id "phone_next" until not screen "office_phone"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
        assert eval chapter.startswith("리아 E01")
        assert eval memory["ria_route_completed"] is True
        assert eval persistent.local_ria_ending is True
        assert eval ending == "ria_good"
        assert eval memory["ria_booklet_state"] == "completed_two_copies"
        assert eval any("그때 각자 다른 거" in h.what or "그날 한 줄씩" in h.what for h in _history_list) == ((case // 3) % 3 != 2)
        run FileSave("6", confirm=False)
        click expression ("처음 가는 길을 하나 찾아보자고 한다." if (case // 3) & 8 else "익숙한 길을 다시 걷자고 한다.") until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
        if screen "office_phone":
            click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
            if screen "office_phone":
                click id route_phone_test_reply()
                click id "phone_next" until not screen "office_phone"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
        assert eval ("ria_e01_recalled_place" in memory) == ((case // 3) % 4 == 1 and not ((case // 3) & 8))
        assert eval "ria_e01_intimacy" not in memory
        assert eval memory["ria_epilogue_completed"] is True
        assert eval affinity["ria"] == 88 + (0 if (case // 3) % 3 == 2 else 2)
        assert eval speech_informal == bool((case // 3) & 1)
        assert eval all(k in completed for k in ("ria_R13", "ria_R14", "ria_R15", "ria_R16", "ria_E01"))
        assert eval "ria_relationship_closed" not in memory
        assert eval not any("[ri(" in h.what for h in _history_list)
        if eval case == 0:
            run FileLoad("6", confirm=False)
            assert screen "choice" timeout 10.0
            assert eval "ria_epilogue_completed" not in memory
            assert eval "ria_e01_intimacy" not in memory
            assert eval "ria_E01" not in completed
            click "익숙한 길을 다시 걷자고 한다." until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            assert eval "ria_e01_intimacy" not in memory
            assert eval affinity["ria"] == 90
            run FileLoad("5", confirm=False)
            assert screen "choice" timeout 10.0
            assert eval memory["ria_conflict"] == "discussing"
            assert eval "ria_route_completed" not in memory
            assert eval "ria_r14_action_confirmed" not in memory
            assert eval trust_ria == 2
            assert eval affinity["ria"] == 63
            click "연애를 마치자고 한다 — 관계 종료 대화로 이어짐."
            click "연애를 마치겠다는 뜻을 확인한다." until not screen "choice"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            assert eval ending == "ria_relationship_closed"
            assert eval dating is False
            assert eval "ria_R14" not in completed
            assert eval "ria_R15" not in completed
            assert eval "ria_E01" not in completed
            assert eval "ria_booklet_state" not in memory
        if eval case == 47:
            click "기록" until screen "history"
            pause 0.2
            screenshot "ria16-history.png"
            click "돌아가기" until not screen "history"

    testcase guards:
        parameter guard = [0, 1, 2]
        $ ria16_fixture["guard"] = guard
        run Start("test_ria16_guard")
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
        if screen "office_phone":
            click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
            if screen "office_phone":
                click id route_phone_test_reply()
                click id "phone_next" until not screen "office_phone"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        if screen "event_cut":
            click id "cut_next" until not screen "event_cut"
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until screen "choice"
        assert eval memory == {}
        assert eval completed == []
        assert eval ending == ""
        assert eval sum(affinity.values()) == 0

    teardown:
        exit

testsuite ria16_flow:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase full_route:
        parameter route = ["ria", "deferred", "close", "colleague", "decline", "no_epilogue", "cosplay", "third"]
        $ phone_fixture["preferred_reply"] = "small_memory" if route == "third" else "miss"
        click id "start_button" until not screen "main_menu"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id route_phone_test_reply()
                    click id "phone_next" until not screen "office_phone"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None or renpy.get_screen("office_phone") is not None
                if screen "office_phone":
                    click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                    if screen "office_phone":
                        click id route_phone_test_reply()
                        click id "phone_next" until not screen "office_phone"
                    advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
        assert eval ria16_final_menu()
        if eval route in ("ria", "deferred", "no_epilogue", "cosplay", "third"):
            assert eval ending == "ria_good"
            assert eval dating is True
            assert eval memory["ria_conflict"] == "resolved"
            assert eval memory["ria_route_completed"] is True
            assert eval persistent.local_ria_ending is True
            assert eval all(k in completed for k in ("ria_R04", "ria_R13", "ria_R14", "ria_R15", "ria_R16"))
            if eval route == "no_epilogue":
                assert eval memory["ria_epilogue_skipped"] is True
                assert eval "ria_E01" not in completed
                assert eval "ria_epilogue_completed" not in memory
                assert eval memory["ria_booklet_state"] == "rough_draft_shared"
            else:
                assert eval memory["ria_epilogue_completed"] is True
                assert eval memory["ria_booklet_state"] == "completed_two_copies"
            if eval route == "deferred":
                assert eval all(memory[k] == "deferred" for k in ("ria_r07_intimacy", "ria_r12_intimacy", "ria_r15_intimacy"))
                assert eval all(memory[k] == "skipped" for k in ("ria_o01_status", "ria_o02_status", "ria_o03_status"))
                assert eval memory["ria_publicity"] == "private"
                assert eval "ria_known_colleagues" not in memory
                assert eval memory["ria_r13_response"] == "cover"
                assert eval memory["ria_r14_understanding_confirmed"] is True
                assert eval first_kiss is False
                assert eval speech_informal is False
            assert eval not any(k in memory for k in ("ria_r09_intimacy", "ria_r11_intimacy", "ria_e01_intimacy"))
            if eval route == "deferred":
                assert eval event_presentations == {}
                assert eval "ria_r15_outfit" not in memory
            if eval route in ("ria", "cosplay", "no_epilogue"):
                assert eval len(event_presentations) == 3
                assert eval all(v["visited_slots"] == list(range(1, 8)) and v["loaded_images"] == [] and v["main_frames_seen"] == [1, 2, 3] and v["base_slots_seen"] == [1, 2, 3] and v["loaded_asset_ids"] == [] and v["status"] == "completed" for v in event_presentations.values())
                assert eval memory["ria_r15_outfit"] == ("cosplay" if route == "cosplay" else "home")
                assert eval "ria_r15:" + memory["ria_r15_outfit"] in event_presentations
            if eval route == "cosplay":
                assert eval any("문 앞에서 웃" in h.what for h in _history_list)
            if eval route == "ria":
                screenshot "ria16-full-route-end.png"
            if eval route == "no_epilogue":
                screenshot "ria16-base-ending.png"
        elif eval route == "close":
            assert eval ending == "ria_relationship_closed"
            assert eval dating is False
            assert eval memory["ria_conflict"] == "closed_without_repair"
            assert eval "ria_route_completed" not in memory
            assert eval not any(k in completed for k in ("ria_R14", "ria_R15", "ria_R16", "ria_E01"))
            screenshot "ria16-relationship-closed.png"
        else:
            assert eval ending == "colleague"
            assert eval dating is False
            assert eval "ria_route_completed" not in memory
            assert eval not any(k in completed for k in ("ria_R13", "ria_R14", "ria_R15", "ria_R16", "ria_E01"))

    teardown:
        exit
