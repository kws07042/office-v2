label seoyun_r05:
    $ progression_enter("seoyun_r05")
    $ progression_checkpoint("seoyun_r05")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R05 · 단골이 되는 순서"
    $ location = "고백 다음 날 토요일 오후 두 시 · 약속한 장소"
    s "오늘 약속, 달력에 네 이름으로 적었어. ‘볼일’이라고 썼다가 고쳤고."
    d "제 이름이면 어떤 표정으로 적으셨어요?"
    s "그건 안 보여 주지~ 대신 지금 내 얼굴 보면 비슷할걸."
    if memory["seoyun_next_date_plan"] == "bookcafe":
        "서점에서 만나 안쪽 북카페에 앉았다. 문이 열릴 때마다 작은 종이 울렸다."
        s "이 자리 자꾸 오면 책보다 사람 기다리는 단골 되겠다."
        d "저는 그 이유도 좋아요. 오늘은 문 열릴 때마다 서윤 씨부터 찾았고요."
        $ remember("seoyun_r05_place", "작은 종이 울리는 북카페")
    elif memory["seoyun_next_date_plan"] == "walk":
        "강변 입구에서 만나 도현이 궁금했던 낮은 다리까지 걸었다. 돌아오는 길에 골목 카페에 들렀다."
        s "오늘은 네가 어디서 멈추나 보면서 왔어. 난간 그림자는 나도 그냥 지나칠 뻔했네."
        d "다음에 혼자 와도 오늘 본 데서 한 번 더 멈출 것 같아요."
        $ remember("seoyun_r05_place", "강변의 낮은 다리와 돌아오는 골목 카페")
    else:
        "서점 앞에서 만나 오늘은 골목 안쪽으로 걷기로 했다. 작은 카페의 그늘진 창가가 마음에 들어 앉았다."
        s "아무것도 안 정하고 오니까 네가 창가 찾는 것도 보네."
        d "서윤 씨가 여기서 걸음 늦추시는 것도 보고요."
        $ remember("seoyun_r05_place", "함께 고른 골목 카페의 그늘진 창가")
    if memory.get("seoyun_r03_affection") == "hug":
        s "수요일에 인사하고 헤어졌을 때 있지. 그 뒤로 네 다음 말이 계속 궁금했어."
    elif memory.get("seoyun_r03_affection") == "hand":
        s "수요일엔 손만 잡고 인사했지. 오늘은 헤어질 시간까지 천천히 써 보자."
    else:
        s "수요일에 또 오고 싶다고 했잖아. 진짜 오니까 또 좋네."
    if memory.get("seoyun_first_kiss"):
        d "어제는 카페 나와서도 자꾸 웃었어요. 오늘은 좀 덜 들킬 줄 알았는데요."
        s "지금도 다 보여~ 나도 거울 봤으면 똑같았을걸."
    else:
        s "어제 네가 편한 만큼만 말해 준 것도 좋았어. 오늘 인사는 미리 정하지 말자."
    "함께 주문한 과자가 나왔다. 서윤이 컵을 내려놓자 창가 그림자가 잔받침 위에 걸렸다. 도현이 노트를 꺼내자 서윤도 그 모서리를 봤다."
    s "뭐 적으려고? 잠깐, 나도 여기서 하나 찾아볼래. 답은 네 거 먼저 듣고~"
    $ progression_enter("seoyun_r05.choice01")
    $ progression_checkpoint("seoyun_r05.choice01")
    menu:
        "문 여닫는 소리를 적는다.":
            "도현은 문 여닫는 소리와 탁자에 컵을 내려놓는 소리를 메모했다."
            d "사람이 안 보여도 누가 잠깐 다녀갔는지는 남는 것 같아서요."
            "서윤이 컵을 들어 잔받침에 가볍게 내려놓았다."
            s "이 소리 다음엔 혼자 남은 자리가 생각나네."
            d "저는 막 사람이 앉은 쪽이요."
            s "그러네. 앞에 사람이 있으면 자꾸 다음 말을 기다리게 되지."
            $ remember("seoyun_r05_subject", "사람이 다녀간 뒤 남는 작은 소리")
            $ remember("seoyun_r05_impression", "소리 뒤에 잠깐 혼자 남은 자리")
        "빛과 그늘이 갈리는 자리를 적는다.":
            "도현은 빛이 걸린 모서리를 손으로 가리켰다. 아직 사진은 찍지 않았다."
            d "다 밝은 데보다 여기부터 보고 싶어요. 다음에 카메라 들고 오고 싶고요."
            "서윤이 손을 조금 옮겨 모서리의 그림자를 바꿨다."
            s "이러면 다음에 카메라 가져왔을 때랑 달라지겠다."
            d "그때도 여기 계셔야겠네요. 같은 그림자 만들어 주시려면요."
            s "...사진 후보 찾다가 사람까지 예약하네?"
            $ remember("seoyun_r05_subject", "그늘과 빛이 만나는 모서리, 촬영 전 후보")
            $ remember("seoyun_r05_impression", "그늘 쪽에 앉은 사람의 시선이 궁금함")
        "또 와서 앉고 싶은 이유를 적는다.":
            d "‘한 번 더 앉아도 되는 곳.’ 지금은 이렇게 남길래요."
            s "한 번 더? 나는 벌써 다음 잔 생각하고 있었는데."
            d "좋네요. 문장은 제가 썼는데 서윤 씨가 바로 실천하시네요."
            s "계속 앉아 있고 싶으면 다음 잔은 네가 시켜도 되고~"
            $ remember("seoyun_r05_subject", "한 번 더 앉아도 되는 곳이라는 메모")
            $ remember("seoyun_r05_impression", "스스로 다시 오고 싶은 느낌")
    "도현이 노트를 넣자 서윤이 접시의 마지막 과자를 가리켰다."
    s "아까부터 저거 양보하는 중이었어?"
    d "아뇨. 서윤 씨 드시는 속도 보고 있었어요. 제 몫이 남나 해서요."
    s "그럼 서로 먹고 싶었던 거네~ 반 나눌까?"
    "반으로 가르자 한쪽이 훨씬 커졌다. 서윤이 큰 쪽을 집으려다 멈췄다."
    d "그거 드세요. 방금은 진짜 양보예요."
    s "...이렇게 말하면 작은 쪽 집으려고 했다는 변명도 못 하겠네."
    "서윤이 큰 조각을 먹었다. 도현도 제 몫을 집자 이번엔 말 대신 접시를 가까이 밀어 줬다."
    $ award_once("seoyun_R05", "seoyun", 4)
    $ progression_note_ending()
    return

