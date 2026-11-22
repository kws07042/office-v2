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
        if art_stage_has_picture():
            add "art stage"
        else:
            add ("gui/cream/stage_" + cream_stage_mode() + ".svg") xysize (1280, 720)
        if art_cg_path():
            pass
        elif heroine_sprite_visible():
            add "heroine stage sprite" xalign 0.5 ypos SPRITE_YPOS at (silk_bust_idle if silk_motion_on() else silk_still)
        elif cream_ria_visible():
            add "ria ui bust" xalign 0.5 ypos 28 at (silk_bust_idle if silk_motion_on() else silk_still)
        elif cream_yujin_visible():
            add "yujin ui bust" xalign 0.5 ypos 50 at (silk_bust_idle if silk_motion_on() else silk_still)

screen cream_heart(fraction):
    fixed:
        xsize 20 ysize 20
        add silk("heart", False, size=(20, 20))
        if fraction > 0:
            add Crop((0, 0, max(1, int(20 * min(1.0, fraction))), 20), silk("heart", True, size=(20, 20)))

transform silk_heart_pulse:
    zoom 1.0
    easein 0.12 zoom 1.22
    easeout_bounce 0.5 zoom 1.0

screen silk_big_heart(value, tier="normal"):
    # 큰 하트 하나가 아래부터 차오른다(0~100). 테두리는 신뢰: 금색(높음) / 보통 / 흐린 점선(낮음).
    $ heart_h = 46
    $ filled = int(heart_h * max(0, min(100, value)) / 100.0)
    $ flash = renpy.get_screen("bond_flash")
    fixed:
        xysize (52, 48)
        at ((bond_shake if (flash and flash.scope.get("kind") == "drop") else (silk_heart_pulse if ((renpy.get_screen("silk_heart_burst") or flash) and silk_motion_on()) else silk_still)) if silk_motion_on() else silk_still)
        add silk("bigheart", "back", size=(52, 48))
        if filled > 0:
            add Crop((0, heart_h - filled, 52, filled), silk("bigheart", "fill", size=(52, 48))) ypos (heart_h - filled)
        add silk("bigheart", ("line_gold" if tier == "gold" else ("line_low" if tier == "low" else "line")), size=(52, 48))
        text str(value) font "fonts/Jua-Regular.ttf" size 17 color ("#FFFDFB" if value >= 45 else "#3B0B22") xalign 0.5 ypos 13 outlines []

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
            xanchor 1.0 xpos 1182 ypos 26 xsize 214
            padding (14, 8, 22, 13)
            background silk_surface("button")
            hbox:
                spacing 11
                use silk_big_heart(bond_mind(focus), bond_trust_tier(focus))
                vbox:
                    spacing 2 yalign 0.5
                    text person_name font "fonts/Jua-Regular.ttf" size 21 color "#3B0B22"
                    text relation_stage(focus) size 13 color ("#A99BA1" if bond_trust_tier(focus) == "low" else "#6E4553")
        if cream_preview_active:
            use cream_preview_controls

init python:
    DOC_OFFICE_WORDS = ("회사", "사무", "회의", "피칭", "클라이언트", "탕비", "옥상", "복도", "계단", "온빛", "팝업", "현장", "작업 공간", "공용")

    def dialogue_doc_stamp():
        place = getattr(renpy.store, "location", "") or ""
        return "내부 메모" if any(w in place for w in DOC_OFFICE_WORDS) else "개인 메모"

default dialogue_cg_mode = False
default dialogue_cg_location = None

init python:
    def dialogue_cg_begin():
        renpy.store.dialogue_cg_mode = True
        renpy.store.dialogue_cg_location = getattr(renpy.store, "location", None)

    def dialogue_cg_check():
        # 친밀 장면이 끝나 장소가 바뀌면 평소 대화창으로 돌아간다.
        st = renpy.store
        if st.dialogue_cg_mode and getattr(st, "location", None) != st.dialogue_cg_location:
            st.dialogue_cg_mode = False

    config.start_interact_callbacks.append(dialogue_cg_check)

