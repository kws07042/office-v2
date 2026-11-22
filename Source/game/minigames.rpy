# 미니게임 5종. 대본 속 장면을 직접 해 보는 짧은 놀이(각 1~3분).
#   sign   안내판 옮기기        리아  C01 첫 출근 행사장
#   cards  빵·차 카드게임       지현  R11 거실
#   photo  기록집 사진          공통  데이트에서 도현의 사진
#   trim   한 줄로 줄이기       서윤  C04 카피 요청
#   spot   어디가 달라졌어요?   유진  C03 시안 비교
# 이야기 중에는 시작 전에 할지 묻고, 건너뛰어도 이야기는 그대로 이어진다(성공하면 마음 +1, 반응 한 줄).
# 자동 검사(테스트) 중이거나 스킵 중이거나 설정에서 끄면 나오지 않는다. 메인 화면 "미니게임"에서 다시 할 수 있다.

default persistent.minigames_on = True
default persistent.minigame_best = {}
default persistent.album = []
default mg_result = None
default persistent.mg_pending = None
default mg_pick = None
default mg_dir = "→"
default mg_cell = (1, 1)
default mg_off = set()

init -2 python:
    MG_INFO = {
        "sign": ("안내판 옮기기", "리아", "손님 줄이 갈라지지 않게, 화살표 안내판을 놓을 자리와 방향을 정하세요."),
        "cards": ("빵·차 카드게임", "지현", "빵과 어울리는 차를 짝지어 모으세요. 다섯 장씩 가져가고, 점수가 높은 쪽이 이깁니다."),
        "photo": ("기록집 사진", "도현", "뷰파인더를 옮겨 오늘의 한 장을 고르세요. 기록집에 남습니다."),
        "trim": ("한 줄로 줄이기", "서윤", "꼭 남겨야 할 말은 지키고, 글자 수 안으로 줄이세요."),
        "spot": ("어디가 달라졌어요?", "유진", "왼쪽 원래 시안과 오른쪽 수정 시안에서 달라진 곳 세 군데를 찾으세요."),
    }

    def mg_should_offer():
        return bool(persistent.minigames_on) and not renpy.is_in_test() and not renpy.is_skipping()

    def mg_record(game, score):
        best = dict(persistent.minigame_best or {})
        best[game] = max(best.get(game, 0), score)
        persistent.minigame_best = best

    # ---------- 1. 안내판 옮기기 ----------
    # 6x4 칸. E 입구, B 부스, P 기둥, 숫자 = 안내판을 놓을 수 있는 자리.
    SIGN_ROUNDS = [
        dict(rows=["E..1.B", "..P...", "2.....", "...3.."], answer=("1", "→"),
             hints={"2": "거긴 입구 바로 옆이라 줄 서는 사람한테 가려.", "3": "거기선 반대쪽 줄에서도 보여. 아까 그 문제야!", "1": "자리는 맞아! 방향만 다시 보자."},
             goal="입구로 들어온 손님이 처음 보는 곳에, 부스 쪽을 가리키게."),
        dict(rows=["......", "E.P1.B", "..2...", "3....."], answer=("2", "↗\uFE0E"),
             hints={"1": "기둥 바로 뒤라 입구에선 안 보여.", "3": "거긴 출구 쪽이야. 들어오는 사람은 못 봐.", "2": "자리는 좋아. 부스가 어느 쪽인지 다시 봐 봐."},
             goal="기둥에 가리지 않게. 부스는 오른쪽 위."),
        dict(rows=["B....E", "..P...", ".1..2.", "....3."], answer=("2", "←"),
             hints={"1": "너무 안쪽이라 손님이 이미 헤매고 난 뒤야.", "3": "거긴 바닥 짐 옆이라 사람들이 안 지나가.", "2": "자리 정답! 입구가 오른쪽이니까 방향은..."},
             goal="이번엔 입구가 오른쪽. 처음 갈림길에서 바로 보이게."),
    ]
    SIGN_DIRS = ["←", "↑", "→", "↓", "↗\uFE0E", "↖\uFE0E"]

    # ---------- 2. 빵·차 카드게임 ----------
    BREADS = ["크루아상", "소금빵", "메론빵"]
    TEAS = ["홍차", "녹차", "유자차"]
    PAIRS = {"크루아상": "홍차", "소금빵": "녹차", "메론빵": "유자차"}
    CARD_ART = {"크루아상": "croissant", "소금빵": "saltbread", "메론빵": "melonbread", "홍차": "blacktea", "녹차": "greentea", "유자차": "yuzutea"}

    def cards_score(hand):
        score = 0
        kinds = 0
        for bread, tea in PAIRS.items():
            n = min(hand.count(bread), hand.count(tea))
            score += 3 * n
            if n:
                kinds += 1
        if kinds == 3:
            score += 2
        return score

    def cards_new_game(seed=None):
        rnd = renpy.random.Random(seed)
        deck = (BREADS + TEAS) * 3
        rnd.shuffle(deck)
        return dict(deck=deck[4:], market=deck[:4], me=[], rival=[], turn="me", log="먼저 가져가. 손님이니까.", rnd=rnd)

    def cards_rival_pick(g):
        best = None
        for i, c in enumerate(g["market"]):
            gain = cards_score(g["rival"] + [c]) - cards_score(g["rival"])
            # 상대에게 필요한 카드를 막는 값도 조금 본다.
            block = cards_score(g["me"] + [c]) - cards_score(g["me"])
            value = gain * 2 + block + g["rnd"].random() * 0.5
            if best is None or value > best[0]:
                best = (value, i)
        return best[1]

    def cards_take(g, i, who):
        card = g["market"].pop(i)
        g[who].append(card)
        if g["deck"]:
            g["market"].append(g["deck"].pop(0))
        return card

    class CardsPick(Action):
        def __init__(self, g, i):
            self.g, self.i = g, i
        def __call__(self):
            g = self.g
            if g["turn"] != "me" or len(g["me"]) >= 5:
                return
            mine = cards_take(g, self.i, "me")
            if len(g["rival"]) < 5:
                j = cards_rival_pick(g)
                theirs = cards_take(g, j, "rival")
                g["log"] = "%s 가져갔네. 나는 %s." % (mine, theirs)
            if len(g["me"]) >= 5:
                g["turn"] = "done"
            renpy.restart_interaction()

    # ---------- 3. 기록집 사진 ----------
    PHOTO_SPOTS = {
        "ria_r15": ("images/bg/bg_park.jpg", (0, 1), "긴 의자에 길게 드리운 빛"),
        "jihyun_r05": ("images/bg/bg_cafe.jpg", (0, 0), "창가로 들어오는 오후 빛"),
        "yujin_r07": ("images/bg/bg_bookcafe.jpg", (1, 0), "책장 사이로 떨어지는 조명"),
        "seoyun_r11": ("images/bg/bg_park.jpg", (2, 0), "강 건너 다리와 하늘"),
        "free": ("images/bg/bg_street.jpg", (1, 1), "퇴근길 가로수 사이"),
    }

    def photo_score(spot, cell):
        tx, ty = PHOTO_SPOTS[spot][1]
        d = abs(tx - cell[0]) + abs(ty - cell[1])
        return 3 if d == 0 else (2 if d == 1 else 1)

    def photo_crop(spot, cell):
        path = PHOTO_SPOTS[spot][0]
        x, y = cell
        return Crop((x * 320, y * 180, 640, 360), path)

    # ---------- 4. 한 줄로 줄이기 ----------
    TRIM_ROUNDS = [
        dict(chips=["이번 주말", "오전 10시부터", "시청 앞 광장에서", "누구나 부담 없이", "즐길 수 있는", "향기 체험 팝업이", "드디어", "열립니다"],
             keep=["이번 주말", "시청 앞 광장에서", "향기 체험 팝업이", "열립니다"], limit=26,
             brief="언제·어디서·무엇은 빼지 말고, 26자 안으로."),
        dict(chips=["바쁜 하루 끝에", "오늘도 정말", "고생 많으셨어요.", "따뜻한 차 한 잔은", "저희가", "준비해 둘게요."],
             keep=["고생 많으셨어요.", "따뜻한 차 한 잔은", "준비해 둘게요."], limit=24,
             brief="인사와 약속은 남기고, 24자 안으로."),
    ]

    def trim_text(chips, off):
        return " ".join(c for c in chips if c not in off)

    def trim_len(chips, off):
        return len(trim_text(chips, off).replace(" ", ""))

    # ---------- 5. 어디가 달라졌어요? ----------
    # 블록: (이름, x, y, w, h)  /  원래·수정 시안의 내용
    SPOT_BLOCKS = [
        ("head", 30, 30, 330, 90), ("sub", 30, 130, 330, 40), ("img", 30, 180, 200, 170),
        ("arrow", 245, 180, 115, 80), ("date", 245, 270, 115, 80), ("logo", 30, 360, 330, 40),
    ]
    SPOT_ORIG = {"head": ("퇴근길 향기", "#B3123F", 40), "sub": ("오늘의 끝에 한 모금", "#3B0B22", 20), "img": ("병 사진", "#F2C14E", 22),
                 "arrow": ("→", "#3B0B22", 44), "date": ("11.24\n토", "#3B0B22", 22), "logo": ("ONBIT", "#6E4553", 18)}
    SPOT_EDIT = dict(SPOT_ORIG, head=("퇴근길 향기", "#2F6E8F", 40), arrow=("←", "#3B0B22", 44), date=("11.24", "#3B0B22", 22))
    SPOT_ANSWERS = {"head", "arrow", "date"}
    # 그림 시안 2쌍. 칸 번호(3x4, 왼쪽 위부터 1~12)가 어느 '달라진 곳'에 속하는지.
    SPOT_PAIRS = [
        dict(img="spot_pair1", groups={1: "title", 2: "title", 3: "title", 8: "arrow", 7: "leaf", 10: "leaf"}),
        dict(img="spot_pair2", groups={5: "steam", 6: "candle", 10: "time"}),
    ]
    def spot_art_ready():
        return all(renpy.loadable("images/minigame/%s_%s.png" % (p["img"], k)) for p in SPOT_PAIRS for k in ("orig", "edit"))

    # ---------- 공통: 함께하는 히로인과 무대 ----------
    # 놀이마다 그 장면의 히로인이 오른쪽에 서서 말풍선으로 반응한다(정답이면 웃고, 틀리면 시무룩).
    MG_HOST = {
        "hub": (None, "images/bg/bg_office.jpg"),
        "sign": ("ria", "images/bg/bg_popup.jpg"),
        "cards": ("jihyun", "images/bg/bg_jihyun_home.jpg"),
        "photo": (None, "images/bg/bg_street.jpg"),
        "trim": ("seoyun", "images/bg/bg_office.jpg"),
        "spot": ("yujin", "images/bg/bg_meeting.jpg"),
    }
    MG_NAME = {"ria": "리아", "jihyun": "지현", "yujin": "유진", "seoyun": "서윤"}
    MG_HELLO = {
        "sign": "입구로 들어온 손님 눈으로 봐 줘! 처음 보이는 데가 어디일까?",
        "cards": "손님이니까 먼저 골라. ...봐주진 않을 거야.",
        "trim": "꼭 남길 말만 남기는 게 요령이야~ 나머진 과감하게!",
        "spot": "저, 저도 처음엔 한참 찾았어요. 천천히 보세요.",
    }
    # 화살표 글자는 윈도에서 파란 그림 글자로 바뀌므로, 같은 → 를 돌려서 그린다.
    MG_ARROW_ANGLE = {"←": 180, "↑": -90, "→": 0, "↓": 90, "↗︎": -45, "↖︎": -135}

    def mg_arrow(d, size=26, color="#3B0B22"):
        return Transform(Text("→", font="fonts/Pretendard-Regular.otf", size=size, color=color, outlines=[]), rotate=MG_ARROW_ANGLE.get(d, 0), rotate_pad=False)

    def mg_portrait(who, face="neutral"):
        face = heroine_resolve_face(face, "office", "pose01", who)
        return "images/characters/%s/%s_office_pose01_%s.png" % (who, who, face)

    def mg_face_thumb(who):
        return Transform(Crop((218, 0, 240, 240), mg_portrait(who, "smile")), xysize=(96, 96))

    def mg_stars(score, top):
        if not top:
            return 1
        ratio = float(score) / top
        return 3 if ratio >= 0.85 else (2 if ratio >= 0.5 else 1)

