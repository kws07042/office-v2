style default:
    font "fonts/Pretendard-Regular.otf"
    size 26
    color "#342932"
style button:
    padding (22, 12)
    background cream_round("button")
    hover_background cream_round("hover")
    insensitive_background cream_round("soft")
style button_text:
    color "#493741"
    hover_color "#864940"
    insensitive_color "#8a7679"
style choice_button is button:
    padding (22, 12)
    xfill True
    yminimum 52
style choice_button_text is button_text:
    size 20
    xalign 0.5
    text_align 0.5
style cream_quick_button is button:
    background None
    hover_background None
    padding (9, 5)
style cream_quick_button_text is button_text:
    size 15
    color "#fff7ed"
    hover_color "#f1b8a8"
    outlines [(1, "#2b222e", 0, 0)]
style event_text is default:
    color "#fff5ef"
style event_button is button:
    background Solid("#3e3141")
    hover_background Solid("#62454e")
style event_button_text is button_text:
    color "#fff5ef"
    hover_color "#ffddc9"

screen cream_stage():
    zorder -100
    if not main_menu and not event_cut_active:
        add ("gui/cream/stage_" + cream_stage_mode() + ".svg") xysize (1280, 720)
        $ portrait_align = 0.92 if renpy.get_screen("choice") else 0.82
        if cream_ria_visible():
            add "ria ui bust" xalign portrait_align ypos 28
        elif cream_yujin_visible():
            add "yujin ui bust" xalign portrait_align ypos 50

screen cream_heart(fraction):
    fixed:
        xsize 22 ysize 22
        add "gui/cream/heart_empty.svg" xysize (22, 22)
        if fraction > 0:
            add Crop((0, 0, max(1, int(22 * min(1.0, fraction))), 22), Transform("gui/cream/heart_full.svg", xysize=(22, 22)))

screen story_header():
    zorder 10
    if not main_menu and not event_cut_active and not cream_menu_open() and not renpy.get_screen("office_phone") and not renpy.get_screen("office_phone_archive"):
        frame:
            xpos 62 ypos 31 padding (12, 8)
            background Solid("#261e2bbf")
            vbox:
                spacing 4
                text chapter size 16 color "#f4bfb0" xmaximum 380
                text location size 14 color "#fff7ed" xmaximum 380
        $ focus = active_route if active_route in affinity else (cream_focus if cream_focus in affinity else "ria")
        $ person_name = {"ria":"강리아", "jihyun":"백지현", "yujin":"차유진", "seoyun":"한서윤"}[focus]
        frame:
            xalign 0.948 ypos 31 padding (12, 8)
            background Solid("#261e2bbf")
            vbox:
                spacing 5
                hbox:
                    spacing 10
                    text person_name size 16 color cream_speaker_color(person_name)
                    text cream_relation_name(focus) size 14 color "#f4bfb0"
                hbox:
                    spacing 4
                    for index in range(5):
                        use cream_heart((affinity[focus] - index * 20) / 20.0)
                    text (str(affinity[focus]) + " / 100") size 13 color "#fff7ed" yalign 0.5
        if cream_preview_active:
            use cream_preview_controls

screen cream_dialogue_panel(who, what, use_substitution=True, advance=True):
    add "gui/window/dialogue_scrim.png" xysize (1280, 720)
    window:
        id "window"
        xpos 116 ypos 562 xsize 1048 ysize 112
        padding (0, 0)
        background None
        foreground None
        text what:
            id "what"
            font "fonts/Pretendard-Regular.otf"
            size 26
            color "#fff7ed"
            outlines [(2, "#2b222e", 0, 0), (1, "#1a142966", 0, 2)]
            xmaximum 1005
            line_spacing 6
            substitute use_substitution
    if who:
        text who:
            id "who"
            xpos 116 ypos 526
            font "fonts/Pretendard-Regular.otf"
            size 21
            color cream_speaker_color(who)
            outlines [(1, "#25202b", 0, 0)]
    if advance:
        text "▾" xpos 1150 ypos 641 size 23 color "#fff7ed" outlines [(2, "#2b222e", 0, 0)]

screen say(who, what):
    use cream_dialogue_panel(who, what)

screen office_choice_list(items, width):
    vbox:
        xsize width spacing 9
        for item in items:
            textbutton item.caption action item.action style "office_choice_button"

screen choice(items):
    zorder 30
    add Solid("#211b2935")
    if _history_list:
        use cream_dialogue_panel(_history_list[-1].who, _history_list[-1].what, False, False)
    if len(items) > 3 or office_ui_long_choices(items):
        viewport:
            id "window_choices"
            xalign 0.5 ypos 138 xsize 620 ysize 362
            mousewheel True draggable True arrowkeys True
            use office_choice_list(items, 620)
        vbar value YScrollValue("window_choices") style "office_scrollbar" xpos 961 ypos 138 ysize 362
    else:
        vbox:
            xalign 0.5 yanchor 1.0 ypos 468 xsize 620 spacing 9
            for item in items:
                textbutton item.caption action item.action style "office_choice_button"

