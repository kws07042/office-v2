# Established Yujin slots R05-R08. New graphics remain deferred.
label yujin_r05:
    if not dating or active_route != "yujin":
        return
    $ chapter = "유진 R05 · 둘이 고른 주말"
    $ location = "약속한 토요일 오후 · 동네 작은 서점"
    if memory.get("yujin_next_date_plan") == "dohyun_suggests":
        "도현이 먼저 제안한 작은 서점 앞에서 만났다. 유진은 창가에 놓인 얇은 책을 보고 고개를 기울인다."
        d "사진이랑 글을 같이 묶은 책을 보고 싶었어요. 오늘은 제가 고른 곳이에요."
        y "알아요. 저 지금 처음 보는 사람으로 오기로 한 약속 지키는 중이에요~"
    elif memory.get("yujin_next_date_plan") == "yujin_suggests":
        "유진이 추천한 서점의 낮은 진열대 앞에서 만났다. 도현은 들고 온 노트를 꺼냈다."
        y "종이 크기랑 넘기는 느낌을 같이 볼 수 있어서 골랐어요. 도현 씨는 어떤 게 궁금하세요?"
        d "이 작은 책이요. 사진보다 글이 먼저 보이는 게 좀 새로워서요."
    else:
        "유진이 고른 서점과 도현이 고른 가까운 공원을 오늘의 후보로 남겼다. 먼저 서점 안을 천천히 둘러본다."
        d "책 보고 나면 공원 벤치에서도 노트 펼쳐 볼까요?"
        y "좋아요. 제 후보랑 도현 씨 후보가 같은 날 들어갔네요."
    if memory.get("yujin_r02_plan") == "follow":
        y "전시 때는 제가 순서를 골랐죠. 오늘 책은 도현 씨 손이 먼저 가는 걸 보고 싶어요."
    elif memory.get("yujin_r02_plan") == "window":
        y "지난번엔 창가부터 보고 돌아왔잖아요. 오늘도 한번 넘겨 본 책은 다시 봐도 돼요~"
    elif memory.get("yujin_r02_plan") == "linger":
        y "첫 그림 앞에 오래 있었던 날 생각나요. 오늘도 한 권만 오래 봐도 좋겠어요."
    "밖으로 나와 작은 공원 벤치에 앉았다. 도현이 자기 노트를 펼치자 유진은 빈 페이지 옆에 손가락을 놓는다."
    d "사진은 골랐는데 첫 페이지가 어렵네요. 보여 주고 싶은 말이 사진 뒤로 자꾸 숨어요."
    "바람에 노트 한 장이 넘어갔다. 유진이 빈 페이지를 눌렀고, 도현은 사진 있는 쪽을 다시 펼쳤다."
    y "바람은 벌써 다음 장 골랐네요. 저희는 첫 장부터 볼까요?"
    menu:
        "사진을 먼저 보여 주고 짧은 글을 뒤에 붙이는 구성을 고른다.":
            $ remember("yujin_r05_layout", "photo_first")
            d "일단 이 풍경을 먼저 보여 주고 싶어요. 글은 그다음에요."
            "유진이 문장 쪽을 손으로 가리고 사진만 봤다."
            y "이렇게요? 저 지금 사진 다음에 무슨 말 나올지 기다리고 있어요."
            d "먼저 읽고 계신 줄 알았어요."
            y "안 봤어요! 궁금해서 손가락이 조금 벌어지긴 했지만요."
            "도현이 사진 다음 칸에 짧은 문장을 적었다. 유진은 글을 읽고 사진을 다시 본다."
        "짧은 글로 시작하고 다음 페이지에서 사진을 보여 준다.":
            $ remember("yujin_r05_layout", "text_first")
            d "저는 이 한 줄부터 들려주고 싶어요. 사진은 페이지 넘겼을 때요."
            "유진은 사진 쪽을 덮고 한 줄을 읽었다. 다음 장을 넘기자 눈썹이 조금 올라갔다."
            y "저는 왼쪽으로 꺾이는 길인 줄 알았어요. 도현 씨는 여기서 돌아보셨네요."
            d "길을 잘못 들어서요. 사진은 그때 건졌고요."
            y "그건 글에 아직 없네요~ 다음에 꼭 들려주세요."
            "도현은 유진이 상상한 골목 방향을 사진 옆에 작게 표시했다. 같은 사진 옆에 다른 길이 하나 생겼다."
        "사진과 글을 나란히 두고 시선이 오가는 구성을 시험한다.":
            $ remember("yujin_r05_layout", "spread")
            d "저는 왔다 갔다 보게 하고 싶어요. 둘 중 하나만 답처럼 남지 않게요."
            "유진이 사진과 글 사이에 손가락 하나를 세웠다가 조금 옮겼다."
            y "여기만큼 비우면 어떨까요? 지금은 둘이 서로 먼저 보라고 당기는 것 같아요."
            d "그럼 사이 좀 띄워 줄게요. 둘 다 제가 데려왔으니까."
            "도현이 빈 공간을 조금 늘린 뒤 노트를 유진 쪽으로 돌렸다. 최종 구성은 나중에 다시 보기로 했다."
    $ remember("yujin_r05_layout_status", "함께 읽어 본 구성 후보, 최종 완성 아님")
    y "나중에 바뀌면 보여 주세요. 바람 의견까지 채택하셨는지도 궁금하고요~"
    d "그럼요. 대신 다음 감상도 들려주세요. 다음 페이지는 또 다를 수 있으니까."
    y "...그 말은 다음에도 노트 들고 만나 주신다는 뜻이죠?"
    d "노트 없이도 만나고요."
    "노트를 덮은 유진이 도현을 본다. 이번에는 바로 눈을 돌리지 않았다."
    y "제가 또 먼저 여쭤볼 게 있어요. 지금 입맞춤해도 돼요?"
    menu:
        "나도 그러고 싶다고 답하고 가까이 다가간다.":
            d "네. 저도 아까부터 그러고 싶었어요."
            "유진이 가까이 와 짧게 입맞춤했다. 떨어진 뒤에는 둘 다 빈 벤치 끝을 한번 보고 웃었다."
            $ first_kiss = True
            $ remember("yujin_first_kiss", "R05")
            $ remember("yujin_r05_affection", "kiss")
            y "먼저 말하는 건 했는데... 그다음 표정은 준비를 못 했어요."
            d "저는 대답하는 표정부터 못 준비했는데요."
        "오늘은 손을 잡고 조금 더 앉아 있고 싶다고 말한다.":
            d "오늘은 손잡고 조금 더 앉아 있고 싶어요. 먼저 물어봐 주신 건 좋았어요."
            y "네. 그럼 오늘은 이쪽 손을 주실래요? 노트는 제가 들고 있을게요."
            "유진이 내민 손을 잡고 벤치에 조금 더 앉았다."
            $ remember("yujin_r05_affection", "hand")
        "입맞춤은 다음으로 두고 같이 조금 더 걷자고 한다.":
            d "그건 조금 더 천천히 하고 싶어요. 대신 저 길 끝까지 같이 걸을래요?"
            y "좋아요. 다음 얘기를 제가 먼저 꺼낸 건 기억해 주세요~"
            "유진이 노트를 돌려주고 도현과 걸음을 맞췄다."
            $ remember("yujin_r05_affection", "walk")
    $ remember("yujin_r05_kiss_proposed")
    $ award_once("yujin_R05", "yujin", 4)
    return

