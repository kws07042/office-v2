# Seoyun is a 32-year-old colleague. Final art/voice production is deferred.
define sn = Character("한서윤", what_prefix="『", what_suffix="』", callback=renpy.curry(cream_note_speaker)("seoyun"))
default seoyun_prepared = False
default seoyun_revision_notice_shown = False

label seoyun_r01:
    $ progression_enter("seoyun_r01")
    $ progression_checkpoint("seoyun_r01")
    $ active_route = "seoyun"
    $ cream_focus = "seoyun"
    $ chapter = "서윤 R01 · 언제 한번 말고 오늘"
    $ location = "목요일 퇴근 무렵 · 공용 테이블"
    "목요일 퇴근 무렵. 서윤이 가방을 메며 도현 책상 옆을 지나갔다."
    s "도현 씨, 고생했어. 언제 한번 커피 마시자~"
    d "그 말, 지난주에도 하셨어요."
    s "...그랬나?"
    d "네. '언제 한번'. 저는 그 '언제'를 기다리고 있었는데요."
    "서윤이 걸음을 멈췄다. 가방끈을 고쳐 메는 손이 잠깐 느려졌다."
    s "그 말 자주 해. 진짜로 만나자고 날짜까지 잡은 지는 좀 됐네."
    d "그럼 전 서운해해도 돼요?"
    s "...대답이 빠르네. 알았어. 다음 주 안에 진짜로 날 잡을게. 이번엔 '언제'에 날짜 넣어서."
    "서윤은 평소의 웃음으로 돌아가 손을 흔들고 나갔다. 도현은 그 웃음이 돌아오기 전의 반 초를 봤다."
    dn "농담으로 넘어갈 뻔한 말을 붙잡았다. 다음 주라. 며칠 남았지."
    $ location = "다음 주 수요일 오후 · 개인 메시지"
    call phone_deliver("seoyun_r01_invite", "seoyun", "'언제 한번 보자' 있잖아\n그거 오늘로 해도 돼? 일곱 시, 회사 앞 작은 카페", contact="seoyun", important=True)
    call phone_deliver("seoyun_r01_accept", "dohyun", "좋아요! 일곱 시에 갈게요\n오늘은 제가 질문하는 날이죠?", contact="seoyun")
    call phone_deliver("seoyun_r01_confirm", "seoyun", "오늘은 네가 먼저 물어봐\n대신 나도 하나는 물을 거야 ㅋㅋ", contact="seoyun")
    $ remember("seoyun_r01_appointment", "수요일 저녁 일곱 시, 회사 앞 카페")
    $ location = "같은 수요일 저녁 일곱 시 · 회사 앞 카페"
    "커피 두 잔과 작은 쿠키 하나. 서윤은 마주 앉자마자 턱을 괴고 도현을 봤다."
    dn "턱 괴고 저렇게 기다리면, 결국 내가 먼저 말하게 된다."
    if memory.get("seoyun_intro") == "humor":
        s "첫날 내 농담 받아치고 질문도 안 놓치더라. 오늘도 그 코스?"
        d "오늘은 웃는 것부터 할까 하는데요."
    elif memory.get("seoyun_intro") == "clarify":
        s "첫날에 문장을 둘로 나눠 보자고 했었지. 오늘도 할 말이 많아?"
        d "좀 많았는데 만나니까 뭐부터 물어볼지 모르겠어요."
    elif memory.get("seoyun_intro") == "draft":
        s "첫날에 초안 소리 내서 읽던 그 배짱, 아직 있어?"
        d "있어요. 오늘은 업무 말고 제 질문에 쓸게요."
    else:
        s "늘 답장 기다리는 쪽이 나였는데. 질문 받는 자리는 좀 어색하네."
        d "전 따로 불러 주신 게 그냥 반가운데요."
    if memory.get("c07_seoyun_next_question"):
        s "저번엔 오 분만 더 있자고 했지. 오늘은 오 분 말고 넉넉하게 빼 왔어."
    $ progression_enter("seoyun_r01.choice01")
    $ progression_checkpoint("seoyun_r01.choice01")
    menu:
        "원래 사람한테 궁금한 게 많으세요?":
            d "질문하실 때 대답을 진짜 기다리시잖아요. 원래 그러세요?"
            s "급할 땐 내가 답도 정해 놓고 묻지. 오늘은 좀 달라. 아까 올 때부터 네가 뭐라고 할지 궁금했어."
            d "알겠어요. 이번엔 서윤 씨 차례예요. 저한텐 뭐가 궁금하세요?"
            "서윤이 입을 열었다가 웃음으로 닫았다. 컵받침을 손끝으로 빙글 돌렸다."
            s "...혼자 마실 때도 커피를 그렇게 아껴 마셔?"
            d "아뇨. 원래는 식기 전에 다 마셔요. 오늘은 좀 아까워서요."
            s "커피가? 아니면... 응, 커피 얘기라고 해 두자."
            $ remember("seoyun_r01_topic", "curiosity")
        "쉬는 날엔 뭐 하세요?":
            d "답장 안 기다려도 되는 날은 뭐 하세요?"
            s "단골집 가서 늘 먹던 거 시켜. 먹으면서 ‘다른 거 시킬걸’ 해. 그리고 다음에 또 같은 거 시켜."
            d "오늘도요?"
            s "응~ 네 커피 냄새 맡으니까 그게 더 맛있어 보여."
            d "다음엔 서윤 씨 메뉴도 제가 골라 볼까요?"
            s "좋아. 대신 내가 오늘 뭐 시켰는지는 기억해 둬."
            "서윤이 가방을 의자 안쪽으로 밀어 넣었다. 테이블 위가 조금 넓어졌다."
            $ remember("seoyun_r01_topic", "rest")
        "일 없었어도 저 부르셨어요?":
            d "오늘 업무가 하나도 없었어도 저 불렀을까요? 전 불렸으면 했어요."
            "서윤의 손이 컵 손잡이에서 멈췄다."
            s "...와. 질문 준비해 왔네. 응, 불렀을 거야. 방금 그 말 듣고 확신했고."
            d "그럼 잘 온 거네요."
            s "근데 첫 질문에 이렇게 바로 답이 나오면 재미없잖아. 좀 버티지."
            d "다 듣고 일어날 생각은 없었어요."
            "서윤의 휴대폰에 알림이 떴다. 서윤은 짧게 답장하고 화면을 엎었다."
            d "받으셔도 돼요."
            s "친구야. 오늘 어디 가냐고. ...답했어. 오늘은 시간 넉넉해."
            s "그러니까 그때까진 네 얘기 마저 해. 커피도 아직 반이고."
            d "제가 붙잡은 거네요."
            s "붙잡힌 척해 주는 거야. 착각은 자유고."
            $ remember("seoyun_r01_topic", "direct")
    "서윤이 설탕 통을 도현 쪽으로 슬쩍 밀었다. 도현은 손대지 않고 커피를 한 모금 마셨다."
    s "어? 그냥 마셔? 하나는 넣을 줄 알았는데."
    d "어떤 사람으로 보셨는데요?"
    s "단 거 주면 절대 거절 못 할 사람."
    d "주시면 먹죠. 커피에 넣는 건 아까워서요."
    "서윤이 설탕 통을 도로 끌어가 포장 하나를 뜯었다. 자기 잔에 털어 넣었다."
    s "남 취향 맞히다가 내 커피만 쓰게 마셨네. ...나 원래 이런 거 잘 맞히거든?"
    d "오늘은요?"
    s "오늘만 봐서는 좀 못하네. 설탕은 틀렸다."
    d "질문 더 하셔도 돼요. 저도 아직 남았어요."
    "도현이 팔을 탁자 위에 편하게 올렸다. 서윤은 그걸 보다가, 아주 작게 고개를 끄덕였다."
    s "그럼 두 번째 질문. 토요일에 내 단골 북카페 가 볼래? 두 시, 서점 입구."
    d "제가 엉뚱한 책 골라도 따라오실 거예요?"
    s "응. 대신 별로면 바로 말할 거야. 나 그런 건 안 참아."
    $ remember("seoyun_r02_appointment", "토요일 오후 두 시, 단골 서점 입구")
    dn "별로면 바로 말한다니. 오늘은 그 ‘별로’만은 듣고 싶지 않다."
    $ award_once("seoyun_R01", "seoyun", 4)
    $ progression_note_ending()
    return

