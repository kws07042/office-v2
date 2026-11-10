# Shared presentation only. No relationship, branching, save or message state changes.
init -6 python:
    OFFICE_UI = {
        "text": "#342932", "secondary": "#62545c", "accent": "#864940",
        "canvas": "#f0e6e0", "paper": "#fff8f2", "line": "#d8c5bd",
        "soft": "#f3e6df", "peer": "#ffffff", "mine": "#fee500",
    }

    def office_ui_surface(kind, radius=7):
        palette = {
            "paper": (OFFICE_UI["paper"], OFFICE_UI["line"]),
            "soft": (OFFICE_UI["soft"], OFFICE_UI["soft"]),
            "choice": ("#2a2432", "#554657"),
            "choice_hover": ("#f6e6dc", "#a86d60"),
            "selected": ("#f5ded1", "#c6988b"),
            "peer": (OFFICE_UI["peer"], OFFICE_UI["peer"]),
            "mine": (OFFICE_UI["mine"], OFFICE_UI["mine"]),
        }
        return CreamRoundedPanel(*palette[kind], radius=radius)

    def office_ui_long_choices(items):
        # Conservative fallback: long Korean replies scroll rather than leave the screen.
        import re
        import unicodedata
        for item in items:
            caption = re.sub(r"\{[^}]*\}", "", item.caption)
            units = sum(1.0 if unicodedata.east_asian_width(c) in ("W", "F") else 0.55 for c in caption)
            if units > 48:
                return True
        return False

screen window_menu_backdrop():
    add "gui/window/title.webp" xysize (1280, 720)
    add Solid("#20212acb")

style window_title_button is button:
    background None
    hover_background Solid("#fff5ed99")
    padding (12, 7)
    xsize 228
    keyboard_focus True

style window_title_button_text is button_text:
    size 20
    color "#382b34"
    hover_color "#873f37"

style office_choice_button is button:
    background office_ui_surface("choice")
    hover_background office_ui_surface("choice_hover")
    selected_background office_ui_surface("choice_hover")
    padding (23, 15)
    yminimum 64
    xfill True
    keyboard_focus True
style office_choice_button_text is button_text:
    font "fonts/Pretendard-Regular.otf"
    size 20
    color "#fff5ed"
    hover_color "#392c35"
    selected_color "#392c35"
    outlines []
    text_align 0.0
    xalign 0.0
    line_spacing 4

style office_scrollbar is vscrollbar:
    xsize 6
    base_bar Solid("#e9dbd5")
    thumb Solid("#b38277")
    unscrollable "hide"

style window_setting_section is default:
    size 15
    bold True
    color "#b6a9b8"
style window_setting_label is default:
    size 20
    color "#eee8e6"
style window_setting_button is button:
    background Solid("#2a2b35")
    hover_background Solid("#3c3a46")
    selected_background Solid("#f2ded3")
    selected_hover_background Solid("#ffe8dc")
    padding (13, 8)
    xminimum 64
    keyboard_focus True
style window_setting_button_text is button_text:
    size 17
    xalign 0.5
    color "#ddd7dd"
    hover_color "#ffffff"
    selected_color "#342831"
    selected_hover_color "#342831"
style window_setting_nav is button:
    background None
    hover_background Solid("#34323e")
    padding (5, 8)
    keyboard_focus True
style window_setting_nav_text is button_text:
    size 18
    color "#ece3e5"
    hover_color "#fff6ec"
style window_setting_bar is bar:
    xsize 220
    ysize 18
    left_bar Solid("#d7b0a7", ysize=3)
    right_bar Solid("#504d59", ysize=3)
    thumb_align 0.5
    thumb Solid("#f2ded3", xysize=(5, 18))
    hover_thumb Solid("#ffffff", xysize=(5, 18))
    thumb_offset 2
    bar_resizing True
style window_settings_scroll is office_scrollbar:
    base_bar Solid("#373640")
    thumb Solid("#817583")

style window_record_panel is frame:
    background Solid("#f5f0ed")
style window_record_button is button:
    background None
    hover_background Solid("#e7ddd9")
    padding (14, 11)
    keyboard_focus True
style window_record_button_text is button_text:
    color "#403640"
    hover_color "#402e3c"