label seoyun_r06:
    $ progression_enter("seoyun_r06")
    $ progression_checkpoint("seoyun_r06")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R06 · 우리 얘기부터 정하자"
    $ location = "다음 주 수요일 저녁 · 동네 식당"
    s "아까 네가 부르는 말 못 들었어. 메뉴 보느라."
    d "서윤 선배요."
    s "응. 잘 들리네. ...둘이 있을 땐 다른 것도 조금 기대했어."
    d "저는 좀 더 생각해 봐야겠는데요. 그래도 한번 불러 보고 싶어요."
    $ progression_enter("seoyun_r06.choice01")
    $ progression_checkpoint("seoyun_r06.choice01")
    menu:
        "‘서윤 누나’라고 불러 본다.":
            d "서윤 누나. 둘이 있을 때는 이렇게 불러도 돼요?"
            s "응. 방금 대답 한 번 더 하게 만들고 싶은데?"
            $ remember("seoyun_private_name", "서윤 누나")
        "‘서윤 씨’가 좋다고 한다.":
            d "저는 서윤 씨라고 부르는 게 좋아요. 이름을 생각하면서 부르는 느낌이라서요."
            s "좋아. 그런 뜻으로 부르면 나도 몇 번이고 돌아보게 되겠네."
            $ remember("seoyun_private_name", "서윤 씨")
        "아직은 ‘서윤 선배’, 대신 보고 싶다고 말한다.":
            d "아직은 서윤 선배가 좀 편해요. 대신 보고 싶어서 부르는 거라는 건 꼭 말할게요."
            s "좋아. 대신 선배가 밥 먹자고 부르면 업무 표정으로 오지 말기~"
            $ remember("seoyun_private_name", "서윤 선배")
    s "나는 둘이 있을 땐 도현아, 하고 부르고 싶어. 회사에서는 도현 씨고."
    d "좋아요. 지금 한번 불러 주세요. 메뉴판 말고 저 보면서요."
    s "도현아."
    "도현이 대답하자 서윤은 주문하려던 메뉴 이름을 잠깐 잊었다."
    s "...이상하네. 부르는 쪽이 덜 떨릴 줄 알았는데."
    $ progression_enter("seoyun_r06.choice02")
    $ progression_checkpoint("seoyun_r06.choice02")
    menu:
        "장난은 좋지만 진심은 진짜로 말해 달라고 한다.":
            d "장난 주고받는 건 좋아요. 좋아한다는 말은 진심인 걸 알게 해 주세요."
            s "응. 좋아해."
            d "...그렇게 바로 말씀하실 줄은 몰랐는데."
            s "장난 빼 달라며. 다음엔 네가 해~"
            $ remember("seoyun_expression", "sincere_first")
        "사람 많은 데선 조용히 하자고 한다.":
            d "둘만 있을 땐 괜찮아요. 사람 많을 때는 조금 조용히 표현하고 싶어요."
            "서윤이 메뉴판을 세워 놓고 그 너머로 목소리를 낮췄다."
            s "그럼 지금은 이 정도? 좋아해."
            d "크기만 줄이셨네요."
            s "응. 내용은 같은데~"
            $ remember("seoyun_expression", "quiet_public")
        "그때그때 좋고 싫은 걸 말하자고 한다.":
            d "제가 웃었다고 다 괜찮은 줄 알진 마세요. 좋은 것도 불편한 것도 말할게요."
            s "응. 나도 재미없는 농담엔 안 웃어 줄게."
            d "갑자기 오늘이 어려워지는데요."
            s "지금 건 조금 웃겼어~"
            $ remember("seoyun_expression", "say_each_time")
    s "회사엔 아직 둘만 아는 걸로. 누가 물어도 네 얘기까지 내가 꺼내진 않을게."
    s "피칭 끝날 때까지는 특히 조용히. 상대 회사 쪽에... 아는 사람이 좀 있어."
    d "아는 사람이요?"
    s "응. 나중에 얘기할게. 오늘은 그 얘기로 이 시간 쓰기 싫어."
    $ remember("seoyun_pitch_secrecy", "피칭이 끝날 때까지 교제를 회사에 알리지 않기로 함, 상대 회사에 아는 사람이 있다고만 말함")
    $ remember("seoyun_publicity", "private")
    $ remember("seoyun_public_boundary", "교제 공개는 나중에 두 사람이 합의, 사적인 내용은 공유하지 않음")
    d "좋아요. 다음 토요일 저녁은 제가 만나자고 할게요."
    s "응. 그럼 이번엔 내가 기다렸다는 말부터 할 수 있겠네."
    $ award_once("seoyun_R06", "seoyun", 6)
    $ progression_note_ending()
    return

