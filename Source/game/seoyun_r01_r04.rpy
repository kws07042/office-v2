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
    $ location = "다음 주 수요일 오후 · 개인 메시지"
    call phone_deliver("seoyun_r01_invite", "seoyun", "‘언제 한번 보자’ 있잖아. 그거 오늘로 해도 돼? 일곱 시, 회사 앞 작은 카페.", contact="seoyun", important=True)
    call phone_deliver("seoyun_r01_accept", "dohyun", "좋아요. 일곱 시에 갈게요. 오늘은 제가 질문하는 날이죠?", contact="seoyun")
    call phone_deliver("seoyun_r01_confirm", "seoyun", "흐음, 각오했어. 오늘은 연락 담당 말고 그냥 한서윤으로 갈게.", contact="seoyun")
    $ remember("seoyun_r01_appointment", "수요일 저녁 일곱 시, 회사 앞 카페")
    $ location = "같은 수요일 저녁 일곱 시 · 회사 앞 카페"
    "커피 두 잔과 작은 쿠키 하나. 서윤은 마주 앉자마자 턱을 괴고 도현을 본다."
    if memory.get("seoyun_intro") == "humor":
        s "첫날 내 농담 받아치고 질문도 안 놓치더라. 오늘도 그 코스?"
        d "오늘은 웃는 것부터 할까 하는데요."
    elif memory.get("seoyun_intro") == "clarify":
        s "오늘도 제목이랑 본문 나눠서 말할 거야?"
        d "제목은 따로 만나서 좋다는 거요. 본문은 지금부터 들으려고요."
    elif memory.get("seoyun_intro") == "draft":
        s "첫날에 초안 소리 내서 읽던 그 배짱, 아직 있어?"
        d "있어요. 오늘은 업무 말고 제 질문에 쓸게요."
    else:
        s "늘 답장 기다리는 쪽이 나였는데. 질문 받는 자리는 좀 어색하네."
        d "저는 따로 불러 주신 게 그냥 반가운데요."
    if memory.get("c07_seoyun_next_question"):
        s "저번엔 오 분만 더 있자고 했지. 오늘은 오 분 말고 넉넉하게 빼 왔어."
    $ progression_enter("seoyun_r01.choice01")
    $ progression_checkpoint("seoyun_r01.choice01")
    menu:
        "원래 사람한테 궁금한 게 많으세요?":
            d "질문하실 때 대답을 진짜 기다리시잖아요. 원래 그러세요?"
            s "일할 땐 대답이 필요해서 기다리지. 지금은... 네가 다음에 무슨 말 할지 궁금해서. 차이 알아?"
            d "알 것 같아요. 그럼 이번엔 서윤 씨가 물어보세요. 저한테 뭐가 궁금해요?"
            "서윤이 입을 열었다가 웃음으로 닫는다. 컵받침을 손끝으로 빙글 돌린다."
            s "...혼자 마실 때도 커피를 그렇게 아껴 마셔?"
            d "아뇨. 원래는 식기 전에 다 마셔요. 오늘은 좀 아까워서요."
            s "커피가? 아니면... 응, 커피 얘기라고 해 두자."
            $ remember("seoyun_r01_topic", "curiosity")
        "쉬는 날엔 뭐 하세요?":
            d "답장 안 기다려도 되는 날은 뭐 하세요?"
            s "단골집 가서 늘 먹던 거 시켜. 먹으면서 ‘다른 거 시킬걸’ 해. 그리고 다음에 또 같은 거 시켜."
            d "오늘도요?"
            s "응. 네 접시 보니까 오늘도 졌어."
            d "한 입 바꿀래요? 대신 다음엔 서윤 씨 메뉴를 제가 정할게요."
            s "어머, 벌써 다음 메뉴까지 쥐겠다고? ...재밌네. 그거 접수."
            "서윤이 가방을 의자 안쪽으로 밀어 넣었다. 테이블 위가 조금 넓어졌다."
            $ remember("seoyun_r01_topic", "rest")
        "일 없었어도 저 부르셨어요?":
            d "오늘 업무가 하나도 없었어도 저 불렀을까요? 저는 불렸으면 했어요."
            "서윤의 손이 컵 손잡이에서 멈춘다."
            s "...와. 질문 준비해 왔네. 응, 불렀을 거야. 방금 그 말 듣고 확신했고."
            d "그럼 잘 온 거네요."
            s "근데 첫 질문에 이렇게 바로 답이 나오면 재미없잖아. 좀 버티지."
            d "다 듣고 일어날 생각은 없었어요."
            "서윤의 휴대폰에 알림이 떴다. 서윤은 짧게 답장하고 화면을 엎었다."
            d "받으셔도 돼요."
            s "친구야. 오늘 어디 가냐고. ...답했어. 오늘은 시간 넉넉해."
            s "그러니까 그때까지는 네 얘기 마저 해. 커피도 아직 반이고."
            d "제가 붙잡은 거네요."
            s "붙잡힌 척해 주는 거야. 착각은 자유고."
            $ remember("seoyun_r01_topic", "direct")
    "서윤이 설탕 통을 도현 쪽으로 슬쩍 민다. 도현은 손대지 않고 커피를 한 모금 마셨다."
    s "어? 그냥 마셔? 하나는 넣을 줄 알았는데."
    d "어떤 사람으로 보셨는데요?"
    s "단 거 주면 절대 거절 못 할 사람."
    d "주시면 먹죠. 커피에 넣는 건 아까워서요."
    "서윤이 설탕 통을 도로 끌어가 포장 하나를 뜯는다. 자기 잔에 털어 넣는다."
    s "남 취향 맞히다가 내 커피만 쓰게 마셨네. ...나 원래 이런 거 잘 맞히거든?"
    d "오늘은요?"
    s "오늘은 두 번 졌어. 메뉴랑 설탕."
    d "질문 더 하셔도 돼요. 저도 아직 남았어요."
    "도현이 팔을 테이블 위에 편하게 올렸다. 서윤은 그걸 보다가, 아주 작게 고개를 끄덕인다."
    s "그럼 두 번째 질문. 토요일에 내 단골 북카페 가 볼래? 두 시, 서점 입구."
    d "제가 엉뚱한 책 골라도 따라오실 거예요?"
    s "응. 대신 별로면 바로 말할 거야. 나 그런 건 안 참아."
    $ remember("seoyun_r02_appointment", "토요일 오후 두 시, 단골 서점 입구")
    $ award_once("seoyun_R01", "seoyun", 4)
    $ progression_note_ending()
    return

