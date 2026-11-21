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

screen mg_frame(title, subtitle=""):
    modal True
    zorder 150
    add Solid("#F6EFE9")
    add Solid("#B3123F") ysize 6
    vbox:
        xpos 40 ypos 24 spacing 2
        text title style "mg_title"
        if subtitle:
            text subtitle style "mg_small"
    transclude

screen mg_offer(game):
    modal True
    zorder 200
    $ info = MG_INFO[game]
    add Solid("#3B0B2299")
    frame:
        xalign 0.5 yalign 0.45 xsize 620 padding (36, 30)
        background Solid("#FFFDFB")
        vbox:
            spacing 14
            text "미니게임 · " + info[0] style "mg_title"
            text info[2] style "mg_text"
            text "건너뛰어도 이야기는 그대로 이어집니다." style "mg_small"
            hbox:
                spacing 14 xalign 1.0
                textbutton "건너뛰기" id "mg_skip" style "mg_button" action Return(False)
                textbutton "해 보기" id "mg_go" style "mg_accent_button" action Return(True)

# ---------------- 1. 안내판 ----------------

screen mg_sign(rnd=0, tries=0, msg=""):
    $ R = SIGN_ROUNDS[rnd]
    $ picked, d = mg_pick, mg_dir
    use mg_frame("안내판 옮기기", "%d / %d판 · %s" % (rnd + 1, len(SIGN_ROUNDS), R["goal"])):
        fixed:
            xpos 40 ypos 110 xysize (720, 480)
            for y, row in enumerate(R["rows"]):
                for x, ch in enumerate(row):
                    $ cx, cy = x * 120, y * 120
                    if ch == "E":
                        frame xpos cx ypos cy xysize (116, 116) background Solid("#3B0B22"):
                            text "입구" style "mg_text" color "#FFFDFB" align (0.5, 0.5)
                    elif ch == "B":
                        frame xpos cx ypos cy xysize (116, 116) background Solid("#F2C14E"):
                            text "부스" style "mg_text" align (0.5, 0.5)
                    elif ch == "P":
                        frame xpos cx ypos cy xysize (116, 116) background Solid("#9C8C91"):
                            text "기둥" style "mg_text" color "#FFFDFB" align (0.5, 0.5)
                    elif ch.isdigit():
                        button xpos cx ypos cy xysize (116, 116) id ("sign_slot_" + ch):
                            background Solid("#B3123F" if picked == ch else "#FFFDFB")
                            hover_background Solid("#F6D9DF")
                            action SetVariable("mg_pick", ch)
                            text (d if picked == ch else "자리 " + ch) style "mg_text" font ("fonts/Pretendard-Regular.otf" if picked == ch else "fonts/GowunDodum-Regular.ttf") size (46 if picked == ch else 18) color ("#FFFDFB" if picked == ch else "#6E4553") align (0.5, 0.5)
                    else:
                        add Solid("#EDE3DC") xpos cx ypos cy xysize (116, 116)
        vbox:
            xpos 800 ypos 120 spacing 12 xsize 440
            text "방향" style "mg_text"
            hbox:
                spacing 6
                for dd in SIGN_DIRS:
                    textbutton dd style "mg_button" text_size 26 text_font "fonts/Pretendard-Regular.otf" action SetVariable("mg_dir", dd) id ("sign_dir_" + str(SIGN_DIRS.index(dd))) selected (d == dd)
            null height 10
            textbutton "여기에 놓기" id "sign_place" style "mg_accent_button" sensitive (picked is not None) action Return(("place", picked, d))
            textbutton "그만하기" id "sign_quit" style "mg_button" action Return(("quit", None, None))
            null height 16
            if msg:
                frame background Solid("#FFFDFB") padding (16, 12) xsize 440:
                    text "리아: " + msg style "mg_text"

