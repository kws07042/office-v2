# 주인공 이름: 새 게임을 시작하면 GY브랜딩 사원증에 이름을 써넣는다(한 칸, 한글 1~5자, 성을 넣어도 되고 이름만 써도 된다, ).
# 쓴 그대로 사원증과 대사에 쓴다(예: "공옥순" → "공옥순 씨", "공옥순아").
# 대본은 기본 이름 '도현'으로 쓰여 있고, 화면에 글자가 나가기 직전(config.replace_text)에
# '도현'과 바로 뒤의 조사를 입력한 이름에 맞게 바꾼다. 받침에 따라 이/가, 은/는, 을/를, 아/야, 과/와, 으로/로, 이었/였을 고른다.
# 이름이 '도현'이면 아무것도 바꾸지 않는다(기존 저장 파일과 검사는 그대로).

default mc_name = "도현"
default mc_name_input = ""
default mc_card_message = ""
default mc_card_date = None

init -10 python:
    import re as _mc_re

    MC_DEFAULT = "도현"
    _MC_PATTERN = _mc_re.compile(r"도현(이었|으로|이(?=[^가-힣]|$)|은(?=[^가-힣]|$)|을(?=[^가-힣]|$)|과(?=[^가-힣]|$)|아(?=[^가-힣]|$))?")

    def mc_has_batchim(word):
        ch = (word or MC_DEFAULT)[-1]
        if not ("가" <= ch <= "힣"):
            return True
        return (ord(ch) - 0xAC00) % 28 != 0

    def mc_last_is_rieul(word):
        ch = (word or MC_DEFAULT)[-1]
        return "가" <= ch <= "힣" and (ord(ch) - 0xAC00) % 28 == 8

    def mc_with_josa(name, josa):
        b = mc_has_batchim(name)
        if not josa:
            return name
        if josa == "이었":
            return name + ("이었" if b else "였")
        if josa == "으로":
            return name + ("으로" if b and not mc_last_is_rieul(name) else "로")
        pairs = {"이": ("이", "가"), "은": ("은", "는"), "을": ("을", "를"), "과": ("과", "와"), "아": ("아", "야")}
        a, c = pairs[josa]
        return name + (a if b else c)

    def mc_apply(text):
        name = getattr(renpy.store, "mc_name", MC_DEFAULT) or MC_DEFAULT
        if name == MC_DEFAULT or "도현" not in text:
            return text
        return _MC_PATTERN.sub(lambda m: mc_with_josa(name, m.group(1)), text)

    _mc_prev_replace = config.replace_text
    def _mc_replace_text(text):
        if _mc_prev_replace is not None:
            text = _mc_prev_replace(text)
        return mc_apply(text)
    config.replace_text = _mc_replace_text

    def mc_card_today():
        """사원증 발급일: 플레이어가 새 게임을 시작한 날(컴퓨터 날짜). 한 번 정하면 저장 파일에 남는다."""
        if not renpy.store.mc_card_date:
            import datetime
            renpy.store.mc_card_date = datetime.date.today().strftime("%Y-%m-%d")
        return renpy.store.mc_card_date

    def mc_card_number():
        y, m, d = mc_card_today().split("-")
        return "GY-%s-%s%s" % (y, m, d)

    def mc_valid(name):
        return 1 <= len(name) <= 5 and all("가" <= ch <= "힣" for ch in name)

    def mc_confirm():
        name = (renpy.store.mc_name_input or "").strip()
        if not name:
            renpy.store.mc_card_message = "이름을 적어야 사원증을 받을 수 있어요."
            renpy.restart_interaction()
            return None
        if not mc_valid(name):
            renpy.store.mc_card_message = "이름은 한글 1~5자로 써 주세요. (완성된 글자만)"
            renpy.restart_interaction()
            return None
        renpy.store.mc_name = name
        renpy.store.mc_card_message = ""
        return True

style mc_card_text is default:
    font "fonts/Pretendard-Regular.otf"
    color "#2B2226"
    outlines []

init -9 python:
    def silk_b_cardtop(w, h):
        return ('<defs><linearGradient id="t" x1="0" y1="0" x2="1" y2="1">'
                '<stop offset="0" stop-color="#C8173F"/><stop offset="1" stop-color="#6E1A63"/></linearGradient></defs>'
                '<path d="M18 0 H%d A18 18 0 0 1 %d 18 V%d H0 V18 A18 18 0 0 1 18 0 Z" fill="url(#t)"/>'
                '<path d="M0 %d C %d %d, %d %d, %d %d V%d H0 Z" fill="#FFFFFF" fill-opacity="0.10"/>' %
                (w - 18, w, h, h * 0.62, w * 0.35, h * 0.40, w * 0.7, h * 0.95, w, h * 0.55, h))

    def silk_b_glow(w, h, color):
        return ('<defs><radialGradient id="g"><stop offset="0" stop-color="%s" stop-opacity="0.35"/>'
                '<stop offset="1" stop-color="%s" stop-opacity="0"/></radialGradient></defs>'
                '<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="url(#g)"/>' % (color, color, w / 2, h / 2, w / 2, h / 2))

    MC_BARCODE = [3, 1, 2, 1, 1, 3, 1, 2, 2, 1, 3, 1, 1, 2, 1, 1, 3, 2, 1, 1, 2, 3, 1, 1, 2, 1, 3, 1, 2, 1, 1, 2]