label seoyun_family_context:
    # A conversation remembered only when actually read, never inferred from old saves.
    if not memory.get("seoyun_family_disclosed"):
        "서윤이 책 사이에 손가락을 끼운 채 도현을 본다. 웃고는 있는데, 농담할 때 얼굴은 아니다."
        s "다음 약속 잡기 전에 하나만. 나 이혼했어. 삼 년 됐고, 지금은 혼자 살아."
        d "......"
        s "표정 봐. 도망갈 거면 지금이 제일 덜 민망할 때야."
        d "커피 아직 반이나 남았는데요."
        s "...그래. 전남편이랑은 연락 안 해. 같은 업계라 가끔 이름은 들리지만."
        d "그분 얘기는 서윤 씨가 하고 싶을 때 들을게요."
        s "지금 대답 하나로 다 괜찮다고 하지는 마. 이혼한 여자랑 만나는 거, 생각보다 귀찮은 일 많아."
        d "약속 말고 오늘 거 하나만요. 더 있다 가고 싶어요."
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
    $ location = "토요일 오후 두 시 · 단골 서점과 북카페"
    if c06_person == "seoyun" and c06_topic == "weekend":
        s "네가 숫자 적어 준 책갈피, 오늘도 꽂아 왔어. 진도 검사는 안 하기로 했지?"
        d "네. 대신 잘 쉬셨는지 물어보기로 했죠."
    elif c06_person == "seoyun" and c06_topic == "place":
        d "같이 오면 서로 다른 책부터 집겠다고 했잖아요. 오늘은 직접 보겠네요."
        s "응. 넌 제목 보고 웃는지부터 볼까?"
    elif c06_person == "seoyun" and c06_topic == "today":
        d "오늘도 책보다 다음 질문이 궁금해지게 해 볼게요."
        s "그 말 기억하네? 나도 오늘은 책 덮고 들을 시간 있어."
    else:
        s "여긴 책 권했다고 독후감 안 받아. 마음에 안 들면 딴 선반 가면 되고."
    "서윤이 좋아한다는 얇은 산문집 『느린 모퉁이』를 꺼냈다. 도현은 표지만 보고 옆 선반의 엉뚱한 제목을 집었다."
    d "저는 이거요. 제목만 보면 서윤 씨가 집을 줄 알았어요."
    s "벌써 날 그렇게 안다고? ...그 책, 사실 한 번도 안 읽었어."
    d "그럼 오늘 제가 틀린 거네요."
    s "응. 근데 어디까지 틀렸는지는 궁금하네. 뒤표지 한 줄만 같이 볼래?"
    "각자 집은 책의 뒷면을 읽었다. 서윤은 자기가 짐작한 도현의 취향도 빗나갔다고 순순히 인정했다."
    d "오늘은 서로 맞힌 것보다 틀린 게 많네요."
    s "다음엔 좀 더 맞히겠지. 아직 서로 모르는 게 더 많잖아~"
    d "서윤 씨는 좋아하는 사람 앞에서도 이렇게 말을 잘하세요?"
    "서윤이 책장을 넘기던 손을 멈췄다. 이번에는 바로 농담이 따라오지 않았다."
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
            d "저는 서윤 씨를 더 알고 싶어서 물었어요. 장난 아니고요."
            s "이렇게 곧장 들어오네. ...잠깐, 좋아하는 표정은 좀 숨기고 싶었는데."
            "서윤이 책을 들었다가 도로 내렸다. 도현이 웃자 이번에는 바로 받아치지 못했다."
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
            s "응. 다음엔 네가 문제 내."
            $ remember("seoyun_r02_response", "unfinished")
    call seoyun_family_context
    if not memory.get("booklet_known_seoyun"):
        d "저는 요즘 동네 사진하고 짧은 글 모아서 작은 기록집 만들고 있어요. 아직은 메모가 더 많고요."
        s "그럼 처음 보는 사람한테도 하나 들려줄래? 잘 정리한 거 말고, 네가 멈춘 순간이 궁금해."
        $ remember("seoyun_booklet_introduced")
    else:
        s "다음에는 네가 남긴 것도 하나 들려줄래? 기록집 얘기 아니어도, 네가 멈춘 순간 하나."
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
    $ award_once("seoyun_R02", "seoyun", 7)
    $ progression_note_ending()
    return