label mg_sign_game:
    $ sign_score = 0
    $ rnd = 0
    while rnd < len(SIGN_ROUNDS):
        $ tries = 0
        $ msg = ""
        $ solved = False
        while not solved and tries < 3:
            $ mg_pick, mg_dir = None, "→"
            $ act, slot, d = renpy.call_screen("mg_sign", rnd=rnd, tries=tries, msg=msg)
            if act == "quit":
                $ mg_result = sign_score
                return
            $ R = SIGN_ROUNDS[rnd]
            if (slot, d) == R["answer"]:
                $ solved = True
                $ sign_score += 3 - tries
            else:
                $ tries += 1
                $ msg = R["hints"].get(slot, "음... 다른 데 놔 볼까?")
        $ rnd += 1
    $ mg_record("sign", sign_score)
    $ mg_result = sign_score
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

screen mg_cards(g):
    use mg_frame("빵·차 카드게임", "짝 하나 3점 · 세 가지 짝을 모두 모으면 +2 · 각자 다섯 장"):
        vbox:
            xpos 40 ypos 100 spacing 10
            text "지현 (%d점)  " % cards_score(g["rival"]) + "  ".join(g["rival"]) style "mg_text"
            null height 6
            text "가운데 카드" style "mg_small"
            hbox:
                spacing 14
                for i, c in enumerate(g["market"]):
                    use mg_card(c, "card_market_%d" % i, CardsPick(g, i) if g["turn"] == "me" else None)
            null height 6
            text "내 카드 (%d점)  " % cards_score(g["me"]) + "  ".join(g["me"]) style "mg_text"
            frame background Solid("#FFFDFB") padding (16, 10):
                text "지현: " + g["log"] style "mg_text"
        hbox:
            xpos 40 ypos 640 spacing 12
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
    return

# ---------------- 3. 사진 ----------------

screen mg_photo(spot):
    $ cell = mg_cell
    $ path, target, hint = PHOTO_SPOTS[spot]
    use mg_frame("기록집 사진", "오늘 남기고 싶은 것: " + hint):
        fixed:
            xpos 40 ypos 100 xysize (960, 540)
            add Transform(path, xysize=(960, 540))
            add Solid("#00000055") xysize (960, 540)
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
        vbox:
            xpos 1030 ypos 120 spacing 14 xsize 220
            text "화면을 눌러 뷰파인더를 옮기세요." style "mg_small"
            textbutton "찰칵" id "photo_shoot" style "mg_accent_button" text_size 28 action Return(cell)
            textbutton "그만하기" id "photo_quit" style "mg_button" action Return(None)

screen mg_photo_result(spot, cell, score):
    use mg_frame("기록집 사진", ("좋은 사진!" if score == 3 else ("괜찮은 사진" if score == 2 else "흔들린 한 장도 기록"))):
        add Transform(photo_crop(spot, cell), xysize=(800, 450)) xalign 0.5 ypos 110
        text ["", "다음엔 " + PHOTO_SPOTS[spot][2] + " 쪽을 노려 보자.", "조금만 옮기면 더 좋았겠다.", "딱 그 장면이다."][score] style "mg_text" xalign 0.5 ypos 580
        textbutton "기록집에 넣기" id "photo_keep" style "mg_accent_button" xalign 0.5 ypos 630 action Return(True)

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

screen mg_trim(rnd=0, msg=""):
    $ off = mg_off
    $ R = TRIM_ROUNDS[rnd]
    $ n = trim_len(R["chips"], off)
    use mg_frame("한 줄로 줄이기", "%d / %d · %s" % (rnd + 1, len(TRIM_ROUNDS), R["brief"])):
        vbox:
            xpos 40 ypos 110 spacing 16 xsize 1200
            text "낱말 조각을 눌러 빼거나 다시 넣으세요." style "mg_small"
            hbox:
                box_wrap True spacing 10
                for i, c in enumerate(R["chips"]):
                    $ gone = c in off
                    button:
                        id "trim_chip_%d" % i
                        padding (14, 10)
                        background Solid("#EDE6E1" if gone else "#FFFDFB")
                        hover_background Solid("#F6D9DF")
                        action SetVariable("mg_off", (off - {c}) if gone else (off | {c}))
                        text c style "mg_text" color ("#B5A8AC" if gone else "#3B0B22") strikethrough gone
            frame background Solid("#FFFDFB") padding (20, 16) xsize 1200:
                vbox:
                    spacing 6
                    text (trim_text(R["chips"], off) or "...") style "mg_text" size 28
                    text "%d / %d자 (띄어쓰기 제외)" % (n, R["limit"]) style "mg_small" color ("#B3123F" if n > R["limit"] else "#2F7A3B")
            hbox:
                spacing 12
                textbutton "이걸로 보내기" id "trim_submit" style "mg_accent_button" action Return(("submit", off))
                textbutton "그만하기" id "trim_quit" style "mg_button" action Return(("quit", off))
            if msg:
                frame background Solid("#FFFDFB") padding (16, 12):
                    text "서윤: " + msg style "mg_text"