label yujin_r06:
    if not dating or active_route != "yujin":
        return
    $ chapter = "유진 R06 · 제가 먼저 말해도 되죠"
    $ location = "그 주 수요일 퇴근 후 · 회사 근처 카페"
    y "오늘은 제가 먼저 퇴근했어요. 약속 기다린 사람은 아직 모르겠지만요."
    d "저는 오후부터 시계 봤어요. 그쪽은요?"
    y "...그럼 제가 이겼네요. 점심 먹고 달력부터 봤는데."
    d "기다리기 시합이었어요? 다음엔 제가 먼저 말씀드릴걸~"
    if memory.get("yujin_first_kiss") == "R05":
        y "지난번엔 먼저 말해 놓고 집에 가서 생각이 더 많아졌어요. 도현 씨 표정 자꾸 생각나서요."
        d "어떤 표정이었는데요?"
        y "설명하면 저만 더 빨개질 것 같아요. 오늘은 한번 넘어가 주세요~"
    else:
        y "지난번 제가 먼저 여쭤본 거요. 다음에도 제가 하고 싶은 걸 먼저 말씀드려도 되죠?"
        d "네. 저는 제 마음으로 답할게요. 오늘도 보고 싶어서 온 거고요."
    y "다음 약속도 자꾸 먼저 생각나요. 도현 씨는 어떤 쪽이 좋아요?"
    menu:
        "유진의 제안이 좋고, 나도 먼저 부르고 싶다고 말한다.":
            $ remember("yujin_r06_expression", "both_initiate")
            d "불러 주시는 건 좋아요. 저도 보고 싶은 날엔 먼저 부를래요."
            y "그러면 이번 주엔 달력보다 메시지를 먼저 봐야겠네요. 제 차례 놓칠까 봐~"
        "좋아도 답을 고를 시간이 조금 필요할 때가 있다고 말한다.":
            $ remember("yujin_r06_expression", "think_first")
            d "저는 좋아도 대답이 늦을 때가 있어요. 무슨 말부터 할지 고르느라요."
            y "네. 그럼 잠깐 기다려 볼게요. 아까도 표정 보고 답을 먼저 정할 뻔했어요."
            d "기다리기만 하시게 두진 않을게요. 지금은 같이 있는 게 좋아요."
        "서로 한 번씩 다음 만남을 제안해 보자고 한다.":
            $ remember("yujin_r06_expression", "take_turns")
            d "다음은 유진 씨, 그다음은 저. 서로 어떤 곳을 고를지 기대해 볼까요?"
            y "좋아요. 그런데 순서 아닌 날에 보고 싶어지면요?"
            d "그건 반칙이어도 받아 줄래요."
            y "그럼 저 벌써 반칙 하나 생각났어요. 토요일에 시간 있으세요?"
    "유진이 휴대폰의 토요일 칸을 열었다가, 도현을 보고 화면을 조금 낮췄다."
    d "어느 날부터 봐 두셨어요?"
    y "토요일이요. 오후 세 시 어때요? 책 보고 저녁도 먹고 싶어서요. 작은 그림도 보여 드리고 싶고요."
    d "세 시 좋아요. 그 시간부터는 괜찮아요."
    $ remember("yujin_r07_appointment", "토요일 오후 세 시, 책을 보고 저녁을 함께 먹기로 함")
    $ location = "같은 수요일 저녁 · 카페 앞"
    y "장소까지 제가 골라도 돼요?"
    d "벌써 정해 두셨어요?"
    y "네. 도현 씨가 좋아하실지도 궁금하지만... 제가 같이 가고 싶어서요."
    d "그럼 따라갈게요."
    "유진이 작은 웃음을 삼키며 가방 끈을 고쳐 잡았다."
    y "...그렇게 바로 따라오신다고 하시면 제가 더 떨리는데요. 그래도 취소는 안 할래요~ 동네 서점 앞에서 만나요."
    d "네. 토요일 세 시에 봬요. 유진 씨가 고른 곳에서요."
    $ remember("yujin_r07_appointment", "토요일 오후 세 시, 동네 서점 앞")
    menu:
        "입맞춤해도 괜찮을지 먼저 묻는다.":
            d "오늘은 제가 먼저 물어볼래요. 입맞춤해도 돼요?"
            y "네. 오늘은 대답 먼저 할 수 있겠어요."
            "둘이 짧게 입맞춤한 뒤 유진이 도현의 소매를 살짝 잡았다."
            if not first_kiss:
                $ first_kiss = True
                $ remember("yujin_first_kiss", "R06")
            $ remember("yujin_r06_affection", "kiss")
        "손을 잡고 정류장까지 함께 걷는다.":
            d "정류장까지 손잡고 갈까요? 오늘은 조금 더 같이 가고 싶어요."
            y "좋아요. 버스 오는 쪽은 제가 볼게요."
            "유진이 손을 내밀었다. 정류장에 도착할 때까지 같은 속도로 걸었다."
            $ remember("yujin_r06_affection", "hand")
        "오늘 좋았던 말을 하나씩 나누고 인사한다.":
            if memory.get("yujin_r06_expression") == "think_first":
                d "저는 아까 대답 고를 때 기다려 주신 게 좋았어요."
            else:
                d "저는 점심부터 오늘 약속 기다리셨다는 말이요. 저보다 먼저였다니 조금 졌네요~"
            y "저는 오후부터 시계 보셨다는 말이요. 이제 저만 기다린 건 아닌 거 알아서요."
            "유진이 버스에 오르기 전에 작게 손을 흔들었다."
            $ remember("yujin_r06_affection", "words")
    $ award_once("yujin_R06", "yujin", 6)
    return

