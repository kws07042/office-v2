# 실크와 립스틱 UI의 화면 캡처와 기본 표시 확인. 본편의 선택·기억·점수는 바꾸지 않는다.
label test_silk_intimate:
    $ chapter = "리아 R07 · 오늘의 속도"
    $ location = "토요일 오후 · 비가 내리는 동네 카페"
    $ active_route = "ria"
    $ dating = True
    $ speech_informal = True
    $ affinity = {"ria":78, "jihyun":0, "yujin":0, "seoyun":0}
    r "그래도 오늘은 여기서 같이 밤을 보내고 싶어. 너는 어때?"
    menu:
        "같은 마음이라고 답한다 — 친밀한 장면으로 이어짐.":
            pass
        "오늘은 차를 마시고 돌아가고 싶다고 말한다.":
            pass
        "오늘은 밤을 보내기보다, 잠깐 더 앉아 서로의 마음을 이야기한다.":
            pass
    return

label test_silk_speakers:
    $ chapter = "C01 · 이름표 색 확인"
    $ location = "오후 · 회사"
    r "리아 이름표입니다."
    j "지현 이름표입니다."
    y "유진 이름표입니다."
    s "서윤 이름표입니다."
    d "도현 이름표입니다."
    "이름표가 없는 지문입니다."
    return

testsuite silk_ui_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase main_menu_look:
        pause 0.3
        screenshot "silk-main.png"

    testcase long_dialogue_look:
        run Start("test_cream_long")
        pause 0.3
        assert eval renpy.get_widget("say", "window").style.background is None
        assert eval renpy.get_widget("say", "what").style.color == Color("#3B0B22")
        assert eval renpy.get_widget("say", "who").style.color == Color("#FFFDFB")
        screenshot "silk-dialogue-long.png"

    testcase intimate_choice_look:
        run Start("test_silk_intimate")
        advance until screen "choice"
        pause 0.3
        assert eval len(renpy.get_screen("choice").scope["items"]) == 3
        assert eval silk_has_intimate(renpy.get_screen("choice").scope["items"]) is True
        screenshot "silk-choice-intimate.png"
        click "오늘은 차를 마시고 돌아가고 싶다고 말한다." until not screen "choice"

    testcase speaker_tags_look:
        run Start("test_silk_speakers")
        pause 0.3
        screenshot "silk-tag-ria.png"
        advance
        pause 0.2
        screenshot "silk-tag-jihyun.png"
        advance
        pause 0.2
        screenshot "silk-tag-yujin.png"
        advance
        pause 0.2
        screenshot "silk-tag-seoyun.png"
        advance
        pause 0.2
        screenshot "silk-tag-dohyun.png"
        advance
        pause 0.2
        screenshot "silk-narration.png"

    testcase save_look:
        run Start("test_cream_long")
        pause 0.3
        click "저장" until screen "save"
        pause 0.2
        screenshot "silk-save.png"
        click "돌아가기" until not screen "save"

    testcase preferences_look:
        run Start("test_cream_long")
        pause 0.3
        click "설정" until screen "preferences"
        pause 0.2
        screenshot "silk-preferences.png"

    testcase history_look:
        run Start("test_cream_long")
        pause 0.3
        click "기록" until screen "history"
        pause 0.2
        screenshot "silk-history.png"
        click "돌아가기" until not screen "history"

    teardown:
        exit
