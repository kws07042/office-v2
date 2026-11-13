# Jihyun: private requests, actual choices, and a boundary that later needs repair.
label jihyun_r05:
    $ progression_enter("jihyun_r05")
    $ progression_checkpoint("jihyun_r05")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 R05 · 비워 둔 일정표"
    $ location = "고백 다음 날 토요일 오후 · 강변 카페"
    if memory.get("jihyun_next_date_plan") == "dohyun_suggests":
        d "제가 찾은 데예요. 여기 창가가 오후엔 좀 한산하더라고요."
        j "응. 오늘은 약속 장소 찾는 것부터 네 몫이었지. 잘 찾았네."
    elif memory.get("jihyun_next_date_plan") == "own_and_shared":
        j "오전엔 조립 좀 했어. 오후는 너 만나려고 비웠고. 넌?"
        d "사진 정리했어요. 다 못 끝냈는데, 그것 때문에 약속을 미루고 싶진 않았어요."
    else:
        j "내가 고른 강변이랑 네가 찾은 카페. 걸어 보니까 꽤 가깝네."
        d "다음 후보도 하나씩 가져와요. 취향 겹치는지 궁금해요."
    "음료 옆에 놓인 종이 냅킨을 지현이 두 번 접었다. 도현은 그 위에 빈 설탕 봉지를 세웠다."
    j "뭐 만드는 거야?"
    d "강변 카페 축소판이요. 이건 간판."
    j "간판이 건물보다 큰데."
    d "잘 찾아오시라고요."
    "지현이 봉지를 눕혔다가 다시 세웠다. 냅킨 한 장을 더 펴서 건물 밑에 댄다."
    j "그럼 카페를 키우지. 간판은 눈에 잘 띄네."
    d "고치면서 칭찬하시는 거예요?"
    j "...그럼 칭찬부터. 간판 잘 만들었네."
    "도현이 간판을 다시 만지려다 멈췄다. 지현은 웃고 나서 휴대폰의 개인 달력을 열었다."
    j "일요일 오전엔 조립할 거야. 이번엔 설명서 똑바로 펴 놓고. 넌?"
    $ progression_enter("jihyun_r05.choice01")
    $ progression_checkpoint("jihyun_r05.choice01")
    menu:
        "일요일 오전엔 사진을 추리고, 저녁 여섯 시에 통화하자고 한다.":
            d "기록집에 넣을 사진 추려 볼게요. 저녁 여섯 시에 뭐 했는지 서로 얘기해요."
            j "응. 난 조립하다 부품 못 찾았다고 전화할 수도 있어."
            $ remember("jihyun_personal_slot", "일요일 오전 사진 고르기")
            $ remember("jihyun_shared_slot", "일요일 저녁 여섯 시 통화")
        "일요일 오후엔 글을 쓰고, 저녁 일곱 시에 통화하자고 한다.":
            d "오후에 한 줄씩 써 보고 싶어요. 저녁 일곱 시에는 통화 괜찮으세요?"
            j "응. 한 줄만 와도 읽어 볼게. 나도 조립 끝내긴 어려울 것 같거든."
            $ remember("jihyun_personal_slot", "일요일 오후 짧은 글 쓰기")
            $ remember("jihyun_shared_slot", "일요일 저녁 일곱 시 통화")
        "일요일엔 푹 쉬고, 월요일 퇴근 후 여섯 시 반에 만나자고 한다.":
            d "내일은 아무것도 안 정하고 쉬고 싶어요. 월요일 여섯 시 반에 저녁 같이 먹어요."
            j "좋아. 월요일엔 잘 잤냐고만 물어볼게. ...좀 부럽네."
            $ remember("jihyun_personal_slot", "일요일 계획 없이 쉬기")
            $ remember("jihyun_shared_slot", "월요일 퇴근 후 여섯 시 반 저녁")
    "카페를 나와 강변을 조금 걸었다. 지현이 발걸음을 늦추고 도현 쪽으로 몸을 돌렸다."
    j "일정 짜는 건 쉬운데... 이건 말로 하기 어렵네. 키스하고 싶어. 너는?"
    $ progression_enter("jihyun_r05.choice02")
    $ progression_checkpoint("jihyun_r05.choice02")
    menu:
        "나도 그러고 싶다고 답하고 다가간다.":
            d "네. 저도요. 말씀하실 때부터 다가가고 싶었어요."
            "입술이 닿기 직전, 지현의 휴대폰이 울렸다. 화면에 ‘본부장’이 떠 있었다. 지현은 전화를 끊어 버리고, 이번엔 망설임 없이 도현의 넥타이를 당겼다."
            j "...회사 전화 처음 씹어 봤어. 표정 관리 안 되네."
            $ first_kiss = True
            $ remember("jihyun_first_kiss", "R05")
            $ remember("jihyun_first_kiss_plan", "R05에서 실제 입맞춤")
            $ remember("jihyun_r05_affection", "kiss")
        "오늘은 손을 잡고 더 걷고 싶다고 한다.":
            d "오늘은 손잡고 더 걷고 싶어요. 물어봐 주신 건 좋았어요."
            j "응. 그럼 이쪽. 손은 내가 내밀게."
            "지현이 내민 손을 잡고 강변을 걸었다."
            $ remember("jihyun_r05_affection", "hand")
        "키스는 다음으로 두고, 지금은 나란히 걷자고 한다.":
            d "지금은 이렇게 걷는 게 좋아요. 다음에도 그렇게 물어봐 주세요."
            j "응. 그럼 저 다리까지만 더 가자."
            $ remember("jihyun_r05_affection", "walk")
    $ award_once("jihyun_R05", "jihyun", 4)
    $ progression_note_ending()
    return

