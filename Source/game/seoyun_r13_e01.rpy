# Seoyun route v002: divorced parent, disclosed before dating.
label seoyun_r13:
    $ progression_enter("seoyun_r13")
    $ progression_checkpoint("seoyun_r13")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R13 · 내 대답까지 고르지 마요"
    $ location = "약속한 월요일 저녁 일곱 시 · 카페"
    "서윤은 수첩을 펴 놓고 있었다. 아이와 보내는 시간 옆에는 비어 있는 칸도 있었다."
    s "금요일 얘기, 생각해 봤어. 아이 소개는 아직 서두르고 싶지 않아."
    d "네. 그건 저도 그래요. 그다음 얘기도 듣고 싶어요."
    s "우린 지금처럼 가끔 보면 되지 않을까. 네가 더 깊이 들어오면 힘들어질 것 같아서."
    d "저한테 힘드냐고 묻기도 전에, 어디까지만 만날지 정하신 거예요?"
    "서윤은 수첩의 빈칸을 가리키던 손을 거뒀다."
    s "...네가 좋다고 하면 내가 계속 욕심낼 것 같았어. 너한테 부탁할 게 자꾸 늘어날까 봐."
    d "부탁을 듣고 대답하는 건 제가 할게요. 아이 있는 거 모르고 시작한 것도 아니고요."
    $ remember("seoyun_conflict", "open")
    $ remember("seoyun_dismissed_request", "가족 공개 이후에도 도현의 의사를 묻기 전에 연애의 범위를 혼자 정하려 함")
    $ progression_enter("seoyun_r13.choice01")
    $ progression_checkpoint("seoyun_r13.choice01")
    menu:
        "아이 일정과 내 마음을 대신 결정하는 일은 다르다고 말한다.":
            d "아이랑 보내는 시간을 줄여 달라는 게 아니에요. 그 안에서 제가 어떤 만남을 원하는지도 물어봐 주세요."
            s "응. 내가 지켜야 할 것부터 말하다가, 네가 정할 부분까지 닫아 버렸네."
            $ remember("seoyun_r13_response", "weight")
        "당장 소개보다 앞으로의 이야기를 함께 할 수 있는지 묻는다.":
            d "지금 소개 안 받아도 괜찮아요. 나중에 어떤 마음이 드는지 서로 말할 수 있는 사이면 좋겠어요."
            s "못 정한 건 못 정했다고 하면 되는 건데. 아예 다음 얘기를 하지 말자고 해 버렸네."
            $ remember("seoyun_r13_response", "unknown")
        "좋아하는 마음과 부담되는 부분을 잠깐 정리하고 말한다.":
            d "저도 안 어려울 거라고는 못 해요. 잠깐만 생각하고 대답할게요."
            "도현이 컵을 내려놓았다. 서윤은 빈칸에 아무것도 적지 않고 기다렸다."
            d "기다릴 수 있는 것과 어려운 건 저도 말하고 싶어요. 다 괜찮다고 해야만 만날 수 있는 건 싫고요."
            s "응. 네가 잠깐 멈춘 걸 거절로 짐작하지도 않을게."
            $ remember("seoyun_r13_response", "pause")
    s "이혼하고 아이랑 사는 건 내가 선택한 생활이야. 그런데 너까지 만나고 싶다고 하니까, 내가 너무 많이 바라는 사람 같았어."
    d "저는 서윤 씨가 뭘 바라는지도 알고 싶어서 만나요. 조건만 듣고 남을지 말지 재는 사람이 되고 싶지는 않아요."
    "서윤이 수첩을 접었다. 탁자 위에는 컵 두 개만 남았다."
    s "보고 싶어. 앞으로도. ...그 말부터 했어야 했네."
    d "저도요. 그다음에 어려운 얘기를 같이 해요."
    if memory.get("seoyun_publicity") == "told_yujin":
        s "유진이한테 우리 만난다고 말할 때도 같이 정했지. 정작 너한테는 혼자 답하려고 했네."
    else:
        s "사귀는 걸 누구한테 알릴지도 같이 정했는데. 우리 얘기는 나 혼자 끝내려고 했네."
    s "수요일에 다시 볼래? 그땐 내 마음이랑 할 수 있는 일을 나눠서 말해 볼게."
    d "네. 저도 원하는 것만큼 어려운 것도 가져올게요."
    $ remember("seoyun_future_question_status", "아이 소개와 연인으로서의 시간을 서로 논의하기로 함, 결혼·동거·부모 역할 확약 없음")
    $ remember("seoyun_trust_status", "needs_mutual_discussion")
    $ remember("seoyun_conflict", "discussing")
    $ award_once("seoyun_R13", "seoyun", 0)
    $ progression_note_ending()
    return

