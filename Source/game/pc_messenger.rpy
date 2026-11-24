# 사내 메신저 'GY톡' (도현의 회사 PC). 업무 시간에만 쓴다.
# 휴대폰(노란 말풍선, 세로 화면)과 구분한다: 가로 PC 창, 흰·회색 바탕, 도현이 보낸 말은 파란 말풍선, 이름 옆에 부서.
# 쓰는 때: 회사 안에서 서로 떨어져 있을 때, 또는 같은 방에 있어도 소리 내어 말할 수 없을 때(회의 중 등).
# 퇴근 후·집·주말 연락은 휴대폰(office_phone.rpy)을 쓴다.
#
# 선택지로 쓰기:  menu (pc=True):  → choice 화면이 이 메신저 모양으로 그려진다.
#   앞의 네 항목은 PC_CONTACTS 순서(리아·지현·유진·서윤)의 사람, 다섯 번째가 있으면 창 아래의 작은 글자 버튼.
#   항목 글자(caption)는 버튼의 alt로 남겨 두어 자동 검사가 예전처럼 글자로 누를 수 있다.

default pc_peek = None

init -1 python:
    PC_CONTACTS = (
        # key, 이름, 부서, 상태 메시지, 상태 색(초록 대화 가능 / 빨강 회의 중 / 노랑 자리 비움)
        ("ria", "강리아", "현장 운영", "현장 체질. 의자 없어도 됨", "#3FB950"),
        ("jihyun", "백지현", "연말 피칭 TF 팀장", "회의 중이면 직접 오세요", "#E5484D"),
        ("yujin", "차유진", "브랜드디자인팀", "(스케치 중)", "#F0B429"),
        ("seoyun", "한서윤", "클라이언트 · 카피", "카피는 짧게, 퇴근은 빠르게", "#3FB950"),
    )
    PC_AVATAR_CROP = (248, 46, 180, 180)

    def pc_avatar(who, size=48):
        path = "images/characters/%s/%s_office_pose01_smile.png" % (who, who)
        if not renpy.loadable(path):
            return Solid("#D9D4DC", xysize=(size, size))
        return Transform(path, crop=PC_AVATAR_CROP, xysize=(size, size))

    def pc_c08_thread(who):
        """C08 퇴근 십 분 전, 그날 업무 대화. (보낸 사람, 글, 시각)"""
        if who == "ria":
            return [("ria", ri("이번 주 현장 사진 공유 폴더에 올렸어!", "이번 주 현장 사진 공유 폴더에 올렸어요!"), "오후 4:12"),
                    ("ria", ri("근데 왜 다 내가 눈 감은 사진이야?", "근데 왜 다 제가 눈 감은 사진이에요?"), "오후 4:12"),
                    ("dohyun", ri("그게 제일 잘 나온 거였어", "그게 제일 잘 나온 거였어요"), "오후 4:15")]
        if who == "jihyun":
            return [("jihyun", "다음 주 검토 안건 두 개로 줄였어. 하나는 도현 씨 안.", "오후 3:40"),
                    ("dohyun", "감사합니다. 근거 자료 더 붙이겠습니다.", "오후 3:41"),
                    ("jihyun", "그건 됐고. 오늘은 일찍 들어가.", "오후 5:32")]
        if who == "yujin":
            return [("yujin", "도현 씨, 아까 화면 시안 괜찮았나요...?", "오후 2:58"),
                    ("yujin", "아 그냥 궁금해서요!! 바쁘시면 안 보셔도 돼요", "오후 2:58"),
                    ("dohyun", "좋았어요. 색 고른 거 유진 씨죠?", "오후 3:20")]
        return [("seoyun", "오늘 클라이언트 전화 세 번. 내 인내심 칭찬해 줘", "오후 5:05"),
                ("dohyun", "대단하세요", "오후 5:06"),
                ("seoyun", "더 길게. 카피 쓰는 사람한테 네 글자는 실례야.", "오후 5:06")]

    def pc_caption_note(caption):
        """'강리아와 다음 약속 잡기 — 친구 같은 …' 에서 줄표 뒤 설명만."""
        return caption.split(" — ", 1)[1] if " — " in caption else ""

    def pc_choice_open():
        if renpy.get_screen("pc_chat_screen"):
            return True
        sc = renpy.get_screen("choice")
        return bool(sc and sc.scope.get("pc"))

    def pc_glass(fill, opacity=1.0, radius=0):
        return silk("glass", fill, opacity, radius)