label jihyun_r06:
    $ progression_enter("jihyun_r06")
    $ progression_checkpoint("jihyun_r06")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 R06 · 회사 밖의 호칭"
    $ location = "다음 주 수요일 저녁 · 작은 식당"
    j "지난번에 혼자 하고 싶다던 거, 해 봤어?"
    if "사진" in memory["jihyun_personal_slot"]:
        d "세 장 골랐어요. 넣었다 뺐다 하다 보니 세 장밖에 못 골랐다고 할 뻔했는데요."
        j "나한테 보고하는 거 아니야~ 그 세 장이 궁금한 거지."
    elif "글" in memory["jihyun_personal_slot"]:
        d "두 줄 썼어요. 한 줄은 지웠고요. 지운 쪽이 더 길었습니다."
        j "그럼 살아남은 한 줄부터. 이유는 듣고 나서 물을게."
    else:
        d "알람도 안 맞추고 잤어요. 덕분에 오늘은 만나자는 말 할 기운이 남았네요."
        j "그럼 쉬는 날 잘 썼네. 오늘 불러 줘서 좋았어."
    if "통화" in memory["jihyun_shared_slot"]:
        "약속한 일요일 저녁에는 통화로 서로의 하루를 들었다. 오늘은 그때 못다 한 얘기를 마주 앉아 이어 갔다."
    else:
        "약속한 월요일 저녁에도 함께 식사했다. 오늘은 그날 얘기하다 웃었던 가게를 다시 떠올렸다."
    $ remember("jihyun_first_shared_slot_kept", memory["jihyun_shared_slot"])
    j "그런데 회사 밖에서도 계속 팀장님이면, 내가 자꾸 밥값 결재해야 할 것 같아."
    $ progression_enter("jihyun_r06.choice01")
    $ progression_checkpoint("jihyun_r06.choice01")
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
            d "호칭은 좀 더 걸릴 것 같아요. 대신 보고 싶다는 말은 안 미룰게요."
            j "좋아. 지금 그 말은 제대로 들었어."
            $ remember("jihyun_private_name", "팀장님")
    j "둘이 있을 땐 도현아. 회사에선 도현 씨. 헷갈리면 벌금."
    d "벌금은 누구한테 내요?"
    "지현이 대답 대신 물잔 옆에 손가락을 톡 얹었다. 도현은 메뉴판을 내려놓았다."
    j "도현아."
    d "네."
    j "...물 좀 따라 줘."
    "도현이 물을 따르는 동안, 지현은 잔이 아니라 도현의 손을 보고 있었다."
    d "용건이 물이었어요?"
    j "아니. 그냥 불러 보고 싶었어."
    d "그럼 두 번째는 제가 듣고 싶은 걸로 불러 주세요."
    j "주문하지 마. ...그런 거 미리 정하면 나 떨린단 말이야."
    "지현은 물잔을 내려놓고 도현의 다음 말을 기다렸다. 회의실에서는 본 적 없는, 기다리는 얼굴이었다."
    j "그리고. 나한테 자꾸 물어보지 마. 회사에서 하루 종일 정하다 왔어."
    d "제가 정한 게 마음에 안 드시면요?"
    j "그땐 싫다고 해. 나 그런 말은 잘하잖아. ...그러니까 지금은 네가 해."
    d "그럼 밥 먹고 바로 안 일어날게요. 오늘은 좀 붙잡고 있을 거예요."
    j "...응. 사실 바로 일어날까 봐 커피 마실 데도 찾아 놨어."
    d "그걸 왜 이제 말해요. 저 방금 용기 엄청 냈는데."
    j "알아. 그래서 좋았어. ...한 번 더 해 봐."
    "주문한 음식이 나왔다. 지현은 메뉴판 밑에 둔 휴대폰을 가방에 넣었다."
    $ progression_enter("jihyun_r06.choice02")
    $ progression_checkpoint("jihyun_r06.choice02")
    menu:
        "밖에서도 손을 잡는 건 좋고, 가까이 다가올 땐 눈을 맞춰 달라고 한다.":
            d "손잡는 건 좋아요. 더 가까워질 때는 한 번 눈 맞춰 주세요."
            j "응. 지금처럼 보면 되지? ...말하고 나니까 내가 더 떨리네."
            $ remember("jihyun_affection_scope", "hand_and_check")
        "애정 표현은 조용히 둘만 있을 때 더 편하다고 말한다.":
            d "사람 많을 때보다 둘만 있을 때가 편해요. 싫어서 피하는 건 아니에요."
            j "응. 그럼 지금은 밥부터. 아까부터 네 손 보느라 젓가락을 안 들었네."
            $ remember("jihyun_affection_scope", "private_place")
        "그때마다 편한지 짧게 말하며 속도를 맞추고 싶다고 한다.":
            d "괜찮을 때도 제가 말해 볼게요. 마음 바뀌면 그것도 말하고요."
            j "그럼 지금 하나 물을게. 밥 먹고 카페에서는 옆에 앉아도 돼?"
            d "네. 그건 좋아요."
            j "응. 그 자리로 봐 뒀어."
            $ remember("jihyun_affection_scope", "say_each_time")
    $ award_once("jihyun_R06", "jihyun", 6)
    $ progression_note_ending()
    return