label seoyun_private_evening(slot, outfit):
    $ progression_enter("seoyun_private_evening.choice01." + slot)
    $ progression_checkpoint("seoyun_private_evening.choice01." + slot)
    menu:
        "나도 같이 밤을 보내고 싶다고 답한다 — 친밀한 장면으로 이어짐.":
            d "저도요. 오늘은 더 같이 있고 싶어요."
            s "응. 이 대답은 장난 없이 들을게. 나도 원하니까."
            call event_sequence("seoyun_" + slot, outfit)
            if not event_main_reached:
                "(장면 생략 · 시간이 흐릅니다.)"
            $ remember("seoyun_" + slot + "_pace", "shared")
            if slot == "r07":
                s "아까 내가 너 붙잡으러 갔을 때 있잖아. 그때 벌써 손 잡고 싶었어."
                d "저는 지금 잡아도 되냐고 물어보려고 했어요."
                "서윤이 이불 밖으로 손을 내밀었다."
            elif slot == "r12":
                s "지금은 말 잘하려는 것보다 옆에 있는 게 좋네."
                d "저도요. 잠깐 조용해져도 그건 그대로예요."
            else:
                s "오늘은 더 같이 있고 싶다고 내 입으로 말하니까 좋네. 다음 약속도 나 혼자 기다리진 않을게."
                d "네. 저도 물어볼게요. 오늘은 여기 좀 더 있을래요."
        "오늘은 집에 간다.":
            d "오늘은 집에서 쉬고 싶어요. 다음에도 보고 싶다는 마음은 같아요."
            s "응. 집에 가서 푹 쉬어. 다음엔 내가 보고 싶다고 연락할게~"
            "현관에서 인사를 나누고 도현은 집으로 돌아갔다."
            $ remember("seoyun_" + slot + "_pace", "deferred")
        "얘기만 조금 더 하고 간다.":
            d "오늘은 마음 얘기를 좀 더 하고 가고 싶어요. 같이 있고 싶다는 것도요."
            s "좋아. 나도 농담 안 붙이고 얘기할게."
            if slot == "r07":
                d "아까 식당에서요. 저도 문자 썼다가 지웠어요. ‘조금 더 걸을래요?’"
                s "보내지 그랬어. 나 전화할 때 네가 이미 지하철 탄 줄 알았어."
                d "횡단보도도 안 건넜어요. 초록불 한 번 보내고 있었는데요."
                s "둘 다 왜 그랬냐~ 다음엔 먼저 가 버리는 사람 없기. 같이 갈 건지부터 묻고."
                "서윤이 다 마신 잔을 보더니 조금만 더 따라 줬다. 도현은 차를 마저 마시고 일어났다."
            elif slot == "r12":
                d "아까 다음에 제대로 하자던 얘기는 잊지 않을게요. 오늘 대답을 재촉하지는 않고요."
                s "응. 나도 미룬 걸로 끝난 얘기라고 생각하지 않을게."
            else:
                "두 사람은 좋았던 말만 고르지 않고 아직 어려운 마음도 꺼내 놓았다."
            "도현은 늦지 않게 귀가했다."
            $ remember("seoyun_" + slot + "_pace", "talk")
    $ progression_note_ending()
    return

label seoyun_r07:
    $ progression_enter("seoyun_r07")
    $ progression_checkpoint("seoyun_r07")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R07 · 농담을 멈춘 저녁"
    $ location = "토요일 오후 · 서윤이 예전에 살던 동네의 헌책방"
    "저녁 약속 전에, 서윤이 데려가고 싶은 데가 있다고 했다. 지하철로 사십 분. 서윤이 결혼했을 때 살던 동네였다."
    "골목 끝 헌책방 주인은 서윤을 바로 알아봤다. “어머, 오랜만이네. 남편분은 잘 계시고?”"
    "서윤의 손이 책장 모서리에서 잠깐 멈췄다. 도현은 숨을 죽였다."
    s "이혼했어요, 사장님. 삼 년 됐어요. ...이쪽은 지금 만나는 사람이고요."
    "주인이 미안한 얼굴로 웃었고, 서윤은 별일 아니라는 듯 웃으며 책 한 권을 계산대에 올렸다. 책방을 나와서야 서윤이 길게 숨을 내쉬었다."
    s "여기, 혼자는 못 오겠더라. 좋아하던 책방인데 그 사람 생각이 같이 나서."
    d "그래서 저랑 오신 거예요?"
    s "응. 덮어쓰려고. 다음에 이 동네 생각나면, 오늘 네 얼굴이 먼저 떠오르게."
    "서윤이 방금 산 책을 도현의 가방에 쑥 넣었다. 첫 장에는 연필로 오늘 날짜가 적혀 있었다."
    $ cream_focus = "seoyun"
    $ location = "토요일 저녁 · 식당 앞"
    "피칭 준비로 TF 전체가 야근하던 주였다. 서윤은 오늘 저녁만은 비워 두겠다고 팀에 말해 놓고 도현과 만났다."
    "식당 문 앞에서 인사하고 서로 반대 방향으로 걸었다. 도현이 횡단보도 신호를 기다리는데 서윤에게 전화가 왔다."
    s "도현아. 아직 안 건넜지?"
    d "네. 뭐 두고 나오셨어요?"
    s "아니. 그냥 가지 마. 내가 그쪽으로 갈게."
    "전화가 먼저 끊겼다. 고개를 돌리니 서윤이 자기 가방을 팔에 낀 채 빠르게 걸어오고 있었다. 도현 앞으로 와서야 숨을 골랐다."
    s "할 말 없으면 다시 들어가자고 둘러대려 했는데. 그냥 네가 더 보고 싶어. 작업실 갈래?"
    d "네. 저 아까 인사할 때부터 붙잡고 싶었어요."
    $ location = "같은 저녁 · 서윤의 작업실"
    "작업실에 들어서자 차를 따르던 서윤이 도현 쪽을 봤다. 도현은 소파 끝에 앉아 있었다. 서윤이 잔 두 개를 탁자에 놓고 쿠션 하나를 자기 무릎으로 옮겼다."
    s "지금은 건너편에 앉기 싫어. 여기 와."
    "도현이 옆으로 옮겨 앉았다. 팔이 살짝 닿았다. 서윤은 잔을 집는 대신 도현 쪽으로 어깨를 돌렸다."
    s "오늘은 같이 밤을 보내고 싶어. 도현아, 너도 그래?"
    call seoyun_private_evening("r07", "casual")
    $ award_once("seoyun_R07", "seoyun", 0)
    $ progression_note_ending()
    return

