define prototype_font = FontGroup().add("DejaVuSans.ttf", 0x0000, 0x04ff).add("DejaVuSans.ttf", 0x2000, 0x206f).add("SourceHanSansLite.ttf", 0x0500, 0x1fff).add("SourceHanSansLite.ttf", 0x2070, 0xffff)

style default:
    font prototype_font
    size 26
    color "#493f4c"
style button:
    padding (22, 12)
    background cream_round("button")
    hover_background cream_round("hover")
    insensitive_background cream_round("soft")
style button_text:
    color "#57485f"
    hover_color "#705286"
    insensitive_color "#aca2aa"
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
    color "#fffdf8"
    hover_color "#efdcff"
    outlines [(1, "#30243f", 0, 0)]
style event_text is default:
    color "#eef0f5"
style event_button is button:
    background Solid("#303a53")
    hover_background Solid("#4c5676")
style event_button_text is button_text:
    color "#eef0f5"
    hover_color "#fff3d9"

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
        xsize 22 ysize 22
        add "gui/cream/heart_empty.svg" xysize (22, 22)
        if fraction > 0:
            add Crop((0, 0, max(1, int(22 * min(1.0, fraction))), 22), Transform("gui/cream/heart_full.svg", xysize=(22, 22)))

screen story_header():
    zorder 10
    if not main_menu and not event_cut_active and not cream_menu_open():
        frame:
            xpos 28 ypos 22 xsize 395 padding (19, 14)
            background cream_round("panel")
            vbox:
                spacing 6
                text chapter size 19 color "#705684" xmaximum 355
                text location size 14 color "#857885" xmaximum 355
        $ focus = active_route if active_route in affinity else (cream_focus if cream_focus in affinity else "ria")
        $ person_name = {"ria":"강리아", "jihyun":"백지현", "yujin":"차유진", "seoyun":"한서윤"}[focus]
        frame:
            xpos 955 ypos 22 xsize 297 padding (17, 13)
            background cream_round("panel")
            vbox:
                spacing 7
                hbox:
                    spacing 13
                    text person_name size 17 color "#705684"
                    text cream_relation_name(focus) size 14 color "#948494"
                hbox:
                    spacing 6
                    for index in range(5):
                        use cream_heart((affinity[focus] - index * 20) / 20.0)
                    text (str(affinity[focus]) + " / 100") size 14 color "#857885" yalign 0.5
        if cream_preview_active:
            use cream_preview_controls

screen cream_dialogue_panel(who, what, use_substitution=True, advance=True):
    window:
        id "window"
        xpos 44 ypos 508 xsize 1192 ysize 154
        padding (32, 27)
        background None
        foreground None
        text what:
            id "what"
            font "fonts/Pretendard-Regular.otf"
            size 26
            color "#fffdf8"
            outlines [(2, "#30243f", 0, 0), (1, "#1a142966", 0, 2)]
            xmaximum 1128
            line_spacing 6
            substitute use_substitution
    if who:
        text who:
            id "who"
            xpos 76 ypos 481
            font "fonts/GowunDodum-Regular.ttf"
            size 23
            color cream_speaker_color(who)
            outlines [(2, cream_speaker_outline(who), 0, 0)]
        add Solid("#ccb8e3c0") xpos 76 ypos 519 xsize 152 ysize 1
    if advance:
        text "›" xpos 1196 ypos 637 size 28 color "#fffdf8" outlines [(2, "#30243f", 0, 0)]

screen say(who, what):
    use cream_dialogue_panel(who, what)

screen office_choice_list(items):
    vbox:
        xsize 588 spacing 10
        for item in items:
            textbutton item.caption action item.action style "office_choice_button"

screen choice(items):
    zorder 30
    if len(items) <= 3:
        if _history_list:
            use cream_dialogue_panel(_history_list[-1].who, _history_list[-1].what, False, False)
        if office_ui_long_choices(items):
            viewport:
                xalign 0.5 ypos 152 xsize 600 ysize 334
                mousewheel True draggable True arrowkeys True
                scrollbars "vertical"
                vscrollbar_style "office_scrollbar"
                use office_choice_list(items)
        else:
            vbox:
                xalign 0.5 yanchor 1.0 ypos 486 xsize 600 spacing 10
                for item in items:
                    textbutton item.caption action item.action style "office_choice_button"
    else:
        frame:
            xpos 66 ypos 142 xsize 1148 ysize 520 padding (24, 22)
            background cream_round("panel")
            viewport:
                mousewheel True draggable True arrowkeys True
                scrollbars "vertical"
                vscrollbar_style "office_scrollbar"
                vbox:
                    xsize 1076 spacing 10
                    for item in items:
                        textbutton item.caption action item.action style "office_choice_button"

