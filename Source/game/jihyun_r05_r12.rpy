# Jihyun: private requests, actual choices, and a boundary that later needs repair.
label jihyun_r05:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 R05 · 비워 둔 일정표"
    $ location = "고백 다음 날 토요일 오후 · 강변 카페"
    if memory.get("jihyun_next_date_plan") == "dohyun_suggests":
        d "제가 고른 곳이에요. 여긴 창가 자리가 오후에 좀 한산하더라고요."
        j "응. 오늘은 약속 장소 찾는 것부터 도현 씨 따라왔어."
    elif memory.get("jihyun_next_date_plan") == "own_and_shared":
        j "오전엔 내 조립품 조금 만졌어. 오후는 같이 쓰려고 남겼고. 도현 씨는?"
        d "사진 정리했어요. 다 못 끝냈는데, 만나는 시간까지 밀어내고 싶진 않았어요."
    else:
        j "내가 고른 강변이랑 도현 씨가 찾은 카페. 걸어 보니까 생각보다 가깝네."
        d "다음 후보도 서로 하나씩 가져오죠. 취향이 겹치는지도 궁금하고요."
    "지현은 일정표에서 회사 계정을 닫고 개인 달력을 열었다."
    j "일요일 오전엔 조립할 거야. 이번엔 설명서부터 똑바로 펴 놓고. 도현 씨는?"
    menu:
        "일요일 오전엔 사진을 고르고, 저녁 여섯 시에 통화하자고 한다.":
            d "기록집에 넣을 사진 골라 볼게요. 저녁 여섯 시에 서로 뭐 했는지 들려줘요."
            j "좋아. 결과물 검사 말고 얘기 듣는 시간."
            $ remember("jihyun_personal_slot", "일요일 오전 사진 고르기")
            $ remember("jihyun_shared_slot", "일요일 저녁 여섯 시 통화")
        "일요일 오후엔 글을 쓰고, 저녁 일곱 시에 통화하자고 한다.":
            d "오후에 한 줄씩 써 보고 싶어요. 저녁 일곱 시에는 통화 괜찮으세요?"
            j "응. 잘 안 써졌다는 얘기도 해 줘. 쓴 것만 보내지 말고."
            $ remember("jihyun_personal_slot", "일요일 오후 짧은 글 쓰기")
            $ remember("jihyun_shared_slot", "일요일 저녁 일곱 시 통화")
        "일요일엔 푹 쉬고, 월요일 퇴근 후 여섯 시 반에 만나자고 한다.":
            d "내일은 아무것도 안 정하고 쉬고 싶어요. 월요일 여섯 시 반에 저녁 같이 먹어요."
            j "그래. 아무것도 안 하는 칸도 지켜 보자."
            $ remember("jihyun_personal_slot", "일요일 계획 없이 쉬기")
            $ remember("jihyun_shared_slot", "월요일 퇴근 후 여섯 시 반 저녁")
    "카페를 나와 강변을 조금 걸었다. 지현이 발걸음을 늦추고 도현 쪽으로 몸을 돌렸다."
    j "일정 정하는 건 괜찮았는데... 이건 먼저 말하는 게 좀 어렵네. 입맞춤하고 싶어. 도현 씨도 그래?"
    menu:
        "나도 그러고 싶다고 답하고 다가간다.":
            d "네. 저도요. 말씀하실 때부터 가까이 가고 싶었어요."
            "짧게 입맞춤한 지현이 도현을 다시 보고 웃었다."
            j "표정까지 이렇게 바로 들킬 줄은 몰랐네."
            $ first_kiss = True
            $ remember("jihyun_first_kiss", "R05")
            $ remember("jihyun_first_kiss_plan", "R05에서 실제 입맞춤")
            $ remember("jihyun_r05_affection", "kiss")
        "오늘은 손을 잡고 더 걷고 싶다고 한다.":
            d "오늘은 손잡고 더 걸을래요. 물어봐 주신 건 좋았어요."
            j "응. 그럼 이쪽. 손 내미는 건 내가 먼저 할게."
            "지현이 내민 손을 잡고 강변을 걸었다."
            $ remember("jihyun_r05_affection", "hand")
        "입맞춤은 다음으로 두고, 지금은 나란히 걷자고 한다.":
            d "지금은 나란히 걷는 게 좋아요. 다음에도 먼저 말씀해 주세요."
            j "알겠어. 다음 기회까지 혼자 결론 내리진 않을게."
            $ remember("jihyun_r05_affection", "walk")
    $ award_once("jihyun_R05", "jihyun", 4)
    return