# 대화창 — 평소(F): 웜그레이 업무 서류 반투명 판 + 와인 이름표 + 클립.
#          친밀 장면(H): 판 없이 아래쪽 어두운 그라데이션 위에 짧은 대사만.
screen cream_dialogue_panel(who, what, use_substitution=True, advance=True):
    if dialogue_cg_mode or event_cut_active:
        add "gui/window/cg_scrim.png" xpos 0 ypos 530
        textbutton "창 숨기기 · H" action HideInterface() background None hover_background None xanchor 1.0 xpos 1250 ypos 104 text_size 15 text_color "#E8C99A" text_hover_color "#FFFDFB" text_outlines [(1, "#14080E66", 0, 0)]
        window:
            id "window"
            xpos 0 ypos 600 xsize 1280 ysize 110
            padding (104, 0, 104, 0)
            background None
            foreground None
            vbox:
                spacing 4
                if who:
                    text who id "who" font silk_title_font(who) size 19 color "#E8C99A" outlines []
                text what:
                    id "what"
                    font "fonts/Pretendard-Regular.otf"
                    size 24
                    color "#FBEFE6"
                    outlines [(2, "#14080E99", 0, 1)]
                    xmaximum 1060
                    line_spacing 6
                    language "korean-with-spaces"
                    substitute use_substitution
        if advance:
            add silk("next", "#E8C99A", size=(14, 9)) xpos 1176 ypos 646 at (silk_next_bob if silk_motion_on() else silk_still)
    else:
        fixed:
            at (silk_panel_in if silk_motion_on() else silk_still)
            xpos 24 ypos 536 xysize (1232, 166)
            add Solid("#14080E") xpos 4 ypos 6 xysize (1232, 166) alpha 0.18
            add Solid("#EFE8E0") xysize (1232, 166) alpha 0.92
            add Solid("#FFFFFF") xysize (1232, 1) alpha 0.5
            add Solid("#B39462") xpos 72 ypos 132 xysize (1088, 1) alpha 0.85
            text "온빛브랜딩 · 연말 피칭 TF" xanchor 1.0 xpos 1080 ypos 14 size 12 color "#9A8B80" kerning 1.5
            frame:
                xanchor 1.0 xpos 1180 ypos 10 padding (1, 1, 1, 1)
                background Solid("#A2394F")
                frame:
                    padding (6, 0, 6, 1)
                    background Solid("#EFE8E0")
                    text dialogue_doc_stamp() size 12 color "#A2394F"
            add "gui/window/paperclip.svg" xpos -8 ypos -34 xysize (26, 72) at Transform(rotate=-7)
        window:
            at (silk_panel_in if silk_motion_on() else silk_still)
            id "window"
            xpos 24 ypos 578 xsize 1232 ysize 100
            padding (72, 0, 96, 0)
            background None
            foreground None
            text what:
                id "what"
                font "fonts/Pretendard-Regular.otf"
                size 25
                color "#2F262B"
                outlines []
                xmaximum 1060
                line_spacing 8
                language "korean-with-spaces"
                substitute use_substitution
        if who:
            frame:
                at (silk_tag_in if silk_motion_on() else silk_still)
                xpos 86 ypos 508 ysize 52
                padding (30, 0, 35, 6)
                background silk("tag", "#6B1E34")
                hbox:
                    spacing 10 yalign 0.5
                    text who:
                        id "who"
                        font silk_title_font(who)
                        size 26
                        color "#FBEFE6"
                        outlines []
                        yalign 0.5
                    if silk_english(who):
                        text silk_english(who) font "fonts/PlayfairDisplay-Italic.ttf" size 16 color "#E8C99A" outlines [] yalign 0.7
        if advance:
            add silk("next", "#6B1E34", size=(14, 9)) xpos 1190 ypos 650 at (silk_next_bob if silk_motion_on() else silk_still)

screen say(who, what):
    use cream_dialogue_panel(who, what)

