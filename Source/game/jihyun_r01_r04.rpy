# Adult colleague from another team. Personal choices do not affect job evaluation.
default jihyun_prepared = False

label jihyun_r01:
    $ progression_enter("jihyun_r01")
    $ progression_checkpoint("jihyun_r01")
    $ cream_focus = "jihyun"
    $ chapter = "지현 R01 · 업무 얘기는 아니야"
    $ location = "목요일 오후 · 회의 공간"
    "다들 회의실을 나섰다. 도현이 따라 나가려는데 지현이 불러 세웠다."
    j "잠깐. 일 분."
    d "네, 팀장님. 자료 어디 고칠까요?"
    j "아니. 자료는 문제없어."
    "지현은 펜 뚜껑을 닫았다가 다시 열었다. 세 번째에서야 입을 뗐다."
    j "너 오늘 저녁에... 그러니까, 퇴근하고."
    "그때 회의실 문이 열리고 다른 팀 과장이 고개를 들이밀었다. 지현은 펜 뚜껑을 탁 닫았다."
    j "아니야. 이따 메시지로 할게. 업무 얘기는 아니야. 그것만 알아 둬."
    "과장이 지현을 데리고 나갔다. 도현은 빈 회의실에 한참 서 있었다."
    dn "결론부터 말하는 사람이 결론을 말하지 못하고 나갔다. 퇴근 시간까지 휴대폰을 세 번 확인했다."
    $ location = "목요일 퇴근 후 · 개인 메시지"
    call phone_deliver("jihyun_r01_invite", "jihyun", "오늘 저녁 일곱 시. 회사 앞 작은 식당\n일 얘기 아님", contact="jihyun", important=True)
    call phone_deliver("jihyun_r01_accept", "dohyun", "좋아요. 일곱 시에 갈게요\n저도 일 말고 여쭤볼 거 있어요", contact="jihyun")
    call phone_deliver("jihyun_r01_question", "jihyun", "뭔데\n...아니다. 만나서 해. 일곱 시까지 일은 해야지", contact="jihyun")
    $ remember("jihyun_r01_appointment", "목요일 저녁 일곱 시, 회사 앞 작은 식당")
    $ location = "같은 목요일 저녁 일곱 시 · 약속한 식당"
    "식당 안쪽 자리. 지현은 메뉴판을 반쯤 펼쳐 놓고 손가락 하나로 한 칸을 꾹 누르고 있다."
    j "왔어? 앉아. 여기 국수가 괜찮아."
    d "그 손가락 밑에 있는 거요?"
    j "이건 그냥 짚고 있던 거고."
    d "저도 국수로 할게요."
    j "따라 하지 마. 다른 거 시켜야 나눠 먹지."
    dn "결론은 역시 빨랐다. 그 뒤에 붙인 말은 회의 때 한 번도 못 들었다."
    j "그래서. 궁금한 게 뭐야?"
    $ progression_enter("jihyun_r01.choice01")
    $ progression_checkpoint("jihyun_r01.choice01")
    menu:
        "오늘 하루 어떠셨어요?":
            d "오늘 결정할 게 많으셨어요? 퇴근하고 얼굴이 좀 피곤해 보여서요."
            j "열한 개. 다 정했어. 방금 국수까지 하면 열두 개."
            d "그럼 열세 번째는 제가 정할게요. 디저트요."
            j "그건 고맙네. 오늘 처음으로 남이 정해 주는 거야."
            $ remember("jihyun_r01_topic", "decision")
        "쉬는 날엔 뭐 하세요?":
            if memory.get("c05_shared_table"):
                d "쉬는 날 조립하신다고 했잖아요. 완성하는 게 좋으세요, 만드는 게 좋으세요?"
                j "조립. 부품 하나 끼우고 삼십 분씩 봐. 다 만들면 보여 줄 사람이 없네."
            else:
                d "쉬는 날엔 뭐 하세요? 회사 밖 팀장님은 상상이 잘 안 돼서요."
                j "작은 모형 조립해. 부품 하나 끼우고 삼십 분씩 봐. 다 만들면 보여 줄 사람이 없네."
            d "그 자랑, 제가 들어도 돼요? 설명서 거꾸로 봐도 안 놀릴게요."
            j "놀릴 거잖아. 표정에 다 쓰여 있어."
            d "...조금만요."
            j "봐. 보여 줄지는 다음에 내가 정해."
            $ remember("jihyun_r01_topic", "hobby")
        "왜 저를 따로 부르셨어요?":
            d "저를 따로 부르신 이유요. 초대받고 그게 제일 궁금했어요."
            "지현이 물컵을 들었다. 마시지 않고 그대로 내려놓았다."
            j "밥 먹자고 했으면 그걸로 넘어갈 줄 알았는데."
            d "넘어가 드릴까요?"
            j "아니. 답은 할게. 오늘 말고. 대신 잊어버리면 안 돼."
            $ remember("jihyun_r01_topic", "why_me")
    "음식이 나왔다. 지현이 도현의 빈 물컵을 턱으로 가리켰다. 도현은 물병을 가운데로 옮겼다."
    d "제가 따를게요. 오늘은 받기만 하는 거 말고요."
    j "그럼 조금만. 아니, 반. 아니, 적당히."
    d "물 따르는 데도 결재가 세 번이네요."
    j "시끄러워. 넘치면 네가 닦아."
    "국수를 한 젓가락 들었던 지현이 그대로 내려놓았다. 도현은 국물 앞에서 숟가락을 멈췄다."
    j "뜨거워. 먹지 마."
    d "명령이에요?"
    j "충고야. 방금 나도 데었거든."
    "조금 식힌 뒤 국물을 맛봤다. 지현은 젓가락 너머로 도현 표정만 보고 있다."
    j "맛없으면 맛없다고 해. 내가 고른 집이라고 봐주지 말고."
    d "맛있어요. 다음엔 다른 것도 먹어 보고 싶을 만큼요."
    j "그럼 됐어. 맛있다는 말만 들어도 됐는데, 뒤에 붙은 게 더 좋네."
    "계산은 각자 했다. 식당 밖에서 지현이 휴대폰 달력을 열었다가 도로 닫았다."
    j "토요일 두 시. 동네 서점 앞. 시간 돼?"
    d "돼요. 이번엔 제 질문도 하나 가져갈게요."
    j "하나만 가져와. 나는 일곱 개 준비할 거니까 줄이는 건 네 몫이야."
    $ remember("jihyun_r02_appointment", "토요일 오후 두 시, 동네 서점 앞")
    dn "일곱 개 중에 여섯 개를 빼야 한다. 뭘 남길까."
    $ award_once("jihyun_R01", "jihyun", 4)
    $ progression_note_ending()
    return

