# Established Yujin slots R05-R08. New graphics remain deferred.
label yujin_r05:
    $ progression_enter("yujin_r05")
    $ progression_checkpoint("yujin_r05")
    if not dating or active_route != "yujin":
        $ progression_note_ending()
        return
    $ chapter = "유진 R05 · 둘이 고른 주말"
    $ location = "약속한 토요일 오후 · 동네 작은 서점"
    if memory.get("yujin_next_date_plan") == "dohyun_suggests":
        "도현이 가자고 한 작은 서점 앞에서 만났다. 유진은 도현이 어디부터 보는지 살피다가 웃었다."
        d "오늘은 제가 정한 데예요. 재미없으면 공원으로 도망가도 돼요."
        y "도망 안 가요. 오늘은 도현 씨가 정했으니까... 졸졸 따라다닐래요~"
    elif memory.get("yujin_next_date_plan") == "yujin_suggests":
        "유진이 추천한 서점의 낮은 진열대 앞에서 만났다. 도현을 보자 유진이 반 걸음 앞서 길을 열었다."
        y "오늘은 제가 데려왔으니까, 보고 싶은 데 하나만 말씀해 주세요."
        d "지금은 유진 씨가 어느 쪽으로 가는지요."
        y "...그러면 천천히 걸어야겠네요."
    else:
        "유진이 고른 서점과 도현이 고른 가까운 공원. 서점부터 잠깐 둘러봤다."
        d "제 후보도 잊지 마세요. 공원 벤치까지 같이 가야 해요."
        y "알아요. 오늘은 두 군데 다 도현 씨랑 가려고 정한 거니까요."
    if memory.get("yujin_r02_plan") == "follow":
        y "전시 때는 제가 순서를 정했죠. 오늘은 도현 씨가 앞장서 주세요."
    elif memory.get("yujin_r02_plan") == "window":
        y "지난번엔 창가부터 보고 돌아왔잖아요. 오늘은 제가 앞서가도 따라오실 거죠~"
    elif memory.get("yujin_r02_plan") == "linger":
        y "첫 그림 앞에 오래 있었던 날 생각나요. 오늘도 한곳에 오래 있어도 좋아요."
    "도현이 여행 사진집 앞에 멈췄다. 유진은 옆 선반에서 표지가 새빨간 요리책을 빼 들었다."
    d "색 보려고 고르셨어요?"
    y "아뇨. 떡볶이요. 맵게 만드는 쪽부터 볼래요."
    d "저는 순한 맛 생각했는데."
    y "저를요, 떡볶이를요?"
    d "...둘 다요. 한 번에 두 개 틀렸네요."
    "유진이 펼친 조리법에서 고추 표시를 짚었다. 도현이 고추 그림 세 개를 가리키고는 손가락 하나만 펴 보였다. 유진은 자기 몫은 세 개라며 손가락 세 개를 폈다."
    y "제 건 세 개요. 도현 씨 건 하나로 해도 되고요~"
    d "나눠 먹겠다는 계획부터 취소해야겠네요."
    y "디저트는 나눠 먹어요. 그건 제가 안 매운 걸로 사 드릴게요."
    "책은 제자리에 꽂았다. 밖에서 작은 구움과자 두 개를 사서 공원 벤치에 앉았다."
    $ location = "같은 토요일 오후 · 작은 공원 벤치"
    "유진이 과자 봉지를 무릎에 놓는 동안 도현은 노트를 꺼냈다."
    d "드시기 전에 이것만요. 첫 장 후보, 셋 중 하나만 봐 주세요."
    y "그럼 한 장만요. 제 과자 식기 전에~"
    $ progression_enter("yujin_r05.choice01")
    $ progression_checkpoint("yujin_r05.choice01")
    menu:
        "사진을 앞에 두고 짧은 글을 뒤에 붙이는 구성을 시험한다.":
            $ remember("yujin_r05_layout", "photo_first")
            d "이 풍경부터 보여 주고 싶어요. 글은 그다음에요."
            "유진이 문장 쪽을 손으로 가리고 사진만 봤다."
            y "이렇게요? 저 지금 사진 다음에 무슨 말 나올지 기다리고 있어요."
            d "벌써 읽고 계신 줄 알았어요."
            y "안 봤어요! ...손가락 사이로 두 글자만요."
            "도현이 아래 문장까지 보여 주자 유진은 사진으로 돌아가 한 번 더 봤다."
        "짧은 글로 시작하고 다음 페이지에서 사진을 보여 준다.":
            $ remember("yujin_r05_layout", "text_first")
            d "저는 이 한 줄부터 들려주고 싶어요. 사진은 페이지 넘겼을 때요."
            "유진은 사진 쪽을 덮고 한 줄을 읽었다. 다음 장을 넘기자 눈썹이 조금 올라갔다."
            y "저는 왼쪽으로 꺾이는 길인 줄 알았어요. 도현 씨는 여기서 돌아보셨네요."
            d "길을 잘못 들어서요. 사진은 그때 건졌고요."
            y "길 잘못 드신 얘기는 왜 빼셨어요? 저는 그게 더 궁금한데요~"
            "도현은 문장 옆에 작은 화살표를 보탰다. 유진은 이번엔 사진보다 한 줄부터 다시 읽었다."
        "사진과 글을 나란히 두고 시선이 오가는 구성을 시험한다.":
            $ remember("yujin_r05_layout", "spread")
            d "저는 같이 놓은 쪽이요. 사진 보다가 글도 보고요."
            "유진이 사진과 글 사이에 손가락을 댔다. 도현은 간격을 조금 벌렸다."
            y "이제 됐어요. 아까는 글 읽을 때 사진이 자꾸 불렀거든요."
            d "사진 편일 줄 알았는데요."
            y "오늘 틀리신 거 세 번째예요~"
            "도현은 벌린 간격을 남긴 채 노트를 닫았다."
    $ remember("yujin_r05_layout_status", "함께 읽어 본 구성 후보, 최종 완성 아님")
    "노트를 넣고 과자를 반씩 나눴다. 유진은 봉지 안에 남은 작은 끝 조각부터 집었다."
    d "그건 저 주시는 줄 알았어요."
    y "아뇨. 여기가 제일 바삭해요. 반은 드렸잖아요~"
    "도현이 제 몫을 한 입 먹자 유진이 기다렸다는 듯 봉지를 내렸다."
    y "어때요? 이건 순한 맛 맞죠?"
    d "네. 고른 분은 아직 잘 모르겠지만요."
    "유진이 웃다가 도현의 눈을 봤다. 빈 봉지를 접어 가방에 넣고도 다시 시선을 맞췄다."
    y "그럼 하나 더 알아 가실래요? ...지금 키스하고 싶어요. 괜찮으세요?"
    $ progression_enter("yujin_r05.choice02")
    $ progression_checkpoint("yujin_r05.choice02")
    menu:
        "나도 그러고 싶다고 답하고 가까이 다가간다.":
            d "네. 저도 아까부터 그러고 싶었어요."
            "유진이 가까이 와 짧게 입을 맞췄다. 떨어진 뒤에는 둘 다 빈 벤치 끝을 보며 웃었다."
            $ first_kiss = True
            $ remember("yujin_first_kiss", "R05")
            $ remember("yujin_r05_affection", "kiss")
            y "말하는 건 했는데... 그다음 표정은 준비를 못 했어요."
            d "저는 대답하는 표정부터 못 준비했는데요."
        "오늘은 손을 잡고 조금 더 앉아 있고 싶다고 말한다.":
            d "오늘은 손잡고 좀 더 앉아 있고 싶어요. 물어봐 주신 건 좋았어요."
            y "네. 그럼 오늘은 이쪽 손을 주실래요? 가방은 옆에 두시고요."
            "유진이 내민 손을 잡고 벤치에 조금 더 앉았다."
            $ remember("yujin_r05_affection", "hand")
        "키스는 다음으로 두고 같이 조금 더 걷자고 한다.":
            d "그건 좀 더 천천히 하고 싶어요. 대신 저 길 끝까지 같이 걸을래요?"
            y "좋아요. 대신 오늘 제가 먼저 말 꺼낸 건 기억해 주세요~"
            "유진이 벤치에서 일어나 도현과 걸음을 맞췄다."
            $ remember("yujin_r05_affection", "walk")
    $ remember("yujin_r05_kiss_proposed")
    $ award_once("yujin_R05", "yujin", 4)
    $ progression_note_ending()
    return

