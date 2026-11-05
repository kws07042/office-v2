# Finale dialogue; all visual/voice production remains deferred.
label yujin_r13:
    $ progression_enter("yujin_r13")
    $ progression_checkpoint("yujin_r13")
    if not dating or active_route != "yujin":
        $ progression_note_ending()
        return
    $ cream_focus = "yujin"
    $ chapter = "유진 R13 · 제가 원하는 도움"
    $ location = "재회 다음 날 금요일 오전 · 검토 전 빈 회의실"
    "유진이 십 분으로 줄어든 검토 시간을 확인했다. 자료를 두 장 골라 놓고 도현을 부른다."
    if memory.get("yujin_support_overstep") and memory.get("yujin_support_repair_status") == "open":
        y "지난번엔 제가 말하기도 전에 도현 씨 설명부터 나왔어요. 그건 조금 서운했어요."
        d "자료 설명이면 빨리 끝날 줄 알았어요. ...제가 말할 차례는 아니었는데. 미안해요."
        y "저도 그 설명 할 수 있었어요. 좀 늦더라도요."
        "도현이 펼치려던 자료를 유진 쪽으로 돌렸다. 유진은 첫 장을 앞에 놓았다."
        y "오늘은 제가 여기부터 할게요. 도와주셨으면 하는 건 그다음이에요."
        $ remember("yujin_r13_path", "repair_open")
    elif memory.get("yujin_support_overstep"):
        if memory.get("yujin_support_repair_action_verified"):
            y "전에 맞췄던 방식은 좋았어요. 오늘은 시간이 달라졌으니까 새로 필요한 부분만 정해 볼까요?"
        else:
            y "먼저 물어보시기로 했던 거 기억해요. 오늘은 자료가 줄어서, 어느 부분을 부탁드릴지 먼저 말씀드릴래요."
        d "네. 오늘 두 장 중 어느 쪽부터예요?"
        $ remember("yujin_r13_path", "check_agreement")
    elif memory.get("yujin_support_action") in ("materials", "agreed_summary"):
        y "지난번처럼 제가 이유부터 말할게요. 오늘은 십 분이라... 두 장 중에 먼저 뭘 보이느냐가 좀 걸려요."
        d "둘 다 앞에 놓고 볼까요? 제가 넘겨야 할 때도 짚어 주세요."
        $ remember("yujin_r13_path", "new_scope")
    else:
        y "첫 답은 제가 할게요. 두 장 다 보여 드리고 싶은데 십 분밖에 없네요."
        d "그러면 설명은 유진 씨, 필요한 데서 제가 거들고요. 어디가 걸려요?"
        $ remember("yujin_r13_path", "ask_current")
    if memory.get("yujin_r12_support_request"):
        d "어제 부탁하신 것 기억해요. 이 두 장으로 맞춰 볼게요."
    y "첫 질문에 제가 답하고, 수정 범위까지 말할 거예요. 남은 질문이 겹치면 그때 도와주세요."
    $ progression_enter("yujin_r13.choice01")
    $ progression_checkpoint("yujin_r13.choice01")
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
    if memory["yujin_r13_support_plan"] == "slides":
        d "그럼 저는 자료 넘기는 데 집중해야겠네요. 미리 웃을까 봐요."
    elif memory["yujin_r13_support_plan"] == "questions":
        d "그럼 저는 질문 순서랑 시간 메모에 집중할게요. 미리 웃을까 봐요."
    else:
        d "그럼 부탁하실 때까지 기다릴게요. 먼저 웃어 버리지만 않으면 되겠네요."
    $ award_once("yujin_R13", "yujin", 0)
    $ progression_note_ending()
    return

