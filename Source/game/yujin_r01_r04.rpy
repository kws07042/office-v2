# Yujin's established early route. No generated art, intimate CG or voice.
default yujin_prepared = False

label yujin_r01:
    $ progression_enter("yujin_r01")
    $ progression_checkpoint("yujin_r01")
    $ cream_focus = "yujin"
    $ chapter = "유진 R01 · 보내려던 메시지"
    $ location = "목요일 퇴근 후 · 개인 메시지"
    call phone_deliver("yujin_r01_info", "yujin", "도현 씨, 이번 주말에 작은 전시가 열려요. 그게... 같이 가고 싶어서요.", contact="yujin")
    call phone_deliver("yujin_r01_title", "yujin", "제목은 ‘오후의 온도’예요. 설명을 세 줄 썼다가 다 지웠어요. 만나서 할게요.", contact="yujin")
    $ phone_context = "yujin_r01_reply"
    $ progression_enter("yujin_r01.choice01")
    $ progression_checkpoint("yujin_r01.choice01")
    call screen office_phone(replies=[("interest", "좋아요. 유진 씨 추천이면 가야죠."), ("time", "토요일 오후 두 시 어때요?"), ("reason", "왜 이 전시예요?")])
    $ remember("yujin_r01_reply", _return)
    $ phone_context = None
    if memory["yujin_r01_reply"] == "interest":
        call phone_deliver("yujin_r01_reply", "dohyun", "좋아요. 유진 씨가 고른 거면 일단 가야죠. 뭐부터 봐요?", contact="yujin")
        call phone_deliver("yujin_r01_answer", "yujin", "입구 쪽 그림이요! ...아, 아니에요. 제가 말하면 도현 씨 감상이 제 감상이 돼 버려요. 참을게요.", contact="yujin")
    elif memory["yujin_r01_reply"] == "time":
        call phone_deliver("yujin_r01_reply", "dohyun", "토요일 오후 두 시 어때요? 그 뒤는 비워 둘게요.", contact="yujin")
        call phone_deliver("yujin_r01_answer", "yujin", "헉. 저 지금 시간을 어떻게 물어볼지 고민하던 중이었는데요. 한 문장 졌네요.", contact="yujin")
    else:
        call phone_deliver("yujin_r01_reply", "dohyun", "가고 싶어요. 근데 왜 이 전시예요?", contact="yujin")
        if c06_person == "yujin" and c06_topic == "weekend":
            call phone_deliver("yujin_r01_answer", "yujin", "지난번에 제목 보고 서로 다른 쪽 고르셨잖아요. 같은 그림 앞에서는 얼마나 다를지... 궁금해서요.", contact="yujin")
        else:
            call phone_deliver("yujin_r01_answer", "yujin", "도현 씨는 같은 걸 봐도 다른 데서 멈출 것 같아서요. 그 멈추는 데를 옆에서 보고 싶었어요.", contact="yujin")
    if memory["yujin_r01_reply"] != "time":
        call phone_deliver("yujin_r01_time", "yujin", "토요일 두 시, 입구 어때요? 사람 많아지기 전에요.", contact="yujin")
        call phone_deliver("yujin_r01_time_reply", "dohyun", "좋아요. 두 시에 입구에서 봬요.", contact="yujin")
    call phone_deliver("yujin_r01_close", "yujin", "그럼 토요일 두 시예요. ...설명하는 사람 말고, 같이 보는 사람으로 와 주세요 :)", contact="yujin", important=True)
    $ remember("yujin_r01_appointment", "토요일 오후 두 시, 작은 전시 공간 입구")
    $ remember("yujin_r01_first_contact")
    $ location = "목요일 저녁 · 도현의 집"
    dn "같이 보는 사람. 일정에 적기엔 긴 말이라 전시 제목 옆에 작게 적어 뒀다."
    $ location = "같은 목요일 저녁 · 유진의 집 — 유진 시점"
    "유진은 보낸 문장을 세 번 다시 읽었다. 달력의 토요일 칸에 작은 별을 그리고, 전시 노트 첫 장은 비워 둔다."
    yn "설명은 가서 해도 돼. 첫 감상은 그분 입으로 듣고 싶으니까."
    $ location = "같은 목요일 저녁 · 도현의 집"
    $ award_once("yujin_R01", "yujin", 4)
    $ progression_note_ending()
    return