screen main_menu():
    tag menu
    default show_preview_links = False
    add "gui/window/title.webp" xysize (1280, 720)
    add "gui/window/title_wash.svg" xysize (1280, 720)
    add "gui/window/wordmark.svg" xpos 69 ypos 168 xysize (245, 150)
    vbox:
        xpos 68 ypos 362
        spacing 2
        textbutton "새 이야기" action [SetVariable("cream_preview_active", False), SetVariable("cream_preview_mode", None), Start()] id "start_button" style "window_title_button" text_color "#864940"
        textbutton "이어 읽기" action ShowMenu("load") style "window_title_button"
        textbutton "우리의 기록" action ShowMenu("progression_hub") style "window_title_button"
        textbutton "설정" action ShowMenu("preferences") style "window_title_button"
        if not renpy.variant("web"):
            textbutton "종료" action Quit(confirm=False) style "window_title_button"
    textbutton "테스트 장면":
        xpos 68 ypos 657
        text_size 15
        action ToggleScreenVariable("show_preview_links")
    if show_preview_links:
        frame:
            xpos 205 ypos 640 xsize 1000 ysize 64 padding (12, 8)
            background cream_round("panel")
            hbox:
                spacing 4
                textbutton "화면 배치" action Start("cream_preview_start") id "cream_preview_button" text_size 15 padding (12, 9)
                textbutton "유진 루트" action Start("yujin_early_preview") id "yujin_preview_button" text_size 15 padding (12, 9)
                textbutton "리아 R02" action Start("ria_r02_preview") id "ria_r02_preview_button" text_size 15 padding (12, 9)
                textbutton "리아 R08" action Start("office_phone_preview") id "phone_preview_button" text_size 15 padding (12, 9)
                textbutton "지현 루트" action Start("jihyun_early_preview") id "jihyun_preview_button" text_size 15 padding (12, 9)
                textbutton "서윤 루트" action Start("seoyun_preview") id "seoyun_preview_button" text_size 15 padding (12, 9)

screen quick_menu():
    zorder 100
    if not main_menu and not cream_menu_open() and not renpy.get_screen("office_phone") and not renpy.get_screen("office_phone_archive"):
        frame:
            xpos (555 if not event_cut_active else 750) ypos (678 if not event_cut_active else 18)
            padding (7, 2)
            background (None if not event_cut_active else Solid("#261e2bdf"))
            hbox:
                spacing 3
                textbutton "되돌리기" action Rollback() style "cream_quick_button"
                textbutton "기록" action ShowMenu("history") style "cream_quick_button"
                if not event_cut_active:
                    textbutton "메신저" action Show("office_phone_archive") style "cream_quick_button"
                if not event_cut_active:
                    textbutton "자동" action Preference("auto-forward", "toggle") style "cream_quick_button"
                    textbutton "스킵" action Skip() style "cream_quick_button"
                textbutton "저장" action ShowMenu("save") style "cream_quick_button"
                textbutton "불러오기" action ShowMenu("load") style "cream_quick_button"
                textbutton "설정" action ShowMenu("preferences") style "cream_quick_button"
                if not event_cut_active:
                    textbutton "메뉴" action MainMenu(confirm=True) style "cream_quick_button"
        if not event_cut_active:
            text "클릭·Enter 다음 / 휠 위로 되돌리기" xpos 116 ypos 691 size 12 color "#fff7ed" outlines [(1, "#2b222e", 0, 0)]

screen cream_preview_controls():
    frame:
        xpos 62 ypos 108 padding (9, 8)
        background cream_round("panel")
        hbox:
            spacing 7
            textbutton "낮" id "preview_day" action Jump("cream_preview_day") text_size 15 xsize 65 padding (12, 7)
            textbutton "밤" id "preview_night" action Jump("cream_preview_night") text_size 15 xsize 65 padding (12, 7)
            textbutton "선택지" id "preview_choices" action Jump("cream_preview_choices") text_size 15 xsize 90 padding (12, 7)
            textbutton "처음" id "preview_exit" action MainMenu(confirm=False) text_size 15 xsize 80 padding (12, 7)

init python:
    config.overlay_screens.append("cream_stage")
    config.overlay_screens.append("story_header")
    config.overlay_screens.append("quick_menu")

