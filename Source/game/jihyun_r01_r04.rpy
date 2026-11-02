# Adult colleague from another team. Personal choices do not affect job evaluation.
default jihyun_prepared = False

label jihyun_r01:
    $ cream_focus = "jihyun"
    $ chapter = "지현 R01 · 업무 얘기는 아니야"
    $ location = "목요일 퇴근 후 · 개인 메시지"
    call phone_deliver("jihyun_r01_invite", "jihyun", "오늘 저녁 시간 있어? 같이 밥 먹고 싶어. 업무 얘기는 아니야. 일곱 시에 회사 앞 작은 식당 어때?", contact="jihyun", important=True)
    call phone_deliver("jihyun_r01_accept", "dohyun", "좋아요. 일곱 시에 뵐게요. 저도 일 얘기 말고 궁금한 게 있어요.", contact="jihyun")
    call phone_deliver("jihyun_r01_question", "jihyun", "그 말은 조금 긴장되네. 오늘은 내가 바로 답 못 해도 기다려 줘.", contact="jihyun")
    $ remember("jihyun_r01_appointment", "목요일 저녁 일곱 시, 회사 앞 작은 식당")
    $ location = "같은 목요일 저녁 일곱 시 · 약속한 식당"
    "지현이 메뉴판을 도현 쪽으로 돌렸다. 평소 쓰던 업무 수첩은 가방에서 꺼내지 않았다."
    "지현은 메뉴판 한쪽을 손끝으로 누르고 있었다. 도현이 같은 칸을 보자 슬쩍 손을 뗀다."
    j "아직 고른 건 아니야. 그냥... 여기부터 보고 있었어."
    d "저도 따뜻한 국수로 할게요. 아까부터 여기 보고 계셨죠?"
    j "티 났어? 아직 메뉴판도 다 못 봤는데."
    d "그럼 조금 더 봐요. 제가 먼저 정했다고 서두르실 건 없고요."
    j "...그래. 국수보다 더 끌리는 게 있나 볼게. 아까 궁금한 게 있다고 했지?"
    menu:
        "오늘은 결정을 내리는 일이 어려웠는지 묻는다.":
            d "오늘 결정할 게 많으셨어요? 퇴근하고는 어떤 기분이신지 궁금했어요."
            j "많았지. 지금은 국수까지 골랐고. 도현 씨한테 할 질문만 못 골랐네."
            d "그럼 국수 나오면 한 입 먹고 생각하세요. 저는 좀 기다릴 수 있는데요."
            j "...그렇게 기다려 주면 괜히 더 좋은 질문 하고 싶어지잖아."
            $ remember("jihyun_r01_topic", "decision")
        "휴일의 조립 취미는 어떻게 보내는 시간인지 묻는다.":
            if memory.get("c05_shared_table"):
                d "쉬는 날에 조립하신다고 했잖아요. 끝내는 것보다 만드는 쪽이 좋으세요?"
                j "응. 부품 하나 끼우고 한참 그냥 봐도 돼. 그런데 완성하면 누군가한테 먼저 보여 주고 싶기도 하고."
            else:
                d "휴일에는 어떤 취미 하세요? 끝내는 것보다 그 시간이 궁금해서요."
                j "작은 조립물 만들어. 부품 하나 끼우고 한참 그냥 봐도 되거든. 완성하면 누군가한테 먼저 보여 주고 싶기도 하고."
            d "저 그 첫 구경꾼 자리 궁금하네요. 설명서 거꾸로 봐도 놀리지는 않을게요."
            j "그건... 다음에 보고 결정해. 놀릴 만한 건 나도 알아서."
            $ remember("jihyun_r01_topic", "hobby")
        "여럿이 아닌 나와 따로 만나고 싶었던 이유를 묻는다.":
            d "저랑 따로 보고 싶으셨던 이유요. 식사 초대받고 그게 먼저 궁금했어요."
            "지현이 물컵을 들었다가 한 모금만 마시고 내려놨다."
            j "같이 밥 먹자는 말이면 적당히 숨겼다고 생각했는데. 질문은 안 숨겨 주네."
            d "바로 답 안 하셔도 돼요. 저는 같이 보고 싶어서 왔어요."
            j "...그럼 나도 답을 남겨 둘게. 그냥 잊은 걸로 하지는 말고."
            $ remember("jihyun_r01_topic", "why_me")
    "주문한 음식이 나왔다. 지현이 도현의 빈 물컵을 가리키자 도현이 물병을 가운데 놓았다."
    d "저도 따를게요. 오늘은 챙겨 주시는 것만 받고 싶지는 않아서요."
    "지현이 자기 컵을 앞으로 밀었다가 물이 넘칠까 봐 손을 멈췄다."
    j "조금만. ...아니, 내가 양까지 정해 주네. 적당히 부탁해."
    d "이건 자신 있습니다. 물컵 경력은 꽤 돼서요."
    "지현이 국수를 한 젓가락 들었다가 내려놓았다. 도현도 국물에 손대려던 숟가락을 멈춘다."
    j "뜨거워. 자신 있는 쪽은 물컵까지만 해."
    d "경력의 한계를 정확히 봐주시네요."
    j "나도 방금 알았으니까. 맛있어 보인다고 서두르면 안 되네."
    "조금 식힌 뒤 도현이 국물을 맛봤다. 지현이 젓가락 너머로 도현을 본다."
    j "골라 준 사람 앞이라 좋다고 할 필요는 없고."
    d "맛있어요. 다음엔 다른 것도 먹어 보고 싶고요."
    j "응. ...첫마디만 들어도 됐는데. 다음 것도 생각해 볼게."
    "식사를 마친 뒤 도현이 계산대 옆에서 기다렸다. 각자 계산을 마치고 식당 밖으로 나왔다."
    j "토요일 두 시에 시간 있어? 동네 서점 앞에서 만나고 싶어. 그 뒤에 잠깐 쉬고."
    d "네. 두 시 괜찮아요. 이번에도 제 질문 하나 가져가도 되죠?"
    j "응. 나도 하나는 준비해 볼게. 일곱 개쯤 되면 줄이고."
    $ remember("jihyun_r02_appointment", "토요일 오후 두 시, 동네 서점 앞")
    $ award_once("jihyun_R01", "jihyun", 4)
    return