# ---------------- 공통 화면 ----------------

style mg_title is default:
    font "fonts/GowunDodum-Regular.ttf"
    bold True
    size 34
    color "#3B0B22"
style mg_text is default:
    font "fonts/GowunDodum-Regular.ttf"
    size 20
    color "#3B0B22"
style mg_small is mg_text:
    size 16
    color "#6E4553"
style mg_button is default:
    background Frame(Solid("#FFFDFB"), 0, 0)
    hover_background Solid("#F6D9DF")
    insensitive_background Solid("#EDE6E1")
    padding (16, 10)
style mg_button_text is mg_text:
    hover_color "#B3123F"
    insensitive_color "#B5A8AC"
style mg_accent_button is mg_button:
    background Solid("#B3123F")
    hover_background Solid("#8E0E32")
style mg_accent_button_text is mg_button_text:
    color "#FFFDFB"
    hover_color "#FFFDFB"

transform mg_host_in:
    on show:
        alpha 0.0 xoffset 40
        easein 0.35 alpha 1.0 xoffset 0
    on replace:
        alpha 1.0 xoffset 0

transform mg_pop:
    on show:
        alpha 0.0 zoom 0.85
        easein_back 0.3 alpha 1.0 zoom 1.0

screen mg_frame(title, subtitle="", game=None, msg="", face="neutral", host=True):
    modal True
    zorder 150
    $ host_who, host_bg = MG_HOST.get(game, (None, None))
    add Solid("#F6EFE9")
    if host_bg and renpy.loadable(host_bg):
        add Transform(host_bg, blur=16, xysize=(1280, 720))
        add Solid("#F6EFE9") alpha 0.78
    add Solid("#B3123F") ysize 6
    if host_who and host:
        add mg_portrait(host_who, face) zoom 0.6 xanchor 0.5 xpos 1096 ypos 168
        frame:
            xpos 900 ypos 52 xsize 356 padding (20, 12, 20, 16)
            background silk_surface("panel")
            vbox:
                spacing 4
                text MG_NAME[host_who] font "fonts/Jua-Regular.ttf" size 20 color cream_speaker_color(MG_NAME[host_who], history=True)
                text (msg or MG_HELLO.get(game, "")) style "mg_text" size 18 line_spacing 4
    vbox:
        xpos 40 ypos 24 spacing 2
        text title style "mg_title"
        if subtitle:
            text subtitle style "mg_small" xmaximum (840 if (host_who and host) else 1200)
    transclude

