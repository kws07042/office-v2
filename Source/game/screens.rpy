define prototype_font = FontGroup().add("DejaVuSans.ttf", 0x0000, 0x04ff).add("DejaVuSans.ttf", 0x2000, 0x206f).add("SourceHanSansLite.ttf", 0x0500, 0x1fff).add("SourceHanSansLite.ttf", 0x2070, 0xffff)

# 화면 모양은 실크와 립스틱(E안)을 따른다. 그리기 도구와 색은 silk_ui.rpy에 있다.
style default:
    font prototype_font
    size 26
    color "#3B0B22"
style button:
    padding (22, 12, 26, 17)
    background silk_surface("button")
    hover_background silk_surface("hover")
    selected_background silk_surface("selected")
    insensitive_background silk_surface("soft")
style button_text:
    color "#3B0B22"
    hover_color "#FFFDFB"
    selected_color "#FFFDFB"
    insensitive_color "#A3959B"
style choice_button is button:
    padding (22, 12, 26, 17)
    xfill True
    yminimum 52
style choice_button_text is button_text:
    size 20
    xalign 0.5
    text_align 0.5
style cream_quick_button is button:
    background None
    hover_background None
    selected_background None
    insensitive_background None
    padding (9, 5)
style cream_quick_button_text is button_text:
    size 15
    color "#6E4553"
    hover_color "#3B0B22"
    selected_color "#3B0B22"
style event_text is default:
    color "#eef0f5"
style event_button is button:
    background Solid("#303a53")
    hover_background Solid("#4c5676")
    selected_background Solid("#4c5676")
    insensitive_background Solid("#252c40")
style event_button_text is button_text:
    color "#eef0f5"
    hover_color "#fff3d9"
    selected_color "#fff3d9"

screen cream_stage():
    zorder -100
    if not main_menu and not event_cut_active:
        add ("gui/cream/stage_" + cream_stage_mode() + ".svg") xysize (1280, 720)
        if cream_ria_visible():
            add "ria ui bust" xalign 0.5 ypos 28
        elif cream_yujin_visible():
            add "yujin ui bust" xalign 0.5 ypos 50

screen cream_heart(fraction):
    fixed:
        xsize 20 ysize 20
        add silk("heart", False, size=(20, 20))
        if fraction > 0:
            add Crop((0, 0, max(1, int(20 * min(1.0, fraction))), 20), silk("heart", True, size=(20, 20)))

screen story_header():
    zorder 10
    if not main_menu and not event_cut_active and not cream_menu_open():
        $ chapter_code, chapter_title = silk_chapter_parts(chapter)
        frame:
            at (silk_header_in(-40) if silk_motion_on() else silk_still)
            xpos (84 if chapter_code else 32) ypos 30 xmaximum 440
            padding ((34 if chapter_code else 24), 9, 28, 14)
            background silk_surface("button")
            vbox:
                spacing 1
                text chapter_title font silk_title_font(chapter_title) size 21 color "#3B0B22" xmaximum 370
                text location size 13 color "#6E4553" xmaximum 370
        if chapter_code:
            fixed:
                at (silk_header_in(-40) if silk_motion_on() else silk_still)
                xpos 32 ypos 26 xysize (72, 73)
                add silk("badge", size=(72, 73))
                text chapter_code font "fonts/Jua-Regular.ttf" size 23 color "#FFFDFB" xpos 34 ypos 34 xanchor 0.5 yanchor 0.5
        $ focus = active_route if active_route in affinity else (cream_focus if cream_focus in affinity else "ria")
        $ person_name = {"ria":"강리아", "jihyun":"백지현", "yujin":"차유진", "seoyun":"한서윤"}[focus]
        frame:
            at (silk_header_in(40) if silk_motion_on() else silk_still)
            xanchor 1.0 xpos 1248 ypos 30
            padding (20, 10, 24, 15)
            background silk_surface("button")
            vbox:
                spacing 4
                hbox:
                    spacing 12
                    text person_name font "fonts/Jua-Regular.ttf" size 20 color "#3B0B22" yalign 0.5
                    hbox:
                        spacing 3 yalign 0.5
                        for index in range(5):
                            use cream_heart((affinity[focus] - index * 20) / 20.0)
                hbox:
                    spacing 10
                    text cream_relation_name(focus) size 12 color "#6E4553"
                    text (str(affinity[focus]) + " / 100") size 12 color "#6E4553"
        if cream_preview_active:
            use cream_preview_controls