label jihyun_r02:
    $ chapter = "지현 R02 · 오늘은 네가 정해 줘"
    $ location = "토요일 오후 두 시 · 동네 서점 앞"
    "지현은 가벼운 가방 하나를 들고 서 있었다. 도현이 도착하자 휴대폰의 일정표를 닫는다."
    j "오늘은 네 시쯤 집에 돌아가고 싶어. 그전엔 조금 쉬고 싶고. 장소랑 순서, 오늘은 도현 씨가 정해 줄래?"
    d "두 시간이면 되겠네요. 시끄러운 곳은 저도 빼고 싶은데, 차가운 음료는 어떠세요?"
    j "오늘은 따뜻한 게 좋아. 그거면 나머진 맡길게."
    menu:
        "조용한 찻집에 먼저 앉아 따뜻한 차를 마시자고 한다.":
            d "서점 안은 다음에 보고, 저 찻집부터 갈까요? 앉아서 오래 얘기하고 싶어요."
            j "좋아. 내 추천이 아니라 도현 씨가 고른 자리로 가 보자."
            $ location = "같은 토요일 오후 · 조용한 찻집"
            "따뜻한 차를 하나씩 골랐다. 지현은 먼저 창밖을 보고 나서 도현 쪽으로 시선을 돌렸다."
            "도현이 따뜻한 찻잔 쪽으로 손을 뻗자 지현이 잔받침을 가까이 밀어 줬다."
            j "일단 식기 전에 마셔. 나 쳐다보다 다 식겠다."
            d "차도 보고 있었어요. 순서는 조금 밀렸지만요."
            "지현이 찻잔을 들어 향을 맡았다. 도현은 한 모금 마신 뒤 잔을 내려놓는다."
            j "어때?"
            d "첫 모금보다 두 번째가 낫네요. 아까는 뜨거운 줄도 모르고 마셔서."
            j "그런 건 먼저 말해. 참는다고 차가 빨리 식진 않아."
            d "네. 이번엔 조금 기다렸다가요."
            "지현도 바로 마시지 않고 찻잔을 손 안에서 천천히 돌렸다."
            j "...나도. 첫 모금은 졌네."
            $ remember("jihyun_r02_plan", "tea_first")
            $ remember("jihyun_r02_action", "도현이 고른 조용한 찻집에서 따뜻한 차를 각자 선택함")
        "짧게 공원을 걷고, 돌아오는 길에 따뜻한 차를 마시자고 한다.":
            d "먼저 저 공원까지만 걸을까요? 돌아와서 차 마시면 네 시 전에 끝낼 수 있어요."
            j "응. 길은 좀 돌아가도 되는데 돌아갈 시각은 그대로 둘게."
            $ location = "같은 토요일 오후 · 공원 산책길"
            "공원 입구에서 한 바퀴만 걸었다. 지현은 시계를 보려다 손목을 내리고 도현과 보폭을 맞췄다."
            d "저는 지금 정도 속도가 좋네요. 옆에서 얘기하기도 편하고요."
            j "나도. 근데 아까 그 갈림길에서 조금 망설였지?"
            d "들켰어요? 돌아가는 길이 더 좋아 보여서요."
            j "그럼 돌아가자. 네 시는 아직 안 됐으니까."
            "갈림길로 돌아간 도현이 먼저 멈췄다. 길이 넓어지는 대신 벤치 하나가 나왔다."
            d "생각보다 금방 끝나네요. 숨겨진 산책로인 줄 알았는데."
            j "그럼 앉았다 가자. 돌아온 보람은 있어야지."
            d "실패한 안내에도 점수를 주시네요."
            j "벤치는 내가 찾았으니까. 내 점수야."
            "나란히 잠깐 쉰 뒤 돌아오는 길에 따뜻한 차를 샀다. 지현은 이번에는 도현이 고른 길을 먼저 본다."
            $ remember("jihyun_r02_plan", "walk_then_tea")
            $ remember("jihyun_r02_action", "공원 한 바퀴 뒤 따뜻한 차, 귀가 시각 유지")
        "서점과 찻집 후보를 하나씩 놓고 지현의 남은 바람도 듣는다.":
            d "저는 서점 한쪽 구경하고 차 마시는 순서가 좋아요. 팀장님도 남기고 싶은 게 하나 있으세요?"
            j "책등 예쁜 데. ...지금 제목 안 읽고 골랐다고 생각했지?"
            d "아직 아무 말도 안 했어요!"
            j "그럼 내가 먼저 고백한 셈이네. 내용은 앉아서 볼래."
            d "그럼 책등 한 선반만요. 그다음은 제가 고른 찻집으로요."
            "한 선반 앞에서 지현은 반듯한 책등을, 도현은 제목이 비스듬하게 놓인 책을 골랐다."
            j "일부러 반대로 고르는 건 아니지?"
            d "아뇨. 저건 혼자 누워 있길래 눈에 띄었어요."
            "지현이 그 책을 똑바로 세워 주고 한 발 물러났다."
            d "지금은 덜 궁금해졌는데요~"
            j "다시 눕히지는 마. 이제 내가 내용이 궁금해졌으니까."
            "서로 고른 제목을 기억해 두고 찻집으로 옮겼다. 지현은 나가기 전에 반듯해진 책등을 한 번 더 봤다."
            $ location = "같은 토요일 오후 · 서점 옆 찻집"
            $ remember("jihyun_r02_plan", "choose_together")
            $ remember("jihyun_r02_action", "서점 한 선반의 제목을 고르고 도현이 고른 찻집으로 이동함")
    $ remember("jihyun_r02_delegated_scope", "네 시 귀가, 조용한 장소·따뜻한 음료, 장소와 순서는 맡기거나 함께 좁힘")
    if c06_person == "jihyun" and c06_topic == "weekend":
        j "설명서 거꾸로 봤던 날엔 내가 먼저 급했지. 오늘은 다 고르기 전에 넘겨 줬네."
    elif c06_person == "jihyun" and c06_topic == "place":
        j "그때 차는 가져가라고만 했는데. 오늘은 같이 앉는 쪽이 됐네."
    else:
        j "다음에 뭘 할지 바로 정하지 않아도 여기 앉아 있을 수 있구나."
    d "지금은 다음 질문 하나만 고르시면 돼요. 저 만나서 어떤 게 제일 의외였어요?"
    j "말이 생각보다 곧장 오는 거. 업무에서만 그런 줄 알았는데."
    d "오늘은 회의 자료가 없으니까 덜 돌려 말해도 될 것 같아서요."
    j "그래. 그럼 내 것도 곧장. 오늘 같이 있어서 좋았어."
    "네 시가 되기 전에 서점 입구에서 인사를 나눴다. 지현이 먼저 돌아서다가 고개를 한 번 더 돌린다."
    j "오늘 고른 차 이름, 나중에 알려 줘. 내가 고른 것보다 먼저 또 마시고 싶어졌네."
    $ remember("jihyun_r02_time_kept")
    $ location = "같은 토요일 저녁 · 지현의 집 — 지현 시점"
    "지현은 완성하지 못한 조립물을 책상 위에 두고 오늘 고른 차 이름을 메모했다. 옆에 다음에 보여 주고 싶은 부품을 하나 올려놓는다."
    jn "같이 쉬자고 먼저 말하는 건 했네. 다음에도 설명부터 준비할 필요는 없겠지."
    $ cream_focus = None
    $ award_once("jihyun_R02", "jihyun", 7)
    return