label seoyun_r08:
    $ progression_enter("seoyun_r08")
    $ progression_checkpoint("seoyun_r08")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R08 · 보고 싶다는 한 문장"
    if memory.get("seoyun_r07_pace") == "shared":
        $ location = "다음 날 일요일 아침 · 서윤의 작업실"
        "작업실의 작은 주방에서 아침을 준비했다. 서윤이 도현의 접시로 잘 구워진 빵을 밀어 주자, 도현은 자기 것을 반으로 갈라 다시 건넸다."
        s "오후엔 클라이언트 자료 봐야 해. 나가기 전엔 여기 설거지부터 하고~"
        d "그럼 제 접시는 제가 씻을게요. 빵 나눈 값으로 치기엔 좀 적네요."
        s "그건 다음에 또 나눠 먹는 걸로 받을게."
        "그릇을 정리하고 작업실 앞에서 인사했다. 서윤은 피칭 자료를, 도현은 집에서 할 일을 하러 돌아갔다."
        $ remember("seoyun_shared_morning")
    $ location = "일요일 오후 · 각자의 집, 개인 메시지"
    if memory.get("seoyun_r07_pace") == "shared":
        call phone_deliver("seoyun_r08_memory", "seoyun", "어제 너 부르러 간 횡단보도 있지. 아까 거기 지났는데 나 혼자 웃고 있더라.", contact="seoyun")
    elif memory.get("seoyun_r07_pace") == "talk":
        call phone_deliver("seoyun_r08_memory", "seoyun", "어제 안 보냈다던 문자 있잖아. 다음엔 그냥 보내. 나도 이제 썼다 지웠다 안 하려고~", contact="seoyun")
    else:
        call phone_deliver("seoyun_r08_memory", "seoyun", "잘 잤어? 어제 안 붙잡았으면 집에 가서 ‘그냥 물어볼걸’ 하고 후회했을 거야. 같이 차 마셔서 좋았어.", contact="seoyun")
    call phone_deliver("seoyun_r08_time", "seoyun", "이따 클라이언트 쪽이랑 통화 있어. 답 늦어도 걱정 마. 저녁에 다시 볼게.", contact="seoyun")
    call phone_deliver("seoyun_r08_direct", "seoyun", "벌써 좀 보고 싶네. 수요일에 같이 저녁 먹을래? 난 일곱 시 괜찮은데, 너는?", contact="seoyun", important=True)
    $ phone_context = "seoyun_r08_reply"
    $ progression_enter("seoyun_r08.choice01")
    $ progression_checkpoint("seoyun_r08.choice01")
    call screen office_phone(replies=[("miss", "보고 싶다고 답한다."), ("story", "오늘 창가에서 있었던 일을 보낸다."), ("invite", "이번엔 내가 식당을 고르겠다고 한다.")])
    $ remember("seoyun_r08_reply", _return)
    $ phone_context = None
    if memory["seoyun_r08_reply"] == "miss":
        call phone_deliver("seoyun_r08_reply", "dohyun", "저도요. 아까부터 연락할까 했어요. 수요일엔 제가 먼저 가 있을게요.", contact="seoyun")
        call phone_deliver("seoyun_r08_confirm", "seoyun", "그래? 그럼 이번엔 내가 너 찾을 차례네. 수요일에 봐.", contact="seoyun", important=True)
    elif memory["seoyun_r08_reply"] == "story":
        call phone_deliver("seoyun_r08_reply", "dohyun", "수요일 돼요. 아까 빨래 널고 창가에 앉았는데 서윤 씨 생각났어요. 왜인지는 만나서 말해 줄게요.", contact="seoyun")
        call phone_deliver("seoyun_r08_confirm", "seoyun", "뭐야, 궁금하게. 그럼 수요일에 만나자마자 물어봐야겠다.", contact="seoyun")
    else:
        call phone_deliver("seoyun_r08_reply", "dohyun", "일곱 시면 돼요. 이번엔 제가 식당 골라도 돼요? 같이 가 보고 싶은 데가 있어요.", contact="seoyun")
        call phone_deliver("seoyun_r08_confirm", "seoyun", "좋지. 어디인지는 나중에 알려 줘도 돼. 수요일에 봐.", contact="seoyun")
    $ remember("seoyun_r09_appointment", "수요일 저녁 일곱 시 함께 식사")
    $ award_once("seoyun_R08", "seoyun", 4)
    $ progression_note_ending()
    return