label yujin_r07:
    if not dating or active_route != "yujin":
        return
    $ chapter = "유진 R07 · 둘이 선택한 속도"
    $ location = "토요일 오후 세 시 · 동네 서점"
    "약속한 시간에 만나 책을 함께 봤다. 유진은 도현이 노트를 꺼내자 지난번 구성 후보를 먼저 알아본다."
    if memory.get("yujin_r05_layout") == "photo_first":
        y "사진 먼저 보이던 페이지죠? 이번엔 글 읽기 전에 조금 더 볼게요."
    elif memory.get("yujin_r05_layout") == "text_first":
        y "글부터 읽고 넘겨 보던 거죠. 오늘도 먼저 상상해 보고 싶어요."
    else:
        y "사진이랑 글 사이를 오가던 페이지죠? 오늘은 어디부터 눈이 갈까요~"
    "저녁을 먹은 뒤 유진의 집에 잠깐 들렀다. 유진은 작은 개인 그림 한 장을 책상에서 보여 줬다."
    $ location = "같은 토요일 저녁 · 유진의 집"
    y "이건 일로 그린 건 아니에요. 집 창가에서 보이던 그림자를 남겨 봤어요."
    d "오늘 보니 유진 씨가 전시에서 빛 얘기하던 게 좀 더 알 것 같아요."
    "노트를 덮은 뒤에도 둘은 자리를 바로 옮기지 않았다."
    y "오늘은 조금 더 가까이 있고 싶어요. 여기서 같이 밤을 보내고 싶은데... 도현 씨는요?"
    menu:
        "나도 함께 밤을 보내고 싶다고 답한다 — 친밀한 장면으로 이어짐.":
            d "저도 같은 마음이에요. 오늘은 같이 있고 싶어요."
            y "네. 그럼 오늘은 저도 조금 천천히 말할게요. 준비해 온 말 말고요."
            call event_sequence("yujin_r07", "casual")
            if not event_main_reached:
                "(거사 — 장면 생략)"
            $ remember("yujin_r07_pace", "shared")
            y "내일 아침에는 제가 먼저 커튼 열어도 돼요? 빛 보여 드리고 싶어서요."
            d "네. 저는 그때도 옆에서 같이 볼게요."
        "오늘은 집으로 돌아가고 다음에 더 함께 있고 싶다고 말한다.":
            d "오늘은 집에 가서 쉬고 싶어요. 다음에도 만나고 싶다는 건 그대로예요."
            y "네. 그럼 내일 제가 먼저 연락해도 되죠? 오늘 보여 드린 그림 얘기 조금 더 하고 싶어요."
            "현관에서 인사를 나누고 각자 쉴 시간을 가졌다."
            $ remember("yujin_r07_pace", "deferred")
        "마음을 조금 더 이야기한 뒤 오늘은 각자 쉬자고 한다.":
            d "가까워지고 싶은 마음은 같아요. 오늘은 그 얘기를 조금 더 하고 갈래요."
            y "네. 그럼 차가 식기 전까지요. 먼저 말씀해 주셔서 좋아요."
            "처음이라 긴장됐던 순간과 다음에도 함께하고 싶은 일을 나눴다. 도현은 귀가할 시각에 자리에서 일어났다."
            $ remember("yujin_r07_pace", "talk")
    $ remember("yujin_personal_drawing_seen", "집 창가의 그림자")
    $ award_once("yujin_R07", "yujin", 0)
    return

