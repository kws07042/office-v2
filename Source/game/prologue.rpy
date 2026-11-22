# 프롤로그 — 피칭 당일의 한 장면을 먼저 보여 주고 "두 달 전, 10월"로 돌아간다.
# 손의 주인은 밝히지 않는다. 각 루트 R16 피칭 장면에서 같은 질문을 되받아 회수한다.

default persistent.seen_prologue = False

label prologue:
    $ chapter = "프롤로그 · 석 달 뒤의 질문"
    $ location = "12월, 피칭 당일 · 클라이언트사 대회의실"
    if not persistent.seen_prologue:
        "숨소리까지 들릴 것 같은 회의실이었다."
        "스크린에는 우리 팀이 두 달 동안 만든 첫 장이 떠 있었다. 발표를 막 시작하려던 참이었다."
        "심사석 가운데 남자가 펜을 내려놓았다."
    "\"하나만 묻겠습니다.\""
    "\"이 팀, 석 달 뒤에도 있습니까?\""
    dn "아무도 바로 대답하지 못했다. 나도 그랬다."
    if not persistent.seen_prologue:
        dn "준비한 답은 있었다. 숫자로, 일정표로, 시험 계획으로. 그런데 그 질문은 숫자를 묻는 게 아니었다."
    $ cg("prologue_hands")
    "그때 책상 아래에서, 누군가 내 손등을 한 번 눌렀다."
    "짧게. 한 번. 괜찮다는 듯이."
    dn "그게 누구의 손이었는지 말하려면, 두 달 전으로 돌아가야 한다."
    if not persistent.seen_prologue:
        dn "편한 신발을 신고 오라던, 첫 출근 날로."
    "— 두 달 전, 10월 —"
    $ persistent.seen_prologue = True
    return