screen cream_dialogue_panel(who, what, use_substitution=True, advance=True):
    # 레이스 가장자리가 달린 종이 면. 창 자체의 배경은 비워 두고 면은 따로 그린다.
    add silk("dialogue", size=(1280, 206)) xpos 0 ypos 514 at (silk_panel_in if silk_motion_on() else silk_still)
    window:
        at (silk_panel_in if silk_motion_on() else silk_still)
        id "window"
        xpos 0 ypos 552 xsize 1280 ysize 122
        padding (96, 10, 96, 0)
        background None
        foreground None
        text what:
            id "what"
            font "fonts/Pretendard-Regular.otf"
            size 25
            color "#3B0B22"
            outlines []
            xmaximum 1060
            line_spacing 8
            language "korean-with-spaces"
            substitute use_substitution
    if who:
        frame:
            at (silk_tag_in if silk_motion_on() else silk_still)
            xpos 84 ypos 484 ysize 56
            padding (30, 0, 35, 6)
            background silk("tag", silk_tag_color(who))
            hbox:
                spacing 10 yalign 0.5
                text who:
                    id "who"
                    font silk_title_font(who)
                    size 27
                    color "#FFFDFB"
                    outlines []
                    yalign 0.5
                if silk_english(who):
                    text silk_english(who) font "fonts/PlayfairDisplay-Italic.ttf" size 16 color "#FFFDFB" outlines [] yalign 0.7
    if advance:
        add silk("next", "#3B0B22", size=(14, 9)) xpos 1170 ypos 652 at (silk_next_bob if silk_motion_on() else silk_still)

screen say(who, what):
    use cream_dialogue_panel(who, what)

screen silk_choice_item(item, i=0):
    $ choice_text, choice_chip = silk_choice_parts(item.caption)
    button:
        at ((silk_choice_in(i), silk_choice_hover) if silk_motion_on() else (silk_still,))
        style "silk_choice_button"
        action item.action
        alt item.caption
        hbox:
            spacing 12
            text choice_text style "silk_choice_text" language "korean-with-spaces" xmaximum (366 if choice_chip else 530) min_width (366 if choice_chip else 0)
            if choice_chip:
                frame:
                    at (silk_chip_glow if silk_motion_on() else silk_still)
                    yalign 0.5
                    padding (13, 5)
                    background silk("flat", "#B3123F", 14)
                    text choice_chip font "fonts/Pretendard-Regular.otf" size 12 color "#FFFDFB" outlines []

screen office_choice_list(items):
    vbox:
        xsize 612 spacing 9
        for i, item in enumerate(items):
            use silk_choice_item(item, i)

screen choice(items):
    zorder 30
    if len(items) <= 3:
        if _history_list:
            use cream_dialogue_panel(_history_list[-1].who, _history_list[-1].what, False, False)
        if office_ui_long_choices(items):
            viewport:
                xalign 0.5 ypos 122 xsize 624 ysize 334
                mousewheel True draggable True arrowkeys True
                scrollbars "vertical"
                vscrollbar_xsize 6 vscrollbar_base_bar Solid("#E1D7CF") vscrollbar_thumb Solid("#B3123F") vscrollbar_unscrollable "hide"
                use office_choice_list(items)
        else:
            vbox:
                xalign 0.5 yanchor 1.0 ypos (446 if silk_has_intimate(items) else 470) xsize 624 spacing 9
                for i, item in enumerate(items):
                    use silk_choice_item(item, i)
        if silk_has_intimate(items):
            frame:
                xalign 0.5 ypos 452
                padding (14, 4)
                background silk("flat", "#FFFDFB", 12)
                text "친밀한 장면을 미루는 선택에는 정답이 없어요." size 13 color "#4A2A36"
    else:
        frame:
            xpos 66 ypos 122 xsize 1148 ysize 350 padding (24, 22, 28, 27)
            background silk_surface("panel")
            viewport:
                mousewheel True draggable True arrowkeys True
                scrollbars "vertical"
                vscrollbar_xsize 6 vscrollbar_base_bar Solid("#E1D7CF") vscrollbar_thumb Solid("#B3123F") vscrollbar_unscrollable "hide"
                vbox:
                    xsize 1070 spacing 9
                    for i, item in enumerate(items):
                        use silk_choice_item(item, i)

