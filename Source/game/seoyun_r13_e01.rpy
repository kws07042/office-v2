label seoyun_r13:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 R13 · 말하지 않은 사람"
    $ location = "다음 월요일 저녁 · 카페"
    "도현은 금요일에 미뤘던 이야기를 꺼내려 했다. 서윤이 가방에서 수첩을 찾다가 작은 반지 케이스를 탁자에 떨어뜨렸다."
    "뚜껑이 벌어진 케이스에는 반지가 하나 있었다. 서윤은 덮으려던 손을 멈췄다."
    d "그 반지, 무슨 반지예요?"
    s "...결혼반지야."
    d "전에 하셨던 결혼이요?"
    s "아니. 나 지금도 결혼한 상태야. 남편하고 같은 집에서 살고 있어."
    $ remember("seoyun_marriage_state", "married_cohabiting")
    $ remember("seoyun_marriage_revealed")
    $ remember("seoyun_conflict", "open")
    $ remember("seoyun_dismissed_request", "혼인 사실과 배우자 동거를 숨긴 채 교제하고 미래 질문을 피함")
    "도현은 반지보다 서윤을 봤다. 서윤은 케이스를 가방에 숨기지 못했다."
    menu:
        "교제하기 전에 왜 말하지 않았는지 묻는다.":
            d "제가 알고도 만나겠다고 한 적은 없잖아요. 왜 사귀기 전에 말 안 하셨어요?"
            s "말하면 네가 안 만날 것 같았어. ...그래서 네가 고를 기회를 뺏었어."
            $ remember("seoyun_r13_response", "weight")
        "별거나 관계 정리가 진행 중인지 사실부터 묻는다.":
            d "별거 중인 것도 아니고요? 정리하고 있다는 말씀이에요?"
            s "아니. 지금 헤어지는 절차를 밟고 있는 것도 아니야. 그렇게 들리게 말하고 싶었는데, 그것도 거짓말이겠지."
            $ remember("seoyun_r13_response", "unknown")
        "지금은 대답하기 어렵다며 잠깐 거리를 둔다.":
            d "잠깐만요. 지금은 아무 말도 잘 안 나와요. 밖에 좀 있다 올게요."
            "도현이 돌아올 때까지 서윤은 혼자 앉아 있었다. 반지 케이스는 닫혀 있었지만 탁자 위에 남아 있었다."
            s "네가 돌아온 걸 괜찮다는 대답으로 듣지는 않을게."
            $ remember("seoyun_r13_response", "pause")
    d "그 작업실은요? 저는 서윤 씨가 혼자 지내는 곳인 줄 알았어요."
    s "개인 작업실이야. 내가 사는 집은 따로 있어. 네가 그렇게 생각하는 걸 알면서 안 고쳤어."
    if memory.get("seoyun_publicity") == "told_yujin":
        d "유진 씨가 축하해 준 것도요. 그 사람도 모르잖아요."
        s "응. 유진이도 몰라. 내가 네 앞에서 그 말을 듣고도 가만히 있었어."
    else:
        d "우리끼리만 알자는 것도 회사 때문만은 아니었네요."
        s "응. 내가 숨길 게 있다는 말을 네가 조심해야 한다는 말로 바꿨어."
    d "그래서 같이 살 생각은 어떠냐는 말에도 답을 못 하셨고요."
    s "응. 너는 나하고 같이 사는 걸 생각했는데, 나는 이미 남편하고 살고 있으니까."
    "서윤은 케이스를 가방에 넣었다. 이번에는 도현이 보고 있는 동안 넣었다."
    s "미안해. 집에 문제가 있다는 말로 내가 한 일을 줄이지는 않을게. 네가 계속 만나 줘야 할 이유도 아니고."
    d "지금 용서한다고는 못 해요. 알고 나서 뭘 할지도 제가 정할게요."
    $ remember("seoyun_future_question_status", "기혼·배우자 동거 공개, 계속 교제할지 도현의 판단 대기")
    $ remember("seoyun_trust_status", "damaged_not_restored")
    $ remember("seoyun_conflict", "discussing")
    $ award_once("seoyun_R13", "seoyun", 0)
    return