screen mg_bubble(who, msg, px=40, py=640):
    # 화면이 넓게 필요한 놀이에서는 아래쪽 말풍선 한 줄로 반응한다.
    if msg:
        frame:
            xpos px ypos py padding (18, 10)
            background silk_surface("panel")
            hbox:
                spacing 10
                text MG_NAME[who] font "fonts/Jua-Regular.ttf" size 18 color cream_speaker_color(MG_NAME[who], history=True) yalign 0.5
                text msg style "mg_text" size 18 yalign 0.5

screen mg_offer(game):
    modal True
    zorder 200
    $ info = MG_INFO[game]
    $ host_who = MG_HOST.get(game, (None, None))[0]
    add Solid("#3B0B2299")
    frame:
        at mg_pop
        xalign 0.5 yalign 0.45 xsize 680 padding (36, 30)
        background silk_surface("panel")
        hbox:
            spacing 22
            if host_who:
                add mg_face_thumb(host_who) yalign 0.0
            vbox:
                spacing 14
                text "미니게임 · " + info[0] style "mg_title"
                text info[2] style "mg_text"
                text "건너뛰어도 이야기는 그대로 이어집니다." style "mg_small"
                hbox:
                    spacing 14 xalign 1.0
                    textbutton "건너뛰기" id "mg_skip" style "mg_button" action Return(False)
                    textbutton "해 보기" id "mg_go" style "mg_accent_button" action Return(True)