label jihyun_r06:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 R06 · 회사 밖의 호칭"
    $ location = "다음 주 수요일 저녁 · 작은 식당"
    j "[memory['jihyun_personal_slot']], 해 봤어?"
    if "사진" in memory["jihyun_personal_slot"]:
        d "세 장 골랐어요. 다시 빼고 넣다 보니 세 장밖에 못 골랐다고 할까 했는데요."
        j "나한테 보고하는 거 아니야~ 그 세 장이 궁금한 거지."
    elif "글" in memory["jihyun_personal_slot"]:
        d "두 줄 썼어요. 한 줄은 지웠고요. 지운 쪽이 더 길었습니다."
        j "그럼 살아남은 한 줄부터. 이유는 듣고 나서 물을게."
    else:
        d "알람도 안 맞추고 잤어요. 덕분에 오늘은 먼저 만나자고 할 기운이 있네요."
        j "그러면 빈칸 잘 썼네. 오늘 먼저 불러 줘서 좋았어."
    if "통화" in memory["jihyun_shared_slot"]:
        "약속한 일요일 저녁에는 통화로 서로의 하루를 들었다. 오늘은 그때 못다 한 얘기를 마주 앉아 이어 갔다."
    else:
        "약속한 월요일 저녁에도 함께 식사했다. 오늘은 그날 얘기하다 웃었던 가게를 다시 떠올렸다."
    $ remember("jihyun_first_shared_slot_kept", memory["jihyun_shared_slot"])
    j "그런데 회사 밖에서도 계속 팀장님이면, 내가 자꾸 밥값 결재해야 할 것 같아."
    menu:
        "둘이 있을 때는 ‘지현 씨’라고 부르고 싶다고 한다.":
            d "지현 씨. ...생각보다 입에 잘 붙는데요?"
            j "그러네. 한 번 더 해 봐. 내가 아직 덜 들었어."
            $ remember("jihyun_private_name", "지현 씨")
        "둘만 있을 때 ‘지현 누나’라고 불러 봐도 되는지 묻는다.":
            d "둘만 있을 때 지현 누나라고 불러도 돼요?"
            j "응. 대신 내가 그 말에 약한 건 회사에 가져가지 마."
            $ remember("jihyun_private_name", "지현 누나")
        "아직은 익숙한 호칭을 쓰되, 사적인 말임을 따로 표현한다.":
            d "호칭은 조금 더 걸릴 것 같아요. 대신 보고 싶다는 말은 안 미룰게요."
            j "좋아. 지금 그 말은 제대로 들었어."
            $ remember("jihyun_private_name", "팀장님")
    j "나는 둘이 있을 때 도현아, 하고 부르고 싶어. 회사에선 도현 씨고."
    d "좋아요. 회사 밖에서는 먼저 돌아볼 것 같네요."
    menu:
        "밖에서도 손을 잡는 건 좋고, 가까이 다가올 땐 눈을 맞춰 달라고 한다.":
            d "손잡는 건 좋아요. 더 가까워질 때는 한 번 눈 맞춰 주세요."
            j "응. 지금처럼 보면 되지? ...말하고 나니까 내가 더 떨리네."
            $ remember("jihyun_affection_scope", "hand_and_check")
        "애정 표현은 조용히 둘만 있을 때 더 편하다고 말한다.":
            d "사람 많을 때보다 둘만 있을 때가 편해요. 싫어서 피하는 건 아니에요."
            j "알겠어. 둘이 있을 때는 내가 먼저 손 내밀 수도 있어. 그때도 네 마음은 말해 줘."
            $ remember("jihyun_affection_scope", "private_place")
        "그때마다 편한지 짧게 말하며 속도를 맞추고 싶다고 한다.":
            d "괜찮을 때도 제가 먼저 말해 볼게요. 마음 바뀌면 그것도 말하고요."
            j "좋아. 그럼 나도 듣기만 하지 않고 말할게. 오늘 보고 싶었다고."
            $ remember("jihyun_affection_scope", "say_each_time")
    $ award_once("jihyun_R06", "jihyun", 6)
    return

