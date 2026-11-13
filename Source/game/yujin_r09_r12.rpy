# Yujin R09-R12: actual support, personal choices and reunion. Art stays deferred.
label yujin_r09:
    $ progression_enter("yujin_r09")
    $ progression_checkpoint("yujin_r09")
    if not dating or active_route != "yujin":
        $ progression_note_ending()
        return
    $ cream_focus = "yujin"
    $ chapter = "유진 R09 · 제안서의 마지막 이름"
    $ location = "지난 금요일 밤 · 피칭 리허설 뒤 TF 회식"
    "피칭 리허설이 끝난 금요일 밤, TF는 회사 앞 고깃집에 모였다. 유진은 도현과 한 칸 떨어진 자리에서 컵만 만지작거렸다."
    r "아 맞다, 요즘 ‘창가’라는 계정 알아요? 그림이 진짜 미쳤어요. 우리 이번 시안이랑 분위기 비슷하던데!"
    "유진의 젓가락이 그대로 멈췄다."
    s "어디 봐. ...오, 예쁘네. 유진 씨 스타일이랑 좀 닮았다?"
    y "저, 저는 이렇게 못 그려요! 그, 그리고 저는 계정 같은 거..."
    d "저도 그 계정 알아요. 근데 시안이랑은 다르던데요. 회사 건 문구가 먼저 보이고, 그 계정은 빛이 먼저 보여요."
    r "오, 도현 씨 은근 그림 보는 눈 있네~"
    "유진이 테이블 아래에서 도현의 소매를 꼭 쥐었다. 손끝이 떨리고 있었다."
    call phone_deliver("yujin_r09_dinner", "yujin", "아까 진짜 심장 떨어지는 줄 알았어요... 대신 말해 주셔서 고마워요. 그리고 빛이 먼저 보인다는 거, 그거 제가 제일 듣고 싶던 말이에요.", contact="yujin")
    $ cream_focus = "yujin"
    if memory.get("yujin_r08_availability") == "thu19":
        $ location = "일요일에 약속한 목요일 오후 · 회사 회의실"
    else:
        $ location = "일요일에 약속한 수요일 오후 · 회사 회의실"
    "검토를 앞두고 유진이 시안의 마지막 장에 이름을 적었다. 도현은 옆에서 연결한 자료 화면을 확인한다."
    y "저는 색 바꾼 이유랑 수정할 부분을 말씀드릴게요. 질문이 겹치면... 순서만 정리해 주실래요?"
    d "네. 자료는 여기까지 띄워 뒀어요."
    "검토가 시작되자 두 질문이 한꺼번에 나왔다. 유진이 첫 장을 다시 열었다."
    $ progression_enter("yujin_r09.choice01")
    $ progression_checkpoint("yujin_r09.choice01")
    menu:
        "질문을 정리하고 자료만 띄운다.":
            d "색 정한 이유부터 듣고, 수정 범위는 그다음에 볼까요? 유진 씨, 첫 장 띄울게요."
            y "네. 이 색은 입구에서도 문장이 먼저 읽히라고 넣었어요. 수정할 부분은 그 아래예요."
            "유진이 설명을 마친 뒤 도현은 요청한 비교 자료를 화면에 올렸다."
            $ remember("yujin_support_action", "materials")
            $ remember("yujin_support_consent", "자료 화면과 질문 순서, 디자인 의도는 유진이 설명")
            $ remember("yujin_support_overstep", False)
            $ remember("yujin_support_repair_status", "not_needed")
        "내가 대신 설명해 버린다.":
            d "제가 핵심부터 말씀드릴게요. 이 색은 입구에서 읽히는 순서를 생각해서—"
            y "도현 씨, 그 부분도 제가 설명하려고 했어요. 이어서 말해도 될까요?"
            d "아, 네. 말씀하세요."
            "유진이 색을 정한 이유와 수정 범위를 직접 설명했다. 도현은 입을 닫고 다음 자료를 준비했다."
            $ remember("yujin_support_action", "self_summary")
            $ remember("yujin_support_consent", "질문 순서만 요청받음, 핵심 설명을 대신할 동의 없음")
            $ remember("yujin_support_overstep", True)
            $ remember("yujin_support_repair_status", "open")
        "첫 문장만 정리해도 되는지 묻는다.":
            d "질문 두 개를 첫 문장으로만 묶어 드릴까요? 설명은 유진 씨가 하시고요."
            y "네. 질문은 두 가지라고만 말씀해 주세요. 그다음은 제가 이어갈게요."
            d "지금 질문은 색을 고른 이유와 수정 범위, 두 가지입니다. 유진 씨가 순서대로 설명하겠습니다."
            "유진이 첫 장을 짚어 설명했다. 도현은 고개를 끄덕이고 다음 화면을 기다렸다."
            $ remember("yujin_support_action", "agreed_summary")
            $ remember("yujin_support_consent", "유진이 부탁한 질문 한 문장 요약, 핵심 의도는 유진이 설명")
            $ remember("yujin_support_overstep", False)
            $ remember("yujin_support_repair_status", "not_needed")
    $ remember("yujin_r09_explained_by", "yujin")
    $ remember("yujin_r09_support_performed")
    if memory.get("yujin_r08_next_appointment"):
        $ location = memory["yujin_r08_next_appointment"] + " · 약속한 저녁"
        "일요일, 정한 시각에 카페에서 만났다. 유진이 들고 온 가방을 옆자리에 내려놓는다."
        $ remember("yujin_r09_kept_appointment", memory["yujin_r08_next_appointment"])
    else:
        $ location = "이날 퇴근 후 · 회사 앞"
        d "오늘 잠깐 카페 갈까요? 유진 씨 얘기 더 듣고 싶어요."
        y "네. 지금은 괜찮아요. 저도 할 얘기 있어요."
        $ location = "같은 저녁 · 회사 근처 카페"
        $ remember("yujin_r09_kept_appointment", "이날 새로 제안하고 동의한 카페 만남")
    if memory.get("yujin_support_overstep"):
        y "아까 설명 이어가게 해 주신 건 고마워요. 그런데... 처음부터 제가 하고 싶었어요. 그 말은 꼭 해 두고 싶어서요."
        $ progression_enter("yujin_r09.choice02")
        $ progression_checkpoint("yujin_r09.choice02")
        menu:
            "앞질러서 미안했다고 사과한다.":
                d "부담 덜어 드린다고 앞질렀어요. 부탁하신 건 순서 정리였는데요. 미안해요. 다음엔 자료만 띄우고 기다릴게요."
                y "네. 질문이 겹치면 순서만요. 설명이 막히면 제가 도와 달라고 할게요."
                $ remember("yujin_support_repair_status", "agreed_pending_action")
                $ remember("yujin_support_followup", "자료와 질문 순서만 돕고 설명 요청을 기다림")
            "왜 급했는지 털어놓는다.":
                d "말 끊기면 더 긴장하실까 봐 그랬어요. 그런데 결국 제가 정해 버렸네요."
                y "긴장해도 제 말로 하고 싶었어요. 오늘은... 그 차이를 좀 생각해 보고 싶어요."
                d "네. 다음엔 끼어들기 전에 여쭤볼게요."
                $ remember("yujin_support_repair_status", "open")
            "다음엔 끼어들기 전에 묻겠다고 한다.":
                d "질문 순서는 도와도, 답할 내용은 제가 정하면 안 되는 거죠? 다음엔 시작하기 전에 물을게요."
                y "네. 그거예요. 도와 달라고 할 때도 있을 거예요. 그땐 제가 말씀드릴게요."
                $ remember("yujin_support_repair_status", "agreed_pending_action")
                $ remember("yujin_support_followup", "대신 요약하기 전 유진에게 범위를 물음")
    else:
        if memory["yujin_support_action"] == "agreed_summary":
            y "아까 그 한 문장요. 딱 거기서 기다려 주셔서 제가 이어 말하기 좋았어요."
        else:
            y "자료가 그때그때 나와서 설명하기 편했어요. 제 차례 기다려 주신 것도요."
        $ progression_enter("yujin_r09.choice03")
        $ progression_checkpoint("yujin_r09.choice03")
        menu:
            "제일 말하고 싶었던 게 뭔지 묻는다.":
                d "유진 씨가 제일 설명하고 싶었던 데는요? 저는 마지막 수정 얘기가 궁금했어요."
                y "그거요! 예뻐서 고른 색이 아니라는 거, 그걸 말하고 싶었어요. 끝까지 듣고 계셨네요~"
                $ remember("yujin_r09_evening", "intention")
            "필요하면 날 부르라고 한다.":
                d "더 필요하면 말씀해 주세요. 저도 어디까지 하면 좋을지 미리 물을게요."
                y "네. 제가 직접 할 부분이랑 부탁할 부분, 둘 다 말해 볼게요."
                $ remember("yujin_r09_evening", "ask")
            "설명 끝나고 눈 맞춘 게 좋았다고 한다.":
                d "설명 끝나고 이쪽 한번 보셨잖아요. 그때 저 꽤 뿌듯했는데요."
                y "저는 끝났으니까 이제 웃어 주셔도 된다는 뜻이었어요. ...지금도요."
                $ remember("yujin_r09_evening", "look")
    "유진이 가방 지퍼를 닫았다. 도현도 회사 메모를 접어 넣는다."
    y "오늘 회사 얘기는 여기까지요. 이제는 그냥... 도현 씨 보고 싶어서 나온 사람으로 있을래요."
    d "그럼 저도 질문 바꿀게요. 이번 토요일, 저랑 좀 오래 있어 줄래요?"
    y "네. 이번에는 제가 보여 드릴 페이지도 가져갈게요~"
    $ remember("yujin_r10_appointment", "같은 주 토요일 오후, 카페에서 개인 노트와 기록집 보기")
    $ award_once("yujin_R09", "yujin", 6)
    $ progression_note_ending()
    return