label seoyun_r14:
    $ progression_enter("seoyun_r14")
    $ progression_checkpoint("seoyun_r14")
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "discussing":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R14 · 두 사람 몫의 대답"
    $ location = "같은 월요일 저녁 · 카페"
    s "난 수요일 일곱 시에 여기 올 수 있어. 너는 어때? 지금 정하기 싫으면 나중에 말해도 돼."
    $ progression_enter("seoyun_r14.choice01")
    $ progression_checkpoint("seoyun_r14.choice01")
    menu:
        "수요일에 서로 원하는 만남부터 이야기하자고 한다.":
            d "수요일에 봐요. 그날은 몇 시에 볼지만 말고, 우리 둘이 뭘 하고 싶은지도 얘기해요."
            s "응. 나도 그건 달력 안 보고 대답할 수 있어."
            $ remember("seoyun_r14_choice", "ready")
        "부담되는 일도 솔직히 말할 수 있어야 한다고 한다.":
            d "저도 늘 괜찮다고는 못 해요. 어렵다고 해도 좋아하는 마음이 없다고는 듣지 말아 주세요."
            s "응. 나도 내 부탁 다 들어줘야 계속 만날 수 있는 것처럼 말하지 않을게."
            $ remember("seoyun_r14_choice", "repair_blunt")
        "연애를 마치고 동료로 지내고 싶다고 말한다 — 관계 종료 확인.":
            $ progression_enter("seoyun_r14.choice02")
            $ progression_checkpoint("seoyun_r14.choice02")
            menu:
                "관계 종료를 확정한다.":
                    d "좋아하지만, 제가 원하는 관계랑은 다른 것 같아요. 연애는 여기서 마치고 싶어요."
                    s "알겠어. 네가 날 감당 못 한 거라고 생각하진 않을게. 수요일 약속도 안 잡을게."
                    $ dating = False
                    $ remember("seoyun_relationship_closed")
                    $ ending = "seoyun_relationship_closed"
                    "인사하고 카페를 나왔다. 사적인 다음 약속은 잡지 않았다."
                    $ progression_note_ending()
                    return
                "결정을 취소하고 수요일에 이야기를 듣는다.":
                    d "끝내겠다는 말은 취소할게요. 서로 생각을 더 듣고 싶어요."
                    s "응. 다음 답까지 미리 받은 걸로 생각하지 않을게."
                    $ remember("seoyun_r14_choice", "reconsidered")
                "종료 결정은 보류하고 서로의 생각을 들은 뒤 다시 정한다.":
                    d "지금은 결정하지 않을게요. 수요일엔 제 마음도 말할래요."
                    s "응. 나도 대답을 준비해 갈게."
                    $ remember("seoyun_r14_choice", "wait_action")
    $ remember("seoyun_repair_appointment", "수요일 저녁 일곱 시, 가능한 시간·연인으로서의 바람·아이 소개의 속도를 함께 논의")
    $ remember("seoyun_conflict", "agreed_pending_action")
    $ location = "약속한 수요일 저녁 일곱 시 · 같은 카페"
    "서윤은 수첩을 가방에 넣은 채 먼저 와 있었다. 도현이 앉자 메뉴판보다 얼굴부터 봤다."
    s "오늘은 네가 어디까지 해 줄 수 있는지부터 묻지 않을게. 난 계속 만나고 싶어. 책 얘기하다 네가 웃는 것도, 아무 말 없이 걷는 것도."
    d "저도 계속 만나고 싶어요. 근데 서윤 씨가 시간 정해서 알려 주기만 하면, 제가 끼어드는 기분이 들 때가 있어요."
    s "응. 아이랑 있기로 한 날은 지켜야 해. 그 외에 언제 볼지는 너한테도 물을게. 갑자기 일 생기면 내가 바로 연락하고."
    d "저도 제 일정이랑 쉬고 싶은 날 말할게요. 서운한 거 참고만 있지는 않고요."
    s "아이를 만나는 건 그다음 일이야. 너만 괜찮다고 끝나는 일도 아니고, 아이 마음과 준비도 봐야 해."
    d "네. 만나게 되더라도 제가 바로 아빠 역할을 맡겠다는 약속으로 만들지는 말아요."
    s "응. 아이 아빠랑 필요한 연락은 계속해. 그렇다고 그 사람이랑 다시 합치려는 건 아니야. 헷갈리면 나한테 물어봐."
    "서윤이 컵을 들었다가 내려놓았다. 이번엔 말을 보태려던 도현을 기다려 줬다."
    d "그리고 둘이 놀러 가고 싶은 데도 하나씩 말해요. 어려운 얘기만 하는 연인은 싫어요."
    s "...나 지금 네가 시킬 디저트가 궁금해. 그건 오늘 물어봐도 되지?"
    d "네. 이번에는 레몬 말고 다른 걸로요."
    "서윤이 웃었다. 도현도 메뉴판을 가운데로 옮겼다."
    $ remember("seoyun_repair_performed", "수요일 실제 대면에서 서로의 시간과 바람을 듣고 소개·부모 역할을 서두르지 않기로 합의")
    $ remember("seoyun_mutual_plan_performed")
    $ remember("seoyun_future_boundary_confirmed")
    $ progression_enter("seoyun_r14.choice03")
    $ progression_checkpoint("seoyun_r14.choice03")
    menu:
        "소개는 천천히 생각하며 연인으로 계속 만나기로 한다.":
            d "계속 만나고 싶어요. 제가 원하는 것도 말하면서요."
            s "응. 나도 보고 싶은 날부터 물어볼게."
            $ remember("seoyun_continues_after_discussion")
        "이야기를 들었지만 연애는 여기서 마치기로 한다.":
            d "생각 말해 주셔서 고마워요. 그래도 저는 지금 이 관계를 이어가기는 어려울 것 같아요."
            s "응. 솔직하게 답해 준 거, 그대로 받을게."
            $ dating = False
            $ remember("seoyun_relationship_closed")
            $ ending = "seoyun_relationship_closed"
            "인사하고 각자 일어났다. 새로운 사적 약속은 잡지 않았다."
            $ progression_note_ending()
            return
        "아직 어려운 점도 말하며 지금의 만남을 이어가고 싶다고 한다.":
            d "아직 모르는 것도 많아요. 미래를 확답하진 못해도 계속 만나 보고 싶어요."
            s "나도 그래. 모르는 건 다시 묻고, 대답이 바뀌면 바로 말해 주자."
            $ remember("seoyun_continues_after_discussion")
            $ remember("seoyun_future_discussion_open")
    $ remember("seoyun_conflict", "resolved")
    $ remember("seoyun_future_question_status", "상호 바람과 시간을 확인하고 교제 지속, 아이 소개·동거·부모 역할은 별도 논의")
    $ remember("seoyun_trust_status", "mutual_answers_confirmed")
    if memory.get("seoyun_r14_choice") == "wait_action":
        $ remember("seoyun_continuation_reconfirmed")
    s "금요일 일곱 시, 같이 저녁 먹을래? 그날 시간은 맞춰 뒀어. 장소는 네가 골라 주면 좋겠어."
    d "좋아요. 이번엔 메뉴부터 궁금해지는 데로요."
    $ remember("seoyun_r15_appointment", "금요일 저녁 일곱 시 함께 식사")
    $ award_once("seoyun_R14", "seoyun", 8)
    $ progression_note_ending()
    return

