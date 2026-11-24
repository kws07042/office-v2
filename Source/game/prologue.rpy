# 프롤로그 — 피칭 당일의 한 장면을 먼저 보여 주고 "두 달 전, 10월"로 돌아간다.
# 손의 주인은 밝히지 않는다. 각 루트 R16 피칭 장면에서 같은 질문을 되받아 회수한다.

default persistent.seen_prologue = False

label prologue:
    $ chapter = "프롤로그 · 석 달 뒤의 질문"
    $ location = "12월, 피칭 당일 · 클라이언트사 대회의실"
    if not persistent.seen_prologue:
        "회의실 끝자리에서 누가 숨을 들이켰다."
        "스크린에 두 달 동안 준비한 발표의 첫 장이 떴다. 첫마디를 떼려던 참이었다."
        "심사석 가운데 남자가 펜을 내려놓았다."
    "\"하나만 묻겠습니다.\""
    "\"이 팀, 석 달 뒤에도 있습니까?\""
    dn "대답이 바로 나오지 않았다. 나도 입을 못 뗐다."
    if not persistent.seen_prologue:
        dn "일정표도 숫자도 외웠다. 저 질문엔 뭘 꺼내야 하지."
    $ cg("prologue_hands")
    "그때 책상 아래에서, 누군가 내 손등을 한 번 눌렀다."
    "손끝이 잠깐 머물렀다. 괜찮다는 듯이."
    dn "누구 손이었냐고? 그 얘긴 두 달 전부터 해야 한다."
    if not persistent.seen_prologue:
        dn "편한 신발을 신고 오라던, 첫 출근 날로."
    "— 두 달 전, 10월 —"
    $ persistent.seen_prologue = True
    return