label seoyun_r14:
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "discussing":
        return
    $ chapter = "서윤 R14 · 알고 나서 고르는 것"
    $ location = "같은 월요일 저녁 · 카페"
    s "이번 수요일 일곱 시에 여기 올게. 지금 네가 결정 못 해도 돼. 대신 그때는 묻는 걸 피하지 않을게."
    menu:
        "수요일에 사실을 더 듣고 관계를 판단하겠다고 한다.":
            d "그날은 제가 묻는 걸 그대로 답해 주세요. 듣고 나서 제 마음도 말할게요."
            $ remember("seoyun_r14_choice", "ready")
        "말만으로는 믿기 어렵다고 하고, 숨긴 사실을 분명히 말해 달라고 한다.":
            d "이제 어떤 말을 믿어야 할지 모르겠어요. 남편하고 끝낼 거라는 약속 말고, 지금 사실부터요."
            s "응. 이혼하기로 정한 것도 아닌데, 그럴 거라고 약속하지는 않을게."
            $ remember("seoyun_r14_choice", "repair_blunt")
        "연애를 마치고 동료로 지내고 싶다고 말한다 — 관계 종료 확인.":
            menu:
                "관계 종료를 확정한다.":
                    d "저는 이 관계를 계속하지 않을래요. 회사에서는 필요한 일만 함께해요."
                    s "알겠어. 내가 숨긴 일 때문에 네가 남아 있어야 하는 건 아니야. 수요일 약속도 잡지 않을게."
                    $ dating = False
                    $ remember("seoyun_relationship_closed")
                    $ ending = "seoyun_relationship_closed"
                    "둘은 따로 카페를 나왔다. 사적인 다음 약속은 잡지 않았다."
                    return
                "결정을 취소하고 수요일에 이야기를 듣는다.":
                    d "지금 끝내겠다는 결정은 취소할게요. 수요일에 한 번 더 듣고 싶어요."
                    s "응. 그걸 용서라고 생각하지 않을게."
                    $ remember("seoyun_r14_choice", "reconsidered")
                "종료 결정은 보류하고 사실을 들은 뒤 다시 고른다.":
                    d "지금은 결정하지 않을게요. 수요일에 듣고 다시 고를래요."
                    s "알겠어. 네 대답을 미리 받아 두려고 하진 않을게."
                    $ remember("seoyun_r14_choice", "wait_action")
    $ remember("seoyun_repair_appointment", "이번 수요일 저녁 일곱 시, 같은 카페에서 혼인 상태와 숨긴 사실 확인")
    $ remember("seoyun_conflict", "agreed_pending_action")
    $ location = "약속한 수요일 저녁 일곱 시 · 같은 카페"
    "서윤은 먼저 와 있었다. 도현이 앉자 휴대폰을 뒤집어 숨기지 않고 가방 안에 넣었다."
    d "지금도 같은 집에서 지내는 거죠?"
    s "응. 그건 월요일하고 달라진 게 없어."
    d "제가 이혼하실 때까지 기다리면 된다는 상황도 아니고요."
    s "응. 끝내겠다고 정하지 않았어. 너한테는 계속 만나고 싶다고 말하면서, 거기는 그대로 두고 있어."
    "도현은 준비한 질문을 보지 않고 한동안 탁자를 봤다."
    d "저를 좋아한다는 말만 들으면 나머지는 제가 눈감아야 하네요."
    s "좋아하는 건 맞아. 그런데 그 말로 내가 한 선택이 없어지지는 않아. 네가 눈감아 줘야 한다고 말할 수도 없고."
    d "앞으로 제가 불편하다고 하면 농담으로 넘기지 마세요. 끝내고 싶다는 말도요."
    s "응. 그리고 우리 만남이 들키지 않게 네가 뭘 해 달라고 요구하지는 않을게. 내가 돌아가는 생활까지 네 책임으로 만들지는 않을 거야."
    "도현은 서윤을 봤다. 월요일보다 사실은 분명해졌지만 마음이 가벼워지지는 않았다."
    $ remember("seoyun_repair_performed", "수요일 실제 대면에서 현재 혼인·배우자 동거·정리 미결정 사실을 확인")
    menu:
        "혼인 사실을 안 상태로도, 지금은 계속 만나기로 한다.":
            d "지금은 계속 만나고 싶어요. 그렇다고 괜찮아졌거나, 끝날 때까지 기다리겠다는 뜻은 아니에요."
            s "응. 네가 오늘 고른 걸 앞으로도 무조건 같은 대답으로 두지 않을게."
            $ remember("seoyun_continues_after_disclosure")
        "사실을 들었지만 관계는 여기서 마치기로 한다.":
            d "좋아하는 마음은 남아 있어요. 그래도 알고 나서는 계속 못 만나겠어요."
            s "알겠어. 오늘 와서 끝까지 말해 준 건 고마워. 내가 더 붙잡지는 않을게."
            $ dating = False
            $ remember("seoyun_relationship_closed")
            $ ending = "seoyun_relationship_closed"
            "두 사람은 각자 일어났다. 다음의 사적인 약속은 없었다."
            return
    $ remember("seoyun_conflict", "resolved")
    $ remember("seoyun_future_question_status", "혼인 지속을 알고 교제 지속 선택, 신뢰 회복·이혼·동거 약속 아님")
    if memory.get("seoyun_r14_choice") == "wait_action":
        $ remember("seoyun_continuation_reconfirmed")
    s "다가오는 금요일 일곱 시, 같이 저녁 먹을래? 지금 물을 수 있는 건 그 만남이야."
    d "네. 금요일 일곱 시요."
    "서윤은 웃으려다 고개만 끄덕였다. 도현이 먼저 일어났고, 서윤은 그가 외투를 입는 동안 기다렸다."
    $ remember("seoyun_r15_appointment", "금요일 저녁 일곱 시 식사")
    $ award_once("seoyun_R14", "seoyun", 8)
    return

