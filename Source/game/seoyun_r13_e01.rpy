label seoyun_r13:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 R13 · 그냥 한 말은 아니었어"
    $ location = "다음 월요일 저녁 · 카페"
    "도현은 지난 금요일에 꺼냈던 질문을 다시 말했다. 지금 이사하자는 답이 아니라 서로의 생각을 듣고 싶다는 말이었다."
    d "다음 달쯤 시간 잡고 이야기해 볼까요? 같이 살 생각은 어떤지, 아직 모르겠는 건 뭔지요."
    s "그거 그냥 해 본 말 아니었어? 벌써 짐 싸야 하나 싶네~"
    "도현은 웃지 않았다. 서윤도 농담 뒤에 기다리던 대답이 오지 않는 걸 알아챘다."
    $ remember("seoyun_conflict", "open")
    $ remember("seoyun_dismissed_request", "동거 확답이 아닌 미래 대화 요청을 그냥 한 말로 낮춰 들음")
    menu:
        "이사하자는 요구가 아니라 진지한 대화 요청이었다고 말한다.":
            d "짐 싸라는 말은 아니었어요. 제 말이 그냥 한 말이 되니까 서운해요. 같이 생각해 보고 싶어서 꺼냈어요."
            s "...응. 네 질문을 내가 다른 말로 바꿔 버렸네."
            $ remember("seoyun_r13_response", "weight")
        "서윤이 아직 모르겠는 부분부터 듣고 싶다고 말한다.":
            d "아직 모르겠으면 모르겠다고 해 주세요. 저는 웃고 넘어가려고 꺼낸 말이 아니었어요."
            s "모르겠는 걸 말하려다 네 기대를 먼저 가볍게 만들었어."
            $ remember("seoyun_r13_response", "unknown")
        "지금은 서운하니 잠깐 쉬었다가 질문을 다시 이야기한다.":
            d "지금은 좀 서운해요. 바로 웃고 넘어가진 못하겠어요. 잠깐 쉬고 다시 이야기할래요."
            s "응. 그동안 대답이 끝났다고 생각하진 않을게. 여기서 기다릴게."
            "잠깐 각자 차를 마셨다. 도현은 같은 질문을 이사 결정과 대화 요청으로 나누어 다시 말했다."
            $ remember("seoyun_r13_response", "pause")
    "서윤이 컵 손잡이를 잡았다 놓았다. 이번에는 웃지 않고 도현을 봤다."
    s "미안해. 나 답 못 하겠다고 말하기 싫어서 네 말을 가볍게 만들었어."
    s "같이 사는 건 아직 자신 있게 답 못 하겠어. 혼자 쉬는 시간도 필요하고, 일하는 방식도 막 바꾸는 중이야. 그래도 너랑 이 얘기 계속하고 싶어."
    d "그 답을 듣고 싶었어요. 오늘 다 정하자는 건 아니에요. 다음엔 그 얘기할 시간을 실제로 정해요."
    $ remember("seoyun_future_question_status", "동거 결정 미정, 대화하고 싶은 마음은 상호 확인")
    $ remember("seoyun_conflict", "discussing")
    $ award_once("seoyun_R13", "seoyun", 0)
    return

