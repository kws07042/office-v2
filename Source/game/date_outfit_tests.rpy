# R12 데이트 옷(special) 입상 전환 검사. 배포 패키지에 넣지 않는다.
testsuite date_outfit_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase special_outfit_only_during_date:
        $ date_outfit = set()
        assert eval heroine_outfit("ria", "토요일 저녁 일곱 시 · 역 앞") == "casual"
        $ date_outfit_on("ria")
        # 그림이 아직 없으면 예전 옷 그대로
        assert eval heroine_has_outfit("ria", "special") or heroine_outfit("ria", "토요일 저녁 일곱 시 · 역 앞") == "casual"
        $ _saved = dict(SPRITE_SET)
        $ SPRITE_SET[("ria", "special", "pose01")] = {"neutral"}
        assert eval heroine_outfit("ria", "토요일 저녁 일곱 시 · 역 앞") == "special"
        assert eval heroine_outfit("ria", "토요일 밤 · 리아의 집") == "special"
        assert eval heroine_outfit("ria", "다음 날 일요일 아침 · 리아의 집") == "home"
        assert eval heroine_outfit("jihyun", "토요일 저녁 일곱 시 · 역 앞") != "special"
        $ date_outfit_off("ria")
        assert eval heroine_outfit("ria", "토요일 밤 · 리아의 집") == "home"
        $ SPRITE_SET.clear()
        $ SPRITE_SET.update(_saved)

    teardown:
        exit

default date_test_who = "ria"

label test_date_outfit_scene:
    $ who = date_test_who
    $ line = "오늘 옷, 너 만나려고 고른 거야."
    scene bg plain
    $ active_route = who
    $ dating = True
    $ cream_focus = who
    $ location = "금요일 저녁 일곱 시 · 약속한 식당"
    $ date_outfit_on(who)
    $ renpy.say({"ria": r, "jihyun": j, "yujin": y, "seoyun": s}[who], line)
    $ location = "같은 밤 · %s의 집" % {"ria": "리아", "jihyun": "지현", "yujin": "유진", "seoyun": "서윤"}[who]
    $ renpy.say({"ria": r, "jihyun": j, "yujin": y, "seoyun": s}[who], "들어와. 오늘은 같이 있고 싶어.")
    $ date_outfit_off(who)
    return

testsuite date_outfit_screens:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase date_outfit_on_screen:
        parameter who = ["ria", "jihyun", "yujin", "seoyun"]
        $ date_test_who = who
        run Start("test_date_outfit_scene")
        pause 1.2
        assert eval heroine_outfit(who) == "special"
        screenshot ("date-outfit-" + who + "-1-restaurant.png")
        advance
        pause 1.2
        assert eval heroine_outfit(who) == "special"
        screenshot ("date-outfit-" + who + "-2-home.png")

    teardown:
        exit
