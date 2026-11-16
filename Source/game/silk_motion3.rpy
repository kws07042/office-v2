# 실크 UI 움직임 3차: 장소 전환, 엔딩 카드, 크레딧, 선택 피드백, 갤러리 반짝임.
# 모두 '화면 움직임 효과' 설정을 따른다(크레딧 화면 자체는 설정과 무관하게 볼 수 있다).

default silk_last_location = None
default silk_last_ending = ""

init -7 python:
    SILK_ENDINGS = {
        "ria_good": ("강리아", "같이 쉬는 사람"),
        "jihyun_good": ("백지현", "책임을 나누는 사람"),
        "yujin_good": ("차유진", "제 이름으로, 우리 마음으로"),
        "seoyun_good": ("한서윤", "함께 고르는 다음"),
        "colleague": ("동료 결말", "좋은 동료로, 우리"),
        "ria_relationship_closed": ("강리아", "서로의 자리로"),
        "jihyun_relationship_closed": ("백지현", "서로의 자리로"),
        "yujin_relationship_closed": ("차유진", "서로의 자리로"),
        "seoyun_relationship_closed": ("한서윤", "서로의 자리로"),
    }
    SILK_QUIET_PLACES = ("메시지", "연락", "각자의")

init 7 python:
    def silk_scene_check():
        st = renpy.store
        if st.main_menu or getattr(st, "event_cut_active", False):
            return
        place = getattr(st, "location", "") or ""
        ending = getattr(st, "ending", "") or ""
        motion = silk_motion_on() and not renpy.is_skipping()
        if ending != st.silk_last_ending:
            st.silk_last_ending = ending
            if ending in SILK_ENDINGS:
                silk_sfx("ending")
            if motion and ending in SILK_ENDINGS:
                who, title = SILK_ENDINGS[ending]
                renpy.show_screen("silk_ending_card", who=who, title=title, good=ending.endswith("_good"), _tag="silk_ending_card")
        if place != st.silk_last_location:
            first = st.silk_last_location is None
            st.silk_last_location = place
            if motion and not first and not any(w in place for w in SILK_QUIET_PLACES) and not renpy.get_screen("silk_chapter_card"):
                renpy.show_screen("silk_location_sweep", _tag="silk_location_sweep")

    config.start_interact_callbacks.append(silk_scene_check)

    def silk_pick(index, count, intimate):
        if not silk_motion_on():
            return
        bottom = 446 if intimate else 470
        y = bottom - (count - index) * 74 + 4
        renpy.show_screen("silk_pick_flash", y=y, _tag="silk_pick_flash")

# ── 장소 전환: 무대 위로 얇은 실크 커튼이 스친다 ──────────────────
transform silk_sweep:
    xoffset -1500 alpha 0.0
    linear 0.08 alpha 1.0
    ease 0.55 xoffset 1500
    linear 0.05 alpha 0.0

screen silk_location_sweep():
    zorder 34
    timer 0.75 action Hide("silk_location_sweep")
    add Solid("#B3123F33") xsize 520 ysize 510 at silk_sweep
    add Solid("#FFFDFB55") xsize 90 ysize 510 xpos 470 at silk_sweep

# ── 선택한 줄이 한 번 반짝인다 ─────────────────────────────────
transform silk_pick_glow:
    alpha 0.0 zoom 0.96
    easein 0.08 alpha 0.85 zoom 1.02
    easeout 0.35 alpha 0.0 zoom 1.06

screen silk_pick_flash(y):
    zorder 31
    timer 0.5 action Hide("silk_pick_flash")
    add silk("flat", "#FFFDFB", 32) xalign 0.5 ypos y xysize (624, 66) at silk_pick_glow

# ── 엔딩 카드 ─────────────────────────────────────────────────
transform silk_end_veil:
    alpha 0.0
    easein 0.5 alpha 1.0
    pause 4.2
    easeout 0.6 alpha 0.0

transform silk_end_word:
    alpha 0.0 zoom 1.25
    pause 0.35
    easein 0.7 alpha 1.0 zoom 1.0
    pause 3.4
    easeout 0.6 alpha 0.0

