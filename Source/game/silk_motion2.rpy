# 실크 UI 움직임 2차: 장 제목 카드, 타이틀 분위기, 메신저, 하트, 입상, 메뉴.
# 모두 '화면 움직임 효과' 설정을 따른다. 선택·기억·점수는 바꾸지 않는다.

default silk_last_chapter = None
default silk_phone_last = -100.0
default silk_phone_fresh_now = True
# 자동 테스트의 '다음 대사' 신호는 카드가 움직이는 동안 먹히므로 테스트 중에는 카드를 띄우지 않는다.
# (실제 마우스·Enter 입력은 카드가 떠 있어도 넘어간다. 카드 화면을 찍을 테스트만 True로 바꾼다.)
default silk_test_cards = False

init 6 python:
    def silk_chapter_check():
        st = renpy.store
        if st.main_menu or getattr(st, "event_cut_active", False):
            return
        current = getattr(st, "chapter", None)
        if not current or current == st.silk_last_chapter:
            return
        if silk_overlay_busy():
            return  # 선택지·메신저 위에는 띄우지 않고 다음 대사에서 보여 준다.
        st.silk_last_chapter = current
        if renpy.is_skipping() or not silk_cards_on():
            return
        code, title = silk_chapter_parts(current)
        if not code:
            return
        silk_sfx("whoosh")
        renpy.show_screen("silk_chapter_card", code=code, title=title, place=getattr(st, "location", ""), _tag="silk_chapter_card")

    def silk_cards_on():
        return silk_motion_on() and not (renpy.is_in_test() and not renpy.store.silk_test_cards)

    def silk_overlay_busy():
        return any(renpy.get_screen(n) for n in ("choice", "office_phone", "office_phone_archive", "event_cut"))

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
        if renpy.store.affinity.get(who, 0) > before and not renpy.store.main_menu:
            silk_sfx("heart")
            if silk_motion_on():
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
    alpha 0.0 yoffset 12
    pause 0.2
    easein 0.4 alpha 1.0 yoffset 0
    pause 1.35
    easeout 0.3 alpha 0.0

screen silk_chapter_card(code, title, place):
    # 장 제목 카드: 대화창과 같은 톤(어두운 그라데이션 띠 + 금색 선). 장 번호·제목·장소를 한 줄 가운데에 맞춘다.
    zorder 35
    timer 2.5 action Hide("silk_chapter_card")
    fixed:
        at silk_card_band
        add "gui/window/card_band.png" ypos 238
        add "gui/window/name_line.png" xysize (980, 2) ypos 238 matrixcolor TintMatrix("#E9C98E") alpha 0.8
        add "gui/window/name_line.png" xysize (980, 2) ypos 360 matrixcolor TintMatrix("#E9C98E") alpha 0.8
    hbox:
        xpos 150 ypos 300 yanchor 0.5 spacing 28
        vbox:
            at silk_card_badge
            yalign 0.5 spacing 0
            text "CHAPTER" font "fonts/PlayfairDisplay-Italic.ttf" size 16 color "#E9C98E" kerning 2.5 xalign 0.5 outlines []
            text code font "fonts/Pretendard-Regular.otf" size 46 color "#FFFFFF" kerning 2 xalign 0.5 outlines []
        add Solid("#E9C98E") xysize (1, 76) yalign 0.5 alpha 0.7 at silk_card_text(0.0)
        vbox:
            yalign 0.5 spacing 6
            text title font silk_title_font(title) size 40 color "#FFFFFF" outlines [] at silk_card_text(0.0)
            text place size 16 color "#F3E7EA" kerning 0.8 outlines [] at silk_card_text(0.15)

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
        for i, (x, dx, d) in enumerate([(974, -12, 0.0), (998, 2, 0.12), (1020, 14, 0.24)]):
            add silk("heart", True, size=(18, 18)) xpos x ypos 30 at silk_heart_rise(dx, d)

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