label yujin_r02:
    $ progression_enter("yujin_r02")
    $ progression_checkpoint("yujin_r02")
    $ chapter = "유진 R02 · 오늘 코스는 제가 골랐어요"
    $ location = "토요일 오후 두 시 · 작은 전시 공간"
    "입구의 안내를 읽던 유진이 도현을 발견하고 노트를 가방에 넣었다."
    y "안 늦으셨네요. 저도 방금 왔어요. ...아, 한 바퀴 돌 만큼 방금은 아니고요."
    d "벌써 보셨어요? 저는 입구 설명도 못 읽었는데."
    y "입구만요! 첫 그림은... 같이 보려고 아껴 뒀어요."
    "작은 전시실 안으로 들어갔다. 유진은 벽을 따라 걷다가 한 그림에서 멈춘다."
    y "이 그림부터 보고 싶었어요. 색은 따뜻한데, 혼자 남은 방 같거든요."
    d "저는 누가 방금 나갔다가 돌아올 것 같은데요. 의자가 조금 비뚤어져 있어서."
    "유진이 의자 부분을 다시 봤다. 노트를 꺼내려다 손을 멈춘다."
    y "그렇게 보니까 누굴 기다리는 그림 같기도 하네요. ...혼자 왔으면 몰랐겠다."
    d "메모하셔도 돼요. 저는 좀 더 볼게요."
    "유진이 작품 아래 제목을 손으로 잠깐 가렸다. 도현이 웃자 손을 내렸다."
    y "제목 먼저 읽으면 그쪽으로만 보일까 봐요. 오늘은 힌트 없이요~"
    d "저 원래 설명부터 읽는 사람인데요."
    y "오늘 한 번만 제 방식으로 봐 주세요. 다음 그림은 도현 씨 방식으로 할게요."
    $ progression_enter("yujin_r02.choice01")
    $ progression_checkpoint("yujin_r02.choice01")
    menu:
        "유진이 짠 순서대로 따라간다.":
            $ remember("yujin_r02_plan", "follow")
            d "다음은 유진 씨 순서대로 볼까요? 이 그림 보니까 궁금한 게 생겼어요."
            y "좋아요. 그럼 바로 옆이요. 같은 방인데 빛이 달라요."
            "유진이 두 그림 사이에 서서 밝은 면과 비어 있는 면을 번갈아 가리켰다. 도현도 한 걸음 물러나 비교한다."
            $ remember("yujin_r02_seen", "같은 방의 다른 빛")
            d "이번엔 유진 씨가 처음 본 쪽에 좀 가까워졌네요."
            "도현이 한 걸음 더 물러나다 유진 옆에 나란히 섰다."
            y "어때요? 같은 방인데 창문 자리만 바꾼 것 같죠?"
            d "저는 아까보다 덜 외로워 보이네요."
            y "그 대답, 제가 짠 순서보다 좋네요."
            "유진이 두 그림 사이에서 반걸음 옮기더니 도현도 같은 자리로 불렀다."
            y "여기서 보세요. 저는 아직 왼쪽이 더 좋아요. 따뜻한데 텅 빈 거요."
            d "같이 보고도 의견은 안 바뀌네요?"
            y "네. 도현 씨랑 같이 보고 싶었던 거지, 제 편 만들려던 건 아니니까요~"
            d "그럼 다음 방에선 제가 정해 볼게요."
            y "좋아요. 저 딴 데 골라도 놀라지 마세요!"
        "창가 그림부터 보고 돌아오자고 한다.":
            $ remember("yujin_r02_plan", "window")
            d "저쪽 창가 그림도 봐도 될까요? 여기랑 빛이 이어지는 것 같아서요."
            y "네. 그러면 여기 다시 올 때 제 감상도 바뀔 수 있겠어요."
            "창가 쪽 그림의 얇은 그림자를 보고 첫 작품 앞으로 돌아왔다."
            $ remember("yujin_r02_seen", "창가의 그림자와 돌아와 본 첫 그림")
            d "아까는 의자만 봤는데, 지금은 바닥에 떨어진 빛이 보이네요."
            "유진이 돌아오는 방향으로 노트에 작은 화살표를 그렸다."
            y "이건 도현 씨 동선이요. 제 동그라미는... 안 지울래요."
            d "제 건 길이 좀 길죠?"
            y "네. 오늘은 그게 좋아요."
            "도현이 노트의 화살표를 따라 손가락을 움직이다가 첫 동그라미에서 멈췄다."
            d "여기 다시 와서 이제 끝인가요?"
            y "노트에는요. 저는 저 창문이 한 번 더 보고 싶어요."
            d "그럼 화살표를 하나 더 그어야겠네요."
            y "안 그릴래요. 여백까지 다 쓰면 다음에 적을 게 없어요~"
            "유진은 노트를 덮고 창가 그림 쪽으로 걸어갔다. 도현은 웃으며 따라갔다."
        "첫 그림 앞에 조금 더 머문다.":
            $ remember("yujin_r02_plan", "linger")
            d "저는 이 그림 좀 더 보고 싶어요. 혼자 남은 방 같다고 하신 것도요."
            y "좋아요. 저도 아직 덜 봤어요. 아까는 설명 다 끝낸 사람처럼 굴었는데~"
            "유진도 그림 쪽으로 몸을 돌렸다. 잠시 뒤에는 말보다 침묵이 길어졌다."
            $ remember("yujin_r02_seen", "첫 그림 앞에 오래 머문 시간")
            y "지금도 누가 돌아올 것 같으세요?"
            d "네. 기다리는 사람이 옆에 더 생겼고요."
            y "...그 말은 작품 설명엔 못 넣겠어요. 저한텐 좀 다르게 들려서요."
            "유진은 제목 쪽에 내려가 있던 시선을 그림으로 돌렸다. 도현은 의자 옆의 빈 공간을 짚었다."
            d "저라면 여기에 앉을 것 같아요. 창문도 보이고요."
            y "저는 맞은편이요. 문 열리는 걸 먼저 볼 수 있잖아요."
            d "그럼 저희 둘 다 앉으면 기다리는 방은 아니겠네요."
            y "그러네요. ...이제 이 그림에서 나가기가 더 싫어졌어요."
            "그림을 한 번 더 보고서야 문 쪽으로 몸을 돌렸다."
    "다음 공간으로 가려던 유진이 손을 가방 끈에서 놓는다."
    y "저... 다음 방까지 손잡고 가도 돼요? 사람 많아서 그러는 건 아니에요."
    $ progression_enter("yujin_r02.choice02")
    $ progression_checkpoint("yujin_r02.choice02")
    menu:
        "나도 잡고 싶었다며 손을 내민다.":
            $ remember("yujin_r02_touch", "hand")
            d "네. 저도 잡고 싶었어요. 유진 씨가 말해 주셨네요."
            "유진이 손을 잡았다. 문턱을 넘은 뒤에도 급하게 놓지 않았다."
            y "한 번은 제가 말해 보고 싶었어요. ...이 손으로는 노트 못 꺼내겠네요~"
            d "감상은 제가 기억할게요. 나중에 틀리면 고쳐 주세요."
        "오늘은 나란히 걷자고 한다.":
            $ remember("yujin_r02_touch", "later")
            d "말해 주신 건 좋아요. 그래도 오늘은 나란히 걷는 쪽이 좀 더 편해요."
            y "네. 그럼 다음 방에서 같이 볼 그림은 제가 정해도 돼요?"
            d "그건 듣고 싶어요."
            "손을 뻗는 대신, 다음 방의 작은 그림 앞에서 나란히 멈췄다."
        "손은 다음에, 그림 얘기를 더 하자고 한다.":
            $ remember("yujin_r02_touch", "talk")
            d "손은 다음에 잡아도 될까요? 지금은 아까 하시려던 말을 더 듣고 싶어요."
            y "네. 그럼 한 문장만 더요. 그림보다... 오늘 누구랑 왔는지가 더 오래 기억날 것 같아요."
            d "그건 저도 그래요. 한 문장 더 들은 보람이 있네요."
    "전시실을 나와 입구의 긴 의자에 잠깐 앉았다. 유진은 노트에 오늘 날짜를 적는다."
    y "다 보셨으니까 이제 제 코스 점수 주세요~"
    d "평점 남겨야 다음에도 불러 주시는 건가요?"
    y "아니요. 다음에도 와 주실지는 그냥 물어보려고요."
    d "그럼 답은 미리 드릴게요. 또 같이 보고 싶어요."
    y "...평점보다 그 말이 좋네요."
    $ remember("yujin_r02_exhibition_visited")
    $ award_once("yujin_R02", "yujin", 7)
    $ progression_note_ending()
    return