label jihyun_r03:
    $ chapter = "지현 R03 · 네 안을 다시 봤어"
    $ location = "다음 주 월요일 오후 · 협업 자료 검토 자리"
    $ cream_focus = "jihyun"
    "지현이 ‘출근길 중심’이라고 적었던 가정을 다시 열었다. 도현에게 검토할 부분을 표시해 화면을 돌린다."
    if memory.get("jihyun_intro") == "evidence":
        j "점심에 다시 와도 되냐는 질문, 다시 봤어. 몇 분 얘기라도 출근길만 보긴 어렵겠네."
    elif memory.get("jihyun_intro") == "check_later" and memory.get("jihyun_followup_delivered"):
        j "다음 날 준 메모 봤어. 기록 없는 데도 표시해 줬더라. 그쪽 시간대부터 더 볼게."
    elif memory.get("jihyun_intro") == "check_later":
        j "더 확인해 본다고 했지. 결과는 아직 못 봤으니까, 지금 아는 것부터 보자."
    elif memory.get("jihyun_intro") == "compare":
        j "첫날 비교했던 두 시간대, 둘 다 확인해 보려고. 어느 쪽이 맞는진 더 봐야겠어."
    else:
        j "이 시간대 가정을 다시 보려고. 도현 씨가 지금 확인할 수 있는 범위부터 듣고 싶어."
    "지현은 도현의 메모를 시간대 표 옆에 붙였다."
    menu:
        "판단을 바꾼 이유를 분명히 들려준 점이 좋았다고 말한다.":
            d "이유까지 말씀해 주셔서 좋아요. 다음에도 다른 의견 있으면 말할게요."
            j "응. 나도 다시 볼게. 오늘처럼."
            $ remember("jihyun_r03_response", "reason")
        "내 의견도 확인 뒤 달라질 수 있다고 말하며 다음 확인을 나눈다.":
            d "저도 더 보면 생각 달라질 수 있어요. 현장에서 확인할 질문은 제가 정리해 볼게요."
            j "좋아. 내 쪽은 시간대 가정 다시 볼게. 바뀐 이유까지 같이 남기자."
            $ remember("jihyun_r03_response", "share_check")
        "업무 의견과 별개로 지현의 태도가 기억에 남았다고 말한다.":
            d "팀장님이 직접 다시 보셨다는 게 기억에 남아요. 제 쪽으로 맞춰 주셨다는 뜻으로 듣지는 않을게요."
            j "응. 의견을 검토한 거야. 그래도 그렇게 말해 주는 건... 좀 기분 좋네."
            $ remember("jihyun_r03_response", "attitude")
    $ remember("jihyun_core_understanding")
    $ location = "같은 월요일 퇴근 후 · 개인 메시지"
    if memory.get("jihyun_r01_topic") == "why_me":
        call phone_deliver("jihyun_r03_personal", "jihyun", "왜 따로 만나고 싶었냐고 물었지. 일 얘기 안 해도 네 다음 말이 궁금했어. 그날 못 한 대답, 지금 할게.", contact="jihyun", important=True)
        $ remember("jihyun_r01_reason_answered")
    elif memory.get("jihyun_r01_topic") == "hobby":
        call phone_deliver("jihyun_r03_personal", "jihyun", "첫 구경꾼 자리 궁금하다고 했지. 아직 완성은 아닌데 다음에 보여 주고 싶어. 재촉 안 할 사람인 건 지난 토요일에 좀 알았고.", contact="jihyun")
    else:
        call phone_deliver("jihyun_r03_personal", "jihyun", "업무 의견 고맙다는 말 말고 하나 더. 지난 토요일에 같이 쉰 게 좋았어. 다음에도 회사 밖에서 만나고 싶어.", contact="jihyun", important=True)
    call phone_deliver("jihyun_r03_reply", "dohyun", "저도요. 금요일 저녁 일곱 시 괜찮으세요? 이번에는 제가 따로 말씀드리고 싶은 게 있어요.", contact="jihyun")
    call phone_deliver("jihyun_r03_confirm", "jihyun", "괜찮아. 회사 앞 카페에서 보자. 그 말도 같이 기다릴게.", contact="jihyun")
    $ remember("jihyun_r04_appointment", "금요일 저녁 일곱 시, 회사 앞 카페")
    $ award_once("jihyun_R03", "jihyun", 8)
    return

