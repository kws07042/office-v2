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
            d "그 책 제목 기억해 둘게요. 아직 안 읽은 부분도 다음에 듣고 싶어요."
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
    "『느린 모퉁이』에서 돌아가는 길에 같은 창문을 한 번 더 보는 짧은 대목을 함께 읽었다. 처음 보는 부분은 서두르지 않았다."
    "서윤은 마지막 문장을 한 번 더 읽다가 도현 쪽으로 책을 밀었다."
    s "여기. 난 여기서 그냥 못 넘어가겠더라. 네가 휙 읽고 넘기면 좀 서운할 것 같고~"
    $ progression_enter("seoyun_o01.choice01")
    $ progression_checkpoint("seoyun_o01.choice01")
    menu:
        "돌아가는 발걸음이 좋았다고 한다.":
            d "저는 돌아가는 쪽이요. 한번 봤다고 꼭 안에 들어가야 하는 건 아니니까요."
            s "난 안쪽부터 봤네. 네 말 들으니까 밖의 발걸음도 궁금해졌어."
            $ remember("seoyun_o01_impression", "창문 밖으로 돌아가는 발걸음")
        "지나쳤던 날들이 궁금하다고 한다.":
            d "이날만 다시 본 건 아닐 것 같아서요. 전에는 어떻게 지나갔을까요?"
            s "그 전날들까지 읽는구나. 난 돌아본 그 순간에만 있었는데."
            $ remember("seoyun_o01_impression", "다시 보기 전 지나쳤던 다른 날들")
        "서로 다른 데서 멈춘 게 좋았다고 한다.":
            d "같이 읽고 대답 기다리는 게 좋아요. 어디가 좋으셨는지 제가 미리 알 수는 없으니까요."
            s "그 말 들으니까 다음 장도 네 대답 기다려 보고 싶네."
            $ remember("seoyun_o01_impression", "같은 대목을 다르게 읽고 답을 기다린 시간")
    $ remember("seoyun_o01_read", "느린 모퉁이의 같은 창문을 다시 보는 대목, 전권 완독 아님")
    $ remember("seoyun_o01_status", "completed")
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
            d "고치면 또 읽어 주실래요? 이번에 좋았던 데가 없어지면 그것도 말해 주세요."
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
    s "이쯤이면 단골 포인트로 나도 한 번 무료 초대 가능한가?"
    "도현이 테이블의 주문서를 들었다가 내려놓았다. 서윤의 시선도 종이로 갔다가 도현에게 돌아왔다."
    $ progression_enter("seoyun_o02.choice01")
    $ progression_checkpoint("seoyun_o02.choice01")
    menu:
        "계산하라는 줄 알았다고 고백한다.":
            d "다음에 제가 전부 계산해야 하나 했어요. 초대하고 싶긴 한데, 포인트 결제는 좀 어렵네요~"
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
            d "저도 재치 있게 받으려다가 말이 막히네요. 다음엔 제가 정한 데 같이 가요."
            s "좋아. 그럼 실패한 대답은 빼고 초대만 남겨 둘게. 날짜는 네 일정 보고 알려 줘."
            $ remember("seoyun_o02_boundary", "장난이 막히면 원하는 말을 직접 꺼내기")
    "무슨 뜻이었는지 알고 나서 같이 웃었다. 날짜는 다음 일정을 보고 정하기로 했다."
    $ remember("seoyun_o02_status", "completed")
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
    s "항상 같은 자리여야 단골인가 했는데. 오늘은 어디 앉아 볼래?"
    $ progression_enter("seoyun_o03.choice01")
    $ progression_checkpoint("seoyun_o03.choice01")
    menu:
        "조명 아래 자리에 앉는다.":
            "탁자에 빛이 떨어지는 자리를 보며 조명을 옮기기 전 자리를 떠올렸다."
            "도현이 손을 펴 조명 아래에 댔다. 손가락 그림자가 노트 한쪽을 가렸다."
            d "여기 앉으면 글은 덜 쓰겠네요. 그림자가 자꾸 끼어들어서."
            s "자리 정한 사람이 나였나?"
            d "제가 정했죠. 그래서 일단 조명 탓부터 하는 거예요."
            "서윤이 제 노트를 옆으로 조금 밀었다. 둘 사이에 밝은 자리 하나가 생겼다."
            s "여기 써. 내 건 오늘 많이 안 쓸 거니까."
            d "왜요?"
            s "네가 손 펴고 노는 걸 보고 싶어서. ...다시 해 봐, 아까 그거."
            $ remember("seoyun_o03_detail", "옮겨진 작은 조명 아래 새 자리")
        "그 책 선반 옆에 앉는다.":
            "『느린 모퉁이』는 같은 선반에 있었다. 새로 꺼내 읽는 대신 오늘 가져온 노트를 펼쳐 놓았다."
            s "책이 있는 건 같은데, 오늘은 네 문장 기다리네."
            d "아직 펴지도 않았는데 압박이 세네요."
            "서윤이 도현의 노트 표지만 보며 손끝으로 제 입을 가렸다."
            s "그럼 아무 말 안 하고 기다릴게."
            d "그게 더 세요. 그냥 평소처럼 놀려 주세요."
            "서윤이 손을 내리고 웃었다. 도현은 노트를 펼치되, 읽어 줄 줄을 제 손으로 가렸다."
            d "찾을 때까지는 보시면 안 됩니다."
            s "알겠어. 그럼 그동안 얼굴만 봐도 돼?"
            "도현이 찾던 줄을 지나쳤다. 서윤은 이번엔 아무 말도 덧붙이지 않았다."
            $ remember("seoyun_o03_detail", "같은 책 선반 앞에서 오늘의 노트를 놓은 자리")
        "처음 앉는 창가로 간다.":
            "처음 앉아 보는 창가로 정했다. 밖을 지나는 사람 대신 유리에 비친 작은 식물 그림자를 같이 봤다."
            d "이 자리 좋네요. 식물은 밖에 있는데 그림자는 테이블까지 들어와요."
            "도현이 빈 컵 받침을 그림자 아래로 옮겼다. 서윤은 제 받침을 그 옆에 놓았다."
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
    $ award_once("seoyun_O03", "seoyun", 2)
    $ progression_note_ending()
    return