label yujin_r06:
    $ progression_enter("yujin_r06")
    $ progression_checkpoint("yujin_r06")
    if not dating or active_route != "yujin":
        $ progression_note_ending()
        return
    $ chapter = "유진 R06 · 제가 먼저 말해도 되죠"
    $ location = "그 주 수요일 퇴근 후 · 회사 근처 카페"
    y "오늘은 제가 일찍 퇴근했어요. 누가 더 기다렸는지는 아직 모르지만요."
    d "저는 오후부터 시계 봤어요. 그쪽은요?"
    y "...그럼 제가 이겼네요. 점심 먹고 달력부터 봤는데."
    d "기다리기 시합이었어요? 다음엔 제가 먼저 말할걸~"
    if memory.get("yujin_first_kiss") == "R05":
        y "지난번에 말해 놓고 집에 가서 생각이 더 많아졌어요. 도현 씨 표정이 자꾸 생각나서요."
        d "어떤 표정이었는데요?"
        y "설명하면 저만 더 빨개질 것 같아요. 오늘은 한번 넘어가 주세요~"
    else:
        y "지난번에 제가 여쭤본 거요. 다음에도 제가 하고 싶은 걸 말해도 되죠?"
        d "네. 저도 제 마음대로 대답할게요. 오늘도 보고 싶어서 온 거고요."
    "유진이 빨대로 음료를 저었다. 도현은 컵 받침에 찍힌 작은 꽃을 가리켰다."
    d "이거 해바라기 같지 않아요?"
    y "데이지 같은데요. 해바라기면 가운데가 더... 잠깐만요."
    "유진이 받침을 돌려 봤다. 도현도 고개를 같은 쪽으로 기울였다."
    y "어느 쪽으로 봐도 데이지예요. 이건 안 져 드릴래요~"
    d "저는 꽃보다 유진 씨 고개 기울이는 게 더 눈에 들어왔는데요."
    y "그럼 고개는 왜 따라 기울이셨어요?"
    "도현이 자세를 바로 하자 유진이 빨대에서 손을 뗐다."
    y "...저도 잠깐 도현 씨만 봤으니까, 이번엔 비긴 걸로 해요."
    "유진이 컵 받침을 자기 쪽으로 당겼다. 아까의 웃음이 조금 늦게 돌아온다."
    y "도현 씨는 다른 분들한테도 그렇게 말씀하세요?"
    d "어떤 말이요?"
    y "보고 싶었다는 거요. ...아, 회사에서 뵙고 싶었다는 말도 하시니까."
    d "지금은 여자친구 만나러 온 건데요. 오후부터 시계 본 것도요."
    "유진이 빨대를 놓았다. 도현은 웃으려다 유진의 다음 말을 기다렸다."
    y "알아요. 아는데도 저한테만 하는 말이 좀 있었으면 했어요."
    d "그 말은 유진 씨한테만 해요. 대신 제가 다른 사람한테 웃었다고 다 같은 뜻은 아니에요."
    "유진이 컵 받침을 도현 앞에 돌려놓았다."
    y "네. 그럼 꽃은 데이지고요. 시계 보면서 기다린 건 저 때문이고요."
    d "그 둘은 왜 같이 묶으세요?"
    y "앞에 건 바로잡고, 뒤에 건 기억해 두려고요~ 다음엔 제가 부르고 싶은데요."
    $ progression_enter("yujin_r06.choice01")
    $ progression_checkpoint("yujin_r06.choice01")
    menu:
        "유진의 제안이 좋고, 나도 보고 싶을 땐 부르고 싶다고 말한다.":
            $ remember("yujin_r06_expression", "both_initiate")
            d "불러 주시는 건 좋아요. 저도 보고 싶은 날엔 부를래요."
            y "그럼 이번 주엔 달력보다 메시지를 더 자주 봐야겠네요. 놓칠까 봐~"
        "좋아도 대답할 시간이 조금 필요할 때가 있다고 말한다.":
            $ remember("yujin_r06_expression", "think_first")
            d "저는 좋아도 대답이 늦을 때가 있어요. 무슨 말부터 할지 생각하느라요."
            y "네. 그럼 기다려 볼게요. 아까도 표정만 보고 대답을 짐작할 뻔했어요."
            d "기다리기만 하시게 두진 않을게요. 지금은 같이 있는 게 좋아요."
        "번갈아 다음 만남을 제안해 보자고 한다.":
            $ remember("yujin_r06_expression", "take_turns")
            d "다음은 유진 씨, 그다음은 저. 서로 어디 데려갈지 기대해 볼까요?"
            y "좋아요. 그런데... 제 순서 아닌 날에 보고 싶어지면요?"
            d "그건 반칙이어도 받아 줄래요."
            y "그럼 저 벌써 반칙 하나 생각났어요. 토요일에 시간 있으세요?"
    "유진이 휴대폰의 토요일 칸을 열었다가, 도현을 보고 화면을 조금 낮췄다."
    d "벌써 날짜도 봐 두셨죠?"
    y "토요일이요. 오후 세 시 어때요? 책 보고 저녁도 먹고 싶어서요. 작은 그림도... 보여 드리고 싶고요."
    d "세 시 좋아요. 그 시간부터는 괜찮아요."
    $ remember("yujin_r07_appointment", "토요일 오후 세 시, 책을 보고 저녁을 함께 먹기로 함")
    $ location = "같은 수요일 저녁 · 카페 앞"
    y "장소도 제가 정해도 돼요?"
    d "벌써 정해 두셨어요?"
    y "네. 좋아하실지도 궁금하지만... 그냥 제가 같이 가고 싶어서요."
    d "그럼 따라갈게요."
    "유진이 작은 웃음을 삼키며 가방 끈을 고쳐 잡았다."
    y "...그렇게 바로 따라오신다고 하면 제가 더 떨리는데요. 그래도 취소는 안 할래요~ 동네 서점 앞에서 만나요."
    d "네. 토요일 세 시에 봬요. 유진 씨가 정한 데서요."
    $ remember("yujin_r07_appointment", "토요일 오후 세 시, 동네 서점 앞")
    $ progression_enter("yujin_r06.choice02")
    $ progression_checkpoint("yujin_r06.choice02")
    menu:
        "키스해도 괜찮을지 묻는다.":
            d "오늘은 제가 물어볼래요. 키스해도 돼요?"
            y "네. 오늘은 대답부터 할 수 있겠어요."
            "짧게 입을 맞춘 뒤 유진이 도현의 소매를 살짝 잡았다."
            if not first_kiss:
                $ first_kiss = True
                $ remember("yujin_first_kiss", "R06")
            $ remember("yujin_r06_affection", "kiss")
        "손을 잡고 정류장까지 함께 걷는다.":
            d "정류장까지 손잡고 갈까요? 오늘은 좀 더 같이 가고 싶어요."
            y "좋아요. 버스 오는 쪽은 제가 볼게요."
            "유진이 손을 내밀었다. 정류장에 도착할 때까지 같은 속도로 걸었다."
            $ remember("yujin_r06_affection", "hand")
        "오늘 좋았던 말을 하나씩 나누고 인사한다.":
            if memory.get("yujin_r06_expression") == "think_first":
                d "저는 아까 대답 기다려 주신 게 좋았어요."
            else:
                d "저는 점심부터 기다리셨다는 말이요. 저보다 빨랐다니 좀 졌네요~"
            y "저는 오후부터 시계 보셨다는 말이요. 이제 저만 기다린 건 아닌 거 알아서요."
            "유진이 버스에 오르기 전에 작게 손을 흔들었다."
            $ remember("yujin_r06_affection", "words")
    $ award_once("yujin_R06", "yujin", 6)
    $ progression_note_ending()
    return