label seoyun_r14:
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "discussing":
        return
    $ chapter = "서윤 R14 · 할 수 있는 약속부터"
    $ location = "같은 월요일 저녁 · 카페"
    s "할 수 있는 약속부터 말할게. 이번 수요일 일곱 시, 여기서 삼십 분. 지금 원하는 생활을 하나씩 말해 보고 싶어. 아직 이사 날짜는 못 정하겠고."
    menu:
        "수요일에 만나 각자 필요한 시간을 이야기하자고 한다.":
            d "좋아요. 저도 제가 필요한 것부터 생각해 올게요. 수요일 일곱 시요."
            $ remember("seoyun_r14_choice", "ready")
        "서툴게 ‘말만 정하면 뭐 해요’라고 했다가, 구체적인 이행을 요청한다.":
            d "이제 시간만 정하면 뭐 해요. 또 농담으로 끝나면요."
            s "그렇게 들리게 했지. 당장 믿으라는 말 대신 수요일에 와서 이야기할게. 그래도 네가 지금 원하는 걸 듣고 싶어."
            d "...저는 아직 서운해서 말이 날카로웠어요. 수요일에는 질문을 끝까지 듣고 답해 주셨으면 해요. 저도 제대로 들을게요."
            $ remember("seoyun_r14_choice", "repair_blunt")
        "연애를 마치고 동료로 지내고 싶다고 말한다 — 관계 종료 확인.":
            menu:
                "관계 종료를 확정한다.":
                    d "저는 연인으로 계속 만나지는 않겠어요. 동료로 지내고 싶어요."
                    s "알겠어. 그 대답도 농담으로 바꾸진 않을게. 수요일 사적인 약속은 잡지 않는 걸로."
                    $ dating = False
                    $ remember("seoyun_relationship_closed")
                    $ ending = "seoyun_relationship_closed"
                    "둘은 각자 집으로 돌아갔다. 다음 업무에서는 동료로 인사하기로 했다."
                    return
                "결정을 취소하고 수요일 약속을 확인한다.":
                    d "끝내겠다는 결정은 취소할게요. 수요일에 대화하고 싶어요."
                    s "응. 취소했다고 지금 서운한 것까지 없어진 걸로 듣지는 않을게."
                    $ remember("seoyun_r14_choice", "reconsidered")
                "종료 결정은 보류하고 실제 대화 뒤 마음을 말한다.":
                    d "지금은 결정하지 않을래요. 수요일에 이야기하고 제 마음도 다시 말할게요."
                    s "알겠어. 대답을 먼저 받아 두려고 하진 않을게."
                    $ remember("seoyun_r14_choice", "wait_action")
    $ remember("seoyun_repair_appointment", "이번 수요일 저녁 일곱 시, 같은 카페에서 삼십 분 생활 이야기")
    $ remember("seoyun_conflict", "agreed_pending_action")
    $ location = "약속한 수요일 저녁 일곱 시 · 같은 카페"
    "서윤은 약속 시간에 와 있었다. ‘혼자 쉬는 시간’과 ‘같이 먹고 싶은 저녁’을 적은 작은 메모를 가져왔다."
    s "오늘은 질문 돌리지 않고 말할게. 같이 살아도 혼자 책 읽는 시간이 필요해. 너랑 저녁 먹는 날도 만들고 싶고. 올해 안에 결정할 수 있을지는 아직 모르겠어."
    d "저도 혼자 글 쓸 시간이 필요해요. 힘들면 연락을 늦게 하는 편이라, 그때는 조용히 쉬고 싶다고 먼저 말하고 싶고요."
    s "응. 나도 책 덮어 놓고 혼자 멍하니 있을 때 있어. 그날은 쉰다고 먼저 말해 둘게. 같이 사는 건, 아직 조금 더 생각하고 싶어."
    "서로 말하는 동안 다른 얘기로 넘기지 않았다. 삼십 분 뒤, 결정한 것과 아직 모르는 것을 따로 적었다."
    $ remember("seoyun_repair_performed", "약속한 수요일19시 실제 만남, 각자 혼자 쉴 시간과 함께 먹을 저녁을 듣고 미정인 결정을 구분")
    $ remember("seoyun_conflict", "resolved")
    $ remember("seoyun_future_question_status", "현재 생활의 바람을 실제 나눔, 동거 결정과 입주 시기는 미정")
    if memory.get("seoyun_r14_choice") == "wait_action":
        d "저는 계속 만나고 싶어요. 모르는 것도 오늘처럼 말해 주신다면요. 미뤄 둔 대답은 지금 할게요."
        s "나도 계속 만나고 싶어. 지금 지킬 수 있는 약속부터 할게. 바라는 건 바라는 대로 말하고."
        $ remember("seoyun_continuation_reconfirmed")
    else:
        d "저도 계속 만나고 싶어요. 바로 다 괜찮아졌다는 건 아니지만, 오늘은 제 질문이 여기 남아 있었어요."
        s "응. 남은 서운함도 다음 얘기로 지워 버리진 않을게."
    s "다가오는 금요일 일곱 시에는 저녁 같이 먹고 싶어. 이번엔 그 약속도 분명히 물을게."
    d "좋아요. 금요일 일곱 시요. 그때는 저도 하고 싶은 얘기 가져올게요."
    $ remember("seoyun_r15_appointment", "금요일 저녁 일곱 시 식사")
    $ award_once("seoyun_R14", "seoyun", 8)
    return

