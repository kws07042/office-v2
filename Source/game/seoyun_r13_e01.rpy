# Seoyun route v003: divorced (no children); ex-husband is the pitch client.
label seoyun_r13:
    $ progression_enter("seoyun_r13")
    $ progression_checkpoint("seoyun_r13")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R13 · 내 대답까지 고르지 마요"
    $ location = "약속한 월요일 저녁 일곱 시 · 카페"
    "오후 미팅은 사십 분 만에 끝났다. 클라이언트 쪽 담당자가 명함을 돌릴 때, 서윤의 손이 반 박자 늦게 나갔다. 명함에는 '정민재'라고 적혀 있었다."
    "그 남자는 서윤을 '한서윤 님'이라고, 처음 보는 사람처럼 불렀다. 그리고 회의 내내 서윤이 말할 때만 펜을 내려놓았다."
    dn "서윤 씨는 미팅 내내 한 번도 장난을 치지 않았다. 끝날 때까지 농담 한마디를 기다렸다."
    "저녁 일곱 시, 카페에는 서윤이 먼저 와 있었다. 앞에 놓인 건 늘 마시던 라테가 아니라 아무것도 넣지 않은 커피였다."
    "서윤은 수첩을 펴 놓고 있었다. 오늘 오후 클라이언트 미팅 메모 위에, 이름 하나가 여러 번 줄로 그어져 있었다."
    s "오늘 미팅, 너도 봤지. 상대 쪽 담당자. ...정민재. 내 전남편이야."
    d "...이름 보고 설마 했어요. 괜찮으세요?"
    s "괜찮아. 그래서 말인데, 피칭 끝날 때까지 우리 회사 밖에서도 좀 떨어져 있자. 네가 엮이면 피곤해져."
    d "저한텐 묻지도 않고, 떨어져 있기로 정하신 거예요?"
    "서윤은 수첩 모서리를 손끝으로 꾹 눌렀다."
    s "다시 만나자고 연락 왔어. 답은 안 했어. 일하다가도 그 연락 생각이 나서, 네가 보면 더 복잡해질까 봤어."
    d "저도 지금 안 듣고 넘어가면 계속 신경 쓰여요. 피칭 끝날 때까지 저만 모르는 건 싫어요. [memory.get('seoyun_private_name', '서윤 씨')]가 직접 얘기해 주셨으면 좋겠어요."
    "서윤의 휴대폰이 탁자 위에서 짧게 울렸다. 화면에 뜬 이름을 도현도 보았다. 서윤은 받지 않고 화면을 엎었다."
    s "봤지. 저래. 삼 년 동안 한 번도 안 하던 연락을, 클라이언트가 되니까 해."
    dn "그 남자가 또 무슨 말을 했을까. 물어보려는데 목에서 소리가 안 나왔다."
    $ face("seoyun", "teary")
    s "못나게 구는 거 알아. 근데 네가 그 사람 눈에 안 띄었으면 좋겠어. 내가 아끼는 걸 어떻게 흔들어야 하는지 잘 알거든."
    $ face("seoyun")
    $ remember("seoyun_conflict", "open")
    $ remember("seoyun_dismissed_request", "전남편이 피칭 상대로 나타나자 도현에게 묻기 전에 거리를 두기로 혼자 정함")
    $ progression_enter("seoyun_r13.choice01")
    $ progression_checkpoint("seoyun_r13.choice01")
    menu:
        "전남편 일로 날 밀어내지 말라고 한다.":
            d "그분이 무슨 연락을 하든, 저까지 밀어내는 건 [memory.get('seoyun_private_name', '서윤 씨')] 혼자 정할 일이 아니에요."
            s "응. 내가 네 대답까지 미리 정했네. 그건 미안해."
            $ remember("seoyun_r13_response", "weight")
            dn "맞는 말만 골랐는데 서윤 씨는 수첩을 덮었다. 나까지 저 사람처럼 들렸나."
        "무슨 일인지부터 듣겠다고 한다.":
            d "떨어져 있자는 말은 나중에 해도 돼요. 지금은 무슨 일이 있었는지부터 들을래요."
            s "...결론부터 던졌네, 내가. 제일 싫어하는 방식인데."
            $ remember("seoyun_r13_response", "unknown")
        "잠깐 생각을 정리하고 말한다.":
            d "저도 안 어려울 거라고는 못 해요. 잠깐만 생각하고 대답할게요."
            "도현이 컵을 내려놓았다. 서윤은 수첩을 덮지 않고 기다렸다."
            d "기다릴 수 있는 건 기다린다고 할게요. 근데 아무 일 없는 척은 못 하겠어요."
            s "알았어. 네가 멈췄다고 싫다는 뜻으로 받진 않을게. ...헷갈리면 바로 물어볼게."
            $ remember("seoyun_r13_response", "pause")
    s "이혼하고 혼자 잘 지냈어. 그 사람이 다시 나타나니까 너까지 거기 끌려들어오는 기분이었어."
    d "그 얘기 듣고 솔직히 저도 겁나요. 그래도 [memory.get('seoyun_private_name', '서윤 씨')]한테서 직접 듣고 싶어요."
    $ cg("seoyun_r13")
    "서윤이 수첩을 접었다. 탁자 위엔 컵 두 개만 남았다."
    s "보고 싶어. 앞으로도. ...그 말부터 했어야 했네."
    d "저도요. 그다음에 그 사람 얘기, 다 해 주세요."
    if memory.get("seoyun_publicity") == "told_yujin":
        s "유진이한테 우리 만난다고 말할 때도 같이 정했지. 정작 너한텐 혼자 답하려고 했네."
    else:
        s "사귀는 걸 누구한테 알릴지도 같이 정했는데. 우리 얘기는 나 혼자 끝내려고 했네."
    s "수요일에 다시 볼래? 그때까지 그 사람한테 할 대답도 정해 갈게."
    d "네. 저도 며칠 그냥 떨어져 있으면 괜찮을지 생각해 볼게요."
    $ remember("seoyun_future_question_status", "전남편과의 일을 숨기지 않고 수요일에 다시 이야기하기로 함")
    $ remember("seoyun_trust_status", "needs_mutual_discussion")
    $ remember("seoyun_conflict", "discussing")
    $ award_once("seoyun_R13", "seoyun", 0)
    $ progression_note_ending()
    return

