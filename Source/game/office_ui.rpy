# Shared presentation only. No relationship, branching, save or message state changes.
init -6 python:
    OFFICE_UI = {
        "text": "#3d3345", "secondary": "#766b7e", "accent": "#705080",
        "canvas": "#f3eff6", "paper": "#fffdfd", "line": "#e4dce9",
        "soft": "#f5f0f8", "peer": "#f3eef7", "mine": "#e8dfef",
    }

    def office_ui_surface(kind, radius=18):
        palette = {
            "paper": (OFFICE_UI["paper"], OFFICE_UI["line"]),
            "soft": (OFFICE_UI["soft"], OFFICE_UI["soft"]),
            "choice": ("#fffdfa", "#dbcee3"),
            "choice_hover": ("#eee4f5", "#a78ab9"),
            "selected": ("#eae0f2", "#d9c9e4"),
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
    color "#594361"
    hover_color "#51365f"
    selected_color "#51365f"
    outlines []
    text_align 0.0
    xalign 0.0
    line_spacing 4

style office_scrollbar is vscrollbar:
    xsize 6
    base_bar Solid("#eae3ee")
    thumb Solid("#bca4ca")
    unscrollable "hide"

