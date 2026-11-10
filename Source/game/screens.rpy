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
    hover_background Solid("#503d43")
    selected_background Solid("#503d43")
    padding (9, 5)
style cream_quick_button_text is button_text:
    size 16
    color "#fff7ed"
    hover_color "#ead3bd"
    selected_color "#ead3bd"
    selected_hover_color "#fff3e8"
    outlines [(1, "#2b222e", 0, 0)]
style event_text is default:
    color "#fff5ef"
style event_button is button:
    background Solid("#49383e")
    hover_background Solid("#655059")
style event_button_text is button_text:
    color "#fff5ef"
    hover_color "#ffddc9"

screen cream_stage():
    zorder -100
    if not main_menu and not event_cut_active and not cream_menu_open():
        if renpy.get_attributes("bg") in (None, ("plain",)):
            add ("gui/cream/stage_" + cream_stage_mode() + ".svg") xysize (1280, 720)
        if cream_ria_visible():
            add "ria ui bust" xalign 0.5 yalign 1.0 xysize (600, 692) fit "contain"
        elif cream_yujin_visible():
            add "yujin ui bust" xalign 0.5 yalign 1.0 xysize (600, 692) fit "contain"

screen story_header():
    zorder 10
    if not main_menu and not event_cut_active and not cream_menu_open() and not renpy.get_screen("office_phone") and not renpy.get_screen("office_phone_archive"):
        frame:
            xpos 37 ypos 24 padding (13, 7)
            background Solid("#292326e6")
            text location size 16 color "#f2e8db" xmaximum 394
        $ focus = active_route if active_route in affinity else (cream_focus if cream_focus in affinity else "ria")
        $ person_name = phone_names(focus)
        frame:
            xalign 0.968 ypos 24 padding (13, 7)
            background Solid("#292326e6")
            hbox:
                spacing 8
                text person_name size 16 color cream_speaker_color(person_name) yalign 0.5
                text cream_relation_name(focus) size 15 color "#eadfda" yalign 0.5
                if persistent.progression_show_numbers:
                    text (str(affinity[focus]) + " / 100") size 14 color "#eadfda" yalign 0.5
        if cream_preview_active:
            use cream_preview_controls

screen cream_dialogue_panel(who, what, use_substitution=True, advance=True):
    window:
        id "window"
        xpos 106 yanchor 1.0 ypos 659
        xsize 1068 yminimum 115
        padding (27, 18)
        background Solid("#292326f6")
        foreground None
        hbox:
            spacing 18
            yalign 0.5
            if who:
                fixed:
                    xysize (124, 57)
                    text who:
                        id "who"
                        size 21
                        color cream_speaker_color(who)
                        yalign 0.5
                        xmaximum 119
                add Solid("#806c6c") xysize (1, 49) yalign 0.5
            text what:
                id "what"
                font "fonts/Pretendard-Regular.otf"
                size 27
                color "#fff5ed"
                xmaximum (790 if who else 970)
                yalign 0.5
                line_spacing 5
                substitute use_substitution
    if advance:
        text "›" xpos 1139 ypos 605 size 23 color "#e0c5ae"

screen say(who, what):
    use cream_dialogue_panel(who, what)

screen office_choice_list(items, width):
    vbox:
        xsize width spacing 9
        for item in items:
            textbutton item.caption action item.action style "office_choice_button"