screen mg_result_card(game, score, top=None, verdict="", face="smile", detail="", line=""):
    $ stars = (3 if verdict == "win" else (2 if verdict == "draw" else 1)) if top is None else mg_stars(score, top)
    $ lines = {3: "완벽해요!", 2: "잘했어요!", 1: "다음엔 더 잘할 수 있어요."}
    use mg_frame(MG_INFO[game][0], "결과", game, line, face):
        frame:
            at mg_pop
            xpos 40 ypos 130 xsize 820 padding (44, 36)
            background silk_surface("panel")
            vbox:
                spacing 18
                hbox:
                    spacing 14
                    for k in range(3):
                        add silk("heart", k < stars, size=(58, 58))
                text lines[stars] font "fonts/Jua-Regular.ttf" size 40 color "#3B0B22"
                text (detail or ("점수 %d / %d" % (score, top))) style "mg_text" size 24
                text "최고 기록 %s" % persistent.minigame_best.get(game, "-") style "mg_small" size 18
                null height 6
                textbutton "계속" id "mg_result_ok" style "mg_accent_button" text_size 24 action Return(True)
    key "dismiss" action Return(True)

# ---------------- 1. 안내판 ----------------

screen mg_sign(rnd=0, tries=0, msg="", face="neutral"):
    $ R = SIGN_ROUNDS[rnd]
    $ picked, d = mg_pick, mg_dir
    use mg_frame("안내판 옮기기", "%d / %d판 · %s" % (rnd + 1, len(SIGN_ROUNDS), R["goal"]), "sign", msg, face):
        fixed:
            xpos 40 ypos 104 xysize (660, 440)
            for y, row in enumerate(R["rows"]):
                for x, ch in enumerate(row):
                    $ cx, cy = x * 110, y * 110
                    if ch == "E":
                        frame xpos cx ypos cy xysize (106, 106) background Solid("#3B0B22"):
                            text "입구" style "mg_text" color "#FFFDFB" align (0.5, 0.5)
                    elif ch == "B":
                        frame xpos cx ypos cy xysize (106, 106) background Solid("#F2C14E"):
                            text "부스" style "mg_text" align (0.5, 0.5)
                    elif ch == "P":
                        frame xpos cx ypos cy xysize (106, 106) background Solid("#9C8C91"):
                            text "기둥" style "mg_text" color "#FFFDFB" align (0.5, 0.5)
                    elif ch.isdigit():
                        button xpos cx ypos cy xysize (106, 106) id ("sign_slot_" + ch):
                            background Solid("#B3123F" if picked == ch else "#FFFDFB")
                            hover_background Solid("#F6D9DF")
                            action SetVariable("mg_pick", ch)
                            if picked == ch:
                                add mg_arrow(d, 46, "#FFFDFB") align (0.5, 0.5)
                            else:
                                text "자리 " + ch style "mg_text" size 18 color "#6E4553" align (0.5, 0.5)
                    else:
                        add Solid("#E6D9CF") xpos cx ypos cy xysize (106, 106)
        hbox:
            xpos 40 ypos 566 spacing 6
            text "방향" style "mg_text" yalign 0.5
            null width 6
            for dd in SIGN_DIRS:
                button:
                    style "mg_button" xysize (56, 50) id ("sign_dir_" + str(SIGN_DIRS.index(dd)))
                    selected_background Solid("#3B0B22")
                    action SetVariable("mg_dir", dd) selected (d == dd)
                    add mg_arrow(dd, 26, ("#FFFDFB" if d == dd else "#3B0B22")) align (0.5, 0.5)
        hbox:
            xpos 40 ypos 634 spacing 12
            textbutton "여기에 놓기" id "sign_place" style "mg_accent_button" sensitive (picked is not None) action Return(("place", picked, d))
            textbutton "그만하기" id "sign_quit" style "mg_button" action Return(("quit", None, None))

label mg_sign_game:
    $ sign_score = 0
    $ rnd = 0
    $ msg = ""
    $ face_now = "neutral"
    while rnd < len(SIGN_ROUNDS):
        $ tries = 0
        $ solved = False
        while not solved and tries < 3:
            $ mg_pick, mg_dir = None, "→"
            $ act, slot, d = renpy.call_screen("mg_sign", rnd=rnd, tries=tries, msg=msg, face=face_now)
            if act == "quit":
                $ mg_result = sign_score
                return
            $ R = SIGN_ROUNDS[rnd]
            if (slot, d) == R["answer"]:
                $ solved = True
                $ sign_score += 3 - tries
                $ msg = ["좋아, 바로 거기! 손님들이 줄 서서 들어오겠다.", "딱 맞아! 이제 안내판 감 잡았네?", "역시! 다음 것도 부탁해~"][tries]
                $ face_now = "smile" if tries else "laugh"
            else:
                $ tries += 1
                $ msg = R["hints"].get(slot, "음... 다른 데 놔 볼까?")
                $ face_now = "serious" if R["hints"].get(slot, "").startswith("자리") else "pout"
        if not solved:
            $ msg = "괜찮아, 정답은 자리 %s에 %s 방향이었어. 다음 거 가 보자!" % (R["answer"][0], {"←": "왼쪽", "↑": "위", "→": "오른쪽", "↓": "아래", "↗︎": "오른쪽 위", "↖︎": "왼쪽 위"}[R["answer"][1]])
            $ face_now = "sad"
        $ rnd += 1
    $ mg_record("sign", sign_score)
    $ mg_result = sign_score
    $ renpy.call_screen("mg_result_card", game="sign", score=sign_score, top=3 * len(SIGN_ROUNDS), face=("laugh" if sign_score >= 7 else "smile"), line=("첫날부터 안내 감각 최고! 합격 도장 꾹!" if sign_score >= 7 else "괜찮아, 나도 첫날엔 화살표 거꾸로 붙였어."))
    return