label seoyun_r03:
    $ progression_enter("seoyun_r03")
    $ progression_checkpoint("seoyun_r03")
    $ chapter = "서윤 R03 · 네가 기억했던 약속"
    $ location = "약속한 수요일 저녁 일곱 시 · 같은 북카페"
    if memory["seoyun_promise"] == "photo":
        "도현이 전날 퇴근길에 찍은 계단 사진을 보여 줬다. 저녁 빛이 난간 끝에만 남아 있었다."
        d "여기서 멈췄어요. 다 내려갔다가 빛 때문에 다시 돌아왔고요."
        s "네가 돌아선 순간은 사진 밖에 있었네. 그 말까지 챙겨 왔구나."
        "서윤이 난간 끝을 보려고 화면 가까이 몸을 기울였다. 도현이 사진을 조금 확대했다."
        s "실제로는 빛이 더 선명했어?"
        d "네. 사진으로 보니 그 느낌이 덜해서 지울까 했어요."
        s "왜 남겼어?"
        d "저기 올라가서 다시 봤다는 건 기억나니까요. 제가 좀 우스워지기도 하고."
        "서윤이 원래 크기로 보고 싶다며 화면 가장자리를 짚었다. 도현이 사진을 줄여 돌려 줬다."
        s "난 작게 볼 때가 좋네. 다 보여 주는 사진은 아니라서."
        d "보여 드리려고 고른 건데, 안 보이는 쪽으로 칭찬받네요."
        s "응. 그건 네가 옆에서 얘기해 줘야 알잖아. 사진만 보는 것보다 그게 좋아."
        $ remember("seoyun_promise_kept", "직접 찍은 난간 끝의 저녁 빛 사진과 멈춘 이유")
    elif memory["seoyun_promise"] == "sound":
        "도현은 휴대폰 메모장에 전날 돌아가는 길에 써 둔 한 줄을 보여 줬다."
        d "‘문 닫는 소리가 나면, 이 골목도 집으로 간다.’ 이 문장이요."
        s "가게 문은 닫혔는데 사람 발소리는 계속될 것 같네. 그 길, 좀 궁금해졌어."
        "서윤이 문장을 한 번 소리 내 읽었다. 도현이 듣다가 마지막 구절에서 고개를 살짝 기울인다."
        s "왜? 내가 다른 길로 읽었어?"
        d "제가 읽을 땐 가게들이 엄청 씩씩하게 퇴근하거든요. 서윤 씨는 끝에서 좀 조용해지고요."
        s "내가 너무 쓸쓸하게 읽었나 보네. 이번엔 네가 읽어 봐."
        "도현이 한 줄을 읽었다. 서윤은 컵을 들려다 말고 웃음을 터뜨렸다."
        s "정말 퇴근하네! 문 닫는 소리까지 좀 신나겠는데~"
        d "그때 제가 빨리 집에 가고 싶었나 봐요."
        s "좋아. 방금 그 목소리로 기억할래. 잘 쓴 문장보다 목소리가 먼저 남네."
        $ remember("seoyun_promise_kept", "직접 쓴 골목 문 닫는 소리 한 줄")
    else:
        d "어제는 소파에 앉아서 창밖만 봤어요. 폰도 멀리 두고요. 뭘 가져와야 하나 싶다가 그냥 쉬었어요."
        s "그래서 어땠어?"
        d "처음엔 이상했는데, 그러다 졸았어요."
        s "좋네. 푹 쉰 얘기 듣다가 내가 다 노곤해지겠다~"
        d "듣는 사람까지 재우면 얘기가 너무 재미없었던 건가요?"
        s "아니. 오늘은 그런 얘기가 듣고 싶었어. 나도 어제 책 펴 놓고 한참 딴생각했거든."
        d "무슨 생각 하셨어요?"
        "서윤이 대답 대신 카페 창밖을 봤다. 도현도 같은 쪽으로 시선을 옮겼다."
        s "지금 말하면 안 되는 생각. 아직은."
        d "그럼 저는 여기 보이는 거나 보고 있을게요."
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
            s "그래서 지금 보고 있어? ...나도 네 얘기 끝나면 뭐 물어볼지 생각하던 참인데."
            $ remember("seoyun_r03_meaning", "waiting_reader")
        "약속이라 지키고 싶었다고 한다.":
            d "만나기 전에 한 번 더 생각해 봤어요. 서윤 씨가 궁금해하셨으니까요."
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
    s "오늘은 이 얘기 하려고 가져왔거든. 근데 네가 오니까 딴 말부터 하고 싶어졌어."
    d "그럼 그 말부터 들어도 돼요."
    s "...나 지금, 너 돌아갈 시간을 자꾸 늦추고 싶어."
    d "저도 아직 갈 생각 없었어요."
    "서윤이 잔을 한쪽으로 밀어 두었다. 둘 사이에 놓인 게 없어지자 이번엔 서윤이 도현 쪽으로 몸을 돌렸다."
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
            s "응. 오늘 대답도 그렇게 기억해 둘게."
            $ remember("seoyun_r03_affection", "hand")
        "오늘 반가웠다고 말로 전한다.":
            d "오늘은 말로 할게요. 만나서 좋았고, 다음에도 또 오고 싶어요."
            s "나도 보고 싶었어. 그 말까지 농담으로 받진 마~"
            $ remember("seoyun_r03_affection", "words")
    $ location = "같은 수요일 밤 · 서윤의 집 — 서윤 시점"
    "서윤은 금요일 일곱 시 옆에 도현의 이름을 적었다. ‘언제 한번’은 적지 않았다."
    sn "가볍게 말하는 건 쉬운데. 이번엔 가볍게 들리지 않았으면 좋겠다."
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
    $ location = "금요일 저녁 일곱 시 · 약속한 북카페"
    call seoyun_family_context
    d "해 주신 얘기 기억해요. 모르는 건 아직 많지만, 그래서 더 만나 보고 싶어요."
    s "응. 나도 이혼했다는 말만 하고 내 마음은 빼먹을 뻔했어. 오늘은 그다음 얘기 할래."
    s "오늘은 내가 할게. 좋아해. 너랑 연애하고 싶어."
    "서윤은 컵을 내려놓고 도현을 보았다. 웃으며 다음 화제로 넘기지 않았다."
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
                $ award_once("seoyun_R04", "seoyun", 5)
            "좋아하지만 첫 연애라 겁난다고 한다." if not seoyun_prepared:
                d "저도 좋아해요. 근데 저 연애는 처음이라서요. 서윤 씨 말이 장난인지 혼자 고민하다가 대답이 늦을 수도 있어요."
                s "그땐 물어봐. 내가 농담처럼 말했으면 다시 말할게. 다 알아듣는 사람이랑 만나고 싶은 건 아니니까."
                d "네. 저도 보고 싶으면 보고 싶다고 할게요. 서윤 씨 대답을 혼자 짐작하지 않고요."
                $ seoyun_prepared = True
                $ remember("seoyun_prepared_conversation")
            "이번 회차는 연애를 시작하지 않고 동료로 지낸다 — 동료 결말 확인.":
                $ progression_enter("seoyun_r04.choice02")
                $ progression_checkpoint("seoyun_r04.choice02")
                menu:
                    "동료로 지내겠다는 뜻을 확인한다.":
                        d "저는 연인으로 만나겠다는 답은 못 드리겠어요. 동료로 지내고 싶어요."
                        s "알겠어. 마음 말한 걸 장난이었다고 바꾸진 않을게. 네 대답도 그대로 받을게."
                        $ remember("seoyun_relationship_declined")
                        call end_common
                        $ progression_note_ending()
                        return
                    "결정을 무른다.":
                        pass
                    "서윤이 원하는 걸 먼저 듣는다.":
                        s "일 없는 날에도 너랑 만나고 싶어. 다음 날짜를 같이 잡는 사이로. 그렇다고 같은 대답 하라는 건 아니야."
    if not seoyun_prepared:
        d "저는 첫 연애예요. 좋아한다는 말은 제가 하려고 했는데, 오늘은 대답부터 하게 됐네요."
        s "내가 먼저 해서 좋았던 것도 좀 남겨 둬~ 나도 지금 꽤 떨려."
    s "사귀는 건 당분간 둘만 알자. 다른 사람한테 말할 땐 같이 정하고."
    d "회사에서는 조심하고 싶으신 거죠?"
    "서윤은 바로 대답하지 않았다. 컵 옆에 놓인 손을 무릎 위로 내렸다."
    s "...응. 회사에서는."
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
            s "좋아. 이번엔 내가 따라가 볼게. 두 시에 강변 입구."
            $ remember("seoyun_next_date_plan", "walk")
        "서점에서 만나 길은 그때 정하자고 한다.":
            d "내일 두 시에 서점에서 만나요. 걷고 싶은 길은 그때 같이 정하고요."
            s "좋아. 오늘 대답 들었다고 내일 취향까지 다 안 건 아니니까."
            $ remember("seoyun_next_date_plan", "both")
    s "...잠깐만. 지금 하고 싶은 거 하나 있는데."
    $ progression_enter("seoyun_r04.choice04")
    $ progression_checkpoint("seoyun_r04.choice04")
    menu:
        "나도라고 답하고 다가간다.":
            d "저도요."
            "얼굴이 가까워지는 순간 카페 문의 종이 요란하게 울렸다. 둘이 동시에 떨어졌다가, 서윤이 웃으며 도현의 셔츠 깃을 다시 당겼다. 이번엔 아무도 들어오지 않았다."
            s "...농담은 좀 이따 해야겠다. 방금 그 종, 평생 미워할 뻔했어."
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
    call seoyun_r07
    call seoyun_r08
    call work_mini_second
    call seoyun_r09
    call seoyun_r10
    call seoyun_o02_offer
    call seoyun_r10_after
    call seoyun_r11
    call seoyun_r12
    call seoyun_r13
    call seoyun_r14
    if dating and memory.get("seoyun_conflict") == "resolved":
        call seoyun_r15
        call seoyun_o03_offer
        call seoyun_r16
        if memory.get("seoyun_route_completed"):
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