label seoyun_r09:
    $ progression_enter("seoyun_r09")
    $ progression_checkpoint("seoyun_r09")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R09 · 웃으면서도 분명하게"
    $ location = "지난 금요일 밤 · 피칭 리허설 뒤 TF 회식"
    "피칭 리허설이 끝난 금요일 밤, TF는 회사 앞 고깃집에 모였다. 서윤은 도현 맞은편에서 능숙하게 고기를 굽고 있었다."
    j "서윤 씨, 클라이언트 쪽 저녁 자리 또 잡혔다며. 괜찮아?"
    s "괜찮아요. 일인데요 뭐."
    "서윤의 휴대폰이 테이블 위에서 진동했다. 화면에 뜬 이름을 보자 서윤은 곧바로 휴대폰을 뒤집었다."
    r "언니, 받아도 돼~ 남자친구야?"
    s "남자친구는 이렇게 늦게 전화 안 해. ...아니, 그냥 스팸이야."
    "서윤은 웃었지만 집게를 든 손이 한 박자 늦었다. 도현이 말없이 집게를 받아 들자, 서윤이 눈만 들어 도현을 봤다."
    y "두 분 손발이 잘 맞으시네요..."
    s "고기 앞에선 원래 다 친해지는 거야~"
    call phone_deliver("seoyun_r09_dinner", "seoyun", "아까 집게 고마워. 전화는... 나중에 얘기할게. 오늘은 네가 맞은편에 있어서 다행이었어.", contact="seoyun")
    $ cream_focus = "seoyun"
    $ location = "수요일 오후 · 협업 테이블"
    s "다 해 달라면 내일 오전엔 못 줘. ...이 사람, 예전부터 이랬어. 제목 후보 두 개랑 설명 하나까지만 보낼게."
    d "예전부터요? 상대 담당자 아세요?"
    s "응, 좀. 아직 안 정한 걸 된다고 말해 버리면 나중엔 그게 약속이 되거든. 이 사람한테는 특히."
    $ progression_enter("seoyun_r09.choice01")
    $ progression_checkpoint("seoyun_r09.choice01")
    menu:
        "추가 요청을 나란히 정리한다.":
            "도현이 요청이 늘어난 지점을 표시했다. 서윤은 이번에 확인받을 범위만 답장에 담았다."
            $ remember("seoyun_r09_support", "scope")
        "자료는 내가, 문구는 서윤이 맡는다.":
            d "현장 자료는 제가요. 표현 후보는 선배 쪽에서 부탁드려요."
            "서윤은 담당자와 확인 시각을 답장에 적었다."
            $ remember("seoyun_r09_support", "roles")
        "받는 사람처럼 읽어 본다.":
            d "여기 ‘내일까지’는 전달인지 확인까지인지 헷갈릴 것 같아요."
            s "좋아. 오전 열 시 초안 전달, 피드백은 따로 조율이라고 쓸게."
            $ remember("seoyun_r09_support", "reader")
    "잠시 뒤 답장이 왔다. 서명란에 ‘정민재’라는 이름이 찍혀 있었다. 서윤은 그 이름을 오래 보지 않고 화면을 닫았다."
    $ location = "같은 수요일 저녁 일곱 시 · 식당"
    if memory.get("seoyun_r08_reply") == "invite":
        "도현이 정한 식당에서 만났다. 서윤은 문 앞에서 도현을 보고 손을 흔들었다."
        s "네가 가 보고 싶다니까 메뉴도 안 찾아봤어. 뭐 먹을까?"
    elif memory.get("seoyun_r08_reply") == "story":
        s "아, 창가에서 왜 내 생각 났는지 말해 준다며. 그거부터 들을래."
        d "날씨 좋길래 같이 걸으면 좋겠다 싶었어요. 그러고 창밖을 봤는데, 제가 널어 둔 수건밖에 안 보이더라고요."
        s "네가 만든 전망이네~"
        d "한 장 걷으면 되는데, 꼭 그 자리가 제일 잘 말라요. 결국 제가 옮겼어요."
        s "창가 얘기라 좀 근사할 줄 알았는데. 수건한테 자리 뺏긴 얘기였어?"
        d "그래도 오늘은 괜찮은 자리 앉았잖아요."
        "서윤이 창 쪽을 봤다가 도현 앞으로 시선을 되돌렸다."
        s "응. 여긴 수건 안 널어도 되고."
    else:
        s "먼저 와 있겠다더니, 진짜네. 많이 기다렸어?"
    d "오늘 일할 때요, 웃으면서도 안 되는 건 딱 자르시는 게 좋았어요. 지금은 웃는 얼굴을 더 오래 보고 싶고요."
    s "칭찬 뒤에 그런 말 붙이면, 밥 먹다 말고 너만 보게 되잖아."
    "서윤이 웃으며 메뉴판을 도현 쪽으로 돌렸다. 평소와 달리 이번에는 설명을 덧붙이지 않았다."
    s "오늘은 네가 시켜 봐. 아까부터 어디 보고 있는지는 대충 알겠지만~"
    d "그럼 버섯 크림 파스타나 토마토 리소토요. 저는 파스타 쪽인데."
    s "나는 리소토. 아까 파스타 사진만 오래 보더라니~"
    d "들켰네요. 버섯 좋아하실 것 같아서 추천한 척했어요."
    s "나도 버섯 좋아해. 오늘은 밥이 먹고 싶을 뿐이지."
    "서윤은 리소토를, 도현은 파스타를 주문했다. 접시가 놓이자 둘 다 말보다 포크와 숟가락이 빨랐다."
    d "추천 설명 안 해서 다행이네요. 지금까지 말했으면 식었겠어요."
    s "응. 다음엔 먹고 나서 자랑해. 나 지금 네 거 살짝 부러워졌으니까."
    d "바꾸고 싶을 정도예요?"
    "서윤이 제 접시를 조금 당겼다."
    s "그 정도는 아니고~ 네가 고른 건 어떤 맛인가 싶어서."
    d "그럼 버섯부터 설명할게요. 제일 자신 있게 추천한 거니까."
    s "...한 입 물어볼 걸. 메뉴 설명을 다 듣게 생겼네."
    "저녁을 먹고 각자 집으로 돌아갔다. 토요일에는 추천한 책 이야기를 더 나누기로 했다."
    $ award_once("seoyun_R09", "seoyun", 6)
    $ progression_note_ending()
    return