label jihyun_r07:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 R07 · 부탁해도 되는 저녁"
    $ location = "토요일 저녁 · 지현의 집"
    "저녁을 먹고 지현이 집에 두고 온 작은 조립품을 보러 갔다. 지현은 평소 입던 사복 그대로 찻잔 두 개를 꺼냈다."
    "지현이 작은 집을 돌려 보여 줬다. 도현이 들여다보려고 몸을 기울이자 손으로 탁자 모서리를 가린다."
    j "머리 조심. 집은 작은데 탁자는 진짜라서."
    d "[memory['jihyun_private_name']], 그럼 오늘은 창틀부터요. 다음에 바뀐 것도 알아볼 수 있겠네요."
    j "...다음 얘기 먼저 하니까 오늘 부탁하기가 조금 쉬워지네."
    j "오늘은 여기서 같이 밤을 보내고 싶어. 도현아, 너는 어때?"
    call jihyun_private_evening("r07", "casual")
    $ award_once("jihyun_R07", "jihyun", 0)
    return

label jihyun_private_evening(slot, outfit):
    menu:
        "나도 같이 밤을 보내고 싶다고 답한다 — 친밀한 장면으로 이어짐.":
            d "저도요. 오늘은 조금 더 같이 있고 싶어요."
            j "응. 서두르지 말자. 나도 원하는 건 말할게."
            call event_sequence("jihyun_" + slot, outfit)
            if not event_main_reached:
                "(거사 — 장면 생략)"
            $ remember("jihyun_" + slot + "_pace", "shared")
            j "이렇게 가까이 있는데 다음 말 기다리는 것도 좋네."
            d "저는 말 고르느라 기다리게 할 수도 있어요. 가고 싶어서 조용한 건 아니에요."
        "오늘은 귀가하고, 다음 만남도 기대한다고 말한다.":
            d "오늘은 집에 가서 쉬고 싶어요. 다음에 또 만나고 싶은 마음은 같아요."
            j "알겠어. 문 앞까지 같이 가자. 다음 약속도 같이 정하고."
            "현관에서 인사를 나누고 도현은 집으로 돌아갔다."
            $ remember("jihyun_" + slot + "_pace", "deferred")
        "마음을 조금 더 나눈 뒤 오늘은 각자 쉬자고 한다.":
            d "같이 있고 싶은 마음은 있어요. 오늘은 그 얘기를 조금 더 하고 돌아갈래요."
            j "응. 긴장한 것도 말해 줘. 나도 오늘은 잘하려고 말 고르는 중이었어."
            "둘은 서로 기대했던 순간과 다음에도 하고 싶은 일을 나눴다. 도현은 늦지 않게 귀가했다."
            $ remember("jihyun_" + slot + "_pace", "talk")
    return

