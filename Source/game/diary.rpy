# '우리의 기록'의 책갈피와 앨범 열람 위치. 기존 해금 데이터는 gallery_seen이 담당한다.
default persistent.diary_recent = {}
default persistent.diary_lines = {}
default persistent.diary_places = {}

init python:
    DIARY_ROLES = {"ria": "현장 운영", "jihyun": "연말 피칭 TF 팀장", "yujin": "브랜드디자인팀", "seoyun": "브랜드전략팀"}
    DIARY_NAMES = dict(GALLERY_TABS)

    def diary_mark(name, place=None):
        persistent.diary_recent[gallery_owner(name)] = name
        if place:
            persistent.diary_places[name] = place

    def diary_recent_item(person, seen):
        latest = (persistent.diary_recent or {}).get(person)
        return latest if latest in seen else (seen[0] if seen else None)

    def diary_title(name):
        if name.endswith(("_sp1", "_sp2")):
            return SPECIAL_TITLES[gallery_owner(name)][int(name[-1]) - 1]
        node = PROGRESSION_NODE_MAP.get(name)
        return node["title"].partition(" · ")[-1] if node else gallery_label(name)

    def diary_caption(name):
        if name in SD_TITLES:
            code = name.rsplit("_", 1)[1]
            return ("공통 " if code[0] == "c" else "루트 ") + str(int(code[1:])) + "장 · SD"
        if name.startswith("evt/"):
            return "이벤트 회상"
        if name.endswith(("_sp1", "_sp2")):
            return "특별 장면 " + name[-1]
        return PROGRESSION_NODE_MAP[name]["title"].partition(" · ")[0] if name in PROGRESSION_NODE_MAP else "장면 CG"

style diary_text is default:
    font "fonts/Pretendard-Regular.otf"
    color "#3C3036"
    size 19
    outlines []

style diary_title is diary_text:
    font "fonts/GowunDodum-Regular.ttf"
    bold True
    size 34

style diary_small is diary_text:
    size 16
    color "#705D62"

style diary_button is button:
    background Solid("#F5ECDE")
    selected_background Solid("#793950")
    hover_background Solid("#673249")
    padding (13, 7)

style diary_button_text is diary_text:
    size 16
    hover_color "#FFFFFF"
    selected_color "#FFFFFF"

style diary_primary is diary_button:
    background Solid("#793950")

style diary_primary_text is diary_button_text:
    color "#FFF9F0"

screen diary_header():
    add Transform("images/bg/bg_office.jpg", xysize=(1280, 720), blur=9)
    add Solid("#241C2AD9")
    text "퇴근 후{color=#F3A58F},{/color} 우리" style "diary_title" color "#FFF4E7" xpos 65 ypos 19

screen diary_record(person):
    $ seen = [n for n in gallery_items(person) if gallery_seen(n)]
    $ recent = diary_recent_item(person, seen)
    $ latest = (persistent.diary_recent or {}).get(person) == recent
    $ quote = (persistent.diary_lines or {}).get(person)
    use diary_header
    hbox:
        xpos 905 ypos 22 spacing 6
        textbutton "관계 기록" style "diary_primary" action NullAction()
        textbutton "회상 앨범" style "diary_button" id "diary_album" action ShowMenu("gallery", initial_tab=person)
        textbutton "돌아가기" style "diary_button" action Return()
    add "gui/diary/book.svg"
    vbox:
        xpos 1173 ypos 145 spacing 5
        for who in pm.HEROES:
            textbutton "\n".join(DIARY_NAMES[who]):
                id "diary_tab_" + who
                style "diary_button" xsize 65 ysize 90 text_align 0.5 text_size 17
                alt DIARY_NAMES[who]
                selected (person == who)
                action SetScreenVariable("person", who)
    text "우리의 기록" style "diary_small" xpos 101 ypos 160
    add Solid("#CAB9AA") xpos 203 ypos 173 xysize (348, 1)
    add mg_face_thumb(person) xpos 99 ypos 204
    text DIARY_NAMES[person] style "diary_title" size 43 xpos 211 ypos 203
    text DIARY_ROLES[person] style "diary_small" xpos 212 ypos 263
    add Solid("#BB858C") xpos 101 ypos 315 xysize (3, 81)
    text ("“" + quote + "”" if quote else "둘이 나눈 말이 여기에 남아요.") style "diary_title" size 25 xpos 126 ypos 328 xmaximum 424
    add Solid("#D7C6B9") xpos 101 ypos 416 xysize (449, 1)
    if main_menu:
        text "현재 관계는 저장을 불러오면 볼 수 있어요." style "diary_small" xpos 101 ypos 445
    else:
        text ("♥  " + relation_stage(person)) style "diary_title" size 22 color "#80354D" xpos 101 ypos 437
        textbutton "관계 수치" style "diary_button" xpos 444 ypos 436 action SetScreenVariable("tab", "details")
    add Solid("#D7C6B9") xpos 101 ypos 487 xysize (449, 1)
    text "함께한 특별 장면" style "diary_small" xpos 101 ypos 507
    vbox:
        xpos 101 ypos 542 spacing 7
        $ unlocked = [n for n in (1, 2) if getattr(persistent, "special_%s_%d" % (person, n), False)]
        for n in unlocked:
            text SPECIAL_TITLES[person][n-1] style "diary_text" size 18
        if len(unlocked) < 2:
            text ("아직 만나지 않은 특별 장면 · %d개" % (2 - len(unlocked))) style "diary_small"
    text ("최근에 본 장면" if recent and latest else "기억에 남은 장면") style "diary_small" xpos 650 ypos 161
    if recent:
        $ open_album = ShowMenu("gallery", initial_tab=person, initial_item=recent)
        button:
            id "diary_photo"
            xpos 654 ypos 218 xysize (476, 275) padding (7, 7)
            background Solid("#FFFDF6") hover_background Solid("#EFC6BD")
            at diary_photo_tilt
            action open_album
            add gallery_path(recent) xysize (462, 260) fit "contain" align (0.5, 0.5)
        add Transform(Solid("#DDCB9BC9", xysize=(63, 17)), rotate=22) xpos 647 ypos 214
        add Transform(Solid("#DDCB9BC9", xysize=(62, 17)), rotate=20) xpos 1085 ypos 467
        vbox:
            xcenter 890 ypos 510 xsize 480 spacing 5
            text diary_title(recent) style "diary_title" size 25 xalign 0.5 text_align 0.5
            text ((persistent.diary_places or {}).get(recent) or diary_caption(recent)) style "diary_small" xalign 0.5
            textbutton "사진 다시 보기　›" style "diary_primary" xalign 0.5 action open_album
    else:
        frame:
            xpos 660 ypos 230 xysize (452, 247) padding (24, 24) background Solid("#EFE5D8")
            text "이야기에서 만난 장면이 이곳에 담겨요." style "diary_small" align (0.5, 0.5)
    hbox:
        xpos 65 ypos 674 spacing 8
        for target, label_text in (("story", "이야기"), ("gallery", "CG 수집 · 재생"), ("endings", "결말"), ("details", "기록 설정")):
            textbutton label_text style "diary_button" action SetScreenVariable("tab", target)
    key "K_LEFT" action SetScreenVariable("person", pm.HEROES[(pm.HEROES.index(person)-1) % len(pm.HEROES)])
    key "K_RIGHT" action SetScreenVariable("person", pm.HEROES[(pm.HEROES.index(person)+1) % len(pm.HEROES)])
    key "game_menu" action Return()

transform diary_photo_tilt:
    rotate -2
    rotate_pad False

transform diary_view_controls(visible):
    alpha (1.0 if visible else 0.0)
