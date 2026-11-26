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
            name = "evt/" + path[len("images/events/"):]
            persistent.cg_seen.add(name)
            diary_mark(name, renpy.store.location)

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

screen gallery(initial_tab="ria", initial_item=None):
    tag menu
    default tab = initial_tab
    default chosen = initial_item
    default photo_index = 0
    $ photos = [ph for ph in reversed(persistent.album or []) if ph.get("spot") in PHOTO_SPOTS and len(ph.get("cell") or []) == 2] if tab == "album" else []
    $ available = gallery_items(tab) if tab != "album" else []
    $ seen = [n for n in available if gallery_seen(n)]
    $ current = chosen if chosen in seen else diary_recent_item(tab, seen)
    $ is_photo = tab == "album"
    $ count = len(photos) if is_photo else len(seen)
    $ idx = min(photo_index, len(photos)-1) if is_photo else (seen.index(current) if current else -1)
    use diary_header
    hbox:
        xpos 877 ypos 22 spacing 6
        textbutton "관계 기록" style "diary_button" action ShowMenu("progression_hub", initial_person=tab if tab in pm.HEROES else "ria")
        textbutton "회상 앨범" style "diary_primary" action NullAction()
        textbutton "돌아가기" id "gallery_back" style "diary_button" action Return()
    hbox:
        xpos 54 ypos 87 spacing 6
        for key, name in GALLERY_TABS:
            textbutton name:
                style "diary_button" id "gallery_tab_" + key
                selected (tab == key)
                action [SetScreenVariable("tab", key), SetScreenVariable("chosen", None), SetScreenVariable("photo_index", 0)]
    fixed:
        xpos 53 ypos 140 xysize (1174, 418)
        add Solid("#322A32")
        if count:
            if is_photo:
                $ ph = photos[idx]
                $ caption = PHOTO_SPOTS[ph["spot"]][2]
                $ image_path = photo_crop(ph["spot"], tuple(ph["cell"]))
                $ scene_info = "기록집 사진　" + "★" * ph.get("score", 1)
            else:
                $ image_path = gallery_path(current)
                $ caption = diary_title(current)
                $ scene_info = (persistent.diary_places or {}).get(current) or diary_caption(current)
            viewport:
                xysize (1174, 418)
                yinitial 0.4
                add Transform(image_path, xysize=(1174, 418), fit="cover")
            add "gui/diary/shade.svg"
            vbox:
                xpos 40 ypos 68 xsize 420 spacing 17
                text DIARY_NAMES[tab] style "diary_small" color "#F4DCCA"
                text caption style "diary_title" size 38 color "#FFFCF4"
                text scene_info style "diary_text" size 18 color "#FCF1E9"
                textbutton "그림만 보기" id "gallery_expand" style "diary_primary" action ([Show("gallery_view", kind="photo", items=photos, index=idx)] if is_photo else [SetScreenVariable("chosen", None), Function(diary_mark, current), Show("gallery_view", kind="cg", items=seen, index=idx)])
        else:
            text ("데이트에서 촬영한 사진이 여기에 모여요." if is_photo else "이야기에서 장면을 만나면 앨범에 담겨요.") style "diary_text" color "#F9EEE6" align (0.5, 0.5)
    add Solid("#FBF2E6") xpos 53 ypos 558 xysize (1174, 106)
    if count:
        $ start = idx // 4 * 4
        hbox:
            xpos 80 ypos 572 spacing 14
            for j in range(start, min(start+4, count)):
                if is_photo:
                    $ thumb = photo_crop(photos[j]["spot"], tuple(photos[j]["cell"]))
                    $ name = PHOTO_SPOTS[photos[j]["spot"]][2]
                    $ select_item = SetScreenVariable("photo_index", j)
                else:
                    $ thumb = gallery_path(seen[j])
                    $ name = diary_title(seen[j])
                    $ select_item = [SetScreenVariable("chosen", seen[j]), Function(diary_mark, seen[j])]
                button:
                    id ("gallery_photo_%d" % j if is_photo else "gallery_cg_" + seen[j])
                    alt name
                    xysize (211, 76) padding (4, 4)
                    background Solid("#FFF9EF") selected_background Solid("#E5C6CB") hover_background Solid("#EBD6D7")
                    selected (idx == j)
                    action select_item
                    hbox:
                        spacing 7
                        add Transform(thumb, xysize=(81, 58), fit="cover") yalign 0.5
                        text name style "diary_text" size 15 xmaximum 112 yalign 0.5
        $ back_idx = max(0, idx-1)
        $ next_idx = min(count-1, idx+1)
        $ prev = SetScreenVariable("photo_index", back_idx) if is_photo else [SetScreenVariable("chosen", seen[back_idx]), Function(diary_mark, seen[back_idx])]
        $ nxt = SetScreenVariable("photo_index", next_idx) if is_photo else [SetScreenVariable("chosen", seen[next_idx]), Function(diary_mark, seen[next_idx])]
        hbox:
            xpos 989 ypos 589 spacing 3
            textbutton "‹" alt "이전 장면" id "album_previous" style "diary_button" sensitive (idx > 0) action prev
            text ("%d / %d" % (idx+1, count)) style "diary_small" yalign 0.5
            textbutton "›" alt "다음 장면" id "album_next" style "diary_button" sensitive (idx+1 < count) action nxt
        if idx > 0:
            key "K_LEFT" action prev
        if idx+1 < count:
            key "K_RIGHT" action nxt
    if not is_photo:
        text ("감상한 장면 %d / %d" % (count, len(available))) style "diary_small" color "#F5E9E1" xpos 56 ypos 681
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
    default show_controls = False
    $ previous = max(0, i - 1)
    $ following = min(len(items) - 1, i + 1)
    $ go_prev = [SetScreenVariable("i", previous), Function(diary_mark, items[previous])] if kind == "cg" else SetScreenVariable("i", previous)
    $ go_next = [SetScreenVariable("i", following), Function(diary_mark, items[following])] if kind == "cg" else SetScreenVariable("i", following)
    button:
        xysize (1280, 720)
        background None
        id "gallery_view_close_area"
        action Hide("gallery_view")
    mousearea:
        ypos 621 xysize (1280, 99)
        hovered SetScreenVariable("show_controls", True)
        unhovered SetScreenVariable("show_controls", False)
    hbox:
        at diary_view_controls(show_controls)
        xalign 0.5 ypos 664 spacing 12
        textbutton "이전" id "gallery_prev" style "mg_button" sensitive (i > 0) action go_prev
        text "%d / %d" % (i + 1, len(items)) style "mg_text" color "#FFFDFB" yalign 0.5
        textbutton "다음" id "gallery_next" style "mg_button" sensitive (i < len(items) - 1) action go_next
        textbutton "닫기" id "gallery_close" style "mg_button" action Hide("gallery_view")
    key "K_LEFT" action go_prev
    key "K_RIGHT" action go_next
    key "game_menu" action Hide("gallery_view")