label jihyun_r04:
    if not memory.get("jihyun_core_understanding"):
        return
    $ chapter = "지현 R04 · 결정은 같이 하자"
    $ location = "금요일 저녁 일곱 시 · 약속한 카페"
    $ cream_focus = "jihyun"
    "지현이 도현을 보고 휴대폰을 가방에 넣었다. 도현은 맞은편 의자에 앉아 준비해 온 말을 한 번 골랐다."
    j "오늘은 도현 씨가 말하고 싶다고 했지. 나도 질문부터 꺼내진 않을게."
    while not dating and not memory.get("jihyun_relationship_declined"):
        menu:
            "지현과 연인으로 만나고 싶다고 먼저 고백한다.":
                d "토요일에 네 시 되니까 헤어졌잖아요. 저는 좀 더 같이 있고 싶었어요. 그 뒤로도 또 보고 싶었고요. 지현 씨, 좋아해요. 저랑 사귀실래요?"
                "지현은 바로 대답하려다 물컵에서 손을 뗐다. 이번에는 도현을 보며 천천히 말한다."
                j "응. 나도 좋아해. ...지금 답하는데 너무 빠르진 않았지?"
                d "기다리셨다는 쪽으로 들을게요."
                j "응. 그쪽이 맞아."
                $ dating = True
                $ remember("jihyun_confession_accepted")
                $ award_once("jihyun_R04", "jihyun", 5)
            "마음은 있지만, 내 서툼과 회사에서의 경계를 조금 더 이야기한다." if not jihyun_prepared:
                d "저 연애는 처음이에요. 좋아하는 마음은 분명한데, 일할 때와 구분하려고 제 마음을 너무 늦게 말할까 봐요."
                j "나도 연애를 아주 익숙하게 하는 쪽은 아니야. 그래도 지금 원하는 건 회사가 아니라 여기서 같이 고를 수 있겠지."
                d "의견이 다르면 일에서는 그대로 말할게요. 보고 싶을 때도 따로 말씀드리고요."
                j "좋아. 부탁을 안 들어줬다고 마음까지 없다고 짐작하진 않을게. 도현 씨도 내 표정으로 먼저 결론 내리지 말고."
                $ jihyun_prepared = True
                $ remember("jihyun_prepared_conversation")
            "이번 회차는 연애를 시작하지 않고 동료로 지낸다 — 동료 결말로 이어짐.":
                d "저는 이번에는 동료로 지내고 싶어요. 연애를 시작하겠다는 말씀은 드릴 수 없어요."
                menu:
                    "동료로 지내겠다는 뜻을 확인한다.":
                        j "알겠어. 오늘 대답은 오늘 대답으로 둘게. 업무 의견을 듣는 건 달라지지 않아."
                        $ remember("jihyun_relationship_declined")
                        call end_common
                        return
                    "결정을 취소하고 마음을 다시 고른다.":
                        pass
                    "결정 전에 지현이 원하는 관계를 한 번 더 듣는다.":
                        j "나는 연인으로 만나 보고 싶어. 그래도 같은 답을 골라야 한다는 뜻은 아니야. 도현 씨 마음을 다시 듣고 싶어."
    if not jihyun_prepared:
        d "저는 첫 연애예요. 먼저 말하는 것부터 좀 연습해 왔는데, 지금은 그 다음이 더 긴장되네요."
        j "난 단정하게 답할 수 있을 줄 알았어. ...계속 도현 씨 얼굴 보게 되는 건 생각 못 했네."
    j "회사에선 지금처럼 의견 말해 줘. 내 부탁도 싫으면 싫다고 하고."
    d "네. 저도 제멋대로 정해 놓고 따라오시라고는 안 할게요."
    j "응. 교제 얘기는 당분간 우리만 알자. 다른 사람한테 말할 땐 서로 묻고."
    $ remember("jihyun_work_boundary", "업무 검토와 연애를 구분, 사적 부탁 거절 가능, 일정·의견은 먼저 물음")
    $ remember("jihyun_publicity", "private")
    menu:
        "첫 연인 데이트는 내가 먼저 장소 후보를 가져오고 싶다고 말한다.":
            d "다음에는 제가 장소 후보 가져올게요. 되는 시간은 같이 정해요."
            j "좋아. 이번엔 기대하는 쪽으로 먼저 와 있을게."
            $ remember("jihyun_next_date_plan", "dohyun_suggests")
        "각자 쉬는 시간과 함께 만날 시간을 하나씩 정해 보자고 한다.":
            d "각자 하던 것도 남겨 두고 싶어요. 같이 만날 시간도 하나 잡고요."
            j "응. 같이 있는 칸을 만들려고 내 일정까지 다 비울 필요는 없겠네. 도현 씨 것도 그렇게 두자."
            $ remember("jihyun_next_date_plan", "own_and_shared")
        "지현의 다음 제안에 내 취향도 보태고 싶다고 말한다.":
            d "팀장님이 보여 주고 싶은 곳도 듣고 싶어요. 제 취향도 하나 보탤게요."
            j "좋아. 이번에도 조용한 데일 가능성은 높은데, 정답은 아닐 거야."
            $ remember("jihyun_next_date_plan", "both_suggest")
    if memory["jihyun_next_date_plan"] == "both_suggest":
        j "아까는 지현 씨라고 하더니, 벌써 다시 팀장님이네."
    else:
        j "아까 지현 씨라고 불렀지. 그건 조금 낯설더라."
    d "좋아한다는 말보다 호칭이 더 오래 걸릴 수도 있겠네요."
    j "기다려 볼게. 대신 아까 그 말은 한 번 더 해 줘."
    d "좋아해요, 지현 씨."
    "지현이 컵 손잡이를 놓고 도현을 똑바로 보았다."
    j "응. 이번엔 천천히 대답했어."
    $ remember("jihyun_r04_complete")
    $ remember("jihyun_first_kiss_plan", "R05에서 교제 후 선택 가능, 현재는 발생하지 않음")
    return

