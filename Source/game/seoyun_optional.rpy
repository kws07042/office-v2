label seoyun_o01_offer:
    $ progression_enter("seoyun_o01_offer")
    $ progression_checkpoint("seoyun_o01_offer")
    if not dating or active_route != "seoyun" or memory.get("seoyun_o01_status"):
        $ progression_note_ending()
        return
    $ progression_enter("seoyun_o01_offer.choice01")
    $ progression_checkpoint("seoyun_o01_offer.choice01")
    menu:
        "잠깐 책 읽기 — 책 제목을 기억하는 사람 (선택 일상)":
            call seoyun_o01
        "본편 계속 — 다음 수요일의 만남으로":
            $ remember("seoyun_o01_status", "skipped")
        "추천한 책은 다음에도 이야기하자고 짧게 말하고 본편 계속":
            d "제목 기억해 둘게요. 다음에 어디까지 읽으셨는지 물어봐도 돼요?"
            s "좋아. 다 읽었냐고 검사부터 하진 않을게~"
            $ remember("seoyun_o01_status", "brief")
    $ progression_note_ending()
    return

label seoyun_o01:
    $ progression_enter("seoyun_o01")
    $ progression_checkpoint("seoyun_o01")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 O01 · 책 제목을 기억하는 사람"
    $ location = "같은 토요일 늦은 오후 · 북카페"
    if memory.get("seoyun_next_date_plan") != "bookcafe":
        "헤어지기 전에 서윤의 단골 북카페로 자리를 옮겼다. 서윤이 추천했던 책을 선반에서 꺼냈다."
    "둘은 『느린 모퉁이』에서 돌아가는 길에 같은 창문을 또 보는 대목을 읽었다. 처음 읽는 구절은 천천히 넘겼다."
    dn "같은 창문을 한 번 더 보는 대목. 서윤 씨가 왜 이 책을 좋아하는지 좀 알 것 같았다."
    "서윤은 마지막 문장을 한 번 더 읽다가 도현 쪽으로 책을 밀었다."
    s "여기. 난 이 줄에서 걸리더라. 너만 휙 넘기면 나 좀 서운해~"
    $ progression_enter("seoyun_o01.choice01")
    $ progression_checkpoint("seoyun_o01.choice01")
    menu:
        "돌아가는 발걸음이 좋았다고 한다.":
            d "전 돌아가는 쪽이요. 한번 봤다고 꼭 안에 들어가야 하는 건 아니니까요."
            s "난 안쪽부터 봤네. 네 말 들으니까 밖의 발걸음도 궁금해졌어."
            $ remember("seoyun_o01_impression", "창문 밖으로 돌아가는 발걸음")
        "지나쳤던 날들이 궁금하다고 한다.":
            d "이날만 다시 본 건 아닐 것 같아서요. 전엔 어떻게 지나갔을까요?"
            s "어제도 거길 지났을까 생각한 거네. 난 딱 뒤돌아보는 데서 멈췄거든."
            $ remember("seoyun_o01_impression", "다시 보기 전 지나쳤던 다른 날들")
        "서로 다른 데서 멈춘 게 좋았다고 한다.":
            d "같이 읽으면 서윤 씨는 어디서 멈추실까 궁금해요. 제 예상이 자주 빗나가거든요."
            s "그 말 들으니까 다음 장도 네 대답 기다려 보고 싶네."
            $ remember("seoyun_o01_impression", "같은 대목을 다르게 읽고 답을 기다린 시간")
    $ remember("seoyun_o01_read", "느린 모퉁이의 같은 창문을 다시 보는 대목, 전권 완독 아님")
    $ remember("seoyun_o01_status", "completed")
    dn "다음 장은 서윤 씨가 어디서 책을 멈출까."
    $ award_once("seoyun_O01", "seoyun", 2)
    $ progression_note_ending()
    return