label seoyun_family_context:
    # A conversation remembered only when actually read, never inferred from old saves.
    if not memory.get("seoyun_family_disclosed"):
        "서윤이 책 사이에 손가락을 끼운 채 도현을 봤다. 웃고는 있는데, 농담할 때 얼굴은 아니다."
        s "다음 약속 잡기 전에 하나만. 나 이혼했어. 삼 년 됐고, 지금은 혼자 살아."
        d "아… 네. 몰랐어요."
        s "표정 봐. 내가 너무 갑자기 말했나?"
        d "커피 아직 반이나 남았는데요."
        s "...그래. 전남편이랑은 연락 안 해. 같은 업계라 가끔 이름은 들리지만."
        d "그분 얘기는 서윤 씨가 하고 싶을 때 들을게요."
        s "지금 다 괜찮다고 말해 줄 필요 없어. 나도 먼저 말하고 싶어서 말한 거야."
        d "그럼 오늘은 한 가지만요. 저는 조금 더 있다 가고 싶어요."
        s "...응. 그건 받을게. 그럼 이 책, 네가 골라 봐. 이상한 거 고르면 웃어 줄게."
        d "벌써 웃을 준비하시는 거 아니에요?"
        s "들켰네."
        $ remember("seoyun_family_disclosed")
        $ remember("seoyun_family_state", "divorced")
        $ remember("seoyun_parenting_context", "이혼 3년, 자녀 없음, 혼자 거주, 전남편과 재결합 관계 아님")
    return

