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