label seoyun_r14:
    $ progression_enter("seoyun_r14")
    $ progression_checkpoint("seoyun_r14")
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "discussing":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R14 · 두 사람 몫의 대답"
    $ location = "같은 월요일 저녁 · 카페"
    s "난 수요일 일곱 시에 여기 올 수 있어. 넌 어때? 지금 정하기 싫으면 나중에 말해도 돼."
    $ progression_enter("seoyun_r14.choice01")
    $ progression_checkpoint("seoyun_r14.choice01")
    menu:
        "수요일에 다 얘기하자고 한다.":
            d "수요일에 봐요. 그날은 몇 시에 볼지만 말고, 우리 둘이 뭘 하고 싶은지도 얘기해요."
            s "응. 나도 그건 달력 안 보고 대답할 수 있어."
            $ remember("seoyun_r14_choice", "ready")
        "어려운 것도 말하자고 한다.":
            d "저도 싫은 건 싫다고 할게요. 그게 서윤 씨가 싫다는 뜻은 아니에요."
            s "응. 나도 부탁할 때 먼저 물어볼게. 네 대답 듣기 전에 결론 내리지 않고."
            $ remember("seoyun_r14_choice", "repair_blunt")
        "연애를 마치자고 한다 — 관계 종료 확인.":
            $ progression_enter("seoyun_r14.choice02")
            $ progression_checkpoint("seoyun_r14.choice02")
            menu:
                "관계 종료를 확정한다.":
                    d "좋아해요. 그래도 제가 바라는 사이하고는 달라요. 사귀는 건 여기서 그만하고 싶어요."
                    s "알겠어. 네가 날 감당 못 했다고 멋대로 생각 안 할게. 수요일 약속도 잡지 말자."
                    $ dating = False
                    $ remember("seoyun_relationship_closed")
                    $ ending = "seoyun_relationship_closed"
                    "인사하고 카페를 나왔다. 사적인 다음 약속은 잡지 않았다."
                    $ progression_note_ending()
                    return
                "끝내자는 말을 거둔다.":
                    d "끝내겠단 말은 취소할게요. 서로 생각을 더 듣고 싶어요."
                    s "취소? ...좋아. 근데 다음 대답까지 미리 받은 걸로는 안 칠게. 그건 수요일에 네 입으로 다시 들을래."
                    $ remember("seoyun_r14_choice", "reconsidered")
                "수요일 얘기를 듣고 정하겠다고 한다.":
                    d "지금은 결정하지 않을게요. 수요일엔 제 마음도 말할래요."
                    s "응. 그날 네 말도 듣고 내 말도 할게. 여기서 다시 봐."
                    $ remember("seoyun_r14_choice", "wait_action")
                    dn "답을 준비한다던 서윤 씨는 컵만 봤다. 수요일까지 기다리는 수밖에."
    $ remember("seoyun_repair_appointment", "수요일 저녁 일곱 시, 전남편 연락과 피칭, 둘의 관계를 숨김없이 이야기")
    $ remember("seoyun_conflict", "agreed_pending_action")
    "카페를 나서자 찬 바람이 불었다. 서윤은 평소처럼 팔짱을 끼려다, 길 건너 클라이언트사 건물을 보고 손을 주머니에 넣었다."
    s "미안. 오늘은 여기까지만. 저 건물 불 꺼질 때까진... 아직 좀 그래."
    d "알아요. 대신 수요일엔 주머니 말고요."
    s "...말은 잘해."
    "서윤이 처음으로 웃었다. 금방 사라지는 웃음이었다. 도현은 그 뒷모습이 골목을 돌 때까지 서 있었다."
    dn "저 건물은 나도 매일 보는데, 오늘부터는 그냥 지나가기가 좀 어려울 것 같았다."
    $ location = "같은 날 밤 · 각자의 집, 개인 메시지"
    call phone_deliver("seoyun_r13_m1", "seoyun", "아까 길에서 미안\n그 건물 앞에서 손이 먼저 움직이더라. 팔짱 낄 뻔한 거 봤지", contact="seoyun")
    call phone_deliver("seoyun_r13_m2", "dohyun", "봤어요. 반쯤 낀 거, 전 좋았어요", contact="seoyun")
    call phone_deliver("seoyun_r13_m3", "seoyun", "...그렇게 말하지 마\n수요일까지 버티기로 한 거 흔들려", contact="seoyun")
    $ location = "화요일 오후 · 클라이언트사 회의실"
    "클라이언트사 회의실. 정민재는 서윤보다 먼저 와서 서윤의 자리 앞에 커피를 놓아 뒀다."
    "“예전처럼 시럽 두 번.” 그가 웃으며 말했다. 서윤은 커피를 옆으로 밀어 두고 자료부터 펼쳤다."
    s "시안 설명 드리겠습니다. 질문은 끝나고 받을게요."
    "회의 내내 서윤은 한 번도 웃지 않았다. 대신 도현은 정민재가 서윤을 부를 때마다 이름 대신 예전 호칭이 튀어나오는 걸 세 번 들었다."
    "질문을 받는 동안, 탁자 위 노트북 구석에 사내 메신저가 떴다. 서윤은 화면에서 눈을 떼지 않은 채였다."
    call pc_chat("seoyun", [("seoyun", "표정 관리."), ("dohyun", "하고 있어요."), ("seoyun", "너 말고 나. ...나 하고 있는 거 맞지?"), ("dohyun", "네. 자료는 여기까지 확인했습니다.")])
    dn "회의 자료보다 그 호칭이 더 오래 귀에 남았다."
    $ location = "화요일 밤 · 개인 메시지"
    call phone_deliver("seoyun_r14_tue", "seoyun", "아까 회의에서 내 얘기 꺼내는 거 듣고 많이 당황했지\n내일 만나서 얘기할게", contact="seoyun")
    $ location = "같은 화요일 밤 · 각자의 집, 전화"
    "메시지를 받고 한 시간쯤 지나서, 열한 시에 전화가 왔다. 수요일까지 하루가 남은 밤이었다."
    s "자?"
    d "아니요."
    s "나 지금 그 사람 번호 차단할까 말까 삼십 분째 보고 있어."
    d "차단하고 싶어요?"
    s "응. 근데 아직 내 개인 번호로도 일 얘기를 해. 그쪽 팀에는 회사 메일로만 달라고 먼저 알려야겠어."
    "수화기 너머로 서윤이 숨을 길게 내쉬었다."
    s "그 사람 때문에 너한테 떨어져 있으라고 한 거. 그게 제일 한심했어. 왜 네가 움직여야 해."
    d "저도 아까 회의실에서 한마디 하려다가 못 했어요."
    s "겁난 거 맞아. 오래 알던 사람이야. 내가 어디를 누르면 무너지는지 알아."
    d "그 얘기 또 나오면 제가 먼저 화낼 수도 있어요. 그래도 들은 척 안 하고 넘기진 않을게요."
    "한참 답은 없었다. 그러다 작게 웃는 소리가 났다."
    s "...너 그런 말을 어디서 배웠어."
    d "월요일에 [memory.get('seoyun_private_name', '서윤 씨')]랑 헤어질 때 하고 싶었던 말이에요. 그때는 입이 안 떨어졌어요."
    s "잘 배웠네. 내일 일곱 시. 이번엔 안 도망가."
    dn "전화를 끊고 나서야 손에 땀이 찬 걸 알았다. 내일 들을 대답이 뭐가든, 오늘 밤 서윤 씨는 혼자 있지 않았다."
    $ location = "약속한 수요일 저녁 일곱 시 · 같은 카페"
    "서윤은 수첩을 가방에 넣은 채 먼저 와 있었다. 도현이 앉자 메뉴판보다 얼굴부터 봤다."
    s "답장 보냈어. 다시 만날 생각 없다고. 난 너랑 만나고 싶어. 책 얘기에 네가 웃다가, 또 잠자코 걷다가. 그렇게."
    d "다행이에요. 월요일부터 그 생각만 했거든요. ...회의실에서 그분 마주치면 얼굴에 다 나올 텐데요."
    s "피칭에선 일 얘기만 할게. 또 따로 보자고 하면 내가 거절할 거야."
    d "저도 회의에선 그냥 TF 막내로 있을게요. 대신 끝나고는 [memory.get('seoyun_private_name', '서윤 씨')] 옆자리 제 거예요."
    s "다시 만나자는 연락, 바로 말 안 해서 미안해. 네가 날 보면 이혼했다는 말만 생각날까 봐."
    d "전 한서윤 씨를 보는 거예요. 앞에 뭐가 붙든 상관없어요."
    s "...그 말은 좀 세네. 피칭만 끝나면 내가 그 사람 이름 꺼낼 일은 없어."
    "서윤이 컵을 들었다가 내려놓았다. 이번엔 말을 보태려던 도현을 기다려 줬다."
    d "그리고 둘이 놀러 가고 싶은 데도 하나씩 말해요. 어려운 얘기만 하는 연인은 싫어요."
    s "...나 지금 네가 시킬 디저트가 궁금해. 그건 오늘 물어봐도 되지?"
    d "네. 이번엔 레몬 말고 다른 걸로요."
    "서윤이 웃었다. 도현은 메뉴판을 가운데로 옮겼다."
    $ remember("seoyun_repair_performed", "수요일 실제 대면에서 전남편의 재회 요청을 거절했다고 밝히고 피칭과 연애를 분리하기로 함")
    $ remember("seoyun_mutual_plan_performed")
    $ remember("seoyun_future_boundary_confirmed")
    $ progression_enter("seoyun_r14.choice03")
    $ progression_checkpoint("seoyun_r14.choice03")
    menu:
        "피칭이 끝날 때까지 기다리지 않고 계속 만난다.":
            d "피칭 끝날 때까지 떨어져 있는 거 말고, 지금부터 계속 만나요."
            s "응. 회의실에선 모르는 척, 끝나면 바로 네 쪽."
            $ remember("seoyun_continues_after_discussion")
        "이야기는 들었지만 여기서 끝낸다.":
            d "생각 말해 주셔서 고마워요. 그래도 전 지금 이 관계를 이어가기는 어려울 것 같아요."
            s "응. 솔직하게 답해 준 거, 그대로 받을게."
            $ dating = False
            $ remember("seoyun_relationship_closed")
            $ ending = "seoyun_relationship_closed"
            "인사하고 각자 일어났다. 새로운 사적 약속은 잡지 않았다."
            $ progression_note_ending()
            return
        "아직 어려워도 계속 만난다.":
            d "그분 일이 다 끝난 건 아니란 거 알아요. 그래도 계속 만나 보고 싶어요."
            s "나도. 오늘 한 얘기 중에 마음에 걸리는 게 생기면 그때 다시 말해 줘. 나도 그럴게."
            $ remember("seoyun_continues_after_discussion")
            $ remember("seoyun_future_discussion_open")
    $ remember("seoyun_conflict", "resolved")
    $ remember("seoyun_future_question_status", "전남편 문제를 공유하고 교제 지속, 피칭 뒤 공개 여부는 별도 논의")
    $ remember("seoyun_trust_status", "mutual_answers_confirmed")
    if memory.get("seoyun_r14_choice") == "wait_action":
        $ remember("seoyun_continuation_reconfirmed")
    s "금요일 일곱 시, 같이 저녁 먹을래? 그날 시간은 맞춰 뒀어. 장소는 네가 골라 주면 좋겠어."
    d "좋아요. 저 먹고 싶은 데 하나 있어요."
    $ remember("seoyun_r15_appointment", "금요일 저녁 일곱 시 함께 식사")
    dn "이젠 정민재 이름을 입에 올린다. 그럴 때면 서윤 씨 손이 내 손을 찾는다."
    $ award_once("seoyun_R14", "seoyun", 8)
    $ progression_note_ending()
    return