label seoyun_r02:
    $ progression_enter("seoyun_r02")
    $ progression_checkpoint("seoyun_r02")
    $ chapter = "서윤 R02 · 누나도 말을 고를 때"
    $ location = "금요일 오후 · 공용 테이블"
    "금요일 오후. 도현이 쓴 안내 문구 초안이 서윤의 책상에 올라갔다. 삼십 분 뒤 돌아온 종이는 빨간 펜으로 덮여 있었다."
    s "울지 마~ 빨간 건 애정이야."
    d "애정이 문장보다 많은데요."
    s "첫 줄만 봐. ‘고객님의 빛나는 일상에 함께하겠습니다.’ 대체 누구 들으라고 쓴 걸까?"
    d "...고객님이요."
    s "안내판을 읽는 사람이 누군지 먼저 보자. 퇴근하면서 잠깐 들른 사람이면 길게 읽을 시간 없잖아."
    "서윤이 빨간 펜으로 첫 줄을 지우고 그 위에 짧게 적었다. '오늘도 수고했어요. 이건 내일의 당신 거예요.'"
    d "...이게 훨씬 좋네요."
    s "당연하지. 삼 년을 혼자 퇴근한 사람이 쓴 거니까."
    "가볍게 한 말이었다. 서윤은 바로 다음 줄로 펜을 옮겼지만, 도현은 그 문장에서 한참 눈을 떼지 못했다."
    s "내일 서점 약속, 잊지 않았지? 거기선 빨간 펜 안 들고 갈게."
    d "책에 줄 긋는 것도 안 하세요?"
    s "책은 안 고쳐. 사람만 고쳐~"
    dn "내일 한 번 더 물어볼까. 아까 웃으면서 한 말 어디까지 믿어도 되냐고."
    $ location = "토요일 오후 두 시 · 단골 서점과 북카페"
    if c06_person == "seoyun" and c06_topic == "weekend":
        s "네가 숫자 적어 준 책갈피, 오늘도 꽂아 왔어. 진도 검사는 안 하기로 했지?"
        d "네. 대신 잘 쉬셨는지 물어보기로 했죠."
    elif c06_person == "seoyun" and c06_topic == "place":
        d "같이 오면 서로 다른 책부터 집겠다고 했잖아요. 오늘은 직접 보겠네요."
        s "그럼 관찰 들어간다~ 넌 제목만 보고도 웃나 한번 보자."
    elif c06_person == "seoyun" and c06_topic == "today":
        d "오늘은 책 덮어 놓고 질문하실 거예요?"
        s "오늘은 책도 같이 봐야지. 그래도 얘기할 시간은 넉넉해."
    else:
        s "내가 권했다고 독후감까지 받진 않아. 별로면 딴 선반 보자."
    $ cg("seoyun_r02")
    "서윤이 좋아한다는 얇은 산문집 『느린 모퉁이』를 꺼냈다. 도현은 표지만 보고 옆 선반의 엉뚱한 제목을 집었다."
    dn "서윤 씨가 고른 책 옆에서 내가 집은 제목만 유난히 컸다. 좀 엉뚱했나."
    d "전 이거요. 제목만 보면 서윤 씨가 집을 줄 알았어요."
    s "벌써 날 그렇게 안다고? ...그 책, 사실 한 번도 안 읽었어."
    d "그럼 오늘 제가 틀린 거네요."
    s "응. 근데 어디까지 틀렸는지는 궁금하네. 뒤표지 한 줄만 같이 볼래?"
    "각자 집은 책의 뒷면을 읽었다. 서윤이 도현에게 어울리겠다고 고른 책도 표지를 넘겨 보니 그의 취향과는 달랐다."
    d "오늘은 서로 맞힌 것보다 틀린 게 많네요."
    s "다음엔 좀 더 맞히겠지. 아직 서로 모르는 게 더 많잖아~"
    d "서윤 씨는 좋아하는 사람 앞에서도 이렇게 말을 잘하세요?"
    "서윤이 책장을 넘기던 손을 멈췄다. 이번엔 바로 농담이 따라오지 않았다."
    $ progression_enter("seoyun_r02.choice01")
    $ progression_checkpoint("seoyun_r02.choice01")
    menu:
        "대답을 재촉하지 않고 기다린다.":
            d "지금 대답 안 나오셔도 돼요. 물어보고 싶어서 물은 거예요."
            "서윤이 책을 내려놓고 도현을 봤다."
            s "...응. 지금 다른 얘기 할 뻔했네. 그 질문은 조금만 기다려 줘."
            d "기다리는 동안 책부터 볼까요?"
            s "응. ...근데 지금은 글씨가 잘 안 들어오네."
            d "그럼 저도 넘기는 척만 할게요."
            s "둘 다 책 보러 온 건 아닌가 봐~"
            $ remember("seoyun_r02_response", "wait")
        "궁금해서 묻는 거라고 못 박는다.":
            d "전 서윤 씨를 더 알고 싶어서 물었어요. 장난 아니고요."
            s "그렇게 바로 말해? ...잠깐만. 나 좋아하는 거 얼굴에 다 나왔지."
            "서윤이 책을 들었다가 도로 내렸다. 도현이 웃자 이번엔 바로 받아치지 못했다."
            s "이럴 때 책 뒤에 숨으면 너무 티 나겠지?"
            d "네. 지금은 내려놓으신 쪽이 좋아요."
            s "...그것까지 바로 대답하면, 나 준비한 말이 없잖아."
            "책 대신 서로를 보고 짧게 웃었다."
            $ remember("seoyun_r02_response", "my_interest")
        "멋진 대답 안 해도 된다고 한다.":
            d "멋있게 답 안 하셔도 돼요. 잠깐 고민하시는 것도 서윤 씨 얘기잖아요."
            s "그럼 방금 내가 네 취향 틀린 것도 봐준 거야?"
            d "그건 다음에 다시 맞혀 보시면 돼요."
            s "...그런 대답은 어디서 배워 와?"
            d "방금 여기서요. 서윤 씨가 먼저 틀리셔서요."
            s "아, 그 얘기 다시 하는 거야?"
            d "틀렸어도 또 물어봐 주실 거죠?"
            s "다음엔 네가 내. 나 틀린 문제일수록 꼬박꼬박 적어 놓거든~"
            $ remember("seoyun_r02_response", "unfinished")
    call seoyun_family_context
    if not memory.get("booklet_known_seoyun"):
        d "전 요즘 동네 사진하고 짧은 글 모아서 작은 기록집 만들고 있어요. 아직은 메모가 더 많고요."
        s "그럼 처음 보는 사람한테도 하나 들려줄래? 잘 정리한 거 말고, 네가 멈춘 순간이 궁금해."
        $ remember("seoyun_booklet_introduced")
    else:
        s "다음엔 네가 남긴 것도 하나 들려줄래? 기록집 얘기 아니어도, 네가 멈춘 순간 하나."
    d "좋아요. 다음 수요일 일곱 시에 이 카페에서요. 하나 가져올게요."
    $ progression_enter("seoyun_r02.choice02")
    $ progression_checkpoint("seoyun_r02.choice02")
    menu:
        "퇴근길 사진 한 장을 가져오겠다고 한다.":
            d "사진 한 장 찍어 올게요. 왜 멈췄는지는 제가 말하고요."
            s "좋아. 사진 밖에 있는 말도 기다릴게."
            $ remember("seoyun_promise", "photo")
        "돌아오는 길의 소리를 한 줄 써 오겠다고 한다.":
            d "한 줄 써 올게요. 제목 멋부리지 않고요."
            s "응. 네가 읽는 목소리까지 들려줘. 내가 엉뚱하게 읽으면 바로 고치고~"
            $ remember("seoyun_promise", "sound")
        "아무것도 안 한 시간을 들려주겠다고 한다.":
            d "아무것도 안 한 시간도 하나 가져올게요. 말로요."
            s "그것도 좋네. 그건 사진으로 보여 달라고도 못 하겠다."
            $ remember("seoyun_promise", "rest")
    $ remember("seoyun_recommended_book", "느린 모퉁이")
    $ remember("seoyun_r03_appointment", "다음 수요일 저녁 일곱 시, 같은 북카페")
    dn "수요일엔 뭘 가져갈지 정했다. 그래도 제일 기다려지는 건 다시 여기 앉는 일이었다."
    $ location = "같은 날 밤 · 각자의 집, 개인 메시지"
    call phone_deliver("seoyun_r02_m1", "seoyun", "느린 모퉁이 펴 봤어?\n아직이면 펴지 마 ㅋㅋ 수요일에 첫 장부터 같이 얘기하고 싶어졌거든", contact="seoyun")
    call phone_deliver("seoyun_r02_m2", "dohyun", "헉 벌써 세 장 읽었는데요...", contact="seoyun")
    call phone_deliver("seoyun_r02_m3", "seoyun", "세 장이나? 빠르네 ㅋㅋ\n거기까지. 네 번째 장은 내가 제일 좋아해. 같이 넘기자", contact="seoyun")
    $ award_once("seoyun_R02", "seoyun", 7)
    $ progression_note_ending()
    return