label jihyun_r07:
    $ progression_enter("jihyun_r07")
    $ progression_checkpoint("jihyun_r07")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 R07 · 부탁해도 되는 저녁"
    $ location = "금요일 오후 · 온빛브랜딩 회의실"
    "도현은 주말 운영안의 첫 장을 띄웠다. 입구를 두 곳으로 열면 줄이 짧아진다는 계산이었다. 지현이 인력표를 보고 펜을 내려놓았다."
    j "잠깐. 두 번째 입구는 누가 봐요?"
    d "줄 길어질 때만 열고, 그때 안내 한 명을 옮기는 걸로 생각했습니다."
    j "그 한 명을 빼면 안쪽에 아무도 안 남아요. 이대로는 못 내요. 입구 하나로 잡은 안은 제가 올릴게요."
    d "그럼 제 안은 끝까지 안 들으시는 거예요?"
    "지현이 화면에서 눈을 뗐다. 회의실이 조용해졌다."
    j "지금 듣고 있어요. 그 한 명이 어디서 오는지, 그걸 묻는 거예요."
    "도현은 다음 장을 띄우려던 손을 내렸다. 거기엔 줄이 얼마나 짧아지는지만 적혀 있었다."
    $ location = "토요일 저녁 · 지현의 집"
    "저녁을 먹고 지현이 집에 두고 온 작은 조립품을 보러 갔다. 지현은 평소 입던 사복 그대로 찻잔 두 개를 꺼냈다."
    "지현이 작은 집을 돌려 보여 줬다. 도현이 들여다보려고 몸을 기울이자 손으로 탁자 모서리를 가린다."
    j "머리 조심. 집은 작은데 탁자는 진짜라서."
    d "[memory['jihyun_private_name']], 여기 창틀은 일부러 비뚤게 하셨어요?"
    j "...아니. 똑바로 했다고 생각했는데."
    "지현이 조립품을 돌려 봤다. 도현이 기울여 보던 고개를 바로 세우자 창틀도 반듯해졌다."
    d "제 쪽이 비뚤었네요. 죄송해요."
    j "벌써 뜯을 뻔했잖아. 반듯하게 보고 칭찬 한번 해 줘."
    d "잘 만드셨어요. 그런데 저는 이거 보여 주실 때가 더 좋은데요. 좋아하는 거 설명하시는 얼굴이요."
    j "...그건 고개 똑바로 하고 말한 거지?"
    "도현이 고개를 끄덕였다. 지현은 조립품을 옆으로 옮기고 도현과 마주 앉았다."
    d "어제 회의 끝나고는 오늘 약속 취소하실 줄 알았어요."
    j "나도 네가 안 올 줄 알았어. 그 안은 다시 봐도 반대야."
    d "그럼 오늘은 왜 부르셨어요?"
    j "보고 싶어서. 그렇게 싸워 놓고도."
    "도현의 휴대폰이 울렸다. 회의방에 수정본이 올라왔다는 알림이었다. 도현이 반사적으로 화면을 켜자 지현도 제목을 봤다."
    j "열어도 돼. 나도 어제 그 표 세 번 열어 봤으니까."
    d "지금 보면 또 어디가 틀렸나부터 찾을 것 같아요."
    "도현이 알림을 지우고 휴대폰을 뒤집었다. 지현도 자기 휴대폰을 도현 것 옆에 엎었다."
    j "월요일엔 봐. 오늘 네가 여기 온 걸로 그 안이 맞아지는 건 아니니까."
    d "알아요. 저도 아직 제가 맞는 부분은 있다고 생각해요."
    "지현은 그제야 등을 소파에 기댔다. 도현에게 내밀려고 들었던 찻잔을 자기 쪽으로 가져가 한 모금 마셨다."
    "도현이 찻잔을 내려놓고 일어나자 지현이 고개를 들었다."
    j "가려고?"
    d "옆에 앉으려고요. 괜찮아요?"
    "지현은 소파에 놓아 둔 방석을 자기 뒤로 뺐다. 도현이 앉고 나서야 다시 입을 열었다."
    j "오늘은 여기서 같이 밤을 보내고 싶어. 도현아, 너는 어때?"
    call jihyun_private_evening("r07", "casual")
    $ award_once("jihyun_R07", "jihyun", 0)
    $ progression_note_ending()
    return

label jihyun_private_evening(slot, outfit):
    $ progression_enter("jihyun_private_evening.choice01." + slot)
    $ progression_checkpoint("jihyun_private_evening.choice01." + slot)
    menu:
        "나도 같이 밤을 보내고 싶다고 답한다 — 친밀한 장면으로 이어짐.":
            d "저도요. 오늘은 조금 더 같이 있고 싶어요."
            if slot == "r07":
                j "그럼 하나만 물을게. 키스해도 돼?"
                d "네."
                "입술이 떨어지자 지현이 도현의 셔츠 깃을 펴 줬다. 손은 거기에 잠깐 더 남았다."
                j "이건 내가 구긴 거야?"
                d "여기 올 땐 멀쩡했는데요."
                j "그래? 그럼 다시 펴 줄 필요는 없겠네."
            else:
                j "응. 서두르지 말자. 나도 원하는 건 말할게."
            call event_sequence("jihyun_" + slot, outfit)
            if not event_main_reached:
                "(장면 생략 · 시간이 흐릅니다.)"
            $ remember("jihyun_" + slot + "_pace", "shared")
            if slot == "r07":
                j "다음엔 그냥 보고 싶다고 하고 부를게. 오늘도 그렇게 말할걸."
                d "네. 저도 그 말 들으면 좋아요."
            elif slot == "r12":
                j "아까 소매만 만지고 있던 건 잊어 줘. 이제 그 말 충분히 들었어."
                d "안 잊을래요. 칭찬 기다리셨다는 것도 알아뒀고요."
                j "...그런 건 기억 잘하네."
            else:
                j "아까 같이 있고 싶다고 했을 때, 대답 정말 기다렸어."
                d "저도 돌아갈 생각 안 하고 있었어요. 말로는 조금 늦게 했네요."
        "오늘은 귀가하고, 다음 만남도 기대한다고 말한다.":
            d "오늘은 집에 가서 쉴래요. 또 보고 싶은 건 그대로예요."
            j "알겠어. 문 앞까지 같이 가. 다음 약속도 거기서 정하고."
            "현관에서 인사를 나누고 도현은 집으로 돌아갔다."
            $ remember("jihyun_" + slot + "_pace", "deferred")
        "마음을 조금 더 나눈 뒤 오늘은 각자 쉬자고 한다.":
            d "같이 있고 싶은 건 맞아요. 오늘은 그 얘기만 조금 더 하고 갈게요."
            j "응. 긴장한 것도 말해. 나도 오늘은 무슨 말 할지 계속 재고 있었어."
            if slot == "r07":
                d "수요일에 물 따라 달라고 하셨을 때요. 또 이름 불러 주실까 봐 기다렸어요."
                j "그럼 그때 더 불러 볼걸. 나는 너무 좋아하는 티 낼까 봐 참았는데."
                d "이미 들켰어요."
                j "네가 기다린 것도 지금 들켰고. ...도현아."
                "도현이 대답하자 지현은 이번엔 다른 용건을 찾지 않고 웃었다."
            elif slot == "r12":
                j "옷 고르면서는 칭찬 한번 듣고 싶다고 생각했어. 내가 부탁하게 될 줄은 몰랐지만."
                d "다음에도 부탁하셔도 돼요. 제가 알아서 말할 날도 있을 거고요."
                "지현이 소매에서 손을 놓고 웃었다. 도현도 돌아가기 전에 그 얼굴을 한 번 더 봤다."
            else:
                j "다음 산책길 후보는 두 군데야. 아직 정한 건 아니고."
                d "그럼 둘 다 보여 주세요. 하나는 제가 정할게요. 나머진 다음 산책 때 가고요."
                j "좋아. 두 번 만날 핑계가 생겼네."
            "도현은 늦지 않게 귀가했다."
            $ remember("jihyun_" + slot + "_pace", "talk")
    $ progression_note_ending()
    return