label seoyun_r15:
    $ progression_enter("seoyun_r15")
    $ progression_checkpoint("seoyun_r15")
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "resolved":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R15 · 다음 금요일은 우리 약속"
    $ location = "목요일 오후 · 회의 공간"
    j "도현 씨, 알고 있어? 클라이언트 담당자가 서윤 씨 개인 번호로 연락하는 거."
    d "...네. 들었습니다."
    j "업무 연락은 공식 채널로만 받겠다고 내 이름으로 메일 보냈어. 서윤 씨가 부탁한 건 아니야. 팀장이 할 일이라서."
    "지현은 보낸 메일 화면을 닫았다."
    j "서윤 씨도 참조에 넣었어. 다시 개인 번호로 오면 답장하지 말고 나한테 전달해 달라고 했고."
    dn "내가 전해 드려야 하나 했는데 벌써 메일이 가 있었다. 이제 개인 전화에 바로 답할 일은 없겠네."
    $ location = "약속한 금요일 저녁 일곱 시 · 식당"
    "서윤은 먼저 와서 메뉴판을 보고 있었다. 도현이 들어오자 자기 옆 빈 의자를 손으로 가리켰다."
    dn "맞은편 자리를 놔두고 제 옆을 짚었다. 오늘은 저기구나."
    s "오늘은 맞은편 말고 여기. 네 접시가 더 맛있어 보이면 바꾸기 편하잖아~"
    d "주문하기도 전에 노리시는 거예요?"
    s "응. 네가 고른 가게라길래 기대치 좀 올려 왔어. 책임져~"
    "도현은 외투를 벗고 앉았다. 서윤이 펼친 목록에는 위스키 이름들이 적혀 있었다."
    s "난 이 향이 좋아. 바닐라 같다가 끝엔 나무 향이 남거든. 너도 작은 잔으로 한 번 맛볼래?"
    d "네. 한 잔만요. 음식은 제가 시켜 볼게요."
    "각자 작은 위스키 한 잔과 음식을 주문했다. 첫입을 먹은 서윤이 도현 쪽을 보고 포크를 잠깐 멈췄다."
    s "내 쪽도 맛있는데 네 표정이 더 맛있어 보이네."
    d "한 입 바꾸실래요? 아까 자리 고르신 이유도 있고요."
    "작은 접시에 한 입씩 덜었다. 바꿔 먹고 나서도 서윤은 자기 접시로 바로 돌아가지 않았다."
    s "오늘 장소는 네가 이겼다."
    d "다음에도 제가 정해도 되는 거죠?"
    s "응. 대신 내 차례도 남겨 둬."
    "식사를 마치고 물을 시켰다. 서윤이 휴대폰 달력을 가운데로 놓았다."
    $ progression_enter("seoyun_r15.choice01")
    $ progression_checkpoint("seoyun_r15.choice01")
    menu:
        "보고 싶다는 마음엔 날짜를 붙이자고 한다.":
            d "다음에도 제가 보고 싶다고 할게요. 언제 시간 되는지도 같이 물을게요."
            s "다음 금요일 일곱 시는 어때? 네 일정도 보고 답해 줘."
            d "좋아요. 그날은 제가 궁금한 가게 하나 더 가져올게요."
            $ remember("seoyun_future_promise", "다음 금요일19시, 서로의 일정을 확인한 뒤 만남 확정")
        "아직 못 정한 건 다시 얘기할 날을 잡자고 한다.":
            d "회사에 알리는 얘기는 오늘 정하지 말고, 피칭 끝나고 다시 해요."
            s "응. 피칭 끝난 다음 주 토요일 두 시 어때? 그때도 아직이면 아직이라고 말하고."
            d "좋아요. 저도 제 생각을 가져올게요."
            $ remember("seoyun_future_promise", "피칭 끝난 다음 주 토요일 14시, 회사와 친구들에게 알릴지 다시 이야기")
        "나도 힘들면 말하겠다고 한다.":
            d "저도 쉬고 싶은 날엔 말할게요. 오늘은 반대예요. 좀 더 같이 있고 싶어요."
            s "그 말 기다렸어. 나도 계산하고 바로 헤어지긴 아까웠거든."
            $ remember("seoyun_future_promise", "서로 쉬는 시간과 함께 있고 싶은 마음을 먼저 말하기")
    $ location = "같은 금요일 저녁 · 서윤의 작업실"
    "피칭 전 마지막 주말이었다. 천천히 걸어 서윤의 개인 작업실에 들렀다."
    "서윤이 물 두 잔을 놓았다. 도현은 가방을 의자 옆에 내려놓고 앉았다."
    s "여기 두고 입는 편한 옷도 있고, 광고 촬영 끝나고 소품으로 받아 둔 의상도 몇 벌 있어. 지금 보여 줄까?"
    $ progression_enter("seoyun_r15.choice02")
    $ progression_checkpoint("seoyun_r15.choice02")
    menu:
        "편한 생활복으로 쉬자고 한다.":
            d "오늘은 편하게요. 같이 앉아 있는 게 좋아요."
            $ remember("seoyun_r15_outfit", "home")
        "촬영 소품 의상이 보고 싶다고 한다.":
            d "[memory.get('seoyun_private_name', '서윤 씨')]도 입어 보고 싶으시면 저도 궁금해요."
            s "내가 보여 주고 싶어서 꺼낸 거야~ 세 벌 중에 골라 봐."
            $ remember("seoyun_r15_outfit", "cosplay")
            menu:
                "바니걸":
                    $ remember("seoyun_r15_costume", "bunny")
                    s "역시 이걸 고를 줄 알았어. 웃으면 다시 벗는다? ...진짜 웃네."
                "간호사":
                    $ remember("seoyun_r15_costume", "nurse")
                    s "아픈 데 있으면 말해. 오늘은 장난 말고 성실하게 봐 줄게~"
                "여경찰":
                    $ remember("seoyun_r15_costume", "police")
                    s "도현아, 묻는 말에만 대답해. 오늘 나 보고 싶었어?"
        "서윤에게 고르게 한다.":
            s "그럼 오늘은 생활복. 갈아입는 동안 네가 무슨 표정일지부터 궁금하네."
            d "여기서 기다리고 있을게요."
            $ remember("seoyun_r15_outfit", "home")
    if memory.get("seoyun_r15_outfit") == "cosplay":
        "서윤이 고른 의상으로 갈아입고 돌아왔다. 도현이 옆자리를 비우자 서윤은 웃으며 앉았다."
    else:
        "서윤이 생활복으로 갈아입고 돌아왔다. 도현이 옆자리를 비우자 서윤은 웃으며 앉았다."
    s "오늘 내가 뭘 했을 때 네가 제일 좋아했는지 궁금한데."
    d "메뉴 기다리는 동안 [memory.get('seoyun_private_name', '서윤 씨')]가 제 쪽으로 의자 당기신 거요."
    s "...그건 못 봤을 줄 알았는데."
    d "저도 좀 당겼어요."
    "서윤이 두 의자 사이를 보고 웃었다. 잠깐 뒤엔 도현 눈을 마주 봤다."
    s "오늘은 여기서 더 같이 있고 싶어. 네 마음도 듣고 싶고."
    call seoyun_private_evening("r15", memory["seoyun_r15_outfit"])
    dn "우리 약속. 서윤 씨가 '우리'라는 말을 이렇게 쉽게 한 건 처음이다."
    $ award_once("seoyun_R15", "seoyun", 5)
    $ progression_note_ending()
    return

