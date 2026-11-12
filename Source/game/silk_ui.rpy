# 실크와 립스틱(E안) UI. 표시만 담당하며 관계·분기·저장·메신저 상태를 바꾸지 않는다.
# 모든 면은 위젯 전체 크기에 맞춘 SVG 한 장으로 그려 조각 경계가 생기지 않게 한다.

init -9 python:
    import hashlib
    import math
    import re

    SILK = {
        "ink": "#3B0B22", "wine": "#B3123F", "paper": "#FFFDFB",
        "mute": "#6E4553", "note": "#4A2A36", "night": "#1B0F14",
        "silk_a": "#F6F2EE", "silk_b": "#E7DFD8", "silk_c": "#E1D7CF",
        "gold": "#F2C14E", "soft": "#EFE9E3", "disabled": "#A3959B",
    }
    SILK_HEART = "M16 28C11 24 2 18 2 10C2 2 12 0 16 7C20 0 30 2 30 10C30 18 21 24 16 28Z"
    SILK_ICONS = {
        "rollback": '<path d="M4 7h7a4 4 0 0 1 0 8H8M4 7l3-3M4 7l3 3"/>',
        "history": '<path d="M4 5h10M4 9h10M4 13h6"/>',
        "phone": '<path d="M3 4h12v8H8l-3 3v-3H3z"/>',
        "auto": '<path d="M6 4l8 5-8 5z"/>',
        "skip": '<path d="M4 4l5 5-5 5M10 4l5 5-5 5"/>',
        "save": '<path d="M4 3h8l2 2v10H4zM6 3v4h5V3M6 15v-4h6v4"/>',
        "load": '<path d="M3 5h4l1.5 2H15v7H3z"/>',
        "prefs": '<path d="M3 6h3M10 6h5M3 12h7M14 12h1"/><circle cx="8" cy="6" r="2"/><circle cx="12" cy="12" r="2"/>',
        "menu": '<path d="M3 9l6-5 6 5M5 8v7h8V8"/>',
    }
    SILK_ENGLISH = {"강리아": "Kang Ria", "백지현": "Baek Jihyun", "차유진": "Cha Yujin", "한서윤": "Han Seoyun"}

    class SilkSVG(renpy.Displayable):
        """builder(width, height, *args)가 돌려준 SVG 본문을 위젯 크기 그대로 그린다."""
        def __init__(self, builder, *args, **kwargs):
            self.fixed_size = kwargs.pop("size", None)
            super(SilkSVG, self).__init__(**kwargs)
            self.builder = builder
            self.args = args

        def render(self, width, height, st, at):
            if self.fixed_size:
                width, height = self.fixed_size
            width, height = max(1, int(width)), max(1, int(height))
            body = self.builder(width, height, *self.args)
            markup = '<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d">%s</svg>' % (width, height, body)
            data = markup.encode("utf-8")
            picture = renpy.display.im.Data(data, "silk-%s.svg" % hashlib.sha1(data).hexdigest())
            child = renpy.render(picture, width, height, st, at)
            result = renpy.Render(width, height)
            result.blit(child, (0, 0))
            return result

    def silk_b_pill(w, h, fill, edge, shadow, radius=None, sx=4, sy=5):
        # 오른쪽·아래로 떨어지는 딱딱한 그림자 + 2px 테두리 면.
        mw, mh = max(4, w - sx), max(4, h - sy)
        r = (mh - 2) / 2.0 if radius is None else min(radius, (mh - 2) / 2.0)
        out = ""
        if shadow:
            out += '<rect x="%d" y="%d" width="%d" height="%d" rx="%s" fill="%s"/>' % (sx + 1, sy + 1, mw - 2, mh - 2, r, shadow)
        out += '<rect x="1" y="1" width="%d" height="%d" rx="%s" fill="%s" stroke="%s" stroke-width="2"/>' % (mw - 2, mh - 2, r, fill, edge)
        return out

    def silk_b_choice(w, h, fill, edge, shadow, mark):
        mh = max(4, h - 5)
        out = silk_b_pill(w, h, fill, edge, shadow)
        if mark == "ring":
            out += '<circle cx="34" cy="%s" r="5" fill="none" stroke="%s" stroke-width="2.5"/>' % (mh / 2.0, SILK["ink"])
        elif mark == "heart":
            out += '<path transform="translate(24 %s) scale(0.625)" fill="%s" d="%s"/>' % (mh / 2.0 - 10, SILK["paper"], SILK_HEART)
        return out

    def silk_b_flat(w, h, fill, radius):
        return '<rect x="0" y="0" width="%d" height="%d" rx="%s" fill="%s"/>' % (w, h, min(radius, h / 2.0), fill)

    def silk_b_dialogue(w, h):
        # 위 가장자리는 반원 레이스, 그 아래는 종이 면, 안쪽에 작은 점 한 줄.
        out = ""
        for x in range(12, w + 12, 24):
            out += '<circle cx="%d" cy="14" r="11.5" fill="%s"/>' % (x, SILK["paper"])
        out += '<rect x="0" y="14" width="%d" height="%d" fill="%s"/>' % (w, max(1, h - 14), SILK["paper"])
        for x in range(108, w - 96, 24):
            out += '<circle cx="%d" cy="36" r="1.7" fill="%s"/>' % (x, SILK["wine"])
        return out

    def silk_b_tag(w, h, fill):
        # 왼쪽으로 10도 기운 이름표와 그림자.
        mw, mh = max(8, w - 5), max(8, h - 6)
        k = mh * math.tan(math.radians(10))
        def poly(dx, dy, color):
            return '<polygon points="%s,%s %s,%s %s,%s %s,%s" fill="%s"/>' % (k + dx, dy, mw + dx, dy, mw - k + dx, mh + dy, dx, mh + dy, color)
        return poly(5, 6, SILK["ink"]) + poly(0, 0, fill)

    def silk_b_badge(w, h):
        d = min(w - 4, h - 5)
        r = d / 2.0
        out = '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (r + 4, r + 5, r, SILK["wine"])
        out += '<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (r, r, r, SILK["ink"])
        out += '<circle cx="%s" cy="%s" r="%s" fill="none" stroke="%s" stroke-width="2"/>' % (r, r, r - 5, SILK["paper"])
        return out

    def silk_b_heart(w, h, full):
        scale = w / 32.0
        if full:
            return '<path transform="scale(%s)" fill="%s" d="%s"/>' % (scale, SILK["wine"], SILK_HEART)
        return '<path transform="scale(%s)" fill="none" stroke="%s" stroke-width="2.6" d="M16 27C11 23 3 18 3 10C3 3 12 1 16 8C20 1 29 3 29 10C29 18 21 23 16 27Z"/>' % (scale, SILK["mute"])

    def silk_b_icon(w, h, name, color):
        return '<g transform="scale(%s)" fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (w / 18.0, color, SILK_ICONS[name])

    def silk_b_next(w, h, color):
        return '<polygon points="0,0 %d,0 %s,%d" fill="%s"/>' % (w, w / 2.0, h, color)

    def silk_b_back(w, h, color):
        return '<path d="M%s %s L%s %s L%s %s" fill="none" stroke="%s" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>' % (w * 0.62, h * 0.2, w * 0.34, h * 0.5, w * 0.62, h * 0.8, color)

    def silk_b_ground(w, h):
        # 118도로 흐르는 실크 주름. 일곱 단의 밝고 어두운 띠.
        angle = math.radians(118 - 90)
        dx, dy = math.cos(angle), math.sin(angle)
        length = abs(w * dx) + abs(h * dy)
        x1, y1 = w / 2.0 - dx * length / 2.0, h / 2.0 - dy * length / 2.0
        x2, y2 = w / 2.0 + dx * length / 2.0, h / 2.0 + dy * length / 2.0
        stops = [(0, "silk_a"), (18, "silk_b"), (34, "silk_a"), (52, "silk_c"), (68, "silk_a"), (84, "silk_b"), (100, "silk_a")]
        out = '<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="%s" y1="%s" x2="%s" y2="%s">' % (x1, y1, x2, y2)
        for offset, key in stops:
            out += '<stop offset="%s" stop-color="%s"/>' % (offset / 100.0, SILK[key])
        out += '</linearGradient></defs><rect x="0" y="0" width="%d" height="%d" fill="url(#g)"/>' % (w, h)
        return out

    def silk_b_band(w, h):
        # 타이틀을 가로지르는 검은 띠와 양쪽 점선. 화면 가운데를 축으로 -7도 기울인다.
        out = '<g transform="rotate(-7 %s %s)">' % (w / 2.0, h / 2.0)
        out += '<rect x="-160" y="%s" width="%d" height="84" fill="%s"/>' % (h / 2.0 - 42, w + 320, SILK["night"])
        for x in range(-148, w + 160, 24):
            out += '<circle cx="%d" cy="%s" r="1.7" fill="%s"/>' % (x, h / 2.0 - 26, SILK["wine"])
            out += '<circle cx="%d" cy="%s" r="1.7" fill="%s"/>' % (x, h / 2.0 + 26, SILK["wine"])
        return out + '</g>'

    def silk_b_lock(w, h):
        return '<g transform="scale(%s)" fill="none" stroke="%s" stroke-width="1.8"><rect x="3" y="10" width="16" height="12" rx="2"/><path d="M6.5 10V7a4.5 4.5 0 0 1 9 0v3"/></g>' % (w / 22.0, "#F3E3DC")

    _silk_cache = {}
    def silk(kind, *args, **kwargs):
        """같은 모양은 한 번만 만든다."""
        key = (kind, args, tuple(sorted(kwargs.items())))
        if key not in _silk_cache:
            _silk_cache[key] = SilkSVG(globals()["silk_b_" + kind], *args, **kwargs)
        return _silk_cache[key]

    def silk_surface(kind):
        """화면 전반에서 쓰는 면. kind: panel, button, hover, soft, focus, chip, chip_on, card, card_on."""
        ink, wine, paper = SILK["ink"], SILK["wine"], SILK["paper"]
        table = {
            "panel": (paper, ink, ink, 22),
            "button": (paper, ink, ink, None),
            "hover": (ink, ink, wine, None),
            "selected": (wine, wine, ink, None),
            "soft": (SILK["soft"], SILK["disabled"], None, None),
            "quiet": (paper, SILK["silk_c"], None, None),
            "card": (paper, ink, ink, 4),
            "card_on": (paper, ink, wine, 4),
            "night": (SILK["night"], SILK["night"], wine, None),
        }
        fill, edge, shadow, radius = table[kind]
        return silk("pill", fill, edge, shadow, radius)

    def silk_choice_surface(state, intimate=False):
        ink, wine, paper = SILK["ink"], SILK["wine"], SILK["paper"]
        if state == "hover":
            return silk("choice", ink, ink, wine, "heart")
        return silk("choice", paper, ink, ink, "ring")

    try:
        _silk_jua = set(renpy.open_file("fonts/Jua-hangul-coverage.txt", encoding="utf-8").read())
    except Exception:
        _silk_jua = set()

    def silk_title_font(text):
        """Jua는 한글 2,367자만 담고 있다. 없는 글자가 섞이면 고운돋움으로 바꾼다."""
        for ch in (text or ""):
            if "가" <= ch <= "힣" and ch not in _silk_jua:
                return "fonts/GowunDodum-Regular.ttf"
            if ch in "·—…":
                return "fonts/GowunDodum-Regular.ttf"
        return "fonts/Jua-Regular.ttf"

    def silk_speaker_key(who):
        return (who or "").split(" · ", 1)[0]

    def silk_tag_color(who):
        # 게임에 정해진 화자 색의 짙은 쪽. 히로인이 아니면 기본 잉크색.
        name = silk_speaker_key(who)
        if name in ("강리아", "리아", "백지현", "지현", "차유진", "유진", "한서윤", "서윤"):
            return cream_speaker_color(who, history=True)
        return SILK["ink"]

    def silk_english(who):
        return SILK_ENGLISH.get(silk_speaker_key(who), "")

    def silk_chapter_parts(chapter):
        """'리아 R07 · 오늘의 속도' -> ('R07', '오늘의 속도'). 장 번호가 없으면 (None, 전체)."""
        text = chapter or ""
        if " · " in text:
            head, tail = text.split(" · ", 1)
            last = head.split(" ")[-1]
            if re.match(r"^[A-Z][0-9]{2}$", last):
                return last, tail
            if re.match(r"^[A-Z_]+[0-9]*$", head):
                return None, tail
        return None, text

    def silk_choice_parts(caption):
        """'같은 마음이라고 답한다 — 친밀한 장면으로 이어짐.' -> (본문, 꼬리표). 그 밖에는 (원문, None)."""
        plain = caption or ""
        if " — " in plain:
            head, tail = plain.rsplit(" — ", 1)
            if "친밀한 장면" in tail and "{" not in tail and "[" not in tail:
                return head, tail.rstrip(".")
        return plain, None

    def silk_has_intimate(items):
        return any(silk_choice_parts(item.caption)[1] for item in items)