label seoyun_r15:
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "resolved":
        return
    $ chapter = "서윤 R15 · 다음 금요일은 우리 약속"
    $ location = "약속한 금요일 저녁 일곱 시 · 식당"
    s "네가 하고 싶은 얘기 가져온다고 했지. 오늘은 그 말부터 듣고 싶어."
    menu:
        "보고 싶다는 마음 뒤에는 다음 날짜도 같이 물어보자고 한다.":
            d "보고 싶다는 말은 자주 하고 싶어요. 만날 때는 가능한 날짜도 서로 물어보고요."
            s "좋아. 다음 금요일도 일곱 시는 가능해. 너는 어때?"
            d "저도요. 다음 금요일 일곱 시, 서점 앞에서요."
            $ remember("seoyun_future_promise", "다음 금요일19시 서점 앞 만남을 상호 확정")
        "아직 못 정한 일은 다시 이야기할 날을 같이 정하자고 한다.":
            d "바로 답 못 하는 일은 다시 묻는 날도 같이 정해요. 기다릴 건지 혼자 짐작하지 않게요."
            s "응. 생활 얘기는 다음 달 둘째 토요일 오후 두 시에 다시 할래? 지금은 그날 이야기할 약속부터."
            d "좋아요. 아직 결정을 약속한 건 아니고, 같이 이야기할 날이요."
            $ remember("seoyun_future_promise", "다음 달 둘째 토요일14시 생활 이야기 재논의")
        "나도 힘들거나 쉬고 싶을 때 먼저 말하겠다고 한다.":
            d "저도 배려하는 척하면서 제 필요를 늦게 말해요. 오늘은 조금 더 같이 있고 싶다고 먼저 할래요."
            s "응. 난 지금 그 부탁 반가워. 안 해도 알아주길 기다리는 것보다."
            $ remember("seoyun_future_promise", "각자 쉬고 싶은 때와 함께 있고 싶은 마음을 먼저 말하기")
    $ location = "같은 금요일 저녁 · 서윤의 집"
    "식사 뒤 서윤의 집으로 갔다. 서윤은 물을 가져오고 도현 옆에 앉았다."
    s "오늘은 편한 옷도 있고, 전에 마음에 들어 사 둔 마술사 재킷도 있어. 한 번 보여 주고 싶긴 했거든."
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
    "서윤이 고른 옷으로 갈아입고 돌아왔다. 책장 옆에 앉아 조금 전 나눈 약속을 달력에 적었다."
    "서윤이 달력을 덮어 멀리 놓았다. 도현을 돌아보며 웃다가 이번에는 먼저 눈을 내린다."
    s "나 오늘은 여유 있는 척 좀 쉬어도 돼? 네가 먼저 보고 싶었다고 말해 줬으면 좋겠어."
    d "보고 싶었어요. 지금도 더 같이 있고 싶고요."
    s "...응. 그 한마디 듣는데 이렇게 오래 걸리네. 오늘은 같이 밤을 보내고 싶어. 너는 어때?"
    call seoyun_private_evening("r15", memory["seoyun_r15_outfit"])
    $ award_once("seoyun_R15", "seoyun", 5)
    return