screen preferences():
    tag menu
    add "gui/window/title.webp" xpos 34 xysize (1280, 720)
    add Solid("#1719223d")
    add Solid("#20212a") xysize (612, 720)
    add Solid("#82717a") xpos 611 xysize (1, 720)

    text "설정" xpos 76 ypos 78 size 48 color "#f4eee9"
    add Solid("#47434d") xpos 76 ypos 158 xysize (500, 1)

    viewport:
        id "window_preferences"
        xpos 76 ypos 183 xsize 504 ysize 414
        mousewheel True draggable True arrowkeys True
        vbox:
            xsize 500 spacing 22
            vbox:
                spacing 8
                text "화면" style "window_setting_section"
                fixed:
                    xysize (500, 40)
                    text "표시 방식" style "window_setting_label" yalign 0.5
                    hbox:
                        xalign 1.0 yalign 0.5 spacing 6
                        textbutton "창 모드" action Preference("display", "window") style "window_setting_button" id "settings_window"
                        textbutton "전체 화면" action Preference("display", "fullscreen") style "window_setting_button" id "settings_fullscreen"
            vbox:
                spacing 8
                text "대사" style "window_setting_section"
                use window_setting_slider("글자 표시 속도", Preference("text speed"))
                use window_setting_slider("자동 진행 간격", Preference("auto-forward time"))
                fixed:
                    xysize (500, 40)
                    text "글자 표시" style "window_setting_label" yalign 0.5
                    textbutton "즉시 표시" action Preference("text speed", 0) style "window_setting_button" xalign 1.0 yalign 0.5 id "settings_instant"
                fixed:
                    xysize (500, 40)
                    text "스킵 범위" style "window_setting_label" yalign 0.5
                    textbutton "읽은 대사만" action Preference("skip", "seen") style "window_setting_button" xalign 1.0 yalign 0.5 id "settings_skip_seen"
            vbox:
                spacing 8
                text "메신저" style "window_setting_section"
                fixed:
                    xysize (500, 40)
                    text "입력 중 표시" style "window_setting_label" yalign 0.5
                    hbox:
                        xalign 1.0 yalign 0.5 spacing 6
                        textbutton "켜기" action SetField(persistent, "phone_typing_enabled", True) style "window_setting_button" id "settings_typing_on"
                        textbutton "끄기" action SetField(persistent, "phone_typing_enabled", False) style "window_setting_button" id "settings_typing_off"
            if config.has_music or config.has_sound or config.has_voice:
                vbox:
                    spacing 8
                    text "소리" style "window_setting_section"
                    if config.has_music:
                        use window_setting_slider("음악", Preference("music volume"))
                    if config.has_sound:
                        use window_setting_slider("효과음", Preference("sound volume"))
                    if config.has_voice:
                        use window_setting_slider("음성", Preference("voice volume"))
    vbar value YScrollValue("window_preferences") style "window_settings_scroll" xpos 589 ypos 183 ysize 414

    add Solid("#47434d") xpos 76 ypos 611 xysize (500, 1)
    hbox:
        xpos 76 ypos 631 spacing 14
        textbutton "‹  돌아가기" action Return() style "window_setting_nav" id "settings_back"
        if not main_menu:
            textbutton "처음 화면" action MainMenu(confirm=True) style "window_setting_nav"

screen window_setting_slider(label, setting):
    fixed:
        xysize (500, 34)
        text label style "window_setting_label" yalign 0.5
        bar value setting style "window_setting_bar" xalign 1.0 yalign 0.5

screen file_slots(mode):
    use window_menu_backdrop
    frame:
        xalign 0.5 yalign 0.5 xsize 990 padding (35, 28)
        style "window_record_panel"
        vbox:
            spacing 15
            text ("저장" if mode == "save" else "불러오기") size 36 color "#403640"
            add Solid("#d6cbc8") xysize (920, 1)
            for slot in range(1, 5):
                $ slot_name = str(slot)
                textbutton ("슬롯 " + slot_name + "  ·  " + FileTime(slot_name, format="%m월 %d일 %H:%M", empty="비어 있음")):
                    xsize 920
                    style "window_record_button"
                    id ("window_slot_" + slot_name)
                    action (FileSave(slot_name, confirm=True) if mode == "save" else FileLoad(slot_name, confirm=True))
            textbutton "돌아가기" action Return() style "window_record_button"

screen save():
    tag menu
    use file_slots("save")
screen load():
    tag menu
    use file_slots("load")

screen history():
    tag menu
    use window_menu_backdrop
    frame:
        xpos 48 ypos 26 xsize 1184 ysize 665 padding (30, 22)
        style "window_record_panel"
        vbox:
            spacing 15
            text "대화 기록" size 33 color "#403640"
            fixed:
                xsize 1124 ysize 500
                viewport:
                    id "history_viewport"
                    xsize 1100 ysize 500
                    mousewheel True draggable True arrowkeys True
                    yinitial 1.0
                    vbox:
                        xsize 1070 spacing 14
                        for entry in _history_list:
                            if entry.who:
                                text entry.who size 19 color cream_speaker_color(entry.who, history=True)
                            text entry.what size 24 substitute False
                vbar value YScrollValue("history_viewport") style "office_scrollbar" xpos 1111 ysize 500
            textbutton "돌아가기" action Return()

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#241b28aa")
    frame:
        xalign 0.5 yalign 0.5 xsize 800 padding (35, 30)
        style "window_record_panel"
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
