"""Compile the reviewed Ria MD dialogue tables into normal Ren'Py statements."""
from pathlib import Path
import json, re
BASE = Path(__file__).resolve().parent.parent
TEXT = (BASE / "story/ria_source.md").read_text(encoding="utf-8-sig")
OUT = []
def line(s="", n=1): OUT.append("    "*n+s if s else "")
def q(s): return json.dumps(s,ensure_ascii=False)
def say(w,a,b=None,n=1):
    if b is None or a == b:
        line((w+" " if w else "")+q(a),n)
    else:
        expr="[ri("+repr(a)+", "+repr(b)+")]"
        line(w+" "+q(expr),n)
def narr(s,n=1): say("",s,n=n)
def rows(start,end=None):
    pos=TEXT.index(start)+len(start)
    if end:
        stop=TEXT.index(end,pos)
    else:
        m=re.search(r"\n(?:### |## )",TEXT[pos:])
        stop=pos+m.start() if m else len(TEXT)
    found=[]
    for raw in TEXT[pos:stop].splitlines():
        if not raw.startswith("|"): continue
        cols=[c.strip() for c in raw.strip("|").split("|")]
        if len(cols)!=3: continue
        who,a,b=cols
        if any(k in who for k in ("리아","도현")):
            found.append((who,a,b))
    return found
def emit(rs,n=1):
    for who,a,b in rs:
        if "보낸 메시지" in who: actor="msgd"
        elif "답장" in who: actor="msgr"
        elif "독백" in who: actor="dn"
        elif "리아" in who: actor="r"
        else: actor="d"
        say(actor,a,b,n)
def label(name,chapter,place):
    line("label "+name+":",0)
    line("$ chapter = "+q(chapter))
    line("$ location = "+q(place))
def menu(options,n=1):
    line("menu:",n)
    for title,statements in options:
        line(q(title)+":",n+1)
        for statement in statements: line(statement,n+2)
def pair(a,b): return "[ri("+repr(a)+", "+repr(b)+")]"

label("ria_r02","리아 R02 · 문 닫힌 가게 앞에서","다음 만남 · 아직 밝은 퇴근길")
narr("리아가 식당 입구의 임시 휴무 안내를 다시 읽는다. 두 사람은 안으로 들어가지 않는다.")
emit(rows("### R02_00"))
prefs=rows("### R02_01")
for i,pref in enumerate(("quiet","meal","suggestion")):
    line(("if" if i==0 else "elif")+" afterwork_preference == "+q(pref)+":")
    emit(prefs[i*2:i*2+2],2)
line("else:"); emit(prefs[6:8],2)
emit(prefs[8:])
menu([
(pair("문 앞 구경은 여기까지 하고, 대안 같이 찾아보자.","문 앞 구경은 여기까지 하고, 대안 같이 찾아볼까요?"),['$ r02_plan = "together"']),
(pair("여긴 다음에 다시 오자. 오늘은 잠깐만 같이 걷고.","여긴 다음에 다시 와요. 오늘은 잠깐만 같이 걸을까요?"),['$ r02_plan = "rebook"'])])
line('if r02_plan == "together":'); emit(rows("**R02_03A","**R02_03B"),2)
line("else:"); emit(rows("**R02_03B","### R02_04"),2)
narr("둘은 골목으로 걷는다. 카페로 가거나, 역으로 가는 길을 조금 돌아가는 중이다.")
menu([(pair("같이 걸을 때 손도 잡고 싶은데, 괜찮아?","같이 걸을 때 손도 잡고 싶은데, 괜찮아요?"),['$ r02_expression = "hand"']),
(pair("걷면서 얘기 좀 더 하자.","걸으면서 얘기 좀 더 해요."),['$ r02_expression = "talk"'])])
line('if r02_expression == "hand":')
say("d","같이 걸을 때 손도 잡고 싶은데, 괜찮아?","같이 걸을 때 손도 잡고 싶은데, 괜찮아요?",2)
rs=rows("**R02_05A","**R02_05B"); emit(rs[:3],2)
narr("리아가 내민 손을 잡고 걸음을 맞춘다. 정면을 보다가 옆을 보고, 다시 앞을 본다.",2)
line('$ remember("ria_hand")',2); emit(rs[3:],2)
line("else:")
say("d","걷면서 얘기 좀 더 하자.","걸으면서 얘기 좀 더 해요.",2)
rs=rows("**R02_05B","### R02_06")
line('if r02_plan == "together":',2); emit(rs[:2],3)
line("else:",2); emit(rs[2:4],3)
emit(rs[4:],2)
line('if r02_plan == "together":')
narr("영업 중인 카페에 들어가 간단한 식사와 음료를 주문한다. 둘은 자리에 앉는다.",2)
line('$ remember("ria_cafe_visited")',2)
line("else:")
narr("길가 벤치에서 잠깐 쉰다. 오늘 식사는 각자 집에 돌아가서 하기로 했다.",2)
line('if r02_expression == "hand":')
narr("앉기 전에 자연스럽게 손을 놓는다.",2)
rs=rows("### R02_06")
emit(rs[:9])
line('if memory.get("booklet_known_ria"):'); emit(rs[9:10],2)
line("else:"); emit(rs[10:13],2)
line('$ remember("booklet_known_ria")')
emit(rs[13:])
line('$ remember("ria_map_habit")')
line('$ remember("ria_title_joke")')
line('$ remember("ria_memo_promise")')
rs=rows("### R02_07")
line('if r02_plan == "together":'); emit(rs[:4],2)
line("else:"); emit(rs[4:8],2)
narr("해가 낮아진 거리에서 각자의 귀가 방향으로 갈라진다.")
emit(rs[8:])
line('$ remember("ria_contact_offer")')
line('$ award_once("ria_R02","ria",7)')
line("return"); line()

