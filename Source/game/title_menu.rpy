# 퇴근 후, 우리 — title/menu v002, 1280x720. No story/save schema changes.
default persistent.office_title_motion = True
define office_title_font = "fonts/NanumMyeongjo-Regular.ttf"
define office_title_people = (
    ("ria", "강리아", "비가 그친 뒤에도, 조금 더 함께."),
    ("jihyun", "백지현", "작은 취미를 나누는, 느긋한 저녁."),
    ("yujin", "차유진", "같은 창가에서 발견한 다른 풍경."),
    ("seoyun", "한서윤", "책장을 넘기듯, 천천히 가까워지는 시간."),
)

transform office_reveal(delay=0.0, duration=0.65):
    alpha 0.0 yoffset 8
    pause delay
    ease duration alpha 1.0 yoffset 0

transform office_intro_lockup:
    xpos 340 ypos 167
    pause 4.0
    ease 1.0 xpos 56 ypos 105 zoom 0.766667 alpha 0.0

transform office_intro_background:
    alpha 0.0
    ease 0.9 alpha 1.0

transform office_light:
    alpha 0.3
    ease 7.0 alpha 0.7 xoffset -12 yoffset 8
    ease 7.0 alpha 0.3 xoffset 0 yoffset 0
    repeat

transform office_mote(delay=0.0):
    alpha 0.0
    pause delay
    parallel:
        linear 15.0 yoffset -48 xoffset 18
    parallel:
        ease 5.0 alpha 0.4
        pause 5.0
        ease 5.0 alpha 0.0
    yoffset 0 xoffset 0
    repeat

transform office_nav_hover:
    on hover:
        ease 0.18 xoffset 5
    on idle:
        ease 0.18 xoffset 0

style office_nav_button is button:
    background None
    hover_background Solid("#eadfe877")
    insensitive_background None
    padding (14, 10)
    xsize 350
    ysize 57
style office_nav_button_text is button_text:
    font office_title_font
    color "#705b75"
    hover_color "#765489"
    size 21
style office_small_button is button:
    background None
    hover_background Solid("#eadfe866")
    padding (12, 8)
style office_small_button_text is button_text:
    color "#978490"
    hover_color "#62406b"
    size 13
style office_person_button is button:
    background None
    hover_background Solid("#fffaf319")
    selected_background Solid("#e5c99822")
    padding (10, 13)
    xsize 111
    ysize 45
style office_person_button_text is button_text:
    color "#eedecf"
    hover_color "#ffffff"
    selected_color "#fff9ed"
    xalign 0.5
    size 15
style office_setting_button is button:
    padding (17, 10)
    xsize 716
    yminimum 43
style office_setting_button_text is button_text:
    size 18
    selected_color "#705286"
style office_slot_button is button:
    padding (12, 12)
    xsize 350
    ysize 177
    background CreamRoundedPanel("#faf5ee", "#e6dbd0", radius=6)
    hover_background CreamRoundedPanel("#f1e8f8", "#ac91be", radius=6)
    insensitive_background CreamRoundedPanel("#faf5ee", "#e6dbd0", radius=6)

screen office_logo_intro():
    modal True
    zorder 300
    add Solid("#302638")
    add "gui/title/cafe_evening_v001.png" xysize (1280, 720) at office_intro_background
    add "gui/title/intro_veil.png"
    if persistent.office_title_motion:
        add "gui/title/light_bloom.png" xpos 700 ypos -120 at office_light
        fixed:
            xysize (600, 350)
            at office_intro_lockup
            add "gui/title/logo_light_motif.png" xysize (600, 350) at office_reveal(0.5, 1.0)
            add "gui/title/logo_light_first.png" xysize (600, 350) at office_reveal(1.0, 1.15)
            add "gui/title/logo_light_second.png" xysize (600, 350) at office_reveal(1.55, 1.15)
            add "gui/title/logo_light_subtitle.png" xysize (600, 350) at office_reveal(2.4, 0.85)
        text "하루의 끝에서, 우리가 시작된다." font office_title_font size 17 color "#fff7eb" xalign 0.5 ypos 546 at office_reveal(2.8, 0.8)
        timer 5.0 action Return()
    else:
        add "gui/title/logo_light_transparent.png" xpos 340 ypos 167 xysize (600, 350)
        timer 1.2 action Return()
    textbutton "클릭 또는 Enter로 건너뛰기  →" xpos 1000 ypos 663 text_size 12 text_color "#efdfc9" background None hover_background None action Return()
    key "dismiss" action Return()
    key "game_menu" action Return()

# Ren'Py calls this once at application startup, not when returning to main_menu.
label splashscreen:
    call screen office_logo_intro
    return