label seoyun_r15:
    $ progression_enter("seoyun_r15")
    $ progression_checkpoint("seoyun_r15")
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "resolved":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R15 · 다음 금요일은 우리 약속"
    $ location = "약속한 금요일 저녁 일곱 시 · 식당"
    "서윤은 먼저 와서 메뉴판을 보고 있었다. 도현이 들어오자 자기 옆 빈 의자를 손으로 가리켰다."
    s "오늘은 맞은편 말고 여기. 네 접시가 더 맛있어 보이면 바꾸기 편하잖아~"
    d "주문하기도 전에 노리시는 거예요?"
    s "응. 네가 정한 데라니까 기대하고 왔어."
    "도현은 외투를 벗고 앉았다. 서윤이 펼친 목록에는 위스키 이름들이 적혀 있었다."
    s "난 이 향이 좋아. 바닐라 같다가 끝엔 나무 향이 남거든. 너도 작은 잔으로 한 번 맛볼래?"
    d "네. 한 잔만요. 음식은 제가 시켜 볼게요."
    "각자 작은 위스키 한 잔과 음식을 주문했다. 첫입을 먹은 서윤이 도현 쪽을 보고 포크를 잠깐 멈췄다."
    s "내 쪽도 맛있는데 네 표정이 더 맛있어 보이네."
    d "한 입 바꾸실래요? 아까 자리 고르신 이유도 있고요."
    "작은 접시에 한 입씩 덜었다. 바꿔 먹고 나서도 서윤은 자기 접시로 바로 돌아가지 않았다."
    s "오늘 장소는 네가 이겼다."
    d "다음에도 제가 정해도 되는 거죠?"
    s "응. 대신 내 차례도 남겨 둬."
    "식사를 마치고 물을 시켰다. 서윤이 휴대폰 달력을 가운데로 놓았다."
    $ progression_enter("seoyun_r15.choice01")
    $ progression_checkpoint("seoyun_r15.choice01")
    menu:
        "보고 싶다는 마음 뒤에는 다음 날짜도 같이 물어보자고 한다.":
            d "다음에도 제가 보고 싶다고 할게요. 언제 시간 되는지도 같이 물을게요."
            s "다음 금요일 일곱 시는 어때? 네 일정도 보고 답해 줘."
            d "좋아요. 그날은 제가 궁금한 가게 하나 더 가져올게요."
            $ remember("seoyun_future_promise", "다음 금요일19시, 서로의 일정을 확인한 뒤 만남 확정")
        "아직 못 정한 일은 다시 이야기할 날을 같이 정하자고 한다.":
            d "소개 같은 얘기는 오늘 다 정하지 말고, 다음 달에 마음이 어떤지 다시 얘기해요."
            s "응. 둘째 토요일 오후 두 시 어때? 그때도 아직이면 아직이라고 말하고."
            d "좋아요. 저도 제 생각을 가져올게요."
            $ remember("seoyun_future_promise", "다음 달 둘째 토요일14시 소개와 서로의 준비를 다시 이야기, 소개 확정 아님")
        "나도 힘들거나 쉬고 싶을 때 먼저 말하겠다고 한다.":
            d "저도 쉬고 싶은 날엔 말할게요. 오늘은 반대예요. 좀 더 같이 있고 싶어요."
            s "그 말 기다렸어. 나도 계산하고 바로 헤어지긴 아까웠거든."
            $ remember("seoyun_future_promise", "서로 쉬는 시간과 함께 있고 싶은 마음을 먼저 말하기")
    $ location = "같은 금요일 저녁 · 서윤의 작업실"
    "돌봄 일정은 미리 맞춰 둔 날이었다. 천천히 걸어 서윤의 개인 작업실에 들렀다."
    "서윤이 물 두 잔을 놓았다. 도현은 가방을 의자 옆에 내려놓고 앉았다."
    s "여기 두고 입는 편한 옷도 있고, 전에 사 둔 마술사 재킷도 있어. 지금 보여 줄까?"
    $ progression_enter("seoyun_r15.choice02")
    $ progression_checkpoint("seoyun_r15.choice02")
    menu:
        "편한 생활복으로 쉬자고 한다.":
            d "오늘은 편하게요. 같이 앉아 있는 게 좋아요."
            $ remember("seoyun_r15_outfit", "home")
        "서윤도 지금 원한다면 마술사 의상을 보고 싶다고 한다.":
            d "서윤 씨도 입어 보고 싶으시면 저도 궁금해요."
            s "내가 보여 주고 싶어서 꺼낸 거야~ 소매에서 꽃 나오는 건 기대하지 말고."
            $ remember("seoyun_r15_outfit", "cosplay")
        "서윤이 오늘 더 편한 쪽을 정해 달라고 한다.":
            s "그럼 오늘은 생활복. 갈아입는 동안 네가 무슨 표정일지부터 궁금하네."
            d "여기서 기다리고 있을게요."
            $ remember("seoyun_r15_outfit", "home")
    "서윤이 생활복으로 갈아입고 돌아왔다. 도현이 옆자리를 비우자 서윤은 웃으며 앉았다."
    s "오늘 내가 뭘 했을 때 네가 제일 좋아했는지 궁금한데."
    d "메뉴 기다리는 동안 서윤 씨가 제 쪽으로 의자 당기신 거요."
    s "...그건 못 봤을 줄 알았는데."
    d "저도 조금 당겼어요."
    "서윤이 두 의자 사이를 보고 웃었다. 잠깐 뒤에는 도현의 눈을 마주 봤다."
    s "오늘은 여기서 더 같이 있고 싶어. 네 마음도 듣고 싶고."
    call seoyun_private_evening("r15", memory["seoyun_r15_outfit"])
    $ award_once("seoyun_R15", "seoyun", 5)
    $ progression_note_ending()
    return

