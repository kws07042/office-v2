# 회상 갤러리: 이야기에서 본 장면 CG(persistent.cg_seen)와 기록집 사진(persistent.album)을 다시 본다.
# 메인 화면 "회상 갤러리" 버튼, 또는 게임 중 메뉴에서 연다.

init -1 python:
    GALLERY_TABS = (
        ("ria", "강리아"), ("jihyun", "백지현"), ("yujin", "차유진"), ("seoyun", "한서윤"),
        ("common", "함께"), ("album", "기록집 사진"),
    )
    GALLERY_ORDER = [
        "prologue_hands",
        "ria_r02", "ria_r04", "ria_r07", "ria_r08", "ria_r10", "ria_r11", "ria_r15", "ria_r16", "ria_e01",
        "ria_x01", "ria_x01b", "ria_x02", "ria_sp1", "ria_sp2", "ria_o04",
        "ria_sd_c01", "ria_sd_r02", "ria_sd_r06", "ria_sd_r09",
        "jihyun_r04", "jihyun_r05", "jihyun_r08", "jihyun_r10", "jihyun_r11", "jihyun_r14", "jihyun_r16", "jihyun_r16b", "jihyun_e01",
        "jihyun_x01", "jihyun_x01b", "jihyun_x02", "jihyun_sp1", "jihyun_sp2",
        "jihyun_sd_r06", "jihyun_sd_r12",
        "yujin_r02", "yujin_r04", "yujin_r07", "yujin_r08", "yujin_r10", "yujin_o02", "yujin_r11", "yujin_r16", "yujin_e01",
        "yujin_x01", "yujin_x01b", "yujin_x02", "yujin_sp1", "yujin_sp2",
        "yujin_sd_r02", "yujin_sd_r05", "yujin_sd_r07",
        "seoyun_r02", "seoyun_r04", "seoyun_r05", "seoyun_r08", "seoyun_r10", "seoyun_r11", "seoyun_r13", "seoyun_r16", "seoyun_e01",
        "seoyun_x01", "seoyun_x01b", "seoyun_x02", "seoyun_sp1", "seoyun_sp2",
        "seoyun_sd_c04", "seoyun_sd_r02", "seoyun_sd_r09",
        "common_c05", "common_colleague_ending", "spring_rooftop", "spring_pitch", "common_sd_c05",
    ]
    GALLERY_CHAPTER = {"o04": "포차 뒤 모텔", "x01": "크리스마스", "x01b": "크리스마스 아침", "x02": "1월", "sp1": "특별 장면 1", "sp2": "특별 장면 2",
                       "e01": "결말", "o02": "작은 이야기"}

    # 성인 이벤트 전후 그림(도입·도입 표정·이후 대화)도 본 것부터 갤러리에 넣는다. 이름은 "evt/<히로인>/<파일>".
    EVENT_GALLERY_SLOTS = [("r07_casual", "R07"), ("r12_special", "R12"), ("r15_home", "R15 생활복")]
    EVENT_GALLERY_COSTUMES = {"ria": ("bunny", "nurse", "cheer"), "jihyun": ("bunny", "nurse", "qipao"),
                              "yujin": ("bunny", "nurse", "maid"), "seoyun": ("bunny", "nurse", "police")}
    EVENT_GALLERY_KINDS = [("intro", "도입"), ("intro_shy", "도입 표정"), ("after", "이후")]

    def event_gallery_names(who):
        slots = list(EVENT_GALLERY_SLOTS) + [("r15_cosplay_" + c, "R15 " + COSTUME_NAMES.get(c, c)) for c in EVENT_GALLERY_COSTUMES[who]]
        return ["evt/%s/%s_%s.webp" % (who, s, k) for s, _ in slots for k, _ in EVENT_GALLERY_KINDS]

    def event_gallery_label(name):
        who, f = name[4:].split("/", 1)
        for s, slabel in list(EVENT_GALLERY_SLOTS) + [("r15_cosplay_" + c, "R15 " + COSTUME_NAMES.get(c, c)) for c in EVENT_GALLERY_COSTUMES[who]]:
            for k, klabel in EVENT_GALLERY_KINDS:
                if f == "%s_%s.webp" % (s, k):
                    return slabel + " · " + klabel
        return f

    def gallery_path(name):
        return "images/events/" + name[4:] if name.startswith("evt/") else CG_DIR + name + ".jpg"

    def gallery_mark_event(path):
        if path and path.startswith("images/events/"):
            persistent.cg_seen.add("evt/" + path[len("images/events/"):])

    def gallery_owner(name):
        if name.startswith("evt/"):
            return name[4:].split("/", 1)[0]
        for who in ("ria", "jihyun", "yujin", "seoyun"):
            if name.startswith(who + "_"):
                return who
        return "common"

    def gallery_all():
        names = list(GALLERY_ORDER)
        for who in ("ria", "jihyun", "yujin", "seoyun"):
            names += event_gallery_names(who)
        return names

    def gallery_items(tab):
        return [n for n in gallery_all() if gallery_owner(n) == tab and renpy.loadable(gallery_path(n))]

    def gallery_seen(name):
        return name in (persistent.cg_seen or set())

    SD_TITLES = {
        "ria_sd_c01": "같은 표지를 가리킨 두 사람",
        "ria_sd_r02": "세 번 읽은 임시 휴무",
        "ria_sd_r06": "택시 불빛이 지나간 뒤",
        "ria_sd_r09": "테이블 아래 운동화",
        "jihyun_sd_r06": "처음 데려오신 분",
        "jihyun_sd_r12": "엘리베이터가 열리는 순간",
        "yujin_sd_r02": "제목은 잠깐 가리고",
        "yujin_sd_r05": "자전거 벨이 지나가면",
        "yujin_sd_r07": "내 배경화면을 그린 사람",
        "seoyun_sd_c04": "첫날에 그걸 들켰네",
        "seoyun_sd_r02": "책으로도 못 가린 표정",
        "seoyun_sd_r09": "수건한테 뺏긴 창가",
        "common_sd_c05": "퇴근하고도 기획해야 해?",
    }

    def gallery_label(name):
        if name in SD_TITLES:
            return SD_TITLES[name]
        if name.startswith("evt/"):
            return event_gallery_label(name)
        tail = name.split("_", 1)[1] if gallery_owner(name) != "common" else name
        special = {"prologue_hands": "프롤로그", "common_c05": "넷이 함께한 점심", "common_colleague_ending": "동료 결말",
                   "spring_rooftop": "이듬해 봄 · 옥상", "spring_pitch": "이듬해 봄 · 피칭"}
        if name in special:
            return special[name]
        return GALLERY_CHAPTER.get(tail, tail.upper())

    def gallery_count(tab):
        if tab == "album":
            return len(persistent.album or []), None
        items = gallery_items(tab)
        return sum(1 for n in items if gallery_seen(n)), len(items)

    def gallery_total():
        items = [n for n in gallery_all() if renpy.loadable(gallery_path(n))]
        return sum(1 for n in items if gallery_seen(n)), len(items)