label jihyun_r02:
    $ progression_enter("jihyun_r02")
    $ progression_checkpoint("jihyun_r02")
    $ chapter = "지현 R02 · 오늘은 네가 정해 줘"
    $ location = "금요일 오후 · 회의 공간"
    "금요일 오후. 회의가 끝나고 지현이 수첩을 덮다 말았다. 토요일 칸에 물음표 하나가 적혀 있었다."
    j "하나 물어봐도 돼. 업무 아니야."
    d "네, 팀장님."
    j "쉬는 날 뭐 해? 난 다음 주 자료 보거든. 남들은 뭐 하나 싶어서."
    "농담인 줄 알고 웃으려다 말았다. 지현의 얼굴은 보고서를 검토할 때만큼 진지했다."
    d "저는 그냥 걸어요. 서점에 들렀다가, 배고프면 눈에 보이는 데서 먹고요."
    j "계획 없이?"
    d "계획 없이요."
    j "그게 되는구나."
    "지현이 물음표 옆에 뭔가를 적었다. 거꾸로 봐서 정확하진 않았지만 '걷기(계획 X)'처럼 보였다."
    j "내일 두 시. 네가 말한 대로 해 보자. 대신 나, 못 견디면 중간에 일정 짤 수도 있어."
    d "그때는 제가 수첩 뺏을게요."
    "지현이 수첩을 가슴 쪽으로 당겼다. 그러면서도 웃고 있었다."
    dn "내일은 길도 내가 보고 시간도 내가 보자. 수첩은 계속 주머니에 있게."
    $ location = "토요일 오후 두 시 · 동네 서점 앞"
    "지현은 가벼운 가방 하나를 들고 서 있었다. 도현을 보자 휴대폰의 일정표를 닫았다."
    dn "일정표를 닫는 손이 조금 어색했다. 닫는 연습을 해 온 사람 같았다."
    j "네 시엔 집에 갈 거야. 그전까진 좀 쉬고 싶고. 장소랑 순서는, 오늘은 네가 정해. 부탁할게."
    d "두 시간이면 충분하겠네요. 시끄러운 데는 저도 빼고요. 음료는 차가운 거 괜찮으세요?"
    j "따뜻한 거. 그거 말곤 다 맡길게."
    $ progression_enter("jihyun_r02.choice01")
    $ progression_checkpoint("jihyun_r02.choice01")
    menu:
        "찻집에서 따뜻한 차부터.":
            d "서점은 다음에 보고, 저 찻집 어때요? 앉아서 얘기 좀 하고 싶어요."
            j "승인. 오늘은 내 추천 말고 네가 찾은 자리로."
            $ location = "같은 토요일 오후 · 조용한 찻집"
            "따뜻한 차를 하나씩 시켰다. 지현은 창밖을 한 번 보고 나서야 도현 쪽으로 시선을 돌렸다."
            "도현이 따뜻한 찻잔 쪽으로 손을 뻗자 지현이 잔받침을 가까이 밀어 줬다."
            j "일단 식기 전에 마셔. 나 쳐다보다 다 식겠다."
            d "차도 보고 있었어요. 순서는 조금 밀렸지만요."
            "지현이 찻잔을 들어 향을 맡았다. 도현은 한 모금 마신 뒤 잔을 내려놓았다."
            j "어때?"
            d "첫 모금보다 두 번째가 낫네요. 아까는 뜨거운 줄도 모르고 마셔서."
            j "뜨거우면 뜨겁다고 해. 참는다고 차가 빨리 식진 않아."
            d "네. 이번엔 좀 기다렸다 마실게요."
            "지현도 바로 마시지 않고 찻잔을 손 안에서 천천히 돌렸다."
            j "나도. 첫 모금은 졌네."
            $ remember("jihyun_r02_plan", "tea_first")
            $ remember("jihyun_r02_action", "도현이 고른 조용한 찻집에서 따뜻한 차를 각자 선택함")
        "공원 한 바퀴, 돌아와서 차 한 잔.":
            d "저 공원까지만 걸을까요? 돌아와서 차 마시면 네 시 전에 끝나요."
            j "응. 길은 돌아가도 돼. 돌아갈 시각만 그대로 두고."
            $ location = "같은 토요일 오후 · 공원 산책길"
            "공원 입구에서 한 바퀴만 걸었다. 지현은 시계를 보려다 손목을 내리고 도현과 보폭을 맞췄다."
            d "저는 지금 정도 속도가 좋네요. 옆에서 얘기하기도 편하고요."
            j "나도. 근데 아까 그 갈림길에서 조금 망설였지?"
            d "들켰어요? 돌아가는 길이 더 좋아 보여서요."
            j "그럼 돌아가자. 네 시는 아직 안 됐으니까."
            "갈림길로 돌아가자 도현이 멈춰 섰다. 길은 금방 끝나고 벤치 하나가 나왔다."
            d "생각보다 금방 끝나네요. 숨겨진 산책로인 줄 알았는데."
            j "그럼 앉았다 가자. 돌아온 보람은 있어야지."
            d "실패한 안내에도 점수를 주시네요."
            j "벤치는 내가 찾았으니까. 내 점수야."
            "잠깐 앉았다가 돌아오는 길에 따뜻한 차를 샀다. 지현은 이번엔 도현이 가자는 길을 따라 걸었다."
            $ remember("jihyun_r02_plan", "walk_then_tea")
            $ remember("jihyun_r02_action", "공원 한 바퀴 뒤 따뜻한 차, 귀가 시각 유지")
        "서점 한 선반, 그다음 찻집.":
            d "저는 서점 잠깐 보고 차 마시는 순서가 좋아요. 팀장님은 꼭 하고 싶은 거 있으세요?"
            j "책등 예쁜 데. 방금 제목도 안 읽고 책 산다고 생각했지?"
            d "아직 아무 말도 안 했어요!"
            j "그럼 내가 자백한 셈이네. 내용은 앉아서 볼 거야."
            d "그럼 책등 예쁜 선반 하나만요. 그다음엔 제가 찾은 찻집으로요."
            "한 선반 앞에서 지현은 반듯한 책등을, 도현은 비스듬히 누운 책을 집었다."
            j "일부러 반대로 집는 거 아니지?"
            d "아뇨. 저건 혼자 누워 있길래 눈에 띄었어요."
            "지현이 그 책을 똑바로 세워 주고 한 발 물러났다."
            d "지금은 덜 궁금해졌는데요~"
            j "다시 눕히지는 마. 이제 내가 내용이 궁금해졌으니까."
            "서로 집었던 제목을 외워 두고 찻집으로 옮겼다. 나가기 전, 지현은 반듯해진 책등을 한 번 더 돌아봤다."
            $ location = "같은 토요일 오후 · 서점 옆 찻집"
            $ remember("jihyun_r02_plan", "choose_together")
            $ remember("jihyun_r02_action", "서점 한 선반의 제목을 고르고 도현이 고른 찻집으로 이동함")
    $ remember("jihyun_r02_delegated_scope", "네 시 귀가, 조용한 장소·따뜻한 음료, 장소와 순서는 맡기거나 함께 좁힘")
    if c06_person == "jihyun" and c06_topic == "weekend":
        j "설명서 거꾸로 봤던 날엔 내가 급했지. 오늘은 네가 다 정할 때까지 기다렸네."
    elif c06_person == "jihyun" and c06_topic == "place":
        j "그때 차는 가져가라고만 했는데. 오늘은 같이 앉는 쪽이 됐네."
    else:
        j "다음 일정 안 정해 놓고도 앉아 있을 수 있구나. 나."
    d "그럼 질문 하나만 할게요. 저 만나 보고 제일 의외였던 거 뭐예요?"
    j "말 안 돌리는 거. 일할 때만 그런 줄 알았어."
    d "오늘은 회의 자료가 없으니까 덜 돌려 말해도 될 것 같아서요."
    j "그래. 그럼 나도 곧장. 오늘 좋았어. 너랑 있어서."
    "네 시가 되기 전에 서점 입구에서 인사를 나눴다. 돌아서던 지현이 고개를 한 번 더 돌렸다."
    j "오늘 마신 차 이름, 나중에 보내. 또 마시고 싶어졌으니까."
    d "차 이름이요? 메뉴판에 있던 건데요."
    j "메뉴판에 있던 건 나도 알아. 네가 고른 거라서 다시 묻는 거야."
    j "보통은 아는 메뉴만 시켜. 근데 네가 고른 거, 이름도 처음 듣는데 맛있더라."
    d "그럼 다음에도 제가 골라요?"
    j "한 번만 더. 그다음엔 내가 고를 거야. 이번엔 무난한 거 말고."
    $ remember("jihyun_r02_time_kept")
    $ location = "같은 토요일 저녁 · 지현의 집 — 지현 시점"
    "지현은 덜 끝낸 조립물을 책상 위에 두고 오늘 마신 차 이름을 메모했다. 옆에는 다음에 보여 주고 싶은 부품 하나를 올려 뒀다."
    jn "쉬자는 말이 내 입에서 다 나오네. 다음엔 설명할 거리부터 찾지 말자."
    $ cream_focus = None
    dn "오늘 지현 씨는 세 번 웃었다. 세 번 다 내가 뭔가를 정했을 때였다."
    $ award_once("jihyun_R02", "jihyun", 7)
    $ progression_note_ending()
    return

