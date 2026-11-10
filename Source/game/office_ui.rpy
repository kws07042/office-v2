define window_title_art = "gui/badge/title.png"

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
            "choice": ("#202839", "#7487a8"),
            "choice_hover": ("#dce7fa", "#dce7fa"),
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

style office_choice_button is button:
    background office_ui_surface("choice", radius=2)
    hover_background office_ui_surface("choice_hover", radius=2)
    selected_background office_ui_surface("choice_hover", radius=2)
    padding (20, 12)
    yminimum 52
    xfill True
    keyboard_focus True
style office_choice_button_text is button_text:
    font "fonts/Pretendard-Regular.otf"
    size 20
    color "#fff5ed"
    hover_color "#1c315a"
    selected_color "#1c315a"
    outlines []
    text_align 0.0
    xalign 0.0
    line_spacing 4

style office_scrollbar is vscrollbar:
    xsize 6
    base_bar Solid("#e9dbd5")
    thumb Solid("#879bbb")
    unscrollable "hide"
