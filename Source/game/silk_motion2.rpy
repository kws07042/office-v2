# 실크 UI 움직임 2차: 장 제목 카드, 타이틀 분위기, 메신저, 하트, 입상, 메뉴.
# 모두 '화면 움직임 효과' 설정을 따른다. 선택·기억·점수는 바꾸지 않는다.

default silk_last_chapter = None
default silk_phone_last = -100.0
default silk_phone_fresh_now = True

init 6 python:
    def silk_chapter_check():
        st = renpy.store
        if st.main_menu or getattr(st, "event_cut_active", False):
            return
        current = getattr(st, "chapter", None)
        if not current or current == st.silk_last_chapter:
            return
        st.silk_last_chapter = current
        if renpy.is_skipping() or not silk_motion_on():
            return
        code, title = silk_chapter_parts(current)
        if not code:
            return
        renpy.show_screen("silk_chapter_card", code=code, title=title, place=getattr(st, "location", ""), _tag="silk_chapter_card")

    config.start_interact_callbacks.append(silk_chapter_check)

    def silk_phone_fresh():
        # 직전 메신저 화면을 닫은 지 4초가 넘었으면 휴대폰이 새로 올라온다.
        return renpy.get_game_runtime() - renpy.store.silk_phone_last > 4.0

    def silk_phone_mark():
        renpy.store.silk_phone_last = renpy.get_game_runtime()

    def silk_phone_has_unread():
        threads = getattr(renpy.store, "phone_threads", {}) or {}
        return any(phone_unread(k) for k in threads)

    # 호감도 알림과 함께 게이지 쪽에서 작은 하트가 떠오른다.
    _silk_award_once_v1 = award_once

    def award_once(event, who, amount, trust=0):
        before = renpy.store.affinity.get(who, 0)
        _silk_award_once_v1(event, who, amount, trust)
        if renpy.store.affinity.get(who, 0) > before and not renpy.store.main_menu and silk_motion_on():
            renpy.show_screen("silk_heart_burst", _tag="silk_heart_burst")

# ── 장 제목 카드 ───────────────────────────────────────────────
transform silk_card_band:
    xoffset -1400 alpha 1.0
    easein 0.45 xoffset 0
    pause 1.5
    easeout 0.4 xoffset 1400

transform silk_card_text(delay=0.0):
    alpha 0.0 xoffset -30
    pause (0.25 + delay)
    easein 0.35 alpha 1.0 xoffset 0
    pause (1.25 - delay)
    easeout 0.3 alpha 0.0

transform silk_card_badge:
    zoom 0.4 alpha 0.0 rotate -20
    pause 0.2
    easein_back 0.45 zoom 1.0 alpha 1.0 rotate 0
    pause 1.3
    easeout 0.3 zoom 0.6 alpha 0.0

screen silk_chapter_card(code, title, place):
    zorder 35
    timer 2.5 action Hide("silk_chapter_card")
    fixed:
        add Solid("#3B0B22e6") xsize 1280 ysize 104 ypos 236 at silk_card_band
        add Solid("#B3123F") xsize 1280 ysize 4 ypos 236 at silk_card_band
        add Solid("#B3123F") xsize 1280 ysize 4 ypos 336 at silk_card_band
        fixed:
            xpos 150 ypos 250 xysize (76, 77)
            at silk_card_badge
            add silk("badge", size=(76, 77))
            text code font "fonts/Jua-Regular.ttf" size 25 color "#FFFDFB" xpos 36 ypos 36 xanchor 0.5 yanchor 0.5
        text title font silk_title_font(title) size 40 color "#FFFDFB" xpos 254 ypos 252 at silk_card_text(0.0)
        text place size 17 color "#F3E7EA" xpos 258 ypos 304 at silk_card_text(0.15)

# ── 타이틀 화면 분위기 ─────────────────────────────────────────
image silk title hearts = SnowBlossom(Transform(silk("heart", True, size=(16, 16)), alpha=0.28), count=14, border=40, xspeed=(-18, 18), yspeed=(-60, -25), start=0, fast=True, horizontal=False)
image silk title dots = SnowBlossom(Transform(silk("flat", "#FFFDFB", 6), xysize=(6, 6), alpha=0.55), count=22, border=20, xspeed=(-10, 10), yspeed=(-30, -12), start=0, fast=True, horizontal=False)

transform silk_logo_float:
    yoffset 0
    ease 2.6 yoffset -6
    ease 2.6 yoffset 0
    repeat

transform silk_logo_in:
    alpha 0.0 zoom 0.94
    easein 0.6 alpha 1.0 zoom 1.0

transform silk_band_in:
    xoffset -300 alpha 0.0
    easein 0.55 xoffset 0 alpha 1.0

# ── 메신저 ─────────────────────────────────────────────────────
transform silk_phone_rise:
    yoffset 90 alpha 0.0
    easein_back 0.42 yoffset 0 alpha 1.0

transform silk_bubble_pop:
    zoom 0.6 alpha 0.0
    easein_back 0.28 zoom 1.0 alpha 1.0

transform silk_phone_ring:
    rotate 0
    pause 2.2
    ease 0.06 rotate -12
    ease 0.08 rotate 12
    ease 0.08 rotate -9
    ease 0.08 rotate 9
    ease 0.06 rotate 0
    repeat

# ── 하트 ───────────────────────────────────────────────────────
transform silk_heart_rise(dx=0, delay=0.0):
    alpha 0.0 zoom 0.5 xoffset 0 yoffset 0
    pause delay
    parallel:
        easein 0.25 alpha 1.0 zoom 1.1
        easeout 0.6 alpha 0.0
    parallel:
        easeout 0.85 yoffset -46 xoffset dx

screen silk_heart_burst():
    zorder 41
    timer 1.4 action Hide("silk_heart_burst")
    if not main_menu and not event_cut_active:
        for i, (x, dx, d) in enumerate([(1150, -10, 0.0), (1178, 6, 0.12), (1206, 14, 0.24)]):
            add silk("heart", True, size=(18, 18)) xpos x ypos 46 at silk_heart_rise(dx, d)

# ── 입상(원화가 들어오면 바로 적용) ─────────────────────────────
transform silk_bust_idle:
    on show:
        alpha 0.0 yoffset 14
        easein 0.32 alpha 1.0 yoffset 0
        block:
            ease 2.4 yoffset -3
            ease 2.4 yoffset 0
            repeat
    on hide:
        easeout 0.2 alpha 0.0

# ── 메뉴 창 ────────────────────────────────────────────────────
transform silk_menu_panel:
    on show:
        alpha 0.0 zoom 0.965
        easein 0.24 alpha 1.0 zoom 1.0