label seoyun_r16:
    $ progression_enter("seoyun_r16")
    $ progression_checkpoint("seoyun_r16")
    if not dating or active_route != "seoyun" or memory.get("seoyun_conflict") != "resolved" or "seoyun_R15" not in completed:
        $ progression_note_ending()
        return
    $ chapter = "서윤 R16 · 함께 고르는 다음"
    $ location = "피칭 전날 밤 · 서윤의 작업실"
    "피칭 전날 밤. 서윤의 작업실 벽에 예상 질문이 적힌 종이가 줄지어 붙어 있었다. 맨 끝 종이만 제목이 달랐다. '그 사람이 물을 것'."
    s "앉아. 네가 정민재야. 제일 못되게 물어봐."
    d "제가 그분을 잘 모르는데요."
    s "쉬워. 웃으면서 상대가 제일 자신 없는 데를 찌르면 돼. 내가 오래 봤어."
    "도현은 종이를 한 장 떼어 읽었다."
    d "'한서윤 님, 이 카피는 지나치게 감상적이지 않습니까. 개인적인 경험이 반영된 건가요?'"
    "서윤의 어깨가 움찔했다. 연습인 줄 알면서도."
    s "...그 사람이면 진짜 그렇게 물어. 다시."
    "같은 질문을 다섯 번 반복했다. 서윤의 대답은 처음엔 변명 같았고, 세 번째엔 화가 섞였고, 다섯 번째에야 평소의 목소리가 됐다."
    s "‘퇴근길에 들르는 분들을 대상으로 썼습니다. 현장에서 짧게 읽히는지도 확인했습니다.’"
    d "...그 대답이면 됩니다."
    s "됐어? 진짜?"
    d "정민재 말고 도현으로 대답하면, 멋있었어요."
    "서윤이 벽의 종이들을 등지고 도현 쪽으로 돌아앉았다."
    s "내일 그 사람 앞에서 네 팔 잡아도 돼? 보여 주려고 그러는 건 아니야. 그냥 네가 옆에 있는 걸 좀 알고 싶어."
    d "잡으세요. 처음부터 그 자리에 있을게요."
    dn "내 앞에서만 다섯 번을 했다. 내일 그 사람 앞에 서도 저 말이 나오면 좋겠다."
    $ location = "피칭 당일 · 클라이언트사 대회의실"
    "발표를 시작하려는 참에, 심사석 가운데 남자가 펜을 내려놓았다. \"하나만 묻겠습니다. 이 팀, 석 달 뒤에도 있습니까?\""
    "회의실이 조용해졌다. 그때 책상 아래에서, 누군가 도현의 손등을 한 번 눌렀다. 서윤이었다. 서윤은 심사석도 도현도 보지 않은 채 정면을 향했다."
    "지현이 대답하려고 몸을 일으키는 사이, 서윤이 먼저 마이크를 당겼다."
    s "있을 겁니다. 현장과 디자인, 카피 담당이 확정돼 있고, 피칭 뒤 수정과 운영까지 같은 팀에서 맡을 예정입니다."
    dn "정민재가 묻자 내 손부터 잡았다. 서윤 씨가."
    "서윤은 심사석 쪽을 한 번도 보지 않고 첫 장을 띄웠다."
    dn "심사석의 정민재. 서윤 씨는 그쪽을 보지 않았지만, 난 그 사람이 서윤 씨만 보고 있다는 걸 알았다."
    s "카피부터 설명드리겠습니다. 이번 캠페인은 ‘짧게 쓰되 하나도 빼지 않는다’는 요청에서 출발했습니다."
    "질의응답 시간, 정민재가 마이크를 당겼다. “한서윤 씨는 예전부터 마감 직전에 다 바꾸는 스타일 아니었나요? 이번 안도 그런 건 아닌지.”"
    "회의실 공기가 굳었다. 리아가 도현의 팔을 툭 쳤다. 도현이 손을 들려는 순간, 서윤이 먼저 웃었다."
    s "마감 직전에 바꾸던 건 예전 얘기고요. 이번 안은 현장 확인을 세 번 거쳐 고정했습니다. 수정 이력은 도현 씨가 정리해 두었어요."
    "도현이 이력 자료를 넘겼다. 정민재가 처음으로 도현을 제대로 봤다."
    s "이번 안의 수정 이력은 여기까지입니다. 시안에 대해 더 궁금한 점 있으실까요?"
    $ location = "피칭 당일 저녁 · 클라이언트사 엘리베이터 앞"
    "엘리베이터를 기다리는 동안 결과 연락이 왔다. TF가 이겼다."
    "엘리베이터 앞에서 정민재가 서윤을 불러 세웠다. 도현은 몇 걸음 떨어져 기다렸다. “그 사람이야?”"
    s "응. 그 사람이야."
    $ cg("seoyun_r16")
    "서윤은 대답을 마치자마자 돌아서서 도현에게 걸어왔다. 그리고 정민재가 보는 앞에서 도현의 팔짱을 꼈다."
    s "가자, 도현아. 오늘 저녁은 내가 살게. 시럽 없는 걸로."
    $ cream_focus = "seoyun"
    $ location = "일요일 저녁 · 북카페"
    "서윤이 다음 제안서의 담당란을 보여 줬다. 이번 업무에서 범위 설명을 직접 맡기로 한 자료였다."
    s "이건 내 소식. 이제 네 거 보여 줘."
    "서윤이 자료를 접어 가방에 넣었다."
    "도현은 [memory['seoyun_private_name']]와 함께 골랐던 '[memory['seoyun_booklet_sentence']]'을 넣은 얇은 초안을 잠깐 보여 줬다."
    s "내가 읽고 싶다던 쪽이네. 이건 완성되면 한 부 꼭 줘."
    "서윤은 종이를 덮고 도현 옆자리로 옮겨 앉았다."
    s "그때까지 오늘은 사람 쪽을 더 볼래."
    d "좋아요. 저도 가까이 앉으신 게 좋아서요."
    $ remember("seoyun_booklet_state", "직접 쓴 문장을 남긴 새 초안, 최종 인쇄 전")
    $ progression_enter("seoyun_r16.choice01")
    $ progression_checkpoint("seoyun_r16.choice01")
    menu:
        "같이 걸은 데를 다시 걷자고 한다.":
            d "[memory['seoyun_walk_detail']], 그날 얘기도 남기고 싶어요. 다음에 같이 다시 봐요."
            s "응. 다음 주말에 우리 둘이 어디 갈지부터 정하자."
            $ remember("seoyun_ending_promise", "revisit")
        "서로 대답을 기다려 주자고 한다.":
            d "모르는 게 생기면 다시 물어보고 싶어요. 좋아한다는 말도 아끼지 않고요."
            s "응. 그럼 나도 아끼면 안 되겠네. ...좋아해. 이건 오늘 치 선불."
            $ remember("seoyun_ending_promise", "next_answer")
        "각자 삶도, 둘의 시간도 지키자고 한다.":
            d "[memory.get('seoyun_private_name', '서윤 씨')] 일상도, 제 일상도 지키면서 계속 만나고 싶어요. 숨어서 말고요."
            s "응. 안 보는 날 보고 싶어지면 말할게. 당장 와 달라는 뜻으로 보내진 않고."
            $ remember("seoyun_ending_promise", "own_and_shared")
    "도현이 초안을 넣는 사이 서윤이 가방을 챙겼다. 이번엔 같이 일어났다."
    d "오늘은 어디까지 걸을까요?"
    s "골목 끝까지. 그다음엔 네가 돌아갈 시간도 봐야지~"
    if memory.get("seoyun_expression") == "quiet_public":
        "조용한 골목에서 손잡고 걸어도 되는지 서로 물었다. 도현이 손을 내밀었다."
    else:
        "카페를 나와 눈을 맞췄다. 좋다는 대답을 듣고 도현이 손을 내밀었다."
    $ remember("seoyun_route_completed")
    $ persistent.local_seoyun_ending = True
    $ ending = "seoyun_good"
    dn "내민 손을 서윤 씨가 잡았다. 길 건너 건물에 불이 켜졌다. 나는 서윤 씨 손을 잡은 채로 걸었다."
    $ award_once("seoyun_R16", "seoyun", 4)
    "서윤 본편 결말 · 함께 고르는 다음"
    $ progression_note_ending()
    return