label seoyun_o02_offer:
    $ progression_enter("seoyun_o02_offer")
    $ progression_checkpoint("seoyun_o02_offer")
    if not dating or active_route != "seoyun" or memory.get("seoyun_o02_status"):
        $ progression_note_ending()
        return
    $ progression_enter("seoyun_o02_offer.choice01")
    $ progression_checkpoint("seoyun_o02_offer.choice01")
    menu:
        "잠깐 더 이야기하기 — 서로 실패한 농담 (선택 일상)":
            call seoyun_o02
        "본편 계속 — 일요일 산책 약속으로":
            $ remember("seoyun_o02_status", "skipped")
        "오늘 고른 문장도 다음에 다시 읽어 달라고 하고 본편 계속":
            d "고치면 한 번 더 읽어 주실래요? 먼저 게 더 좋던 대목도 짚어 주세요."
            s "좋아. 대신 지우면 안 된다고 우길지도 몰라~"
            $ remember("seoyun_o02_status", "brief")
    $ progression_note_ending()
    return

label seoyun_o02:
    $ progression_enter("seoyun_o02")
    $ progression_checkpoint("seoyun_o02")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 O02 · 서로 실패한 농담"
    $ location = "같은 토요일 늦은 오후 · 북카페"
    s "이쯤 되면 나도 한 번쯤 네 쪽에서 불러 줘야 되는 거 아냐? 단골 우대 같은 거 없어?"
    dn "아까 그 말도 반쯤 농담이겠지. 근데 어느 쪽 절반이지."
    "도현이 주문서를 들었다가 내려놓았다. 서윤도 그 종이를 봤다가 다시 도현을 봤다."
    $ progression_enter("seoyun_o02.choice01")
    $ progression_checkpoint("seoyun_o02.choice01")
    menu:
        "계산하라는 줄 알았다고 고백한다.":
            d "다음엔 제가 다 사야 하나 했어요. 초대는 하고 싶은데 포인트는 좀 모자라네요~"
            s "아, 계산 말고. 네가 불러 주면 또 오고 싶다고."
            d "그러면 포인트는 안 모아도 되네요."
            s "응. 초대는 지금도 받고 있어."
            $ remember("seoyun_o02_boundary", "돈 계산과 초대를 농담 하나로 묶지 않기")
        "한 번만 더 말해 달라고 한다.":
            d "손님이 메뉴 설명을 놓쳤는데요. 이번만 한 번 더 말해 주세요."
            s "네가 정해서 불러 주면 좋겠다고. ...아, 대놓고 말하니까 짧네."
            d "메뉴 설명은 합격입니다."
            s "손님이 좀 까다로운데~"
            $ remember("seoyun_o02_boundary", "못 알아들은 농담은 뜻을 다시 묻고 말하기")
        "받아치려다 실패하고 그냥 초대한다.":
            d "저도 재밌게 받으려 했는데 말이 안 나오네요. 다음엔 제가 고른 데 가요."
            s "그래. 그 말이 듣고 싶었어. 언제 되는지 알려 줘~"
            $ remember("seoyun_o02_boundary", "장난이 막히면 원하는 말을 직접 꺼내기")
    "무슨 뜻이었는지 알고 나서 같이 웃었다. 날짜는 다음 일정을 보고 정하기로 했다."
    $ remember("seoyun_o02_status", "completed")
    dn "둘 다 농담엔 실패했다. 집에 가긴 아직 아까운데."
    $ award_once("seoyun_O02", "seoyun", 2)
    $ progression_note_ending()
    return

label seoyun_o03_offer:
    $ progression_enter("seoyun_o03_offer")
    $ progression_checkpoint("seoyun_o03_offer")
    if not dating or active_route != "seoyun" or memory.get("seoyun_o03_status"):
        $ progression_note_ending()
        return
    $ progression_enter("seoyun_o03_offer.choice01")
    $ progression_checkpoint("seoyun_o03_offer.choice01")
    menu:
        "잠깐 만나기 — 우리도 단골인가 (선택 일상)":
            call seoyun_o03
        "본편 계속 — 일요일 저녁 북카페로":
            $ remember("seoyun_o03_status", "skipped")
        "저녁에는 전에 쓴 문장도 가져가겠다고 하고 본편 계속":
            d "저녁엔 초안도 가져갈게요. 제가 쓴 문장부터 보여 드리고 싶어요."
            s "응. 내가 대신 쓴 말 아니니까 더 궁금하지."
            $ remember("seoyun_o03_status", "brief")
    $ progression_note_ending()
    return

