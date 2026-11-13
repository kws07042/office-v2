default cream_focus = None
default cream_preview_active = False
default cream_preview_mode = None
default cream_preview_reply = None

init -10 python:
    class CreamRoundedPanel(renpy.Displayable):
        """Draw one continuous surface, without nine-slice SVG seams."""
        def __init__(self, fill, edge, radius=22, **kwargs):
            super(CreamRoundedPanel, self).__init__(**kwargs)
            self.fill = fill
            self.edge = edge
            self.radius = radius

        def render(self, width, height, st, at):
            width, height = max(1, int(width)), max(1, int(height))
            # A single SVG sized to the complete widget avoids frame tile joins.
            radius = min(self.radius, max(0, (height - 2) / 2.0))
            markup = '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d"><rect x="1" y="1" width="%d" height="%d" rx="%s" fill="%s" stroke="%s" stroke-width="2"/></svg>' % (width, height, max(0,width-2), max(0,height-2), radius, self.fill, self.edge)
            picture = renpy.display.im.Data(markup.encode("utf-8"), "cream-panel-%d-%d.svg" % (width, height))
            child = renpy.render(picture, width, height, st, at)
            result = renpy.Render(width, height)
            result.blit(child, (0, 0))
            return result

    def cream_round(kind):
        palette = {
            "panel": ("#FFFDFB", "#3B0B22"),
            "button": ("#FFFDFB", "#3B0B22"),
            "hover": ("#F3E7EA", "#B3123F"),
            "accent": ("#B3123F", "#B3123F"),
            "accent_hover": ("#3B0B22", "#3B0B22"),
            "soft": ("#EFE9E3", "#A3959B"),
        }
        return CreamRoundedPanel(*palette[kind], radius=8)

    def cream_speaker_color(who, history=False):
        # Light fills over artwork; darker companions on the cream history panel.
        palette = {
            "강리아": ("#F4D298", "#765019"), "리아": ("#F4D298", "#765019"),
            "백지현": ("#F2A89C", "#923F44"), "지현": ("#F2A89C", "#923F44"),
            "차유진": ("#B6DFCC", "#32634F"), "유진": ("#B6DFCC", "#32634F"),
            "한서윤": ("#D5C6F1", "#654B85"), "서윤": ("#D5C6F1", "#654B85"),
        }
        name = (who or "").split(" · ", 1)[0]
        return palette.get(name, ("#fff8f2", "#864940"))[1 if history else 0]

    def cream_note_speaker(person, event, **kwargs):
        if event == "begin" and person not in ("dohyun", "narrator"):
            renpy.store.cream_focus = person

    def cream_stage_mode():
        if renpy.store.cream_preview_mode:
            return renpy.store.cream_preview_mode
        return "night" if any(word in renpy.store.location for word in ("저녁", "밤", "퇴근 후", "퇴근길")) else "day"

    def cream_ria_visible():
        if not renpy.loadable("images/characters/ria/ui_master_v2.png"):
            return False
        if renpy.store.cream_focus != "ria":
            return False
        if any(word in renpy.store.location for word in ("메시지", "각자의", "연락")):
            return False
        return True

    def cream_yujin_visible():
        if not renpy.loadable("images/characters/yujin/ui_temp_v001.png"):
            return False
        if renpy.store.cream_focus != "yujin":
            return False
        if "도현의 집" in renpy.store.location and "유진" not in renpy.store.location:
            return False
        if any(word in renpy.store.location for word in ("메시지", "각자의", "연락")):
            return False
        return True

    def cream_relation_name(person="ria"):
        if person == "seoyun":
            if renpy.store.dating and renpy.store.active_route == "seoyun":
                return "약속 조율 중" if renpy.store.memory.get("seoyun_conflict") in ("open", "discussing", "agreed_pending_action") else "교제 중"
            return "동료로 지내는 중" if renpy.store.memory.get("seoyun_relationship_declined") or renpy.store.memory.get("seoyun_relationship_closed") else "알아가는 중"
        if person == "jihyun":
            if renpy.store.dating and renpy.store.active_route == "jihyun":
                return "약속 조율 중" if renpy.store.memory.get("jihyun_conflict") in ("open", "agreed_pending_action") else "교제 중"
            return "동료로 지내는 중" if renpy.store.memory.get("jihyun_relationship_declined") or renpy.store.memory.get("jihyun_relationship_closed") else "알아가는 중"
        if person == "yujin":
            return "교제 중" if renpy.store.dating and renpy.store.active_route == "yujin" else ("동료로 지내는 중" if renpy.store.memory.get("yujin_relationship_declined") or renpy.store.memory.get("yujin_relationship_closed") else "알아가는 중")
        if renpy.store.dating and renpy.store.active_route == "ria":
            return "약속 조율 중" if renpy.store.memory.get("ria_conflict") in ("open", "discussing", "agreed") else "교제 중"
        if renpy.store.memory.get("ria_relationship_closed"):
            return "동료로 지내는 중"
        return "알아가는 중"

    def cream_menu_open():
        return any(renpy.get_screen(name) for name in ("save", "load", "history", "preferences", "progression_hub", "progression_cg_view"))

image ria ui bust = DynamicDisplayable(ria_portrait_display)
image yujin ui bust = (Transform(Crop((230, 0, 570, 850), "images/characters/yujin/ui_temp_v001.png"), zoom=1.0) if renpy.loadable("images/characters/yujin/ui_temp_v001.png") else Null())

label cream_preview_start:
    $ cream_preview_active = True
    $ cream_focus = "ria"
    $ active_route = "ria"
    $ speech_informal = True
    $ dating = True
    $ affinity = {"ria": 58, "jihyun": 0, "yujin": 0, "seoyun": 0}
    jump cream_preview_day

label cream_preview_day:
    $ cream_preview_mode = "day"
    $ chapter = "강리아 · 퇴근 전의 약속"
    $ location = "초여름 오후 · 온빛브랜딩"
    scene bg plain
    r "오늘 퇴근하고 시간 있어? 가 보고 싶은 곳이 하나 생겼어~"
    d "있어. 이번에는 나도 같이 고르고 싶어."
    jump cream_preview_choices

label cream_preview_night:
    $ cream_preview_mode = "night"
    $ chapter = "강리아 · 조금 더 같이"
    $ location = "초여름 저녁 · 퇴근 후"
    scene bg plain
    r "오늘은 코스 안 정해도 괜찮지? 그냥 조금 더 같이 있고 싶어서."
    d "응. 오늘은 네 얘기 듣고 싶어. 어디로 갈지는 같이 정하자."
    jump cream_preview_choices

label cream_preview_choices:
    menu:
        "조용한 카페에서 조금 더 이야기하자.":
            $ cream_preview_reply = "cafe"
            r "좋아. 오늘은 내가 고른 자리도 네가 한번 봐 줘~"
        "천천히 걷자. 목적지는 걸으면서 고르고.":
            $ cream_preview_reply = "walk"
            r "좋아! 대신 너무 빨리 걷기 없기. 나 지금 같이 있는 게 좋거든."
        "오늘은 내가 고른 곳도 하나 보여 주고 싶어.":
            $ cream_preview_reply = "suggest"
            r "...그 말은 좀 기대되는데? 오늘은 내가 따라가 볼게~"
    "화면 배치 확인용 장면입니다. 실제 본편의 선택·기억·점수는 바꾸지 않습니다."
    jump cream_preview_choices