label seoyun_r15:
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "resolved":
        return
    $ chapter = "서윤 R15 · 다음 금요일은 우리 약속"
    $ location = "약속한 금요일 저녁 일곱 시 · 식당"
    "서윤은 식당의 위스키 목록을 펼쳤다. 평소 좋아하는 한 종류를 짚고 도현에게는 향이 다른 쪽을 보여 줬다."
    s "난 이 향이 좋아. 바닐라 같다가 끝엔 나무 향이 남거든. 너도 작은 잔으로 한 번 맛볼래?"
    d "네. 한 잔만요. 술은 추천받았으니까 음식은 제가 골라도 돼요?"
    s "오, 교환 조건이 생겼네? 좋아. 오늘은 네가 고른 걸 먹어 볼게. 중간에 바꿔 달라고는 안 할게~"
    "각자 작은 위스키 한 잔과 음식을 주문했다. 서윤은 향을 먼저 맡고 한 모금 맛본 뒤 도현의 접시를 보며 웃었다."
    s "잠깐. 네 쪽이 더 맛있어 보이는 건 인정할게. 한 입 바꿀래?"
    d "아까는 바꾸자는 말 안 하신다더니요?"
    s "...말 바꿀게. 나 네가 고른 것도 먹고 싶어."
    "도현이 자기 접시를 밀어 주자 서윤도 제 접시를 도현 쪽으로 돌렸다. 둘은 식사와 함께 잔을 비우고 물을 주문했다."
    s "이번 주엔 하고 싶던 말을 메시지로 다 못 했어. 지금은 얼굴 보고 들을래."
    menu:
        "보고 싶다는 마음 뒤에는 다음 날짜도 같이 물어보자고 한다.":
            d "보고 싶다는 말만 보내고 달력만 들여다보진 않으려고요. 다음엔 언제 괜찮으세요?"
            s "다음 금요일 일곱 시. 서점 앞에서 볼까?"
            d "좋아요. 그날은 제가 먼저 가서 기다릴게요. 오늘처럼 음식도 제가 고르고요."
            s "그건 한 번 더 심사해 봐야겠는데~"
            $ remember("seoyun_future_promise", "다음 금요일19시 서점 앞 만남을 상호 확정")
        "아직 못 정한 일은 다시 이야기할 날을 같이 정하자고 한다.":
            d "바로 답 못 하는 일은 다시 묻는 날도 같이 정해요. 기다릴 건지 혼자 짐작하지 않게요."
            s "응. 다음 달 둘째 토요일 오후 두 시에 다시 이야기할래? 그때도 정하지 못한 건 그대로 말할게."
            d "좋아요. 그때 저도 제 생각 가져올게요. 오늘 못 정한 것부터요."
            $ remember("seoyun_future_promise", "다음 달 둘째 토요일14시 현재 관계의 한계와 지속 여부 재논의")
        "나도 힘들거나 쉬고 싶을 때 먼저 말하겠다고 한다.":
            d "저도 힘들면 쉰다고 먼저 말할게요. 오늘은 반대예요. 조금 더 같이 있고 싶어요."
            "서윤이 계산서를 보려다 손을 거뒀다."
            s "응. 그럼 서두르지 말자. 나도 지금 네 앞에 더 있고 싶어."
            $ remember("seoyun_future_promise", "각자 쉬고 싶은 때와 함께 있고 싶은 마음을 먼저 말하기")
    $ location = "같은 금요일 저녁 · 서윤의 작업실"
    "식사를 마치고 한동안 걸어 개인 작업실에 도착했다."
    "작업실에 들어와 서윤이 물 두 잔을 놓았다. 도현은 가방을 바로 내려놓지 않았다."
    d "오늘 온 걸로 그 얘기 다 끝났다고 생각하진 말아 주세요."
    s "응. 네가 지금 돌아가고 싶어져도 말해 줘."
    "도현은 잠깐 뒤에야 가방을 의자 옆에 놓았다."
    s "여기 두고 입는 편한 옷도 있고, 전에 사 둔 마술사 재킷도 있어. 지금 보여 줘도 괜찮을까?"
    menu:
        "편한 생활복으로 쉬자고 한다.":
            d "오늘은 편하게요. 같이 앉아 있는 게 좋아요."
            $ remember("seoyun_r15_outfit", "home")
        "서윤도 지금 원한다면 마술사 의상을 보고 싶다고 한다.":
            d "지금도 입어 보고 싶으시면, 저도 보고 싶어요. 맞춰 주시려고 무리하진 말고요."
            s "내가 보여 주고 싶어서 꺼낸 거야~ 소매에서 꽃이 나오는지는 기대하지 말고."
            $ remember("seoyun_r15_outfit", "cosplay")
        "서윤이 오늘 더 편한 쪽을 골라 달라고 한다.":
            s "그럼 오늘은 생활복. 옷까지 골라 보이려니까 좀 웃기네, 나."
            d "먼저 보여 주고 싶다고 하신 것도 좋았어요. 오늘 아니어도요."
            $ remember("seoyun_r15_outfit", "home")
    "서윤이 고른 옷으로 돌아왔다. 도현은 식당에서 자기 접시를 건네던 그녀의 표정이 다시 떠올랐다."
    d "아까 제 음식 달라고 하실 때, 말 바꾸는 게 조금 좋았어요."
    s "그걸 지금 꺼내? ...나 오늘은 여유 있는 척 좀 쉬어도 돼?"
    d "네. 저도 지금은 서윤 씨만 보고 싶어요."
    "작업실에서도 한참 이야기를 나눴다. 서윤은 웃다가 말을 고르듯 잠깐 멈추고 도현과 눈을 맞췄다."
    s "오늘은 여기서 더 같이 있고 싶어. 지금 네 마음도 듣고 싶어."
    call seoyun_private_evening("r15", memory["seoyun_r15_outfit"])
    $ award_once("seoyun_R15", "seoyun", 5)
    return