label yujin_r14:
    $ progression_enter("yujin_r14")
    $ progression_checkpoint("yujin_r14")
    if not dating or active_route != "yujin" or not memory.get("yujin_r13_agreed_scope"):
        $ progression_note_ending()
        return
    $ chapter = "유진 R14 · 제가 설명할 순서"
    $ location = "같은 금요일 오전 · 검토 직전"
    $ progression_enter("yujin_r14.choice01")
    $ progression_checkpoint("yujin_r14.choice01")
    menu:
        "합의한 역할로 준비하고 유진의 설명을 기다린다.":
            $ remember("yujin_r14_readiness", "ready")
        "시작 전에 합의한 신호와 지원 범위를 한 번 더 확인한다.":
            d "아까 정한 범위까지만요. 바뀌면 유진 씨가 먼저 말씀해 주시는 거죠?"
            y "네. 지금은 그대로예요. 같이 확인하니까 좀 덜 급해지네요."
            $ remember("yujin_r14_readiness", "rechecked")
        "검토를 마친 뒤, 둘의 관계에 관해 따로 이야기하자고 한다.":
            d "퇴근하고 잠깐 이야기할 수 있을까요? 오늘은 회사 얘기 말고, 저희 둘 얘기요."
            y "네. 저도 듣고 싶어요. 지금은 이 두 장부터 끝내고요."
            $ remember("yujin_r14_readiness", "relationship_talk")
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
    $ location = "같은 금요일 퇴근 후 · 회사 앞"
    if memory.get("yujin_r14_readiness") == "relationship_talk":
        "사람들이 빠져나간 뒤, 둘은 정류장 쪽으로 바로 가지 않고 회사 앞 벤치에 앉았다."
        y "아까 하시려던 얘기요. 지금은 자료 안 봐도 되니까, 도현 씨 얼굴 보고 들을게요."
        $ progression_enter("yujin_r14.choice02")
        $ progression_checkpoint("yujin_r14.choice02")
        menu:
            "연애를 마치고 동료로 지내겠다는 뜻을 분명히 전한다.":
                d "저는 연인으로는 여기까지 만나고 싶어요. 잠깐 쉬자는 뜻은 아니에요."
                "유진은 가방 끈을 쥐었다가 천천히 놓았다."
                y "...알겠어요. 이유는 듣고 싶지만, 대답을 바꾸시라고 하지는 않을게요."
                d "좋아하는 마음만으로 계속 만나겠다고 약속하기는 어려워요. 유진 씨가 오늘 뭘 잘못하셨다는 뜻은 아니고요."
                y "네. 오늘 일은 함께 마쳤고요. 이제는 저도 혼자 돌아갈게요."
                "도현은 붙잡지 않고 인사했다. 사적인 다음 약속은 잡지 않았다."
                $ dating = False
                $ remember("yujin_relationship_closed")
                $ ending = "yujin_relationship_closed"
                "유진 관계 종료 · 서로의 자리로"
                $ progression_note_ending()
                return
            "일 이야기에 가려졌던 좋아하는 마음을 먼저 말한다.":
                d "요즘 만나면 작업 얘기부터 했잖아요. 오늘은 유진 씨가 보고 싶어서 기다렸다고 먼저 말하고 싶었어요."
                y "...그 말 하시려고 따로 앉으신 거예요?"
                d "네. 걸으면서 하면 또 버스 언제 오느냐는 얘기로 샐 것 같아서요."
                "유진이 벤치 등받이에 기대다가 웃었다."
                y "저 지금 꽤 긴장했는데요. 그럼 버스 한 대는 놓치셔야겠어요."
                d "두 대째부터는 같이 시간표 봐요."
                y "네. 첫 번째는 제 얘기 들으시고요."
                $ remember("yujin_r14_readiness", "reassured")
            "연애하면서 마음에 걸렸던 일을 꺼내고, 계속 만나고 싶은 마음도 전한다.":
                if memory.get("yujin_support_overstep"):
                    d "전에 제가 먼저 설명했던 일요. 사과한 뒤에도 또 앞서갈까 봐, 둘이 있을 때까지 말을 재게 되더라고요."
                    y "오늘 기다려 주신 건 좋았어요. 그렇다고 저한테 하고 싶은 말까지 다 참으시면, 저는 그것도 모르잖아요."
                    d "네. 저는 계속 만나고 싶어요. 실수 안 하겠다는 말만 하느라 그 말을 빼먹었네요."
                    y "저도 계속 만나고 싶어요. 아직 서운한 게 남으면 그때 말씀드릴게요."
                else:
                    d "같이 만나서도 자꾸 작업부터 꺼내게 돼요. 유진 씨랑 할 말이 그것밖에 없는 사람처럼요."
                    y "저도 보여 드릴 게 있어야 만나자고 하기 쉽더라고요. 도현 씨는 이제 그런 핑계 없어도 오실 것 같은데."
                    d "네. 오늘도 그래서 기다렸어요. 앞으로도 만나고 싶고요."
                    y "...그럼 다음엔 빈손으로 와 보세요. 저도 노트는 두고 나와 볼게요."
                $ remember("yujin_r14_readiness", "talk_after")
        $ remember("yujin_r14_relationship_talk_completed")
    if memory.get("yujin_r14_readiness") == "talk_after":
        "도현은 손을 내밀려다 유진이 가방을 고쳐 메는 동안 기다렸다. 유진이 먼저 옆으로 한 걸음 다가왔다."
        y "오늘 다 정리해서 말하려고 하진 말아요. 정류장까지는 그냥 같이 걷고 싶어요."
        d "네. 제 얘기도 걷다가 생각나면 할게요."
        "둘은 나란히 걸었다. 건널목 앞에서 멈췄을 때 유진의 손이 도현의 손등에 잠깐 닿았다."
    elif memory.get("yujin_r14_readiness") != "reassured":
        if memory.get("yujin_support_overstep"):
            y "오늘은 제가 마지막 말까지 했네요. 도현 씨 쪽 봤을 때도 안 급해져서 좋았어요."
        else:
            y "오늘도 끝까지 했네요. 중간에 도현 씨 쪽 한 번 봤는데, 아셨어요?"
        d "이제 웃으셔도 되는 시간이죠? 저도 좀 기다렸어요."
        y "...지금은 먼저 웃어 주셔도 되는데요~"
        "도현이 웃자 유진이 들고 있던 가방 끈을 다시 고쳐 쥐었다."
        y "아, 잠깐만요. 끝나면 제가 먼저 웃어 드리려고 했는데."
        d "그럼 다시 기다릴까요?"
        y "아뇨. 이제 그만 기다리고 같이 가요."
        "유진이 먼저 걸음을 뗐다. 도현이 따라오자 이번에는 돌아보며 웃었다."
    $ remember("yujin_support_alignment_verified")
    $ remember("yujin_r14_performed_plan", memory["yujin_r13_support_plan"])
    if memory.get("yujin_support_overstep"):
        $ remember("yujin_support_repair_action_verified")
        $ remember("yujin_support_repair_status", "resolved")
    $ remember("yujin_r14_complete")
    $ award_once("yujin_R14", "yujin", 8)
    $ progression_note_ending()
    return