label yujin_r10:
    $ progression_enter("yujin_r10")
    $ progression_checkpoint("yujin_r10")
    if not dating or active_route != "yujin":
        $ progression_note_ending()
        return
    $ cream_focus = "yujin"
    $ chapter = "유진 R10 · 아직 남겨 둔 페이지"
    $ location = "같은 주 토요일 오후 · 동네 카페"
    "유진이 개인 노트를 펼쳤다. 안쪽 주머니에서 지난 전시 티켓이 나왔다."
    y "이거 붙일 자리 정하려다가... 오늘 같이 보려고 아껴 뒀어요."
    if memory.get("yujin_r02_plan") == "follow":
        y "같은 방인데 빛이 다른 두 그림, 번갈아 보셨잖아요. 저는 그 사이에 서 있던 게 생각나요."
    elif memory.get("yujin_r02_plan") == "window":
        y "창가 그림 보고 돌아왔을 때요. 처음 그림이 좀 달라 보였잖아요. 돌아가는 화살표도 그려 놨어요."
    elif memory.get("yujin_r02_plan") == "linger":
        y "첫 그림 앞에 오래 있었죠. 저는 티켓 옆에 그 시간을 적어 두고 싶어요."
    else:
        y "저는 티켓보다 옆에 어떤 말을 남길지가 더 어렵더라고요. 도현 씨는 뭘 적고 싶으세요?"
    d "저는 지금도 같이 보고 있다는 거요. 그날 표는 한 장인데 얘기는 자꾸 생기네요."
    y "그건... 티켓 옆에 그대로 적어도 돼요? 제 말인 척은 안 할게요~"
    "도현이 웃으며 고개를 끄덕였다. 유진은 방금 들은 말을 날짜 아래에 적었다."
    $ remember("yujin_r10_ticket_note", "그날 표는 한 장인데 얘기는 자꾸 생긴다")
    "이번에는 도현이 자기 기록집 노트를 펼쳤다."
    if memory.get("yujin_r05_layout") == "photo_first":
        y "지난번 사진 먼저 보던 구성은 남겨 두셨네요. 이번엔 다음 장으로 넘어가는 게 궁금해요."
    elif memory.get("yujin_r05_layout") == "text_first":
        y "그 한 줄 읽고 사진 넘기던 순서요. 다음 페이지도 글부터일 필요는 없겠죠?"
    elif memory.get("yujin_r05_layout") == "spread":
        y "같이 놓고 보니까 빈 공간도 그림 같았어요. 다음 장은 조금 달라도 재밌겠어요."
    d "네. 아직 후보예요. 오늘은 다음 페이지 같이 봐 주실래요? 혼자 보니까 자꾸 첫 장으로 돌아가네요."
    "유진이 노트 두 권을 겹치려다가 도현의 것을 다시 가운데 놓았다."
    y "또 첫 장으로 가시면 제가 여기 잡고 있을게요. 오늘은 다음 장도 보고 싶어요."
    $ progression_enter("yujin_r10.choice01")
    $ progression_checkpoint("yujin_r10.choice01")
    menu:
        "전시장 입구 긴 의자로 정한다.":
            d "저는 그날 앉았던 의자요. 사진은 다음에 찍고, 둘이 앉았던 날짜도 남기고 싶어요."
            y "저는 거기서 무슨 말 할지 고민하던 게 생각나요. 의자보다 옆자리가 더 신경 쓰였거든요."
            d "저도 조용해서 좋았다고만 할 뻔했네요."
            y "그날도 그러셨어요? 저만 말 고민한 거 아니었네요~"
            "유진이 티켓을 노트 안쪽 주머니에 넣고 빈 페이지를 펼쳐 보였다."
            y "사진은 나중에 여기서 같이 봐요. 그때도 의자 얘기만 하시면 제가 캐물을 거예요."
            $ remember("yujin_r10_page", "entrance_bench")
            $ remember("yujin_r10_impression", "도현은 함께 앉은 날짜, 유진은 옆자리에서 고르던 다음 말")
        "사진 없이 그 한 문장만 놓는다.":
            d "저는 방금 티켓 옆에 적은 말이요. 사진 없는 장도 하나 두고 싶어요."
            "유진이 티켓 옆에 방금 적은 말을 읽었다가 도현의 빈 페이지를 봤다."
            y "제 노트에 제가 먼저 적었는데, 벌써 가져가세요?"
            d "원래 제가 한 말인데요?"
            y "알아요~ 그런데 이쪽에도 남겨 주세요. 그 말 듣고 오늘 여기서 적은 거니까요."
            "도현이 유진의 노트를 돌려줬다. 유진은 같은 문장을 끝까지 한 번 더 읽었다."
            $ remember("yujin_r10_page", "one_sentence")
            $ remember("yujin_r10_impression", "도현은 오늘 고른 한 문장, 유진은 넘기기 전 머무는 시간")
        "빈칸을 남겨 두자고 한다.":
            d "저는 이쪽에 빈칸 남길래요. 다음에 같이 걷고 나서 적을 말도 있었으면 해서요."
            y "여기엔 아직 아무것도 안 그릴게요. 나중에 같이 걷고 나서 도현 씨가 채우세요."
            d "그러다 다음에도 비어 있으면요?"
            y "같이 걸었으면 괜찮아요. ...다녀와서 저보다 노트부터 펴시면 조금 삐칠 거고요~"
            d "그럼 노트는 가방 안에요. 유진 씨랑 얘기하고 꺼낼게요."
            $ remember("yujin_r10_page", "open_space")
            $ remember("yujin_r10_impression", "도현은 다음 만남 뒤 채울 빈칸, 유진은 기록보다 먼저 정하는 약속")
    $ remember("yujin_r10_booklet_state", "다음 페이지 후보를 고름, 촬영·책 전체 완성 아님")
    $ remember("yujin_r10_help_received", "유진이 독자로서 감상을 말하고 도현이 구성 후보를 선택함")
    "유진이 작업 수첩과 개인 노트를 따로 정리했다. 도현은 정한 후보 옆에 오늘 날짜를 적고, 남은 노트 쪽으로 손을 뻗었다."
    y "잠깐만요, 그건 제 노트예요."
    "도현이 겹쳐 둔 두 권 중 위쪽 것을 내려놓았다. 펼쳐진 장 구석에 ‘창가’ 서명이 든 스케치가 보였다. 유진이 노트를 얼른 가방에 넣었다."
    d "회사에서 그거 펼쳐 놓으면 들켜요."
    y "그러니까 도현 씨 앞에서만 펼치는 거예요~ 오늘은 여기까지만요."
    y "그런 말 들으면 보여 드릴 게 자꾸 늘어날 텐데... 내일은 음악 하나 어때요?"
    d "좋아요. 저도 한 곡 가져올게요."
    $ remember("yujin_r11_appointment", "다음 날 일요일 저녁, 유진 집에서 음악 추천을 나눔")
    y "그리고 저희 사귀는 거요. 지현 팀장님한테는 말씀드리고 싶어요. 회사 전체 말고 그분 한 명한테요."
    d "축하받고 싶으세요?"
    y "네. ...도현 씨 여자친구라고 말해 보고 싶은 것도 있어요. 제가 혼자만 알고 있는 것 같아질 때가 있어서요."
    $ progression_enter("yujin_r10.choice02")
    $ progression_checkpoint("yujin_r10.choice02")
    menu:
        "팀장님한테만 말하자고 한다.":
            d "네. 내일 같이 메시지 보낼까요? 사귄다는 것까지만요."
            y "좋아요. 축하받고 싶어서요. 나머지 얘기는 저희끼리만요."
            $ remember("yujin_publicity", "agreed_jihyun")
        "당분간 둘만 알자고 한다.":
            d "저는 좀 더 둘만 알고 싶어요. 나중에 다시 얘기해도 될까요?"
            "유진은 바로 대답하지 않고 노트 귀퉁이를 접었다가 폈다."
            y "좀 아쉽긴 해요. 그래도 둘만 아는 거랑, 제가 여자친구가 아닌 건 다른 얘기죠."
            d "네. 숨기고 싶은 사람이어서 그런 건 아니에요."
            y "알겠어요. 오늘 말 안 한다고 저 혼자 이상한 결론 내리지는 않을게요."
            $ remember("yujin_publicity", "private")
        "알리고 싶은 마음부터 듣는다.":
            d "알리고 싶은 이유 좀 더 듣고 싶어요. 오늘 결정하지는 말고요."
            y "좋아하는 사람 생겼다고 자랑하고 싶은 마음도 있어요. ...말로 하니까 더 부끄럽네요."
            d "그 마음은 좋아요. 저는 좀 더 익숙해지고 나서 같이 말하고 싶어요."
            y "네. 지금은 도현 씨한테만 자랑한 걸로요~ ...서운한 건 좀 있는데, 그걸로 재촉하진 않을게요."
            $ remember("yujin_publicity", "private")
            $ remember("yujin_disclosure_reason_heard")
    $ award_once("yujin_R10", "yujin", 4)
    $ progression_note_ending()
    return