label jihyun_r03:
    $ progression_enter("jihyun_r03")
    $ progression_checkpoint("jihyun_r03")
    $ chapter = "지현 R03 · 네 안을 다시 봤어"
    $ location = "월요일 오전 · 탕비실"
    "월요일 오전. 탕비실에서 지현과 마주쳤다. 토요일 이후 처음이었다."
    j "주말 잘 쉬었어?"
    d "네. 팀장님은요?"
    j "쉬어 봤어. 일요일에 네 말대로 그냥 걸었거든. 이십 분 만에 돌아오긴 했지만."
    d "이십 분이면 처음치고 길어요."
    j "그래? 십 분쯤 지나니까 불안하더라. 어디로 가는지 모르는 게."
    "지현이 커피를 내리면서 덧붙였다."
    j "근데 돌아오는 길에 처음 보는 꽃집이 있었어. 삼 년을 다닌 길인데."
    d "계획이 있었으면 못 봤겠네요."
    j "맞아. 보고서엔 못 쓰는 성과지만."
    "문 쪽에서 발소리가 났다. 지현은 한 걸음 물러서며 목소리를 평소대로 돌렸다."
    j "오후에 검토. 네 메모 가져와."
    d "네, 팀장님."
    "나가다 말고 지현이 아주 작게 말했다."
    j "꽃집 얘기는 너한테만 한 거야."
    dn "삼 년 다닌 길의 꽃집. 그 얘기를 들은 사람이 나 하나라는 게, 월요일 오전치고는 과분했다."
    $ location = "다음 주 월요일 오후 · 협업 자료 검토 자리"
    $ cream_focus = "jihyun"
    "지현은 ‘출근길 중심’이라 적은 가정을 다시 열었다. 검토할 곳에 표시하고 도현 쪽으로 화면을 돌렸다."
    dn "팀장이 자기 가정을 다시 연다. 회사에서 그게 얼마나 드문 일인지 나는 안다."
    if memory.get("jihyun_intro") == "evidence":
        j "점심에 다시 와도 되냐는 질문, 다시 봤어. 몇 분 얘기라도 출근길만 보긴 어렵겠네."
    elif memory.get("jihyun_intro") == "check_later" and memory.get("jihyun_followup_delivered"):
        j "다음 날 준 메모 봤어. 기록 없는 데도 표시해 줬더라. 그쪽 시간대부터 더 볼게."
    elif memory.get("jihyun_intro") == "check_later":
        j "더 확인해 본다고 했지. 결과는 아직 못 봤으니까, 지금 아는 것부터 보자."
    elif memory.get("jihyun_intro") == "compare":
        j "첫날 비교했던 두 시간대, 둘 다 다시 볼 거야. 어느 쪽이 맞는진 아직 몰라."
    else:
        j "이 시간대 가정, 다시 볼 거야. 네가 지금 확인할 수 있는 범위부터 말해."
    "지현은 도현이 쓴 메모를 시간대 표 옆에 붙였다."
    $ progression_enter("jihyun_r03.choice01")
    $ progression_checkpoint("jihyun_r03.choice01")
    menu:
        "생각을 바꾼 이유가 좋았다고 말한다.":
            d "바꾼 이유까지 말씀해 주셔서 좋았어요. 다음에도 다른 의견 있으면 말할게요."
            j "그래. 그럼 나도 또 뒤집어 볼게. 틀렸다고 말하는 거, 해 보니까 할 만하더라."
            $ remember("jihyun_r03_response", "reason")
        "나도 틀릴 수 있다고 웃는다.":
            d "저도 더 보면 생각 바뀔 수 있어요. 현장에서 물어볼 건 제가 정리할게요."
            j "좋아. 난 시간대 가정 다시 본다. 왜 바꿨는지까지 같이 남기자."
            $ remember("jihyun_r03_response", "share_check")
        "팀장님이 직접 다시 본 게 좋았다고 한다.":
            d "팀장님이 직접 다시 보셨다는 게 기억에 남아요. 제 말에 맞춰 주셨다고 생각하진 않을게요."
            j "응. 의견을 검토한 거야. 그래도 그렇게 말해 주니까 좀 기분 좋네."
            $ remember("jihyun_r03_response", "attitude")
    $ remember("jihyun_core_understanding")
    "검토가 끝나자 회의실에는 둘만 남았다. 지현은 화이트보드에 적힌 '출근길 중심'을 지우개로 지웠다. 도현이 지우개를 하나 더 집어 반대쪽부터 지웠다."
    j "안 해도 돼. 내가 쓴 거야."
    d "같이 쓴 거로 하죠. 물음표는 제가 붙였으니까요."
    "지현이 지우던 손을 멈췄다. 화이트보드 한가운데에 물음표 하나만 남았다."
    j "이건 남겨 두자. 다음에 내가 또 너무 빨리 정하면 이거 가리켜."
    d "가리켜도 화 안 내시는 거죠?"
    j "화는 낼 거야. 그래도 볼게."
    "창밖은 벌써 어두웠다. 지현은 재킷을 걸치다 말고 도현이 걸친 얇은 겉옷을 봤다."
    j "내일부터 추워진대. 목도리 해. 이건 업무 지시 아니고."
    dn "업무 지시 아니라고 굳이 덧붙였다. 퇴근길 내내 그 말만 남았다."
    $ location = "같은 월요일 퇴근 후 · 개인 메시지"
    if memory.get("jihyun_r01_topic") == "why_me":
        call phone_deliver("jihyun_r03_personal", "jihyun", "왜 따로 보자고 했냐고 물었지\n일 얘기 끝나도 네 다음 말이 궁금했어. 그날 못 한 답이야", contact="jihyun", important=True)
        $ remember("jihyun_r01_reason_answered")
    elif memory.get("jihyun_r01_topic") == "hobby":
        call phone_deliver("jihyun_r03_personal", "jihyun", "첫 구경꾼 자리 궁금하다며\n아직 덜 만들었어. 토요일에 보니까 넌 옆에서 재촉 안 하더라. 보여 줄게", contact="jihyun")
    else:
        call phone_deliver("jihyun_r03_personal", "jihyun", "업무 말고 하나 더\n지난 토요일 좋았어. 다음에도 회사 밖에서 보자", contact="jihyun", important=True)
    call phone_deliver("jihyun_r03_reply", "dohyun", "저도요. 금요일 저녁 일곱 시 어때요?\n따로 드릴 말씀이 있어요", contact="jihyun")
    call phone_deliver("jihyun_r03_confirm", "jihyun", "좋아. 회사 앞 카페\n무슨 얘긴지는 금요일까지 안 물어볼게", contact="jihyun")
    $ remember("jihyun_r04_appointment", "금요일 저녁 일곱 시, 회사 앞 카페")
    dn "기분 좋다는 말을 저렇게 어렵게 하는 사람은 처음 봤다. 그래서 더 오래 기억날 것 같다."
    $ award_once("jihyun_R03", "jihyun", 8)
    $ progression_note_ending()
    return