screen gallery():
    tag menu
    default tab = "ria"
    use mg_frame("회상 갤러리", "본 장면은 다시 볼 수 있어요 · 전체 %d / %d" % gallery_total()):
        hbox:
            xpos 40 ypos 104 spacing 8
            for key, name in GALLERY_TABS:
                $ seen, total = gallery_count(key)
                textbutton (name + ("  %d/%d" % (seen, total) if total is not None else "  %d장" % seen)):
                    id "gallery_tab_" + key
                    style "mg_button"
                    selected (tab == key)
                    selected_background Solid("#B3123F")
                    selected_foreground None
                    text_selected_color "#FFFDFB"
                    action SetScreenVariable("tab", key)
        if tab == "album":
            $ photos = list(reversed(persistent.album or []))
            if not photos:
                text "데이트에서 '기록집 사진'을 찍으면 여기에 모입니다." style "mg_text" xpos 40 ypos 170
            else:
                frame:
                    xpos 40 ypos 160 xysize (1220, 460) padding (0, 0) background None
                    viewport:
                        mousewheel True draggable True scrollbars "vertical"
                        vscrollbar_xsize 6 vscrollbar_base_bar Solid("#E1D7CF") vscrollbar_thumb Solid("#B3123F") vscrollbar_unscrollable "hide"
                        vbox:
                            spacing 14
                            for row in range(0, len(photos), 4):
                                hbox:
                                    spacing 14
                                    for i, ph in [(k, photos[k]) for k in range(row, min(row + 4, len(photos)))]:
                                                if ph.get("spot") in PHOTO_SPOTS:
                                                    button:
                                                        id "gallery_photo_%d" % i
                                                        xysize (284, 182) padding (6, 6)
                                                        background Solid("#FFFDFB")
                                                        hover_background Solid("#F6D9DF")
                                                        action Show("gallery_view", kind="photo", items=photos, index=i)
                                                        vbox:
                                                            add Transform(photo_crop(ph["spot"], tuple(ph["cell"])), xysize=(272, 153))
                                                            text ("★" * ph.get("score", 1)) style "mg_small" size 12 font "fonts/Pretendard-Regular.otf"
        else:
            $ items = gallery_items(tab)
            frame:
                xpos 40 ypos 160 xysize (1220, 460) padding (0, 0) background None
                viewport:
                    mousewheel True draggable True scrollbars "vertical"
                    vscrollbar_xsize 6 vscrollbar_base_bar Solid("#E1D7CF") vscrollbar_thumb Solid("#B3123F") vscrollbar_unscrollable "hide"
                    vbox:
                        spacing 14
                        for row in range(0, len(items), 4):
                            hbox:
                                spacing 14
                                for i, name in [(k, items[k]) for k in range(row, min(row + 4, len(items)))]:
                                            $ seen = gallery_seen(name)
                                            button:
                                                id "gallery_cg_" + name
                                                xysize (284, 190) padding (6, 6)
                                                background Solid("#FFFDFB")
                                                hover_background Solid("#F6D9DF")
                                                insensitive_background Solid("#EDE6E1")
                                                sensitive seen
                                                action Show("gallery_view", kind="cg", items=[n for n in items if gallery_seen(n)], index=[n for n in items if gallery_seen(n)].index(name) if seen else 0)
                                                vbox:
                                                    spacing 4
                                                    if seen:
                                                        add Transform(gallery_path(name), xysize=(272, 153))
                                                    else:
                                                        fixed:
                                                            xysize (272, 153)
                                                            add Solid("#D9CDC6")
                                                            text "?" style "mg_title" size 56 color "#FFFDFB" align (0.5, 0.5)
                                                    hbox:
                                                        spacing 6
                                                        text (gallery_label(name) if seen else "아직 보지 않은 장면") style "mg_small" size 14
                                                        if seen and name in SD_TITLES:
                                                            $ code = name.rsplit("_", 1)[1]
                                                            text (("공통 " if code.startswith("c") else "루트 ") + str(int(code[1:])) + "장 · SD") style "mg_small" size 11 yalign 0.5
        textbutton "돌아가기" id "gallery_back" style "mg_button" xpos 40 ypos 640 action Return()
        key "game_menu" action Return()