label seoyun_r16:
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "resolved" or "seoyun_R15" not in completed:
        return
    $ chapter = "서윤 R16 · 농담 뒤의 약속"
    $ location = "일요일 저녁 · 북카페"
    "서윤은 금요일에 확인받은 문구 범위를 이야기했다. 다음 단계 제안서에서도 직접 약속의 범위를 설명하는 역할을 맡기로 했다."
    s "지킬 수 없는 말까지 예쁘게 쓰고 싶진 않더라. 다음에도 표현만 만드는 사람 말고, 범위까지 설명하는 실무를 맡고 싶어."
    d "저는 그 역할 잘 어울린다고 생각해요. 제 질문에도 기다렸다가 답해 주신 사람이고요."
    "도현은 기록집의 새 초안을 보여 줬다. 두 사람이 함께 본 공간 옆에 직접 쓴 문장이 남아 있었다."
    d "[memory['seoyun_private_name']], 이 문장은 이번 초안에 남겼어요."
    d "[memory['seoyun_booklet_sentence']]"
    "서윤이 자기 감상을 찾아 읽다가 그 옆의 도현 문장으로 다시 눈을 옮겼다."
    s "내 메모 옆에 네 글씨 있으니까, 그날 네가 무슨 표정이었는지 먼저 생각나네."
    d "제 글씨가 그렇게 삐뚤었나요?"
    s "손이 급했지. 나한테 보여 주려던 것 같아서 그건 좀 좋았고~"
    $ remember("seoyun_booklet_state", "직접 쓴 문장을 남긴 새 초안, 최종 인쇄 전")
    menu:
        "같이 걸은 곳을 다시 찾으며 다음 페이지도 쓰고 싶다고 한다.":
            d "[memory['seoyun_walk_detail']], 그날 얘기도 남기고 싶어요. 다음에 같이 다시 봐요."
            s "응. 다음에 바뀐 것도 내가 먼저 다 아는 척 안 하고 볼게."
            $ remember("seoyun_ending_promise", "revisit")
        "앞으로도 다음 질문과 대답을 서로 기다려 주자고 한다.":
            d "모르는 말이 남아 있어도 서로 물어볼 수 있었으면 좋겠어요. 좋아하는 마음도 제가 먼저 말하고요."
            s "응. 나는 대답이 늦는다고 질문까지 없던 걸로 하지 않을게."
            $ remember("seoyun_ending_promise", "next_answer")
        "각자의 일과 혼자 쉬는 시간도 남기는 연인이 되고 싶다고 한다.":
            d "각자 하던 것도 좋아하면서 계속 만나요. 보고 싶은 날엔 따로 말하고요."
            s "좋아. 혼자 읽다 재밌는 문장 보면 보내 줄게. 답장에 꼭 감상문 쓸 필요는 없고~"
            $ remember("seoyun_ending_promise", "own_and_shared")
    s "그래서 다음에도 보고 싶어. 농담 뒤에 숨길 말은 아니고."
    d "저도요. 오늘은 책 덮고 조금 걸을까요?"
    if memory.get("seoyun_expression") == "quiet_public":
        "카페를 나와 조용한 골목에서 손을 잡아도 되는지 서로 물었다. 도현이 먼저 손을 내밀었다."
    else:
        "카페를 나와 서로 눈을 맞췄다. 손잡고 걸어도 좋겠다는 대답을 듣고 도현이 먼저 손을 내밀었다."
    $ remember("seoyun_route_completed")
    $ persistent.local_seoyun_ending = True
    $ ending = "seoyun_good"
    $ award_once("seoyun_R16", "seoyun", 4)
    "서윤 본편 결말 · 농담 뒤의 약속"
    return