screen choice(items):
    zorder 30
    add Solid("#2923264f")
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
    $ resume_slot = renpy.newest_slot(r"^(?:[0-9]+|quick|auto)-[0-9]+$")
    add Solid("#292326")
    add Crop((350, 0, 930, 720), Transform(window_title_art, xysize=(1280, 720))) xpos 350
    add "gui/badge/threshold.svg" xpos 330 xysize (21, 720)

    text "퇴근 후," xpos 58 ypos 87 size 62 font "fonts/GowunDodum-Regular.ttf" color "#f3e9dd"
    text "우리" xpos 89 ypos 150 size 92 font "fonts/GowunDodum-Regular.ttf" color "#f3e9dd"
    add Solid("#806e6b") xpos 60 ypos 278 xysize (228, 1)

    vbox:
        xpos 59 ypos 300 spacing 5
        textbutton "새 게임" action [SetVariable("cream_preview_active", False), SetVariable("cream_preview_mode", None), Start()] id "start_button" style "afterwork_title_button"
        textbutton "이어하기" action (FileLoad(resume_slot, slot=True) if resume_slot else NullAction()) sensitive resume_slot is not None id "badge_continue" style "afterwork_title_button"

    vbox:
        xpos 60 ypos 453 spacing 1
        textbutton "불러오기" action ShowMenu("load") id "badge_load" style "afterwork_title_link"
        textbutton "갤러리" action ShowMenu("progression_hub", initial_tab="gallery") id "badge_gallery" style "afterwork_title_link"
        textbutton "환경설정" action ShowMenu("preferences") style "afterwork_title_link"
        if not renpy.variant("web"):
            textbutton "종료" action Quit(confirm=True) style "afterwork_title_link"

    if config.developer:
        textbutton "테스트 장면" xpos 60 ypos 657 action ToggleScreenVariable("show_preview_links") style "afterwork_title_link" text_size 14
        if show_preview_links:
            frame:
                xpos 351 ypos 654 xsize 780 ysize 52 padding (10, 4)
                background Solid(badge_paper)
                hbox:
                    spacing 4
                    textbutton "화면 배치" action Start("cream_preview_start") id "cream_preview_button" style "badge_button" text_size 15
                    textbutton "유진 루트" action Start("yujin_early_preview") id "yujin_preview_button" style "badge_button" text_size 15
                    textbutton "리아 R02" action Start("ria_r02_preview") id "ria_r02_preview_button" style "badge_button" text_size 15
                    textbutton "리아 R08" action Start("office_phone_preview") id "phone_preview_button" style "badge_button" text_size 15
                    textbutton "지현 루트" action Start("jihyun_early_preview") id "jihyun_preview_button" style "badge_button" text_size 15
                    textbutton "서윤 루트" action Start("seoyun_preview") id "seoyun_preview_button" style "badge_button" text_size 15

screen quick_menu():
    zorder 100
    if not main_menu and not cream_menu_open() and not renpy.get_screen("office_phone") and not renpy.get_screen("office_phone_archive"):
        if not event_cut_active:
            add Solid("#292326") ypos 659 xysize (1280, 61)
        frame:
            xalign (0.5 if not event_cut_active else 0.96) ypos (673 if not event_cut_active else 18)
            padding (7, 2)
            background (None if not event_cut_active else Solid("#292326eb"))
            hbox:
                spacing 6
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
                    if not renpy.get_screen("choice"):
                        textbutton "UI 숨기기" id "badge_hide" action HideInterface() style "cream_quick_button"

screen cream_preview_controls():
    frame:
        xpos 37 ypos 71 padding (9, 8)
        background cream_round("panel")
        hbox:
            spacing 7
            textbutton "낮" id "preview_day" action Jump("cream_preview_day") text_size 15 xsize 65 padding (12, 7)
            textbutton "밤" id "preview_night" action Jump("cream_preview_night") text_size 15 xsize 65 padding (12, 7)
            textbutton "선택지" id "preview_choices" action Jump("cream_preview_choices") text_size 15 xsize 90 padding (12, 7)
            textbutton "처음" id "preview_exit" action MainMenu(confirm=False) text_size 15 xsize 80 padding (12, 7)

init python:
    config.always_shown_screens.append("cream_stage")
    config.overlay_screens.append("story_header")
    config.overlay_screens.append("quick_menu")