label seoyun_r10:
    $ progression_enter("seoyun_r10")
    $ progression_checkpoint("seoyun_r10")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R10 · 단골도 틀리는 취향"
    $ location = "토요일 오후 · 단골 북카페"
    "서윤이 펼친 책 옆으로 작은 접시 두 개가 들어왔다. 레몬 케이크와 진한 초콜릿 케이크였다."
    s "네 건 초콜릿. 단 거 주면 먹는다고 했지?"
    d "맞아요. 그런데 오늘은 레몬이 더 궁금한데요."
    "서윤이 자기 접시 위에 포크를 세웠다."
    s "정하기 전엔 말 안 하고? 나 이거 꽤 오래 고민했는데."
    d "서윤 씨가 좋아하시는 건 알아서 다 시키실 것 같아서 기다렸죠."
    s "좋아. 한 입만 바꾸자. 나도 레몬이 맛있을 줄 알고 시켰으니까~"
    "서로 한 조각씩 덜어 줬다. 도현은 레몬을 먹고 물을 찾았고, 서윤은 초콜릿을 먹고 자기 접시를 다시 봤다."
    d "...생각한 것보다 시네요."
    s "난 네 쪽이 더 좋다. 취향 맞히는 사람부터 바꿔야겠는데?"
    if memory.get("seoyun_o01_status") == "completed":
        s "책은 서로 다른 데서 멈추더니. 케이크는 반대로 시켜 놓고 먹네."
    elif memory.get("seoyun_r02_response") == "wait":
        s "그때는 대답 기다려 달랬는데. 오늘은 내 포크 좀 기다려 줘. 초콜릿 한 입만 더."
    else:
        s "취향 맞히기는 다음에 할래. 일단 내가 먹고 싶은 거부터."
    "접시를 서로 바꿨다. 도현은 커피와 레몬을 번갈아 먹고, 서윤은 초콜릿 한 입을 천천히 맛봤다."
    d "사진 한 장도 안 찍고 먹었네요. 오늘 건 한 줄만 적을래요."
    s "초콜릿이 레몬보다 맛있었다고만 적어 줘. 몇 입 먹었는지는 빼고~"
    $ progression_enter("seoyun_r10.choice01")
    $ progression_checkpoint("seoyun_r10.choice01")
    menu:
        "‘오늘은 돌아갈 길을 조금 늦게 골랐다.’라고 쓴다.":
            d "집엔 갈 건데, 지금 일어나기는 싫어서요."
            s "좋아. 그럼 남은 케이크 먹는 동안만 더 있자."
            d "아직도 레몬은 안 되겠어요?"
            "서윤이 초콜릿 접시를 제 쪽으로 조금 당겼다."
            s "응. 이건 오늘 내 거야."
            $ remember("seoyun_booklet_sentence", "오늘은 돌아갈 길을 조금 늦게 골랐다.")
            $ remember("seoyun_booklet_impression", "스스로 조금 더 남은 시간")
        "‘한 잔이 식는 동안 이 골목이 익숙해졌다.’라고 쓴다.":
            "서윤이 제 잔을 들었다가 한 모금 마시고 내려놓았다."
            s "다음 잔도 생각나네. 이번엔 네가 시켜 줘."
            d "케이크도 서윤 씨가 시키셨다가 바꿨잖아요."
            s "그럼 두 번 맛볼 수 있지~"
            "도현이 남은 커피를 들어 보이자, 서윤은 새 음료를 주문하려다 메뉴판을 내려놓았다."
            d "지금 잔부터요. 이번 건 제가 안 넘길 거예요."
            $ remember("seoyun_booklet_sentence", "한 잔이 식는 동안 이 골목이 익숙해졌다.")
            $ remember("seoyun_booklet_impression", "다음 한 잔의 자리가 남는 문장")
        "‘다음에 올 이유는 아직 적지 않았다.’라고 쓴다.":
            d "레몬 때문에 또 온다고 쓰면 반쯤 거짓말이라서요."
            s "나머지 반은?"
            d "서윤 씨가 초콜릿 드시는 거, 계속 보고 싶어요."
            "서윤이 포크를 들다 말고 도현을 봤다."
            s "...내가 그렇게 티 나게 먹었어?"
            d "네. 아까 고른 책보다 오래 보셨어요."
            s "그건 안 적은 이유로 남겨 줘~"
            $ remember("seoyun_booklet_sentence", "다음에 올 이유는 아직 적지 않았다.")
            $ remember("seoyun_booklet_impression", "빈칸에도 다시 오고 싶은 마음이 들림")
    "도현이 한 줄 옆에 서윤의 반응을 작게 적고 노트를 닫았다. 서윤도 책 사이에 끼워 둔 메모지를 꺼내 같은 문장과 자기 감상을 적었다."
    "서윤이 펜을 내려놓고 남은 케이크를 두 조각으로 나눴다."
    s "마지막은 반씩. 이번엔 내가 집기 전에 가져가."
    d "제가 더 큰 쪽 집어도요?"
    "서윤은 포크를 들지 않고 도현의 손을 봤다. 도현이 작은 쪽을 가져가자 곧바로 접시를 밀었다."
    s "아, 그렇게 주면 내가 큰 거 고른 사람 같잖아."
    d "들켰네요. 이번엔 제가 양보한 건데."
    "서윤은 대꾸 대신 큰 조각의 끝을 조금 잘라 도현 쪽에 놓았다."
    $ remember("seoyun_booklet_state", "직접 쓴 문장과 독자 감상이 있는 초안, 인쇄 완성 전")
    $ progression_enter("seoyun_r10.choice02")
    $ progression_checkpoint("seoyun_r10.choice02")
    menu:
        "유진 씨한테만 말하자고 한다.":
            d "유진 씨한테는 저희 만나는 것만 말할까요? 둘 다 괜찮으면요."
            s "응. 사적인 얘기는 우리한테 두고. 내일 같이 보내자."
            $ remember("seoyun_publicity", "agreed_yujin")
        "당분간 둘만 알자고 한다.":
            d "아직은 둘만 알고 싶어요. 마음 바뀌면 말씀드릴게요."
            s "응. 누가 물어도 내가 혼자 대답 정해서 말하진 않을게."
            $ remember("seoyun_publicity", "private")
        "말할 땐 사귄다는 것까지만.":
            d "말하게 되면 사귄다는 것까지만요. 언제인지는 더 생각할래요."
            s "좋아. ‘언젠가’라고 했다고 내일 발송 예약 걸지는 않기~"
            $ remember("seoyun_publicity", "discuss_later")
    $ award_once("seoyun_R10", "seoyun", 4)
    $ progression_note_ending()
    return