transform silk_end_line(delay=0.0):
    alpha 0.0 yoffset 16
    pause (0.9 + delay)
    easein 0.5 alpha 1.0 yoffset 0
    pause (2.7 - delay)
    easeout 0.6 alpha 0.0

transform silk_end_rule:
    xzoom 0.0 alpha 1.0
    pause 0.8
    easein 0.6 xzoom 1.0
    pause 3.0
    easeout 0.6 alpha 0.0

screen silk_ending_card(who, title, good):
    zorder 36
    timer 5.4 action Hide("silk_ending_card")
    add Solid("#3B0B22d9") at silk_end_veil
    if good:
        add "silk title hearts" at silk_end_veil
    text ("The End" if good else "Another Day") font "fonts/PlayfairDisplay-Italic.ttf" size 92 color "#FFFDFB" xalign 0.5 ypos 190 at silk_end_word
    add Solid("#B3123F") xysize (360, 3) xalign 0.5 ypos 316 at silk_end_rule
    text who font "fonts/Jua-Regular.ttf" size 30 color "#F3E7EA" xalign 0.5 ypos 338 at silk_end_line(0.0)
    text title font silk_title_font(title) size 44 color "#FFFDFB" xalign 0.5 ypos 384 at silk_end_line(0.2)

# ── 크레딧 ────────────────────────────────────────────────────
define silk_credits_rows = [
    ("title", "퇴근 후, 우리"),
    ("sub", "After Work, With You"),
    ("gap", ""),
    ("head", "기획 · 시나리오"),
    ("name", "퇴근 후, 우리 제작팀"),
    ("gap", ""),
    ("head", "캐릭터 · 원화"),
    ("name", "퇴근 후, 우리 제작팀"),
    ("gap", ""),
    ("head", "UI · 연출 · 프로그래밍"),
    ("name", "퇴근 후, 우리 제작팀"),
    ("gap", ""),
    ("head", "엔진"),
    ("name", "Ren'Py Visual Novel Engine"),
    ("gap", ""),
    ("head", "글꼴"),
    ("name", "Pretendard · Gowun Dodum · Jua · Playfair Display (SIL OFL 1.1)"),
    ("gap", ""),
    ("gap", ""),
    ("head", "강리아 · 백지현 · 차유진 · 한서윤"),
    ("name", "그리고 퇴근길을 함께해 준 당신에게"),
    ("gap", ""),
    ("sub", "Thank you for playing"),
]

transform silk_credits_roll:
    yoffset 760
    linear 26.0 yoffset -1100

screen silk_credits():
    tag menu
    modal True
    add "silk ground"
    add "silk title dots"
    key "game_menu" action Return()
    key "dismiss" action Return()
    vbox:
        xalign 0.5 spacing 14
        at silk_credits_roll
        for kind, value in silk_credits_rows:
            if kind == "title":
                text value font "fonts/Jua-Regular.ttf" size 64 color "#3B0B22" xalign 0.5
            elif kind == "sub":
                text value font "fonts/PlayfairDisplay-Italic.ttf" size 28 color "#B3123F" xalign 0.5
            elif kind == "head":
                text value font "fonts/Jua-Regular.ttf" size 22 color "#B3123F" xalign 0.5
            elif kind == "name":
                text value size 24 color "#3B0B22" xalign 0.5
            else:
                null height 24
    timer 27.5 action Return()
    textbutton "닫기" action Return() style "silk_small_button" xanchor 1.0 xpos 1248 ypos 24

# ── 갤러리 ────────────────────────────────────────────────────
transform silk_tile_in(i=0):
    alpha 0.0 yoffset 12
    pause (0.05 * i)
    easein 0.3 alpha 1.0 yoffset 0

transform silk_tile_spark(i=0):
    alpha 0.0 zoom 0.4
    pause (0.6 + 0.37 * (i % 5))
    block:
        easein 0.25 alpha 1.0 zoom 1.0
        easeout 0.35 alpha 0.0 zoom 0.6
        pause 2.4
        repeat
