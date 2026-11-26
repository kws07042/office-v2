# 배경과 장면 CG를 무대에 놓는다.
# 배경: 장소 문구(location)에서 배경 23곳 중 하나를 고르고, 시간대(저녁·밤)에 따라 색을 덮는다.
#       아직 저녁·밤 그림이 없어 낮 그림 위에 반투명 색을 얹는다. 그림체 통일 뒤 시간대 그림으로 바꾼다.
# 장면 CG: 대본에서  $ cg("ria_r07")  로 띄운다. 장소가 바뀌거나  $ cg()  를 부르면 내려간다.

default scene_cg = None
default scene_cg_location = None
default sd_cut_prev = None
default persistent.cg_seen = set()

init -3 python:
    BG_DIR = "images/bg/"
    CG_DIR = "images/cg/"

    # 위에서부터 먼저 맞는 것을 쓴다. 장소 부분(마지막 "·" 뒤)만 본다.
    BG_RULES = (
        ("bg_motel", ("모텔", "숙소")),
        ("bg_dohyun_room", ("메시지", "각자의 집", "전화", "연락", "도현의 집")),
        ("bg_street", ("집 앞", "작업실 앞")),
        ("bg_ria_home", ("리아의 집",)),
        ("bg_jihyun_home", ("지현의 집", "조립품")),
        ("bg_yujin_home", ("유진의 집",)),
        ("bg_seoyun_studio", ("서윤의 작업실", "서윤의 집")),
        ("bg_restaurant", ("식당", "밥집", "포차", "국밥", "고깃집", "회식")),
        ("bg_popup", ("팝업", "행사장", "현장")),
        ("bg_corridor", ("엘리베이터", "복도")),
        ("bg_client_hall", ("대회의실", "클라이언트사 회의실", "클라이언트사 로비")),
        ("bg_laundry", ("세탁",)),
        ("bg_train", ("기차", "지하철")),
        ("bg_gallery", ("전시",)),
        ("bg_street", ("서점 앞", "서점 맞은편", "화방")),
        ("bg_bookcafe", ("북카페", "서점", "헌책방")),
        ("bg_cafe", ("카페", "찻집")),
        ("bg_rooftop", ("옥상",)),
        ("bg_stairs", ("비상계단",)),
        ("bg_pantry", ("탕비실",)),
        ("bg_meeting", ("회의", "검토", "리허설")),
        ("bg_company_front", ("회사 앞", "GY브랜딩 앞", "횡단보도", "정류장")),
        ("bg_park", ("공원", "산책길", "벤치", "강변", "다리")),
        ("bg_street", ("퇴근길", "출근길", "역 앞", "골목", "샛길", "길", "거리", "앞", "부품 가게")),
        ("bg_office", ("사무실", "작업 공간", "공용", "테이블", "GY브랜딩", "회사", "안내 공간", "자리", "점심")),
    )
    NIGHT_WORDS = ("밤", "깊은", "자정", "열한 시", "열 시", "아홉 시")
    EVENING_WORDS = ("저녁", "퇴근", "일곱 시", "여섯 시", "해 질")

    def art_place(location=None):
        location = getattr(renpy.store, "location", "") if location is None else location
        return (location or "").split("·")[-1]

    def art_bg_name(location=None):
        place = art_place(location)
        full = getattr(renpy.store, "location", "") if location is None else (location or "")
        for text in (place, full):
            for name, words in BG_RULES:
                if any(word in text for word in words):
                    return name
        return None

    def art_time(location=None):
        location = getattr(renpy.store, "location", "") if location is None else location
        location = location or ""
        if any(word in location for word in NIGHT_WORDS):
            return "night"
        if any(word in location for word in EVENING_WORDS):
            return "evening"
        return "day"

    def art_bg_path(location=None):
        name = art_bg_name(location)
        if not name:
            return None
        path = BG_DIR + name + ".jpg"
        return path if renpy.loadable(path) else None

    def cg(name=None, record=True):
        st = renpy.store
        if name:
            path = CG_DIR + name + ".jpg"
            if not renpy.loadable(path):
                st.scene_cg = None
                return
            st.scene_cg = name
            st.scene_cg_location = st.location
            persistent.cg_seen.add(name)
            if record:
                diary_mark(name, st.location)
        else:
            st.scene_cg = None

    # SD 코믹 컷: 장면 CG 위에 잠깐 띄웠다가, 끝나면 원래 장면 CG로 돌아간다.
    def sd_cut(name):
        st = renpy.store
        st.sd_cut_prev = st.scene_cg if art_cg_path() else None
        cg(name)

    def sd_cut_end():
        st = renpy.store
        prev = getattr(st, "sd_cut_prev", None)
        st.sd_cut_prev = None
        cg(prev, record=False)

    def art_cg_path():
        st = renpy.store
        if not st.scene_cg:
            return None
        if st.scene_cg_location != st.location:
            st.scene_cg = None
            return None
        return CG_DIR + st.scene_cg + ".jpg"

    def art_stage_display(st_time, at):
        cg_path = art_cg_path()
        if cg_path:
            return Image(cg_path), None
        bg = art_bg_path()
        if not bg:
            return Null(), None
        time = art_time()
        layers = [Image(bg)]
        if time == "evening":
            layers.append(Solid("#ff9a5229"))
            layers.append(Solid("#3b1f4a2e"))
        elif time == "night":
            layers.append(Solid("#0d163885"))
        return Fixed(*layers, xysize=(1280, 720)), None

    def art_stage_has_picture():
        return bool(art_cg_path() or art_bg_path())

image art stage = DynamicDisplayable(art_stage_display)
