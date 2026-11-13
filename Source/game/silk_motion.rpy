# 실크와 립스틱 UI의 움직임. 화면 구성·선택·기억·점수는 바꾸지 않는다.
# 설정의 '화면 움직임 효과'를 끄면 모든 움직임이 멈춘 그대로 표시된다.

default persistent.silk_motion = True

init -8 python:
    def silk_motion_on():
        return persistent.silk_motion is not False

    SILK_GAIN_NAMES = {"ria": "강리아", "jihyun": "백지현", "yujin": "차유진", "seoyun": "한서윤"}

init 5 python:
    # 호감도가 실제로 오른 순간에만 작은 알림을 띄운다. 계산은 원래 함수가 그대로 한다.
    _silk_award_once_base = award_once

    def award_once(event, who, amount, trust=0):
        before = renpy.store.affinity.get(who, 0)
        _silk_award_once_base(event, who, amount, trust)
        gained = renpy.store.affinity.get(who, 0) - before
        if gained > 0 and who in SILK_GAIN_NAMES and not renpy.store.main_menu:
            renpy.show_screen("silk_gain", who=who, amount=gained, _tag="silk_gain")

transform silk_still:
    alpha 1.0

# 대화창: 장면이 바뀌거나 선택지·메뉴에서 돌아올 때 아래에서 올라온다.
transform silk_panel_in:
    on show:
        yoffset 26 alpha 0.0
        easein 0.28 yoffset 0 alpha 1.0
    on hide:
        easeout 0.16 yoffset 16 alpha 0.0

# 이름표: 처음엔 왼쪽에서 들어오고, 말하는 사람이 이어지면 살짝만 튄다.
transform silk_tag_in:
    on show:
        xoffset -26 alpha 0.0
        easein 0.22 xoffset 0 alpha 1.0
    on replace:
        yoffset 5 alpha 0.85
        easein 0.14 yoffset 0 alpha 1.0

transform silk_next_bob:
    yoffset 0 alpha 1.0
    ease 0.55 yoffset 5 alpha 0.55
    ease 0.55 yoffset 0 alpha 1.0
    repeat

# 선택지: 위에서부터 하나씩 떠오르고, 가리키면 오른쪽으로 비켜 선다.
transform silk_choice_in(i=0):
    alpha 0.0 yoffset 18
    pause (0.04 + i * 0.07)
    easein 0.24 alpha 1.0 yoffset 0

transform silk_choice_hover:
    on idle:
        ease 0.14 xoffset 0
    on hover, selected_hover:
        ease 0.14 xoffset 9

transform silk_chip_glow:
    alpha 1.0
    ease 0.9 alpha 0.72
    ease 0.9 alpha 1.0
    repeat

# 상단 장 카드와 호감도 패널
transform silk_header_in(dx=-40):
    on show:
        xoffset dx alpha 0.0
        easein 0.36 xoffset 0 alpha 1.0

transform silk_quick_hover:
    on idle:
        ease 0.12 yoffset 0
    on hover:
        ease 0.12 yoffset -3

# 메인 메뉴 항목이 순서대로 미끄러져 들어온다.
transform silk_menu_in(i=0):
    alpha 0.0 xoffset -30
    pause (0.15 + i * 0.08)
    easein 0.3 alpha 1.0 xoffset 0

transform silk_menu_hover:
    on idle:
        ease 0.15 zoom 1.0
    on hover, selected_hover:
        ease 0.15 zoom 1.04

transform silk_gain_float:
    alpha 0.0 yoffset 14
    easein 0.25 alpha 1.0 yoffset 0
    pause 1.3
    easeout 0.45 alpha 0.0 yoffset -12

transform silk_heart_pop:
    zoom 0.6
    easein 0.18 zoom 1.25
    easeout 0.22 zoom 1.0

screen silk_gain(who, amount):
    zorder 40
    timer 2.2 action Hide("silk_gain")
    if not main_menu and not event_cut_active:
        frame:
            at (silk_gain_float if silk_motion_on() else silk_still)
            xanchor 1.0 xpos 1248 ypos 112
            padding (16, 7, 20, 11)
            background silk("flat", "#3B0B22", 18)
            hbox:
                spacing 8
                add silk("heart", True, size=(18, 18)) yalign 0.5 at (silk_heart_pop if silk_motion_on() else silk_still)
                text SILK_GAIN_NAMES[who] font "fonts/Jua-Regular.ttf" size 17 color "#FFFDFB" outlines [] yalign 0.5
                text ("+" + str(amount)) font "fonts/Jua-Regular.ttf" size 19 color "#FFFDFB" outlines [] yalign 0.5