label seoyun_e01:
    $ progression_enter("seoyun_e01")
    $ progression_checkpoint("seoyun_e01")
    if not dating or active_route != "seoyun" or not memory.get("seoyun_route_completed"):
        $ progression_note_ending()
        return
    $ chapter = "서윤 E01 · 같이 고른 자리"
    $ location = "약 반년 뒤, 쉬는 날 오전 · 예전 동네의 헌책방"
    "쉬는 날 오전, 둘은 서윤이 예전에 살던 동네의 헌책방에 다시 들렀다. 주인은 돋보기 너머로 둘을 번갈아 봤다."
    "'지난번 그 청년이네.' 주인이 말했다. '그 시집은 다 읽었고?'"
    s "첫 장에 날짜 적었어요, 사장님. 시키신 대로. 둘이 같이 읽은 날로요."
    "'날짜만 적으면 뭐 해. 끝까지 같이 읽어야지.'"
    s "그래서 다시 왔어요. 이번엔 제대로 소개하려고요."
    "서윤이 도현 팔을 잡아 앞으로 끌었다."
    s "지난번엔 지금 만나는 사람이라고 했죠, 사장님. 그 말 고칠게요. 오래 볼 사람이에요."
    "주인은 한참 말이 없다가 계산대 밑에서 낡은 책 한 권을 꺼냈다. 같은 시인의 다른 시집이었다."
    "'이건 안 파는 건데, 오래 볼 사람들한테는 빌려줘. 다 읽으면 둘이 같이 반납하러 와.'"
    d "꼭 같이 올게요."
    "가게를 나서며 서윤이 책을 가슴에 안았다."
    s "저 책을 빌려주시네. 전에는 아무리 졸라도 안 된다셨거든."
    d "알아들었어요."
    s "그럼 됐어. ...나, 이 동네 오는 게 이제 안 무서워."
    dn "삼 년 전 서윤 씨가 떠난 동네를, 오늘은 서윤 씨가 내 팔을 잡고 걸었다."
    $ location = "약 반년 뒤, 쉬는 날 오후 · 단골 북카페"
    "피칭은 TF의 승리로 끝났고, 서윤은 그 회사 일은 공식 연락으로만 받았다. 도현과 만날 날은 이제 서로의 달력을 보고 정했다."
    dn "다음 약속은 내가 먼저 달력을 열었다. 이번엔 서윤 씨가 날짜를 골랐다."
    $ remember("seoyun_family_state", "divorced")
    "도현은 완성한 기록집을 건넸다. '[memory['seoyun_booklet_sentence']]'와 서윤의 감상도 남아 있었다."
    s "내가 읽고 싶다고 한쪽, 진짜 남겼네."
    d "[memory.get('seoyun_private_name', '서윤 씨')] 몫은 첫 부예요. 다른 페이지도 같이 보고 싶어서요."
    $ cg("seoyun_e01")
    "서윤이 표지를 손바닥으로 쓸었다. 첫 장을 읽고 나서는 자기 컵보다 책을 먼저 도현 쪽으로 밀었다."
    s "여기서 웃었어. 왜인지는 네가 맞혀 볼래?"
    $ remember("seoyun_booklet_state", "이후 직접 촬영·글 정리를 마쳐 인쇄 기록집 완성")
    if memory.get("seoyun_o03_status") == "completed":
        s "그날 우리가 앉았던 자리도 생각나. 오늘은 또 다른 쪽이네."
        d "오늘 빛은 여기까지 들어오길래요."
    if memory.get("seoyun_walk_route") == "familiar":
        s "나갈 때 서점 뒤 골목까지 걸을래? 화분이 하나 더 늘었더라."
    elif memory.get("seoyun_walk_route") == "riverside":
        s "그 다리까지 걸을래? 오늘은 바람이 덜 부는 것 같아."
    else:
        s "골목 쪽으로 좀 걸을래? 어디서 돌아갈지는 같이 정하고."
    s "그리고 팀장님이 우리 사이 눈치챘어. 대놓고 묻진 않았는데, 회식 자리 배치가 수상하더라."
    d "네. [memory.get('seoyun_private_name', '서윤 씨')]는 지금 어떻게 생각하세요?"
    s "이제 숨길 이유는 없잖아. 근데 네가 회사에서 불편해질까 봐, 그건 네 대답부터 듣고 싶어."
    $ remember("seoyun_friends_know_relationship")
    $ progression_enter("seoyun_e01.choice01")
    $ progression_checkpoint("seoyun_e01.choice01")
    menu:
        "팀에 알리자고 한다.":
            d "저는 알리고 싶어요. 회식 때 [memory.get('seoyun_private_name', '서윤 씨')] 옆자리에 눈치 안 보고 앉고 싶어서요."
            s "응. 다음 주 회의 끝나고 같이 말하자. 팀장님 표정 볼만하겠다~"
            $ remember("seoyun_epilogue_choice", "consider_introduction")
            $ remember("seoyun_publicity_status", "서로 의향만 확인, 팀에 알릴 구체적 일정은 확인 전")
        "조금 더 비밀로 하자고 한다.":
            d "전 조금만 더 둘만 알고 싶어요. 회사에서 여러 사람한테 한꺼번에 얘기할 준비는 아직 안 됐어요."
            s "응. 네가 마음 바뀌면 알려 줘. 내가 먼저 말하고 싶어져도 물어볼게."
            $ remember("seoyun_epilogue_choice", "couple_time")
            $ remember("seoyun_publicity_status", "공개 보류, 둘만의 교제 지속")
        "공개보다 칫솔 얘기가 먼저라고 한다.":
            d "알리는 것보다... 저는 [memory.get('seoyun_private_name', '서윤 씨')] 집에 제 칫솔 두는 얘기가 더 하고 싶은데요."
            s "칫솔? ...색은 내가 골라도 돼? 내 거 옆에 꽂혔을 때 잘 어울리는 걸로."
            $ remember("seoyun_epilogue_choice", "discuss_life")
            $ remember("seoyun_publicity_status", "공개·동거 결정 전 생활 방식부터 논의")
    "서윤이 책갈피를 끼워 기록집을 넣었다. 나란히 골목으로 걸어 나왔다."
    s "오늘 내가 갖고 싶은 게 하나 더 있는데."
    d "어떤 거요?"
    s "네 손. 길 끝까지만 잡아도 되고, 더 걷고 싶으면 그때 물어볼게."
    "도현은 손을 내밀었다. 돌아갈 시간이 되자 인사를 나누고 각자의 집으로 향했다."
    $ remember("seoyun_relationship_status", "이혼 후 혼자 사는 서윤과 전남편 문제를 정리하고 교제 지속")
    $ remember("seoyun_cohabitation_status", "결혼·동거 확약 없음, 주변 공개는 둘이 정한 때에")
    $ remember("seoyun_epilogue_completed")
    dn "집에 도착하기 전에 서윤 씨가 책 사진을 보냈다. 첫 장에 오늘 날짜가 또 적혀 있었다."
    $ award_once("seoyun_E01", "seoyun", 8)
    $ progression_note_ending()
    return
