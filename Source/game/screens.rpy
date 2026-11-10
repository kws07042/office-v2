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
        if renpy.get_attributes("bg") in (None, ("plain",)):
            add ("gui/cream/stage_" + cream_stage_mode() + ".svg") xysize (1280, 720)
        if cream_ria_visible():
            add "ria ui bust" xalign 0.5 ypos 28
        elif cream_yujin_visible():
            add "yujin ui bust" xalign 0.5 ypos 50

screen cream_heart(fraction):
    fixed:
        xsize 22 ysize 22
        add "gui/cream/heart_empty.svg" xysize (22, 22)
        if fraction > 0:
            add Crop((0, 0, max(1, int(22 * min(1.0, fraction))), 22), Transform("gui/cream/heart_full.svg", xysize=(22, 22)))

screen story_header():
    zorder 10
    if not main_menu and not event_cut_active and not cream_menu_open() and not renpy.get_screen("office_phone") and not renpy.get_screen("office_phone_archive"):
        add Solid("#18171de8") xysize (1280, 48)
        hbox:
            xpos 65 ypos 13 spacing 10
            text location size 17 color "#eee5e1" xmaximum 320
            if chapter:
                text "·" size 17 color "#aaa1ab"
                text chapter size 17 color "#c9c0c5" xmaximum 310
        $ focus = active_route if active_route in affinity else (cream_focus if cream_focus in affinity else "ria")
        $ person_name = phone_names(focus)
        hbox:
            xalign 0.95 ypos 12 spacing 8
            text person_name size 16 color cream_speaker_color(person_name) yalign 0.5
            text cream_relation_name(focus) size 14 color "#d8ced3" yalign 0.5
            for index in range(5):
                use cream_heart((affinity[focus] - index * 20) / 20.0)
            text (str(affinity[focus]) + " / 100") size 13 color "#eee5e1" yalign 0.5
        if cream_preview_active:
            use cream_preview_controls

screen cream_dialogue_panel(who, what, use_substitution=True, advance=True):
    add "gui/window/dialogue_scrim.png" xysize (1280, 720)
    window:
        id "window"
        xalign 0.5 yanchor 1.0 ypos 651
        xsize 1020 yminimum 71
        padding (0, 0)
        background None
        foreground None
        vbox:
            xalign 0.5 spacing 7
            if who:
                text who:
                    id "who"
                    xalign 0.5
                    size 21
                    color cream_speaker_color(who)
                    outlines [(1, "#24212a", 0, 0)]
            text what:
                id "what"
                xalign 0.5
                text_align 0.5
                font "fonts/Pretendard-Regular.otf"
                size 27
                color "#fff5ed"
                outlines [(1, "#211e25", 0, 0), (1, "#18171db0", 0, 2)]
                xmaximum 980
                line_spacing 5
                substitute use_substitution
    if advance:
        text "›" xpos 1152 ypos 613 size 23 color "#e3d9d4"

screen say(who, what):
    use cream_dialogue_panel(who, what)

screen office_choice_list(items, width):
    vbox:
        xsize width spacing 9
        for item in items:
            textbutton item.caption action item.action style "office_choice_button"

screen choice(items):
    zorder 30
    add Solid("#18171d40")
    if _history_list:
        use cream_dialogue_panel(_history_list[-1].who, _history_list[-1].what, False, False)
    if len(items) > 3 or office_ui_long_choices(items):
        viewport:
            id "window_choices"
            xalign 0.5 ypos 194 xsize 570 ysize 325
            mousewheel True draggable True arrowkeys True
            use office_choice_list(items, 570)
        vbar value YScrollValue("window_choices") style "office_scrollbar" xpos 938 ypos 194 ysize 325
    else:
        vbox:
            xalign 0.5 yanchor 1.0 ypos 510 xsize 570 spacing 8
            for item in items:
                textbutton item.caption action item.action style "office_choice_button"

screen main_menu():
    tag menu
    default show_preview_links = False
    add window_title_art xysize (1280, 720)
    add "gui/window/film_title_scrim.png" xysize (1280, 720)
    add window_title_wordmark xpos 71 yanchor 1.0 ypos 613 xysize (293, 158) fit "contain"
    vbox:
        xalign 0.95 yanchor 1.0 ypos 618
        spacing 2
        textbutton "새 이야기" action [SetVariable("cream_preview_active", False), SetVariable("cream_preview_mode", None), Start()] id "start_button" style "window_title_button" text_color "#f0d6b6"
        textbutton "이어 읽기" action ShowMenu("load") style "window_title_button"
        textbutton "우리의 기록" action ShowMenu("progression_hub") style "window_title_button"
        textbutton "설정" action ShowMenu("preferences") style "window_title_button"
        if not renpy.variant("web"):
            textbutton "종료" action Quit(confirm=False) style "window_title_button"
    textbutton "테스트 장면":
        xpos 68 ypos 657
        style "window_setting_nav" text_size 15
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
            xalign (0.5 if not event_cut_active else 0.96) ypos (675 if not event_cut_active else 18)
            padding (7, 2)
            background (None if not event_cut_active else Solid("#1d1b23df"))
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