screen silk_choice_item(item, i=0, n=0, intimate=False, wide=False):
    $ choice_text, choice_chip = silk_choice_parts(item.caption)
    $ choice_sub = None
    if wide and not choice_chip and " — " in choice_text:
        $ choice_text, choice_sub = choice_text.split(" — ", 1)
    button:
        at ((silk_choice_in(i), silk_choice_hover) if silk_motion_on() else (silk_still,))
        style "silk_choice_button"
        action ([Function(silk_pick, i, n, intimate), item.action] if n else item.action)
        alt item.caption
        hbox:
            spacing 12
            text choice_text style "silk_choice_text" language "korean-with-spaces" xmaximum (366 if choice_chip else (980 if wide else 530)) min_width (366 if choice_chip else 0)
            if choice_sub:
                text choice_sub style "silk_choice_sub" yalign 0.5 xmaximum (960 - 19 * len(choice_text))
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
                    use silk_choice_item(item, i, len(items), silk_has_intimate(items))
        if silk_has_intimate(items):
            frame:
                xalign 0.5 ypos 452
                padding (14, 4)
                background silk("flat", "#FFFDFB", 12)
                text "친밀한 장면을 미루는 선택에는 정답이 없어요." size 13 color "#4A2A36"
    else:
        frame:
            xpos 66 ypos 96 xsize 1148 ysize 428 padding (24, 22, 28, 27)
            background silk_surface("panel")
            viewport:
                mousewheel True draggable True arrowkeys True
                scrollbars "vertical"
                vscrollbar_xsize 6 vscrollbar_base_bar Solid("#E1D7CF") vscrollbar_thumb Solid("#B3123F") vscrollbar_unscrollable "hide"
                vbox:
                    xsize 1070 spacing 9
                    for i, item in enumerate(items):
                        use silk_choice_item(item, i, wide=True)

screen main_menu():
    tag menu
    add "silk ground"
    if renpy.loadable("images/cg/title_keyvisual.jpg"):
        add "images/cg/title_keyvisual.jpg"
    if silk_motion_on():
        add "silk title dots"
    if not renpy.loadable("images/cg/title_keyvisual.jpg"):
        add silk("band", size=(1280, 584)) at (silk_band_in if silk_motion_on() else silk_still)
    if silk_motion_on():
        add "silk title hearts"
    $ title_art = renpy.loadable("images/cg/title_keyvisual.jpg")
    vbox:
        at (((silk_tilt, silk_logo_in, silk_logo_float) if silk_motion_on() else (silk_tilt,)) + ((Transform(zoom=0.62),) if title_art else ()))
        xpos (40 if title_art else 84) ypos (40 if title_art else 150)
        spacing -6
        text "After Work, With You" font "fonts/PlayfairDisplay-Italic.ttf" size 30 color "#B3123F" xpos 8
        text "퇴근 후{color=#F2C14E},{/color} 우리":
            font "fonts/Jua-Regular.ttf"
            size 150
            kerning -3
            color "#FFFDFB"
            outlines [(4, "#B3123F", 11, 12), (4, "#3B0B22", 0, 0)]
    # 개발 중 확인용 진입점. 배포판(개발자 모드 꺼짐)에서는 보이지 않는다.
    default show_preview_links = False
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
    textbutton "크레딧" id "credits_button" action ShowMenu("silk_credits") style "silk_small_button" xpos 32 ypos 24
    if spring_story_unlocked():
        textbutton "숨은 이야기 · 이듬해 봄" id "spring_story_button" action Start("spring_story") style "silk_small_button" xpos 32 ypos 64
    textbutton "미니게임" id "minigame_button" action ShowMenu("minigame_hub") style "silk_small_button" xpos 32 ypos (104 if spring_story_unlocked() else 64)
    textbutton "회상 갤러리" id "gallery_button" action ShowMenu("gallery") style "silk_small_button" xpos 32 ypos (144 if spring_story_unlocked() else 104)
    if config.developer:
        text "네 히로인 전체 대본 · 아트 준비 중" xanchor 1.0 xpos 1216 ypos 688 size 12 color "#6E4553"