label seoyun_r03:
    $ progression_enter("seoyun_r03")
    $ progression_checkpoint("seoyun_r03")
    $ chapter = "서윤 R03 · 네가 기억했던 약속"
    $ location = "수요일 점심 · 회사 옥상"
    "점심을 먹고 올라간 옥상 구석 벤치에 서윤이 앉아 있었다. 흡연 구역 바로 옆이었지만 손엔 종이컵뿐이었다."
    d "담배 피우세요?"
    s "아니. 끊은 것도 아니고 원래 안 피워. 여기가 이 건물에서 제일 조용해서."
    "서윤이 옆자리의 낙엽을 손으로 쓸어 냈다. 앉으라는 뜻이었다."
    s "여기 앉으면 다들 담배 피우나 보다 하고 지나가. 혼자 있고 싶은 날에 일일이 말 안 해도 되거든."
    d "그럼 제가 방해한 거네요."
    s "넌 예외. 오늘 저녁에 볼 사람이니까 예습이라고 치지 뭐."
    "바람이 불어 서윤의 머리카락이 종이컵에 닿았다. 서윤은 머리를 넘기지 않고 그냥 뒀다."
    s "나 원래 말 많은 사람 아니야. 회사에서만 많아. 조용하면 사람들이 물어보거든. 괜찮냐고."
    d "괜찮으세요?"
    "서윤이 웃음을 터뜨렸다. 이번 웃음은 평소보다 한 톤 낮았다."
    s "방금 물어봤네. ...응. 오늘은 괜찮아. 저녁에 약속 있어서."
    dn "혼자 있고 싶을 때 오는 자리라면서 날 앉혔다. 저녁까지 그 자리가 생각났다."
    $ location = "약속한 수요일 저녁 일곱 시 · 같은 북카페"
    if memory["seoyun_promise"] == "photo":
        "도현이 전날 퇴근길에 찍은 계단 사진을 보여 줬다. 저녁 빛이 난간 끝에만 남아 있었다."
        d "여기서 멈췄어요. 다 내려갔다가 빛 때문에 다시 돌아왔고요."
        s "네가 돌아선 순간은 사진 밖에 있었네. 그 말까지 챙겨 왔구나."
        "서윤이 난간 끝을 보려고 화면 가까이 몸을 기울였다. 도현이 사진을 조금 확대했다."
        s "실제로는 빛이 더 선명했어?"
        d "네. 사진으로 보니 그 느낌이 덜해서 지울까 했어요."
        s "왜 남겼어?"
        d "올라가서 다시 봤던 건 기억나니까요. 돌아보면 제가 좀 우습기도 하고."
        "서윤이 원래 크기로 보고 싶다며 화면 가장자리를 짚었다. 도현이 사진을 줄여 돌려 줬다."
        s "난 작게 볼 때가 좋네. 다 보여 주는 사진은 아니라서."
        d "보여 드리려고 고른 건데, 안 보이는 쪽으로 칭찬받네요."
        s "응. 사진만 받았으면 네가 계단을 다시 올라갔다는 건 몰랐겠지. 난 그 얘기가 더 좋아."
        $ remember("seoyun_promise_kept", "직접 찍은 난간 끝의 저녁 빛 사진과 멈춘 이유")
    elif memory["seoyun_promise"] == "sound":
        "도현은 휴대폰 메모장에 전날 돌아가는 길에 써 둔 한 줄을 보여 줬다."
        d "‘문 닫는 소리가 나면, 이 골목도 집으로 간다.’ 이 문장이요."
        s "가게는 문 닫아도 발소리는 나겠네. 그 길 궁금하다."
        "서윤이 문장을 한 번 소리 내 읽었다. 도현이 듣다가 마지막 구절에서 고개를 살짝 기울였다."
        s "왜? 내가 다른 길로 읽었어?"
        d "제가 읽을 땐 가게들이 엄청 씩씩하게 퇴근하거든요. 서윤 씨는 끝에서 좀 조용해지고요."
        s "내가 너무 쓸쓸하게 읽었나 보네. 이번엔 네가 읽어 봐."
        "도현이 한 줄을 읽었다. 서윤은 컵을 들려다 말고 웃음을 터뜨렸다."
        s "정말 퇴근하네! 문 닫는 소리까지 좀 신나겠는데~"
        d "그때 제가 빨리 집에 가고 싶었나 봐요."
        s "좋아. 방금 그 목소리로 기억할래. 잘 쓴 문장보다 목소리가 먼저 남네."
        $ remember("seoyun_promise_kept", "직접 쓴 골목 문 닫는 소리 한 줄")
    else:
        d "어젠 소파에 앉아서 창밖만 봤어요. 폰도 멀리 두고요. 뭘 가져와야 하나 싶다가 그냥 쉬었어요."
        s "그래서 어땠어?"
        d "처음엔 이상했는데, 그러다 졸았어요."
        s "좋네. 푹 쉰 얘기 듣다가 내가 다 노곤해지겠다~"
        d "듣는 사람까지 재우면 얘기가 너무 재미없었던 건가요?"
        s "아니, 오늘은 그런 얘기가 듣고 싶었어. 나도 어제 책만 펴 놓고 딴생각했거든."
        d "무슨 생각 하셨어요?"
        "서윤이 대답 대신 카페 창밖을 봤다. 도현은 같은 쪽으로 눈을 돌렸다."
        s "지금 말하면 안 되는 생각. 아직은."
        d "그럼 전 여기 보이는 거나 보고 있을게요."
        "창밖의 신호가 바뀌고 사람들이 건넜다. 도현은 지나가는 차를 보다가 서윤이 아직 자기 쪽을 보고 있는 걸 알아챘다."
        d "저쪽 보시는 줄 알았는데요."
        s "어제도 이렇게 마주 앉는 생각 했거든."
        $ remember("seoyun_promise_kept", "휴대폰을 내려놓고 창밖 보며 쉰 실제 시간 이야기")
    if memory["seoyun_r02_response"] == "wait":
        s "지난번에 기다려 달라고 했지. 좋아하는 사람 앞에선 나도 잘 말하고 싶어서 늦어져. 오늘은 그 대답부터 할게."
    elif memory["seoyun_r02_response"] == "my_interest":
        s "관심 있어서 묻는다고 했잖아. 나도 그래서 오늘 옷 한 번 더 갈아입었어. 책만 보러 온 거 아니야."
    else:
        s "멋있게 답 안 해도 듣겠다고 했지. 그럼 오늘은 대충 고른 말로. 너 오는 거, 기다렸어."
    $ progression_enter("seoyun_r03.choice01")
    $ progression_checkpoint("seoyun_r03.choice01")
    menu:
        "대답 기다릴 사람이 있어 좋았다고 한다.":
            d "오늘 오기 전에도 이 얘기 들으면 어떤 표정 지으실까 궁금했어요."
            s "그래서 지금 날 보는 중이야? 나도 네 말 끝나면 뭘 물어볼까 하고 있었는데."
            $ remember("seoyun_r03_meaning", "waiting_reader")
        "약속이라 지키고 싶었다고 한다.":
            d "만나기 전에 한 번 더 생각해 봤어요. 서윤 씨가 물어보신 거니까요."
            if memory["seoyun_promise"] == "rest":
                "서윤이 책을 펴려다가 손을 떼고 도현 쪽으로 몸을 돌렸다."
                s "아무것도 안 한 날도 잊지 않고 얘기해 줬네. 나 오늘 결과물 검사하는 사람 될 뻔했어~"
            else:
                "서윤이 도현이 보여 준 휴대폰 화면을 다시 들여다봤다."
                s "잠깐만 더 보여 줘. 약속 지켰다고 한 번 보고 끝내긴 아깝잖아."
            $ remember("seoyun_r03_meaning", "small_promise")
        "서윤 씨 보러 왔다고 말한다.":
            d "가져온 거 보여 드리러 온 것도 맞는데요. 제일 큰 이유는 서윤 씨 보고 싶어서예요."
            s "...그 말 들으니까 아까 하려던 얘기 다 까먹겠네."
            $ remember("seoyun_r03_meaning", "meet_you")
    "서윤은 가방에서 책을 꺼냈다가 다시 넣었다. 도현이 왜 그러냐는 얼굴로 보자 웃음이 새어 나왔다."
    dn "아까 펴 보기로 했던 책 같은데, 내가 먼저 묻지는 않았다."
    s "오늘은 이 얘기 하려고 가져왔거든. 근데 네가 오니까 딴 말부터 하고 싶어졌어."
    d "그럼 그 말부터 들어도 돼요."
    s "...나 지금, 너 돌아갈 시간을 자꾸 늦추고 싶어."
    d "저도 아직 갈 생각 없었어요."
    "서윤이 잔을 한쪽으로 밀어 뒀다. 둘 사이에 놓인 게 없어지자 이번엔 서윤이 도현 쪽으로 몸을 돌렸다."
    s "금요일 저녁 일곱 시에도 만날래? 이 카페에서. 그땐 내가 먼저 하고 싶은 말이 있어."
    d "네. 금요일 일곱 시요. 준비물 없이 서윤 씨 얘기 들으러 올게요."
    $ remember("seoyun_core_understanding")
    $ remember("seoyun_r04_appointment", "금요일 저녁 일곱 시, 북카페")
    s "오늘 인사할 때 잠깐 안아도 돼? 장난으로 팔 벌리는 거 말고."
    $ progression_enter("seoyun_r03.choice02")
    $ progression_checkpoint("seoyun_r03.choice02")
    menu:
        "나도라고 답하고 안는다.":
            d "네. 저도요."
            "짧게 안았다가 떨어졌다. 서윤은 다음 말을 농담으로 돌리지 않았다."
            s "오늘 와 줘서 좋았어. 금요일에도 보고 싶어."
            $ remember("seoyun_r03_affection", "hug")
        "손만 잡고 인사한다.":
            d "오늘은 손잡고 인사할래요. 금요일에도 보고 싶어요."
            "서윤이 내민 손을 잠깐 잡았다."
            s "손으로 대답하는 거, 반칙인데. ...그래도 그렇게 기억해 둘게."
            $ remember("seoyun_r03_affection", "hand")
        "오늘 반가웠다고 말로 전한다.":
            d "오늘은 말로 할게요. 만나서 좋았고, 다음에도 또 오고 싶어요."
            s "나도 보고 싶었어. 그 말까지 농담으로 받진 마~"
            $ remember("seoyun_r03_affection", "words")
    $ location = "같은 수요일 밤 · 서윤의 집 — 서윤 시점"
    "서윤은 금요일 일곱 시 옆에 도현 이름을 적었다. ‘언제 한번’은 적지 않았다."
    sn "웃어넘기는 건 쉬운데. 오늘은 웃은 것만 기억하면 곤란한데."
    dn "금요일 일곱 시. 집에 와서도 약속 시간부터 다시 확인했다."
    $ location = "다음 날 아침 · 출근길, 개인 메시지"
    call phone_deliver("seoyun_r03_m1", "seoyun", "금요일 일곱 시 수첩에 적었어\n펜으로. 연필 아니고", contact="seoyun")
    call phone_deliver("seoyun_r03_m2", "dohyun", "그게 달라요?", contact="seoyun")
    call phone_deliver("seoyun_r03_m3", "seoyun", "연필은 지울 수 있잖아\n펜으로 약속 적은 거 오랜만이야. 그러니까 늦지 마~", contact="seoyun")
    $ award_once("seoyun_R03", "seoyun", 8)
    $ progression_note_ending()
    return