# ---------------- 2. 카드 ----------------

screen mg_card(c, button_id=None, action=None):
    $ bread = c in BREADS
    $ img = "images/minigame/card_" + CARD_ART[c] + ".png"
    button:
        xysize (150, 200)
        id button_id
        background None
        action action
        at mg_card_hover
        fixed:
            xysize (150, 200)
            if renpy.loadable(img):
                add Transform(img, xysize=(150, 200))
            else:
                add Solid("#FBE7C8" if bread else "#DDEFD8")
            add Solid("#E0A84B" if bread else "#8DBF8A") xysize (150, 4) ypos 196
            vbox:
                xalign 0.5 ypos 128 spacing 2
                text c style "mg_text" size 22 xalign 0.5
                text ("짝: " + (PAIRS[c] if bread else [b for b, t in PAIRS.items() if t == c][0])) style "mg_small" size 13 xalign 0.5

transform mg_card_hover:
    on idle:
        ease 0.12 yoffset 0
    on hover:
        ease 0.12 yoffset -10

screen mg_hand(cards, label):
    vbox:
        spacing 6
        text label style "mg_text"
        hbox:
            spacing 6
            for c in cards:
                $ img = "images/minigame/card_" + CARD_ART[c] + ".png"
                fixed:
                    xysize (72, 96)
                    if renpy.loadable(img):
                        add Transform(img, xysize=(72, 96))
                    else:
                        add Solid("#FBE7C8" if c in BREADS else "#DDEFD8")
                        text c style "mg_small" size 12 align (0.5, 0.5)
            for k in range(5 - len(cards)):
                add Solid("#FFFDFB88") xysize (72, 96)

screen mg_cards(g):
    use mg_frame("빵·차 카드게임", "짝 하나 3점 · 세 가지 짝을 모두 모으면 +2 · 각자 다섯 장", "cards", g["log"], g.get("face", "neutral")):
        vbox:
            xpos 40 ypos 96 spacing 14
            use mg_hand(g["rival"], "지현 (%d점)" % cards_score(g["rival"]))
            text "가운데 카드 · 한 장을 고르세요" style "mg_small"
            hbox:
                spacing 14
                for i, c in enumerate(g["market"]):
                    use mg_card(c, "card_market_%d" % i, CardsPick(g, i) if g["turn"] == "me" else None)
            use mg_hand(g["me"], "내 카드 (%d점)" % cards_score(g["me"]))
        hbox:
            xpos 40 ypos 650 spacing 12
            if g["turn"] == "done":
                textbutton "결과 보기" id "cards_done" style "mg_accent_button" action Return("done")
            textbutton "그만하기" id "cards_quit" style "mg_button" action Return("quit")

label mg_cards_game:
    $ g = cards_new_game()
    $ act = renpy.call_screen("mg_cards", g=g)
    $ me, rival = cards_score(g["me"]), cards_score(g["rival"])
    if act == "quit":
        $ mg_result = None
        return
    $ mg_record("cards", me)
    $ mg_result = (me, rival)
    $ cards_verdict = "win" if me > rival else ("draw" if me == rival else "lose")
    $ renpy.call_screen("mg_result_card", game="cards", score=me, top=None, verdict=cards_verdict, face={"win": "pout", "draw": "serious", "lose": "smile"}[cards_verdict], detail="나 %d점 : 지현 %d점" % (me, rival), line={"win": "...졌네. 다음 판은 진지하게 한다.", "draw": "동점이라. 결론은 다음으로 미루자.", "lose": "내가 이겼네. 다시 붙어 볼래?"}[cards_verdict])
    return

# ---------------- 3. 사진 ----------------

screen mg_photo(spot):
    $ cell = mg_cell
    $ path, target, hint = PHOTO_SPOTS[spot]
    use mg_frame("기록집 사진", "오늘 남기고 싶은 것: " + hint, "photo"):
        frame:
            xpos 34 ypos 94 padding (6, 6, 6, 6)
            background Solid("#3B0B22")
            fixed:
                xysize (960, 540)
                add Transform(path, xysize=(960, 540))
                add Solid("#00000066") xysize (960, 540)
                for gx in range(3):
                    for gy in range(3):
                        button:
                            xpos gx * 240 ypos gy * 135 xysize (480, 270)
                            id "photo_cell_%d_%d" % (gx, gy)
                            background None
                            action SetVariable("mg_cell", (gx, gy))
                add Transform(Crop((cell[0] * 320, cell[1] * 180, 640, 360), path), xysize=(480, 270)) xpos cell[0] * 240 ypos cell[1] * 135
                add Solid("#FFFDFB") xpos cell[0] * 240 ypos cell[1] * 135 xysize (480, 4)
                add Solid("#FFFDFB") xpos cell[0] * 240 ypos cell[1] * 135 + 266 xysize (480, 4)
                add Solid("#FFFDFB") xpos cell[0] * 240 ypos cell[1] * 135 xysize (4, 270)
                add Solid("#FFFDFB") xpos cell[0] * 240 + 476 ypos cell[1] * 135 xysize (4, 270)
                text "+" size 34 color "#FFFDFB" xpos cell[0] * 240 + 240 ypos cell[1] * 135 + 135 xanchor 0.5 yanchor 0.5
        vbox:
            xpos 1030 ypos 120 spacing 14 xsize 220
            text "화면을 눌러 뷰파인더를 옮기세요." style "mg_small"
            textbutton "찰칵" id "photo_shoot" style "mg_accent_button" text_size 28 action Return(cell)
            textbutton "그만하기" id "photo_quit" style "mg_button" action Return(None)