screen silk_quick_item(label, icon, target, ring=False):
    button:
        at ((silk_quick_hover, silk_phone_ring) if (ring and silk_motion_on()) else ((silk_quick_hover if silk_motion_on() else silk_still),))
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
        if not event_cut_active and not dialogue_cg_mode:
            hbox:
                xanchor 1.0 xpos 1196 ypos 676 spacing 0
                use silk_quick_item("되돌리기", "rollback", Rollback())
                use silk_quick_item("기록", "history", ShowMenu("history"))
                use silk_quick_item("자동", "auto", Preference("auto-forward", "toggle"))
                use silk_quick_item("스킵", "skip", Skip())
                use silk_quick_item("저장", "save", ShowMenu("save"))
                use silk_quick_item("불러오기", "load", ShowMenu("load"))
                use silk_quick_item("퀵저장", "qsave", QuickSave())
                use silk_quick_item("퀵로드", "qload", QuickLoad(confirm=True))
                use silk_quick_item("기록함", "album", ShowMenu("progression_hub"))
                use silk_quick_item("설정", "prefs", ShowMenu("preferences"))
                use silk_quick_item("메뉴", "menu", MainMenu(confirm=True))
            button:
                id "phone_open_button"
                at ((silk_quick_hover, silk_phone_ring) if (silk_phone_has_unread() and silk_motion_on()) else ((silk_quick_hover if silk_motion_on() else silk_still),))
                xanchor 1.0 xpos 1248 ypos 31 xysize (56, 57) padding (0, 0)
                background silk("pill", "#FFFDFB", "#3B0B22", "#3B0B22", None)
                hover_background silk("pill", "#3B0B22", "#3B0B22", "#B3123F", None)
                action Show("office_phone_archive")
                alt "메신저"
                add silk("icon", "phone", "#3B0B22", size=(24, 24)) xpos 14 ypos 13
                if silk_phone_has_unread():
                    add silk("flat", "#B3123F", 7) xysize (14, 14) xpos 38 ypos 0
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

# 메뉴 뒤에는 직전 게임 화면을 흐리게 깐다. 타이틀에서 열면 실크 바탕.
screen silk_menu_backdrop():
    if main_menu:
        add "silk ground"
    else:
        add Solid("#E7DFD8")
        add Transform(FileCurrentScreenshot(), xysize=(1280, 720), fit="cover", blur=10)
        add Solid("#3B0B2259")

style silk_pref_bar is bar:
    ysize 26
    left_bar Fixed(Transform(silk("flat", "#B3123F", 4), ysize=8, yalign=0.5))
    right_bar Fixed(Transform(silk("flat", "#E1D7CF", 4), ysize=8, yalign=0.5))
    thumb silk("pill", "#FFFDFB", "#3B0B22", "#3B0B22", None, 2, 3, size=(26, 27))
    thumb_offset 13
    left_gutter 13
    right_gutter 13
style silk_tab_button is button:
    background None
    hover_background silk("flat", "#EADFE2", 24)
    selected_background silk("pill", "#B3123F", "#3B0B22", "#3B0B22", None, 3, 4)
    xsize 190 ysize 52 padding (22, 0, 22, 5)
style silk_tab_button_text is default:
    font "fonts/Jua-Regular.ttf"
    size 21
    color "#3B0B22"
    selected_color "#FFFDFB"
    yalign 0.5
    outlines []
style silk_switch_button is button:
    background silk("pill", "#FFFDFB", "#3B0B22", None, None, 0, 0)
    selected_background silk("pill", "#B3123F", "#3B0B22", None, None, 0, 0)
    xysize (60, 32) padding (0, 0)

screen silk_pref_slider(label, value):
    vbox:
        spacing 8
        text label size 19 color "#3B0B22"
        bar value value xsize 620 style "silk_pref_bar"

screen silk_pref_switch(label, note, action, on):
    hbox:
        xsize 620
        vbox:
            spacing 3 xsize 540
            text label size 19 color "#3B0B22"
            if note:
                text note size 14 color "#6E4553"
        button:
            style "silk_switch_button"
            yalign 0.5
            action action
            selected on
            alt label
            add silk("pill", ("#FFFDFB" if on else "#E1D7CF"), "#3B0B22", None, None, 0, 0, size=(24, 24)) xpos (32 if on else 4) ypos 4