label yujin_r11:
    $ progression_enter("yujin_r11")
    $ progression_checkpoint("yujin_r11")
    if not dating or active_route != "yujin":
        $ progression_note_ending()
        return
    $ cream_focus = "yujin"
    $ chapter = "유진 R11 · 제안한 사람의 마음"
    $ location = "다음 날 일요일 저녁 · 유진의 집"
    "유진이 작은 음악 기기 옆을 비우고 컵 두 개를 가져왔다. 도현은 골라 온 곡 이름을 적었다."
    if memory.get("yujin_publicity") == "agreed_jihyun":
        "어제 정한 대로, 지현에게 같이 메시지를 보냈다."
        $ location = "같은 일요일 저녁 · 지현에게 함께 보낸 개인 메시지"
        call phone_deliver("yujin_disclosure_1", "dohyun", "팀장님, 저희 둘이 사귀게 됐어요. 유진 씨랑 같이 보내는 거예요. 다른 분들께는 아직 말하지 말아 주세요.", contact="jihyun")
        call phone_deliver("yujin_disclosure_2", "jihyun", "축하해요, 두 사람. 두 분이 직접 말하기 전까지는 나도 다른 사람에게 말하지 않을게요.", contact="jihyun", important=True)
        call phone_deliver("yujin_disclosure_3", "jihyun", "유진 씨가 정한 문장이죠? 오늘은 수정 의견 안 달게요. 좋은 저녁 보내요 :)", contact="jihyun")
        $ remember("yujin_disclosed_to", "jihyun")
        $ phone_active_contact = "yujin"
        $ location = "같은 일요일 저녁 · 유진의 집"
        y "답장 오기 전까지 화면만 봤네요. ...이제 노래 고를까요?"
        d "네. 오늘 수정 의견은 안 온다고 하셨으니까요~"
    else:
        "유진은 컵을 내려놓고 휴대폰을 뒤집어 뒀다."
        y "오늘은 저희끼리만 아는 저녁이네요. 들려드리려고 아껴 둔 게 있어요."
    y "제 추천은 ‘창가에 남은 오후’예요. 피아노랑 기타가 조용히 이어져요. 그림 그리기 전에 듣는 곡이에요."
    d "저는 ‘한 정거장 더’요. 기타랑 가벼운 리듬이 있어서 걸을 때 듣고 싶었어요."
    $ progression_enter("yujin_r11.choice01")
    $ progression_checkpoint("yujin_r11.choice01")
    menu:
        "유진의 잔잔한 곡부터 듣는다.":
            "유진이 고른 곡을 들었다. 유진은 컵을 쥔 채 도현의 반응을 기다렸다."
            d "저는 마지막 음이 남는 게 좋네요. 끝나기 전에 좀 더 앉아 있고 싶어져요."
            "곡이 끝났는데 유진의 손은 재생 버튼 옆에 남아 있었다."
            y "한 번 더 들어도 돼요? 이번엔 마지막 음에서 도현 씨 표정도 보려고요."
            d "저도요. 아까는 곡 얘기 생각하느라 유진 씨를 늦게 봤어요."
            $ remember("yujin_r11_music", "yujin_calm")
            $ remember("yujin_r11_heard", ["창가에 남은 오후"])
            $ remember("yujin_r11_music_impression", "도현은 마지막 음 뒤 머무는 시간, 유진은 다음 선을 생각하는 여백")
        "내 경쾌한 곡부터 듣는다.":
            "도현이 가져온 곡을 함께 들었다. 유진이 리듬을 따라 손가락을 조금 움직였다."
            d "저는 이 부분에서 한 정거장 더 걸어도 되겠다 싶었어요."
            y "저는 누굴 만나러 가는 길 같아요. 도현 씨 생각하면서 들으니까 약속에 늦으면 안 될 것 같고요~"
            d "늦지는 마세요. 기다리는 사람 마음도 생각해 주시고요~"
            y "오늘은 제가 집에서 기다렸는데요? 다음엔 제가 찾아갈게요~"
            $ remember("yujin_r11_music", "dohyun_bright")
            $ remember("yujin_r11_heard", ["한 정거장 더"])
            $ remember("yujin_r11_music_impression", "도현은 더 걷고 싶은 길, 유진은 누군가를 만나러 가는 걸음")
        "한 곡씩 번갈아 듣는다.":
            "유진의 곡을 들은 뒤 도현의 곡으로 바꿨다. 곡 이름 옆에 듣고 싶은 순간을 하나씩 적었다."
            d "저는 만남 전에 걸을 땐 제 곡, 돌아와서 조금 더 있을 땐 유진 씨 곡이요."
            y "저는 기다릴 땐 조용한 쪽이요. 만나러 나갈 때는 도현 씨 곡 틀어 보고 싶어요."
            d "그럼 오늘 제 곡 차례는 이미 지났네요."
            "유진이 재생 목록의 다음 곡을 도현 쪽으로 돌려 보여 줬다."
            y "네. 다음 곡은 아직 남았어요. 도현 씨도... 좀 더 계셔야 하고요~"
            $ remember("yujin_r11_music", "both")
            $ remember("yujin_r11_heard", ["창가에 남은 오후", "한 정거장 더"])
            $ remember("yujin_r11_music_impression", "둘이 만남 전 걸음과 만남 뒤 머무는 시간을 다르게 골랐음")
    $ remember("yujin_r11_music_shared")
    "유진이 곡 이름 옆 메모를 도현 쪽으로 돌렸다. 도현은 다음 주 일정이 적힌 작은 수첩을 펼친다."
    d "저 월요일부터 수요일까지 외근이에요. 저녁에도 정리가 있어서 평소처럼 만나긴 어려울 것 같아요."
    y "저도 수요일까지 납품 마감이에요. 보고 싶은 날이랑 시간 되는 날이 꼭 같지는 않네요."
    d "그럼 짧게라도 연락할게요. 답장은 편할 때 하시고요."
    y "네. 목요일엔 제가 시간 여쭤볼게요. 그때까진 좀 기다리는 걸로요~"
    $ remember("yujin_r11_busy_plan", "월~수 도현 외근·유진 납품 마감, 목요일 만남은 다시 확인하기로 함")
    $ award_once("yujin_R11", "yujin", 0)
    $ progression_note_ending()
    return