label yujin_r07:
    $ progression_enter("yujin_r07")
    $ progression_checkpoint("yujin_r07")
    if not dating or active_route != "yujin":
        $ progression_note_ending()
        return
    $ chapter = "유진 R07 · 둘이 선택한 속도"
    $ location = "토요일 오후 세 시 · 동네 서점"
    "약속한 시간에 만나 책을 같이 봤다. 도현이 노트를 꺼내자 유진은 지난번 구성 후보를 바로 알아봤다."
    if memory.get("yujin_r05_layout") == "photo_first":
        y "사진 먼저 보이던 페이지죠? 이번엔 글 읽기 전에 조금 더 볼게요."
    elif memory.get("yujin_r05_layout") == "text_first":
        y "글부터 읽고 넘기던 거죠. 오늘도 상상부터 해 볼래요."
    else:
        y "사진이랑 글 사이를 오가던 페이지죠? 오늘은 어디부터 눈이 갈까요~"
    "노트는 서점에서 넣고 나왔다. 저녁에는 같은 떡볶이를 순한 맛과 매운맛으로 따로 주문했다. 유진이 도현 앞에 물잔을 밀자 도현은 아직 첫입도 안 먹었다며 웃었다."
    d "물까지 주시니까 제 것도 무서울 것 같은데요."
    y "순한 걸로 시켰어요. 물은... 제 거 맛보고 싶어 하실까 봐요."
    d "표정에 써 있었어요?"
    y "아까부터 제 접시만 보셨잖아요~"
    "식당을 나와 횡단보도 앞을 지나는데 유진이 무인 사진관 문을 잡았다. 도현은 유진이 안쪽을 구경하고 나올 줄 알았다. 유진은 이미 두 사람 몫을 결제하고 있었다."
    y "저랑 찍어요. 사진 잘 나오는 표정 말고, 아까 제 접시 볼 때 하신 표정으로요."
    d "그 표정으로 찍으면 사진 못 가져가요."
    y "그럼 저 주세요. 제가 보고 싶어서 찍는 건데요~"
    "첫 컷에서 둘 다 카메라를 봤다. 두 번째 컷을 앞두고 도현이 몸을 틀었다."
    d "이번에는 유진 씨 보고 있어도 돼요?"
    "유진은 남은 초를 확인하지 않고 고개를 돌렸다. 셔터가 울린 건 둘 다 웃고 난 뒤였다."
    "사진이 나오자 유진이 두 번째 컷을 손가락으로 짚었다. 그 사진이 든 한 장은 자기가 가져가겠다며 냉큼 챙겼다. 낮에 약속한 작은 그림을 보러 유진의 집에 들렀다."
    $ location = "같은 토요일 저녁 · 유진의 집"
    y "이건 일로 그린 건 아니에요. 집 창가에서 보이던 그림자를 남겨 봤어요."
    d "아까 식당에서는 제 표정 기다리시더니. 이번엔 제가 기다릴게요. 어디부터 보여 주고 싶으세요?"
    "유진은 그림을 가리키려던 손을 내렸다."
    y "그림은 아까부터 보여 드리고 싶었는데... 지금은 도현 씨가 오래 봐 주시는 게 더 좋네요."
    d "조금 더 있을래요. 그림 다 봤다고 바로 가긴 싫어서요."
    "유진은 그림 옆에 사진을 세웠다. 두 잔 사이로 몸을 조금 기울여 도현의 얼굴을 보았다."
    y "아까 두 번째 사진 있잖아요. 찍히기 전에 도현 씨가 저 먼저 봤죠."
    d "네. 실은 첫 번째부터 그러고 싶었어요."
    y "저도요. 지금도 카메라 없으니까 더 오래 봐도 되죠?"
    "도현이 유진 쪽으로 앉은 방향을 바꿨다. 둘 사이에 놓여 있던 찻잔은 손도 대지 않은 채였다."
    y "오늘은 좀 더 가까이 있고 싶어요. 여기서 같이 밤을 보내고 싶은데... 도현 씨는요?"
    $ progression_enter("yujin_r07.choice01")
    $ progression_checkpoint("yujin_r07.choice01")
    menu:
        "나도 함께 밤을 보내고 싶다고 답한다 — 친밀한 장면으로 이어짐.":
            d "저도요. 오늘은 같이 있고 싶어요."
            "유진이 도현의 손을 잡았다. 시선을 내린 건 도현 쪽이었다."
            y "손 차갑죠? 사진 찍을 때도 이랬어요. 도현 씨만 긴장한 줄 알았죠?"
            call event_sequence("yujin_r07", "casual")
            if not event_main_reached:
                "(장면 생략 · 시간이 흐릅니다.)"
            $ remember("yujin_r07_pace", "shared")
            y "내일 아침엔 제가 커튼 열어도 돼요? 빛 보여 드리고 싶어서요."
            d "네. 저는 그때도 옆에서 같이 볼게요."
        "오늘은 집으로 돌아가고 다음에 더 함께 있고 싶다고 말한다.":
            d "오늘은 집에 가서 쉴게요. 또 만나고 싶은 건 그대로예요."
            y "네. 그럼 내일 제가 연락해도 되죠? 오늘 보여 드린 그림 얘기 좀 더 하고 싶어요."
            "현관에서 인사를 나누고 각자 쉴 시간을 가졌다."
            $ remember("yujin_r07_pace", "deferred")
        "마음을 조금 더 이야기한 뒤 오늘은 각자 쉬자고 한다.":
            d "가까워지고 싶은 건 저도 그래요. 오늘은 그 얘기만 좀 더 하고 갈게요."
            y "네. 그럼 차 식기 전까지요. 말해 주셔서 좋아요."
            d "아까 사진 찍기 전에 긴장한 거 들켰어요?"
            y "네. 첫 컷에서 제 어깨에 손 올리려다가 내리셨잖아요."
            d "그것도 보셨어요?"
            y "거울에 다 비쳤어요. 다음에 찍을 땐 물어봐 주세요. 저 아마 된다고 할걸요."
            "도현은 차를 마저 마시고 일어났다. 현관을 나가기 전 주머니에서 사진을 꺼내 한 번 더 봤다."
            $ remember("yujin_r07_pace", "talk")
    $ remember("yujin_personal_drawing_seen", "집 창가의 그림자")
    $ award_once("yujin_R07", "yujin", 0)
    $ progression_note_ending()
    return