label jihyun_r08:
    $ progression_enter("jihyun_r08")
    $ progression_checkpoint("jihyun_r08")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 R08 · 평소처럼, 조금 다르게"
    if memory.get("jihyun_r07_pace") == "shared":
        $ location = "일요일 아침 · 지현의 집"
        "지현이 빵을 굽는 동안 도현은 접시 두 개를 꺼냈다. 잼 병을 보자마자 자기 쪽으로 당겼다."
        d "저는 잼 넉넉하게요."
        j "나는 끝에 조금만. 너무 달면 빵 맛이 안 나잖아."
        d "그럼 제 건 제가 바를게요. 빵 맛은 다음 조각에서 찾고요~"
        "각자 빵에 잼을 발랐다. 도현의 빵을 보던 지현이 자기 것에도 잼을 더 얹었다."
        d "빵 맛 안 난다면서요."
        j "...네 건 맛있어 보여서."
        "아침을 마치고 도현은 자기 집으로 돌아갔다."
        $ remember("jihyun_r08_shared_morning")
    $ location = "월요일 오후 · 온빛브랜딩 회의실"
    "현장팀이 보내 온 지난 행사 근무표가 회의 자료에 붙었다. 도현은 입구를 본 직원과 장비를 들인 직원 이름이 같은 걸 알아봤다."
    dn "내 안은 이 사람을 두 번째 입구로 보내고, 팀장님 안은 첫 번째 입구에 남긴다. 그런데 둘 다 그 시간에 이 사람이 장비를 옮겨야 한다는 걸 빼먹었다."
    "수요일 검토 안건에는 지현이 올린 안 하나만 남아 있었다. 도현은 현장팀에 장비가 몇 시에 들어오는지 물어봤다. 사적인 메시지는 퇴근 후 따로 왔다."
    $ location = "같은 월요일 퇴근 후 · 개인 메시지"
    if memory.get("jihyun_r07_pace") == "shared":
        call phone_deliver("jihyun_r08_memory", "jihyun", "잼은 찬장에 넣었어. 네가 바른 만큼 따라 발랐다가 너무 달아서 빵 한 장 더 먹었네.", contact="jihyun")
    elif memory.get("jihyun_r07_pace") == "talk":
        call phone_deliver("jihyun_r08_memory", "jihyun", "토요일에 내가 이름 불렀을 때 바로 돌아봤잖아. 그거 또 생각났어. 이번엔 물 달라는 거 아니고.", contact="jihyun")
    else:
        call phone_deliver("jihyun_r08_memory", "jihyun", "창틀은 그대로 뒀어. 오늘 다시 봐도 반듯해 :) 집에선 잘 쉬었어?", contact="jihyun")
    call phone_deliver("jihyun_r08_request", "jihyun", "수요일 저녁에 밥 먹자. 이번엔 일 얘기 빼고. 일곱 시 괜찮아?", contact="jihyun", important=True)
    $ phone_context = "jihyun_r08_reply"
    $ progression_enter("jihyun_r08.choice01")
    $ progression_checkpoint("jihyun_r08.choice01")
    call screen office_phone(replies=[("restaurant", "좋다고 답하고 조용한 식당을 내가 찾아보겠다고 한다."), ("menu", "좋다고 답하고 지현이 먹고 싶은 메뉴를 묻는다."), ("affection", "좋다고 답하고 나도 보고 싶었다고 먼저 표현한다.")])
    $ remember("jihyun_r08_reply", _return)
    $ phone_context = None
    if memory["jihyun_r08_reply"] == "restaurant":
        call phone_deliver("jihyun_r08_reply", "dohyun", "좋아요. 조용한 식당 제가 찾아볼게요. 일곱 시에 봐요.", contact="jihyun")
        call phone_deliver("jihyun_r08_confirm", "jihyun", "좋아. 이번엔 간판 큰 데로 부탁해. 네 냅킨 카페만큼 클 필요는 없고~ 수요일 일곱 시!", contact="jihyun")
    elif memory["jihyun_r08_reply"] == "menu":
        call phone_deliver("jihyun_r08_reply", "dohyun", "일곱 시 돼요. 오늘은 지현 씨가 고르실래요? 뭐 당기세요?", contact="jihyun")
        call phone_deliver("jihyun_r08_confirm", "jihyun", "국수. 뜨거운 국물 있는 걸로. 수요일에 봐.", contact="jihyun")
    else:
        call phone_deliver("jihyun_r08_reply", "dohyun", "저도 보고 싶었어요. 일곱 시에 봬요. 이번에는 제가 먼저 손 내밀게요.", contact="jihyun")
        call phone_deliver("jihyun_r08_confirm", "jihyun", "응. 그 말 읽으니까 수요일이 좀 멀게 느껴지네. 일곱 시에 기다릴게.", contact="jihyun", important=True)
    $ remember("jihyun_r09_appointment", "수요일 저녁 일곱 시 식사")
    $ award_once("jihyun_R08", "jihyun", 4)
    $ progression_note_ending()
    return

