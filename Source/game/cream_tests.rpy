label test_cream_speakers:
    $ chapter = "공통 · 인물 표시 검사"
    $ location = "오후 · 회사"
    r "리아 대화의 상반신 표시를 확인합니다."
    j "지현 대화에서는 리아 그림을 표시하지 않습니다."
    d "현재 대화 상대의 상태를 유지합니다."
    r "리아 대화로 돌아왔습니다."
    menu:
        "검사 종료":
            pass
    return

label test_cream_long:
    $ chapter = "강리아 · 긴 대사 확인"
    $ location = "오후 · 카페"
    r "처음에는 어디에 가면 좋을지부터 생각했는데, 오늘은 그냥 같이 있는 시간이 좋아. 네가 좋아하는 곳도 알고 싶고, 내가 쉬고 싶을 때는 먼저 말해 보고 싶어. 멋있는 계획이 없어도 다음에 또 만나고 싶다는 건 그대로니까~"
    menu:
        "검사 종료":
            pass
    return

label test_clear_r14:
    $ active_route = "ria"
    $ dating = True
    $ speech_informal = True
    $ affinity = {"ria":71, "jihyun":0, "yujin":0, "seoyun":0}
    $ completed = ["ria_R13"]
    $ memory = {"ria_conflict":"discussing", "ria_r13_response":"honest"}
    call ria_r14
    menu:
        "검사 종료":
            pass
    return

testsuite cream_ui_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase main_and_day_portrait:
        pause 0.2
        screenshot "cream-main.png"
        click id "preview_toggle"
        click id "cream_preview_button" until not screen "main_menu"
        pause 0.2
        assert eval cream_preview_active is True
        assert eval cream_stage_mode() == "day"
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        screenshot "cream-day-dialogue.png"
        advance until screen "choice"
        pause 0.2
        assert eval len(renpy.get_screen("choice").scope["items"]) == 3
        screenshot "cream-three-choices.png"
        click "조용한 카페에서 조금 더 이야기하자." until not screen "choice"
        assert eval cream_preview_reply == "cafe"
        assert eval affinity["ria"] == 58
        assert eval memory == {}

    testcase night_save_restore_and_history:
        run Start("cream_preview_start")
        click id "preview_night"
        pause 0.2
        assert eval cream_stage_mode() == "night"
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        screenshot "cream-night-dialogue.png"
        move pos (1200, 440)
        advance until screen "choice"
        pause 0.2
        screenshot "cream-night-choices.png"
        run FileSave("9", confirm=False)
        click "천천히 걷자. 목적지는 걸으면서 고르고." until not screen "choice"
        assert eval cream_preview_reply == "walk"
        click "저장" until screen "save"
        pause 0.2
        screenshot "cream-save.png"
        click "돌아가기" until not screen "save"
        run FileLoad("9", confirm=False)
        assert screen "choice" timeout 10.0
        assert eval cream_preview_reply is None
        assert eval cream_stage_mode() == "night"
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        click "기록" until screen "history"
        pause 0.2
        screenshot "cream-history.png"
        click "돌아가기" until not screen "history"
        click "설정" until screen "preferences"
        pause 0.2
        screenshot "cream-settings.png"
        click "돌아가기" until not screen "preferences"
        assert screen "choice"

    testcase speaker_identity:
        run Start("test_cream_speakers")
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        advance until eval cream_focus == "jihyun"
        assert eval cream_ria_visible() is False
        pause 0.1
        screenshot "cream-other-speaker.png"
        advance until eval cream_focus == "ria"
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))

    testcase long_dialogue:
        run Start("test_cream_long")
        pause 0.2
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        screenshot "cream-long-dialogue.png"
        click "저장" until screen "save"
        click "돌아가기" until not screen "save"
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))

    testcase transparent_text:
        run Start("test_cream_long")
        pause 0.2
        # Evening-threshold UI (PR #8): a solid dark panel with warm text replaced the transparent outlined text.
        assert eval renpy.get_widget("say", "window").style.background is not None
        assert eval renpy.get_widget("say", "window").style.foreground is None
        assert eval renpy.get_widget("say", "what").style.color == Color("#fff5ed")
        screenshot "clear-long-outlined-dialogue.png"

    testcase scaled_r14_choices:
        run Start("test_clear_r14")
        run renpy.set_physical_size((1792, 1008))
        advance until screen "choice"
        pause 0.4
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        assert eval len(renpy.get_screen("choice").scope["items"]) == 3
        assert eval renpy.get_physical_size()[0] >= 1700
        assert eval isinstance(cream_round("button"), CreamRoundedPanel)
        screenshot "clear-r14-scaled-1792.png"
        run renpy.set_physical_size((1280,720))

    teardown:
        exit