label yujin_r03:
    $ progression_enter("yujin_r03")
    $ progression_checkpoint("yujin_r03")
    $ chapter = "유진 R03 · 질문을 기억한 시안"
    $ location = "다음 주 월요일 점심 · 개인 메시지"
    if memory.get("yujin_r02_touch") == "hand":
        call phone_deliver("yujin_r03_memory", "yujin", "지난번 다음 방으로 가는 길이요. 손 놓을 때까지 노트 생각이 안 났어요. 그건 안 적어도 기억나네요.", contact="yujin")
    elif memory.get("yujin_r02_touch") == "later":
        call phone_deliver("yujin_r03_memory", "yujin", "지난번에 나란히 걷다가 같이 멈췄던 그림이요. 오늘 노트 첫 줄에 적었어요. 다음에도 보여 드리고 싶어요.", contact="yujin")
    elif memory.get("yujin_r02_touch") == "talk":
        call phone_deliver("yujin_r03_memory", "yujin", "지난번에 한 문장 더 듣고 싶다고 하셨잖아요. 오늘은 짧게 설명할 게 있어서요. 시안도... 같이 보실래요?", contact="yujin")
    else:
        call phone_deliver("yujin_r03_memory", "yujin", "오늘 다듬은 시안, 같이 보실래요? 설명 듣기 전 감상이 궁금해요.", contact="yujin")
    call phone_deliver("yujin_r03_answer", "dohyun", "좋아요. 이번에도 처음 본 느낌부터 말할게요. 점심 끝나고 잠깐 들를게요.", contact="yujin")
    $ location = "같은 월요일 오후 · 디자인 작업 공간"
    "유진이 모니터를 도현 쪽으로 돌렸다. 책상 한쪽에는 전시 때 쓰던 노트가 놓여 있었다."
    if memory.get("yujin_intro") == "flow":
        y "처음에 반대쪽에서 오는 사람은 어떻게 보냐고 하셨죠. 양쪽에서 다 확인한 시안이에요."
        d "돌아 들어오는 쪽에서도 문구가 먼저 보이네요."
        y "네. 이제 어느 쪽으로 들어와도 안내가 보여요."
    elif memory.get("yujin_intro") == "message":
        y "처음에 색보다 문구가 오래 남는다고 하셨잖아요. 이번에도 그런지 보고 싶어서요."
        d "작게 봐도 쓰는 장면이 떠오르네요. 배경도 덜 튀고요."
        y "그거 남기려고 색을 좀 뺐어요. 덜 예쁘게 하려던 건 아니고요~"
    elif memory.get("yujin_intro") == "process":
        y "처음에 제가 끝까지 고민하던 간격 물어보셨죠. 실제 크기로 놓고 다시 봤어요."
        d "문구는 읽히고 제품도 너무 작아지지 않았네요."
        y "네. 뭘 포기할지 말고, 둘 다 살릴 방법부터 찾았어요."
    else:
        y "이번엔 제가 설명하기 전에 질문부터 받아 볼래요. 어디에 눈이 제일 먼저 가세요?"
        d "안내 문구, 그다음에 입구 방향이 보여요. 읽는 순서를 잡으신 거예요?"
        y "네. 제가 생각한 순서로 읽히는지 확인하고 싶었어요."
    $ progression_enter("yujin_r03.choice01")
    $ progression_checkpoint("yujin_r03.choice01")
    menu:
        "꼭 지키고 싶던 게 뭔지 묻는다.":
            $ remember("yujin_r03_response", "intent")
            d "바꾸면서도 꼭 지키고 싶었던 건 뭐예요?"
            y "보는 사람이 어디 서 있는지요. 제가 보기 좋은 자리만 생각하고 싶진 않았어요."
            d "그럼 저는 지금 서 있는 데서 한 번 더 볼게요."
            "도현이 한 걸음 옮기자 유진도 모니터 각도를 바꿔 줬다."
        "내가 읽은 의도가 맞는지 묻는다.":
            $ remember("yujin_r03_response", "impression")
            d "길 묻기 전에 한 번 멈춰 서게 되는 시안 같았어요. 유진 씨 의도도 그쪽이에요?"
            y "네. 알아서 보이겠지 하고 넘기기 싫었어요. 멈출 틈을 하나 주고 싶었고요."
        "서로 다르게 본 곳을 짚는다.":
            $ remember("yujin_r03_response", "compare")
            d "저는 이 빈칸에서 멈췄어요. 유진 씨는 어디부터 보세요?"
            y "저는 문구요. 그래서 그 앞 빈칸을 자꾸 지나쳤나 봐요."
            d "전시 때랑 반대네요. 이번에는 제가 옆에서 다른 데를 보고 있었고요."
            y "좋네요. 제 설명 대신 해 주시는 것보다, 그런 감상이 더 궁금해요."
    "유진이 수정 창을 닫고 노트를 정리했다."
    $ location = "같은 월요일 퇴근 후 · 회사 근처 카페"
    "각자 일을 마친 뒤 회사 밖 카페에서 다시 만났다."
    y "오늘은 제 설명 많이 들으셨네요. 이제... 도현 씨가 보여 주실 거죠?"
    d "저도 보여 드릴 거 있어요. 오늘 퇴근길에 몇 장 찍어 왔어요."
    "도현이 카페로 오며 찍은 골목 사진 두 장을 차례로 보여 줬다. 유진이 휴대폰을 당겨 보기 전에 눈으로 허락을 구하자, 도현이 화면을 돌려 줬다."
    if not memory.get("booklet_known_yujin"):
        d "동네 사진이랑 짧은 글을 작은 기록집으로 묶어 보려고요. 아직 제목도 자주 바뀌어요."
        $ remember("booklet_known_yujin")
    y "제목부터 여쭤보면 오래 계실 거예요?"
    d "‘한 번 더 돌아본 골목’이요. 실제로 돌아갔거든요."
    "유진이 사진을 보다가 고개를 들어 도현을 봤다."
    y "두 사진이 거의 같은데요. 다시 찍으신 거예요?"
    d "네. 저분 지나가실 때까지 기다렸다가 한 장 더 찍었어요."
    y "그럼 저는 두 번째요. 기다렸다 찍으셨다는 것도 좋고요. 제목은 아직 지우지 마세요~"
    d "네. 첫 독자 의견으로 적어 둘게요."
    y "다음 장은 아직 안 보여 주실 거예요?"
    d "그럼 그 약속부터 잡을까요? 금요일 저녁 괜찮으세요?"
    y "네. 오늘 못 한 얘기, 그날 제가 해도 돼요?"
    d "듣고 싶어요. 일곱 시에 여기서 봬요."
    $ remember("yujin_r03_friday_appointment", "금요일 저녁 일곱 시, 회사 근처 카페")
    $ remember("yujin_core_understanding")
    $ award_once("yujin_R03", "yujin", 8)
    $ progression_note_ending()
    return