transform mg_flash:
    alpha 0.9
    linear 0.35 alpha 0.0

screen mg_photo_result(spot, cell, score):
    use mg_frame("기록집 사진", ("좋은 사진!" if score == 3 else ("괜찮은 사진" if score == 2 else "흔들린 한 장도 기록")), "photo"):
        frame:
            at mg_pop
            xalign 0.5 ypos 104 padding (12, 12, 12, 40)
            background Solid("#FFFDFB")
            add Transform(photo_crop(spot, cell), xysize=(760, 428))
        hbox:
            xalign 0.5 ypos 560 spacing 10
            for k in range(3):
                add silk("heart", k < score, size=(30, 30))
        text ["", "다음엔 " + PHOTO_SPOTS[spot][2] + " 쪽을 노려 보자.", "조금만 옮기면 더 좋았겠다.", "딱 그 장면이다."][score] style "mg_text" xalign 0.5 ypos 600
        textbutton "기록집에 넣기" id "photo_keep" style "mg_accent_button" xalign 0.5 ypos 640 action Return(True)
    add Solid("#FFFFFF") at mg_flash

label mg_photo_game(spot="free"):
    $ mg_cell = (1, 1)
    $ cell = renpy.call_screen("mg_photo", spot=spot)
    if cell is None:
        $ mg_result = None
        return
    $ score = photo_score(spot, cell)
    $ renpy.call_screen("mg_photo_result", spot=spot, cell=cell, score=score)
    $ persistent.album = (persistent.album or []) + [dict(spot=spot, cell=list(cell), score=score)]
    $ mg_record("photo", score)
    $ mg_result = score
    return

# ---------------- 4. 한 줄로 줄이기 ----------------

screen mg_trim(rnd=0, msg="", face="neutral"):
    $ off = mg_off
    $ R = TRIM_ROUNDS[rnd]
    $ n = trim_len(R["chips"], off)
    use mg_frame("한 줄로 줄이기", "%d / %d · %s" % (rnd + 1, len(TRIM_ROUNDS), R["brief"]), "trim", msg, face):
        vbox:
            xpos 40 ypos 110 spacing 16 xsize 820
            text "낱말 조각을 눌러 빼거나 다시 넣으세요." style "mg_small"
            hbox:
                box_wrap True spacing 10 xsize 820
                for i, c in enumerate(R["chips"]):
                    $ gone = c in off
                    button:
                        id "trim_chip_%d" % i
                        padding (14, 10)
                        background Solid("#EDE6E1" if gone else "#FFFDFB")
                        hover_background Solid("#F6D9DF")
                        action SetVariable("mg_off", (off - {c}) if gone else (off | {c}))
                        text c style "mg_text" color ("#B5A8AC" if gone else "#3B0B22") strikethrough gone
            frame background silk_surface("panel") padding (24, 18) xsize 820:
                vbox:
                    spacing 8
                    text (trim_text(R["chips"], off) or "...") style "mg_text" size 26
                    hbox:
                        spacing 12
                        frame:
                            xsize 400 ysize 10 padding (0, 0)
                            background Solid("#EDE6E1")
                            add Solid("#B3123F" if n > R["limit"] else "#2F7A3B") xsize max(1, int(400 * min(1.0, float(n) / max(1, len("".join(R["chips"]))))))
                        text "%d / %d자 (띄어쓰기 제외)" % (n, R["limit"]) style "mg_small" color ("#B3123F" if n > R["limit"] else "#2F7A3B") yalign 0.5
            hbox:
                spacing 12
                textbutton "이걸로 보내기" id "trim_submit" style "mg_accent_button" action Return(("submit", off))
                textbutton "그만하기" id "trim_quit" style "mg_button" action Return(("quit", off))