screen preferences():
    tag menu
    default tab = "screen"
    use silk_menu_backdrop
    frame:
        at (silk_menu_panel if silk_motion_on() else silk_still)
        xalign 0.5 yalign 0.5 xsize 1046 ysize 606 padding (0, 0, 6, 7)
        background silk_surface("panel")
        hbox:
            frame:
                xsize 246 ysize 596 padding (26, 30, 22, 26)
                background silk("flat", "#F6F2EE", 22)
                vbox:
                    spacing 8
                    use silk_menu_title("설정", "Config")
                    null height 14
                    for key, label in (("screen", "화면"), ("text", "글자"), ("sound", "소리"), ("motion", "연출")):
                        textbutton label action SetScreenVariable("tab", key) selected (tab == key) style "silk_tab_button" id ("pref_tab_" + key)
                vbox:
                    yalign 1.0 spacing 8
                    textbutton "돌아가기" action Return() style "silk_small_button"
                    if not main_menu:
                        textbutton "처음 화면" action MainMenu(confirm=True) style "silk_small_button"
            add Solid("#3B0B22") xsize 2 ysize 596
            frame:
                xsize 790 ysize 596 padding (56, 46, 50, 40)
                background None
                vbox:
                    spacing 28
                    if tab == "screen":
                        text "화면 모드" size 19 color "#3B0B22"
                        hbox:
                            spacing 10
                            textbutton "창모드" action Preference("display", "window") text_size 19
                            textbutton "전체화면" action Preference("display", "fullscreen") text_size 19
                        text "전체화면은 F11 키로도 바꿀 수 있어요." size 14 color "#6E4553"
                    elif tab == "text":
                        use silk_pref_slider("글자 표시 속도", Preference("text speed"))
                        use silk_pref_slider("자동 진행 대기 시간", Preference("auto-forward time"))
                        use silk_pref_switch("글자 즉시 표시", "대사를 한 번에 보여 줍니다.", Preference("text speed", 0), preferences.text_cps == 0)
                        use silk_pref_switch("읽은 대사만 스킵", "처음 보는 대사에서는 스킵이 멈춥니다.", Preference("skip", "toggle"), not preferences.skip_unseen)
                    elif tab == "sound":
                        if config.has_music:
                            use silk_pref_slider("배경 음악", Preference("music volume"))
                        if config.has_sound:
                            use silk_pref_slider("효과음", Preference("sound volume"))
                        if config.has_voice:
                            use silk_pref_slider("음성", Preference("voice volume"))
                        use silk_pref_switch("전체 소리 끄기", None, Preference("all mute", "toggle"), preferences.get_mute("music") and preferences.get_mute("sfx"))
                    else:
                        use silk_pref_switch("화면 움직임 효과", "장 제목 카드, 버튼 움직임, 하트 같은 연출", ToggleField(persistent, "silk_motion", True, False), silk_motion_on())
                        use silk_pref_switch("메신저 입력 중 연출", "상대가 입력하는 동안 잠깐 기다립니다.", ToggleField(persistent, "phone_typing_enabled"), bool(persistent.phone_typing_enabled))
                        text "호감도는 함께 겪은 관계의 진전을 보여 줍니다.\n취향에 정답은 없고, 선택에 따라 반응과 기억이 달라집니다." size 15 color "#6E4553" line_spacing 4 xmaximum 620

# 저장·불러오기: 장면 썸네일이 보이는 3×2 카드, 쪽 넘김, 자동·퀵 저장 칸.
# 1쪽의 칸 이름은 예전과 같은 "1"~"6"이라 이전 저장도 그대로 보인다.

define config.thumbnail_width = 384
define config.thumbnail_height = 216
define SILK_FILE_PAGES = 6
define SILK_FILE_COLS = 3
define SILK_FILE_ROWS = 2

init 8 python:
    def silk_save_name():
        # 저장 칸에 보일 한 줄: '장 제목 · 장소'
        st = renpy.store
        chapter = getattr(st, "chapter", "") or ""
        place = (getattr(st, "location", "") or "").rpartition("·")[2].strip()
        st.save_name = " · ".join(x for x in (chapter, place) if x)

    config.start_interact_callbacks.append(silk_save_name)

