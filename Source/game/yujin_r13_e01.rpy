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
    "피칭 전 마지막 검토가 십 분으로 줄었다. 유진이 자료 두 장을 추려 놓고 도현을 부른다."
    if memory.get("yujin_support_overstep") and memory.get("yujin_support_repair_status") == "open":
        y "지난번엔 제가 말하기도 전에 도현 씨 설명이 나왔어요. 그건... 좀 서운했어요."
        d "자료 설명이면 빨리 끝날 줄 알았어요. ...제가 나설 자리가 아니었는데. 미안해요."
        y "저도 그 설명 할 수 있었어요. 좀 늦더라도요."
        "도현이 펼치려던 자료를 유진 쪽으로 돌렸다. 유진은 첫 장을 앞에 놓았다."
        y "오늘은 제가 처음부터 할게요. 도현 씨는... 옆에만 있어 주세요."
        $ remember("yujin_r13_path", "repair_open")
    elif memory.get("yujin_support_overstep"):
        if memory.get("yujin_support_repair_action_verified"):
            y "전에 정한 신호 좋았어요. 근데 오늘은 시간이 반이라... 솔직히 좀 무서워요."
        else:
            y "미리 물어보기로 하셨잖아요. 그 말, 기억해 줘서 고마워요. 오늘은 제가 먼저 말할게요."
        d "네. 오늘 두 장 중 어느 쪽부터예요?"
        $ remember("yujin_r13_path", "check_agreement")
    elif memory.get("yujin_support_action") in ("materials", "agreed_summary"):
        y "이유는 제가 말할게요. 근데 십 분이라... 두 장 중에 뭘 앞에 둘지 아직도 손이 떨려요."
        d "둘 다 앞에 놓고 해요. 넘길 때 저 한 번 쳐다보시면 넘길게요."
        $ remember("yujin_r13_path", "new_scope")
    else:
        y "첫 답은 제가 해요. 두 장 다 보여 주고 싶은데, 십 분이 너무 짧아요."
        d "설명은 유진 씨 거예요. 저는 유진 씨가 막혔을 때만요. 지금 어디가 제일 걸려요?"
        $ remember("yujin_r13_path", "ask_current")
    if memory.get("yujin_r12_support_request"):
        d "어제 하신 말 기억해요. 오늘은 유진 씨 목소리로 가요."
    y "첫 질문은 제가 받아요. 숨 막히면... 그때 도현 씨 쪽 볼게요."
    $ progression_enter("yujin_r13.choice01")
    $ progression_checkpoint("yujin_r13.choice01")
    menu:
        "자료만 넘기고 설명은 유진에게 맡긴다.":
            d "첫 답이 끝나면 두 번째 자료요. 넘어갈 때 신호 주시면 맞출게요."
            y "네. 손으로 페이지 짚을게요. 제가 말하는 속도로요."
            $ remember("yujin_r13_support_plan", "slides")
        "남은 시간만 조용히 알려 주기로 한다.":
            d "질문이 몰리면 그때만 정리할게요. 이 분 남으면 메모 들어 보일게요."
            y "네. 제 설명에서 뭘 줄일지는 제가 정할게요. 그 메모 부탁드려요."
            $ remember("yujin_r13_support_plan", "questions")
        "부탁할 때만 질문을 정리하기로 한다.":
            d "정말 막히면 말해요. 질문만 묶고, 답은 다시 유진 씨한테 돌려줄게요."
            y "네. 제가 ‘두 질문만 정리해 주세요’라고 할게요. 그 전에는 제가 이어 볼래요."
            $ remember("yujin_r13_support_plan", "requested_summary")
    $ remember("yujin_r13_agreed_scope")
    if memory.get("yujin_support_overstep") and not memory.get("yujin_support_repair_action_verified"):
        $ remember("yujin_support_repair_status", "agreed_pending_action")
    y "...오늘도 끝나면 이쪽 볼 거예요. 끝났다고 웃는 건 제가 할게요~"
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
        "정한 대로 준비하고 기다린다.":
            $ remember("yujin_r14_readiness", "ready")
        "신호를 한 번 더 맞춰 본다.":
            d "아까 정한 범위까지만요. 바뀌면 유진 씨가 말씀해 주시는 거죠?"
            y "네. 지금은 그대로예요. 같이 확인하니까 좀 덜 급해지네요."
            $ remember("yujin_r14_readiness", "rechecked")
        "끝나고 우리 얘기를 하자고 한다.":
            d "퇴근하고 잠깐 얘기할 수 있을까요? 오늘은 회사 얘기 말고, 저희 얘기요."
            y "네. 저도 듣고 싶어요. 지금은 이 두 장부터 끝내고요."
            $ remember("yujin_r14_readiness", "relationship_talk")
    $ location = "같은 금요일 오전 · 짧은 검토 회의"
    "첫 질문이 나왔다. 유진이 시안을 짚으며 색을 고른 이유부터 설명했다."
    if memory["yujin_r13_support_plan"] == "slides":
        "도현은 유진이 첫 장 모서리를 짚을 때까지 기다렸다. 신호를 보고 두 번째 자료를 올리자 유진이 수정 범위를 이어 말했다."
        y "이 부분은 그대로 두고, 아래 문장 사이만 넓히겠습니다. 비교 자료의 오른쪽을 봐 주세요."
    elif memory["yujin_r13_support_plan"] == "questions":
        "질문이 겹치자 도현이 순서만 정리했다. 남은 시간 이 분을 메모로 보이자 유진은 핵심 근거만 추려 설명했다."
        d "수정 범위부터 답을 듣고, 적용 일정은 다음 질문으로 받을게요."
        y "네. 그 순서로 말씀드릴게요."
    else:
        y "도현 씨, 두 질문만 정리해 주실래요? 답은 제가 이어갈게요."
        d "지금 질문은 수정할 부분과 유지할 부분, 두 가지입니다. 유진 씨가 차례로 설명하겠습니다."
        "도현이 멈추자 유진이 두 항목을 직접 비교해 답했다."
    "검토를 마친 뒤 유진은 확정한 수정 사항을 자기 작업 노트에 적었다. 시안 아래에는 유진의 이름이 남았다."
    $ location = "같은 금요일 퇴근 후 · 회사 앞"
    if memory.get("yujin_r14_readiness") == "relationship_talk":
        "사람들이 빠져나간 뒤, 정류장으로 바로 가지 않고 회사 앞 벤치에 앉았다."
        y "아까 하시려던 얘기요. 이제 자료 안 봐도 되니까... 도현 씨 얼굴 보고 들을게요."
        $ progression_enter("yujin_r14.choice02")
        $ progression_checkpoint("yujin_r14.choice02")
        menu:
            "연애를 마치고 동료로 지내겠다는 뜻을 분명히 전한다.":
                d "저는 연인으로는 여기까지 만나고 싶어요. 잠깐 쉬자는 뜻은 아니에요."
                "유진은 가방 끈을 쥐었다가 천천히 놓았다."
                y "...알겠어요. 이유는 듣고 싶지만, 대답을 바꿔 달라고는 안 할게요."
                d "좋아하는 마음만으로 계속 만나겠다고 약속하기는 어려워요. 유진 씨가 오늘 뭘 잘못하셨다는 뜻은 아니고요."
                y "네. 오늘 일은 같이 끝냈고요. 이제 저 혼자 갈게요."
                "도현은 붙잡지 않고 인사했다. 사적인 다음 약속은 잡지 않았다."
                $ dating = False
                $ remember("yujin_relationship_closed")
                $ ending = "yujin_relationship_closed"
                "유진 관계 종료 · 서로의 자리로"
                $ progression_note_ending()
                return
            "보고 싶었다는 말부터 한다.":
                d "요즘 만나면 작업 얘기부터 했잖아요. 오늘은 유진 씨 보고 싶어서 기다렸다는 말부터 하고 싶었어요."
                y "...그 말 하시려고 따로 앉으신 거예요?"
                d "네. 걸으면서 하면 또 버스 언제 오냐는 얘기로 샐 것 같아서요."
                "유진이 벤치 등받이에 기대다가 웃었다."
                y "저 지금 꽤 긴장했는데요. 그럼 버스 한 대는 놓치셔야겠어요."
                d "두 대째부터는 같이 시간표 봐요."
                y "네. 첫 번째는 제 얘기 들으시고요."
                $ remember("yujin_r14_readiness", "reassured")
            "마음에 걸렸던 걸 꺼낸다.":
                if memory.get("yujin_support_overstep"):
                    d "전에 제가 먼저 설명했던 일요. 사과한 뒤에도 또 앞서갈까 봐, 둘이 있을 때까지 말을 재게 되더라고요."
                    y "오늘 기다려 주신 건 좋았어요. 그렇다고 저한테 하고 싶은 말까지 다 참으시면, 저는 그것도 모르잖아요."
                    d "네. 저는 계속 만나고 싶어요. 실수 안 하겠다는 말만 하느라 정작 그 말을 빼먹었네요."
                    y "저도 계속 만나고 싶어요. 아직 서운한 게 남으면... 그땐 말할게요."
                else:
                    d "만나서도 자꾸 작업 얘기부터 꺼내게 돼요. 유진 씨랑 할 얘기가 그것밖에 없는 사람처럼요."
                    y "저도 보여 드릴 게 있어야 만나자고 하기 쉽더라고요. 도현 씨는 이제 그런 핑계 없어도 오실 것 같은데."
                    d "네. 오늘도 그래서 기다렸어요. 앞으로도 만나고 싶어요."
                    y "...그럼 다음엔 빈손으로 와 보세요. 저도 노트는 두고 나와 볼게요."
                $ remember("yujin_r14_readiness", "talk_after")
        $ remember("yujin_r14_relationship_talk_completed")
    if memory.get("yujin_r14_readiness") == "talk_after":
        "도현은 손을 내밀려다 유진이 가방을 고쳐 메는 동안 기다렸다. 유진이 옆으로 한 걸음 다가왔다."
        y "오늘 다 정리해서 말하려고 하진 말아요. 정류장까지는 그냥 같이 걷고 싶어요."
        d "네. 제 얘기도 걷다가 생각나면 할게요."
        "나란히 걸었다. 건널목 앞에서 멈췄을 때 유진의 손이 도현의 손등에 잠깐 닿았다."
    elif memory.get("yujin_r14_readiness") != "reassured":
        if memory.get("yujin_support_overstep"):
            y "오늘은 제가 마지막 말까지 했네요. 도현 씨 쪽 봤을 때도 안 급해져서 좋았어요."
        else:
            y "오늘도 끝까지 했네요. 중간에 도현 씨 쪽 한 번 봤는데, 아셨어요?"
        d "이제 웃으셔도 되는 시간이죠? 저도 좀 기다렸어요."
        y "...지금은 도현 씨가 웃어 주셔도 되는데요~"
        "도현이 웃자 유진이 들고 있던 가방 끈을 다시 고쳐 쥐었다."
        y "아, 잠깐만요. 끝나면 제가 웃어 드리려고 했는데."
        d "그럼 다시 기다릴까요?"
        y "아뇨. 이제 그만 기다리고 같이 가요."
        "유진이 걸음을 뗐다. 도현이 따라오자 이번에는 돌아보며 웃었다."
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
    y "네. 앉을지는 도현 씨 마음이고요. 저는 지금 오래 기다린 척할래요~"
    "도현이 자리를 옮기자 유진은 준비해 둔 과자를 둘 사이에 놓았다. 접시는 하나였다."
    if memory.get("yujin_r14_readiness") in ("talk_after", "reconsidered"):
        y "어제 얘기가 다 끝났다고 생각하진 않아요. 그래도 오늘 옆에 계셨으면 해서 제가 먼저 불렀어요."
        d "네. 저도 그 마음으로 왔어요."
    y "오늘은 도와 달라는 말보다 같이 있고 싶다는 말을 할게요. 연습은 했는데... 지금이 더 쉽네요."
    $ progression_enter("yujin_r15.choice01")
    $ progression_checkpoint("yujin_r15.choice01")
    menu:
        "핑계 없이 보자고 하자고 한다.":
            d "볼 전시 없어도 부를게요. 오늘처럼 옆에 앉아 있어도 좋고요."
            y "그럼 안내지 모으는 건 좀 쉬어야겠네요. 만나자고 하려고 괜히 하나씩 챙겼는데~"
            $ remember("yujin_r15_future", "say_first")
        "작업은 보여 주되 묻고 돕자고 한다.":
            d "구경해 달라는 날인지 도와 달라는 날인지, 물어볼게요. 제 노트도 그렇게 말씀드리고요."
            y "좋아요. 오늘은 아무것도 안 보여 드릴래요. 대신 이 자리는 조금 오래 쓰세요~"
            $ remember("yujin_r15_future", "ask_scope")
        "같이 쉴 날, 각자 쉴 날을 정하자고 한다.":
            d "쉬는 날엔 저도 집에서 늦잠 잘래요. 보고 싶으면 일어나서 연락하고요."
            y "네. 일찍 깨면 제 아침부터 먹을게요. 답장 없다고 혼자 삐치기 전에요~"
            d "일어나면 그 자랑부터 볼게요."
            y "그럼 예쁘게 담아야겠네요. 배고프면 먹긴 할 거예요!"
            $ remember("yujin_r15_future", "rest_balance")
    "과자를 나눠 먹은 뒤 유진이 접시를 치웠다. 돌아와서는 도현 옆의 자기 자리에 다시 앉았다."
    y "오늘 밤은 같이 있고 싶어요. 도현 씨도 괜찮으시면요."
    $ progression_enter("yujin_r15.choice02")
    $ progression_checkpoint("yujin_r15.choice02")
    menu:
        "나도 함께 있고 싶다고 답한다 — 친밀한 장면으로 이어짐.":
            d "네. 저도 같이 있고 싶어요."
            y "분위기를 좀 바꿔 보고 싶기도 해요. 특별한 의상... 같이 골라 볼까요? 지금처럼 편하게 있어도 좋고요."
            $ progression_enter("yujin_r15.choice03")
            $ progression_checkpoint("yujin_r15.choice03")
            menu:
                "지금의 편한 생활복이 좋다고 말한다.":
                    d "오늘은 지금 모습이 좋아요. 옆에서 편하게 쉬는 유진 씨요."
                    y "그 말 들으니까 준비 다 한 것 같네요~"
                    $ remember("yujin_r15_outfit", "home")
                "코스프레 의상을 같이 고르자고 한다.":
                    "마음에 드는 특별 의상을 함께 골랐다. 갈아입고 나온 유진이 잠깐 문가에 멈췄다."
                    y "...그렇게 조용히 보시면 제가 더 부끄러워지는데요."
                    d "잘 어울려요. 이런 모습을 유진 씨가 보여 주고 싶어 했다는 게 좋아요."
                    y "네. 그 말은 준비한 답보다 좋네요."
                    $ remember("yujin_r15_outfit", "cosplay")
                "유진에게 고르게 한다.":
                    y "오늘은 편한 쪽이요. 다른 의상은 다음에 같이 고르고 싶어요."
                    d "저도 지금이 좋아요. 다음에 고르는 날도 같이 정해요."
                    $ remember("yujin_r15_outfit", "home")
                    $ remember("yujin_r15_outfit_delegated")
            call event_sequence("yujin_r15", memory["yujin_r15_outfit"])
            if not event_main_reached:
                "(장면 생략 · 시간이 흐릅니다.)"
            $ remember("yujin_r15_intimacy", "shared")
            y "아까 연습한 말, 중간부터 다 잊었어요."
            d "중간부터가 더 좋았는데요."
            "유진이 대답하려다 웃었다. 도현도 다음 말을 재촉하지 않았다."
        "오늘은 집에 간다.":
            d "오늘은 집에서 쉴게요. 내일 같이 노트 보기로 한 건 그대로고요."
            y "네. 남은 과자는 싸 드릴게요. 내일도 같이 볼 페이지는 남아 있어요."
            $ remember("yujin_r15_intimacy", "deferred")
        "얘기만 더 하고 잠은 각자 잔다.":
            d "오늘은 좀 더 얘기하고 갈래요. 밤에는 각자 쉬고요."
            y "좋아요. 제가 말하다가 늦어지면 시계도 같이 봐 주세요~"
            "서로 가장 좋았던 말을 하나씩 꼽은 뒤 인사를 나눴다."
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
    $ location = "피칭 당일 · 클라이언트사 대회의실"
    "피칭 당일. 디자인 파트는 유진의 차례였다. 유진은 시안을 띄우고 숨을 한 번 고른 뒤, 원고를 보지 않고 말을 시작했다."
    y "이 안내는 문구가 먼저 보이고, 빛은 그다음에 보이게 만들었습니다."
    "질의응답 시간. 클라이언트 쪽 젊은 담당자가 손을 들었다. “혹시... 이거 ‘창가’ 그림체랑 비슷하지 않아요? 저 그 계정 팔로우하거든요.”"
    "회의실이 잠깐 조용해졌다. 리아가 ‘거봐요’ 하는 얼굴로 도현을 봤다. 리모컨을 쥔 유진의 손가락이 하얗게 굳었다."
    "도현은 끼어들지 않았다. 대신 유진이 이쪽을 봤을 때, 아주 작게 고개를 끄덕였다."
    y "...비슷한 게 아니라, 제가 그렸어요. ‘창가’는 제 계정이에요."
    y "회사 작업이랑은 분리해 왔고요. 그래도 같은 사람이 그린 거라, 빛을 다루는 방식은... 숨겨지지가 않았나 봐요."
    "잠깐의 정적 뒤, 질문했던 담당자가 박수를 쳤다. 심사석 몇 사람이 웃었다. 지현은 말없이 시안 옆에 펜으로 동그라미를 그렸다."
    $ location = "피칭 당일 저녁 · 회사 앞 횡단보도"
    "결과는 저녁에 나왔다. TF가 이겼다."
    y "저 오늘... 회사 사람들 앞에서 말해 버렸어요. 계정."
    d "봤어요. 오늘 제일 멋있었어요."
    y "도현 씨가 고개 끄덕여 줘서요. 그거 아니었으면 또 ‘아니에요’ 했을 거예요."
    "신호가 바뀌었다. 건너려던 유진이 돌아서서 도현의 손을 잡았다. 회사 앞인데도 놓지 않았다."
    y "이제 숨길 거 하나 줄었으니까... 이것도 안 숨길래요."
    $ cream_focus = "yujin"
    $ location = "같은 주 일요일 저녁 · 동네 카페"
    "유진이 검토 의견을 반영한 최종 시안을 저장했다. 월요일 전달할 파일 이름 끝에 자기 이름을 확인하고 화면을 닫았다."
    y "됐어요. 오늘은 이걸로 끝. 이제 도현 씨 가져오신 거 볼래요."
    $ remember("yujin_design_state", "검토 의견을 반영한 최종 시안 저장, 다음 출근일 전달 예정")
    "도현은 두 장을 접어 만든 기록집 초안을 꺼냈다. 유진은 한쪽만 보고 다시 도현에게 돌려줬다."
    if memory.get("yujin_r10_page") == "entrance_bench":
        if memory.get("yujin_o03_photo_taken"):
            d "오늘 찍은 의자 사진은 후보로 옆에 뒀어요. 이 초안엔 날짜랑 기억부터 넣었고요."
        else:
            d "그 의자는 아직 촬영 후보예요. 여기엔 같이 앉았던 날짜만 남겼어요."
    elif memory.get("yujin_r10_page") == "one_sentence":
        d "티켓 옆에 적었던 말요. 오늘 초안의 한 페이지에 그대로 놓아 봤어요."
    elif memory.get("yujin_r10_page") == "open_space":
        d "빈칸은 아직 남겨 뒀어요. 다음에 만나고 나서 적으려고 비워 둔 칸이니까요."
    else:
        d "아직 두 장짜리예요. 완성되기 전에 보여 드리고 싶었어요."
    $ remember("yujin_r16_booklet_state", "두 장 접지 초안 공유, 완성된 책 아님")
    if memory.get("yujin_disclosed_to") == "jihyun":
        y "팀장님 답장 기억나요? 수정 의견 안 보태신다고요. 축하한다는 말만 들으니까 기분 좋았어요~"
    else:
        "유진은 개인 노트를 펼쳤다. 교제 이야기를 다른 사람에게 전하는 메시지는 보내지 않았다."
    if memory.get("yujin_support_overstep"):
        "도현이 설명을 시작하려다 멈추자 유진은 이미 펼쳐 둔 페이지를 보여 줬다."
        y "여기요. 이번엔 제가 궁금한 쪽부터 볼래요."
    else:
        "유진이 도현의 초안 옆에 자기 노트를 놓았다."
        y "이쪽도 펼쳐 놓을까요? 옆에 두고 보고 싶어요."
    "유진은 자기 노트를 덮어 도현의 초안 옆에 두었다. 가방을 챙겨 일어난 뒤 도현 곁의 빈자리로 옮겨 앉았다."
    y "새 작업은 제 이름으로 할래요. 다 못 그린 날에도... 도현 씨는 와 주셨으면 좋겠고요."
    d "제 옆자리부터 예약하시네요."
    y "네. 이번엔 제가 먼저 찜했어요."
    $ progression_enter("yujin_r16.choice01")
    $ progression_checkpoint("yujin_r16.choice01")
    menu:
        "계속 서로 부르며 만나자고 한다.":
            d "저도 계속 만나고 싶어요. 다음 작업 설명보다 보고 싶다는 말부터 듣는 날도 만들고요."
            y "그건 제가 또 선수 칠 수도 있어요~"
            $ remember("yujin_r16_promise", "keep_inviting")
        "각자 일 하면서 같이 할 날도 두자고 한다.":
            d "저도 유진 씨 다음 작업 옆에 제 노트 들고 올게요. 각자 하는 일도, 만나는 날도 남겨 두고요."
            y "네. 각자 하던 것도 들려주세요. 제가 먼저 옆에 앉았다고 놀리지는 마시고요~"
            $ remember("yujin_r16_promise", "own_pages")
        "도와줄 때도 마음은 숨기지 말자고 한다.":
            d "앞으로도 같이 있고 싶어요. 잘 도와드리려다 제 마음을 늦게 말하지는 않을게요. 제가 원하는 것도 말씀드릴래요."
            y "네. 저도 잘해 드리고 싶다는 말 뒤에 보고 싶다는 마음 숨기지 않을래요."
            $ remember("yujin_r16_promise", "say_own_needs")
    "유진은 도현 쪽으로 조금 더 붙어 앉았다. 도현이 초안을 다시 펼치려 하자 손으로 살짝 덮었다."
    y "다음 장은 나중에 볼래요. 지금은 도현 씨랑 얘기하고 싶어요."
    d "좋아요. 무슨 얘기부터요?"
    y "아까 제가 먼저 옆에 앉은 얘기요. ...도현 씨도 좋았잖아요?"
    "이번에는 도현이 바로 대답하지 못했다. 유진이 그 표정을 보고 웃음을 터뜨렸다."
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
    "피칭은 TF의 승리로 끝났고, 그 시안은 납품까지 마쳤다. 이후 유진은 ‘창가’ 계정의 그림을 묶어 처음으로 자기 이름을 건 작은 전시를 열었다. 오늘은 인쇄한 소개지를 도현에게 가장 먼저 보여 준다."
    y "이번엔 ‘창가’ 말고 차유진으로 하는 거예요. 제 이름만 적었다가... 처음 보여 주고 싶은 사람 이름도 따로 써 놨어요."
    d "그쪽은 제가 맞힐 수 있을 것 같은데요."
    y "네. 오늘도 오셨으니까 힌트는 여기까지요~"
    "도현도 직접 찍은 사진과 짧은 글을 모아 완성한 작은 기록집을 건넸다. 유진은 예전에 봤던 접지 초안 옆에 나란히 놓고 차이를 한눈에 봤다."
    if memory.get("yujin_r10_page") == "entrance_bench":
        "나중에 다시 찾아가 촬영한 입구의 긴 의자 사진을 함께 펼쳤다."
        y "이제 사진도 있네요. 저는 아직 그날 옆자리부터 생각나요."
    elif memory.get("yujin_r10_page") == "one_sentence":
        y "티켓 옆에 쓰신 그 한 문장도 남았네요. 저는 그날 도현 씨가 앉은 자리부터 기억나요."
    elif memory.get("yujin_r10_page") == "open_space":
        y "남겨 둔 칸, 결국 다음에 만나고 나서 채우셨네요. 약속 지키신 거 기억해요."
    $ remember("yujin_epilogue_booklet_state", "이후 직접 촬영·글 정리를 마쳐 작은 인쇄 기록집 완성")
    if memory.get("yujin_o01_status") == "completed":
        "유진이 전시에서 서로 다르게 봤던 부분을 적은 쪽지를 소개지 밑에서 꺼내 보여 줬다."
        y "여긴 아직 제 쪽이 더 좋아요. 도현 씨가 고르신 쪽도 기억나지만요~"
    if memory.get("yujin_o02_status") == "completed":
        y "작은 스케치 보여 드렸던 것도요. 빛이 겹친 컵 그림, 그 노트에 아직 있어요."
    if memory.get("yujin_o03_status") == "completed":
        y "도현 씨 취향대로 간 날, 저도 좋았어요. 그래서 오늘 소개지도 도현 씨 몫부터 빼 뒀죠~"
    if memory.get("yujin_r11_music") == "yujin_calm":
        "함께 들었던 ‘창가에 남은 오후’를 틀었다. 유진이 리듬에 맞춰 도현의 손등을 가볍게 두드렸다."
    elif memory.get("yujin_r11_music") == "dohyun_bright":
        y "나중에 나갈 때는 ‘한 정거장 더’ 틀래요. 오늘은 같이 걷는 쪽으로요."
    elif memory.get("yujin_r11_music") == "both":
        y "지금은 조용한 쪽, 나갈 때는 걸어가던 쪽. 그때 정한 두 곡 순서도 남겨 뒀어요."
    if memory.get("yujin_support_repair_action_verified"):
        "유진이 소개지 두 장을 나란히 놓았다. 도현이 어느 쪽을 볼지 묻자 자기가 원하는 쪽을 냉큼 짚었다."
    y "내년에는 이 작업으로 전시도 신청해 보고 싶어요. 휴가에는 둘이 며칠 다녀오고 싶고요. 도현 씨는 어때요?"
    $ progression_enter("yujin_e01.choice01")
    $ progression_checkpoint("yujin_e01.choice01")
    menu:
        "전시 모집부터 찾아보자고 한다.":
            d "전시 모집부터 찾아봐요. 유진 씨 작업 걸린 거 꼭 보고 싶어요. 여행 날짜는 그다음에 맞추고요."
            $ remember("yujin_e01_plan", "exhibition_first")
        "휴가 날짜부터 맞춰 보자고 한다.":
            d "저는 둘이 쉴 날부터 적어 보고 싶어요. 신청 일정이 정해지면 같이 맞춰 봐요."
            $ remember("yujin_e01_plan", "holiday_first")
        "후보를 하나씩 가져오자고 한다.":
            d "전시랑 가 보고 싶은 동네 후보를 하나씩 가져올까요? 다음 주말에 같이 정하고요."
            $ remember("yujin_e01_plan", "bring_candidates")
    "유진이 달력 옆에 적던 ‘준비물’에서 펜을 멈췄다."
    y "아직 예약도 안 했는데 준비물부터 적었네요. 저 좀 기대했나 봐요."
    d "저는 카메라부터 생각했어요. 아직 어디 갈지도 안 정했는데."
    y "그건 가져오세요. 제 작업 말고 저도 찍어 주셔야죠~"
    "유진은 기록집과 소개지를 나란히 놓았다. 도현이 잠깐 휴대폰을 보자 말을 멈췄다가, 남은 과자를 자기 접시로 가져왔다."
    y "답장 다 하시면 제 쪽도 봐 주세요. 과자는 그동안 제가 찜할게요."
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