screen cream_preview_controls():
    frame:
        xpos 62 ypos 63 padding (9, 8)
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
    default section = "reading"
    add window_title_art xysize (1280, 720)
    add Solid("#18171d55")
    add "gui/window/film_title_scrim.png" xysize (1280, 720)
    add Solid("#1e1c23") ypos 517 xysize (1280, 203)
    add Solid("#625d67") ypos 517 xysize (1280, 1)

    text "설정" xpos 72 ypos 72 size 44 color "#fff5ed" outlines [(2, "#18171d", 0, 0)]
    vbox:
        xpos 67 ypos 141 spacing 5
        textbutton "화면·대사" action SetScreenVariable("section", "reading") style "window_setting_button" selected section == "reading" id "settings_reading"
        textbutton "메신저" action SetScreenVariable("section", "messenger") style "window_setting_button" selected section == "messenger" id "settings_messenger"
        if config.has_music or config.has_sound or config.has_voice:
            textbutton "소리" action SetScreenVariable("section", "sound") style "window_setting_button" selected section == "sound" id "settings_audio"

    hbox:
        xpos 64 ypos 474 spacing 14
        textbutton "‹  돌아가기" action Return() style "window_setting_nav" id "settings_back"
        if not main_menu:
            textbutton "처음 화면" action MainMenu(confirm=True) style "window_setting_nav"

    text ({"reading":"화면·대사", "messenger":"메신저", "sound":"소리"}[section]) xpos 72 ypos 545 style "window_setting_section"
    hbox:
        xpos 72 ypos 584 spacing 24
        if section == "reading":
            vbox:
                xsize 235 spacing 11
                text "표시 방식" style "window_setting_label"
                hbox:
                    spacing 6
                    textbutton "창 모드" action Preference("display", "window") style "window_setting_button" id "settings_window"
                    textbutton "전체 화면" action Preference("display", "fullscreen") style "window_setting_button" id "settings_fullscreen"
            use window_setting_divider
            vbox:
                xsize 245 spacing 7
                text "글자 표시 속도" style "window_setting_label"
                bar value Preference("text speed") style "window_setting_bar"
                textbutton "즉시 표시" action Preference("text speed", 0) style "window_setting_button" id "settings_instant"
            use window_setting_divider
            vbox:
                xsize 245 spacing 11
                text "자동 진행 간격" style "window_setting_label"
                bar value Preference("auto-forward time") style "window_setting_bar"
            use window_setting_divider
            vbox:
                spacing 11
                text "스킵 범위" style "window_setting_label"
                textbutton "읽은 대사만" action Preference("skip", "seen") style "window_setting_button" id "settings_skip_seen"
        elif section == "messenger":
            vbox:
                spacing 11
                text "입력 중 표시" style "window_setting_label"
                hbox:
                    spacing 6
                    textbutton "켜기" action SetField(persistent, "phone_typing_enabled", True) style "window_setting_button" id "settings_typing_on"
                    textbutton "끄기" action SetField(persistent, "phone_typing_enabled", False) style "window_setting_button" id "settings_typing_off"
        else:
            if config.has_music:
                use window_setting_slider("음악", Preference("music volume"))
            if config.has_sound:
                use window_setting_slider("효과음", Preference("sound volume"))
            if config.has_voice:
                use window_setting_slider("음성", Preference("voice volume"))

screen window_setting_divider():
    add Solid("#4d4852") xysize (1, 75)

screen window_setting_slider(label, setting):
    vbox:
        xsize 245 spacing 11
        text label style "window_setting_label"
        bar value setting style "window_setting_bar"

screen file_slots(mode):
    style_prefix "window_record"
    use window_menu_backdrop
    text ("저장" if mode == "save" else "불러오기") xpos 73 ypos 129 size 45 color "#f4eee9"
    textbutton "돌아가기" xpos 67 ypos 598 action Return()
    frame:
        xpos 735 ypos 132 xsize 470 padding (24, 20)
        style "window_record_panel"
        vbox:
            spacing 5
            for slot in range(1, 5):
                $ slot_name = str(slot)
                add Solid("#5b535e") xysize (422, 1)
                textbutton ("슬롯 " + slot_name + "  ·  " + FileTime(slot_name, format="%m월 %d일 %H:%M", empty="비어 있음")):
                    xsize 422
                    id ("window_slot_" + slot_name)
                    action (FileSave(slot_name, confirm=True) if mode == "save" else FileLoad(slot_name, confirm=True))

screen save():
    tag menu
    use file_slots("save")
screen load():
    tag menu
    use file_slots("load")

screen history():
    tag menu
    style_prefix "window_record"
    use window_menu_backdrop
    frame:
        xpos 48 ypos 26 xsize 1184 ysize 665 padding (30, 22)
        style "window_record_panel"
        vbox:
            spacing 15
            text "대화 기록" size 33 color "#f4eee9"
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
                                text entry.who size 19 color cream_speaker_color(entry.who)
                            text entry.what size 24 substitute False
                vbar value YScrollValue("history_viewport") style "window_record_scroll" xpos 1111 ysize 500
            textbutton "돌아가기" action Return()

screen confirm(message, yes_action, no_action):
    style_prefix "window_record"
    modal True
    zorder 200
    add Solid("#18171daa")
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
