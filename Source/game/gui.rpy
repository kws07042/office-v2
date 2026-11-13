# Visual tokens for the 1280 × 720 Ren'Py canvas initialized in options.rpy.
define badge_ink = "#352b2b"
define badge_accent = "#69424b"
define badge_paper = "#f0ebe2"
define badge_rail = "#e5dcd1"
define badge_rule = "#bfb0a8"
define badge_muted = "#625252"
define badge_focus = "#e9d8d5"
define badge_font = "fonts/Pretendard-Regular.otf"

style badge_text is default:
    font badge_font
    size 20
    color badge_ink
style badge_button is button:
    background None
    hover_background Solid(badge_focus)
    selected_background Solid(badge_focus)
    selected_hover_background Solid("#e1cdcc")
    insensitive_background None
    padding (12, 9)
    yminimum 42
    keyboard_focus True
style badge_button_text is badge_text:
    size 18
    hover_color badge_accent
    selected_color badge_accent
    insensitive_color "#766663"
style badge_primary_button is badge_button:
    background Solid(badge_accent)
    hover_background Solid("#4c3039")
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
    selected_hover_background Solid("#4c3039")
    padding (11, 8)
    yminimum 38
style badge_segment_button_text is badge_button_text:
    size 17
    selected_color "#ffffff"
    selected_hover_color "#ffffff"
style badge_scroll is vscrollbar:
    xsize 5
    base_bar Solid(badge_rail)
    thumb Solid("#99817d")
    unscrollable "hide"
style badge_slider is bar:
    xsize 215
    ysize 22
    left_bar Solid(badge_accent, ysize=3)
    right_bar Solid("#b8a6a1", ysize=3)
    thumb Solid(badge_accent, xysize=(7, 18))
    hover_thumb Solid("#4c3039", xysize=(9, 20))
    thumb_align 0.5
    thumb_offset 3
    bar_resizing True

screen badge_shell(active, heading):
    add Solid(badge_paper)
    add Solid("#33292d") xysize (1280, 88)
    add Solid(badge_rule) ypos 87 xysize (1280, 1)
    textbutton "돌아가기" xpos 61 ypos 24 action Return() style "afterwork_page_tab"
    hbox:
        xalign 0.94 ypos 24 spacing 15
        textbutton "설정" action ShowMenu("preferences") selected active == "preferences" style "afterwork_page_tab"
        textbutton "우리의 기록" action ShowMenu("progression_hub") selected active == "progression_hub" style "afterwork_page_tab"
        if not main_menu:
            textbutton "대화 기록" action ShowMenu("history") selected active == "history" style "afterwork_page_tab"
        textbutton "저장·불러오기":
            action ShowMenu("load" if main_menu else "save")
            selected active in ("save", "load")
            style "afterwork_page_tab"
    text heading xpos 71 ypos 167 size 53 font "fonts/GowunDodum-Regular.ttf" color badge_ink
    add Solid(badge_rule) xpos 73 ypos 251 xysize (218, 1)
    add Solid(badge_rule) xpos 356 ypos 135 xysize (1, 505)

screen badge_setting_row(label):
    fixed:
        xysize (786, 61)
        add Solid(badge_rule) ypos 60 xysize (786, 1)
        text label style "badge_text" yalign 0.5
        hbox:
            xalign 1.0 yalign 0.5 spacing 6
            transclude

style afterwork_title_button is button:
    xsize 228
    yminimum 51
    padding (12, 10)
    background Solid("#46383b")
    hover_background Solid("#e7d6c6")
    insensitive_background None
    keyboard_focus True
style afterwork_title_button_text is button_text:
    size 22
    color "#f5ede2"
    hover_color "#302428"
    insensitive_color "#b3a2a3"
style afterwork_title_link is button:
    xsize 228
    yminimum 36
    padding (12, 7)
    background None
    hover_background Solid("#46383b")
    keyboard_focus True
style afterwork_title_link_text is button_text:
    size 18
    color "#dfd1c8"
    hover_color "#ffffff"

style afterwork_page_tab is badge_button:
    hover_background Solid("#59434a")
    selected_background Solid("#59434a")
    selected_hover_background Solid("#654e55")
style afterwork_page_tab_text is badge_button_text:
    color "#eee1d5"
    hover_color "#fff4e7"
    selected_color "#fff4e7"
    selected_hover_color "#fff4e7"