label seoyun_r16:
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "resolved" or "seoyun_R15" not in completed:
        return
    $ chapter = "서윤 R16 · 농담 뒤의 약속"
    $ location = "일요일 저녁 · 북카페"
    "서윤이 다음 제안서의 담당란을 보여 줬다. 이번 업무에서 범위 설명을 직접 맡기로 한 자료였다."
    s "이건 내 쪽 소식. 이제 네 거 보여 줘."
    "서윤이 자료를 접어 가방에 넣었다."
    "도현은 [memory['seoyun_private_name']]와 함께 골랐던 '[memory['seoyun_booklet_sentence']]'을 넣은 얇은 초안을 잠깐 보여 줬다."
    s "넣었네. 고마워."
    "서윤은 종이를 덮고 도현의 맞은편에서 옆자리로 옮겨 앉았다."
    s "이젠 글씨 말고 너를 볼래. 오늘 나한테 먼저 할 말 없어?"
    d "있어요. 지금처럼 가까이 앉으니까 좋네요."
    s "...그렇게 바로 말할 줄은 몰랐는데."
    $ remember("seoyun_booklet_state", "직접 쓴 문장을 남긴 새 초안, 최종 인쇄 전")
    menu:
        "같이 걸은 곳을 다시 찾으며 다음 페이지도 쓰고 싶다고 한다.":
            d "[memory['seoyun_walk_detail']], 그날 얘기도 남기고 싶어요. 다음에 같이 다시 봐요."
            s "응. 그땐 네가 먼저 길을 고르든, 내가 고르든 한번 따라가 볼게."
            $ remember("seoyun_ending_promise", "revisit")
        "앞으로도 다음 질문과 대답을 서로 기다려 주자고 한다.":
            d "모르는 말이 남아 있어도 서로 물어볼 수 있었으면 좋겠어요. 좋아하는 마음도 제가 먼저 말하고요."
            s "응. 오늘은 바로 대답할게. 더 걷고 싶어."
            $ remember("seoyun_ending_promise", "next_answer")
        "각자의 일과 혼자 쉬는 시간도 남기는 연인이 되고 싶다고 한다.":
            d "각자 하던 것도 좋아하면서 계속 만나요. 보고 싶은 날엔 따로 말하고요."
            s "응. 안 만나는 날에 보고 싶어지면 말할게. 그날 네가 와야 한다는 뜻으로 보내지는 않고."
            $ remember("seoyun_ending_promise", "own_and_shared")
    "도현이 초안을 가방에 넣는 사이 서윤은 계산을 마치고 먼저 일어났다."
    d "이제 어디 가요?"
    s "네가 아까 가까이 앉는 게 좋다고 했잖아. 걷는 동안도 그런지 확인하러."
    "도현이 웃으며 따라나섰다. 서윤은 출입문을 잡고 그를 기다렸다."
    if memory.get("seoyun_expression") == "quiet_public":
        "카페를 나와 조용한 골목에서 손을 잡아도 되는지 서로 물었다. 도현이 먼저 손을 내밀었다."
    else:
        "카페를 나와 서로 눈을 맞췄다. 손잡고 걸어도 좋겠다는 대답을 듣고 도현이 먼저 손을 내밀었다."
    $ remember("seoyun_route_completed")
    $ persistent.local_seoyun_ending = True
    $ ending = "seoyun_good"
    $ award_once("seoyun_R16", "seoyun", 4)
    "서윤 본편 결말 · 알고도 고른 다음"
    return

