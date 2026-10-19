# 유진 구현 대본 — yujin_r13_e01.rpy

```renpy
# Finale dialogue; all visual/voice production remains deferred.
label yujin_r13:
    if not dating or active_route != "yujin":
        return
    $ cream_focus = "yujin"
    $ chapter = "유진 R13 · 제가 원하는 도움"
    $ location = "재회 다음 날 금요일 오전 · 검토 전 빈 회의실"
    "유진이 십 분으로 줄어든 검토 시간을 확인했다. 자료를 두 장 골라 놓고 도현을 부른다."
    if memory.get("yujin_support_overstep") and memory.get("yujin_support_repair_status") == "open":
        y "지난번 먼저 설명하셨을 때요. 도와주신 마음은 알지만, 제 이유까지 도현 씨 말로 시작돼서 좀 서운했어요."
        d "요청하신 것보다 제가 앞서 나갔어요. 미안해요. 오늘은 먼저 듣고, 정한 부분만 돕고 싶어요."
        y "네. 긴장해도 제 설명은 제가 하고 싶어요. 막히면 어떤 도움을 부탁드릴지도 지금 정해 볼게요."
        $ remember("yujin_r13_path", "repair_open")
    elif memory.get("yujin_support_overstep"):
        if memory.get("yujin_support_repair_action_verified"):
            y "전에 맞췄던 방식은 좋았어요. 오늘은 시간이 달라졌으니까 새로 필요한 부분만 정해 볼까요?"
        else:
            y "먼저 물어보시기로 했던 거 기억해요. 오늘은 자료가 줄어서, 어느 부분을 부탁드릴지 먼저 말씀드릴래요."
        d "네. 전에 정한 걸 지우지 않고 오늘 순서에 맞춰 볼게요."
        $ remember("yujin_r13_path", "check_agreement")
    elif memory.get("yujin_support_action") in ("materials", "agreed_summary"):
        y "지난번엔 제 차례 기다려 주셔서 좋았어요. 오늘도 제가 이유를 설명할게요. 시간이 짧아서 도움받을 부분만 조금 바꾸고 싶어요."
        d "네. 이번에 필요한 쪽부터 말씀해 주세요."
        $ remember("yujin_r13_path", "new_scope")
    else:
        y "오늘은 제 의도를 먼저 설명하고 싶어요. 도현 씨께 부탁드릴 부분도 시작 전에 정하고 싶고요."
        d "어디까지 도우면 좋을지 지금 같이 보죠."
        $ remember("yujin_r13_path", "ask_current")
    if memory.get("yujin_r12_support_request"):
        d "어제 얘기한 것도 기억해요. 구체적인 자료랑 순서는 지금 확인하면 되겠네요."
    y "첫 질문에 제가 답하고, 수정 범위까지 말할 거예요. 남은 질문이 겹치면 그때 도와주세요."
    menu:
        "자료 두 장을 요청한 순서로 띄우고, 설명은 유진에게 맡긴다.":
            d "첫 답이 끝나면 두 번째 자료요. 넘어갈 때 신호 주시면 맞출게요."
            y "네. 손으로 페이지 짚을게요. 제가 말하는 속도로요."
            $ remember("yujin_r13_support_plan", "slides")
        "질문 순서를 정리하고 남은 시간만 조용히 알려주기로 한다.":
            d "질문이 겹치면 순서만 정리할게요. 끝나기 이 분 전에 메모 보여 드려도 돼요?"
            y "네. 제 설명을 줄일 부분은 제가 고를게요. 그 메모 부탁드려요."
            $ remember("yujin_r13_support_plan", "questions")
        "유진이 요청할 때만 정해 둔 질문 한 문장을 요약하기로 한다.":
            d "요약이 필요하면 먼저 말씀해 주세요. 질문만 묶고 답은 유진 씨께 넘길게요."
            y "네. 제가 ‘두 질문만 정리해 주세요’라고 할게요. 그 전에는 제가 이어 볼래요."
            $ remember("yujin_r13_support_plan", "requested_summary")
    $ remember("yujin_r13_agreed_scope")
    if memory.get("yujin_support_overstep") and not memory.get("yujin_support_repair_action_verified"):
        $ remember("yujin_support_repair_status", "agreed_pending_action")
    y "...오늘도 끝나면 이쪽 볼 거예요. 설명 끝났다고 웃는 건 제가 먼저 할게요~"
    d "그럼 저는 자료 넘기는 데만 집중해야겠네요. 미리 웃을까 봐요."
    $ award_once("yujin_R13", "yujin", 0)
    return

label yujin_r14:
    if not dating or active_route != "yujin" or not memory.get("yujin_r13_agreed_scope"):
        return
    $ chapter = "유진 R14 · 제가 설명할 순서"
    $ location = "같은 금요일 오전 · 검토 직전"
    menu:
        "합의한 역할로 준비하고 유진의 설명을 기다린다.":
            $ remember("yujin_r14_readiness", "ready")
        "시작 전에 합의한 신호와 지원 범위를 한 번 더 확인한다.":
            d "아까 정한 범위까지만요. 바뀌면 유진 씨가 먼저 말씀해 주시는 거죠?"
            y "네. 지금은 그대로예요. 같이 확인하니까 좀 덜 급해지네요."
            $ remember("yujin_r14_readiness", "rechecked")
        "연애를 마치고 동료로 지내고 싶다고 말한다 — 관계 종료 확인으로 이어짐.":
            d "업무는 합의한 대로 돕겠지만, 연애는 여기서 마치고 싶어요. 잠깐 쉬자는 뜻은 아니에요."
            menu:
                "연애를 마치겠다는 뜻을 확인한다.":
                    y "알겠어요. 오늘 일은 일로 마치고, 그 뒤에는 서로 시간 좀 두면 좋겠어요."
                    "검토에서는 정해 둔 역할을 수행하고 업무를 인계했다. 사적인 다음 약속은 잡지 않았다."
                    $ dating = False
                    $ remember("yujin_relationship_closed")
                    $ ending = "yujin_relationship_closed"
                    "유진 관계 종료 · 서로의 자리로"
                    return
                "결정을 취소하고, 합의한 역할로 검토를 준비한다.":
                    d "제가 원하는 걸 아직 정리하지 못했어요. 끝내겠다는 결정은 취소할게요. 뒤에 시간을 잡고 제 마음도 제대로 말하고 싶어요."
                    y "네. 그 얘기는 따로 듣고 싶어요. 지금 업무 약속은 그대로 준비할게요."
                    $ remember("yujin_r14_readiness", "reconsidered")
                "관계 종료 결정은 보류하고, 검토 뒤에 대화할 시간을 잡는다.":
                    d "지금 결론 내리지는 않을게요. 검토 뒤에 제 마음부터 차분히 말씀드리고 싶어요."
                    y "네. 업무가 끝나면 저도 제 마음 말씀드릴게요."
                    $ remember("yujin_r14_readiness", "talk_after")
    $ location = "같은 금요일 오전 · 짧은 검토 회의"
    "첫 질문이 나왔다. 유진이 시안을 짚으며 색을 고른 이유부터 설명했다."
    if memory["yujin_r13_support_plan"] == "slides":
        "도현은 유진이 첫 장 모서리를 짚을 때까지 기다렸다. 신호를 보고 두 번째 자료를 올리자 유진이 수정 범위를 이어 말했다."
        y "이 부분은 그대로 두고, 아래 문장 사이만 넓히겠습니다. 비교 자료의 오른쪽을 봐 주세요."
    elif memory["yujin_r13_support_plan"] == "questions":
        "질문이 겹치자 도현이 순서만 정리했다. 남은 시간 이 분을 메모로 보이자 유진은 핵심 근거를 골라 설명했다."
        d "수정 범위부터 답을 듣고, 적용 일정은 다음 질문으로 받을게요."
        y "네. 그 순서로 말씀드릴게요."
    else:
        y "도현 씨, 두 질문만 정리해 주실래요? 답은 제가 이어갈게요."
        d "지금 질문은 수정할 부분과 유지할 부분, 두 가지입니다. 유진 씨가 차례로 설명하겠습니다."
        "도현이 멈추자 유진이 두 항목을 직접 비교해 답했다."
    "검토를 마친 뒤 유진은 확정한 수정 사항을 자기 작업 노트에 적었다. 시안 아래에는 유진의 이름이 남았다."
    $ remember("yujin_support_alignment_verified")
    $ remember("yujin_r14_performed_plan", memory["yujin_r13_support_plan"])
    if memory.get("yujin_support_overstep"):
        $ remember("yujin_support_repair_action_verified")
        $ remember("yujin_support_repair_status", "resolved")
    $ location = "같은 금요일 퇴근 후 · 회사 앞"
    if memory.get("yujin_r14_readiness") in ("talk_after", "reconsidered"):
        d "아까 제 마음을 말한다고 했죠. 저는 아직 서툴 때 먼저 끝낼 말부터 고르려 했어요. 지금은 유진 씨와 계속 만나고 싶어요. 어려운 말도 피하지 않고요."
        y "저는 무슨 결정인지 기다리는 시간이 힘들었어요. 계속 만나고 싶다는 말은 저도 같아요. 다음엔 정해지지 않은 건 정해지지 않았다고 먼저 말해 주세요."
        d "네. 오늘처럼 취소한 결정도 없던 말로 넘기지 않을게요."
        $ remember("yujin_r14_relationship_talk_completed")
    if memory.get("yujin_support_overstep"):
        y "오늘은 제가 끝까지 말했고, 도현 씨는 약속한 데서 도와주셨어요. 저는 그게 좋았어요."
    else:
        y "이번에도 제가 설명할 수 있었어요. 오늘 정한 도움도 딱 필요한 때 왔고요."
    d "이제 웃으셔도 되는 시간이죠? 저도 좀 기다렸어요."
    y "...지금은 먼저 웃어 주셔도 되는데요~"
    $ remember("yujin_r14_complete")
    $ award_once("yujin_R14", "yujin", 8)
    return

label yujin_r15:
    if not dating or active_route != "yujin" or not memory.get("yujin_support_alignment_verified"):
        return
    $ chapter = "유진 R15 · 다음에도 제가 말할게요"
    $ location = "다음 날 토요일 저녁 · 유진의 집"
    "유진이 작업 수첩을 서랍에 넣었다. 식탁에는 내일 같이 볼 개인 노트와 차 두 잔만 남겼다."
    y "오늘은 도와달라는 말보다 같이 있고 싶다는 말을 먼저 하려고요. 그런데... 그 말도 떨리네요."
    d "저는 듣고 싶어서 조금 기다리고 있었어요. 너무 오래 준비하시면 제가 먼저 말할 뻔했고요."
    y "그럼 다음에는 기다리지만 말고 먼저 해 주세요. 저도 제 말 고르고 있을 테니까."
    menu:
        "만나고 싶은 날에는 이유를 찾기 전에 서로 말하자고 한다.":
            d "같이 보고 싶은 전시 없어도 부를게요. 보고 싶다는 말부터요."
            y "네. 초대 문장보다 이름부터 찾기로 한 약속, 계속할래요."
            $ remember("yujin_r15_future", "say_first")
        "서로 작업을 보여 주되, 도와줄 범위는 매번 먼저 묻자고 한다.":
            d "구경해 달라는 날이랑 도와달라는 날, 먼저 물어볼게요. 제 노트도 그렇게 말씀드리고요."
            y "좋아요. 오늘은 구경만 해 주셔도 되고... 옆에는 조금 오래 계셔도 돼요~"
            $ remember("yujin_r15_future", "ask_scope")
        "함께 있는 날과 각자 쉬는 날을 같이 고르자고 한다.":
            d "각자 쉬는 날도 남겨 두고 싶어요. 그날 보고 싶어지면 그 마음도 말하고요."
            y "네. 쉬자는 말이 싫다는 뜻은 아닌 걸, 서로 짐작하지 않게요."
            $ remember("yujin_r15_future", "rest_balance")
    "유진이 빈 컵을 치운 뒤 돌아왔다. 문가에서 머뭇거리던 시선이 도현에게 닿는다."
    y "오늘 밤은 같이 있고 싶어요. 도현 씨도 괜찮으시면요."
    menu:
        "나도 함께 있고 싶다고 답한다 — 친밀한 장면으로 이어짐.":
            d "네. 저도 같이 있고 싶어요."
            y "분위기 조금 바꿔 보고 싶기도 해요. 특별한 의상 같이 골라 볼까요? 지금처럼 편하게 있어도 좋고요."
            menu:
                "지금의 편한 생활복이 좋다고 말한다.":
                    d "오늘은 지금 모습이 좋아요. 옆에서 편하게 쉬는 유진 씨요."
                    y "그 말 들으니까 준비 다 한 것 같네요~"
                    $ remember("yujin_r15_outfit", "home")
                "코스프레 의상을 함께 고르고 싶다고 말한다.":
                    "두 사람이 마음에 드는 특별 의상을 함께 골랐다. 갈아입고 나온 유진이 잠깐 문가에 멈췄다."
                    y "...조용히 보시면 제가 먼저 부끄러워질 것 같은데요."
                    d "잘 어울려요. 다른 모습도 유진 씨가 먼저 보여 주고 싶었다는 게 좋아요."
                    y "네. 그 말은 준비한 답보다 좋네요."
                    $ remember("yujin_r15_outfit", "cosplay")
                "유진이 오늘 더 편한 쪽을 먼저 고르고 내 마음도 말한다.":
                    y "오늘은 편한 쪽이요. 다른 의상은 다음에 같이 고르고 싶어요."
                    d "저도 지금이 좋아요. 다음에 고르는 날도 같이 정해요."
                    $ remember("yujin_r15_outfit", "home")
                    $ remember("yujin_r15_outfit_delegated")
            call event_sequence("yujin_r15", memory["yujin_r15_outfit"])
            if not event_main_reached:
                "(거사 — 장면 생략)"
            $ remember("yujin_r15_intimacy", "shared")
            y "다음에 하고 싶은 말도 제가 먼저 할 수 있을 것 같아요. 오늘처럼 도현 씨 마음도 듣고요."
            d "저도 제 말 남겨 둘게요. 기다리시기만 하진 않게요."
        "오늘은 귀가해서 쉬고, 다음에도 만나고 싶다고 말한다.":
            d "오늘은 집에서 쉬고 싶어요. 내일 같이 노트 보기로 한 건 그대로고요."
            y "네. 차는 마저 드시고 가세요. 내일도 제가 보여 드릴 페이지 남아 있어요."
            $ remember("yujin_r15_intimacy", "deferred")
        "조금 더 이야기한 뒤 잠은 각자 집에서 자고 싶다고 말한다.":
            d "오늘은 조금 더 이야기하고 갈래요. 밤에는 각자 쉬고요."
            y "좋아요. 제가 말하다가 늦어지면 시계도 같이 봐 주세요~"
            "서로 가장 좋았던 말을 하나씩 고른 뒤 인사를 나눴다."
            $ remember("yujin_r15_intimacy", "talk")
    $ remember("yujin_r15_complete")
    $ award_once("yujin_R15", "yujin", 5)
    return

label yujin_r16:
    if not dating or active_route != "yujin" or not memory.get("yujin_r14_complete") or not memory.get("yujin_r15_complete"):
        return
    $ chapter = "유진 R16 · 제 이름으로, 우리 마음으로"
    $ location = "같은 주 일요일 저녁 · 동네 카페"
    "유진이 금요일 검토 의견을 반영한 최종 시안을 보여 줬다. 수정한 줄과 자기 이름을 확인하고 파일을 저장했다."
    y "월요일에 전달할 최종본이에요. 제 이름 볼 때마다 설명 끝내고 웃었던 순간도 생각날 것 같아요."
    d "저는 제 차례 기다리던 순간이요. 옆에서 같이 마친 일이라 좋네요."
    $ remember("yujin_design_state", "검토 의견을 반영한 최종 시안 저장, 다음 출근일 전달 예정")
    "도현은 두 장을 접어 만든 기록집 초안을 꺼냈다. 유진은 먼저 넘기지 않고 도현이 펼치는 쪽을 기다렸다."
    if memory.get("yujin_r10_page") == "entrance_bench":
        if memory.get("yujin_o03_photo_taken"):
            d "오늘 찍은 의자 사진은 후보로 옆에 뒀어요. 이 초안엔 우선 날짜랑 기억부터 넣었고요."
        else:
            d "그 의자는 아직 촬영 후보예요. 여기는 먼저 같이 앉았던 날짜만 남겼어요."
    elif memory.get("yujin_r10_page") == "one_sentence":
        d "티켓 옆에 적었던 말요. 오늘 초안의 한 페이지에 그대로 놓아 봤어요."
    elif memory.get("yujin_r10_page") == "open_space":
        d "빈칸은 아직 남겨 뒀어요. 다음 만남 뒤에 적으려고 고른 칸이니까요."
    else:
        d "아직 두 장짜리예요. 완성되기 전에 먼저 보여 드리고 싶었어요."
    $ remember("yujin_r16_booklet_state", "두 장 접지 초안 공유, 완성된 책 아님")
    if memory.get("yujin_disclosed_to") == "jihyun":
        y "팀장님이 두 사람 다음에도 같이 보자고 하셨어요. 아직 다른 분들께는 말씀 안 하셨대요."
    else:
        y "우리 얘기는 아직 둘이 먼저 아는 걸로요. 나중에 말할 때도 같이 정하고 싶어요."
    if memory.get("yujin_support_overstep"):
        y "도움을 정하는 건 아직 연습하겠지만, 이번엔 말한 걸 행동으로 지켜 주셔서 좋았어요."
    else:
        y "제 얘기 기다려 주시는 것도 좋고, 필요한 순간에 같이 움직여 주시는 것도 좋아요."
    y "저 다음 작업도 제 이름으로 해 보고 싶어요. 그 옆에서 도현 씨는 계속 만나고 싶고요."
    menu:
        "앞으로도 서로 먼저 부르며 연인으로 만나고 싶다고 답한다.":
            d "저도 계속 만나고 싶어요. 다음 작업 설명보다 보고 싶다는 말부터 듣는 날도 만들고요."
            y "그건 제가 또 먼저 할 수도 있어요~"
            $ remember("yujin_r16_promise", "keep_inviting")
        "각자 하던 일과 취미를 이어가면서 함께할 날을 정하자고 한다.":
            d "저도 유진 씨 다음 작업 옆에 제 노트 들고 올게요. 각자 하는 일도, 만나는 날도 남겨 두고요."
            y "네. 다음 페이지가 둘 다 있는 거네요."
            $ remember("yujin_r16_promise", "own_pages")
        "도움을 주고받을 때도 연인으로서 자기 마음부터 말하자고 한다.":
            d "앞으로도 같이 있고 싶어요. 잘 도와드리려다가 제 마음을 늦게 말하지는 않을게요. 제가 원하는 것도 먼저 말씀드릴래요."
            y "네. 저도 잘해 드리고 싶다는 말 뒤에 보고 싶다는 마음 숨기지 않을래요."
            $ remember("yujin_r16_promise", "say_own_needs")
    "유진이 초안의 모서리를 가볍게 눌렀다. 빈 곳을 채우기보다 도현 쪽으로 조금 더 가까이 앉는다."
    y "도현 씨. ...다음에도 저랑 만나 주세요."
    d "네. 이번에는 저도 먼저 약속할게요."
    $ remember("yujin_route_completed")
    $ persistent.local_yujin_ending = True
    $ ending = "yujin_good"
    $ award_once("yujin_R16", "yujin", 4)
    "유진 본편 결말 · 제 이름으로, 우리 마음으로"
    return

label yujin_e01:
    if not dating or active_route != "yujin" or not memory.get("yujin_route_completed"):
        return
    $ chapter = "유진 E01 · 제 이름 옆의 우리"
    $ location = "약 반년 뒤 겨울의 휴일 오후 · 유진의 집"
    "그 시안은 다음 출근일에 전달했고 납품도 마쳤다. 이후 유진은 창가 그림에서 시작한 작은 개인 작업 묶음을 완성했다. 오늘은 인쇄한 소개지를 도현에게 먼저 보여 준다."
    y "이번에는 제 개인 작업이에요. 제 이름만 적었다가, 처음 보여 주고 싶은 사람 이름도 따로 써 놨어요."
    d "그쪽은 제가 맞힐 수 있을 것 같은데요."
    y "네. 오늘도 오셨으니까 힌트는 여기까지요~"
    "도현도 몇 달 동안 직접 찍은 사진과 짧은 글을 모아 완성한 작은 기록집을 건넸다. 유진은 예전에 봤던 접지 초안과 완성본을 나란히 놓았다."
    if memory.get("yujin_r10_page") == "entrance_bench":
        "나중에 다시 찾아가 촬영한 입구의 긴 의자 사진을 함께 펼쳤다."
        y "이제 사진도 있네요. 저는 아직 그날 옆자리부터 생각나요."
    elif memory.get("yujin_r10_page") == "one_sentence":
        y "이 한 문장요. 티켓 옆에서 책 한 페이지로 옮겨 왔네요. 저는 아직 여기서 좀 오래 머물래요."
    elif memory.get("yujin_r10_page") == "open_space":
        y "남겨 둔 칸, 결국 다음 만남 뒤에 채우셨네요. 약속이 먼저였던 거 기억해요."
    $ remember("yujin_epilogue_booklet_state", "이후 직접 촬영·글 정리를 마쳐 작은 인쇄 기록집 완성")
    if memory.get("yujin_o01_status") == "completed":
        y "전시 그림 보고 감상이 달랐던 날도 적어 뒀어요. 같은 걸 봐도 대답까지 같을 필요는 없어서 좋아요."
    if memory.get("yujin_o02_status") == "completed":
        y "작은 스케치 보여 드렸던 것도요. 빛이 겹친 컵 그림, 그 노트에 아직 있어요."
    if memory.get("yujin_o03_status") == "completed":
        y "이번엔 제가 도현 씨 취향 고르기로 했던 날도 생각나요. 다음 후보도 하나 남겨 뒀고요~"
    if memory.get("yujin_r11_music") == "yujin_calm":
        "함께 들었던 ‘창가에 남은 오후’를 골라 두고 두 사람은 마지막 페이지까지 읽었다."
    elif memory.get("yujin_r11_music") == "dohyun_bright":
        y "나중에 나갈 때는 ‘한 정거장 더’ 고를래요. 오늘은 같이 걷는 쪽으로요."
    elif memory.get("yujin_r11_music") == "both":
        y "책 보는 동안은 조용한 쪽, 나갈 때는 걸어가던 쪽. 그때 고른 두 곡 순서도 남겨 뒀어요."
    if memory.get("yujin_support_repair_action_verified"):
        y "새로 부탁할 때도 먼저 물어봐 주시는 거 좋아요. 그날 정한 게 그날만의 말은 아니어서요."
    y "내년에는 이 작업으로 전시도 신청해 보고 싶어요. 휴가에는 둘이 며칠 다녀오고 싶고요. 도현 씨는 어때요?"
    menu:
        "전시 모집 일정을 먼저 찾고, 그 뒤 함께 쉴 날을 고르자고 한다.":
            d "전시 신청부터 같이 찾아볼까요? 여행은 서로 가능한 날을 그다음에 확인하고요."
            $ remember("yujin_e01_plan", "exhibition_first")
        "서로 가능한 휴가 기간부터 적고 전시 일정과 맞춰 보자고 한다.":
            d "저는 둘이 쉴 날부터 적어 보고 싶어요. 신청 일정이 정해지면 같이 맞춰 봐요."
            $ remember("yujin_e01_plan", "holiday_first")
        "각자 후보를 하나씩 가져와 다음 주말에 함께 고르자고 한다.":
            d "전시랑 가 보고 싶은 동네 후보를 하나씩 가져올까요? 다음 주말에 같이 고르고요."
            $ remember("yujin_e01_plan", "bring_candidates")
    y "좋아요. 아직 떠난 건 아니지만, 같이 고를 사람이 정해진 건 좋네요."
    d "저도요. 다음 주말에는 제가 먼저 부를게요."
    y "그럼 오늘은 제가 한 번 더요. 도현 씨, 기록집 덮고 저도 좀 봐 주세요~"
    $ remember("yujin_e01_travel_state", "전시 신청·휴가 여행 계획을 함께 시작함, 예약·참가·여행 완료 아님")
    $ remember("yujin_epilogue_completed")
    $ award_once("yujin_E01", "yujin", 8)
    "유진 후일담 · 제 이름 옆의 우리"
    return

```