label seoyun_r10_after:
    $ progression_enter("seoyun_r10_after")
    $ progression_checkpoint("seoyun_r10_after")
    if not dating or active_route != "seoyun" or "seoyun_R10" not in completed:
        $ progression_note_ending()
        return
    $ location = "같은 토요일 밤 · 서윤의 작업실 — 서윤 시점"
    "서윤은 책 사이에서 오늘 쓴 메모를 꺼냈다. 도현의 문장은 고치지 않고 자기 감상만 다시 읽었다."
    sn "농담 안 붙여도 다음 말 기다려 주네. 나도 그냥 보고 싶다고 하면 되는데."
    "휴대폰에 적던 ‘심심하면’을 지우고 메시지를 보냈다."
    call phone_deliver("seoyun_r10_after", "seoyun", "내일도 보고 싶어. 저녁 먹고 같이 걸을래? 여섯 시 반, 서점 앞에서.", contact="seoyun", important=True)
    call phone_deliver("seoyun_r10_accept", "dohyun", "좋아요. 여섯 시 반에 서점 앞에서 봐요. 걸을 길은 그때 같이 정해요.", contact="seoyun")
    $ progression_note_ending()
    return

label seoyun_r11:
    $ progression_enter("seoyun_r11")
    $ progression_checkpoint("seoyun_r11")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R11 · 다음 주의 일정"
    $ location = "일요일 저녁 여섯 시 반 · 서점 앞"
    if memory.get("seoyun_publicity") == "agreed_yujin":
        d "어제 정한 메시지, 같이 보낼까요?"
        s "응. 나도 지금 옆에 있다고 써 줘."
        call phone_deliver("seoyun_r11_disclose", "dohyun", "서윤 씨와 연인으로 만나고 있어요. 지금 둘이 함께 말씀드려요. 다른 분들께는 저희가 따로 이야기할게요.", contact="yujin")
        call phone_deliver("seoyun_r11_congrats", "yujin", "축하해요! 두 분이 같이 말씀해 주셔서 더 반갑네요. 다른 분들께 먼저 전하지 않을게요. 다음에 얼굴 보고도 축하할래요 :)", contact="yujin")
        $ remember("seoyun_publicity", "told_yujin")
        $ remember("seoyun_disclosure_delivered")
    s "오늘은 네가 길 정해 줘. 나 좀 따라가 보고 싶어."
    d "마음에 안 들면 말씀하셔야 해요."
    s "그건 잘하지~ 그런데 지금은 기대하는 중이야."
    d "그럼 천천히 가요. 오늘은 제가 안내할게요."
    "서윤이 웃으며 도현 옆으로 한 걸음 다가왔다. 늘 방향을 짚던 손은 가방 끈 위에 얹었다."
    s "...응. 그 말 들으니까 맡기길 잘했네. 늘 가던 골목도 좋고, 네가 보여 주고 싶은 길도 좋아."
    $ progression_enter("seoyun_r11.choice01")
    $ progression_checkpoint("seoyun_r11.choice01")
    menu:
        "서윤의 단골 골목을 걷는다.":
            "서점 뒤 골목에서 화분이 늘어난 작은 계단을 봤다. 서윤도 새 화분 하나는 처음 보는 눈치였다."
            "서윤이 익숙한 계단을 한 칸 지나쳤다가 도현을 따라 돌아섰다."
            s "이 화분 언제 늘었지? 단골이 더 늦게 봤네."
            d "오늘은 제가 안내한다고 했잖아요."
            s "응. 설명 잘 들었어. 여기서는 조금 더 보고 갈래."
            $ remember("seoyun_walk_route", "familiar")
            $ remember("seoyun_walk_detail", "서점 뒤 계단에 늘어난 작은 화분")
        "내가 궁금했던 다리로 간다.":
            "도현이 고른 다리 아래로 걸었다. 난간 사이로 바람이 들어와 둘은 잠깐 멈췄다."
            d "여기 오면 저도 목소리가 작아져요. 말 잘 못해도 바람 탓할 수 있고요."
            s "핑계부터 좋은 데네~ 그럼 아까 하고 싶던 말 해 봐."
            d "서윤 씨랑 여기 오고 싶었어요. 그게 다인데요."
            "서윤은 난간 쪽을 보다가 도현 쪽으로 다시 고개를 돌렸다."
            s "...응. 바람 없이도 잘 들리네."
            $ remember("seoyun_walk_route", "riverside")
            $ remember("seoyun_walk_detail", "난간 사이 바람 때문에 목소리를 낮춘 다리")
        "골목 반, 강변 반으로 걷는다.":
            "그늘진 골목을 먼저 걷고 강변 입구에서 돌아왔다. 돌아갈 지점은 바람을 맞으며 같이 정했다."
            s "골목도 보고 강변도 봤네. 너는 집에 가는 길까지 조금 돌아가는 편이야?"
            d "오늘은요. 혼자 오면 버스부터 탈 때도 있어요."
            s "그럼 오늘은 나도 여기까지만 돌아갈래."
            $ remember("seoyun_walk_route", "both")
            $ remember("seoyun_walk_detail", "그늘 골목 뒤 강변 입구에서 함께 고른 귀가 지점")
    s "다음 주엔 월요일부터 목요일까지 외근이 잡혔어. 금요일 저녁 일곱 시는 비워 둘 수 있어."
    d "저도 금요일 좋아요. 중간에도 연락해요. 별일 없었다는 얘기여도요."
    s "응. 금요일 일곱 시에 이 앞에서. 못 본 얘기 쌓아 놓고 올게."
    $ remember("seoyun_reunion_plan", "금요일 저녁 일곱 시, 서점 앞 재회")
    $ award_once("seoyun_R11", "seoyun", 0)
    $ progression_note_ending()
    return