screen main_menu():
    tag menu
    add "silk ground"
    add silk("band", size=(1280, 584))
    vbox:
        at silk_tilt
        xpos 84 ypos 150
        spacing -6
        text "After Work, With You" font "fonts/PlayfairDisplay-Italic.ttf" size 30 color "#B3123F" xpos 8
        text "퇴근 후{color=#F2C14E},{/color} 우리":
            font "fonts/Jua-Regular.ttf"
            size 150
            kerning -3
            color "#FFFDFB"
            outlines [(4, "#B3123F", 11, 12), (4, "#3B0B22", 0, 0)]
    # 개발 중 확인용 진입점. 기존 이름과 동작을 그대로 둔다.
    vbox:
        xanchor 1.0 xpos 1248 ypos 24 spacing 5
        text "개발 확인용" size 12 color "#6E4553" xalign 1.0
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
    add silk("dialogue", size=(1280, 176)) xpos 0 ypos 544
    hbox:
        xpos 64 ypos 594 spacing 8
        button:
            at ((silk_menu_in(0), silk_menu_hover) if silk_motion_on() else (silk_still,))
            style "silk_menu_button"
            action [SetVariable("cream_preview_active", False), SetVariable("cream_preview_mode", None), Start()]
            alt "처음부터 읽기"
            id "start_button"
            default_focus True
            vbox:
                xalign 0.5 yalign 0.5 spacing 0
                text "처음부터 읽기" style "silk_menu_text"
                text "New game" style "silk_menu_caption"
        button:
            at ((silk_menu_in(1), silk_menu_hover) if silk_motion_on() else (silk_still,))
            style "silk_menu_button"
            action ShowMenu("load")
            alt "이어 읽기"
            vbox:
                xalign 0.5 yalign 0.5 spacing 0
                text "이어 읽기" style "silk_menu_text"
                text "Continue" style "silk_menu_caption"
        button:
            at ((silk_menu_in(2), silk_menu_hover) if silk_motion_on() else (silk_still,))
            style "silk_menu_button"
            action ShowMenu("progression_hub")
            alt "우리의 기록"
            vbox:
                xalign 0.5 yalign 0.5 spacing 0
                text "우리의 기록" style "silk_menu_text"
                text "Album" style "silk_menu_caption"
        button:
            at ((silk_menu_in(3), silk_menu_hover) if silk_motion_on() else (silk_still,))
            style "silk_menu_button"
            action ShowMenu("preferences")
            alt "설정"
            vbox:
                xalign 0.5 yalign 0.5 spacing 0
                text "설정" style "silk_menu_text"
                text "Config" style "silk_menu_caption"
        if not renpy.variant("web"):
            button:
                at ((silk_menu_in(4), silk_menu_hover) if silk_motion_on() else (silk_still,))
                style "silk_menu_button"
                action Quit(confirm=False)
                alt "종료"
                vbox:
                    xalign 0.5 yalign 0.5 spacing 0
                    text "종료" style "silk_menu_text"
                    text "Exit" style "silk_menu_caption"
    text ("ver " + config.version) xpos 64 ypos 688 size 12 color "#6E4553"
    text "네 히로인 전체 대본 · 아트 준비 중" xanchor 1.0 xpos 1216 ypos 688 size 12 color "#6E4553"