transform silk_slot_in(i=0):
    on show:
        alpha 0.0 yoffset 10
        pause (0.04 * i)
        easein 0.24 alpha 1.0 yoffset 0

style silk_slot_button is button:
    background silk_surface("card")
    hover_background silk_surface("card_on")
    insensitive_background silk_surface("quiet")
    padding (11, 11, 13, 15)
    xysize (292, 230)
style silk_page_button is silk_small_button:
    selected_background silk_surface("selected")
    xminimum 46
style silk_page_button_text is silk_small_button_text:
    selected_color "#FFFDFB"
    xalign 0.5

screen file_slots(mode):
    $ page = FileCurrentPage()
    if (page in ("auto", "quick") and mode == "save") or (page not in ("auto", "quick") and not (page.isdigit() and 1 <= int(page) <= SILK_FILE_PAGES)):
        $ page = "1"
    use silk_menu_backdrop
    frame:
        at (silk_menu_panel if silk_motion_on() else silk_still)
        xalign 0.5 yalign 0.5 xsize 1010 ysize 660 padding (36, 26, 40, 30)
        background silk_surface("panel")
        vbox:
            spacing 12
            hbox:
                spacing 18
                use silk_menu_title(("저장" if mode == "save" else "불러오기"), ("Save" if mode == "save" else "Load"))
                text ("저장할 칸을 고르세요. 선택과 기억이 함께 저장됩니다." if mode == "save" else "이어서 읽을 장면을 고르세요.") size 17 color "#6E4553" yalign 0.75
            hbox:
                spacing 6
                for p in range(1, SILK_FILE_PAGES + 1):
                    textbutton str(p) action FilePage(str(p)) selected (page == str(p)) style "silk_page_button" id ("file_page_%d" % p)
                null width 14
                if mode == "load":
                    textbutton "자동" action FilePage("auto") selected (page == "auto") style "silk_page_button" id "file_page_auto"
                    textbutton "퀵" action FilePage("quick") selected (page == "quick") style "silk_page_button" id "file_page_quick"
            grid SILK_FILE_COLS SILK_FILE_ROWS:
                spacing 14
                for i in range(1, SILK_FILE_COLS * SILK_FILE_ROWS + 1):
                    $ slot = str(i)
                    $ pg = page
                    $ filled = FileLoadable(slot, page=pg)
                    button:
                        at (silk_slot_in(i) if silk_motion_on() else silk_still)
                        style "silk_slot_button"
                        id ("file_slot_%s_%s" % (pg, slot))
                        action (FileSave(slot, confirm=True, page=pg) if mode == "save" else FileLoad(slot, confirm=True, page=pg))
                        sensitive (mode == "save" or filled)
                        alt ("%s쪽 %s칸" % (pg, slot))
                        vbox:
                            spacing 6
                            fixed:
                                xysize (270, 152)
                                add Solid("#E7DFD8")
                                if filled:
                                    add FileScreenshot(slot, page=pg) xysize (270, 152) fit "contain" xalign 0.5 yalign 0.5
                                else:
                                    text "비어 있음" size 17 color "#A3959B" xalign 0.5 yalign 0.5
                            hbox:
                                spacing 8
                                text (("자동 " if page == "auto" else ("퀵 " if page == "quick" else "")) + slot) font "fonts/Jua-Regular.ttf" size 18 color "#B3123F"
                                text FileTime(slot, page=pg, format="%m월 %d일 %H:%M", empty="") size 14 color "#6E4553" yalign 0.8
                            $ save_line = FileSaveName(slot, empty="", page=pg)
                            text (save_line if len(save_line) <= 24 else save_line[:23] + "…") size 14 color "#3B0B22" xmaximum 270
        hbox:
            yalign 1.0 xalign 1.0 spacing 10
            textbutton "돌아가기" action Return() style "silk_small_button"

screen save():
    tag menu
    use file_slots("save")
screen load():
    tag menu
    use file_slots("load")

screen history():
    tag menu
    use silk_menu_backdrop
    frame:
        at (silk_menu_panel if silk_motion_on() else silk_still)
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