label seoyun_r04:
    $ progression_enter("seoyun_r04")
    $ progression_checkpoint("seoyun_r04")
    if not memory.get("seoyun_core_understanding"):
        $ progression_note_ending()
        return
    $ chapter = "서윤 R04 · 그 말은 농담으로 하지 마"
    $ location = "전날 밤 · 각자의 집, 전화"
    "약속 전날 밤. 도현은 내일 할 말을 메모장에 적다가 지웠다. 세 번째로 지웠을 때 전화가 왔다. 서윤이었다."
    s "안 잤지? 목소리 듣고 싶어서. ...농담. 내일 몇 시였나 해서."
    d "문자로 물어보셔도 되는데요."
    s "그러게. 문자로 물어볼걸."
    "수화기 너머로 책장 넘기는 소리가 들렸다. 한참 입을 열지 않았다."
    s "이혼 얘기 한 뒤로 너, 말 고르는 시간이 길어졌어. 그게 싫다는 건 아니야."
    d "티 났어요?"
    s "고맙지. 근데 좀 겁도 나. 매번 내 눈치 보면 너부터 지칠 텐데."
    d "저도 눈치 보다가 진짜 하고 싶은 말은 못 할 때가 있어요. 오늘도 좀 그랬고요."
    s "알아. ...내일 하려는 말, 어렴풋이 알겠어. 부탁 하나만 해도 돼?"
    d "네."
    s "내일은 그 말, 농담처럼 하지 마. 나도 장난으로 돌리지 않고 들을게."
    "전화가 끊긴 뒤 도현은 메모장을 덮었다. 적어 둔 문장은 필요 없었다."
    dn "농담은 하지 말랬다. 내일 할 말은 한마디면 되겠다."
    $ location = "금요일 저녁 일곱 시 · 약속한 북카페"
    call seoyun_family_context
    d "해 주신 얘긴 기억해요. 아직 모르는 게 많아서 더 만나 보고 싶어요."
    dn "말부터 해 놓고 보니 어젯밤에 적은 문장은 하나도 안 썼다."
    s "응. 나도 이혼했단 말만 하고 정작 내 마음은 빼먹을 뻔했어. 그러니까 이번엔 그다음 얘기."
    s "내가 먼저 할게. 좋아해. 너랑 연애하고 싶어."
    $ cg("seoyun_r04")
    "서윤은 컵을 내려놓고 도현을 봤다. 웃으며 다음 화제로 넘기지 않았다."
    s "오늘은 뭐 가져왔는지 안 물어볼 거야. 내가 기다린 건 너였으니까. ...대답해 줄래?"
    while not dating and not memory.get("seoyun_relationship_declined"):
        $ progression_enter("seoyun_r04.choice01")
        $ progression_checkpoint("seoyun_r04.choice01")
        menu:
            "나도 좋아하며, 사귀자고 답한다.":
                d "저도 좋아해요. 오늘은 뭘 보여 드릴지 안 정했어요. 서윤 씨만 보러 오면 됐으니까요. 사귀어요, 우리."
                s "응. ...그 말, 그대로 듣고 싶었어."
                $ dating = True
                $ remember("seoyun_confession_accepted")
                dn "오늘은 농담 한마디 안 붙이고 말했다. 서윤 씨 눈에서 웃음기가 빠지는 게 보였다."
                $ award_once("seoyun_R04", "seoyun", 5)
            "좋아하지만 첫 연애라 겁난다고 한다." if not seoyun_prepared:
                d "저도 좋아해요. 근데 저 연애는 처음이라서요. 서윤 씨 말이 장난인지 혼자 고민하다가 대답이 늦을 수도 있어요."
                s "그땐 한 번 더 물어봐. 내가 장난처럼 말했으면 내가 다시 말할게. 네가 어떻게 다 알아듣겠어."
                d "저도 보고 싶으면 그렇게 말할게요. 서윤 씨 대답까지 미리 정하진 않고요."
                $ seoyun_prepared = True
                $ remember("seoyun_prepared_conversation")
            "이번 회차는 연애를 시작하지 않고 동료로 지낸다 — 동료 결말 확인.":
                $ progression_enter("seoyun_r04.choice02")
                $ progression_checkpoint("seoyun_r04.choice02")
                menu:
                    "동료로 지내겠다는 뜻을 확인한다.":
                        d "전 연인으로 만나겠다는 답은 못 드리겠어요. 동료로 지내고 싶어요."
                        s "알았어. 이제 와서 농담이었다곤 안 해. 네 대답도 들은 그대로 둘게."
                        $ remember("seoyun_relationship_declined")
                        call end_common
                        $ progression_note_ending()
                        return
                    "결정을 무른다.":
                        pass
                    "서윤이 원하는 걸 먼저 듣는다.":
                        s "일 없는 날에도 너 보고 싶어. 헤어질 때 다음 약속 잡는 사이로. 너도 그렇다고 서둘러 말할 건 없고."
    if not seoyun_prepared:
        d "전 첫 연애예요. 좋아한다는 말은 제가 하려고 했는데, 오늘은 대답부터 하게 됐네요."
        s "내가 먼저 해서 좋았던 것도 좀 남겨 둬~ 나도 지금 꽤 떨려."
    s "당분간은 우리만 알자. 누구한테 얘기하고 싶어지면 둘이 먼저 정하고."
    d "회사에선 조심하고 싶으신 거죠?"
    "서윤은 바로 대답하지 않았다. 컵 옆에 놓인 손을 무릎 위로 내렸다."
    s "...응. 회사에선."
    "도현이 고개를 끄덕이자 서윤은 말을 덧붙이려다가 삼켰다."
    $ remember("seoyun_publicity", "private")
    $ progression_enter("seoyun_r04.choice03")
    $ progression_checkpoint("seoyun_r04.choice03")
    menu:
        "단골 북카페를 더 보고 싶다고 한다.":
            d "내일은 그 책 있는 선반을 더 보고 싶어요. 서윤 씨랑요."
            s "응. 토요일 두 시. 이제 내 단골 자리 하나 뺏기는 건가~"
            $ remember("seoyun_next_date_plan", "bookcafe")
        "내가 궁금한 강변 길로 초대한다.":
            d "내일 두 시에 강변 입구 어때요? 이번엔 제가 궁금한 길 같이 걸어요."
            s "좋아. 내일 두 시에 강변 입구. 늦는 사람이 커피 사는 거야~"
            $ remember("seoyun_next_date_plan", "walk")
        "서점에서 만나 길은 그때 정하자고 한다.":
            d "내일 두 시에 서점에서 만나요. 걷고 싶은 길은 그때 같이 정하고요."
            s "좋아. 오늘 대답 들었다고 내일 취향까지 다 안 건 아니니까."
            $ remember("seoyun_next_date_plan", "both")
    s "잠깐만. 지금 키스해도 돼?"
    $ progression_enter("seoyun_r04.choice04")
    $ progression_checkpoint("seoyun_r04.choice04")
    menu:
        "나도라고 답하고 다가간다.":
            d "저도요."
            "얼굴이 가까워지는 순간 카페 문의 종이 요란하게 울렸다. 둘이 동시에 떨어졌다가, 서윤이 웃으며 도현의 셔츠 깃을 다시 당겼다. 이번엔 아무도 들어오지 않았다."
            s "방금 종 울릴 때 나만 놀란 줄 알았어. 너도 놀랐지?"
            $ first_kiss = True
            $ remember("seoyun_first_kiss", "R04")
            $ remember("seoyun_r04_affection", "kiss")
        "손잡고 조금 더 앉아 있자고 한다.":
            d "오늘은 손잡고 좀 더 앉아 있을래요. 물어봐 주신 건 좋았어요."
            "서윤이 손을 내밀었다. 카페가 조금 조용해질 때까지 그대로 앉아 있었다."
            $ remember("seoyun_r04_affection", "hand")
        "키스는 아끼고 말로 전한다.":
            d "오늘은 좋아한다는 말 좀 더 하고 싶어요. 키스는 다음으로 둘래요."
            s "응. 그럼 오늘은 듣는 쪽으로 욕심 좀 낼게."
            $ remember("seoyun_r04_affection", "words")
    $ remember("seoyun_r04_complete")
    $ progression_note_ending()
    return