label yujin_r04:
    $ progression_enter("yujin_r04")
    $ progression_checkpoint("yujin_r04")
    if not memory.get("yujin_core_understanding"):
        $ progression_note_ending()
        return
    $ chapter = "유진 R04 · 부끄럽지만 말할게요"
    $ location = "금요일 저녁 일곱 시 · 약속한 카페"
    "유진은 앞에 둔 메뉴판을 덮었다. 도현이 앉자 인사보다 먼저 한 번 숨을 고른다."
    y "오늘은 제가 할 말 있다고 했잖아요. 좀 길어져도... 끝까지 들어 주실래요?"
    d "네. 오늘은 제가 질문을 잠깐 아낄게요."
    y "전시 다 보고 나서도 집에 가기 아쉬웠어요. 다음엔 전시 같은 핑계 없이 만나고 싶었고요."
    "유진이 손가락으로 메뉴판 모서리를 만지다가 손을 내려놓는다."
    y "도현 씨랑 연인으로 만나고 싶어요. ...이건 노트에 안 적고 왔어요."
    dn "답을 기다리는 눈을 보자 준비한 농담이 사라졌다. 다행히 하고 싶은 대답은 짧았다."
    while not dating and not memory.get("yujin_relationship_declined"):
        $ progression_enter("yujin_r04.choice01")
        $ progression_checkpoint("yujin_r04.choice01")
        menu:
            "나도 좋아한다고 답한다.":
                d "저도 좋아해요. 그날 헤어지고 또 불러 주셨으면 했어요. 다음엔 제가 만나자고 해야겠다고 생각했고요."
                y "그럼... 우리 사귀는 거 맞죠? 제가 고백해 놓고 또 확인하네요."
                d "네. 저랑 사귀어요, 유진 씨."
                $ dating = True
                $ remember("yujin_confession_accepted")
                $ award_once("yujin_R04", "yujin", 5)
            "마음은 있지만 더 얘기하고 싶다고 한다." if not yujin_prepared:
                d "저도 마음 있어요. 그런데 연애는 처음이라, 잘하려다가 혼자 짐작하고 말을 늦게 할까 봐요."
                y "저도 처음이에요. 오늘 말할 순서도 적어 왔어요. ...거의 못 지켰지만요."
                d "그 노트 보고 시험 치는 줄 알았으면 긴장했겠네요."
                y "시험이면 제가 질문을 더 잘했겠죠~ 저는 도현 씨가 뭘 원하는지도 듣고 싶어요."
                d "좋아하면 표현하고 싶어요. 서툴러도요. 오늘도 저도 좋다고 바로 말하고 싶었고요."
                y "저도요. 다음에 보고 싶으면 전시부터 안 찾을게요. 도현 씨 이름부터 누를래요."
                $ yujin_prepared = True
                $ remember("yujin_prepared_conversation")
            "이번 회차는 연애를 시작하지 않고 동료로 지낸다 — 동료 결말로 이어짐.":
                d "유진 씨 마음을 들었지만, 저는 동료로 지내고 싶어요. 연애를 시작하겠다는 답은 드릴 수 없어요."
                $ progression_enter("yujin_r04.choice02")
                $ progression_checkpoint("yujin_r04.choice02")
                menu:
                    "동료로 지내겠다는 뜻을 확인한다.":
                        y "알겠어요. 솔직하게 말해 주셔서... 괜찮아요. 오늘 제 얘기는 다른 사람한텐 하지 말아 주세요."
                        d "네. 오늘 들은 건 저만 알고 있을게요."
                        $ remember("yujin_relationship_declined")
                        call end_common
                        $ progression_note_ending()
                        return
                    "결정을 다시 고른다.":
                        pass
    y "말해 놓고 나니까... 도현 씨라고 부르는 것도 새로워요. 호칭은 그대로인데."
    d "저는 대답이 조금 늦어질 것 같아요. 부르시는 게 좋아서요."
    y "그러면 한 번 더요. 도현 씨."
    d "네, 여자친구님."
    y "...그쪽은 연습이 더 필요하겠어요!"
    if not yujin_prepared:
        d "저 사실 연애는 처음이에요. 방금 호칭도 좀 욕심냈네요."
        y "저도 처음이에요. 그건 같이 서툴러도 되겠어요. 호칭은... 다음에 한 번만 더 해 보세요~"
    $ progression_enter("yujin_r04.choice03")
    $ progression_checkpoint("yujin_r04.choice03")
    menu:
        "다음 데이트는 내가 정한다.":
            $ remember("yujin_next_date_plan", "dohyun_suggests")
            d "다음 토요일엔 제가 가 보고 싶은 데로 모실게요."
            y "좋아요. 그날은 제가 처음 보는 사람으로 갈게요."
        "가고 싶은 곳을 하나씩 가져오자고 한다.":
            $ remember("yujin_next_date_plan", "both_suggest")
            d "장소 하나씩 가져와 볼까요? 같이 보고 끌리는 쪽으로요."
            y "네. 제 후보만 두 개 되는 건... 하나로 줄여 올게요!"
        "유진 추천에 내 취향을 얹는다.":
            $ remember("yujin_next_date_plan", "yujin_suggests")
            d "유진 씨가 또 보여 주고 싶은 것도 듣고 싶어요. 이번엔 제 취향도 하나 보탤게요."
            y "좋아요. 집 가는 길에 찾아볼게요. ...사실 벌써 하나 떠올랐어요."
    $ remember("yujin_r04_next_appointment", "다음 토요일 후보, 장소와 시각은 후속 대화에서 확인")
    "카페 앞에서 인사를 나눴다. 돌아서던 유진이 도현을 한 번 더 부르고, 대답을 듣고 나서야 걸음을 옮긴다."
    $ remember("yujin_r04_complete")
    $ progression_note_ending()
    return