label jihyun_r08:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 R08 · 평소처럼, 조금 다르게"
    if memory.get("jihyun_r07_pace") == "shared":
        $ location = "일요일 아침 · 지현의 집"
        "지현이 먼저 깨어 빵을 굽다가 도현에게 접시를 부탁했다. 아침을 함께 먹고 도현은 집으로 돌아갔다."
        j "다음엔 내가 접시 들게. 빵 굽는 취향도 좀 알고 싶어."
        $ remember("jihyun_r08_shared_morning")
    $ location = "월요일 오후 · 온빛브랜딩 회의실"
    j "이 수치는 원본 확인 전까지 보류하자. 방향이 맞는 것과 근거가 있는 건 따로 봐야 해."
    "지현은 항목별 확인 담당을 정하고 회의를 끝냈다. 사적인 메시지는 퇴근 후 따로 왔다."
    $ location = "같은 월요일 퇴근 후 · 개인 메시지"
    if memory.get("jihyun_r07_pace") == "shared":
        call phone_deliver("jihyun_r08_memory", "jihyun", "접시 하나 꺼냈다가 또 찬장 열었어. 어제 네 몫 놓던 게 손에 남았나 봐.", contact="jihyun")
    elif memory.get("jihyun_r07_pace") == "talk":
        call phone_deliver("jihyun_r08_memory", "jihyun", "토요일에 긴장한 얘기까지 들려줘서 좋았어. 나도 다 아는 척 안 하고 말할 수 있었고.", contact="jihyun")
    else:
        call phone_deliver("jihyun_r08_memory", "jihyun", "토요일에 보여 준 창틀, 오늘 보니까 같이 보던 시간이 먼저 생각나. 집에서는 잘 쉬었어?", contact="jihyun")
    call phone_deliver("jihyun_r08_request", "jihyun", "업무 말고 부탁 하나. 다음 수요일 저녁에 같이 먹고 싶어. 일곱 시 괜찮아?", contact="jihyun", important=True)
    $ phone_context = "jihyun_r08_reply"
    call screen office_phone(replies=[("restaurant", "좋다고 답하고 조용한 식당을 내가 찾아보겠다고 한다."), ("menu", "좋다고 답하고 지현이 먹고 싶은 메뉴를 묻는다."), ("affection", "좋다고 답하고 나도 보고 싶었다고 먼저 표현한다.")])
    $ remember("jihyun_r08_reply", _return)
    $ phone_context = None
    if memory["jihyun_r08_reply"] == "restaurant":
        call phone_deliver("jihyun_r08_reply", "dohyun", "좋아요. 조용한 식당 제가 찾아볼게요. 일곱 시에 봐요.", contact="jihyun")
        call phone_deliver("jihyun_r08_confirm", "jihyun", "응. 식당 찾는 동안 나도 네가 좋아할 메뉴 하나 생각해 둘게. 수요일 일곱 시에 봐.", contact="jihyun")
    elif memory["jihyun_r08_reply"] == "menu":
        call phone_deliver("jihyun_r08_reply", "dohyun", "일곱 시 괜찮아요. 이번엔 먼저 먹고 싶은 걸 말씀해 주세요.", contact="jihyun")
        call phone_deliver("jihyun_r08_confirm", "jihyun", "따뜻한 국수. 오늘은 내가 먼저 골랐어 :) 수요일 일곱 시에 봐.", contact="jihyun")
    else:
        call phone_deliver("jihyun_r08_reply", "dohyun", "저도 보고 싶었어요. 일곱 시에 봬요. 이번에는 제가 먼저 손 내밀게요.", contact="jihyun")
        call phone_deliver("jihyun_r08_confirm", "jihyun", "응. 그 말 읽으니까 수요일이 좀 멀게 느껴지네. 일곱 시에 기다릴게.", contact="jihyun", important=True)
    $ remember("jihyun_r09_appointment", "수요일 저녁 일곱 시 식사")
    $ award_once("jihyun_R08", "jihyun", 4)
    return