screen gallery_view(kind, items, index=0):
    modal True
    zorder 200
    default i = index
    $ i = max(0, min(i, len(items) - 1))
    add Solid("#1E1418")
    if kind == "cg":
        add Transform(gallery_path(items[i]), xysize=(1280, 720))
    else:
        $ ph = items[i]
        add Transform(photo_crop(ph["spot"], tuple(ph["cell"])), xysize=(1280, 720))
    button:
        xysize (1280, 720)
        background None
        id "gallery_view_close_area"
        action Hide("gallery_view")
    hbox:
        xalign 0.5 ypos 664 spacing 12
        textbutton "이전" id "gallery_prev" style "mg_button" sensitive (i > 0) action SetScreenVariable("i", i - 1)
        text "%d / %d" % (i + 1, len(items)) style "mg_text" color "#FFFDFB" yalign 0.5
        textbutton "다음" id "gallery_next" style "mg_button" sensitive (i < len(items) - 1) action SetScreenVariable("i", i + 1)
        textbutton "닫기" id "gallery_close" style "mg_button" action Hide("gallery_view")
    key "K_LEFT" action SetScreenVariable("i", max(0, i - 1))
    key "K_RIGHT" action SetScreenVariable("i", min(len(items) - 1, i + 1))
    key "game_menu" action Hide("gallery_view")