label jihyun_r09:
    $ progression_enter("jihyun_r09")
    $ progression_checkpoint("jihyun_r09")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 R09 · 판단을 바꾸는 책임"
    $ location = "지난 금요일 밤 · 피칭 리허설 뒤 TF 회식"
    "피칭 리허설이 끝난 금요일 밤, TF는 회사 앞 고깃집에 모였다. 지현은 늘 그렇듯 문 옆 자리에 앉았고, 하필 그 옆만 비어 있었다."
    r "팀장님 옆자리는 원래 아무도 안 앉는데~ 도현 씨 용감하다."
    j "자리 남는 데 앉은 거야. 괜히 의미 붙이지 마."
    s "의미는 원래 붙이는 사람 마음이지~"
    "지현이 잔을 들다가 도현 쪽으로 물수건을 밀었다. 아무도 못 봤을 거라고 생각한 순간, 리아와 눈이 마주쳤다."
    r "...팀장님, 저도 물수건 주세요."
    j "네 앞에 있잖아."
    r "아, 그러네요. 제 앞에 있네요~"
    "리아는 웃으며 물수건을 집었지만, 그 뒤로도 몇 번이나 도현 쪽을 힐끔거렸다. 그 눈빛이 장난만은 아니라는 걸, 도현은 조금 늦게 알아챘다."
    call phone_deliver("jihyun_r09_dinner", "jihyun", "물수건은 내 실수. 리아 눈치 빠른 거 깜빡했어. ...근데 옆에 앉아 줘서 좋았어.", contact="jihyun")
    $ cream_focus = "jihyun"
    $ location = "수요일 오후 · 검토 회의 직전"
    "검토까지 이십 분. 현장팀에서 장비가 들어오는 시각을 확인해 줬다. 도현은 자기 안과 지현의 안을 다시 펼쳤다. 두 장 모두 같은 시간에 같은 사람을 다른 곳에 세우고 있었다."
    "회의방에 메시지가 올라왔다. 주말 스태프가 오늘 안으로 출근 시각을 받아야 한다고 했다. 회의가 끝나면 방금 본 표가 그대로 나갈 참이었다."
    "지현은 회의실 앞에서 자신이 올린 자료를 열고 있었다. 도현을 보고 옆자리 의자를 조금 빼 줬다. 주말에 소파 자리를 내어 주던 때와 같은 손이었다."
    $ progression_enter("jihyun_r09.choice01")
    $ progression_checkpoint("jihyun_r09.choice01")
    menu:
        "지현에게 먼저 근무표를 보여 주고 같이 고친다.":
            d "팀장님, 잠깐만요. 이 직원, 그 시간에 입구에 못 서요. 장비 받으러 뒤에 가 있어야 해요."
            j "…네 안에도 같은 이름이네."
            d "네. 그래서 두 장 다 가져왔어요."
            "지현이 회의실 문을 닫았다. 두 사람은 장비 반입이 끝난 뒤 입구 한 곳만 열기로 했다. 회의에서 지현이 자기 표의 빈칸을 짚고, 도현이 근무표를 띄웠다."
            $ remember("jihyun_r09_support", "evidence")
        "내 안의 오류부터 회의에서 공개하고 지현의 안도 다시 보자고 한다.":
            "지현이 첫 장을 띄우자 도현이 손을 들었다."
            d "제 안부터 철회하겠습니다. 장비 받는 사람을 입구에도 넣었어요. 팀장님 안에도 같은 문제가 있습니다."
            "지현이 넘기려던 화면을 멈췄다. 잠깐 도현을 본 뒤 근무표를 띄워 달라고 했다. 두 사람은 회의에서 개장 시각을 늦췄다."
            $ remember("jihyun_r09_support", "share")
        "현장 담당자에게 반입 순서를 직접 설명해 달라고 부탁한다.":
            "도현은 회의에 온 현장 담당자 옆에 근무표를 놓고, 입구를 열기 전에 누가 어디에 있는지 설명해 줄 수 있냐고 물었다."
            "담당자가 장비가 들어오는 통로를 짚자 지현은 도면을 돌려 봤다. 자기 안의 개장 시각부터 지웠다."
            $ remember("jihyun_r09_support", "reader")
    j "설치 시간을 내가 빠뜨렸어요. 개장 늦추는 이유는 제가 전달할게요."
    $ location = "같은 수요일 저녁 일곱 시 · 식당"
    if memory.get("jihyun_r09_support") == "evidence":
        j "아까 왜 바로 내 자리로 왔어? 회의에서 말해도 네가 맞았는데."
        d "제 안도 틀렸잖아요. 누가 맞는지 따지기 전에 열 수 있는 안을 만들고 싶었어요."
        j "그래. 다음에도 들고 와. 내 표부터 보게."
    elif memory.get("jihyun_r09_support") == "share":
        "지현은 앉자마자 휴대폰을 엎었다. 도현이 따라 하려는데 먼저 입을 열었다."
        j "아까 사람들 앞에서 네가 손 들었을 때, 솔직히 기분 나빴어. 회의 전에 한마디 할 수도 있었잖아."
        d "미리 말하면 제가 또 그냥 넘어갈까 봐 겁났어요. 금요일엔 제 안도 제대로 설명 못 했으니까."
        j "그때 내가 네 말 잘랐지. 다음엔 내가 끝까지 들을게. 너도 사람들 앞에서 말하기 전에 한 번만 나 불러."
        d "네. 그래도 회의에서 말할 게 있으면 말할 거예요."
        j "그건 해. 둘이 만나는 것 때문에 일에서 눈치 보면, 나도 너 만나기 힘들어."
    else:
        j "현장팀이 통로 짚고 나서야 내 표가 이상한 게 보이더라. 넌 언제 알아봤어?"
        d "월요일에요. 오늘 실제 시각 듣기 전까진 저도 표만 보고 있었고요."
        j "그분한테 물어본 거 잘했어. 나도 다음엔 그래야겠다."
    d "틀린 거 바로 인정하시는 거 좋았어요. 멋있다고 생각했고요."
    j "같이 일하는 사람으로도, 만나고 있는 사람으로도?"
    d "네. 두 쪽 다요. 지금은 밥 먹다 자꾸 보게 되는 쪽이 더 크네요."
    j "...그렇게 말하면 나도 평소처럼 먹기는 어렵지."
    "지현이 젓가락으로 집은 면을 그릇에 도로 내려놓았다. 도현도 뒤늦게 자기 그릇으로 눈을 돌렸다."
    d "그럼 일단 세 입은 먹고요."
    j "그런 규칙은 처음 듣네."
    d "저도 지금 만들었어요. 배고픈데 자꾸 딴 데 보게 돼서."
    "두 입째에 지현이 웃었다. 도현이 젓가락을 멈추자 손가락 세 개를 펴 보였다."
    j "아직 한 입 남았어. 네가 정했잖아~"
    "도현이 마지막 한 입을 먹고 고개를 들었다. 지현은 이번엔 피하지 않았다."
    j "됐어. 나도 먹는 동안 기다렸거든."
    "도현이 대답 대신 물을 한 모금 마셨다. 지현이 메뉴판을 치우고 그릇을 조금 당겼다."
    "저녁을 먹고 각자의 집으로 향했다. 토요일에는 지현의 취미와 도현의 노트를 같이 보기로 했다."
    $ award_once("jihyun_R09", "jihyun", 6)
    $ progression_note_ending()
    return