label yujin_r15:
    $ progression_enter("yujin_r15")
    $ progression_checkpoint("yujin_r15")
    if not dating or active_route != "yujin" or not memory.get("yujin_support_alignment_verified"):
        $ progression_note_ending()
        return
    $ chapter = "유진 R15 · 다음에도 제가 말할게요"
    $ location = "다음 날 토요일 저녁 · 유진의 집"
    "유진은 작업 수첩을 서랍에 넣고 도현이 앉은 맞은편을 봤다. 자기 옆의 빈 자리를 손바닥으로 가볍게 쳤다."
    y "오늘은 여기요. 제가 옆에 앉으라고 하기 전까지 계속 저쪽에 계실 생각이었어요?"
    d "맞은편이면 얼굴 잘 보이니까요."
    y "오늘은 옆이 좋아요. ...다른 사람한테는 그 자리 안 내줄래요."
    d "제 자리 예약해 두신 거예요?"
    y "네. 앉을지는 도현 씨가 고르시고요. 저는 지금 좀 오래 기다린 척할래요~"
    "도현이 자리를 옮기자 유진은 준비해 둔 과자를 둘 사이에 놓았다. 접시는 하나였다."
    if memory.get("yujin_r14_readiness") in ("talk_after", "reconsidered"):
        y "어제 얘기가 다 끝났다고 생각하진 않아요. 그래도 오늘 옆에 계셨으면 해서 제가 먼저 불렀어요."
        d "네. 저도 그 마음으로 왔어요."
    y "오늘은 도와달라는 말보다 같이 있고 싶다는 말을 먼저 할게요. 연습은 했는데... 지금이 더 쉽네요."
    $ progression_enter("yujin_r15.choice01")
    $ progression_checkpoint("yujin_r15.choice01")
    menu:
        "만나고 싶은 날에는 이유를 찾기 전에 서로 말하자고 한다.":
            d "볼 전시 없어도 부를게요. 오늘처럼 옆에 앉아 있어도 좋고요."
            y "그럼 안내지 모으는 건 좀 쉬어야겠네요. 만나자고 하려고 괜히 하나씩 챙겼는데~"
            $ remember("yujin_r15_future", "say_first")
        "서로 작업을 보여 주되, 도와줄 범위는 매번 먼저 묻자고 한다.":
            d "구경해 달라는 날이랑 도와달라는 날, 먼저 물어볼게요. 제 노트도 그렇게 말씀드리고요."
            y "좋아요. 오늘은 아무것도 안 보여 드릴래요. 대신 이 자리는 조금 오래 쓰세요~"
            $ remember("yujin_r15_future", "ask_scope")
        "함께 있는 날과 각자 쉬는 날을 같이 고르자고 한다.":
            d "쉬는 날엔 저도 집에서 늦잠 잘래요. 보고 싶으면 일어나서 연락하고요."
            y "네. 먼저 깨면 제 아침부터 먹을게요. 답장 없는 걸로 혼자 삐치기 전에요~"
            d "일어나면 그 자랑부터 볼게요."
            y "그럼 예쁘게 담아야겠네요. 배고프면 먼저 먹긴 할 거예요!"
            $ remember("yujin_r15_future", "rest_balance")
    "과자를 나눠 먹은 뒤 유진이 접시를 치웠다. 돌아와서는 도현 옆의 자기 자리에 다시 앉았다."
    y "오늘 밤은 같이 있고 싶어요. 도현 씨도 괜찮으시면요."
    $ progression_enter("yujin_r15.choice02")
    $ progression_checkpoint("yujin_r15.choice02")
    menu:
        "나도 함께 있고 싶다고 답한다 — 친밀한 장면으로 이어짐.":
            d "네. 저도 같이 있고 싶어요."
            y "분위기 조금 바꿔 보고 싶기도 해요. 특별한 의상 같이 골라 볼까요? 지금처럼 편하게 있어도 좋고요."
            $ progression_enter("yujin_r15.choice03")
            $ progression_checkpoint("yujin_r15.choice03")
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
            y "아까 연습한 말, 중간부터 다 잊었어요."
            d "중간부터가 더 좋았는데요."
            "유진이 대답하려다 웃었다. 도현도 다음 말을 재촉하지 않았다."
        "오늘은 귀가해서 쉬고, 다음에도 만나고 싶다고 말한다.":
            d "오늘은 집에서 쉬고 싶어요. 내일 같이 노트 보기로 한 건 그대로고요."
            y "네. 남은 과자는 싸 드릴게요. 내일도 같이 볼 페이지는 남아 있어요."
            $ remember("yujin_r15_intimacy", "deferred")
        "조금 더 이야기한 뒤 잠은 각자 집에서 자고 싶다고 말한다.":
            d "오늘은 조금 더 이야기하고 갈래요. 밤에는 각자 쉬고요."
            y "좋아요. 제가 말하다가 늦어지면 시계도 같이 봐 주세요~"
            "서로 가장 좋았던 말을 하나씩 고른 뒤 인사를 나눴다."
            $ remember("yujin_r15_intimacy", "talk")
    $ remember("yujin_r15_complete")
    $ award_once("yujin_R15", "yujin", 5)
    $ progression_note_ending()
    return