label jihyun_r09:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 R09 · 판단을 바꾸는 책임"
    $ location = "수요일 오후 · 검토 회의"
    j "내가 제안한 주말 운영안, 인력 산정에 설치 시간을 빠뜨렸어. 이대로 승인하면 현장에 무리가 생겨. 수정할게."
    d "이전 표랑 실제 동선 같이 놓으면 차이가 보일 것 같아요."
    menu:
        "현장 동선 자료를 찾아 수정 근거에 보탠다.":
            "도현이 설치 동선을 표시했다. 지현은 빠진 시간과 영향을 자료에 직접 적었다."
            $ remember("jihyun_r09_support", "evidence")
        "확인이 필요한 항목을 나눠 맡고 결과를 전달한다.":
            d "장비 반입 시간은 제가 확인할게요. 인원 배치는 팀장님 쪽에서요."
            "각자 확인한 결과를 합쳐 운영 시간을 고쳤다."
            $ remember("jihyun_r09_support", "share")
        "수정안을 처음 보는 사람처럼 읽고 질문을 정리한다.":
            "도현이 왜 바뀌는지 처음 보는 사람도 알 수 있는지 읽었다. 지현은 질문 두 개를 설명에 반영했다."
            $ remember("jihyun_r09_support", "reader")
    j "내 판단에서 빠진 항목이었어. 바꾼 이유까지 같이 전달할게."
    $ location = "같은 수요일 저녁 일곱 시 · 식당"
    d "오늘 바로 틀린 부분 말하시는 게 좋았어요. 멋있다고 생각했고요."
    j "같이 일하는 사람으로도, 만나고 있는 사람으로도?"
    d "네. 두 쪽 다요. 지금은 밥 먹다 자꾸 보게 되는 쪽이 더 크네요."
    j "...그렇게 말하면 나도 평소처럼 먹기는 어렵지."
    "저녁을 먹고 각자의 집으로 향했다. 토요일에는 지현의 취미와 도현의 노트를 같이 보기로 했다."
    $ award_once("jihyun_R09", "jihyun", 6)
    return

label jihyun_r10:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 R10 · 천천히 만드는 취미"
    $ location = "토요일 오후 · 지현의 집"
    "지현은 조립 중인 작은 집을 탁자에 놓았다. 창틀 옆에는 아직 붙이지 않은 지붕이 있었다."
    j "아직 지붕 안 붙였어. 서둘러 닫으면 안쪽 들여다보기 어렵거든."
    d "그럼 안쪽부터요. 제가 고개 넣다가 지붕 닫지는 마세요."
    j "그렇게 큰 모형 아니야."
    d "그건 제가 알아서 작아져 볼게요."
    "지현이 웃다가 붙이지 않은 지붕을 도현 손이 닿지 않는 쪽으로 옮겼다."
    j "그쪽 자신감은 알겠고. 지붕은 내 담당."
    "조립품을 함께 본 뒤 도현이 동네 사진과 짧은 글을 모은 노트를 펼쳤다."
    j "제일 남기고 싶은 건 뭐야? 수정할 점부터 찾지는 않을게."
    menu:
        "저녁 빛이 길게 드는 계단 사진을 남기고 싶다고 한다.":
            d "이 계단이요. 내려가려다 다시 올라가서 찍었어요. 빛이 한 칸만 더 남아서요."
            j "나는 마지막 칸이 어두운 게 좋아. 밖으로 걸어 나가는 것 같아서."
            $ remember("jihyun_booklet_subject", "저녁 계단 사진")
            $ remember("jihyun_booklet_impression", "어두운 마지막 칸이 바깥으로 이어지는 느낌")
        "골목 빵집 문 닫는 소리에 관한 짧은 글을 남긴다.":
            d "문 닫는 소리 들으면 저도 집 갈 시간이구나 싶어서요. 이 문장이 좋아요."
            j "다 읽고 나니까 빵 냄새보다 걸어가는 뒷시간이 생각나네."
            $ remember("jihyun_booklet_subject", "빵집 문 닫는 소리에 관한 글")
            $ remember("jihyun_booklet_impression", "문 닫힌 뒤 집으로 걸어가는 시간")
        "사진 옆에 여백을 남겨 독자가 잠깐 쉬게 하고 싶다고 한다.":
            d "다 설명하지 않고 이 칸은 비워 둘래요. 저는 여기서 잠깐 멈췄으면 좋겠어요."
            j "응. 난 이쪽에 손 얹고 한 번 더 볼 것 같아. 안 적은 것도 남는구나."
            $ remember("jihyun_booklet_subject", "사진 옆 쉬어 가는 여백")
            $ remember("jihyun_booklet_impression", "손을 얹고 한 번 더 보고 싶은 빈칸")
    d "그 감상은 남겨 둘게요. 최종 페이지는 제가 더 골라 보고요."
    j "좋아. 첫 구경꾼은 다음 판도 보고 싶어. 완성 전이어도."
    $ remember("jihyun_booklet_state", "함께 읽은 초안, 최종 구성은 도현이 선택 예정")
    menu:
        "둘이 합의해서 리아에게 교제 사실만 짧게 알리자고 한다.":
            d "리아 씨에게만 저희 만나는 건 말씀드릴까요? 둘이 괜찮다면요."
            j "응. 만난다는 것만. 사적인 얘기는 우리한테 남겨 두자. 내일 같이 보내자."
            $ remember("jihyun_publicity", "agreed_ria")
        "교제 사실은 당분간 둘만 알고 싶다고 한다.":
            d "지금은 둘만 아는 게 좋아요. 바뀌면 먼저 이야기할게요."
            j "응. 오늘 안 알리는 걸 계속 숨기자는 약속으로 묶진 말고."
            $ remember("jihyun_publicity", "private")
        "공개할 때 알려 줄 범위만 정하고 시점은 나중에 정한다.":
            d "나중에 말하면 만난다는 것만요. 언제인지는 더 생각할래요."
            j "좋아. 아직 합의 안 한 날짜를 먼저 잡지는 않을게."
            $ remember("jihyun_publicity", "discuss_later")
    $ award_once("jihyun_R10", "jihyun", 4)
    return