label mg_trim_game:
    $ trim_score = 0
    $ rnd = 0
    $ msg = ""
    $ face_now = "neutral"
    while rnd < len(TRIM_ROUNDS):
        $ R = TRIM_ROUNDS[rnd]
        $ mg_off = set()
        $ attempts = 0
        $ passed = False
        while not passed:
            $ act, off = renpy.call_screen("mg_trim", rnd=rnd, msg=msg, face=face_now)
            if act == "quit":
                $ mg_result = trim_score
                return
            $ attempts += 1
            $ lost = [k for k in R["keep"] if k in off]
            if lost:
                $ msg = "‘%s’ 빼면 손님이 못 와. 그건 살려 줘." % lost[0]
                $ face_now = "serious"
            elif trim_len(R["chips"], off) > R["limit"]:
                $ msg = "아직 길어. 클라이언트가 또 ‘짧게’라고 할걸?"
                $ face_now = "pout"
            else:
                $ trim_score += 2 if attempts == 1 else 1
                $ msg = "오, 깔끔하다! 이건 바로 보내도 되겠어~" if attempts == 1 else "좋아, 이 정도면 통과!"
                $ face_now = "laugh" if attempts == 1 else "smile"
                $ passed = True
        $ rnd += 1
    $ mg_record("trim", trim_score)
    $ mg_result = trim_score
    $ renpy.call_screen("mg_result_card", game="trim", score=trim_score, top=2 * len(TRIM_ROUNDS), face=("laugh" if trim_score >= 3 else "smile"), line=("이 정도면 나 오늘 일찍 퇴근해도 되겠다~" if trim_score >= 3 else "줄이는 게 쓰는 것보다 어렵지? 그래도 잘했어."))
    return

# ---------------- 5. 어디가 달라졌어요? ----------------

screen mg_spot_poster(data, px, clickable=False, found=set()):
    fixed:
        xpos px ypos 120 xysize (390, 430)
        add Solid("#FFFDFB")
        for name, bx, by, bw, bh in SPOT_BLOCKS:
            $ label, color, size = data[name]
            if clickable:
                button:
                    xpos bx ypos by xysize (bw, bh)
                    id "spot_" + name
                    background Solid("#F2C14E55" if name in found else "#00000000")
                    hover_background Solid("#F6D9DF88")
                    action Return(name)
                    text label style "mg_text" font ("fonts/Pretendard-Regular.otf" if name == "arrow" else "fonts/GowunDodum-Regular.ttf") color color size size align (0.5, 0.5) text_align 0.5
            else:
                text label style "mg_text" font ("fonts/Pretendard-Regular.otf" if name == "arrow" else "fonts/GowunDodum-Regular.ttf") color color size size xpos bx + bw // 2 ypos by + bh // 2 xanchor 0.5 yanchor 0.5 text_align 0.5
        if not clickable:
            add Solid("#EDE3DC") xpos 30 ypos 180 xysize (200, 4)

