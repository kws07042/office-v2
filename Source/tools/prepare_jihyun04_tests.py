from pathlib import Path
P=Path(__file__).resolve().parents[1]
s='''init python:
    jihyun_fixture = {"case":0}
    def jihyun_test_choice(index=0):
        return renpy.substitute(renpy.get_screen("choice").scope["items"][index].caption)
    def jihyun_test_common_caption():
        captions=[renpy.substitute(i.caption) for i in renpy.get_screen("choice").scope["items"]]
        if chapter.startswith("C08"):
            return next(c for c in captions if c.startswith("백지현과"))
        return captions[0]

label test_jihyun04_entry:
    $ active_route = "jihyun"
    $ affinity = {"ria":0,"jihyun":0,"yujin":0,"seoyun":0}
    $ memory = {}
    $ speech_informal = bool(jihyun_fixture["case"] % 2)
    if jihyun_fixture["case"] // 3 < 4:
        $ remember("jihyun_intro", ["evidence","check_later","check_later","compare"][jihyun_fixture["case"] // 3])
    if jihyun_fixture["case"] // 3 == 1:
        $ remember("jihyun_followup_delivered")
    if jihyun_fixture["case"] % 2 == 0:
        $ remember("c05_shared_table")
    if jihyun_fixture["case"] % 3 < 2:
        $ c06_person = "jihyun"
        $ c06_topic = ["weekend","place"][jihyun_fixture["case"] % 3]
    call jihyun_early_route
    $ remember("jihyun_test_done")
    menu:
        "검사 종료":
            pass
    return

testsuite jihyun04_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase early_choices_and_consent:
        parameter case = list(range(15))
        $ jihyun_fixture["case"] = case
        run SetField(persistent, "local_jihyun_ending", bool(case % 2))
        run Start("test_jihyun04_entry")
        advance until screen "office_phone"
        assert eval phone_active_contact == "jihyun"
        assert eval not cream_ria_visible() and not cream_yujin_visible()
        click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        assert eval memory["jihyun_r01_appointment"] == "목요일 저녁 일곱 시, 회사 앞 작은 식당"
        assert eval cream_relation_name("jihyun") == "알아가는 중"
        click expression jihyun_test_choice(case % 3)
        advance until screen "choice"
        assert eval memory["jihyun_r01_topic"] == ["decision","hobby","why_me"][case % 3]
        if eval case == 0:
            run FileSave("52", confirm=False)
            click expression jihyun_test_choice(2)
            advance until screen "choice"
            assert eval memory["jihyun_r02_plan"] == "choose_together"
            run FileLoad("52", confirm=False)
        click expression jihyun_test_choice((case // 3) % 3)
        advance until screen "choice"
        assert eval memory["jihyun_r02_plan"] == ["tea_first","walk_then_tea","choose_together"][(case // 3) % 3]
        assert eval memory["jihyun_r02_time_kept"]
        assert eval "네 시 귀가" in memory["jihyun_r02_delegated_scope"]
        if eval case // 3 == 2:
            assert eval any("확인 결과가 있는 걸로 넘기지는" in h.what for h in _history_list)
            assert eval not any("다음 날 가져온 확인 메모 봤어" in h.what for h in _history_list)
        if eval case // 3 == 4:
            assert eval not any("첫날에 점심 재방문 질문" in h.what for h in _history_list)
        click expression jihyun_test_choice((case+1) % 3)
        advance until screen "office_phone"
        assert eval memory["jihyun_core_understanding"] and not dating
        click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        assert eval bool(memory.get("jihyun_r01_reason_answered")) == (case % 3 == 2)
        assert eval memory["jihyun_r04_appointment"] == "금요일 저녁 일곱 시, 회사 앞 카페"
        assert eval affinity["jihyun"] == 19 and not dating
        if eval case == 0:
            screenshot "jihyun-confession-choice.png"
        if eval case % 5 == 1:
            click "마음은 있지만, 내 서툼과 회사에서의 경계를 조금 더 이야기한다."
            advance until screen "choice"
            assert eval jihyun_prepared and not dating
        if eval case % 5 in (2,3,4):
            click "이번 회차는 연애를 시작하지 않고 동료로 지낸다 — 동료 결말로 이어짐."
            advance until screen "choice"
            click expression jihyun_test_choice({2:0,3:1,4:2}[case % 5])
            if eval case % 5 != 2:
                advance until screen "choice"
        if eval case % 5 != 2:
            click "지현과 연인으로 만나고 싶다고 먼저 고백한다."
            advance until screen "choice"
            assert eval dating and memory["jihyun_confession_accepted"]
            assert eval affinity["jihyun"] == 24
            assert eval cream_relation_name("jihyun") == "교제 중"
            click expression jihyun_test_choice(case % 3)
        advance until eval memory.get("jihyun_test_done")
        assert eval dating == (case % 5 != 2)
        assert eval bool(memory.get("jihyun_r04_complete")) == (case % 5 != 2)
        assert eval ending == ("colleague" if case % 5 == 2 else "jihyun_early_segment_complete")
        assert eval first_kiss is False
        assert eval bool(persistent.local_jihyun_ending) == bool(case % 2)
        assert eval not any(k.startswith(("ria_","yujin_")) for k in memory)
        assert eval all(not phone_threads[k] for k in ("ria","yujin","seoyun"))
        assert eval len({r["id"] for r in phone_threads["jihyun"]}) == len(phone_threads["jihyun"])
        if eval case % 5 != 2:
            assert eval not cream_ria_visible() and not cream_yujin_visible()
        run Show("office_phone_archive")
        assert "백지현"
        if eval case == 0:
            screenshot "jihyun-message-history.png"
        click id "phone_archive_close"

    testcase preview_entry:
        screenshot "review-jihyun-main-menu.png"
        click id "jihyun_preview_button"
        advance until screen "office_phone"
        assert eval active_route == "jihyun" and phone_active_contact == "jihyun"
        assert eval memory.get("jihyun_intro") is None

    testcase common_to_jihyun:
        run Start()
'''
step='''        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval yujin_test_menu_end():
                click expression jihyun_test_common_caption()
'''
s+=step*42+'''        assert eval yujin_test_menu_end()
        assert eval active_route == "jihyun" and memory["jihyun_intro"] == "evidence"
        assert eval memory["jihyun_r04_complete"] and dating
        assert eval ending == "jihyun_early_segment_complete"
        assert eval not any(k.startswith("yujin_r") for k in memory)

    teardown:
        exit
'''
(P/'game/jihyun_tests.rpy').write_text(s,encoding='utf-8')