transform silk_tilt:
    rotate -7
    rotate_pad False
    subpixel True

image silk ground = SilkSVG(silk_b_ground, size=(1280, 720))

style silk_choice_button is button:
    background silk_choice_surface("idle")
    hover_background silk_choice_surface("hover")
    selected_background silk_choice_surface("hover")
    padding (60, 14, 30, 19)
    yminimum 65
    xfill True
    keyboard_focus True
style silk_choice_text is default:
    font "fonts/Pretendard-Regular.otf"
    size 19
    color "#3B0B22"
    hover_color "#FFFDFB"
    selected_color "#FFFDFB"
    outlines []
    line_spacing 5
    yalign 0.5

style silk_quick_button is button:
    background None
    hover_background silk("flat", "#F3E7EA", 20)
    insensitive_background None
    padding (9, 9, 10, 9)
style silk_quick_text is default:
    font "fonts/Pretendard-Regular.otf"
    size 13
    color "#6E4553"
    hover_color "#3B0B22"
    insensitive_color "#A3959B"
    outlines []
    yalign 0.5

style silk_menu_button is button:
    background silk_surface("quiet")
    hover_background silk_surface("selected")
    selected_background silk_surface("selected")
    padding (10, 10, 14, 15)
    xsize 224
    ysize 77
style silk_menu_text is default:
    font "fonts/Jua-Regular.ttf"
    size 24
    color "#3B0B22"
    hover_color "#FFFDFB"
    selected_color "#FFFDFB"
    outlines []
    xalign 0.5
style silk_menu_caption is default:
    font "fonts/PlayfairDisplay-Italic.ttf"
    size 13
    color "#6E4553"
    hover_color "#F6E4DC"
    selected_color "#F6E4DC"
    outlines []
    xalign 0.5

style silk_small_button is button:
    background silk_surface("button")
    hover_background silk_surface("hover")
    padding (16, 8, 20, 13)
style silk_small_button_text is button_text:
    size 15