label seoyun_r16:
    $ progression_enter("seoyun_r16")
    $ progression_checkpoint("seoyun_r16")
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "resolved" or "seoyun_R15" not in completed:
        $ progression_note_ending()
        return
    $ chapter = "서윤 R16 · 함께 고르는 다음"
    $ location = "일요일 저녁 · 북카페"
    "서윤이 다음 제안서의 담당란을 보여 줬다. 이번 업무에서 범위 설명을 직접 맡기로 한 자료였다."
    s "이건 내 소식. 이제 네 거 보여 줘."
    "서윤이 자료를 접어 가방에 넣었다."
    "도현은 [memory['seoyun_private_name']]와 함께 골랐던 '[memory['seoyun_booklet_sentence']]'을 넣은 얇은 초안을 잠깐 보여 줬다."
    s "내가 읽고 싶다던 쪽이네. 이건 완성되면 한 부 꼭 줘."
    "서윤은 종이를 덮고 도현의 옆자리로 옮겨 앉았다."
    s "그때까지 오늘은 사람 쪽을 더 볼래."
    d "좋아요. 저도 가까이 앉으신 게 좋아서요."
    $ remember("seoyun_booklet_state", "직접 쓴 문장을 남긴 새 초안, 최종 인쇄 전")
    $ progression_enter("seoyun_r16.choice01")
    $ progression_checkpoint("seoyun_r16.choice01")
    menu:
        "같이 걸은 곳을 다시 찾으며 다음 페이지도 쓰고 싶다고 한다.":
            d "[memory['seoyun_walk_detail']], 그날 얘기도 남기고 싶어요. 다음에 같이 다시 봐요."
            s "응. 아이랑 보내는 날이랑 네 일정 보고, 우리 둘이 갈 날 정하자."
            $ remember("seoyun_ending_promise", "revisit")
        "앞으로도 다음 질문과 대답을 서로 기다려 주자고 한다.":
            d "모르는 게 생기면 다시 물어보고 싶어요. 좋아한다는 말도 아끼지 않고요."
            s "응. 나도 괜히 어려울 거라고 미리 결론 내지 않을게."
            $ remember("seoyun_ending_promise", "next_answer")
        "각자의 생활과 함께 보내는 시간을 모두 존중하는 연인이 되고 싶다고 한다.":
            d "아이가 있는 서윤 씨 일상도, 제 일상도 지키면서 계속 만나고 싶어요. 둘이 바라는 시간도 같이 만들고요."
            s "응. 안 보는 날 보고 싶어지면 말할게. 당장 와 달라는 뜻으로 보내진 않고."
            $ remember("seoyun_ending_promise", "own_and_shared")
    "도현이 초안을 넣는 사이 서윤이 가방을 챙겼다. 이번엔 같이 일어났다."
    d "오늘은 어디까지 걸을까요?"
    s "골목 끝까지. 그다음엔 네가 돌아갈 시간도 봐야지~"
    if memory.get("seoyun_expression") == "quiet_public":
        "조용한 골목에서 손잡고 걸어도 되는지 서로 물었다. 도현이 손을 내밀었다."
    else:
        "카페를 나와 눈을 맞췄다. 좋다는 대답을 듣고 도현이 손을 내밀었다."
    $ remember("seoyun_route_completed")
    $ persistent.local_seoyun_ending = True
    $ ending = "seoyun_good"
    $ award_once("seoyun_R16", "seoyun", 4)
    "서윤 본편 결말 · 함께 고르는 다음"
    $ progression_note_ending()
    return