label("ria_r03","리아 R03 · 네가 말했던 자리","다음 날 · 약속 연락")
rs=rows("### R03_00")
emit(rs[:1])
line('if memory.get("ria_cafe_visited"):'); emit(rs[1:2],2)
line("else:")
say("msgr","응, 괜찮아! 회사 뒤 카페에서 보자~ 위치 보내 줄게 :)","네, 괜찮아요! 회사 뒤 카페에서 봐요~ 위치 보내 드릴게요 :)",2)
line('$ remember("ria_r03_messages_received")')
line('$ remember("ria_r03_appointment")')
line('$ location = "R02로부터 이틀 뒤 · 약속한 카페"')
narr("이틀 뒤의 퇴근길. 약속한 카페 앞에서 리아를 만난다.")
emit(rs[2:])
rs=rows("### R03_01")
for i,(pref,start,end,action) in enumerate([
("quiet",0,3,"리아가 창가에서 조금 떨어진 조용한 자리로 먼저 안내한다. 도현이 앉아 주변을 본다."),
("meal",3,6,"리아가 간단한 식사를 주문할 수 있는 자리를 보여준다. 메뉴를 펼친 뒤 각자 고른 음식을 주문한다."),
("suggestion",6,10,"리아가 입구에서 카페 안 두 자리의 분위기를 보여준다. 도현은 안쪽에 앉는다.")]):
    line(("if" if i==0 else "elif")+" afterwork_preference == "+q(pref)+":")
    narr(action,2); emit(rs[start:end],2)
line("else:")
narr("리아가 빈 자리로 먼저 안내한다. 둘이 앉은 뒤 오늘의 제안을 설명한다.",2)
emit(rs[10:],2)
rs=rows("### R03_02")
line('if memory.get("ria_hand"):'); emit(rs[:4],2)
line('elif r02_expression == "talk" and memory.get("ria_map_habit"):'); emit(rs[4:8],2)
line("else:"); emit(rs[8:],2)
rs=rows("### R03_03")
line('if memory.get("ria_memo_promise"):'); emit(rs[:2],2)
line("else:")
line('if not memory.get("booklet_known_ria"):',2)
say("d","동네 사진이랑 짧은 글을 작은 기록집으로 남겨 보려고 해.","동네 사진이랑 짧은 글을 작은 기록집으로 남겨 보려고 해요.",3)
say("d","오늘 가져온 메모가 있는데, 하나 보여줘도 돼?","오늘 가져온 메모가 있는데, 하나 보여드려도 돼요?",2)
say("r","응. 보고 싶어.","네. 보고 싶어요.",2)
narr("도현이 짧은 메모를 보여준다. 제목 후보는 ‘퇴근길의 빛’과 ‘해가 늦게 지는 골목’이다. 리아가 실제로 읽는다.")
line('if memory.get("ria_title_joke"):'); emit(rs[2:4],2)
line("else:")
say("r","제목 둘 중에서 고르는 거야?","제목 둘 중에서 고르는 거예요?",2)
say("d","응. 혼자서는 아직 못 고르겠더라.","네. 혼자서는 아직 못 고르겠더라고요.",2)
emit(rs[4:])
line('$ remember("ria_memo_read")')
line('$ remember("ria_memo_title","해가 늦게 지는 골목")')
narr("대화가 잠깐 끊긴다. 리아는 휴대폰을 가방에 넣고 편하게 기대 앉는다.")
emit(rows("### R03_04"))
narr("리아가 고개를 끄덕인다. 잠깐 대화 없이 같은 자리에 머문다.")
menu([(pair("내가 했던 말 기억해서 준비해 준 거, 좋았어.","제가 했던 말 기억해서 준비해 주신 거, 좋았어요."),['$ r03_reply = "thanks"']),
(pair("다음엔 내가 시간하고 장소부터 제안해 볼게.","다음엔 제가 시간하고 장소부터 제안해 볼게요."),['$ r03_reply = "next"'])])
line('if r03_reply == "thanks":'); emit(rows("**R03_06A","**R03_06B"),2)
line("else:"); emit(rows("**R03_06B","### R03_07"),2)
narr("카페를 나와 익숙한 퇴근길로 걷는다.")
emit(rows("### R03_07"))
line('$ remember("ria_friday_appointment")')
line('$ remember("ria_rest_wish")')
line('$ remember("ria_core_understanding")')
line('$ award_once("ria_R03","ria",9,1)')
narr("리아 시점 · 도현과 헤어진 뒤, 카페 앞.")
narr("리아는 달력의 금요일 약속을 한 번 더 확인한다.")
narr("메시지창에 오늘 즐거웠다는 말을 썼다가 지운다. 금요일에 조금 일찍 가겠다는 말도 적지만, 전송하지 않고 화면을 닫는다.")
say("rn","조금 일찍 가면... 조금 더 볼 수도 있으니까.")
narr("도현 시점으로 돌아갑니다.")
line("return"); line()