label yujin_early_route(through_r08=False, through_r12=False, full_route=False):
    $ active_route = "yujin"
    $ cream_focus = "yujin"
    $ phone_active_contact = "yujin"
    call yujin_r01
    call yujin_r02
    call yujin_r03
    call yujin_r04
    if memory.get("yujin_r04_complete"):
        if through_r08 or through_r12 or full_route:
            call yujin_r05
            if full_route:
                call yujin_o01_offer
            call yujin_r06
            call yujin_r07
            call yujin_r08
            if through_r12 or full_route:
                call work_mini_second
                call yujin_r09
                call yujin_r10
                if full_route:
                    call yujin_o02_offer
                call yujin_r11
                call yujin_r12
                if full_route:
                    call yujin_r13
                    call yujin_r14
                    if dating and memory.get("yujin_support_alignment_verified"):
                        call yujin_r15
                        call yujin_o03_offer
                        call yujin_r16
                        if memory.get("yujin_route_completed"):
                            menu:
                                "후일담 읽기 — 약 반년 뒤의 두 사람":
                                    call yujin_e01
                                "본편 결말에서 마치기 — 후일담은 이번에 읽지 않음":
                                    $ remember("yujin_epilogue_skipped")
                                "지금의 약속을 한 줄 더 나눈 뒤 후일담 읽기":
                                    d "다음엔 제가 부르기로 한 거, 안 잊을게요."
                                    y "네. 저도 보고 싶으면 바로 연락할게요~"
                                    $ remember("yujin_epilogue_bridge")
                                    call yujin_e01
                    "유진 대본 수록 구간을 마쳤습니다. 최종 그림·배경·음성·영상은 준비 중입니다."
                else:
                    $ ending = "yujin_r12_segment_complete"
                    "유진 R01~R12 확인 구간을 마쳤습니다."
            else:
                $ ending = "yujin_r08_segment_complete"
                "유진 R01~R08 확인 구간을 마쳤습니다."
        else:
            $ ending = "yujin_early_segment_complete"
            "유진 R01~R04 확인 구간을 마쳤습니다."
    return

label yujin_early_preview:
    $ cream_preview_active = False
    "유진 전체 대본 확인입니다. 공통 만남의 세부 기억은 없는 상태로 시작합니다."
    call yujin_early_route(full_route=True)
    return