screen preferences():
    tag menu
    default section = "reading"
    use badge_shell("preferences", "설정")
    hbox:
        xpos 400 ypos 147 spacing 9
        textbutton "화면·대사" action SetScreenVariable("section", "reading") selected section == "reading" id "settings_reading" style "badge_tab_button"
        textbutton "메신저" action SetScreenVariable("section", "messenger") selected section == "messenger" id "settings_messenger" style "badge_tab_button"
        if config.has_music or config.has_sound or config.has_voice:
            textbutton "소리" action SetScreenVariable("section", "sound") selected section == "sound" id "settings_audio" style "badge_tab_button"
    add Solid(badge_rule) xpos 400 ypos 201 xysize (786, 1)
    vbox:
        xpos 400 ypos 218 spacing 4
        if section == "reading":
            use badge_setting_row("표시 방식"):
                textbutton "창 모드" action Preference("display", "window") id "settings_window" style "badge_segment_button"
                textbutton "전체 화면" action Preference("display", "fullscreen") id "settings_fullscreen" style "badge_segment_button"
            use badge_setting_row("글자 표시 속도"):
                bar value Preference("text speed") style "badge_slider"
            use badge_setting_row("자동 진행 간격"):
                bar value Preference("auto-forward time") style "badge_slider"
            use badge_setting_row("글자 표시"):
                textbutton "즉시 표시" action Preference("text speed", 0) id "settings_instant" style "badge_segment_button"
            use badge_setting_row("스킵 범위"):
                textbutton "읽은 대사만" action Preference("skip", "seen") id "settings_skip_seen" style "badge_segment_button"
                textbutton "읽지 않은 대사도" action Preference("skip", "all") style "badge_segment_button"
        elif section == "messenger":
            use badge_setting_row("입력 중 표시"):
                textbutton "켜기" action SetField(persistent, "phone_typing_enabled", True) id "settings_typing_on" style "badge_segment_button"
                textbutton "끄기" action SetField(persistent, "phone_typing_enabled", False) id "settings_typing_off" style "badge_segment_button"
        else:
            if config.has_music:
                use badge_setting_row("음악"):
                    bar value Preference("music volume") style "badge_slider"
            if config.has_sound:
                use badge_setting_row("효과음"):
                    bar value Preference("sound volume") style "badge_slider"
            if config.has_voice:
                use badge_setting_row("음성"):
                    bar value Preference("voice volume") style "badge_slider"
    if not main_menu:
        textbutton "처음 화면으로" xpos 390 ypos 638 action MainMenu(confirm=True) style "badge_button"

screen file_slots(mode):
    use badge_shell(mode, "저장" if mode == "save" else "불러오기")
    hbox:
        xpos 400 ypos 147 spacing 10
        if not main_menu:
            textbutton "저장" action ShowMenu("save") selected mode == "save" style "badge_tab_button"
        textbutton "불러오기" action ShowMenu("load") selected mode == "load" style "badge_tab_button"
    grid 2 2:
        xpos 400 ypos 216 spacing 20
        for slot in range(1, 5):
            $ slot_name = str(slot)
            button:
                id ("window_slot_" + slot_name)
                style "badge_button"
                xysize (373, 121)
                padding (15, 11)
                action (FileSave(slot_name, confirm=True) if mode == "save" else FileLoad(slot_name, confirm=True))
                fixed:
                    add Solid(badge_rule) xysize (343, 1)
                    text ("슬롯 " + slot_name) style "badge_text" size 25 ypos 17
                    text FileTime(slot_name, format="%m월 %d일 %H:%M", empty="비어 있음") size 17 color badge_muted ypos 60

screen save():
    tag menu
    use file_slots("save")

screen load():
    tag menu
    use file_slots("load")

screen history():
    tag menu
    use badge_shell("history", "대화 기록")
    add Solid(badge_rule) xpos 400 ypos 160 xysize (786, 1)
    if not _history_list:
        text "이야기를 진행하면 대화가 여기에 기록돼요." xpos 400 ypos 189 size 20 color badge_muted
    else:
        viewport:
            id "history_viewport"
            xpos 400 ypos 184 xsize 766 ysize 456
            mousewheel True draggable True arrowkeys True
            yinitial 1.0
            vbox:
                xsize 755 spacing 14
                for entry in _history_list:
                    hbox:
                        spacing 16
                        fixed:
                            xysize (126, 30)
                            if entry.who:
                                text entry.who size 18 color cream_speaker_color(entry.who, history=True) xmaximum 126
                        text entry.what size 22 color badge_ink xmaximum 605 line_spacing 4 substitute False
                    add Solid(badge_rule) xysize (755, 1)
        vbar value YScrollValue("history_viewport") style "badge_scroll" xpos 1182 ypos 184 ysize 456

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#2923269e")
    frame:
        xalign 0.5 yalign 0.53 xsize 610 padding (34, 27)
        background Solid(badge_paper)
        vbox:
            spacing 18
            text message size 27 color badge_ink xmaximum 542
            add Solid(badge_rule) xysize (542, 1)
            hbox:
                xalign 1.0 spacing 11
                textbutton "아니요" action no_action style "badge_button"
                textbutton "예" action yes_action style "badge_primary_button"

translate None strings:
    old "Are you sure?"
    new "계속할까요?"
    old "Are you sure you want to overwrite your save?"
    new "이 저장 슬롯을 덮어쓸까요?"
    old "Loading will lose unsaved progress.\nAre you sure you want to do this?"
    new "저장하지 않은 진행은 사라집니다. 불러올까요?"
    old "Are you sure you want to return to the main menu?\nThis will lose unsaved progress."
    new "저장하지 않은 진행을 마치고 처음 화면으로 돌아갈까요?"