label jihyun_early_route(full_route=False):
    $ active_route = "jihyun"
    $ cream_focus = "jihyun"
    $ phone_active_contact = "jihyun"
    call jihyun_r01
    call jihyun_r02
    call jihyun_r03
    call jihyun_r04
    if memory.get("jihyun_r04_complete") and full_route:
        call jihyun_r05
        call jihyun_o01_offer
        call jihyun_r06
        call jihyun_r07
        call jihyun_r08
        call work_mini_second
        call jihyun_r09
        call jihyun_r10
        call jihyun_o02_offer
        call jihyun_r10_after
        call jihyun_r11
        call jihyun_r12
        call jihyun_r13
        call jihyun_r14
        if dating and memory.get("jihyun_conflict") == "resolved":
            call jihyun_r15
            call jihyun_o03_offer
            call jihyun_r16
            if memory.get("jihyun_route_completed"):
                menu:
                    "후일담 읽기 — 약 반년 뒤 쉬는 날의 부탁":
                        call jihyun_e01
                    "본편 결말에서 마치기 — 후일담은 이번에 읽지 않음":
                        $ remember("jihyun_epilogue_skipped")
                    "다음에도 만나고 싶다고 한마디 나누고 후일담 읽기":
                        d "다음에도 제가 먼저 만나자고 할게요."
                        j "응. 나는 기다리는 쪽도 기꺼이 해 볼게."
                        $ remember("jihyun_epilogue_bridge")
                        call jihyun_e01
    elif memory.get("jihyun_r04_complete"):
        $ ending = "jihyun_early_segment_complete"
        "지현 R01~R04 내부 확인 구간을 마쳤습니다. 시작 화면의 지현 전체 대본 확인에서는 후속 이야기도 이어집니다."
    return

label jihyun_early_preview:
    $ cream_preview_active = False
    "지현 전체 대본 확인입니다. 공통의 세부 선택 기억 없이 시작하며, 최종 그림·영상·음성은 아직 준비 중입니다."
    call jihyun_early_route(full_route=True)
    return