label jihyun_r10_after:
    if not dating or active_route != "jihyun" or "jihyun_R10" not in completed:
        return
    $ location = "같은 토요일 밤 · 지현의 집 — 지현 시점"
    "도현이 돌아간 뒤, 지현은 조립품 옆에 노트를 두던 자리를 한 번 보았다."
    jn "다음 판도 보고 싶다고 했지. ...그냥 다음에도 보고 싶다는 말을 먼저 해도 됐는데."
    "지현은 다음 날 약속 메시지에 ‘노트 없어도 와’를 덧붙여 보냈다."
    call phone_deliver("jihyun_r10_after", "jihyun", "내일은 노트 없어도 와. 같이 놀고 싶어서 부르는 거야~", contact="jihyun")
    $ remember("jihyun_r10_after_completed")
    return

label jihyun_r11:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 R11 · 결정하지 않는 시간"
    $ location = "일요일 저녁 · 지현의 집"
    if memory.get("jihyun_publicity") == "agreed_ria":
        d "어제 정한 대로, 같이 있는 지금 보낼까요?"
        j "응. 나도 옆에서 볼게."
        call phone_deliver("jihyun_r11_disclose", "dohyun", "지현 씨와 연인으로 만나고 있어요. 둘이 같이 말씀드려요. 다른 분들께는 저희가 따로 이야기할게요.", contact="ria")
        call phone_deliver("jihyun_r11_congrats", "ria", "와, 축하해요!! 두 분이 같이 보낸 거예요? 알겠어요~ 다른 데다 먼저 말 안 할게요. 다음에 밥 한 번 같이 먹어요!", contact="ria")
        $ remember("jihyun_publicity", "told_ria")
        $ remember("jihyun_disclosure_delivered")
    "저녁을 먹고 지현이 작은 카드 상자를 꺼냈다. 빵과 차 그림을 모으는 가벼운 게임이었다."
    "지현이 카드를 빠르게 섞다가 도현의 시선을 보고 속도를 늦췄다."
    j "룰은 알려 줄게. 이기는 방법까지는 말고."
    menu:
        "진지하게 한 판 겨뤄 보자고 한다.":
            d "봐주시면 바로 알 거예요. 저도 이기러 왔어요."
            "마지막 차 카드 한 장을 지현이 먼저 골랐다. 도현이 점수를 다시 세자 지현도 손가락으로 옆에서 짚었다."
            d "다시 세도 한 점이네요."
            j "응. 세 번째까지 세면 두 점 될까?"
            j "다음 판도 안 봐줄 거야. ...지금 그렇게 쳐다봐도 안 돼~"
            $ remember("jihyun_game_mode", "competitive")
            $ remember("jihyun_game_result", "지현이 한 점 차이로 이긴 대결")
        "같은 편으로 목표 그림을 모으는 협동 한 판을 고른다.":
            d "이번에는 같은 편으로요. 제가 빵 모으면 차 부탁드려요."
            "마지막 차례에 필요한 그림을 모았다. 지현은 완성된 조합보다 도현의 안도한 표정을 먼저 봤다."
            "지현이 도현의 빵 카드 옆에 차 카드를 붙여 놓았다."
            j "잘했어. 이건 칭찬해도 되지?"
            d "네. 한 번 더 해 주셔도 되고요."
            j "그쪽도 좋아하는구나. 기억했어."
            $ remember("jihyun_game_mode", "cooperative")
            $ remember("jihyun_game_result", "마지막 차례에 목표를 채운 협동")
        "점수 없이 그림으로 내일 먹고 싶은 조합을 만들어 본다.":
            d "저는 빵 두 개랑 차요. 이건 점수보다 내일 아침 생각나네요."
            j "내 조합엔 잼도 있어. 빵만 두 개면 조금 섭섭하지."
            d "점수 안 세니까 취향이 더 세게 나오시네요."
            j "이건 이겨도 잼이 안 생기잖아. 지금 고를래."
            "그림 카드를 나란히 놓고 먹고 싶은 조합을 이야기했다. 점수는 세지 않았다."
            $ remember("jihyun_game_mode", "picture_talk")
            $ remember("jihyun_game_result", "점수 없이 빵·차·잼 조합을 나눈 놀이")
    j "다음 주는 외부 보고 때문에 목요일 저녁까진 좀 엇갈리겠어. 금요일 일곱 시는 비워 둘 수 있는데."
    d "저도 금요일 괜찮아요. 연락은 중간에도 해요. 결과 나올 때만 말하지 말고요."
    $ remember("jihyun_reunion_plan", "다음 금요일 저녁 일곱 시")
    $ award_once("jihyun_R11", "jihyun", 0)
    return

