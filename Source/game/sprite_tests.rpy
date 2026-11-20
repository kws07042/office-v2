default sprite_step = 0

label sprite_preview:
    $ cream_preview_active = False
    $ cream_preview_mode = None
    $ chapter = "입상 확인"
    $ sprite_step = 1
    $ location = "수요일 오후 · 회의 공간"
    r "이번 시안 일정부터 확인할게요."
    $ sprite_step = 2
    $ location = "토요일 오후 · 비가 내리는 동네 카페"
    j "하하, 진짜요?"
    $ sprite_step = 3
    $ location = "다음 날 일요일 아침 · 유진의 집"
    y "좋아해요. 그 말 하고 싶었어요."
    $ sprite_step = 4
    $ location = "1월, 평일 저녁 · 퇴근길"
    s "고마워요. 오늘 와 줘서."
    $ sprite_step = 5
    $ location = "목요일 오전 · 탕비실"
    r "미안해. 내가 너무 몰아붙였지."
    $ sprite_step = 6
    $ location = "같은 날 저녁 · 개인 메시지"
    r "이 줄에서는 입상이 보이면 안 된다."
    $ sprite_step = 7
    $ location = "목요일 오전 · 탕비실"
    $ face("jihyun", "pout")
    j "이건 직접 정한 표정이에요."
    $ sprite_step = 8
    $ chapter = "리아 R13 · 다음엔 더 재밌게라는 말"
    r "오늘은 먼저 와서 기다리는 여자친구! 어때?"
    $ sprite_step = 9
    r "좋아하는데... 우리 여기까지 하자."
    $ sprite_step = 10
    return

testsuite sprite_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase stage_sprites:
        run Start("sprite_preview")
        advance until eval sprite_step == 1 and renpy.get_screen("say") timeout 20.0
        assert eval heroine_sprite_path("ria").endswith("ria_office_pose01_serious.png") or "_office_pose0" in heroine_sprite_path("ria")
        assert eval heroine_sprite_visible()
        screenshot "sprite-1-ria-office.png"
        advance until eval sprite_step == 2 timeout 10.0
        assert eval heroine_outfit("jihyun") == "casual" and heroine_face("jihyun") == "laugh"
        screenshot "sprite-2-jihyun-casual.png"
        advance until eval sprite_step == 3 timeout 10.0
        assert eval heroine_outfit("yujin") == "home" and heroine_sprite_path("yujin").endswith("yujin_home_pose01_blush.png")
        screenshot "sprite-3-yujin-home.png"
        advance until eval sprite_step == 4 timeout 10.0
        assert eval heroine_sprite_path("seoyun").endswith("seoyun_winter_pose01_smile.png")
        screenshot "sprite-4-seoyun-winter.png"
        advance until eval sprite_step == 5 timeout 10.0
        assert eval heroine_face("ria") == "sad"
        screenshot "sprite-5-ria-sad.png"
        advance until eval sprite_step == 6 timeout 10.0
        assert eval not heroine_sprite_visible()
        advance until eval sprite_step == 7 timeout 10.0
        assert eval heroine_sprite_path("jihyun").endswith("_pout.png") or heroine_sprite_path("jihyun").endswith("_serious.png")
        screenshot "sprite-7-jihyun-face-lock.png"
        advance until eval sprite_step == 8 and renpy.get_screen("say") timeout 10.0
        assert eval heroine_tense_scene() and heroine_face("ria") == "neutral"
        advance until eval sprite_step == 9 and renpy.get_screen("say") timeout 10.0
        assert eval heroine_face("ria") == "sad"
        advance until screen "main_menu" timeout 20.0

    teardown:
        exit
