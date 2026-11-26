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
    dn "아무도 바로 대답하지 못했다."
    if not persistent.seen_prologue:
        dn "일정표도 숫자도 다 외웠는데, 저 질문은 연습한 적이 없었다."
    $ cg("prologue_hands")
    "그때 누군가 책상 아래로 내 손등을 눌렀다."
    "내가 숨을 내쉴 때까지 그 손은 그대로였다."
    dn "그 팀에 처음 온 건 두 달 전이었다."
    if not persistent.seen_prologue:
        dn "첫 출근 안내에는 편한 신발을 신고 오라고 쓰여 있었다."
    "— 두 달 전, 10월 —"
    $ persistent.seen_prologue = True
    return