style pc_text is default:
    font "fonts/Pretendard-Regular.otf"
    color "#222226"
    outlines []
    size 16
style pc_small is pc_text:
    size 13
    color "#8B8B95"
style pc_contact_button is button:
    xsize 330
    padding (16, 12, 14, 12)
    background None
    hover_background Solid("#ECEEF3")
    selected_background Solid("#E3E9F7")
    selected_hover_background Solid("#DCE4F6")

screen pc_messenger_choice(items):
    $ people = [(PC_CONTACTS[i], items[i]) for i in range(min(4, len(items)))]
    $ extra = items[4:]
    $ shown = pc_peek if pc_peek in [row[0] for row, it in people] else (people[0][0][0] if people else "ria")
    $ info = dict((row[0], row) for row in PC_CONTACTS)[shown]
    $ shown_item = dict((row[0], it) for row, it in people).get(shown)

    add Solid("#0E0A1680")

    # 창
    frame:
        id "pc_messenger"
        xalign 0.5 ypos 40 xysize (1000, 572) padding (0, 0)
        background pc_glass("#FFFFFF", 1.0, 8)
        at ((silk_menu_in(0),) if silk_motion_on() else (silk_still,))
        # 제목 줄
        frame:
            xysize (1000, 38) padding (16, 0) background pc_glass("#F3F3F5", 1.0, 8)
            text "GY톡" style "pc_text" size 14 color "#55555E" yalign 0.5
            hbox:
                xalign 1.0 yalign 0.5 spacing 22
                add Solid("#77777F") xysize (11, 1) yalign 0.5
                add silk("glass", "#FFFFFF", 0.0, 1, "#55555E") xysize (11, 11) yalign 0.5
                text "×" style "pc_text" size 18 color "#55555E" yalign 0.5
        add Solid("#E2E2E6") ypos 38 xysize (1000, 1)

        # 친구 목록
        frame:
            xpos 0 ypos 39 xysize (330, 533) padding (0, 0) background Solid("#FAFAFB")
            vbox:
                frame:
                    xpos 14 ypos 14 xysize (302, 34) padding (12, 0) background pc_glass("#EEEEF1", 1.0, 6)
                    text "이름, 부서 검색" style "pc_small" yalign 0.5
                null height 26
                text ("연말 피칭 TF · %d" % len(people)) style "pc_small" xpos 16
                null height 6
                for (key, name, dept, status, dot), item in people:
                    button:
                        id "pc_contact_" + key
                        style "pc_contact_button"
                        selected (shown == key)
                        hovered SetVariable("pc_peek", key)
                        action item.action
                        alt renpy.substitute(item.caption)
                        hbox:
                            spacing 12
                            fixed:
                                xysize (48, 48)
                                add pc_avatar(key, 48)
                                add silk("flat", "#FAFAFB", 8) xysize (16, 16) xpos 36 ypos 36
                                add silk("flat", dot, 6) xysize (12, 12) xpos 38 ypos 38
                            vbox:
                                yalign 0.5 spacing 2
                                hbox:
                                    spacing 6
                                    text name style "pc_text" size 17
                                    text dept style "pc_small" yalign 1.0
                                text status style "pc_small" size 14 color "#6E6E78"
            add Solid("#ECECF0") xpos 329 xysize (1, 533)
            text "나 · 도현 (기획팀)" style "pc_small" xpos 16 ypos 500

        # 대화 창
        frame:
            xpos 331 ypos 39 xysize (669, 533) padding (0, 0) background Solid("#BCC9D8")
            frame:
                xysize (669, 54) padding (20, 0) background Solid("#FFFFFF")
                hbox:
                    yalign 0.5 spacing 10
                    text info[1] style "pc_text" size 18
                    text info[2] style "pc_small" yalign 1.0
            add Solid("#E2E2E6") ypos 54 xysize (669, 1)
            vbox:
                xpos 24 ypos 76 xsize 621 spacing 10
                frame:
                    xalign 0.5 padding (12, 3) background pc_glass("#000000", 0.18, 10)
                    text "오늘" style "pc_small" color "#FFFFFF"
                for sender, body, at_time in pc_c08_thread(shown):
                    if sender == "dohyun":
                        hbox:
                            xalign 1.0 spacing 6
                            text at_time style "pc_small" size 11 color "#4A5866" yalign 1.0
                            frame:
                                padding (14, 9) background pc_glass("#3E6FD8", 1.0, 12)
                                text body style "pc_text" color "#FFFFFF" size 16
                    else:
                        hbox:
                            spacing 6
                            frame:
                                padding (14, 9) background pc_glass("#FFFFFF", 1.0, 12)
                                text body style "pc_text" size 16
                            text at_time style "pc_small" size 11 color "#4A5866" yalign 1.0
            # 아래: 이 사람이 어떤 연애인지 + 안내
            frame:
                xpos 0 ypos 393 xysize (669, 140) padding (22, 16, 22, 14) background Solid("#FFFFFF")
                vbox:
                    spacing 8
                    if shown_item is not None:
                        text pc_caption_note(renpy.substitute(shown_item.caption)) style "pc_text" size 17 color "#2B2B33"
                    text "회사 메신저로 할 말은 아니다. 이름을 누르면 이 사람에게 휴대폰으로 따로 연락한다." style "pc_small" size 14
                    if shown_item is not None:
                        textbutton (info[1] + "에게 휴대폰으로 연락하기"):
                            id "pc_pick_" + shown
                            action shown_item.action
                            alt info[1] + "에게 휴대폰으로 연락하기"
                            padding (16, 8) background pc_glass("#3E6FD8", 1.0, 6) hover_background pc_glass("#2F59B5", 1.0, 6)
                            text_style "pc_text" text_color "#FFFFFF" text_size 15

    # 다섯 번째 이후 항목(동료로 지내기 등)은 창 밖 아래에 글자 버튼으로.
    for n, item in enumerate(extra):
        textbutton renpy.substitute(item.caption):
            id "pc_extra_%d" % n
            xalign 0.5 ypos 626 + n * 30
            action item.action
            background None
            text_style "pc_text" text_size 15 text_color "#FFFFFFB0" text_hover_color "#FFFFFF"

    # 작업 표시줄(타이틀의 바탕화면과 같은 모양)
    frame:
        xpos 0 ypos 664 xysize (1280, 56) padding (10, 8, 18, 8)
        background silk("glass", "#1B1530", 0.88, 0)
        hbox:
            spacing 8 yalign 0.5
            frame:
                xysize (118, 40) padding (0, 0) background silk("startbtn")
                text "퇴근 후{color=#F2C14E},{/color}" font "fonts/Jua-Regular.ttf" size 21 color "#FFFFFF" align (0.5, 0.5)
            frame:
                ysize 40 padding (14, 0) background silk("glass", "#FFFFFF", 0.14, 8)
                text "GY톡" style "desk_tiny" yalign 0.5
        text "오후 5:50" style "desk_tiny" color "#FFFFFF" xalign 1.0 yalign 0.5

