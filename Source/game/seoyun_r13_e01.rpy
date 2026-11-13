# Seoyun route v003: divorced (no children); ex-husband is the pitch client.
label seoyun_r13:
    $ progression_enter("seoyun_r13")
    $ progression_checkpoint("seoyun_r13")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R13 · 내 대답까지 고르지 마요"
    $ location = "약속한 월요일 저녁 일곱 시 · 카페"
    "서윤은 수첩을 펴 놓고 있었다. 오늘 오후 클라이언트 미팅 메모 위에, 이름 하나가 여러 번 줄로 그어져 있었다."
    s "오늘 미팅, 너도 봤지. 상대 쪽 담당자. ...정민재. 내 전남편이야."
    d "...이름 보고 설마 했어요. 괜찮으세요?"
    s "괜찮아. 그래서 말인데, 피칭 끝날 때까지 우리 회사 밖에서도 좀 떨어져 있자. 네가 엮이면 피곤해져."
    d "저한테는 묻지도 않고, 떨어져 있기로 정하신 거예요?"
    "서윤은 수첩 모서리를 손끝으로 꾹 눌렀다."
    s "...그 사람, 다시 만나자고 연락했어. 네가 알면 신경 쓸 거고, 피칭까지 망치면 다 내 탓 같을 것 같아서."
    d "신경 쓸지 말지는 제가 해요. 서윤 씨가 혼자 다 막으면, 저는 옆에서 아무것도 모르는 사람이잖아요."
    $ remember("seoyun_conflict", "open")
    $ remember("seoyun_dismissed_request", "전남편이 피칭 상대로 나타나자 도현에게 묻기 전에 거리를 두기로 혼자 정함")
    $ progression_enter("seoyun_r13.choice01")
    $ progression_checkpoint("seoyun_r13.choice01")
    menu:
        "전남편 일과 내 마음을 대신 결정하는 건 다르다고 말한다.":
            d "그분이 무슨 연락을 하든, 저까지 밀어내는 건 서윤 씨 혼자 정할 일이 아니에요."
            s "응. 너 지키는 척하면서, 사실은 내가 도망친 거네."
            $ remember("seoyun_r13_response", "weight")
        "떨어져 있자는 말보다 무슨 일인지부터 듣고 싶다고 한다.":
            d "떨어져 있자는 말은 나중에 해도 돼요. 지금은 무슨 일이 있었는지부터 들을래요."
            s "...결론부터 던졌네, 내가. 제일 싫어하는 방식인데."
            $ remember("seoyun_r13_response", "unknown")
        "좋아하는 마음과 부담되는 부분을 잠깐 정리하고 말한다.":
            d "저도 안 어려울 거라고는 못 해요. 잠깐만 생각하고 대답할게요."
            "도현이 컵을 내려놓았다. 서윤은 수첩을 덮지 않고 기다렸다."
            d "기다릴 수 있는 것과 싫은 건 저도 말할게요. 아무 일 없는 척하라는 건 싫어요."
            s "응. 네가 잠깐 멈춘 걸 거절로 짐작하지도 않을게."
            $ remember("seoyun_r13_response", "pause")
    s "이혼하고 혼자 잘 살았어. 근데 그 사람이 다시 나타나니까, 너까지 내 지난 일에 끌어들이는 것 같았어."
    d "저는 서윤 씨 지난 일까지 알고 만나는 거예요. 좋은 데만 골라 보여 주는 사람이랑 만나고 싶진 않아요."
    "서윤이 수첩을 접었다. 탁자 위에는 컵 두 개만 남았다."
    s "보고 싶어. 앞으로도. ...그 말부터 했어야 했네."
    d "저도요. 그다음에 그 사람 얘기, 다 해 주세요."
    if memory.get("seoyun_publicity") == "told_yujin":
        s "유진이한테 우리 만난다고 말할 때도 같이 정했지. 정작 너한테는 혼자 답하려고 했네."
    else:
        s "사귀는 걸 누구한테 알릴지도 같이 정했는데. 우리 얘기는 나 혼자 끝내려고 했네."
    s "수요일에 다시 볼래? 그때까지 그 사람한테 할 대답도 정해 갈게."
    d "네. 저도 제가 뭘 견딜 수 있는지 생각해 올게요."
    $ remember("seoyun_future_question_status", "전남편과의 일을 숨기지 않고 수요일에 다시 이야기하기로 함")
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
    $ remember("seoyun_repair_appointment", "수요일 저녁 일곱 시, 전남편 연락과 피칭, 둘의 관계를 숨김없이 이야기")
    $ remember("seoyun_conflict", "agreed_pending_action")
    $ location = "약속한 수요일 저녁 일곱 시 · 같은 카페"
    "서윤은 수첩을 가방에 넣은 채 먼저 와 있었다. 도현이 앉자 메뉴판보다 얼굴부터 봤다."
    s "먼저 말할게. 그 사람한테 답장 보냈어. 다시 만날 생각 없다고. 난 너랑 계속 만나고 싶어. 책 얘기하다 네가 웃는 것도, 아무 말 없이 걷는 것도."
    d "다행이에요. ...솔직히 월요일부터 그 생각만 났어요. 근데 회의실에서 그분 얼굴 또 보면, 저 표정 관리 못 할 것 같아요."
    s "응. 피칭은 피칭으로만 할 거야. 그 사람이 회의 끝나고 따로 보자고 해도, 너 없는 자리엔 안 나가."
    d "저도 회의에선 그냥 TF 막내로 있을게요. 대신 끝나고는 서윤 씨 옆자리 제 거예요."
    s "다시 만나자는 연락 온 거, 바로 말 못 해서 미안해. 네가 날 이혼한 여자로만 볼까 봐, 그게 무서웠나 봐."
    d "저는 한서윤 씨를 보는 거예요. 앞에 뭐가 붙든 상관없어요."
    s "...그 말, 생각보다 세게 들어오네. 피칭 끝나면 그 사람 이름은 내 입에서 다시 안 나올 거야."
    "서윤이 컵을 들었다가 내려놓았다. 이번엔 말을 보태려던 도현을 기다려 줬다."
    d "그리고 둘이 놀러 가고 싶은 데도 하나씩 말해요. 어려운 얘기만 하는 연인은 싫어요."
    s "...나 지금 네가 시킬 디저트가 궁금해. 그건 오늘 물어봐도 되지?"
    d "네. 이번에는 레몬 말고 다른 걸로요."
    "서윤이 웃었다. 도현도 메뉴판을 가운데로 옮겼다."
    $ remember("seoyun_repair_performed", "수요일 실제 대면에서 전남편의 재회 요청을 거절했다고 밝히고 피칭과 연애를 분리하기로 함")
    $ remember("seoyun_mutual_plan_performed")
    $ remember("seoyun_future_boundary_confirmed")
    $ progression_enter("seoyun_r14.choice03")
    $ progression_checkpoint("seoyun_r14.choice03")
    menu:
        "피칭이 끝날 때까지 기다리지 않고 연인으로 계속 만나기로 한다.":
            d "피칭 끝날 때까지 떨어져 있는 거 말고, 지금부터 계속 만나요."
            s "응. 회의실에선 모르는 척, 끝나면 바로 네 쪽."
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
            d "그분 일이 다 끝난 건 아니란 거 알아요. 그래도 계속 만나 보고 싶어요."
            s "나도 그래. 모르는 건 다시 묻고, 대답이 바뀌면 바로 말해 주자."
            $ remember("seoyun_continues_after_discussion")
            $ remember("seoyun_future_discussion_open")
    $ remember("seoyun_conflict", "resolved")
    $ remember("seoyun_future_question_status", "전남편 문제를 공유하고 교제 지속, 피칭 뒤 공개 여부는 별도 논의")
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
            d "회사에 알리는 얘기는 오늘 정하지 말고, 피칭 끝나고 다시 해요."
            s "응. 피칭 끝난 다음 주 토요일 두 시 어때? 그때도 아직이면 아직이라고 말하고."
            d "좋아요. 저도 제 생각을 가져올게요."
            $ remember("seoyun_future_promise", "피칭 끝난 다음 주 토요일 14시, 회사와 친구들에게 알릴지 다시 이야기")
        "나도 힘들거나 쉬고 싶을 때 먼저 말하겠다고 한다.":
            d "저도 쉬고 싶은 날엔 말할게요. 오늘은 반대예요. 좀 더 같이 있고 싶어요."
            s "그 말 기다렸어. 나도 계산하고 바로 헤어지긴 아까웠거든."
            $ remember("seoyun_future_promise", "서로 쉬는 시간과 함께 있고 싶은 마음을 먼저 말하기")
    $ location = "같은 금요일 저녁 · 서윤의 작업실"
    "피칭 전 마지막 주말이었다. 천천히 걸어 서윤의 개인 작업실에 들렀다."
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
            s "응. 피칭 끝나고 첫 주말, 우리 둘이 갈 데부터 정하자."
            $ remember("seoyun_ending_promise", "revisit")
        "앞으로도 다음 질문과 대답을 서로 기다려 주자고 한다.":
            d "모르는 게 생기면 다시 물어보고 싶어요. 좋아한다는 말도 아끼지 않고요."
            s "응. 나도 괜히 어려울 거라고 미리 결론 내지 않을게."
            $ remember("seoyun_ending_promise", "next_answer")
        "각자의 생활과 함께 보내는 시간을 모두 존중하는 연인이 되고 싶다고 한다.":
            d "서윤 씨 일상도, 제 일상도 지키면서 계속 만나고 싶어요. 숨어서 말고요."
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
    "피칭은 TF의 승리로 끝났고, 정민재라는 이름은 그 뒤로 서윤의 입에서 다시 나오지 않았다. 도현과 만날 날은 이제 서로의 달력을 보고 정했다."
    $ remember("seoyun_family_state", "divorced")
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
    s "그리고 팀장님이 우리 사이 눈치챘어. 대놓고 묻진 않았는데, 회식 자리 배치가 수상하더라."
    d "네. 서윤 씨는 지금 어떻게 생각하세요?"
    s "이제 숨길 이유는 없잖아. 근데 네가 회사에서 불편해질까 봐, 그건 네 대답부터 듣고 싶어."
    $ remember("seoyun_friends_know_relationship")
    $ progression_enter("seoyun_e01.choice01")
    $ progression_checkpoint("seoyun_e01.choice01")
    menu:
        "팀에 둘의 관계를 알리자고 한다.":
            d "저는 알리고 싶어요. 회식 때 서윤 씨 옆자리에 눈치 안 보고 앉고 싶어서요."
            s "응. 다음 주 회의 끝나고 같이 말하자. 팀장님 표정 볼만하겠다~"
            $ remember("seoyun_epilogue_choice", "consider_introduction")
            $ remember("seoyun_publicity_status", "서로 의향만 확인, 팀에 알릴 구체적 일정은 확인 전")
        "공개는 조금 더 미루고 둘만의 데이트를 이어가고 싶다고 한다.":
            d "저는 조금만 더 둘만 알고 싶어요. 들킬 듯 말 듯한 것도 아직 재밌어서요."
            s "...그 취향은 몰랐네. 좋아, 오늘 대답은 그걸로 들을게. 돌아가는 길엔 내가 하나 더 물어볼래~"
            $ remember("seoyun_epilogue_choice", "couple_time")
            $ remember("seoyun_publicity_status", "공개 보류, 둘만의 교제 지속")
        "공개보다 같이 사는 얘기를 먼저 해 보고 싶다고 한다.":
            d "알리는 것보다... 저는 서윤 씨 집에 제 칫솔 두는 얘기가 더 하고 싶은데요."
            s "응. 나도 네가 바라는 하루부터 듣고 싶어. 내가 혼자 그려 놓은 집 말고."
            $ remember("seoyun_epilogue_choice", "discuss_life")
            $ remember("seoyun_publicity_status", "공개·동거 결정 전 생활 방식부터 논의")
    "서윤이 책갈피를 끼워 기록집을 넣었다. 나란히 골목으로 걸어 나왔다."
    s "오늘 내가 갖고 싶은 게 하나 더 있는데."
    d "어떤 거요?"
    s "네 손. 길 끝까지만 잡아도 되고, 더 걷고 싶으면 그때 물어볼게."
    "도현은 손을 내밀었다. 돌아갈 시간이 되자 인사를 나누고 각자의 집으로 향했다."
    $ remember("seoyun_relationship_status", "이혼 후 혼자 사는 서윤과 전남편 문제를 정리하고 교제 지속")
    $ remember("seoyun_cohabitation_status", "결혼·동거 확약 없음, 주변 공개는 둘이 정한 때에")
    $ remember("seoyun_epilogue_completed")
    $ award_once("seoyun_E01", "seoyun", 8)
    $ progression_note_ending()
    return