label seoyun_e01:
    $ progression_enter("seoyun_e01")
    $ progression_checkpoint("seoyun_e01")
    if not dating or active_route != "seoyun" or not memory.get("seoyun_route_completed"):
        $ progression_note_ending()
        return
    $ chapter = "서윤 E01 · 같이 고른 자리"
    $ location = "약 반년 뒤, 쉬는 날 오후 · 단골 북카페"
    "서윤은 이혼 후 아이와 지내는 생활을 이어 가고 있었다. 아이 아빠와는 필요한 일정만 조율했고, 도현과 만날 날은 서로의 달력을 보고 정했다."
    $ remember("seoyun_family_state", "divorced_parent")
    "도현은 완성한 기록집을 건넸다. '[memory['seoyun_booklet_sentence']]'와 서윤의 감상도 남아 있었다."
    s "내가 읽고 싶다고 한 쪽, 진짜 남겼네."
    d "서윤 씨 몫은 첫 부예요. 다른 페이지도 같이 보고 싶어서요."
    "서윤이 표지를 손바닥으로 쓸었다. 첫 장을 읽고 나서는 자기 컵보다 책을 먼저 도현 쪽으로 밀었다."
    s "여기서 웃었어. 왜인지는 네가 맞혀 볼래?"
    $ remember("seoyun_booklet_state", "이후 직접 촬영·글 정리를 마쳐 인쇄 기록집 완성")
    if memory.get("seoyun_o03_status") == "completed":
        s "그날 우리가 앉았던 자리도 생각나. 오늘은 또 다른 쪽이네."
        d "오늘 빛은 여기까지 들어오길래요."
    if memory.get("seoyun_walk_route") == "familiar":
        s "나갈 때 서점 뒤 골목까지 걸을래? 화분이 하나 더 늘었더라."
    elif memory.get("seoyun_walk_route") == "riverside":
        s "그 다리까지 걸을래? 오늘은 바람이 덜 부는 것 같아."
    else:
        s "골목 쪽으로 좀 걸을래? 어디서 돌아갈지는 같이 정하고."
    s "그리고 아이한테 엄마가 만나는 사람이 있다고 얘기했어. 너한테 당장 만나 달라는 건 아니고."
    d "네. 서윤 씨는 지금 어떻게 생각하세요?"
    s "천천히 생각해 보고 싶어. 아이도 편해야 하고, 네 마음이 어떤지도 듣고 싶고."
    $ remember("seoyun_child_knows_relationship")
    $ progression_enter("seoyun_e01.choice01")
    $ progression_checkpoint("seoyun_e01.choice01")
    menu:
        "모두 편한 때에 짧게 인사할 만남을 함께 생각해 본다.":
            d "저도 인사해 보고 싶어요. 아이도 괜찮다면 잠깐 만나는 날부터 같이 정해요."
            s "응. 아이한테도 물어볼게. 서로 괜찮으면 그때 가볍게 인사부터 하자."
            $ remember("seoyun_epilogue_choice", "consider_introduction")
            $ remember("seoyun_child_introduction_status", "서로 의향만 확인, 아이의 의사와 구체적 일정은 확인 전")
        "소개는 조금 더 생각하고 둘만의 데이트를 이어가고 싶다고 한다.":
            d "저는 좀 더 생각하고 싶어요. 오늘은 서윤 씨랑 걷고, 다음에도 이렇게 만나고 싶고요."
            s "응. 오늘 대답은 그걸로 들을게. 돌아가는 길엔 내가 하나 더 물어볼래~"
            $ remember("seoyun_epilogue_choice", "couple_time")
            $ remember("seoyun_child_introduction_status", "소개 보류, 둘만의 교제 지속")
        "각자의 생활을 어떻게 지킬지부터 더 이야기하고 싶다고 한다.":
            d "가까워지면 저희 생활이 어떻게 달라질지도 얘기하고 싶어요. 오늘 다 정하지 않아도요."
            s "응. 나도 네가 바라는 하루부터 듣고 싶어. 내가 혼자 그려 놓은 집 말고."
            $ remember("seoyun_epilogue_choice", "discuss_life")
            $ remember("seoyun_child_introduction_status", "소개·동거 결정 전 생활 방식부터 논의")
    "서윤이 책갈피를 끼워 기록집을 넣었다. 나란히 골목으로 걸어 나왔다."
    s "오늘 내가 갖고 싶은 게 하나 더 있는데."
    d "어떤 거요?"
    s "네 손. 길 끝까지만 잡아도 되고, 더 걷고 싶으면 그때 물어볼게."
    "도현은 손을 내밀었다. 돌아갈 시간이 되자 인사를 나누고 각자의 집으로 향했다."
    $ remember("seoyun_relationship_status", "이혼 후 아이를 키우는 서윤과 서로의 생활·의사를 존중하며 교제 지속")
    $ remember("seoyun_cohabitation_status", "결혼·동거·부모 역할 확약 없음, 소개는 각자의 준비에 따라 별도 논의")
    $ remember("seoyun_epilogue_completed")
    $ award_once("seoyun_E01", "seoyun", 8)
    $ progression_note_ending()
    return