label seoyun_e01:
    if not dating or active_route != "seoyun" or not memory.get("seoyun_route_completed"):
        return
    $ chapter = "서윤 E01 · 날짜가 있는 다음"
    $ location = "약 반년 뒤, 쉬는 날 오후 · 단골 북카페"
    "도현은 인쇄한 동네 기록집을 가져왔다. 이후에 직접 찍은 사진과 정리한 글이 작은 책으로 묶여 있었다."
    s "[memory['seoyun_booklet_sentence']] 여긴 종이로 읽으니까 잠깐 멈추는 느낌이 또 다르네."
    d "초안 읽어 주실 때 감상도 기억나요. [memory['seoyun_booklet_impression']], 그 말이요."
    $ remember("seoyun_booklet_state", "이후 직접 촬영·글 정리를 마쳐 인쇄 기록집 완성")
    s "나는 다음 분기에도 제안서를 직접 맡기로 했어. 범위를 설명하는 자리까지 내가 들어가고. 그건 내 쪽 다음 계획이고."
    if memory.get("seoyun_walk_route") == "familiar":
        s "오는 길에 서점 뒤 화분 봤어? 그때보다 하나 더 늘었더라. 오늘 네가 가도 먼저 멈출 것 같아."
    elif memory.get("seoyun_walk_route") == "riverside":
        s "책 읽고 그 다리까지 갈까? 바람 때문에 목소리 낮췄던 날 생각났어."
    else:
        s "오늘도 골목 먼저 걷고 강변 입구에서 돌아올까? 돌아가는 지점은 오늘 다시 고르고."
    if memory.get("seoyun_o01_status") == "completed":
        s "같은 책 읽고도 서로 다른 데 멈춘 날 있지. 난 아직도 네 감상 생각나서 그 장 다시 읽어."
    if memory.get("seoyun_o02_status") == "completed":
        s "지난번 안 통했던 농담은 오늘도 설명 붙여야 웃기겠네. 그때 바로 다시 말해 줘서 좋았어."
    if memory.get("seoyun_o03_status") == "completed":
        d "같이 앉던 자리도 조금씩 바뀌더라고요. 저희가 단골인 이유도요."
    s "같이 살 준비, 이번엔 날짜를 정해서 한 단계씩 이야기하고 싶어. 집 계약까지 오늘 끝내자는 건 아니야."
    menu:
        "다음 달 둘째 토요일 오후 두 시에 비용과 통근 조건을 맞춰 본다.":
            d "그날 서로 생활비랑 통근 조건 적어 와요. 가능한 범위를 같이 보죠."
            s "응. 다음 달 둘째 토요일 두 시, 여기서. 집부터 골라 오지는 않을게."
            $ remember("seoyun_cohabitation_plan", "다음 달 둘째 토요일14시 북카페에서 비용·통근 조건 비교")
        "두 주 뒤 일요일 오후 세 시에 각자의 공간과 생활 시간을 이야기한다.":
            d "책상하고 혼자 쉴 자리, 생활 시간부터요. 두 주 뒤 일요일 세 시 어때요?"
            s "좋아. 여기서 각자 적어 온 걸 놓고 보자. 아직 답 안 맞는 것도 같이."
            $ remember("seoyun_cohabitation_plan", "두 주 뒤 일요일15시 북카페에서 공간·생활 시간 비교")
        "다음 달 첫 토요일 오후 두 시에 준비 목록과 결정 순서부터 정한다.":
            d "뭐부터 알아볼지 같이 적어요. 결정이 필요한 날도 그때 정하고요."
            s "응. 첫 토요일 두 시. 준비 목록을 고르는 약속이지, 그날 꼭 이사 결정한다는 뜻은 아니고."
            $ remember("seoyun_cohabitation_plan", "다음 달 첫 토요일14시 북카페에서 준비 목록·결정 순서 조율")
    "두 사람은 각자 달력에 같은 약속을 적었다. 아직 계약한 집도, 정해 놓은 입주일도 없었다."
    "서윤이 완성된 기록집에 책갈피를 끼웠다. 책갈피는 마지막 장보다 한참 앞에 있었다."
    s "여기 한 번 더 읽으려고. 네가 옆에 있어도 다시 궁금한 게 생기네."
    d "다음 질문도 가져올게요. 그 전에 그냥 보고 싶어서 연락도 하고요."
    s "응. 그건 나도 먼저 할 거야~ 오늘은 조금 더 앉아 있자."
    $ remember("seoyun_cohabitation_status", "함께 살 준비를 위한 다음 대화 날짜·항목 확정, 계약·입주 완료 아님")
    $ remember("seoyun_epilogue_completed")
    $ award_once("seoyun_E01", "seoyun", 8)
    return