label yujin_r08:
    $ progression_enter("yujin_r08")
    $ progression_checkpoint("yujin_r08")
    if not dating or active_route != "yujin":
        $ progression_note_ending()
        return
    $ chapter = "유진 R08 · 다음 약속은 제가"
    if memory.get("yujin_r07_pace") == "shared":
        $ location = "다음 날 일요일 아침 · 유진의 집"
        "유진이 커튼을 조금 열었다. 도현도 일어나 반대쪽 커튼을 조금 걷었다. 어제 그림에서 봤던 그림자가 창가에 비쳤다."
        y "여기 보세요. 커튼 끝이 어제 그림이랑 달라졌죠?"
        d "제가 조금 더 열었나 봐요. 원래대로 해 둘까요?"
        y "아뇨. 오늘은 이대로요. ...도현 씨 눈부신 쪽 말고 이쪽에 앉으세요."
        "유진이 아침 접시를 그늘 쪽으로 옮겼다. 도현은 커튼에서 손을 떼고 그 옆에 앉아 아침을 먹었다."
        "도현은 자기 집에서 할 일을 마치기로 하고 돌아갔다."
        $ remember("yujin_r08_morning_shared")
    $ location = "같은 일요일 오후 · 각자의 집, 개인 메시지"
    if memory.get("yujin_r07_pace") == "shared":
        call phone_deliver("yujin_r08_memory", "yujin", "어제 두 번째 사진, 그림 옆에 뒀어요. 오늘 아침에도 도현 씨가 저렇게 봤는데 그땐 사진이 없네요.", contact="yujin")
    elif memory.get("yujin_r07_pace") == "talk":
        call phone_deliver("yujin_r08_memory", "yujin", "사진 다시 보니까 도현 씨 손 망설인 거 첫 컷에 다 나왔어요. 그거 보고 제가 웃은 것도요~", contact="yujin")
    else:
        call phone_deliver("yujin_r08_memory", "yujin", "푹 쉬셨어요? 사진 정리하다 보니까 저희 둘 다 카메라 안 보는 게 제일 잘 나왔어요. 다음에도 그걸로 찍어요~", contact="yujin")
    if memory.get("yujin_r06_expression") == "think_first":
        call phone_deliver("yujin_r08_invite", "yujin", "다음 주 수요일에 잠깐 만날까요? 생각해 보시고 편한 시간 알려 주세요. 저는 목요일도 괜찮아요.", contact="yujin")
    else:
        call phone_deliver("yujin_r08_invite", "yujin", "이번에도 제가 부를게요~ 다음 주 수요일에 잠깐 만날까요? 저는 목요일도 괜찮아요.", contact="yujin")
    $ phone_context = "yujin_r08_reply"
    $ progression_enter("yujin_r08.choice01")
    $ progression_checkpoint("yujin_r08.choice01")
    call screen office_phone(replies=[("wed19", "수요일 저녁 일곱 시가 좋다고 답한다."), ("thu19", "목요일 저녁 일곱 시를 제안한다."), ("wed1930", "수요일 일곱 시 반이 더 편하다고 말한다.")])
    $ remember("yujin_r08_availability", _return)
    $ phone_context = None
    if memory["yujin_r08_availability"] == "wed19":
        $ remember("yujin_r08_next_appointment", "수요일 저녁 일곱 시, 회사 근처 카페")
        call phone_deliver("yujin_r08_reply", "dohyun", "수요일엔 일곱 시쯤 나올 수 있어요. 회사 근처 카페에서 볼까요?", contact="yujin")
    elif memory["yujin_r08_availability"] == "thu19":
        $ remember("yujin_r08_next_appointment", "목요일 저녁 일곱 시, 회사 근처 카페")
        call phone_deliver("yujin_r08_reply", "dohyun", "저는 목요일 일곱 시가 더 편해요. 회사 근처 카페는 어때요?", contact="yujin")
    else:
        $ remember("yujin_r08_next_appointment", "수요일 저녁 일곱 시 반, 회사 근처 카페")
        call phone_deliver("yujin_r08_reply", "dohyun", "수요일 일곱 시 반이면 좋아요. 제 일 마무리하고 카페로 갈게요.", contact="yujin")
    if memory["yujin_r08_availability"] == "wed19":
        call phone_deliver("yujin_r08_confirm", "yujin", "네, 거기 좋아요. 컵 받침 이번에도 해바라기라고 하시면 저 진짜 사진 찍어 둘 거예요~", contact="yujin", important=True)
    elif memory["yujin_r08_availability"] == "thu19":
        call phone_deliver("yujin_r08_confirm", "yujin", "목요일 일곱 시에 봬요. 이번에도 제가 창가 자리부터 볼게요.", contact="yujin", important=True)
    else:
        call phone_deliver("yujin_r08_confirm", "yujin", "일곱 시 반도 괜찮아요. 먼저 도착하면 자리 잡고 연락드릴게요.", contact="yujin", important=True)
    $ remember("yujin_r08_proposer", "yujin")
    $ location = "같은 일요일 오후 · 유진의 집 — 유진 시점"
    "유진은 정한 약속을 달력에 적었다. ‘그때까지 보고 싶으면 또 연락해도 되죠?’라고 쓰다가 보내지 않고 지웠다."
    yn "약속까지 했는데 또 확인하려고 했네."
    "휴대폰을 엎어 뒀다가 다시 들었다. 이번에는 알람만 맞추고 음악을 틀었다."
    yn "보고 싶으면 그냥 보고 싶다고 보내면 되지. 대답 시험처럼 묻지는 말자."
    $ location = "같은 일요일 오후 · 도현의 집"
    $ cream_focus = None
    dn "정해진 시간 옆에 이름을 적었다. 이번엔 유진 씨가 정한 다음 약속이었다."
    $ remember("yujin_r08_complete")
    $ award_once("yujin_R08", "yujin", 4)
    $ progression_note_ending()
    return