screen mg_spot(found=set(), misses=0, rnd=0, msg=""):
    if spot_art_ready():
        $ P = SPOT_PAIRS[rnd]
        use mg_frame("어디가 달라졌어요?", "%d / %d · 오른쪽 수정 시안에서 달라진 곳을 누르세요" % (rnd + 1, len(SPOT_PAIRS)), "spot", host=False):
            hbox:
                xanchor 1.0 xpos 1240 ypos 34 spacing 18
                hbox:
                    spacing 4
                    for k in range(3):
                        add silk("heart", k < len(found), size=(26, 26))
                text "남은 기회 %d" % (3 - misses) style "mg_text" yalign 0.5
            text "원래 시안" style "mg_small" xpos 140 ypos 108
            text "수정 시안" style "mg_small" xpos 690 ypos 108
            add ("images/minigame/%s_orig.png" % P["img"]) xpos 140 ypos 132
            fixed:
                xpos 690 ypos 132 xysize (450, 500)
                add ("images/minigame/%s_edit.png" % P["img"])
                for n in range(1, 13):
                    $ g = P["groups"].get(n)
                    button:
                        xpos ((n - 1) % 3) * 150 ypos ((n - 1) // 3) * 125 xysize (150, 125)
                        id "spot_cell_%d" % n
                        background (Solid("#F2C14E66") if g in found else None)
                        hover_background Solid("#F6D9DF55")
                        action Return(g or "miss")
            textbutton "그만하기" id "spot_quit" style "mg_button" xpos 40 ypos 650 action Return("quit")
            use mg_bubble("yujin", msg or MG_HELLO["spot"], 190, 646)
    else:
        use mg_frame("어디가 달라졌어요?", "오른쪽 수정 시안에서 달라진 곳을 누르세요 · 찾은 곳 %d / 3 · 남은 기회 %d" % (len(found), 3 - misses), "spot", host=False):
            text "원래 시안" style "mg_small" xpos 120 ypos 96
            text "수정 시안" style "mg_small" xpos 720 ypos 96
            use mg_spot_poster(SPOT_ORIG, 120)
            use mg_spot_poster(SPOT_EDIT, 720, True, found)
            textbutton "그만하기" id "spot_quit" style "mg_button" xpos 40 ypos 650 action Return("quit")
            use mg_bubble("yujin", msg or MG_HELLO["spot"], 190, 646)

label mg_spot_game:
    $ spot_total = 0
    $ rounds = len(SPOT_PAIRS) if spot_art_ready() else 1
    $ rnd = 0
    $ msg = ""
    while rnd < rounds:
        $ found = set()
        $ misses = 0
        $ answers = set(SPOT_PAIRS[rnd]["groups"].values()) if spot_art_ready() else SPOT_ANSWERS
        while len(found) < 3 and misses < 3:
            $ pick = renpy.call_screen("mg_spot", found=found, misses=misses, rnd=rnd, msg=msg)
            if pick == "quit":
                $ mg_result = spot_total + len(found)
                return
            if pick in found:
                $ msg = "거긴 아까 찾으셨어요!"
            elif pick in answers:
                $ found = found | {pick}
                $ msg = ["맞아요, 거기예요!", "와, 또 찾으셨네요!", "다 찾으셨어요! 다음 시안으로 가요."][len(found) - 1]
            else:
                $ misses += 1
                $ msg = "음... 거긴 그대로예요. 다시 한번 비교해 보세요."
        $ spot_total += len(found)
        $ rnd += 1
    $ mg_record("spot", spot_total)
    $ mg_result = spot_total
    $ renpy.call_screen("mg_result_card", game="spot", score=spot_total, top=3 * rounds, face=("laugh" if spot_total >= 3 * rounds - 1 else "smile"), line=("다 찾으셨어요? ...저 이거 회의 때 써먹어도 돼요?" if spot_total >= 3 * rounds - 1 else "괜찮아요. 저도 어제 한참 걸렸어요."))
    return

# ---------------- 이야기 속 호출 ----------------

label minigame(game, spot="free"):
    if not mg_should_offer():
        return
    if not renpy.call_screen("mg_offer", game):
        return
    $ mg_result = None
    if game == "photo":
        call mg_photo_game(spot)
    else:
        call expression ("mg_" + game + "_game")
    call minigame_reaction(game)
    return

label minigame_reaction(game):
    if mg_result is None:
        return
    if game == "sign":
        if mg_result >= 7:
            $ award_once("mg_sign", "ria", 1)
            r "[ri('와, 첫날부터 안내 감각 장난 아닌데? 합격 도장 꾹!', '와, 첫날부터 안내 감각 장난 아닌데요? 합격 도장 꾹!')]"
        else:
            r "[ri('괜찮아, 나도 첫날엔 화살표 거꾸로 붙였어. 진짜로!', '괜찮아요, 저도 첫날엔 화살표 거꾸로 붙였어요. 진짜로요!')]"
    elif game == "cards":
        $ me, rival = mg_result
        if me > rival:
            $ award_once("mg_cards", "jihyun", 1)
            j "...졌네. 한 판 더. 이번 건 연습이었어."
        elif me == rival:
            j "동점. 이런 결과는 결재가 안 나는데. 다음에 결론 내자."
        else:
            j "내가 이겼네. 한 점 차이도 아니고. ...봐주진 않았어."
    elif game == "photo":
        if mg_result == 3:
            $ award_once("mg_photo_" + (chapter or ""), cream_focus if cream_focus in ("ria", "jihyun", "yujin", "seoyun") else "ria", 1)
        dn "기록집에 한 장이 늘었다. 이 사진을 볼 때마다 오늘 옆에 누가 있었는지 떠오를 것이다."
    elif game == "trim":
        if mg_result >= 3:
            $ award_once("mg_trim", "seoyun", 1)
            s "오, 첫날에 이걸 한 번에? 나 오늘 일찍 퇴근해도 되겠다~"
        else:
            s "줄이는 게 쓰는 것보다 어렵지. 그래서 내가 월급 받는 거야~"
    elif game == "spot":
        if mg_result >= (5 if spot_art_ready() else 3):
            $ award_once("mg_spot", "yujin", 1)
            y "다, 다 찾으셨어요? ...저 이거 회의 때 써먹어도 돼요?"
        else:
            y "괜찮아요. 저도 어제 찾는 데 한참 걸렸어요. 다른 데를 먼저 보셨네요."
    return

# ---------------- 메인 화면: 미니게임 모음 ----------------

screen minigame_hub():
    tag menu
    use mg_frame("미니게임", "이야기 속 장면을 다시 해 볼 수 있습니다.", "hub"):
        grid 3 2:
            xpos 40 ypos 104 spacing 18
            for key in ("sign", "cards", "photo", "trim", "spot"):
                $ info = MG_INFO[key]
                $ who = MG_HOST[key][0]
                $ best = persistent.minigame_best.get(key)
                button:
                    id ("hub_" + key)
                    xysize (384, 196) padding (20, 18)
                    background silk_surface("panel")
                    hover_background silk_surface("hover")
                    action [SetField(persistent, "mg_pending", key), Start("minigame_free")]
                    at mg_card_hover
                    hbox:
                        spacing 16
                        if who:
                            add mg_face_thumb(who)
                        else:
                            add Transform(Crop((320, 180, 640, 360), "images/bg/bg_street.jpg"), xysize=(96, 96))
                        vbox:
                            spacing 6
                            text info[0] font silk_title_font(info[0]) size 26 color "#3B0B22" hover_color "#FFFDFB"
                            text "함께: " + info[1] style "mg_small" hover_color "#F3E7EA"
                            text ("최고 기록 %s" % best if best is not None else "아직 기록 없음") style "mg_small" hover_color "#F3E7EA"
            null
        hbox:
            xpos 40 ypos 560 spacing 16
            textbutton ("이야기 중 미니게임 제안: " + ("켜짐" if persistent.minigames_on else "꺼짐")) id "hub_toggle" style "mg_button" action ToggleField(persistent, "minigames_on")
            text "기록집 사진 %d장" % len(persistent.album or []) style "mg_small" yalign 0.5
        textbutton "돌아가기" id "hub_back" style "mg_button" xpos 40 ypos 640 action Return()

label minigame_free:
    $ game = persistent.mg_pending or "sign"
    $ chapter = "미니게임"
    $ location = "미니게임"
    $ cream_focus = None
    if game == "photo":
        call mg_photo_game("free")
    else:
        call expression ("mg_" + game + "_game")
    return
