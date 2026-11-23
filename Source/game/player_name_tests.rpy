# 주인공 이름 입력·조사 검사. 배포 패키지에 넣지 않는다.
default mc_card_in_test = False

label test_mc_card_entry:
    scene bg plain
    $ mc_card_in_test = True
    call player_name_card
    $ mc_card_in_test = False
    d "안녕하세요. 오늘부터 일하게 된 도현입니다."
    r "도현아, 여기!"
    "도현이 고개를 들었다. 리아는 도현을 보고 웃었다."
    return

testsuite player_name_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase josa_rules:
        $ mc_name = "민수"
        assert eval mc_apply("도현이 웃었다. 도현은 갔다. 도현을 봤다. 도현과 걸었다. 도현아, 도현으로, 도현이었다, 도현 씨, 도현의") == "민수가 웃었다. 민수는 갔다. 민수를 봤다. 민수와 걸었다. 민수야, 민수로, 민수였다, 민수 씨, 민수의"
        assert eval mc_apply("범인은 도현은. 이건 도현을!") == "범인은 민수는. 이건 민수를!"
        $ mc_name = "지훈"
        assert eval mc_apply("도현이 웃었다. 도현아, 도현으로") == "지훈이 웃었다. 지훈아, 지훈으로"
        $ mc_name = "한결"
        assert eval mc_apply("도현으로 정했다") == "한결로 정했다"
        $ mc_name = "공옥순"
        assert eval mc_apply("도현 씨, 도현아! 도현이 웃었다") == "공옥순 씨, 공옥순아! 공옥순이 웃었다"
        $ mc_name = "Alex"
        assert eval mc_apply("도현 씨, 도현이 웃었다, 도현아") == "Alex 씨, Alex가 웃었다, Alex야"
        $ mc_name = "Tom"
        assert eval mc_apply("도현이 웃었다, 도현으로") == "Tom이 웃었다, Tom으로"
        $ mc_name = "민수3"
        assert eval mc_apply("도현은 갔다") == "민수3은 갔다"
        $ mc_name = "도현"
        assert eval mc_apply("도현이 웃었다") == "도현이 웃었다"
        assert eval mc_valid("민수") and mc_valid("Alex") and mc_valid("공옥순99") and not mc_valid("") and not mc_valid("아홉글자짜리이름이다")

    testcase card_input_and_screen:
        run Start("test_mc_card_entry")
        advance until screen "employee_card" timeout 20.0
        assert eval mc_card_date and len(mc_card_date) == 10 and mc_card_number() == "GY-" + mc_card_date[:4] + "-" + mc_card_date[5:7] + mc_card_date[8:]
        pause 0.5
        screenshot "player-name-1-card.png"
        click id "mc_card_confirm"
        pause 0.3
        assert eval mc_card_message != "" and renpy.get_screen("employee_card") is not None
        $ mc_name_input = "공옥순"
        pause 0.3
        screenshot "player-name-1b-typed.png"
        click id "mc_card_confirm"
        advance until eval mc_name == "공옥순" and renpy.get_screen("employee_card") is None timeout 10.0
        pause 0.6
        screenshot "player-name-2-dialogue.png"
        advance
        advance
        pause 0.5
        screenshot "player-name-3-josa.png"
        $ mc_name = "도현"

    teardown:
        exit