label("ria_r04","리아 R04 · 장난은 여기까지","금요일 저녁 · 카페")
line('if not memory.get("ria_core_understanding"):')
narr("이 시험판은 R03의 실제 만남을 거친 뒤 고백 장면으로 이어집니다.",2)
line("return",2)
narr("도현이 약속 시각에 카페에 도착한다. 리아가 먼저 와 있다.")
rs=rows("### R04_00"); emit(rs[:4])
line('if r03_reply == "thanks":'); emit(rs[4:6],2)
line('elif r03_reply == "next":'); emit(rs[6:8],2)
line("else:"); emit(rs[8:10],2)
narr("음료를 주문하고 맞은편에 앉는다."); emit(rs[10:])
line("while not dating:")
line("menu:",2)
line(q(pair("너랑 연인으로 만나고 싶다고 말한다.","리아 씨와 연인으로 만나고 싶다고 말한다."))+":",3)
line("call ria_confess",4)
line(q("마음을 더 이야기하고 싶다고 말한다.")+" if not prepared:",3)
line("call ria_prepare",4)
line(q("이번 회차는 연애를 시작하지 않고 동료로 지낸다 — 동료 결말로 이어짐.")+":",3)
emit(rows("### R04_03","**R04_03_END"),4)
line("menu:",4)
line(q(pair("응, 동료로 지낼게.","네, 동료로 지낼게요."))+":",5)
emit(rows("**R04_03_END","### R04_04")[:3],6)
line("call end_common",6)
line("return",6)
line(q(pair("아니, 결정을 다시 고를게.","아니요, 결정을 다시 고를게요."))+":",5)
line("pass",6)
line('$ location = "금요일 저녁 · 조명이 켜진 산책길"')
narr("카페를 나와 도현이 제안한 짧은 산책길로 간다. 거리 조명이 켜진다.")
rs=rows("### R04_05","**R04_06A")
emit(rs[:2])
line('if memory.get("ria_r03_messages_received"):'); emit(rs[2:5],2)
line("else:")
say("r","앞으로는 나도 먼저 연락할게.","앞으로는 저도 먼저 연락할게요.",2)
say("d","좋아. 나도 기다리기만 하진 않을게.","좋아요. 저도 기다리기만 하진 않을게요.",2)
narr("둘이 조용한 길에서 잠깐 멈춘다.")
line("menu:")
line(q(pair("지금 너한테 입맞춤하고 싶은데, 괜찮아?","지금 리아 씨한테 입맞춤하고 싶은데, 괜찮아요?"))+":",2)
say("d","지금 너한테 입맞춤하고 싶은데, 괜찮아?","지금 리아 씨한테 입맞춤하고 싶은데, 괜찮아요?",3)
line("$ kiss_proposed = True",3)
rs=rows("**R04_06A","**R04_06B"); emit(rs[:1],3)
narr("두 사람이 짧게 입맞춤한다. 리아는 다시 눈을 마주치려다가 웃는다.",3)
line("$ first_kiss = True",3)
line('$ remember("ria_first_kiss","R04")',3)
emit(rs[1:],3)
line(q(pair("오늘은 조금 더 이야기하다가 인사하고 싶어.","오늘은 조금 더 이야기하다가 인사하고 싶어요."))+":",2)
say("d","오늘은 조금 더 이야기하다가 인사하고 싶어.","오늘은 조금 더 이야기하다가 인사하고 싶어요.",3)
emit(rows("**R04_06B","### R04_07"),3)
line('$ remember("ria_r04_talk_goodbye")',3)
emit(rows("### R04_07"))
line("return"); line()

line("label ria_prepare:",0)
emit(rows("### R04_02","**같은 장면에서"))
line("$ prepared = True")
line('$ remember("ria_prepared_conversation")')
narr("마음을 더 이야기했다. 이제 이 자리에서 관계를 어떻게 이어갈지 결정한다.")
line("return"); line()

line("label ria_confess:",0)
rs=rows("### R04_04"); emit(rs[:4])
line("$ dating = True")
line('$ remember("ria_confession_accepted")')
line('$ award_once("ria_R04","ria",5)')
narr("리아가 도현을 바라보다 웃는다.")
emit(rs[4:9])
line("if not prepared:"); emit(rs[9:],2)
line("return")
(BASE/"game/ria_r02_r04.rpy").write_text("\n".join(OUT)+"\n",encoding="utf-8")
print(json.dumps({"generated":"game/ria_r02_r04.rpy","lines":len(OUT)},ensure_ascii=True))