screen silk_quick_item(label, icon, target):
    button:
        at (silk_quick_hover if silk_motion_on() else silk_still)
        style "silk_quick_button"
        action target
        alt label
        hbox:
            spacing 6
            add silk("icon", icon, "#6E4553", size=(17, 17)) yalign 0.5
            text label style "silk_quick_text"

screen quick_menu():
    zorder 100
    if not main_menu and not cream_menu_open() and not renpy.get_screen("office_phone") and not renpy.get_screen("office_phone_archive"):
        if not event_cut_active:
            hbox:
                xanchor 1.0 xpos 1196 ypos 676 spacing 0
                use silk_quick_item("되돌리기", "rollback", Rollback())
                use silk_quick_item("기록", "history", ShowMenu("history"))
                use silk_quick_item("메신저", "phone", Show("office_phone_archive"))
                use silk_quick_item("자동", "auto", Preference("auto-forward", "toggle"))
                use silk_quick_item("스킵", "skip", Skip())
                use silk_quick_item("저장", "save", ShowMenu("save"))
                use silk_quick_item("불러오기", "load", ShowMenu("load"))
                use silk_quick_item("설정", "prefs", ShowMenu("preferences"))
                use silk_quick_item("메뉴", "menu", MainMenu(confirm=True))
            text "클릭·Enter 다음 / 휠 위로 되돌리기" xpos 96 ypos 692 size 12 color "#6E4553"
        else:
            frame:
                xpos 750 ypos 18
                padding (12, 4, 16, 9)
                background silk_surface("button")
                hbox:
                    spacing 0
                    use silk_quick_item("되돌리기", "rollback", Rollback())
                    use silk_quick_item("기록", "history", ShowMenu("history"))
                    use silk_quick_item("저장", "save", ShowMenu("save"))
                    use silk_quick_item("불러오기", "load", ShowMenu("load"))
                    use silk_quick_item("설정", "prefs", ShowMenu("preferences"))

screen cream_preview_controls():
    hbox:
        xpos 32 ypos 112 spacing 6
        textbutton "낮" id "preview_day" action Jump("cream_preview_day") style "silk_small_button"
        textbutton "밤" id "preview_night" action Jump("cream_preview_night") style "silk_small_button"
        textbutton "선택지" id "preview_choices" action Jump("cream_preview_choices") style "silk_small_button"
        textbutton "처음" id "preview_exit" action MainMenu(confirm=False) style "silk_small_button"

init python:
    config.overlay_screens.append("cream_stage")
    config.overlay_screens.append("story_header")
    config.overlay_screens.append("quick_menu")

screen silk_menu_title(title, caption):
    hbox:
        spacing 12
        text title font "fonts/Jua-Regular.ttf" size 40 color "#3B0B22" yalign 1.0
        text caption font "fonts/PlayfairDisplay-Italic.ttf" size 20 color "#B3123F" yalign 0.8

