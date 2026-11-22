# 타이틀 화면: 도현의 회사 PC 바탕화면 (시안 T3).
# 키 비주얼을 바탕화면으로 깔고, 메뉴는 바탕화면 아이콘과 작업 표시줄의 '퇴근 후' 시작 메뉴로 연다.
# 아이콘과 면은 모두 코드로 그린 SVG라 외부 그림 파일이 없다.
# 키 비주얼이 없으면 예전 실크 타이틀(main_menu_silk)을 그대로 쓴다.

init -2 python:
    import time as _dt_time

    def silk_b_glass(w, h, fill, opacity, radius, stroke=None):
        out = '<rect x="0" y="0" width="%d" height="%d" rx="%s" fill="%s" fill-opacity="%s"/>' % (w, h, min(radius, h / 2.0), fill, opacity)
        if stroke:
            out += '<rect x="1" y="1" width="%d" height="%d" rx="%s" fill="none" stroke="%s" stroke-opacity="0.5" stroke-width="1.5"/>' % (w - 2, h - 2, min(radius, h / 2.0), stroke)
        return out

    def silk_b_startbtn(w, h):
        return ('<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">'
                '<stop offset="0" stop-color="#C8173F"/><stop offset="1" stop-color="#7C1A6D"/></linearGradient></defs>'
                '<rect x="0" y="0" width="%d" height="%d" rx="9" fill="url(#g)"/>' % (w, h))

    def silk_b_note(w, h):
        return ('<rect x="4" y="6" width="%d" height="%d" fill="#000000" fill-opacity="0.28"/>'
                '<rect x="0" y="0" width="%d" height="%d" fill="#FFF2A8"/>'
                '<rect x="%d" y="-6" width="64" height="18" fill="#FFFFFF" fill-opacity="0.6"/>' % (w - 4, h - 6, w - 4, h - 6, (w - 64) // 2))

    DESKTOP_ICON_SVG = {
        "doc": '<rect x="8" y="5" width="32" height="38" rx="3" fill="#FFFFFF"/><path d="M29 5v8a3 3 0 003 3h8z" fill="#DFE6F3"/>'
               '<rect x="14" y="22" width="20" height="2.5" rx="1" fill="#B3123F"/><rect x="14" y="28" width="16" height="2.5" rx="1" fill="#C9CFDB"/>'
               '<rect x="14" y="34" width="12" height="2.5" rx="1" fill="#C9CFDB"/>',
        "folder_play": '<path d="M4 12a3 3 0 013-3h11l4 4h19a3 3 0 013 3v22a3 3 0 01-3 3H7a3 3 0 01-3-3z" fill="#F2C14E"/>'
                       '<path d="M4 18h40v20a3 3 0 01-3 3H7a3 3 0 01-3-3z" fill="#FFD66E"/><path d="M20 25l9 4.5-9 4.5z" fill="#8A5A00"/>',
        "album": '<rect x="9" y="6" width="30" height="36" rx="3" fill="#B3123F"/><rect x="13" y="6" width="3" height="36" fill="#7C0E2D"/>'
                 '<path d="M27 18c-2-3-7-2-7 2 0 3 4 6 7 8 3-2 7-5 7-8 0-4-5-5-7-2z" fill="#FFD6DE"/>',
        "photo": '<rect x="6" y="9" width="36" height="30" rx="3" fill="#FFFFFF"/><rect x="9" y="12" width="30" height="20" fill="#7C5CC4"/>'
                 '<circle cx="31" cy="18" r="3" fill="#FFD66E"/><path d="M9 32l9-10 7 7 4-4 10 7z" fill="#C8173F"/>',
        "pad": '<rect x="5" y="14" width="38" height="22" rx="11" fill="#E7A88F"/><rect x="12" y="23" width="9" height="3" rx="1" fill="#FFFFFF"/>'
               '<rect x="15" y="20" width="3" height="9" rx="1" fill="#FFFFFF"/><circle cx="32" cy="22" r="2.4" fill="#FFFFFF"/><circle cx="36" cy="27" r="2.4" fill="#FFFFFF"/>',
        "flower": '<circle cx="24" cy="15" r="7" fill="#F7B6C8"/><circle cx="15" cy="23" r="7" fill="#F7B6C8"/><circle cx="33" cy="23" r="7" fill="#F7B6C8"/>'
                  '<circle cx="19" cy="32" r="7" fill="#F7B6C8"/><circle cx="29" cy="32" r="7" fill="#F7B6C8"/><circle cx="24" cy="24" r="5" fill="#F2C14E"/>',
        "gear": '<g fill="#9AA3B5"><rect x="21" y="3" width="6" height="8" rx="1"/><rect x="21" y="37" width="6" height="8" rx="1"/>'
                '<rect x="3" y="21" width="8" height="6" rx="1"/><rect x="37" y="21" width="8" height="6" rx="1"/></g>'
                '<circle cx="24" cy="24" r="16" fill="#9AA3B5"/><circle cx="24" cy="24" r="7" fill="#E9EDF5"/>',
        "card": '<rect x="5" y="10" width="38" height="28" rx="3" fill="#FFFDFB"/><circle cx="16" cy="22" r="5" fill="#C9CFDB"/>'
                '<rect x="12" y="29" width="8" height="4" rx="2" fill="#C9CFDB"/><rect x="25" y="18" width="13" height="2.5" rx="1" fill="#B3123F"/>'
                '<rect x="25" y="24" width="10" height="2.5" rx="1" fill="#C9CFDB"/><rect x="25" y="30" width="12" height="2.5" rx="1" fill="#C9CFDB"/>',
        "bin": '<path d="M12 14h24l-2 28H14z" fill="#CFD6E3"/><rect x="9" y="9" width="30" height="5" rx="2" fill="#AEB7C8"/>'
               '<rect x="19" y="5" width="10" height="5" rx="2" fill="#AEB7C8"/>',
        "wifi": '<path d="M24 37l6-7.2a9.2 9.2 0 00-12 0zM11.2 23.4l3.8 4.4a14 14 0 0118 0l3.8-4.4a20 20 0 00-25.6 0zM4 15l3.8 4.6a26 26 0 0132.4 0L44 15a32 32 0 00-40 0z" fill="#FFFFFF"/>',
    }

    def silk_b_dicon(w, h, name):
        return '<g transform="scale(%s,%s)">%s</g>' % (w / 48.0, h / 48.0, DESKTOP_ICON_SVG[name])

    def desktop_clock():
        t = _dt_time.localtime()
        return "%02d:%02d" % (t.tm_hour, t.tm_min), "%04d-%02d-%02d" % (t.tm_year, t.tm_mon, t.tm_mday)

    def desktop_items():
        """(아이콘, 이름, 동작, 버튼 id). 테스트가 누르는 id는 예전 타이틀과 같다."""
        new_game = [SetVariable("cream_preview_active", False), SetVariable("cream_preview_mode", None), Start()]
        items = [
            ("doc", "처음부터", new_game, "start_button"),
            ("folder_play", "이어하기", ShowMenu("load"), "continue_button"),
            ("album", "우리의 기록", ShowMenu("progression_hub"), "album_button"),
            ("photo", "회상 갤러리", ShowMenu("gallery"), "gallery_button"),
            ("pad", "미니게임", ShowMenu("minigame_hub"), "minigame_button"),
        ]
        if spring_story_unlocked():
            items.append(("flower", "숨은 이야기\n이듬해 봄", Start("spring_story"), "spring_story_button"))
        items += [
            ("gear", "환경 설정", ShowMenu("preferences"), "prefs_button"),
            ("card", "크레딧", ShowMenu("silk_credits"), "credits_button"),
        ]
        if not renpy.variant("web"):
            items.append(("bin", "퇴근(종료)", Quit(confirm=False), "quit_button"))
        return items

style desk_icon_button is button:
    xysize (104, 96)
    padding (4, 8, 4, 6)
    background None
    hover_background silk("glass", "#7FB2FF", 0.28, 8, "#A9CCFF")
style desk_icon_text is default:
    font "fonts/GowunDodum-Regular.ttf"
    size 15
    color "#FFFFFF"
    outlines [(2, "#00000099", 0, 1)]
    text_align 0.5
    xalign 0.5
    line_spacing -2
style desk_start_item is button:
    xsize 356
    padding (14, 9, 14, 9)
    background None
    hover_background silk("glass", "#FFFFFF", 0.1, 8)
style desk_start_text is default:
    font "fonts/GowunDodum-Regular.ttf"
    size 19
    color "#F2EBF8"
style desk_start_caption is default:
    font "fonts/PlayfairDisplay-Italic.ttf"
    size 13
    color "#FFFFFF77"
    yalign 0.5
style desk_tiny is default:
    font "fonts/GowunDodum-Regular.ttf"
    size 14
    color "#FFFFFFCC"

screen main_menu():
    tag menu
    default start_open = False
    default show_preview_links = False
    if not renpy.loadable("images/cg/title_keyvisual.jpg"):
        use main_menu_silk
    else:
        $ items = desktop_items()
        $ clock, today = desktop_clock()
        add "images/cg/title_keyvisual.jpg"
        timer 20.0 repeat True action Function(renpy.restart_interaction)

        # 바탕화면 아이콘: 세로 4칸씩 채운다.
        for n, (icon, label, act, bid) in enumerate(items):
            button:
                id bid
                style "desk_icon_button"
                selected False
                xpos 16 + (n // 4) * 108 ypos 16 + (n % 4) * 100
                at ((silk_menu_in(n),) if silk_motion_on() else (silk_still,))
                action ([SetScreenVariable("start_open", False)] + (act if isinstance(act, list) else [act]))
                alt label.replace("\n", " ")
                if n == 0:
                    default_focus True
                vbox:
                    xalign 0.5 spacing 5
                    add silk("dicon", icon, size=(50, 50)) xalign 0.5
                    text label style "desk_icon_text"

        # 포스트잇
        fixed:
            xpos 360 ypos 26 xysize (220, 150)
            at Transform(rotate=-2.5, rotate_pad=False)
            add silk("note", size=(220, 150))
            vbox:
                xpos 18 ypos 16 spacing 2
                text "오늘 할 일" font "fonts/Jua-Regular.ttf" size 21 color "#4A3A10"
                text "{s}· 행사장 안내판 고치기{/s}" font "fonts/GowunDodum-Regular.ttf" size 15 color "#4A3A1088"
                text "· 피칭 자료 3장까지" font "fonts/GowunDodum-Regular.ttf" size 15 color "#4A3A10"
                text "· 6시 정시 퇴근!!" font "fonts/GowunDodum-Regular.ttf" size 15 color "#4A3A10"

        # 로고
        vbox:
            at ((silk_logo_in,) if silk_motion_on() else (silk_still,))
            xpos 36 yanchor 1.0 ypos 648 spacing -4
            text "After Work, With You" font "fonts/PlayfairDisplay-Italic.ttf" size 21 color "#FFE3E9" outlines [(2, "#3B0B2288", 0, 1)] xpos 4
            text "퇴근 후{color=#F2C14E},{/color} 우리":
                font "fonts/Jua-Regular.ttf"
                size 72
                kerning -1
                color "#FFFFFF"
                outlines [(3, "#3B0B22AA", 0, 3)]

        # 시작 메뉴
        if start_open:
            button:
                xysize (1280, 664) background None action SetScreenVariable("start_open", False)
            frame:
                id "desktop_start_menu"
                xpos 10 yanchor 1.0 ypos 656 xsize 388
                padding (16, 16, 16, 14)
                background silk("glass", "#211A38", 0.96, 14, "#FFFFFF")
                at ((silk_menu_in(0),) if silk_motion_on() else (silk_still,))
                vbox:
                    spacing 2
                    hbox:
                        spacing 12
                        fixed:
                            xysize (44, 44)
                            add silk("flat", "#555566", 22)
                            text "도" font "fonts/Jua-Regular.ttf" size 20 color "#FFFFFF" align (0.5, 0.5)
                        vbox:
                            yalign 0.5
                            text "도현" font "fonts/GowunDodum-Regular.ttf" size 18 color "#FFFFFF"
                            text "온빛브랜딩 · 연말 피칭 TF" style "desk_tiny" size 13 color "#FFFFFF99"
                    null height 10
                    add Solid("#FFFFFF22") ysize 1
                    null height 6
                    for icon, label, act, bid in items:
                        button:
                            style "desk_start_item"
                            selected False
                            action ([SetScreenVariable("start_open", False)] + (act if isinstance(act, list) else [act]))
                            alt label.replace("\n", " ")
                            hbox:
                                spacing 12
                                add silk("dicon", icon, size=(26, 26)) yalign 0.5
                                text label.replace("\n", " · ") style "desk_start_text" yalign 0.5

        # 작업 표시줄
        frame:
            xpos 0 ypos 664 xysize (1280, 56) padding (10, 8, 18, 8)
            background silk("glass", "#1B1530", 0.88, 0)
            hbox:
                spacing 8 yalign 0.5
                button:
                    id "desktop_start_button"
                    xysize (118, 40)
                    background silk("startbtn")
                    hover_background silk("startbtn")
                    action ToggleScreenVariable("start_open")
                    alt "시작 메뉴"
                    at ((silk_menu_hover,) if silk_motion_on() else (silk_still,))
                    text "퇴근 후{color=#F2C14E},{/color}" font "fonts/Jua-Regular.ttf" size 21 color "#FFFFFF" align (0.5, 0.5)
                frame:
                    ysize 40 padding (14, 0, 14, 0)
                    background silk("glass", "#FFFFFF", 0.07, 8)
                    text "피칭_최종_진짜최종.pptx" style "desk_tiny" yalign 0.5
            hbox:
                xalign 1.0 yalign 0.5 spacing 16
                text ("ver " + config.version) style "desk_tiny" size 12 color "#FFFFFF77" yalign 0.5
                add silk("dicon", "wifi", size=(20, 20)) yalign 0.5
                vbox:
                    yalign 0.5
                    text clock style "desk_tiny" color "#FFFFFF" xalign 1.0
                    text today style "desk_tiny" size 12 xalign 1.0

        key "game_menu" action SetScreenVariable("start_open", False)

        # 개발 중 확인용 진입점. 배포판(개발자 모드 꺼짐)에서는 보이지 않는다.
        if config.developer:
            vbox:
                xanchor 1.0 xpos 1248 ypos 24 spacing 5
                textbutton "테스트 장면" id "preview_toggle" action ToggleScreenVariable("show_preview_links") style "silk_small_button" xalign 1.0
                if show_preview_links:
                    hbox:
                        spacing 6 xalign 1.0
                        textbutton "화면 배치 확인" action Start("cream_preview_start") id "cream_preview_button" style "silk_small_button"
                        textbutton "R02 대화 확인" action Start("ria_r02_preview") id "ria_r02_preview_button" style "silk_small_button"
                        textbutton "R08 메신저 확인" action Start("office_phone_preview") id "phone_preview_button" style "silk_small_button"
                    hbox:
                        spacing 6 xalign 1.0
                        textbutton "유진 전체 대본 확인" action Start("yujin_early_preview") id "yujin_preview_button" style "silk_small_button"
                        textbutton "지현 전체 대본 확인" action Start("jihyun_early_preview") id "jihyun_preview_button" style "silk_small_button"
                        textbutton "서윤 전체 대본 확인" action Start("seoyun_preview") id "seoyun_preview_button" style "silk_small_button"