label jihyun_r12:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 R12 · 일정표에 남긴 자리"
    $ location = "금요일 저녁 일곱 시 · 약속한 식당"
    "수요일엔 외부 보고가 늦어졌다는 메시지가, 목요일엔 검토가 끝났다는 메시지가 왔다. 약속한 금요일에 둘이 마주 앉았다."
    j "다음 주 발표 준비도 있어서 미룰까 했어. 그래도 오늘은 보고 싶었어."
    d "저도요. 일요일에 같이 놀던 거 가끔 생각났어요."
    if memory.get("jihyun_game_mode") == "competitive":
        j "한 점 차이 얘기? 아직 재대결 신청 안 받았는데~"
    elif memory.get("jihyun_game_mode") == "cooperative":
        j "같은 편 하자는 말? 오늘도 내 쪽 자리 하나 비워 뒀어."
    else:
        j "잼은 내가 골랐다는 말? 그런 것도 기억해 주는구나."
    j "다음 주 네 발표 안은 내가 먼저 위험한 부분을 추려 둘게. 일정도 덜 힘들게 바꾸면..."
    d "일정 바꾸는 건 제 시간도 확인해 주세요. 지금은 저녁 먹으러 온 거고요."
    j "응. 지금 여기 약속부터. 발표 쪽은 월요일에 자료 놓고 얘기하자."
    $ remember("jihyun_r12_boundary_reminder")
    "식사를 마치고 지현의 집에서 차를 마셨다. 지현은 오늘 만나려고 고른 옷의 소매를 한 번 정리했다."
    j "오늘 너 만나려고 골랐어. 오늘은 잘했다는 말 말고."
    d "예쁘다는 말이요?"
    j "...응. 알아들었으면 그렇게 웃지만 말고."
    d "예뻐요. 들어오실 때부터 말씀드리고 싶었어요."
    "지현이 소매를 놓고 웃었다. 도현을 마주 보는 쪽이 평소보다 조금 늦었다."
    j "그럼 조금 일찍 해 주지. 나 아까부터 소매만 만지고 있었잖아."
    d "다음에는 눈 마주치면 바로 말할게요. 지금도 예뻐요."
    j "...응. 오늘도 같이 있고 싶어."
    call jihyun_private_evening("r12", "special")
    $ award_once("jihyun_R12", "jihyun", 4)
    return