label seoyun_e01:
    if not dating or active_route != "seoyun" or not memory.get("seoyun_route_completed"):
        return
    $ chapter = "서윤 E01 · 같은 집으로 가지 않는 사람들"
    $ location = "약 반년 뒤, 쉬는 날 오후 · 단골 북카페"
    "서윤은 여전히 혼인 상태였고 배우자와 같은 집에서 지냈다. 반년이 흘렀다고 그 사실이 달라지지는 않았다."
    $ remember("seoyun_marriage_state", "married_cohabiting")
    "도현은 완성한 기록집을 건넸다. '[memory['seoyun_booklet_sentence']]'와 서윤의 감상도 남아 있었다. 서윤은 둘이 처음 그 말을 나눈 쪽에서 멈췄다."
    s "이때는 네가 나에 대해 모르는 게 많았지."
    d "지금은 알고 있는 게 늘었고요. 책에 적지 않은 것도."
    "서윤은 변명하지 않고 페이지를 넘겼다. 도현은 맞은편에 그대로 앉았다."
    $ remember("seoyun_booklet_state", "이후 직접 촬영·글 정리를 마쳐 인쇄 기록집 완성")
    if memory.get("seoyun_o03_status") == "completed":
        s "그날 네가 고른 자리 생각나. 오늘도 네가 골랐네."
        d "오늘은 여기서 얼굴 보고 말하고 싶어서요."
    if memory.get("seoyun_walk_route") == "familiar":
        s "나갈 때 서점 뒤 골목까지 걸을래? 그 화분은 아직 있더라."
    elif memory.get("seoyun_walk_route") == "riverside":
        s "그 다리까지 걸을래? 오늘은 바람이 덜 부는 것 같아."
    else:
        s "골목 쪽으로 조금 걸을래? 돌아갈 데는 오늘 정하고."
    menu:
        "오늘은 함께 걷되, 같이 살 미래를 약속하지는 않는다.":
            d "걷고 싶어요. 오늘 같이 있고 싶은 건 사실이니까요. 그 뒤까지 약속하지는 않을게요."
            s "응. 오늘 걷는 길까지."
            $ remember("seoyun_epilogue_choice", "walk_now")
        "오늘은 먼저 돌아가며, 기다리는 역할에 익숙해지고 싶지 않다고 말한다.":
            d "오늘은 제가 먼저 갈래요. 늘 서윤 씨가 돌아갈 시간만 기다리는 사람이 되고 싶지는 않아서요."
            s "알겠어. 그 말은 내가 들어야 하는 말이네."
            $ remember("seoyun_epilogue_choice", "leave_first")
        "다음 만남도 그때의 마음으로 고르겠다고 분명히 한다.":
            d "다음에도 제가 원해서 만나고 싶어요. 오늘 왔다고 계속 기다리겠다는 대답은 아니에요."
            s "응. 다음 대답도 다시 들을게."
            $ remember("seoyun_epilogue_choice", "no_waiting_promise")
    "서윤은 책갈피를 끼워 기록집을 가방에 넣었다. 둘은 카페를 나왔다."
    if memory.get("seoyun_epilogue_choice") == "leave_first":
        "도현이 먼저 역 쪽으로 걸었다. 서윤은 따라 붙잡지 않고 인사했다. 둘이 함께 살 집을 고르는 약속은 하지 않았다."
    else:
        "골목 끝까지 함께 걸은 뒤 서로 다른 방향으로 돌아섰다. 서윤은 도현이 가리키는 길을 따라갈 수 없었다."
        s "오늘 만나서 좋았어."
        d "저도 좋았어요. 그렇다고 아직 힘든 게 없어진 건 아니고요."
    $ remember("seoyun_relationship_status", "혼인·배우자 동거 지속을 알고 만나는 관계, 이혼·동거 확약 없음")
    $ remember("seoyun_cohabitation_status", "동거 약속 없음, 배우자와 동거 중인 기혼 관계 지속")
    $ remember("seoyun_epilogue_completed")
    $ award_once("seoyun_E01", "seoyun", 8)
    return
