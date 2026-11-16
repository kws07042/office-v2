# 소리: 장소 분위기에 맞춘 배경음과 화면 효과음.
# 음원은 모두 Source/tools/make_audio.py로 직접 합성한 것이다(외부 샘플 없음).
# 파일이 없으면 조용히 건너뛰므로, 나중에 같은 이름의 파일로 바꿔 끼우면 된다.

define config.main_menu_music = "audio/bgm/title.ogg"
define config.enter_sound = "audio/sfx/menu.ogg"
define config.exit_sound = "audio/sfx/menu.ogg"
define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.8
define config.fade_music = 1.2

style button:
    hover_sound "audio/sfx/hover.ogg"
    activate_sound "audio/sfx/click.ogg"

style silk_choice_button:
    activate_sound "audio/sfx/pick.ogg"

init -6 python:
    SILK_BGM = {
        "title": "audio/bgm/title.ogg",
        "office": "audio/bgm/office.ogg",
        "cafe": "audio/bgm/cafe.ogg",
        "evening": "audio/bgm/evening.ogg",
        "night": "audio/bgm/night.ogg",
        "home": "audio/bgm/home.ogg",
        "pitch": "audio/bgm/pitch.ogg",
        "ending": "audio/bgm/ending.ogg",
    }

    # 위에서부터 먼저 맞는 규칙을 쓴다. 장소 문자열의 '·' 뒤쪽(장소)만 본다.
    SILK_MOOD_RULES = (
        ("night", ("회식", "포차", "모텔", "숙소")),
        ("evening", ("집 앞",)),
        ("cafe", ("카페", "찻집", "서점", "책방", "전시", "식당", "가게")),
        ("home", ("집", "작업실")),
        ("evening", ("퇴근", "옥상", "횡단보도", "계단", "역", "골목", "산책", "공원", "벤치", "정류장", "길", "앞", "강변")),
    )

    def silk_bgm_mood(location, ending):
        if ending in SILK_ENDINGS:
            return "ending"
        location = location or ""
        if any(w in location for w in ("메시지", "연락")):
            return None
        when, _, place = location.rpartition("·")
        place = place.strip()
        if "피칭 당일" in when and ("클라이언트사" in place or "회의" in place):
            return "pitch"
        mood = "office"
        for name, words in SILK_MOOD_RULES:
            if any(w in place for w in words):
                mood = name
                break
        if "밤" in when and mood in ("evening", "cafe"):
            mood = "night"
        return mood

    def silk_sfx(name):
        path = "audio/sfx/%s.ogg" % name
        if renpy.is_skipping() or not renpy.loadable(path):
            return
        renpy.play(path, channel="audio")

init 8 python:
    def silk_audio_check():
        st = renpy.store
        if st.main_menu:
            return
        mood = silk_bgm_mood(getattr(st, "location", ""), getattr(st, "ending", ""))
        if mood is None:
            return
        path = SILK_BGM[mood]
        if not renpy.loadable(path) or renpy.music.get_playing("music") == path:
            return
        renpy.music.play(path, channel="music", loop=True, fadeout=1.5, fadein=2.0, if_changed=True)

    config.start_interact_callbacks.append(silk_audio_check)