label yujin_r16:
    $ progression_enter("yujin_r16")
    $ progression_checkpoint("yujin_r16")
    if not dating or active_route != "yujin" or not memory.get("yujin_r14_complete") or not memory.get("yujin_r15_complete"):
        $ progression_note_ending()
        return
    $ chapter = "유진 R16 · 제 이름으로, 우리 마음으로"
    $ location = "같은 주 일요일 저녁 · 동네 카페"
    "유진이 검토 의견을 반영한 최종 시안을 저장했다. 월요일 전달할 파일 이름 끝에 자기 이름을 확인하고 화면을 닫았다."
    y "됐어요. 오늘은 이걸로 끝. 도현 씨 가져오신 것도 볼래요."
    $ remember("yujin_design_state", "검토 의견을 반영한 최종 시안 저장, 다음 출근일 전달 예정")
    "도현은 두 장을 접어 만든 기록집 초안을 꺼냈다. 유진은 고른 한쪽만 보고 다시 도현에게 돌려줬다."
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
        y "팀장님 답장 기억나요? 수정 의견 안 보태신다고요. 축하한다는 말만 들으니까 기분 좋았어요~"
    else:
        "유진은 개인 노트를 펼쳤다. 교제 이야기를 다른 사람에게 전하는 메시지는 보내지 않았다."
    if memory.get("yujin_support_overstep"):
        "도현이 설명을 시작하려다 멈추자 유진은 이미 고른 페이지를 펼쳐 보여 줬다."
        y "여기요. 이번엔 제가 궁금한 쪽부터 볼래요."
    else:
        "유진이 도현의 초안 옆에 자기 노트를 놓았다."
        y "이쪽도 펼쳐 놓을까요? 옆에 두고 보고 싶어요."
    "유진은 자기 노트를 덮어 도현의 초안 옆에 두었다. 가방을 챙겨 일어난 뒤 도현 곁의 빈자리로 옮겨 앉았다."
    y "새 작업은 제 이름으로 할래요. 다 못 그린 날에도 도현 씨는 오셨으면 좋겠고요."
    d "제 옆자리부터 예약하시네요."
    y "네. 이번엔 제가 먼저요."
    $ progression_enter("yujin_r16.choice01")
    $ progression_checkpoint("yujin_r16.choice01")
    menu:
        "앞으로도 서로 먼저 부르며 연인으로 만나고 싶다고 답한다.":
            d "저도 계속 만나고 싶어요. 다음 작업 설명보다 보고 싶다는 말부터 듣는 날도 만들고요."
            y "그건 제가 또 먼저 할 수도 있어요~"
            $ remember("yujin_r16_promise", "keep_inviting")
        "각자 하던 일과 취미를 이어가면서 함께할 날을 정하자고 한다.":
            d "저도 유진 씨 다음 작업 옆에 제 노트 들고 올게요. 각자 하는 일도, 만나는 날도 남겨 두고요."
            y "네. 각자 하던 것도 들려주세요. 제가 먼저 옆에 앉았다고 놀리지는 마시고요~"
            $ remember("yujin_r16_promise", "own_pages")
        "도움을 주고받을 때도 연인으로서 자기 마음부터 말하자고 한다.":
            d "앞으로도 같이 있고 싶어요. 잘 도와드리려다가 제 마음을 늦게 말하지는 않을게요. 제가 원하는 것도 먼저 말씀드릴래요."
            y "네. 저도 잘해 드리고 싶다는 말 뒤에 보고 싶다는 마음 숨기지 않을래요."
            $ remember("yujin_r16_promise", "say_own_needs")
    "유진은 도현 쪽으로 조금 더 가까이 앉았다. 도현이 초안을 다시 펼치려 하자 조용히 손으로 덮었다."
    y "다음 장은 나중에 볼래요. 지금은 도현 씨랑 얘기하고 싶어요."
    d "좋아요. 무슨 얘기부터요?"
    y "아까 제가 먼저 옆에 앉은 얘기요. ...도현 씨도 좋아하셨잖아요?"
    "이번에는 도현이 바로 대답하지 못했다. 유진이 그 표정을 보고 먼저 웃었다."
    $ remember("yujin_route_completed")
    $ persistent.local_yujin_ending = True
    $ ending = "yujin_good"
    $ award_once("yujin_R16", "yujin", 4)
    "유진 본편 결말 · 제 이름으로, 우리 마음으로"
    $ progression_note_ending()
    return

