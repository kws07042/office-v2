# 배경·입상·장면 CG가 실제로 무대에 그려지는지 확인한다(개발용).
default art_step = 0

label art_preview:
    $ cream_preview_active = False
    $ cream_preview_mode = None
    $ chapter = "그림 연결 확인"
    $ cream_focus = "ria"
    $ art_step = 1
    $ location = "수요일 오전 · 디자인 작업 공간"
    r "사무실 배경에 업무복."
    $ art_step = 2
    $ cream_focus = "seoyun"
    $ location = "토요일 오후 · 단골 북카페"
    s "북카페 배경에 새 사복."
    $ art_step = 3
    $ cream_focus = "jihyun"
    $ location = "토요일 저녁 · 지현의 집"
    j "저녁 집 배경."
    $ art_step = 4
    $ cream_focus = "yujin"
    $ location = "일요일 밤 · 유진의 집"
    $ face("yujin", "teary")
    y "밤, 울먹 표정은 생활복에 없어서 슬픔으로."
    $ face("yujin")
    $ art_step = 5
    $ location = "토요일 오후 · 비가 내리는 동네 카페"
    $ cg("ria_r07")
    r "장면 CG가 뜨고 입상은 숨는다."
    $ art_step = 6
    $ location = "토요일 오후 · 동네 산책길"
    r "장소가 바뀌면 CG가 내려간다."
    $ art_step = 7
    return

testsuite art_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)

    testcase stage_art:
        screenshot "art-0-title.png"
        run Start("art_preview")
        advance until eval art_step == 1 and renpy.get_screen("say") timeout 20.0
        assert eval art_bg_path() == "images/bg/bg_office.jpg" and heroine_sprite_visible()
        screenshot "art-1-office.png"
        advance until eval art_step == 2 and renpy.get_screen("say") timeout 10.0
        assert eval art_bg_path() == "images/bg/bg_bookcafe.jpg" and heroine_sprite_path("seoyun").startswith("images/characters/seoyun/seoyun_casual_")
        screenshot "art-2-bookcafe.png"
        advance until eval art_step == 3 and renpy.get_screen("say") timeout 10.0
        assert eval art_time() == "evening" and art_bg_path() == "images/bg/bg_jihyun_home.jpg"
        screenshot "art-3-evening.png"
        advance until eval art_step == 4 and renpy.get_screen("say") timeout 10.0
        assert eval art_time() == "night" and heroine_sprite_path("yujin").endswith("_sad.png")
        screenshot "art-4-night.png"
        advance until eval art_step == 5 and renpy.get_screen("say") timeout 10.0
        assert eval art_cg_path() == "images/cg/ria_r07.jpg" and not heroine_sprite_visible() and "ria_r07" in persistent.cg_seen
        screenshot "art-5-cg.png"
        advance until eval art_step == 6 and renpy.get_screen("say") timeout 10.0
        assert eval art_cg_path() is None
        advance until screen "main_menu" timeout 20.0

    teardown:
        exit
