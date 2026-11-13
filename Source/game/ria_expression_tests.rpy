init python:
    ria_expression_fixture = {}

    def ria_expression_test_caption(index):
        return renpy.substitute(renpy.get_screen("choice").scope["items"][index].caption)

label test_ria_r02_expression_entry:
    $ cream_focus = "ria"
    $ active_route = "ria"
    $ speech_informal = bool(ria_expression_fixture["case"] % 2)
    $ afterwork_preference = "quiet"
    $ completed = []
    $ memory = {}
    $ affinity = {"ria":14, "jihyun":0, "yujin":0, "seoyun":0}
    call ria_r02
    $ remember("ria_expression_test_returned")
    menu:
        "표정 흐름 검사 종료":
            pass
    return

testsuite ria_expression_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase expression_day_and_night:
        parameter mode = ["day", "night"]
        run Start("ria_expression_preview")
        run SetVariable("cream_preview_mode", mode)
        pause 0.4
        assert eval cream_stage_mode() == mode
        assert eval ria_expression == "base"
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        screenshot ("ria-expression-" + mode + "-base.png")
        advance until eval ria_expression == "smile"
        pause 0.2
        assert eval renpy.loadable("images/characters/ria/expressions/smile.png")
        screenshot ("ria-expression-" + mode + "-smile.png")
        advance until eval ria_expression == "shy"
        pause 0.2
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        screenshot ("ria-expression-" + mode + "-shy.png")
        advance until eval ria_expression == "serious"
        pause 0.2
        assert eval renpy.loadable("images/characters/ria/expressions/serious.png")
        screenshot ("ria-expression-" + mode + "-serious.png")
        advance until screen "choice"
        assert eval ria_expression == "base"
        assert eval renpy.loadable(RIA_MASTER_V2)

    testcase real_r02_all_choices_both_speech_styles:
        parameter case = list(range(18))
        $ ria_expression_fixture["case"] = case
        run Start("test_ria_r02_expression_entry")
        advance until screen "choice"
        assert eval ria_expression == "serious"
        assert eval len(renpy.get_screen("choice").scope["items"]) == 3
        click expression ria_expression_test_caption((case // 2) // 3) until not screen "choice"
        advance until screen "choice"
        assert eval len(renpy.get_screen("choice").scope["items"]) == 3
        if eval case == 1:
            screenshot "ria-r02-choices.png"
        click expression ria_expression_test_caption((case // 2) % 3) until not screen "choice"
        advance until eval ria_expression == "shy"
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        if eval case in (1, 3, 5):
            pause 0.2
            screenshot ("ria-r02-reaction-" + str(case) + ".png")
        advance until eval memory.get("ria_expression_test_returned")
        assert eval ria_expression == "base"
        assert eval affinity["ria"] == 21
        assert eval "ria_R02" in completed
        assert eval memory.get("ria_hand", False) == (((case // 2) % 3) == 0)
        assert eval memory.get("ria_memo_promise") is True
        assert eval memory.get("ria_contact_offer") is True

    testcase save_restores_expression:
        run Start("ria_expression_preview")
        advance until eval ria_expression == "shy"
        run FileSave("12", confirm=False)
        advance until eval ria_expression == "serious"
        assert eval ria_expression == "serious"
        run FileLoad("12", confirm=False)
        assert eval ria_expression == "shy"
        assert eval cream_ria_visible() == bool(renpy.loadable("images/characters/ria/ui_master_v2.png"))
        pause 0.2
        screenshot "ria-expression-restored.png"

    testcase main_menu_entry:
        screenshot "ria-expression-main-menu.png"
        click id "ria_r02_preview_button" until not screen "main_menu"
        assert eval chapter == "리아 R02 · 문 닫힌 가게 앞에서"
        assert eval ria_expression == "serious"
        assert eval speech_informal is True

    teardown:
        exit