label jihyun_r10:
    $ progression_enter("jihyun_r10")
    $ progression_checkpoint("jihyun_r10")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 R10 · 천천히 만드는 취미"
    $ location = "토요일 오후 · 지현의 집"
    "지현은 조립 중인 작은 집을 탁자에 놓았다. 창틀 옆에는 아직 붙이지 않은 지붕이 있었다."
    j "지붕은 아직. 그 전에 문손잡이 붙이려고."
    "도현이 핀셋으로 집은 부품이 두 번 미끄러졌다. 세 번째에 지현이 손바닥을 아래에 받쳤다."
    d "지금 제 실력 못 믿으시는 거죠?"
    j "응. 바닥에서 찾는 실력은 내 것도 못 믿고."
    "부품이 다시 떨어져 지현의 손바닥에 앉았다. 도현은 핀셋을 내려놓고 두 손을 들었다."
    d "정확한 판단이셨네요."
    j "이번엔 내가 집을게. 집은 네가 잡아 줘."
    "도현이 작은 집을 잡았다. 지현이 손잡이를 붙이고 한 발 물러나자 도현도 손을 뗐다."
    d "문은 안 열리네요?"
    j "모형이잖아."
    d "손잡이까지 붙였는데 손님은 못 받는 집이네요."
    "지현이 웃다가 도현의 손가락에 붙은 작은 종이 조각을 떼 줬다."
    j "한 명은 이미 와 있는데. 오늘은 차까지 마시고 가."
    "손을 정리한 뒤 도현이 기록집 노트를 펼쳤다. 지현은 작은 집을 둘 다 보이는 곳에 두고 가까이 앉았다."
    j "오늘은 하나만 보여 줘. 보고 나서 차 마저 마시자."
    $ progression_enter("jihyun_r10.choice01")
    $ progression_checkpoint("jihyun_r10.choice01")
    menu:
        "저녁 빛이 길게 드는 계단 사진을 남기고 싶다고 한다.":
            d "이 계단이요. 빛이 한 칸만 더 남아서 돌아가 찍었어요."
            "지현은 밝은 칸 아래의 어두운 계단을 짚었다."
            j "여긴 안 잘랐으면 좋겠어. 어두운 칸 지나서 사진 밖까지 걸어갈 것 같아."
            d "자르려고 했는데. 오늘은 핀셋보다 어려운 걸 맡기시네요."
            j "정하는 건 네가 해. 난 여기 좋다고만 할게."
            $ remember("jihyun_booklet_subject", "저녁 계단 사진")
            $ remember("jihyun_booklet_impression", "어두운 마지막 칸이 바깥으로 이어지는 느낌")
        "골목 빵집 문 닫는 소리에 관한 짧은 글을 남긴다.":
            d "빵집 문 닫는 소리 들으면 저도 집 갈 시간이구나 싶어서요."
            j "이 뒤엔 집까지 얼마나 걸려?"
            d "십 분쯤요. 빵 얘기부터 하실 줄 알았는데."
            j "빵집은 닫혔잖아. 난 그다음 네가 어디로 갔는지 궁금한데."
            d "그 얘기는 차 마시면서요. 글로 쓰기 전에 말로 해 드릴게요."
            $ remember("jihyun_booklet_subject", "빵집 문 닫는 소리에 관한 글")
            $ remember("jihyun_booklet_impression", "문 닫힌 뒤 집으로 걸어가는 시간")
        "사진 옆에 여백을 남겨 독자가 잠깐 쉬게 하고 싶다고 한다.":
            d "여긴 비워 두려고요. 잠깐 쉬는 칸이에요."
            "지현이 빈칸에 손을 얹었다가 사진을 한 번 더 봤다. 작은 집의 남은 지붕으로 시선이 옮겨 갔다."
            j "그럼 내 지붕도 오늘은 쉬는 걸로."
            d "안 붙이실 핑계 찾으신 거죠?"
            j "응. 오늘은 차 식기 전에 마시고 싶어."
            $ remember("jihyun_booklet_subject", "사진 옆 쉬어 가는 여백")
            $ remember("jihyun_booklet_impression", "손을 얹고 한 번 더 보고 싶은 빈칸")
    "도현이 감상을 적고 노트를 당겼다. 지현이 손을 거두는 건 조금 늦었다."
    d "다 보셨어요?"
    j "응. ...조금만 더 둬도 되는데. 차 마시면서도 보게."
    "도현은 다른 후보를 볼 때도 노트를 둘 사이에 펼쳐 뒀다."
    $ remember("jihyun_booklet_state", "함께 읽은 초안, 최종 구성은 도현이 선택 예정")
    $ progression_enter("jihyun_r10.choice02")
    $ progression_checkpoint("jihyun_r10.choice02")
    menu:
        "둘이 합의해서 리아에게 교제 사실만 짧게 알리자고 한다.":
            d "리아 씨에게만 저희 만나는 건 말씀드릴까요? 둘이 괜찮다면요."
            j "응. 만난다는 것만. 사적인 얘기는 우리한테 남겨 두자. 내일 같이 보내자."
            $ remember("jihyun_publicity", "agreed_ria")
        "교제 사실은 당분간 둘만 알고 싶다고 한다.":
            d "지금은 둘만 아는 게 좋아요. 마음 바뀌면 말씀드릴게요."
            j "응. 오늘 안 알린다고 계속 숨기기로 한 건 아니야. 그것만 알아 둬."
            $ remember("jihyun_publicity", "private")
        "공개할 때 알려 줄 범위만 정하고 시점은 나중에 정한다.":
            d "나중에 말하면 만난다는 것만요. 언제인지는 더 생각할래요."
            j "좋아. 날짜는 둘이 정할 때까지 안 잡을게."
            $ remember("jihyun_publicity", "discuss_later")
    $ award_once("jihyun_R10", "jihyun", 4)
    $ progression_note_ending()
    return