screen preferences():
    tag menu
    add "silk ground"
    frame:
        xalign 0.5 yalign 0.5 xsize 724 ysize 677 padding (42, 35, 46, 40)
        background silk_surface("panel")
        viewport:
            xsize 636 ysize 602
            mousewheel True draggable True
            scrollbars "vertical"
            vscrollbar_xsize 6 vscrollbar_base_bar Solid("#E1D7CF") vscrollbar_thumb Solid("#B3123F") vscrollbar_unscrollable "hide"
            vbox:
                spacing 16
                use silk_menu_title("설정", "Config")
                text "글자 표시 속도" size 23
                textbutton "창모드" action Preference("display", "window") text_size 20
                textbutton "전체화면" action Preference("display", "fullscreen") text_size 20
                textbutton "읽은 대사만 스킵" action Preference("skip", "seen") text_size 20
                bar value Preference("text speed") xsize 600 ysize 14 left_bar Solid("#B3123F") right_bar Solid("#E1D7CF")
                textbutton "글자 즉시 표시" action Preference("text speed", 0)
                text "자동 진행 대기 시간" size 21
                bar value Preference("auto-forward time") xsize 600 ysize 14 left_bar Solid("#B3123F") right_bar Solid("#E1D7CF")
                if config.has_music:
                    text "음악" size 20
                    bar value Preference("music volume") xsize 600 ysize 14 left_bar Solid("#B3123F") right_bar Solid("#E1D7CF")
                if config.has_sound:
                    text "효과음" size 20
                    bar value Preference("sound volume") xsize 600 ysize 14 left_bar Solid("#B3123F") right_bar Solid("#E1D7CF")
                if config.has_voice:
                    text "음성" size 20
                    bar value Preference("voice volume") xsize 600 ysize 14 left_bar Solid("#B3123F") right_bar Solid("#E1D7CF")
                textbutton ("화면 움직임 효과: 켜짐" if silk_motion_on() else "화면 움직임 효과: 꺼짐") action ToggleField(persistent, "silk_motion", True, False) text_size 21
                textbutton ("메신저 입력 중 연출: 켜짐" if persistent.phone_typing_enabled else "메신저 입력 중 연출: 꺼짐") action ToggleField(persistent, "phone_typing_enabled") text_size 21
                text "호감도는 함께 겪은 관계의 진전을 보여 줍니다.\n취향에 정답은 없고, 선택에 따라 반응과 기억이 달라집니다." size 17 color "#6E4553" line_spacing 4 xmaximum 600
                textbutton "돌아가기" action Return()
                if not main_menu:
                    textbutton "처음 화면" action MainMenu(confirm=True)

screen file_slots(mode):
    add "silk ground"
    frame:
        xalign 0.5 yalign 0.5 xsize 994 padding (35, 28, 39, 33)
        background silk_surface("panel")
        vbox:
            spacing 15
            use silk_menu_title(("저장" if mode == "save" else "불러오기"), ("Save" if mode == "save" else "Load"))
            text "대사와 선택·기억을 함께 저장합니다." size 20 color "#6E4553"
            for slot in range(1, 5):
                $ slot_name = str(slot)
                textbutton ("슬롯 " + slot_name + "  ·  " + FileTime(slot_name, format="%m월 %d일 %H:%M", empty="비어 있음")):
                    xsize 920
                    action (FileSave(slot_name, confirm=True) if mode == "save" else FileLoad(slot_name, confirm=True))
            textbutton "돌아가기" action Return()

screen save():
    tag menu
    use file_slots("save")
screen load():
    tag menu
    use file_slots("load")

screen history():
    tag menu
    add "silk ground"
    frame:
        xpos 48 ypos 26 xsize 1188 ysize 670 padding (30, 22, 34, 27)
        background silk_surface("panel")
        vbox:
            spacing 15
            use silk_menu_title("대화 기록", "Log")
            viewport:
                id "history_viewport"
                xsize 1124 ysize 490
                mousewheel True draggable True
                scrollbars "vertical"
                vscrollbar_xsize 12
                vscrollbar_base_bar Solid("#E1D7CF")
                vscrollbar_thumb Solid("#B3123F")
                yinitial 1.0
                vbox:
                    xsize 1070 spacing 14
                    for entry in _history_list:
                        if entry.who:
                            text entry.who size 19 color cream_speaker_color(entry.who, history=True)
                        text entry.what size 24 substitute False language "korean-with-spaces"
            textbutton "돌아가기" action Return()

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#1B0F1499")
    frame:
        xalign 0.5 yalign 0.5 xsize 804 padding (35, 30, 39, 35)
        background silk_surface("panel")
        vbox:
            spacing 24
            text message size 26
            hbox:
                spacing 25
                textbutton "예" action yes_action
                textbutton "아니요" action no_action

translate None strings:
    old "Are you sure?"
    new "계속할까요?"
    old "Are you sure you want to overwrite your save?"
    new "이 저장 슬롯을 덮어쓸까요?"
    old "Loading will lose unsaved progress.\nAre you sure you want to do this?"
    new "저장하지 않은 진행은 사라집니다. 불러올까요?"
    old "Are you sure you want to return to the main menu?\nThis will lose unsaved progress."
    new "저장하지 않은 진행을 마치고 처음 화면으로 돌아갈까요?"