label yujin_r12:
    $ progression_enter("yujin_r12")
    $ progression_checkpoint("yujin_r12")
    if not dating or active_route != "yujin":
        $ progression_note_ending()
        return
    $ chapter = "유진 R12 · 먼저 잡은 재회"
    $ location = "다음 주 월요일 저녁 · 각자의 일정, 개인 메시지"
    call phone_deliver("yujin_r12_mon", "dohyun", "외근 끝나고 정리 중이에요. 아까 지나간 길에 유진 씨 생각나는 창문이 있었어요. 다음에 얘기해 드릴게요.", contact="yujin")
    call phone_deliver("yujin_r12_mon_y", "yujin", "저는 아직 작업실이에요. 무슨 창문인지 궁금해졌어요. 제 생각났다는 부분은 두 번 읽었어요. ...오늘 좀 듣고 싶었거든요 :)", contact="yujin")
    $ location = "화요일 밤 · 각자의 집, 개인 메시지"
    if memory.get("yujin_r11_music") == "yujin_calm":
        call phone_deliver("yujin_r12_tue", "yujin", "지난번 같이 들은 ‘창가에 남은 오후’요. 마지막 음 들을 때 옆자리 생각이 나네요. 오늘은 곡 끝나면 쉬려고요.", contact="yujin")
    elif memory.get("yujin_r11_music") == "dohyun_bright":
        call phone_deliver("yujin_r12_tue", "yujin", "같이 들은 ‘한 정거장 더’ 다시 들었어요. 오늘은 한 정거장 더 말고 바로 집에 왔지만요~ 다음엔 만나러 갈 때 틀어 볼래요.", contact="yujin")
    elif memory.get("yujin_r11_music") == "both":
        call phone_deliver("yujin_r12_tue", "yujin", "번갈아 들은 두 곡 중에 오늘은 조용한 쪽이요. 만나러 가는 날엔 도현 씨 곡 고르기로 한 거 기억해요.", contact="yujin")
    else:
        call phone_deliver("yujin_r12_tue", "yujin", "오늘은 좀 일찍 집에 왔어요. 다음에 만나면 도현 씨 외근 얘기부터 듣고 싶어요.", contact="yujin")
    call phone_deliver("yujin_r12_tue_d", "dohyun", "저도 오늘은 여기까지만 할게요. 만나서 얘기할 건 남겨 두고요. 잘 자요, 유진 씨.", contact="yujin")
    $ location = "수요일 저녁 · 각자의 집, 개인 메시지"
    call phone_deliver("yujin_r12_invite", "yujin", "납품 끝났어요! 내일 저녁에 만날까요? 저는 여섯 시 반부터 괜찮아요. 그냥 보고 싶어서요.", contact="yujin", important=True)
    $ phone_context = "yujin_r12_reunion_reply"
    $ progression_enter("yujin_r12.choice01")
    $ progression_checkpoint("yujin_r12.choice01")
    call screen office_phone(replies=[("cafe1830", "목요일 여섯 시 반, 카페에서 만나자고 한다."), ("cafe19", "목요일 일곱 시가 편하다고 제안한다."), ("bookshop1830", "목요일 여섯 시 반, 서점 앞에서 만나자고 한다.")])
    $ remember("yujin_r12_reunion_reply", _return)
    $ phone_context = None
    if memory["yujin_r12_reunion_reply"] == "cafe19":
        $ remember("yujin_r12_appointment", "목요일 저녁 일곱 시 · 회사 근처 카페")
        call phone_deliver("yujin_r12_reply", "dohyun", "저는 일곱 시가 편해요. 회사 근처 카페에서 만날까요? 보고 싶었어요.", contact="yujin")
    elif memory["yujin_r12_reunion_reply"] == "bookshop1830":
        $ remember("yujin_r12_appointment", "목요일 저녁 여섯 시 반 · 동네 서점 앞")
        call phone_deliver("yujin_r12_reply", "dohyun", "여섯 시 반 좋아요. 이번엔 서점 앞에서 볼까요? 얼굴 보고 조금 걷고 싶어요.", contact="yujin")
    else:
        $ remember("yujin_r12_appointment", "목요일 저녁 여섯 시 반 · 회사 근처 카페")
        call phone_deliver("yujin_r12_reply", "dohyun", "여섯 시 반에 카페에서 봬요. 저도 기다리고 있었어요.", contact="yujin")
    call phone_deliver("yujin_r12_confirm", "yujin", "네. 달력 말고 이제 도현 씨 얼굴 보러 갈게요~ 내일 만나요.", contact="yujin")
    $ location = memory["yujin_r12_appointment"]
    $ cream_focus = "yujin"
    "약속한 곳에 유진이 와 있었다. 도현을 보자 들고 있던 가방을 양손으로 고쳐 잡았다."
    y "메시지로는 할 말 많았는데. 지금은 인사부터 하고 싶어요. 보고 싶었어요."
    d "저도요. 말 고르다 또 늦어지기 전에 말할게요."
    if memory.get("yujin_r11_music") == "yujin_calm":
        y "혼자 그 곡 들을 땐 옆자리가 비어 있었는데, 오늘은 도현 씨가 있네요. 좀 더 같이 있고 싶어요."
    elif memory.get("yujin_r11_music") == "dohyun_bright":
        y "오늘은 그 곡 들으면서 만나러 왔어요. 한 정거장 더 걸으면 늦을까 봐 딱 여기까지만요~"
    elif memory.get("yujin_r11_music") == "both":
        y "만나러 오는 곡 순서는 지났어요. 이제는... 같이 있는 곡 틀어도 되죠?"
    "자리를 잡고 월요일에 본 창문과 이번 주 얘기를 짧게 나눴다. 유진이 작업 수첩을 꺼내려다 멈춘다."
    if memory.get("yujin_support_overstep"):
        if memory.get("yujin_support_repair_status") == "open":
            y "그날 설명 가로채셨던 얘기도요. 제가 원하는 도움을 아직 제대로 말씀 못 드린 것 같아요. 다음 검토 전에 잠깐 맞춰 보고 싶어요."
        else:
            y "지난번에 미리 물어보시기로 한 거요. 내일 검토가 짧아져서, 어디까지 부탁드릴지 다시 말씀드리고 싶어요."
    elif memory.get("yujin_support_action") == "agreed_summary":
        y "지난번 질문 한 문장으로 정리해 주신 건 좋았어요. 내일은 검토 시간이 짧아져서, 부탁드릴 부분을 다시 정하고 싶어요."
    elif memory.get("yujin_support_action") == "materials":
        y "지난번처럼 제가 설명하고 싶어요. 내일은 검토 시간이 짧아져서, 자료랑 질문 순서를 조금 다르게 부탁드릴 것 같아요."
    else:
        y "내일 짧은 검토가 하나 있어요. 이번엔 어떤 도움이 필요한지 제가 말씀드리고 싶어요."
    $ progression_enter("yujin_r12.choice02")
    $ progression_checkpoint("yujin_r12.choice02")
    menu:
        "필요한 도움을 듣고 내일 맞추자고 한다.":
            d "유진 씨가 직접 말할 부분부터 들을게요. 내일 시작 전에 자료랑 순서 같이 볼까요?"
            y "네. 오늘은 그 약속까지요. 정확한 순서는 내일 자료 보고 제가 말씀드릴게요."
            $ remember("yujin_r12_support_request", "내일 시작 전 유진의 설명 범위와 자료·질문 순서를 확인")
            if memory.get("yujin_support_overstep") and memory.get("yujin_support_repair_status") == "open":
                $ remember("yujin_support_repair_status", "agreed_pending_action")
        "약속은 그대로, 세부는 내일 정하자고 한다.":
            d "말씀하신 건 기억할게요. 구체적인 순서는 내일 시작 전에 같이 봐요. 제가 혼자 정하진 않을게요."
            y "네. 그 얘기는 내일 제가 꺼낼게요. 오늘은 만나서 좋다는 말을 좀 더 하고 싶어요."
            $ remember("yujin_r12_support_request", "기존 기록을 보존하고 구체적 지원 범위는 내일 다시 합의")
        "부탁한 만큼만 돕겠다고 한다.":
            d "요약이 필요하시면 범위부터 말씀해 주세요. 시작하기 전에 한 번 더 확인할게요."
            y "네. 어떤 문장까지인지 같이 정해요. 제 답은 제가 이어가고요."
            $ remember("yujin_r12_support_request", "부탁받은 요약 범위를 먼저 확인하고 유진이 답을 이어감")
            if memory.get("yujin_support_overstep") and memory.get("yujin_support_repair_status") == "open":
                $ remember("yujin_support_repair_status", "agreed_pending_action")
    "아직 하지 않은 내일 일은 수첩에 남겼다. 유진이 가방을 닫고 몸을 도현 쪽으로 돌렸다."
    y "이제 그 창문 얘기요. 제 생각났다는 부분은 좀 자세히 들려주세요~"
    d "빛보다 유진 씨가 생각난 건 맞아요. 유진 씨라면 어디서 멈춰 볼지 궁금했거든요."
    "그날 얘기를 나누고 저녁을 먹었다. 유진은 평소와 다른 옷소매를 한번 내려다본다."
    y "오늘 옷도 좀 오래 골랐어요. 알아봐 달라고 말하려니까... 지금이 더 부끄럽네요."
    d "알아봤어요. 예쁘다는 말부터 하고 싶었는데 인사가 튀어나와 버렸네요."
    "유진은 소매를 만지던 손을 내려놓고 도현의 눈을 마주 봤다."
    y "그 말은 지금 들어도 좋아요. ...이번엔 제가 안 피했네요. 도현 씨가 먼저 보셨는데~"
    d "졌네요. 그런데 다시 봐도 돼요?"
    y "네. 오늘은 저도 더 보고 싶어요. ...집에 들르실래요?"
    $ progression_enter("yujin_r12.choice03")
    $ progression_checkpoint("yujin_r12.choice03")
    menu:
        "나도 더 함께 있고 싶다고 답한다 — 친밀한 장면으로 이어짐.":
            d "네. 오늘은 저도 더 같이 있고 싶어요."
            $ location = "같은 목요일 밤 · 유진의 집"
            "함께 집에 들어와 가방을 내려놨다. 유진은 할 말을 찾는 대신 도현을 바라봤다."
            call event_sequence("yujin_r12", "special")
            if not event_main_reached:
                "(장면 생략 · 시간이 흐릅니다.)"
            $ remember("yujin_r12_intimacy", "shared")
            y "오늘은 같이 있다는 말이 메시지가 아니라서 좋네요."
            d "저도요. 지금은 답장 고를 시간도 필요 없네요."
        "오늘은 집에 간다.":
            $ location = "같은 목요일 밤 · 정류장"
            d "오늘은 집에서 쉴게요. 다음에 더 같이 있을 날도 정하고 싶고요."
            y "네. 저도 오늘 좋았어요. 집에 도착하시면 톡 주세요. 다음에 어디 갈지도 얘기하고 싶어요."
            "정류장에서 인사를 나눴다."
            $ remember("yujin_r12_intimacy", "deferred")
        "조금 더 걷고 각자 쉰다.":
            $ location = "같은 목요일 밤 · 유진의 집 앞"
            d "오늘은 좀 더 걷고 싶어요. 집 앞까지 얘기하면서 가도 될까요? 그다음엔 각자 쉬고요."
            y "좋아요. 다음 모퉁이까진 제가 말할래요~"
            "유진의 집 앞까지 함께 걸었다. 현관 앞에서 인사한 뒤 도현은 돌아갔다."
            $ remember("yujin_r12_intimacy", "walk")
    $ remember("yujin_r12_reunion_kept", memory["yujin_r12_appointment"])
    $ remember("yujin_r12_complete")
    $ award_once("yujin_R12", "yujin", 4)
    $ progression_note_ending()
    return