label jihyun_r04:
    $ progression_enter("jihyun_r04")
    $ progression_checkpoint("jihyun_r04")
    if not memory.get("jihyun_core_understanding"):
        $ progression_note_ending()
        return
    $ chapter = "지현 R04 · 결정은 같이 하자"
    $ location = "목요일 밤 열 시 · 사무실"
    "두고 온 충전기를 가지러 사무실에 돌아갔다. 불이 다 꺼진 층에 스탠드 하나만 켜져 있었다."
    "지현이 책상에서 삼각김밥 포장을 뜯고 있었다. 한 손은 여전히 마우스 위에 있었다."
    j "왜 왔어. 퇴근했잖아."
    d "충전기요. 팀장님은 저녁이 그거예요?"
    j "효율적이야. 삼 분이면 먹어."
    "도현은 충전기 대신 탕비실로 갔다. 컵라면 두 개에 물을 붓고 돌아와 하나를 지현의 책상에 놓았다."
    d "이것도 삼 분이에요. 대신 삼 분 동안은 아무것도 못 해요. 기다려야 해서."
    "지현이 컵라면과 모니터를 번갈아 보다가 마우스에서 손을 뗐다."
    j "삼 분 동안 뭐 해, 그럼."
    d "그냥 있어요."
    "둘은 스탠드 불빛 아래서 뚜껑 위에 젓가락을 올려 두고 앉아 있었다. 창밖으로 첫서리가 내린 주차장이 보였다."
    j "이상하네. 삼 분이 긴데, 안 아까워."
    dn "내일 저녁 일곱 시에 할 말이 있다. 준비한 문장은 세 개인데, 방금 그 한마디에 세 문장이 다 흐려졌다."
    $ location = "금요일 저녁 일곱 시 · 약속한 카페"
    $ cream_focus = "jihyun"
    "지현이 도현을 보고 휴대폰을 가방에 넣었다. 도현은 맞은편에 앉아 준비해 온 말을 속으로 한 번 더 굴렸다."
    dn "준비한 말은 세 문장이었다. 첫 문장부터 목이 말랐다."
    j "오늘은 네가 할 말 있다고 했지. 나도 질문 안 할게. 해."
    while not dating and not memory.get("jihyun_relationship_declined"):
        $ progression_enter("jihyun_r04.choice01")
        $ progression_checkpoint("jihyun_r04.choice01")
        menu:
            "좋아한다고 고백한다.":
                d "토요일에 네 시 돼서 헤어졌잖아요. 전 더 있고 싶었어요. 지현 씨, 저랑 사귀실래요?"
                $ cg("jihyun_r04")
                "지현은 바로 대답하려다 물컵에서 손을 뗐다. 이번에는 도현을 보며 천천히 말했다."
                j "응. 나도 좋아해. ...너무 빨리 대답했나."
                d "기다리셨다는 쪽으로 들을게요."
                j "정답이야. ...그러니까 그만 확인해."
                $ dating = True
                $ remember("jihyun_confession_accepted")
                dn "'정답이야.' 검토 회의에서나 듣던 말이 오늘은 전혀 다르게 들렸다."
                $ award_once("jihyun_R04", "jihyun", 5)
            "마음은 있지만, 겁나는 것도 말한다." if not jihyun_prepared:
                d "저 연애는 처음이에요. 마음은 분명한데, 일이랑 구분하려다가 말이 늦어질까 봐요."
                j "나도 이런 말 잘 못 해. 그래도 지금은 팀장한테 보고하는 자리 아니잖아. 늦어도 그냥 말해."
                d "일에서 의견 다르면 그대로 말할게요. 보고 싶을 때도 그냥 말할게요."
                j "회의 때 네 안에 반대해도 삐치기 없기. 나도 네 표정 보고 혼자 결론 안 낼게."
                $ jihyun_prepared = True
                $ remember("jihyun_prepared_conversation")
            "이번 회차는 연애를 시작하지 않고 동료로 지낸다 — 동료 결말로 이어짐.":
                d "저는 이번에는 동료로 지내고 싶어요. 연애를 시작하겠다는 말씀은 드릴 수 없어요."
                $ progression_enter("jihyun_r04.choice02")
                $ progression_checkpoint("jihyun_r04.choice02")
                menu:
                    "동료로 지내겠다는 뜻을 확인한다.":
                        j "알겠어. 오늘 대답은 오늘 대답대로 둘게. 업무 의견 듣는 건 그대로야."
                        $ remember("jihyun_relationship_declined")
                        call end_common
                        $ progression_note_ending()
                        return
                    "결정을 무른다.":
                        pass
                    "지현이 원하는 걸 먼저 듣는다.":
                        j "난 너랑 사귀고 싶어. 넌 어때? 네 얘기도 다시 듣고 싶어."
    if not jihyun_prepared:
        d "저 연애는 처음이에요. 고백하는 것까진 연습해 왔는데, 그다음이 더 떨리네요."
        j "난 깔끔하게 대답할 줄 알았어. 자꾸 네 얼굴 보게 되는 건 계산에 없었네."
    j "회사에선 지금처럼 의견 말해. 내 부탁도 싫으면 싫다고 하고."
    d "네. 저도 혼자 정해 놓고 따라오시라고는 안 할게요."
    j "그리고 하나 더. 사귀는 건 당분간 우리만 알아. 누구한테 말할 땐 서로 결재 받고."
    $ remember("jihyun_work_boundary", "업무 검토와 연애를 구분, 사적 부탁 거절 가능, 일정·의견은 먼저 물음")
    $ remember("jihyun_publicity", "private")
    $ progression_enter("jihyun_r04.choice03")
    $ progression_checkpoint("jihyun_r04.choice03")
    menu:
        "첫 데이트 장소는 내가 정한다.":
            d "다음엔 제가 장소 후보 가져올게요. 시간은 팀장님 비는 데로요."
            j "좋아. 후보는 세 개 이상. 이번엔 기대하면서 기다릴게."
            $ remember("jihyun_next_date_plan", "dohyun_suggests")
            dn "기대하겠다는 말 뒤에서, 지현 씨가 수첩의 '같이 정하기'에 그어 둔 밑줄을 조용히 지웠다."
        "각자 시간도, 같이 볼 날도 남기자고 한다.":
            d "각자 하던 것도 남겨 두고 싶어요. 같이 보는 날도 하나 잡고요."
            j "응. 너랑 있을 시간 만든다고 내 일정까지 다 비울 필요는 없겠네. 네 것도 그렇게 두자."
            $ remember("jihyun_next_date_plan", "own_and_shared")
        "팀장님 추천에 내 취향을 얹는다.":
            d "팀장님이 보여 주고 싶은 데도 궁금해요. 제 취향도 하나 끼워 넣을게요."
            j "좋아. 이번에도 조용한 데일 확률이 높긴 한데. 네 취향 들어갈 자리는 남겨 둘게."
            $ remember("jihyun_next_date_plan", "both_suggest")
    if memory["jihyun_next_date_plan"] == "both_suggest":
        j "아까는 지현 씨라고 하더니, 벌써 다시 팀장님이네."
    else:
        j "아까 지현 씨라고 불렀지. 그건 조금 낯설더라."
    d "좋아한다는 말보다 호칭이 더 오래 걸릴 수도 있겠네요."
    j "기다려 줄게. 대신 아까 그 말, 한 번만 더 해."
    d "좋아해요, 지현 씨."
    "지현이 컵 손잡이를 놓고 도현을 똑바로 보았다."
    j "응. 이번엔 안 서두르고 대답했어."
    $ remember("jihyun_r04_complete")
    $ remember("jihyun_first_kiss_plan", "R05에서 교제 후 선택 가능, 현재는 발생하지 않음")
    $ progression_note_ending()
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
        call special_scene("jihyun", 1)
        call jihyun_r07
        call jihyun_r08
        call work_mini_second
        call jihyun_r09
        call jihyun_r10
        call jihyun_o02_offer
        call jihyun_r10_after
        call jihyun_r11
        call special_scene("jihyun", 2)
        call jihyun_r12
        call jihyun_r13
        call jihyun_r14
        if dating and bond_trust("jihyun") <= BOND_BREAKUP_TRUST:
            call bond_breakup("jihyun")
        if dating and memory.get("jihyun_conflict") == "resolved":
            call jihyun_r15
            call jihyun_o03_offer
            call jihyun_r16
            if memory.get("jihyun_route_completed"):
                call jihyun_x01
                menu:
                    "후일담 읽기 — 약 반년 뒤 쉬는 날의 부탁":
                        call jihyun_e01
                    "본편 결말에서 마치기 — 후일담은 이번에 읽지 않음":
                        $ remember("jihyun_epilogue_skipped")
                    "다음에도 만나고 싶다고 한마디 나누고 후일담 읽기":
                        d "다음엔 제가 만나자고 연락할게요."
                        j "좋아. 이번엔 내가 기다리는 쪽 해 볼게."
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