label seoyun_o03:
    $ progression_enter("seoyun_o03")
    $ progression_checkpoint("seoyun_o03")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 O03 · 우리도 단골인가"
    $ location = "일요일 늦은 오후 · 다시 찾은 북카페"
    "각자 오전을 보내고 저녁 약속보다 조금 일찍 만났다. 도현은 지난번과 다른 자리의 작은 조명을 봤다."
    dn "저번엔 조명이 저기 있는 줄도 몰랐다. 오늘은 그 밑에 한 번 앉아 보고 싶다."
    s "항상 같은 자리여야 단골인가 했는데. 오늘은 어디 앉아 볼래?"
    $ progression_enter("seoyun_o03.choice01")
    $ progression_checkpoint("seoyun_o03.choice01")
    menu:
        "조명 아래 자리에 앉는다.":
            "탁자에 빛이 떨어지는 자리를 보며 조명을 옮기기 전 자리를 떠올렸다."
            "도현이 손을 펴 조명 아래에 댔다. 손가락 그림자가 노트 한쪽을 가렸다."
            d "여기 앉으면 글은 덜 쓰겠네요. 그림자가 자꾸 끼어들어서."
            s "잠깐, 자리 고른 게 나였어?"
            d "제가 정했죠. 그래서 일단 조명 탓부터 하는 거예요."
            "서윤이 제 노트를 옆으로 조금 밀었다. 둘 사이에 밝은 자리 하나가 생겼다."
            s "여기 써. 내 건 오늘 많이 안 쓸 거니까."
            d "왜요?"
            s "네가 손 활짝 펴고 노는 게 보고 싶어서. 아까 그거 한 번만 더."
            $ remember("seoyun_o03_detail", "옮겨진 작은 조명 아래 새 자리")
        "그 책 선반 옆에 앉는다.":
            "『느린 모퉁이』는 같은 선반에 꽂혀 있었다. 오늘은 그 자리에 두고 가져온 노트를 펼쳤다."
            s "책은 그대로 있는데 오늘은 네가 쓴 문장부터 기다리게 되네."
            d "아직 펴지도 않았는데 압박이 세네요."
            "서윤이 도현 노트 표지만 보며 손끝으로 제 입을 가렸다."
            s "그럼 아무 말 안 하고 기다릴게."
            d "그 말이 더 세요. 차라리 평소처럼 놀려 주세요."
            "서윤이 손을 내리고 웃었다. 도현은 노트를 펼치되, 읽어 줄 줄을 제 손으로 가렸다."
            d "찾을 때까지는 보시면 안 됩니다."
            s "알겠어. 그럼 그동안 얼굴만 봐도 돼?"
            "도현이 찾던 줄을 지나쳤다. 서윤은 이번엔 아무 말도 덧붙이지 않았다."
            $ remember("seoyun_o03_detail", "같은 책 선반 앞에서 오늘의 노트를 놓은 자리")
        "처음 앉는 창가로 간다.":
            "처음 앉는 창가 자리였다. 두 사람은 행인 대신 유리에 비친 작은 식물 그림자를 봤다."
            d "이 자리 좋네요. 밖에 있는 식물 그림자가 여기 탁자까지 와요."
            "도현이 빈 컵받침을 그림자 아래로 옮겼다. 서윤은 제 받침을 그 옆에 놓았다."
            s "화분 두 개 됐네."
            d "제 건 잎이 세 장인데, 그쪽은 한 장이에요."
            s "그럼 조금만 옆으로... 아, 없어졌다."
            "그림자 밖으로 나간 받침을 서윤이 다시 끌어왔다. 도현은 제 것을 원래 자리로 돌리지 않았다."
            d "한 장짜리가 제일 잘 보이는 자리 드릴게요."
            s "네 화분은?"
            d "지금은 그거 다시 맞추시는 게 더 재밌어서요."
            "서윤이 받침을 놓던 손을 멈췄다. 한 장짜리 잎 끝이 테두리에 걸렸다."
            s "...다 맞췄는데, 좀만 더 볼래?"
            $ remember("seoyun_o03_detail", "처음 고른 창가의 식물 그림자")
    $ remember("seoyun_o03_status", "completed")
    dn "가게 안에서 자리를 이렇게 오래 고른 건 처음이다. 저녁은 조금 늦어져도 되겠다."
    $ award_once("seoyun_O03", "seoyun", 2)
    $ progression_note_ending()
    return