label jihyun_r10_after:
    $ progression_enter("jihyun_r10_after")
    $ progression_checkpoint("jihyun_r10_after")
    if not dating or active_route != "jihyun" or "jihyun_R10" not in completed:
        $ progression_note_ending()
        return
    $ location = "같은 토요일 밤 · 지현의 집 — 지현 시점"
    "도현이 돌아간 뒤, 지현은 조립품 옆에 노트를 두던 자리를 한 번 보았다."
    jn "노트는 조금 더 두라고 했지. ...그냥 네가 조금 더 있었으면 좋겠다고 할걸."
    "지현은 다음 날 약속 메시지에 ‘노트 없어도 와’를 덧붙여 보냈다."
    call phone_deliver("jihyun_r10_after", "jihyun", "내일은 노트 없어도 와. 같이 놀고 싶어서 부르는 거야~", contact="jihyun")
    $ remember("jihyun_r10_after_completed")
    $ progression_note_ending()
    return

label jihyun_r11:
    $ progression_enter("jihyun_r11")
    $ progression_checkpoint("jihyun_r11")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 R11 · 결정하지 않는 시간"
    $ location = "일요일 저녁 · 지현의 집"
    if memory.get("jihyun_publicity") == "agreed_ria":
        d "어제 정한 대로, 같이 있는 지금 보낼까요?"
        j "응. 나도 옆에서 볼게."
        call phone_deliver("jihyun_r11_disclose", "dohyun", "리아 씨, 저 지현 씨랑 사귀어요. 지금 둘이 같이 보내는 거예요. 다른 분들한텐 저희가 직접 말할게요.", contact="ria")
        call phone_deliver("jihyun_r11_congrats", "ria", "와... 진짜요? 축하해요!! 팀장님이 메시지에 웃는 표시 붙이는 날이 오다니. 다른 데 말 안 할게요. 근데 도현 씨, 나중에 커피 한 잔 사요. 저 좀 서운하거든요~", contact="ria")
        $ remember("jihyun_publicity", "told_ria")
        $ remember("jihyun_disclosure_delivered")
    "저녁을 먹고 지현이 작은 카드 상자를 꺼냈다. 빵과 차 그림을 모으는 가벼운 게임이었다."
    "지현이 카드 뒷면을 맞춰 쌓았다. 도현이 빵 카드를 집자 그 밑에 숨은 차 카드까지 같이 따라왔다."
    j "두 장 가져가면 안 돼."
    d "붙어 있던 건데요. 벌써 경계하시네요."
    j "처음이라도 손은 봐야지. 룰은 알려 줄게. 이기는 법까지는 말고."
    $ progression_enter("jihyun_r11.choice01")
    $ progression_checkpoint("jihyun_r11.choice01")
    menu:
        "진지하게 한 판 겨뤄 보자고 한다.":
            d "봐주시면 바로 알 거예요. 저도 이기러 왔어요."
            "도현이 같은 빵 세 장을 모으자 지현의 손이 마지막 차 카드 위에서 멈췄다. 도현이 웃자 지현은 곧 그 카드를 가져갔다."
            j "좋아하기엔 아직 한 장 남았어."
            "점수를 세니 지현이 한 점 앞섰다. 도현은 자기가 모은 빵을 뒤집어 보다가 다시 내려놨다."
            d "빵집은 제가 더 큰데요."
            j "차가 없잖아. 손님들 목마르겠네."
            "지현은 이긴 카드를 정리하면서도 순서가 보이게 천천히 모았다."
            d "다음엔 그 차부터 가져갈 거예요."
            j "...지금 알려 주면 내가 피하지."
            d "한 번쯤 놀라시는 얼굴도 보고 싶어서요."
            "지현이 가지런한 카드 묶음을 다시 섞었다."
            j "다음엔 보고도 이겨 봐. 한 점 차이였으니까."
            $ remember("jihyun_game_mode", "competitive")
            $ remember("jihyun_game_result", "지현이 한 점 차이로 이긴 대결")
        "같은 편으로 목표 그림을 모으는 협동 한 판을 고른다.":
            d "이번에는 같은 편으로요. 제가 빵 모으면 차 부탁드려요."
            "도현이 빵을 내려놓자 지현이 손에 든 차 카드를 뒤집었다. 필요한 그림이 마지막 장에서 다 모였다."
            d "방금 제 빵 보고 바꾸셨죠?"
            j "응. 네가 빵 카드를 내길래 차로 맞췄어."
            d "잘했다고 해 주실 줄 알았는데, 손부터 읽혔네요."
            j "잘했어. ...내가 맞춰 준 것도 잘했고."
            "도현이 자기 빵 카드 옆에 지현의 차를 붙였다."
            d "그럼 오늘 잘한 사람은 둘이네요."
            j "응. 내 칭찬까지 셀프로 할 뻔했네."
            $ remember("jihyun_game_mode", "cooperative")
            $ remember("jihyun_game_result", "마지막 차례에 목표를 채운 협동")
        "점수 없이 그림으로 내일 먹고 싶은 조합을 만들어 본다.":
            d "저는 빵 두 개랑 차요. 이건 점수보다 내일 아침이 생각나네요."
            j "내 조합엔 잼도 있어. 빵만 두 개면 조금 섭섭하지."
            "도현이 잼 카드를 빵 위에 얹었다. 지현은 도로 자기 쪽으로 당겼다."
            j "그건 내 아침이야."
            d "그림도 안 나눠 주세요?"
            j "딸기잼은 안 돼. 살구면 생각해 볼게."
            "도현이 살구 카드를 찾아 같은 빵 사이에 놓았다. 지현은 그제야 손을 뗐다."
            d "게임보다 아침 협상이 어렵네요."
            j "내일 진짜 먹을 수도 있잖아. 그림일 때 정해 둬야지~"
            "카드로 만든 두 아침을 나란히 놓았다. 점수는 세지 않았다."
            $ remember("jihyun_game_mode", "picture_talk")
            $ remember("jihyun_game_result", "점수 없이 빵·차·잼 조합을 나눈 놀이")
    j "다음 주는 외부 보고 때문에 목요일 저녁까진 좀 엇갈리겠어. 금요일 일곱 시는 비워 둘 수 있는데."
    if memory.get("jihyun_game_mode") == "competitive":
        d "금요일 좋아요. 오늘 카드 순서는 사진 찍어 둘래요. 다음에 준비해 오시기 전에 저도 좀 보고요."
        j "공부까지 해 오려고? ...그럼 다음엔 나도 그렇게 쉽게 읽히면 안 되겠네."
    elif memory.get("jihyun_game_mode") == "cooperative":
        d "금요일 좋아요. 오늘 맞춘 빵이랑 차는 사진으로 남겨 둘래요. 마지막에 딱 맞았잖아요."
        j "다음엔 내가 빵 고를게. 네가 차 맞춰 줘."
    else:
        d "금요일 좋아요. 오늘 고른 아침 사진 찍어 둘래요. 내일은 진짜로 이 조합 먹어 볼까 봐요."
        j "잼은 사 놓은 걸로 골라. 카드에서만 찾으면 아침 굶겠네~"
    "도현이 휴대폰을 들자 지현이 카드를 다시 펼쳤다. 자기 몫의 잼 그림은 맨 앞에 뒀다."
    $ remember("jihyun_reunion_plan", "다음 금요일 저녁 일곱 시")
    $ award_once("jihyun_R11", "jihyun", 0)
    $ progression_note_ending()
    return