screen office_title_art(person):
    add "gui/title/cafe_evening_v001.png" xysize (1280, 720)
    fixed:
        xpos 480 ypos 0 xysize (800, 720)
        clipping True
        add Transform("gui/title/" + person + ".png", xysize=(1280, 720)) xpos -240
    add "gui/title/bottom_shade.png"
    add "gui/title/menu_veil.png"
    if persistent.office_title_motion:
        add "gui/title/light_bloom.png" xpos 720 ypos -270 at office_light
        for index in range(9):
            add "gui/title/mote.png" xpos (510 + (index * 83) % 730) ypos (85 + (index * 109) % 540) at office_mote(index * 1.7)

screen office_title_menu(person):
    use office_title_art(person)
    $ person_index = {"ria":0, "jihyun":1, "yujin":2, "seoyun":3}[person]
    $ current = office_title_people[person_index]
    add Solid("#b59a6a") xpos 93 ypos 93 xysize (32, 1)
    text "A LITTLE CLOSER, AFTER WORK" xpos 141 ypos 85 size 11 kerning 1.5 color "#9c806d"
    add "gui/title/logo_dark_transparent.png" xpos 56 ypos 105 xysize (460, 268)
    text "하루가 끝나고,\n우리의 이야기가 시작되는 시간." xpos 103 ypos 388 font office_title_font size 18 color "#9b8590" line_spacing 9
    vbox:
        xpos 90 ypos 460 spacing 4
        button:
            id "start_button"
            style "office_nav_button"
            at office_nav_hover
            action [SetVariable("cream_preview_active", False), SetVariable("cream_preview_mode", None), Start()]
            hbox:
                spacing 20
                text "01" size 13 color "#b79b83" yalign 0.5
                text "처음부터 읽기" font office_title_font size 23 color "#5e426c"
                text "↗" size 22 color "#ae8e59"
        button:
            id "office_load_button"
            style "office_nav_button"
            at office_nav_hover
            action ShowMenu("load", _transition=Dissolve(0.3))
            hbox:
                spacing 20
                text "02" size 13 color "#b79b83" yalign 0.5
                text "이어 읽기" font office_title_font size 23 color "#705b75"
        button:
            id "office_preferences_button"
            style "office_nav_button"
            at office_nav_hover
            action ShowMenu("preferences", _transition=Dissolve(0.3))
            hbox:
                spacing 20
                text "03" size 13 color "#b79b83" yalign 0.5
                text "설정" font office_title_font size 23 color "#705b75"
    text "초여름, 퇴근 이후의 이야기" xpos 103 ypos 670 size 12 color "#ac9ba6"
    if not renpy.variant("web"):
        textbutton "종료" xpos 373 ypos 658 style "office_small_button" action Quit(confirm=True)
    text ("0%d / 04     ─     AFTER HOURS" % (person_index + 1)) xpos 966 ypos 47 size 12 color "#fff4e9" outlines [(1, "#30243f88", 0, 1)]
    text "네 사람, 서로 다른 온도의 저녁" xpos 748 ypos 527 size 13 color "#ead9c8" outlines [(1, "#30243f88", 0, 1)]
    text current[1] xpos 748 ypos 555 font office_title_font size 38 kerning 2 color "#fff4e9" outlines [(1, "#30243f88", 0, 1)]
    text current[2] xpos 748 ypos 608 size 14 color "#ead9c8" outlines [(1, "#30243f88", 0, 1)]
    hbox:
        xpos 738 ypos 645 spacing 9
        for key, person_name, caption in office_title_people:
            vbox:
                add Solid("#e5c998" if key == person else "#fff5") xysize (111, 1)
                textbutton person_name:
                    id ("office_title_" + key)
                    style "office_person_button"
                    selected key == person
                    action [SetScreenVariable("title_person", key), With(Dissolve(0.9))]
    if config.developer:
        textbutton "개발용 장면 보기" xpos 1065 ypos 10 style "office_small_button" text_color "#fffaf3" action ShowMenu("office_dev_menu")

screen office_menu_backdrop():
    add "gui/title/cafe_evening_v001.png" xysize (1280, 720)
    add "gui/title/menu_wash.png"

screen office_menu_heading(title, subtitle):
    add "gui/title/logo_dark_transparent.png" xpos 52 ypos 56 xysize (240, 140)
    add Solid("#b59a6a") xpos 85 ypos 221 xysize (32, 1)
    text title xpos 84 ypos 253 font office_title_font size 47 color "#58445f"
    text subtitle xpos 86 ypos 325 size 16 color "#998594"
    textbutton "이야기 보관함" xpos 73 ypos 416 style "office_small_button" action ShowMenu("load", _transition=Dissolve(0.3))
    textbutton "설정" xpos 73 ypos 463 style "office_small_button" action ShowMenu("preferences", _transition=Dissolve(0.3))
    textbutton "←   돌아가기" xpos 72 ypos 610 style "office_nav_button" text_size 19 action Return()
    if not main_menu:
        textbutton "처음 화면" xpos 86 ypos 675 style "office_small_button" action MainMenu(confirm=True)

