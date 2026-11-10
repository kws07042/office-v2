# Visual tokens for the 1280 × 720 Ren'Py canvas initialized in options.rpy.
define badge_ink = "#202a3f"
define badge_accent = "#294da1"
define badge_paper = "#f4f5f7"
define badge_rail = "#e8edf4"
define badge_rule = "#c8d0df"
define badge_muted = "#4d5f7a"
define badge_focus = "#dbe5f5"
define badge_font = "fonts/Pretendard-Regular.otf"

style badge_text is default:
    font badge_font
    size 20
    color badge_ink
style badge_button is button:
    background None
    hover_background Solid(badge_focus)
    selected_background Solid(badge_focus)
    selected_hover_background Solid("#cfdcf2")
    insensitive_background None
    padding (12, 9)
    yminimum 42
    keyboard_focus True
style badge_button_text is badge_text:
    size 18
    hover_color badge_accent
    selected_color badge_accent
    insensitive_color "#627089"
style badge_primary_button is badge_button:
    background Solid(badge_accent)
    hover_background Solid("#1d387a")
style badge_primary_button_text is badge_button_text:
    color "#ffffff"
    hover_color "#ffffff"
style badge_tab_button is badge_button:
    padding (12, 8)
    yminimum 42
style badge_tab_button_text is badge_button_text
style badge_segment_button is badge_button:
    background Solid(badge_rail)
    selected_background Solid(badge_accent)
    selected_hover_background Solid("#1d387a")
    padding (11, 8)
    yminimum 38
style badge_segment_button_text is badge_button_text:
    size 17
    selected_color "#ffffff"
    selected_hover_color "#ffffff"
style badge_scroll is vscrollbar:
    xsize 5
    base_bar Solid(badge_rail)
    thumb Solid("#879bbb")
    unscrollable "hide"
style badge_slider is bar:
    xsize 215
    ysize 22
    left_bar Solid(badge_accent, ysize=3)
    right_bar Solid("#abbad1", ysize=3)
    thumb Solid(badge_accent, xysize=(7, 18))
    hover_thumb Solid("#1d387a", xysize=(9, 20))
    thumb_align 0.5
    thumb_offset 3
    bar_resizing True

screen badge_shell(active):
    add Solid(badge_paper)
    add Solid(badge_rail) xysize (256, 720)
    add Solid(badge_accent) xysize (5, 720)
    add Solid(badge_rule) xpos 255 xysize (1, 720)
    add "gui/badge/office-id.svg" xpos 37 ypos 44 xysize (24, 25)
    text "퇴근 후, 우리" xpos 70 ypos 47 size 20 color badge_ink
    vbox:
        xpos 34 ypos 134 spacing 7
        textbutton "설정" action ShowMenu("preferences") selected active == "preferences" style "badge_button" xsize 190
        textbutton "우리의 기록" action ShowMenu("progression_hub") selected active == "progression_hub" style "badge_button" xsize 190
        if not main_menu:
            textbutton "대화 기록" action ShowMenu("history") selected active == "history" style "badge_button" xsize 190
        textbutton "저장·불러오기":
            action ShowMenu("load" if main_menu else "save")
            selected active in ("save", "load")
            style "badge_button"
            xsize 190
    textbutton "돌아가기" xpos 34 ypos 637 action Return() style "badge_button"

screen badge_setting_row(label):
    fixed:
        xysize (870, 61)
        add Solid(badge_rule) ypos 60 xysize (870, 1)
        text label style "badge_text" yalign 0.5
        hbox:
            xalign 1.0 yalign 0.5 spacing 6
            transclude