label jihyun_r12:
    $ progression_enter("jihyun_r12")
    $ progression_checkpoint("jihyun_r12")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 R12 · 일정표에 남긴 자리"
    $ location = "수요일 밤 · 외부 보고 출장, 숙소 복도"
    "외부 보고 출장에 도현도 자료 담당으로 따라갔다. 보고가 늦게 끝나 숙소에 도착하니 열한 시가 넘어 있었다."
    "방은 따로였다. 복도 끝 자판기 앞에서, 지현이 캔커피 두 개를 들고 서 있었다."
    j "보고 잘했어. 이건 팀장으로 하는 말."
    d "그럼 지금은요?"
    j "...지금은 퇴근했어. 그래도 복도라서 손은 못 잡아. 누가 나올지 몰라."
    "그렇게 말하면서도 지현은 캔을 건넨 손을 바로 거두지 않았다. 손끝이 잠깐 겹쳤다."
    "엘리베이터가 띵 하고 열렸다. 둘은 동시에 한 걸음씩 물러났다. 내린 건 처음 보는 투숙객이었다."
    j "...심장에 안 좋네, 이거."
    d "방 번호는 안 물어볼게요."
    j "물어봐도 안 알려 줘. 금요일에 보자. 그땐 복도 말고."
    $ location = "금요일 저녁 일곱 시 · 약속한 식당"
    "출장에서 돌아오고 이틀 뒤, 약속한 금요일에 둘이 마주 앉았다. 복도에서 못 한 말이 아직 남아 있었다."
    j "위에서 회의가 길어져서 미룰까 했어. ...별일 아니야. 그래도 오늘은 보고 싶었어."
    d "저도요. 일요일에 같이 놀던 거 가끔 생각났어요."
    if memory.get("jihyun_game_mode") == "competitive":
        j "한 점 차이 얘기? 아직 재대결 신청 안 받았는데~"
    elif memory.get("jihyun_game_mode") == "cooperative":
        j "같은 편 하자는 말? 오늘도 내 쪽 자리 하나 비워 뒀어."
    else:
        j "잼은 내가 골랐다는 말? 그런 것도 기억해 주는구나."
    j "다음 주 네 발표 안, 위험한 데는 내가 추려 둘게. 일정도 덜 빡빡하게... 지금 위에서 분위기가 좀 안 좋아서."
    d "일정 바꾸는 건 제 시간도 확인해 주세요. 지금은 저녁 먹으러 온 거고요."
    j "응. 지금은 이 약속부터. 발표는 월요일에 자료 놓고 얘기해."
    $ remember("jihyun_r12_boundary_reminder")
    "식사를 마치고 지현의 집에서 차를 마셨다. 지현은 오늘을 위해 꺼낸 옷의 소매를 한 번 정리했다."
    j "오늘 너 만나려고 입은 거야. 잘했다는 말 말고."
    d "예쁘다는 말이요?"
    j "...응. 알아들었으면 그렇게 웃지만 말고."
    d "예뻐요. 들어오실 때부터 말씀드리고 싶었어요."
    "지현이 소매를 놓고 웃었다. 도현을 마주 보는 쪽이 평소보다 조금 늦었다."
    j "그럼 조금 일찍 해 주지. 나 아까부터 소매만 만지고 있었잖아."
    d "다음에는 눈 마주치면 바로 말할게요. 지금도 예뻐요."
    j "...응. 오늘도 같이 있고 싶어."
    call jihyun_private_evening("r12", "special")
    $ award_once("jihyun_R12", "jihyun", 4)
    $ progression_note_ending()
    return
