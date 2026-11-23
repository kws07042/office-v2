default date_outfit = set()
# 히로인 입상: 말하는 히로인을 무대 가운데에 세운다.
# 의상은 장소 문구(location)로, 포즈는 장면마다 하나로, 표정은 대사 내용으로 고른다.
# 대본에서 표정을 직접 정하려면:  $ face("ria", "sad")   (다음 장소가 바뀔 때까지 유지)
#                                  $ face("ria")          (자동으로 되돌림)

default heroine_face_lock = {}
default heroine_face_auto = {}
default heroine_face_lock_location = {}

init -4 python:
    import re as _hs_re
    import zlib as _hs_zlib

    HEROINES = ("ria", "jihyun", "yujin", "seoyun")
    HEROINE_HOME = {
        "ria": ("리아의 집",),
        "jihyun": ("지현의 집",),
        "yujin": ("유진의 집",),
        "seoyun": ("서윤의 집",),
    }
    # 서윤은 작업실에서 지낸다. 아침에만 생활복, 그 밖에는 외출복으로 둔다.
    HEROINE_HOME_MORNING = {"seoyun": ("서윤의 작업실",)}
    # 게임 폴더의 입상 파일을 보고 (인물, 의상, 포즈)별로 있는 표정을 모은다.
    def _hs_scan_sprites():
        found = {}
        for path in renpy.list_files():
            m = _hs_re.match(r"images/characters/(ria|jihyun|yujin|seoyun)/(?:ria|jihyun|yujin|seoyun)_(office|casual|home|winter)_(pose\d\d)_([a-z]+)\.png$", path)
            if m:
                found.setdefault((m.group(1), m.group(2), m.group(3)), set()).add(m.group(4))
        return found
    SPRITE_SET = _hs_scan_sprites()

    # 그 포즈에 없는 표정은 가장 가까운 표정으로 바꾼다.
    SPRITE_FALLBACK = {
        "teary": ("sad", "serious", "neutral"),
        "laugh": ("smile",),
        "surprise": ("blush", "neutral"),
        "pout": ("serious", "neutral"),
        "sad": ("serious", "neutral"),
        "serious": ("neutral",),
        "blush": ("smile",),
        "smile": ("neutral",),
    }
    # 표정 이름은 기존 리아 표정 변수와도 맞춘다.
    RIA_LEGACY_FACE = {"smile": "smile", "shy": "blush", "serious": "serious"}

    WEEKEND_WORDS = ("토요일", "일요일", "휴일", "쉬는 날", "주말")
    WINTER_WORDS = ("12월", "1월", "2월", "크리스마스", "겨울")
    WORKPLACE_WORDS = ("회사", "사무실", "회의", "탕비실", "온빛브랜딩", "클라이언트사", "작업 공간", "공용",
        "협업", "옥상", "비상계단", "복도", "엘리베이터", "현장", "행사장", "출장", "피칭", "검토", "출근",
        "퇴근", "회식", "리허설", "야근", "안내 공간", "숙소", "점심")
    INDOOR_WORK_WORDS = ("사무실", "회의", "탕비실", "작업 공간", "공용", "복도", "협업", "안내 공간")
    HIDDEN_PLACE_WORDS = ("메시지", "각자의", "연락", "전화")

    # 이별·사과·아픔이 분명한 말은 다른 단어보다 먼저 슬픈 얼굴로 둔다("좋아하지만 그만 만나자" 같은 줄).
    STRONG_SAD_WORDS = ("그만 만나", "여기까지 하자", "여기까지 해요", "여기서 멈추자", "헤어지", "끝내자", "끝내겠",
        "아파", "속상", "눈물", "울고", "울었", "미안해", "죄송해요")
    FACE_RULES = (
        ("laugh", ("하하", "푸핫", "ㅋㅋ", "크크", "웃겨", "깔깔")),
        ("blush", ("좋아해", "사랑해", "보고 싶", "설레", "부끄", "키스", "입맞", "안아", "같이 있고 싶", "두근", "예뻐", "귀여")),
        ("surprise", ("어?", "에?", "뭐?", "네?", "헉", "엇", "앗", "?!", "!?", "깜짝", "진짜?", "정말?")),
        ("sad", ("미안", "죄송", "서운", "슬프", "힘들", "무서", "외로", "걱정")),
        ("pout", ("흥", "치사", "몰라", "됐거든", "너무해", "삐졌", "반칙")),
        ("serious", ("확인", "일정", "마감", "자료", "보고", "검토", "결정", "문제", "위험", "설명", "이유", "솔직히", "진지", "결론")),
        ("smile", ("고마", "다행", "좋아", "좋네", "좋았", "재밌", "재미있", "ㅎㅎ", "후후", "맛있", "합격", "최고", "~", "♪", "!")),
    )
    # 갈등·이별 장면(장 제목으로 판별)에서는 "!"·"~"만으로 웃지 않고, 크게 웃음·삐짐도 쓰지 않는다.
    TENSE_CHAPTER_MARKERS = ("R13 ·", "R14 ·", "재미없는 날의 대답", "결론부터 말할게", "제 말로 할게요", "농담 없이 하는 말")
    TENSE_IGNORED_MARKS = ("~", "♪", "!")

    def _hs_place():
        return getattr(renpy.store, "location", "") or ""

    def heroine_has_outfit(who, outfit):
        return any(w == who and o == outfit for (w, o, p) in SPRITE_SET)

    def date_outfit_on(who):
        """R12 데이트: 그날을 위해 고른 옷(special) 입상을 보여 준다. 다음 날 아침이 되면 저절로 꺼진다."""
        renpy.store.date_outfit = set(renpy.store.date_outfit) | {who}

    def date_outfit_off(who):
        renpy.store.date_outfit = set(renpy.store.date_outfit) - {who}

    def heroine_outfit(who, place=None):
        place = _hs_place() if place is None else place
        if who in renpy.store.date_outfit and "아침" not in place and "다음 날" not in place and heroine_has_outfit(who, "special"):
            return "special"
        if any(word in place for word in HEROINE_HOME.get(who, ())):
            return "home"
        own_studio = any(word in place for word in HEROINE_HOME_MORNING.get(who, ()))
        if own_studio and "아침" in place:
            return "home"
        at_work = any(word in place for word in WORKPLACE_WORDS)
        indoor_work = any(word in place for word in INDOOR_WORK_WORDS) or "회사 회의실" in place
        if any(word in place for word in WINTER_WORDS):
            if indoor_work:
                return "office"
            return "casual" if own_studio else "winter"
        if any(word in place for word in WEEKEND_WORDS):
            return "office" if indoor_work or any(word in place for word in ("맡은 행사장", "현장")) else "casual"
        if own_studio:
            return "casual"
        if at_work or "평일" in place or any(day in place for day in ("월요일", "화요일", "수요일", "목요일", "금요일")):
            return "office"
        return "casual"

    def heroine_poses(who, outfit):
        return sorted(pose for (w, o, pose) in SPRITE_SET if w == who and o == outfit) or ["pose01"]

    def heroine_pose(who, outfit, place=None, face=None):
        place = _hs_place() if place is None else place
        poses = heroine_poses(who, outfit)
        # 직접 정한 표정(예: 울먹)이 이 의상의 어느 포즈에만 있으면 그 포즈를 쓴다.
        if face:
            with_face = [p for p in poses if face in SPRITE_SET.get((who, outfit, p), ())]
            if with_face:
                return with_face[0]
        # 같은 장면 안에서는 몸이 바뀌지 않게 장소 문구로 포즈를 하나 고른다(업무복은 절반이 기본 포즈).
        roll = _hs_zlib.crc32((who + "|" + place).encode("utf-8"))
        if outfit == "office" and len(poses) >= 3:
            return ("pose01", "pose01", poses[1], poses[2])[roll % 4]
        return poses[roll % len(poses)]

    def heroine_tense_scene(chapter=None):
        chapter = getattr(renpy.store, "chapter", "") if chapter is None else chapter
        return any(marker in (chapter or "") for marker in TENSE_CHAPTER_MARKERS)

    def heroine_text_face(what, chapter=None):
        text = _hs_re.sub(r"\{[^}]*\}", "", what or "")
        tense = heroine_tense_scene(chapter)
        if any(word in text for word in STRONG_SAD_WORDS) and not text.rstrip().endswith("~"):
            return "sad"
        for face, words in FACE_RULES:
            if tense and face == "smile":
                words = tuple(word for word in words if word not in TENSE_IGNORED_MARKS)
            if any(word in text for word in words):
                if tense and face in ("laugh", "pout"):
                    return "neutral"
                return face
        return "neutral"

    def heroine_resolve_face(face, outfit, pose, who="ria"):
        allowed = SPRITE_SET.get((who, outfit, pose), {"neutral"})
        seen = set()
        while face not in allowed and face not in seen:
            seen.add(face)
            face = next((alt for alt in SPRITE_FALLBACK.get(face, ()) if alt in allowed), SPRITE_FALLBACK.get(face, ("neutral",))[0])
        return face if face in allowed else "neutral"

    def heroine_face(who):
        st = renpy.store
        lock = st.heroine_face_lock.get(who)
        if lock and st.heroine_face_lock_location.get(who) == _hs_place():
            return lock
        if who == "ria" and RIA_LEGACY_FACE.get(getattr(st, "ria_expression", "base")):
            return RIA_LEGACY_FACE[st.ria_expression]
        return st.heroine_face_auto.get(who, "neutral")

    def face(who, expression=None):
        st = renpy.store
        if expression:
            st.heroine_face_lock[who] = expression
            st.heroine_face_lock_location[who] = _hs_place()
        else:
            st.heroine_face_lock.pop(who, None)

    def heroine_sprite_path(who, place=None):
        outfit = heroine_outfit(who, place)
        wanted = heroine_face(who)
        locked = renpy.store.heroine_face_lock.get(who) == wanted
        pose = heroine_pose(who, outfit, place, wanted if locked else None)
        expression = heroine_resolve_face(wanted, outfit, pose, who)
        return "images/characters/%s/%s_%s_%s_%s.png" % (who, who, outfit, pose, expression)

    def heroine_sprite_visible():
        st = renpy.store
        who = st.cream_focus
        if who not in HEROINES or st.dialogue_cg_mode or st.event_cut_active:
            return False
        if art_cg_path():
            return False
        if any(word in _hs_place() for word in HIDDEN_PLACE_WORDS):
            return False
        return renpy.loadable(heroine_sprite_path(who))

    def heroine_note_line(who):
        # 말풍선이 열리기 직전에 불린다. 이번 대사 내용으로 자동 표정을 정한다.
        what = getattr(renpy.store, "_last_raw_what", "") or ""
        renpy.store.heroine_face_auto[who] = heroine_text_face(what)

    # 무대에 놓는 크기: 머리 위가 화면 약 50px, 대화창(ypos 536) 윗선에서 잘라 글씨 뒤로 몸이 비치지 않게 한다.
    # 게임용 사본은 이미 화면 크기(원본의 66%, 676×1014)로 줄여 두어 확대·축소 없이 그린다.
    SPRITE_SIZE = (676, 1014)
    SPRITE_YPOS = 20
    SPRITE_CROP_H = 536 - SPRITE_YPOS

    def heroine_sprite_display(st, at):
        if not heroine_sprite_visible():
            return Null(), None
        path = heroine_sprite_path(renpy.store.cream_focus)
        return Crop((0, 0, SPRITE_SIZE[0], SPRITE_CROP_H), path), None

image heroine stage sprite = DynamicDisplayable(heroine_sprite_display)