label mg_trim_game:
    $ trim_score = 0
    $ rnd = 0
    while rnd < len(TRIM_ROUNDS):
        $ R = TRIM_ROUNDS[rnd]
        $ mg_off = set()
        $ msg = ""
        $ attempts = 0
        $ passed = False
        while not passed:
            $ act, off = renpy.call_screen("mg_trim", rnd=rnd, msg=msg)
            if act == "quit":
                $ mg_result = trim_score
                return
            $ attempts += 1
            $ lost = [k for k in R["keep"] if k in off]
            if lost:
                $ msg = "‘%s’ 빼면 손님이 못 와. 그건 살려 줘." % lost[0]
            elif trim_len(R["chips"], off) > R["limit"]:
                $ msg = "아직 길어. 클라이언트가 또 ‘짧게’라고 할걸?"
            else:
                $ trim_score += 2 if attempts == 1 else 1
                $ msg = ""
                $ passed = True
        $ rnd += 1
    $ mg_record("trim", trim_score)
    $ mg_result = trim_score
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

screen mg_spot(found=set(), misses=0):
    use mg_frame("어디가 달라졌어요?", "오른쪽 수정 시안에서 달라진 곳을 누르세요 · 찾은 곳 %d / 3 · 남은 기회 %d" % (len(found), 3 - misses)):
        text "원래 시안" style "mg_small" xpos 120 ypos 96
        text "수정 시안" style "mg_small" xpos 720 ypos 96
        use mg_spot_poster(SPOT_ORIG, 120)
        use mg_spot_poster(SPOT_EDIT, 720, True, found)
        textbutton "그만하기" id "spot_quit" style "mg_button" xpos 40 ypos 640 action Return("quit")

label mg_spot_game:
    $ found = set()
    $ misses = 0
    while len(found) < 3 and misses < 3:
        $ pick = renpy.call_screen("mg_spot", found=found, misses=misses)
        if pick == "quit":
            $ mg_result = len(found)
            return
        if pick in SPOT_ANSWERS:
            $ found = found | {pick}
        else:
            $ misses += 1
    $ mg_record("spot", len(found))
    $ mg_result = len(found)
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
        if mg_result >= 3:
            $ award_once("mg_spot", "yujin", 1)
            y "세, 세 군데 다요? ...저 이거 회의 때 써먹어도 돼요?"
        else:
            y "괜찮아요. 저도 어제 찾는 데 한참 걸렸어요. 다른 데를 먼저 보셨네요."
    return

# ---------------- 메인 화면: 미니게임 모음 ----------------

screen minigame_hub():
    tag menu
    use mg_frame("미니게임", "이야기 속 장면을 다시 해 볼 수 있습니다."):
        vbox:
            xpos 40 ypos 110 spacing 12
            for key in ("sign", "cards", "photo", "trim", "spot"):
                $ info = MG_INFO[key]
                hbox:
                    spacing 16
                    textbutton info[0] id ("hub_" + key) style "mg_accent_button" xsize 300 action [SetField(persistent, "mg_pending", key), Start("minigame_free")]
                    text "%s · 최고 %s" % (info[1], persistent.minigame_best.get(key, "-")) style "mg_text" yalign 0.5
            null height 10
            textbutton ("이야기 중 미니게임 제안: " + ("켜짐" if persistent.minigames_on else "꺼짐")) id "hub_toggle" style "mg_button" action ToggleField(persistent, "minigames_on")
            text "기록집 사진 %d장" % len(persistent.album or []) style "mg_small"
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