label seoyun_r12:
    $ progression_enter("seoyun_r12")
    $ progression_checkpoint("seoyun_r12")
    if not dating or active_route != "seoyun":
        $ progression_note_ending()
        return
    $ chapter = "서윤 R12 · 이번엔 날짜까지 말할게"
    $ location = "화요일 저녁 · 각자의 자리, 개인 메시지"
    call phone_deliver("seoyun_r12_tuesday", "seoyun", "오늘은 이동이 길었어. 클라이언트 쪽 저녁 자리도 있었고... 좀 지치네. 금요일엔 너랑만 저녁 먹고 싶어~", contact="seoyun")
    $ location = "목요일 퇴근 후 · 개인 메시지"
    call phone_deliver("seoyun_r12_thursday", "seoyun", "외근 끝났어. 내일 일곱 시 서점 앞 약속 그대로야. 내일은 얼굴 보고 보고 싶었다고 말할래.", contact="seoyun", important=True)
    call phone_deliver("seoyun_r12_reply", "dohyun", "저도요. 내일 일곱 시 서점 앞에서 봬요. 오늘은 푹 쉬세요.", contact="seoyun")
    $ location = "금요일 저녁 일곱 시 · 서점 앞"
    "출장 내내 클라이언트 쪽 저녁 자리가 이어졌다고 했다. 서윤은 휴대폰을 가방 깊숙이 넣고 약속 장소로 왔다."
    "금요일 약속한 시간에 서윤이 걸어왔다. 메시지 화면 대신 서로의 얼굴을 보고 인사했다."
    s "보고 싶었어. 이번 주는 메시지로만 주고받으니까 할 말이 더 쌓이더라."
    d "저도요. 일요일에 걸었던 데 생각도 났고요."
    s "[memory['seoyun_walk_detail']], 그거? 나도 생각났어."
    "함께 저녁을 먹었다. 서윤은 오늘 만나려고 꺼내 입었다는 옷의 소매를 정리했다."
    d "다음 계절에도 이렇게 만나고 싶어요. 피칭 끝나면, 서윤 씨 친구들한테도 회사에도 저 소개해 줄 수 있어요?"
    s "벌써 공개 연애 신청이야? 경쟁 PT보다 떨리는데~"
    d "농담 아니에요. 숨어서 만나는 거 말고, 서윤 씨 옆에 서 있고 싶어요."
    "서윤은 냅킨을 접다가 같은 모서리를 다시 눌렀다."
    s "...그건 다음에 제대로 얘기하자. 겁나니까 장난부터 나왔네. 피칭 끝나기 전엔... 좀 복잡해."
    d "네. 월요일 저녁에 그 얘기만 하러 만날까요? 어떤 대답이든 직접 듣고 싶어요."
    s "응. 일곱 시, 카페에서. 말 돌리지 않고 내 생각 가져갈게."
    $ remember("seoyun_future_question", "주변에 서로를 소개하고 공개적으로 만나고 싶다는 제안, 서윤이 피칭을 이유로 미룸")
    $ remember("seoyun_future_question_status", "아직 제대로 답하지 않은 질문")
    $ remember("seoyun_r13_appointment", "월요일 저녁 일곱 시, 카페에서 앞으로의 관계 이야기")
    "저녁 뒤 서윤의 개인 작업실에 들렀다. 서윤은 물을 건네고 도현이 옆에 앉기를 기다렸다."
    s "오늘 다시 만나서 좋아. 그건 지금 분명히 말할 수 있어. 오늘은 여기서 같이 밤을 보내고 싶어. 너도 괜찮으면."
    call seoyun_private_evening("r12", "special")
    $ award_once("seoyun_R12", "seoyun", 4)
    $ progression_note_ending()
    return