label yujin_e01:
    $ progression_enter("yujin_e01")
    $ progression_checkpoint("yujin_e01")
    if not dating or active_route != "yujin" or not memory.get("yujin_route_completed"):
        $ progression_note_ending()
        return
    $ chapter = "유진 E01 · 제 이름 옆의 우리"
    $ location = "약 반년 뒤 겨울의 휴일 오후 · 유진의 집"
    "그 시안은 다음 출근일에 전달했고 납품도 마쳤다. 이후 유진은 창가 그림에서 시작한 작은 개인 작업 묶음을 완성했다. 오늘은 인쇄한 소개지를 도현에게 먼저 보여 준다."
    y "이번에는 제 개인 작업이에요. 제 이름만 적었다가, 처음 보여 주고 싶은 사람 이름도 따로 써 놨어요."
    d "그쪽은 제가 맞힐 수 있을 것 같은데요."
    y "네. 오늘도 오셨으니까 힌트는 여기까지요~"
    "도현도 직접 찍은 사진과 짧은 글을 모아 완성한 작은 기록집을 건넸다. 유진은 예전에 봤던 접지 초안 옆에 나란히 놓고 차이를 한눈에 봤다."
    if memory.get("yujin_r10_page") == "entrance_bench":
        "나중에 다시 찾아가 촬영한 입구의 긴 의자 사진을 함께 펼쳤다."
        y "이제 사진도 있네요. 저는 아직 그날 옆자리부터 생각나요."
    elif memory.get("yujin_r10_page") == "one_sentence":
        y "티켓 옆에 쓰신 그 한 문장도 남았네요. 저는 그날 도현 씨가 고른 자리부터 기억나요."
    elif memory.get("yujin_r10_page") == "open_space":
        y "남겨 둔 칸, 결국 다음 만남 뒤에 채우셨네요. 약속이 먼저였던 거 기억해요."
    $ remember("yujin_epilogue_booklet_state", "이후 직접 촬영·글 정리를 마쳐 작은 인쇄 기록집 완성")
    if memory.get("yujin_o01_status") == "completed":
        "유진이 전시에서 서로 다르게 봤던 부분을 적은 쪽지를 소개지 밑에서 꺼내 보여 줬다."
        y "여긴 아직 제 쪽이 더 좋아요. 도현 씨가 고르신 쪽도 기억나지만요~"
    if memory.get("yujin_o02_status") == "completed":
        y "작은 스케치 보여 드렸던 것도요. 빛이 겹친 컵 그림, 그 노트에 아직 있어요."
    if memory.get("yujin_o03_status") == "completed":
        y "도현 씨 취향으로 고른 날, 저도 좋았어요. 그래서 오늘 이 소개지도 도현 씨 몫부터 빼 뒀죠~"
    if memory.get("yujin_r11_music") == "yujin_calm":
        "함께 들었던 ‘창가에 남은 오후’를 틀었다. 유진이 리듬에 맞춰 도현의 손등을 가볍게 두드렸다."
    elif memory.get("yujin_r11_music") == "dohyun_bright":
        y "나중에 나갈 때는 ‘한 정거장 더’ 고를래요. 오늘은 같이 걷는 쪽으로요."
    elif memory.get("yujin_r11_music") == "both":
        y "지금은 조용한 쪽, 나갈 때는 걸어가던 쪽. 그때 고른 두 곡 순서도 남겨 뒀어요."
    if memory.get("yujin_support_repair_action_verified"):
        "유진이 소개지 두 장을 비교해 놓았다. 도현이 어느 쪽을 볼지 묻자 자기가 원하는 쪽을 먼저 짚었다."
    y "내년에는 이 작업으로 전시도 신청해 보고 싶어요. 휴가에는 둘이 며칠 다녀오고 싶고요. 도현 씨는 어때요?"
    $ progression_enter("yujin_e01.choice01")
    $ progression_checkpoint("yujin_e01.choice01")
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
    "유진이 달력 옆에 적던 ‘준비물’에서 펜을 멈췄다."
    y "아직 예약도 안 했는데 준비물부터 적었네요. 저 좀 기대했나 봐요."
    d "저는 카메라부터 생각했어요. 아직 어디 갈지도 안 골랐는데."
    y "그건 가져오세요. 제 작업 말고 저도 찍어 주셔야죠~"
    "유진은 기록집과 소개지를 나란히 놓았다. 도현이 잠깐 휴대폰을 보자 말을 멈췄다가, 남은 과자를 자기 접시로 가져왔다."
    y "답장 마치시면 제 쪽도 봐 주세요. 과자는 그동안 제가 먼저 고를게요."
    d "끝났어요. 그 큰 조각은 좀 남겨 주실래요?"
    y "늦으셨어요~ 대신 옆자리는 아직 도현 씨 거예요."
    "유진이 제 이름 옆에 따로 써 둔 도현의 이름을 손가락으로 짚었다."
    d "오늘 건 이쪽도 같이 가져가도 돼요?"
    y "네. 그건 처음부터 도현 씨 거예요."
    $ remember("yujin_e01_travel_state", "전시 신청·휴가 여행 계획을 함께 시작함, 예약·참가·여행 완료 아님")
    $ remember("yujin_epilogue_completed")
    $ award_once("yujin_E01", "yujin", 8)
    "유진 후일담 · 제 이름 옆의 우리"
    $ progression_note_ending()
    return