screen main_menu():
    tag menu
    add "gui/cream/stage_day.svg" xysize (1280, 720)
    frame:
        xpos 82 ypos 62 xsize 580 ysize 596 padding (40, 34)
        background cream_round("panel")
        vbox:
            spacing 14
            text "AFTER WORK, WITH YOU" size 15 color "#a38d9f" kerning 2
            text "퇴근 후, 우리" size 58 color "#79608d"
            text "초여름, 퇴근 이후의 이야기" size 23 color "#80737f"
            null height 12
            textbutton "처음부터 읽기" action [SetVariable("cream_preview_active", False), SetVariable("cream_preview_mode", None), Start()] id "start_button" xsize 490
            textbutton "이어 읽기" action ShowMenu("load") xsize 490
            hbox:
                spacing 14
                textbutton "화면 배치 확인" action Start("cream_preview_start") id "cream_preview_button" xsize 238 text_size 20
                textbutton "유진 전체 대본 확인" action Start("yujin_early_preview") id "yujin_preview_button" xsize 238 text_size 20
            hbox:
                spacing 14
                textbutton "R02 대화 확인" action Start("ria_r02_preview") id "ria_r02_preview_button" xsize 238 text_size 20
                textbutton "R08 메신저 확인" action Start("office_phone_preview") id "phone_preview_button" xsize 238 text_size 20
            hbox:
                spacing 14
                textbutton "설정" action ShowMenu("preferences") xsize 238
                if not renpy.variant("web"):
                    textbutton "종료" action Quit(confirm=False) xsize 238
            text "네 히로인 전체 대본 · 아트 준비 중" size 15 color "#9c8f98"
    textbutton "우리의 기록 · 이야기 / CG / 결말":
        xpos 730 ypos 475 xsize 430 text_size 20
        action ShowMenu("progression_hub")
    textbutton "지현 전체 대본 확인":
        id "jihyun_preview_button"
        xpos 730 ypos 545 xsize 430
        action Start("jihyun_early_preview")
    textbutton "서윤 전체 대본 확인":
        id "seoyun_preview_button"
        xpos 730 ypos 610 xsize 430
        action Start("seoyun_preview")

screen quick_menu():
    zorder 100
    if not main_menu and not cream_menu_open() and not renpy.get_screen("office_phone") and not renpy.get_screen("office_phone_archive"):
        frame:
            xpos (565 if not event_cut_active else 750) ypos (678 if not event_cut_active else 18)
            padding (7, 2)
            background (None if not event_cut_active else cream_round("panel"))
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
            text "클릭·Enter 다음 / 휠 위로 되돌리기" xpos 76 ypos 691 size 12 color "#fffdf8" outlines [(1, "#30243f", 0, 0)]

screen cream_preview_controls():
    frame:
        xpos 28 ypos 111 padding (9, 8)
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
    add "gui/cream/stage_day.svg" xysize (1280, 720)
    frame:
        xalign 0.5 yalign 0.5 xsize 720 ysize 672 padding (42, 35)
        background cream_round("panel")
        viewport:
            xsize 636 ysize 602
            mousewheel True draggable True
            scrollbars "vertical"
            vbox:
                spacing 16
                text "설정" size 36 color "#79608d"
                text "글자 표시 속도" size 23
                textbutton "창모드" action Preference("display", "window") text_size 20
                textbutton "전체화면" action Preference("display", "fullscreen") text_size 20
                textbutton "읽은 대사만 스킵" action Preference("skip", "seen") text_size 20
                bar value Preference("text speed") xsize 620 ysize 14 left_bar Solid("#9c80b2") right_bar Solid("#e9dfd5")
                textbutton "글자 즉시 표시" action Preference("text speed", 0)
                text "자동 진행 대기 시간" size 21
                bar value Preference("auto-forward time") xsize 620 ysize 14 left_bar Solid("#9c80b2") right_bar Solid("#e9dfd5")
                if config.has_music:
                    text "음악" size 20
                    bar value Preference("music volume") xsize 620
                if config.has_sound:
                    text "효과음" size 20
                    bar value Preference("sound volume") xsize 620
                if config.has_voice:
                    text "음성" size 20
                    bar value Preference("voice volume") xsize 620
                textbutton ("메신저 입력 중 연출: 켜짐" if persistent.phone_typing_enabled else "메신저 입력 중 연출: 꺼짐") action ToggleField(persistent, "phone_typing_enabled") text_size 21
                text "호감도는 함께 겪은 관계의 진전을 보여 줍니다.\n취향에 정답은 없고, 선택에 따라 반응과 기억이 달라집니다." size 17 color "#796d82" line_spacing 4 xmaximum 620
                textbutton "돌아가기" action Return()
                if not main_menu:
                    textbutton "처음 화면" action MainMenu(confirm=True)

screen file_slots(mode):
    add "gui/cream/stage_day.svg" xysize (1280, 720)
    frame:
        xalign 0.5 yalign 0.5 xsize 990 padding (35, 28)
        background cream_round("panel")
        vbox:
            spacing 15
            text ("저장" if mode == "save" else "불러오기") size 36 color "#79608d"
            text "대사와 선택·기억을 함께 저장합니다." size 20 color "#9a8995"
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
    add "gui/cream/stage_day.svg" xysize (1280, 720)
    frame:
        xpos 48 ypos 26 xsize 1184 ysize 665 padding (30, 22)
        background cream_round("panel")
        vbox:
            spacing 15
            text "대화 기록" size 33 color "#79608d"
            viewport:
                id "history_viewport"
                xsize 1124 ysize 500
                mousewheel True draggable True
                scrollbars "vertical"
                vscrollbar_xsize 12
                vscrollbar_base_bar Solid("#e9dfd5")
                vscrollbar_thumb Solid("#ad93bd")
                yinitial 1.0
                vbox:
                    xsize 1070 spacing 14
                    for entry in _history_list:
                        if entry.who:
                            text entry.who size 19 color cream_speaker_color(entry.who, history=True)
                        text entry.what size 24 substitute False
            textbutton "돌아가기" action Return()

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    add Solid("#32243899")
    frame:
        xalign 0.5 yalign 0.5 xsize 800 padding (35, 30)
        background cream_round("panel")
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