label yujin_r08:
    if not dating or active_route != "yujin":
        return
    $ chapter = "유진 R08 · 다음 약속은 제가"
    if memory.get("yujin_r07_pace") == "shared":
        $ location = "다음 날 일요일 아침 · 유진의 집"
        "유진이 커튼을 조금 열었다. 두 사람은 어제 그림에서 보았던 창가의 빛을 함께 본 뒤 아침을 먹었다."
        y "같이 보니까 또 다른 그림 같네요. 다음에는 이 자리도 그려 볼래요."
        d "다 그리시면 저도 보고 싶어요. 오늘 본 건 저도 기억하고 있을게요."
        "도현은 자기 집에서 할 일을 마치기로 하고 돌아갔다."
        $ remember("yujin_r08_morning_shared")
    $ location = "같은 일요일 오후 · 각자의 집, 개인 메시지"
    if memory.get("yujin_r07_pace") == "shared":
        call phone_deliver("yujin_r08_memory", "yujin", "아침에 커튼 열던 순간이요. 그 빛이 어제 그림 옆에 하나 더 남은 것 같아요.", contact="yujin")
    elif memory.get("yujin_r07_pace") == "talk":
        call phone_deliver("yujin_r08_memory", "yujin", "어제 차 마시면서 한 얘기, 오늘 노트에 적다가 혼자 웃었어요. 제목은 비밀이에요~", contact="yujin")
    else:
        call phone_deliver("yujin_r08_memory", "yujin", "집에서 푹 쉬셨어요? 어제 보여 드린 그림 옆에 날짜도 적어 뒀어요. 같이 본 날로요.", contact="yujin")
    if memory.get("yujin_r06_expression") == "think_first":
        call phone_deliver("yujin_r08_invite", "yujin", "다음 주 수요일에 잠깐 만날까요? 생각해 보시고 편한 시간 알려 주세요. 저는 목요일도 괜찮아요.", contact="yujin")
    else:
        call phone_deliver("yujin_r08_invite", "yujin", "이번에도 제가 먼저요~ 다음 주 수요일에 잠깐 만날까요? 저는 목요일도 괜찮아요.", contact="yujin")
    $ phone_context = "yujin_r08_reply"
    call screen office_phone(replies=[("wed19", "수요일 저녁 일곱 시가 좋다고 답한다."), ("thu19", "목요일 저녁 일곱 시를 제안한다."), ("wed1930", "수요일 일곱 시 반이 더 편하다고 말한다.")])
    $ remember("yujin_r08_availability", _return)
    $ phone_context = None
    if memory["yujin_r08_availability"] == "wed19":
        $ remember("yujin_r08_next_appointment", "수요일 저녁 일곱 시, 회사 근처 카페")
        call phone_deliver("yujin_r08_reply", "dohyun", "수요일 일곱 시 좋아요. 회사 근처 카페에서 봬요.", contact="yujin")
    elif memory["yujin_r08_availability"] == "thu19":
        $ remember("yujin_r08_next_appointment", "목요일 저녁 일곱 시, 회사 근처 카페")
        call phone_deliver("yujin_r08_reply", "dohyun", "저는 목요일 일곱 시가 더 편해요. 회사 근처 카페는 어때요?", contact="yujin")
    else:
        $ remember("yujin_r08_next_appointment", "수요일 저녁 일곱 시 반, 회사 근처 카페")
        call phone_deliver("yujin_r08_reply", "dohyun", "수요일 일곱 시 반이면 좋아요. 제 일 마무리하고 카페로 갈게요.", contact="yujin")
    call phone_deliver("yujin_r08_confirm", "yujin", "좋아요. 그날 제가 먼저 자리 볼게요. 노트는 없어도 돼요. 도현 씨만 오시면요 :)", contact="yujin", important=True)
    $ remember("yujin_r08_proposer", "yujin")
    $ location = "같은 일요일 오후 · 유진의 집 — 유진 시점"
    "유진은 확정한 약속을 달력에 적었다. 새 전시를 찾으려던 창을 닫고, 방금 받은 답장을 한 번 더 본다."
    yn "긴장되는 건 맞지만. 이번에도 내가 먼저 말하고 싶다."
    $ location = "같은 일요일 오후 · 도현의 집"
    $ cream_focus = None
    dn "정해진 시간 옆에 이름을 적었다. 이번엔 유진 씨가 먼저 고른 다음 약속이었다."
    $ remember("yujin_r08_complete")
    $ award_once("yujin_R08", "yujin", 4)
    return