label seoyun_route:
    $ active_route = "seoyun"
    $ cream_focus = "seoyun"
    $ phone_active_contact = "seoyun"
    call seoyun_r01
    call seoyun_r02
    call seoyun_r03
    call seoyun_r04
    if not dating or not memory.get("seoyun_r04_complete"):
        return
    call seoyun_r05
    call seoyun_o01_offer
    call seoyun_r06
    call special_scene("seoyun", 1)
    call seoyun_r07
    call seoyun_r08
    call work_mini_second
    call seoyun_r09
    call seoyun_r10
    call seoyun_o02_offer
    call seoyun_r10_after
    call seoyun_r11
    call special_scene("seoyun", 2)
    call seoyun_r12
    call seoyun_r13
    call seoyun_r14
    if dating and bond_trust("seoyun") <= BOND_BREAKUP_TRUST:
        call bond_breakup("seoyun")
    if dating and memory.get("seoyun_conflict") == "resolved":
        call seoyun_r15
        call seoyun_o03_offer
        call seoyun_r16
        if memory.get("seoyun_route_completed"):
            call seoyun_x01
            menu:
                "후일담 읽기 — 약 반년 뒤, 날짜가 있는 다음":
                    call seoyun_e01
                "본편 결말에서 마치기 — 후일담은 이번에 읽지 않음":
                    $ remember("seoyun_epilogue_skipped")
                "다음에도 보고 싶다고 말하고 후일담 읽기":
                    d "다음에도 제가 만나자고 할게요."
                    s "응. 근데 나도 보고 싶으면 연락할 거야. 그건 양보 못 해~"
                    $ remember("seoyun_epilogue_bridge")
                    call seoyun_e01
    return

label seoyun_preview:
    $ cream_preview_active = False
    "서윤 전체 대본 확인입니다. 공통의 세부 선택 기억 없이 시작합니다. 최종 그림·영상·음성은 준비 중입니다."
    call seoyun_route
    return