screen office_preferences():
    use office_menu_backdrop
    use office_menu_heading("설정", "나에게 편안한 속도로")
    frame:
        xpos 404 ypos 106 xysize (792, 508) padding (36, 30)
        background CreamRoundedPanel("#fffcf7", "#ddcfc0", radius=8)
        vbox:
            spacing 18
            text "나의 읽기 환경" font office_title_font size 25 color "#66516e"
            add Solid("#e8ddd2") xysize (716, 1)
            text "글자 표시 속도" size 19 color "#6c576d"
            bar value Preference("text speed") xsize 716 ysize 12 left_bar Solid("#8e7194") right_bar Solid("#e8ddd2")
            textbutton "글자 즉시 표시" style "office_setting_button" action Preference("text speed", 0)
            textbutton ("메신저 입력 연출  ·  켜짐" if persistent.phone_typing_enabled else "메신저 입력 연출  ·  꺼짐") style "office_setting_button" action ToggleField(persistent, "phone_typing_enabled")
            textbutton ("타이틀 움직임  ·  켜짐" if persistent.office_title_motion else "타이틀 움직임  ·  꺼짐") style "office_setting_button" action ToggleField(persistent, "office_title_motion")
            if not renpy.variant("web"):
                hbox:
                    spacing 12
                    textbutton "창 모드" style "office_setting_button" xsize 352 action Preference("display", "window")
                    textbutton "전체 화면" style "office_setting_button" xsize 352 action Preference("display", "fullscreen")
            text "당신의 속도로 읽어 주세요." font office_title_font size 17 color "#b39b9c" xalign 0.5

screen office_file_slots(mode):
    use office_menu_backdrop
    use office_menu_heading(("저장" if mode == "save" else "불러오기"), "우리의 이야기가 머문 곳")
    frame:
        xpos 404 ypos 106 xysize (792, 508) padding (36, 26)
        background CreamRoundedPanel("#fffcf7", "#ddcfc0", radius=8)
        vbox:
            spacing 18
            text "이야기가 머문 곳" font office_title_font size 25 color "#66516e"
            add Solid("#e8ddd2") xysize (716, 1)
            grid 2 2:
                spacing 16
                for slot in range(1, 5):
                    $ slot_name = str(slot)
                    button:
                        id ("office_slot_" + slot_name)
                        style "office_slot_button"
                        sensitive (mode == "save" or FileLoadable(slot_name))
                        action (FileSave(slot_name, confirm=True) if mode == "save" else FileLoad(slot_name, confirm=True))
                        vbox:
                            spacing 7
                            fixed:
                                xysize (326, 81)
                                add Solid("#ece5e1")
                                if FileLoadable(slot_name):
                                    add FileScreenshot(slot_name) xysize (326, 81)
                                else:
                                    text ("0" + slot_name) xpos 12 ypos 10 size 18 color "#c6b5bc"
                                    text "+" xalign 0.5 yalign 0.5 size 27 color "#d3c2c7"
                            text ("STORY 0" + slot_name) size 12 color "#a894a1"
                            text FileTime(slot_name, format="%m월 %d일  %H:%M", empty="비어 있는 이야기") size 17 color "#a18d9d"
            text "대사와 선택, 함께 쌓은 기억이 저장됩니다." size 13 color "#b39b9c" xalign 0.5

screen office_dev_menu():
    tag menu
    use office_menu_backdrop
    use office_menu_heading("장면 확인", "개발용 바로가기")
    frame:
        xpos 404 ypos 106 xsize 792 padding (36, 28)
        background CreamRoundedPanel("#fffcf7", "#ddcfc0", radius=8)
        vbox:
            spacing 12
            textbutton "화면 배치 확인" id "cream_preview_button" xsize 716 action Start("cream_preview_start")
            textbutton "유진 전체 대본 확인" id "yujin_preview_button" xsize 716 action Start("yujin_early_preview")
            textbutton "지현 전체 대본 확인" id "jihyun_preview_button" xsize 716 action Start("jihyun_early_preview")
            textbutton "서윤 전체 대본 확인" id "seoyun_preview_button" xsize 716 action Start("seoyun_preview")
            textbutton "R02 대화 확인" id "ria_r02_preview_button" xsize 716 action Start("ria_r02_preview")
            textbutton "R08 메신저 확인" id "phone_preview_button" xsize 716 action Start("office_phone_preview")

screen office_confirm(message, yes_action, no_action):
    add Solid("#21172eaa")
    frame:
        xalign 0.5 yalign 0.5 xsize 640 padding (38, 32)
        background CreamRoundedPanel("#fff9f0", "#d4b783", radius=8)
        vbox:
            spacing 24
            text "◌" xalign 0.5 size 34 color "#b79b68"
            text message font office_title_font size 26 color "#67506e" xmaximum 564 text_align 0.5 xalign 0.5
            hbox:
                spacing 12
                textbutton "돌아가기" xsize 276 text_size 19 action no_action
                textbutton "계속하기" xsize 276 text_size 19 action yes_action