# ── 장면 속 사내 메신저 대화 ───────────────────────────────
#   call pc_chat("jihyun", [("jihyun", "근무표 3쪽."), ("dohyun", "확인했어요.")])
# 클릭(또는 스페이스·엔터)할 때마다 한 줄씩 나오고, 다 나온 뒤 한 번 더 누르면 닫힌다.
default pc_chat_n = 1
default pc_chat_test_hold = False

label pc_chat(contact, rows, when="오후"):
    $ pc_chat_n = 1
    $ silk_sfx("phone")
    call screen pc_chat_screen(contact, rows, when)
    return

screen pc_chat_screen(contact, rows, when="오후"):
    modal True
    zorder 40
    $ info = dict((row[0], row) for row in PC_CONTACTS)[contact]
    $ n = max(1, min(pc_chat_n, len(rows)))
    $ more = n < len(rows)
    # 자동 검사의 'advance'는 키를 한 번 보내고 다음 대사를 기다린다. 검사 중에는 한 번에 닫는다
    # (화면을 한 줄씩 보는 검사는 pc_chat_test_hold를 켠다).
    $ step = SetVariable("pc_chat_n", n + 1) if (more and (pc_chat_test_hold or not renpy.is_in_test())) else Return()
    if renpy.is_skipping():
        timer 0.05 action Return()
    add Solid("#0E0A1680")
    button:
        xysize (1280, 720) background None action step
    frame:
        id "pc_chat_window"
        xalign 0.5 ypos 70 xysize (760, 500) padding (0, 0)
        background silk("glass", "#FFFFFF", 1.0, 8)
        at ((silk_menu_in(0),) if silk_motion_on() else (silk_still,))
        frame:
            xysize (760, 38) padding (16, 0) background silk("glass", "#F3F3F5", 1.0, 8)
            text "GY톡" style "pc_text" size 14 color "#55555E" yalign 0.5
            hbox:
                xalign 1.0 yalign 0.5 spacing 22
                add Solid("#77777F") xysize (11, 1) yalign 0.5
                add silk("glass", "#FFFFFF", 0.0, 1, "#55555E") xysize (11, 11) yalign 0.5
                text "×" style "pc_text" size 18 color "#55555E" yalign 0.5
        frame:
            ypos 38 xysize (760, 62) padding (18, 0) background Solid("#FFFFFF")
            hbox:
                yalign 0.5 spacing 12
                fixed:
                    xysize (40, 40)
                    add pc_avatar(contact, 40)
                    add silk("flat", "#FFFFFF", 7) xysize (14, 14) xpos 29 ypos 29
                    add silk("flat", info[4], 5) xysize (10, 10) xpos 31 ypos 31
                vbox:
                    yalign 0.5
                    hbox:
                        spacing 8
                        text info[1] style "pc_text" size 18
                        text info[2] style "pc_small" yalign 1.0
                    text info[3] style "pc_small" size 13
        add Solid("#E2E2E6") ypos 100 xysize (760, 1)
        frame:
            ypos 101 xysize (760, 399) padding (24, 18, 24, 18) background Solid("#BCC9D8")
            vbox:
                xfill True spacing 10 yalign 1.0
                for sender, body in rows[:n]:
                    if sender == "dohyun":
                        frame:
                            xalign 1.0 xmaximum 480 padding (14, 9) background silk("glass", "#3E6FD8", 1.0, 12)
                            text body style "pc_text" color "#FFFFFF" size 17
                    else:
                        frame:
                            xmaximum 480 padding (14, 9) background silk("glass", "#FFFFFF", 1.0, 12)
                            text body style "pc_text" size 17
    textbutton ("다음" if more else "닫기"):
        id "pc_next"
        xalign 0.5 ypos 590
        padding (22, 8) background silk("glass", "#FFFFFF", 0.9, 6) hover_background silk("glass", "#FFFFFF", 1.0, 6)
        text_style "pc_text" text_size 15
        action step
    key "dismiss" action step