screen employee_card():
    modal True
    zorder 120
    $ ready = bool((mc_name_input or "").strip())
    add Solid("#17111C")
    add silk("glow", "#B3123F", size=(900, 700)) xalign 0.5 yalign 0.55
    text "첫 출근" font "fonts/Jua-Regular.ttf" size 30 color "#F4ECEF" xpos 64 ypos 56
    text "오늘부터 쓸 사원증에 이름을 적어 주세요." style "mc_card_text" size 17 color "#CDBFC6" xpos 64 ypos 100

    # 목걸이 줄과 금속 클립
    add Solid("#22325F") xysize (26, 64) xalign 0.5 ypos 0
    add silk("glass", "#C9CED8", 1.0, 5, "#8A909C") xysize (40, 24) xalign 0.5 ypos 58

    fixed:
        xalign 0.5 ypos 92 xysize (384, 592)
        # 그림자와 카드 몸체
        add silk("glass", "#000000", 0.35, 20) xysize (384, 592) xpos 6 ypos 10
        add silk("glass", "#FBFAF7", 1.0, 20) xysize (384, 592)
        add silk("cardtop", size=(384, 150))
        add silk("flat", "#17111C", 6) xysize (64, 12) xalign 0.5 ypos 16
        vbox:
            xalign 0.5 ypos 40 spacing 0
            text "GY브랜딩" font "fonts/Jua-Regular.ttf" size 30 color "#FFFFFF" xalign 0.5
            text "G Y   B R A N D I N G" style "mc_card_text" size 11 color "#F6D9E1" xalign 0.5
        # 사진: 가운데, 띠 위에 걸쳐 놓는다
        frame:
            xalign 0.5 ypos 104 xysize (196, 240) padding (7, 7)
            background silk("glass", "#FFFFFF", 1.0, 10, "#D9D2D6")
            fixed:
                add Solid("#DCE2EC")
                add silk("flat", "#AEB8C8", 50) xysize (92, 92) xalign 0.5 ypos 38
                add silk("flat", "#AEB8C8", 70) xysize (150, 84) xalign 0.5 ypos 142
        # 이름
        text "NAME" style "mc_card_text" size 11 color "#A0969C" xalign 0.5 ypos 362
        frame:
            id "mc_name_field"
            xalign 0.5 ypos 380 xysize (300, 58) padding (12, 4)
            background None
            input:
                id "mc_name_input_box"
                value VariableInputValue("mc_name_input")
                length 5
                font "fonts/GowunDodum-Regular.ttf" size 38 color "#1E1820"
                xalign 0.5 yalign 0.5
            if not mc_name_input:
                text "이름 입력" font "fonts/GowunDodum-Regular.ttf" size 30 color "#CFC7CC" xalign 0.5 yalign 0.5 xoffset 16
        add Solid(("#B3123F" if ready else "#D9D2D6")) xysize (240, 2) xalign 0.5 ypos 440
        text "기획팀  ·  연말 피칭 TF" style "mc_card_text" size 15 color "#6E6470" xalign 0.5 ypos 456
        # 아래 띠: 사번, 홀로그램, 바코드
        add silk("glass", "#F0ECEE", 1.0, 20) xysize (384, 96) ypos 496
        add Solid("#F0ECEE") xysize (384, 40) ypos 496
        add silk("flat", "#B3123F", 0) xysize (384, 4) ypos 496
        vbox:
            xpos 26 ypos 516 spacing 2
            text "EMPLOYEE NO." style "mc_card_text" size 10 color "#A0969C"
            text mc_card_number() style "mc_card_text" size 15 color "#3A3036"
            text ("발급 " + mc_card_today()) style "mc_card_text" size 11 color "#8A8086"
        add silk("glass", "#E2C46A", 1.0, 4, "#B8963A") xysize (34, 26) xpos 186 ypos 524
        hbox:
            xpos 238 ypos 520 spacing 2
            for wbar in MC_BARCODE:
                add Solid("#2B2226") xysize (wbar, 44)

    text mc_card_message style "mc_card_text" size 16 color "#FF8FA8" xpos 1216 xanchor 1.0 ypos 556 text_align 1.0 xmaximum 330
    textbutton "사원증 받기":
        id "mc_card_confirm"
        xpos 1216 xanchor 1.0 ypos 664 yanchor 1.0
        padding (34, 14)
        background silk("glass", ("#B3123F" if ready else "#4A3E46"), 1.0, 10)
        hover_background silk("glass", ("#8E0E32" if ready else "#4A3E46"), 1.0, 10)
        text_style "mc_card_text" text_color ("#FFFFFF" if ready else "#9A8E95") text_size 21
        action Function(_mc_try_confirm)
    key "K_RETURN" action Function(_mc_try_confirm)
    key "K_KP_ENTER" action Function(_mc_try_confirm)

init -10 python:
    def _mc_try_confirm():
        if mc_confirm():
            return True
        return None

label player_name_card:
    $ mc_name_input = ""
    $ mc_card_date = None
    $ mc_card_today()
    $ mc_card_message = ""
    if renpy.is_in_test() and not getattr(store, "mc_card_in_test", False):
        return
    call screen employee_card
    return
