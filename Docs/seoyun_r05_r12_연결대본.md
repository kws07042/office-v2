> 현행 갱신: 기획 v3.07 / Windows 0.34.0-early-couple — 2026-10-21
> R05~R08의 교제 변화를 실제 식사·호칭·취향·장난으로 편집했다. R07의 동기와 R08의 실제 선택 기억을 연결한다. 교제초반_편집보고서_v1.md와 실행 소스를 우선한다. 사건 수·핵심 분기·기억·CG 계획·인물 설정은 유지한다. 아래 구버전 갱신은 이력이다.

> 현행 갱신: 기획 v3.05 / Windows 0.32.0-dialogue-clarity — 2026-10-21
> 뜻을 짐작해야 하는 농담·혼합 비유·대답의 연결·화자와 소품 불일치를 정리했다. 대사이해도_전체검수_보고서_v1.md와 현행 실행 대본을 우선한다. 사건·선택 기억·인물 설정·자산 계획은 유지한다. 아래 이전 갱신은 이력이다.

# 서윤 실제 구현 대본 — seoyun_r05_r12.rpy

```renpy
label seoyun_r05:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 R05 · 단골이 되는 순서"
    $ location = "고백 다음 날 토요일 오후 두 시 · 약속한 장소"
    if memory["seoyun_next_date_plan"] == "bookcafe":
        "서점에서 만나 안쪽 북카페에 앉았다. 문이 열릴 때마다 작은 종이 울렸다."
        s "이 자리 자꾸 오면 책보다 사람 기다리는 단골 되겠는데."
        d "저는 그 이유도 좋아요. 오늘은 문 열릴 때 서윤 씨 먼저 찾았고요."
        $ remember("seoyun_r05_place", "작은 종이 울리는 북카페")
    elif memory["seoyun_next_date_plan"] == "walk":
        "강변 입구에서 만나 도현이 궁금했던 낮은 다리까지 걸었다. 돌아오는 길에 골목 카페에 들렀다."
        s "오늘은 네가 자꾸 멈추는 데 보면서 왔어. 나도 난간 그림자는 못 보고 지나갈 뻔했네."
        d "다음에 혼자 와도 오늘 본 데서 한 번 더 멈출 것 같아요."
        $ remember("seoyun_r05_place", "강변의 낮은 다리와 돌아오는 골목 카페")
    else:
        "서점 앞에서 만나 오늘은 골목 안쪽으로 걷기로 했다. 작은 카페의 그늘진 창가가 마음에 들어 앉았다."
        s "정해 오지 않으니까 네가 창가 찾는 것도 보네."
        d "서윤 씨가 여기서 걸음 늦추시는 것도 보고요."
        $ remember("seoyun_r05_place", "함께 고른 골목 카페의 그늘진 창가")
    if memory.get("seoyun_r03_affection") == "hug":
        s "수요일에 인사하고 떨어졌을 때 있지. 오늘은 다음 말까지 더 듣고 싶었어."
    elif memory.get("seoyun_r03_affection") == "hand":
        s "수요일엔 잠깐 손잡고 인사했지. 오늘은 헤어질 시간까지 안 급하게 써 보자."
    else:
        s "수요일에 다음에도 오고 싶다고 했잖아. 오늘 실제로 오니까 또 좋네."
    if memory.get("seoyun_first_kiss"):
        d "어제는 카페 나와서도 자꾸 웃었어요. 오늘은 좀 덜 들킬 줄 알았는데요."
        s "지금도 다 보여~ 나도 거울 봤으면 비슷했을 것 같고."
    else:
        s "어제 네가 편한 만큼 말해 준 것도 좋았어. 오늘 할 인사까지 미리 정하진 말자."
    s "여길 네 기록집에 남긴다면 뭐부터 보여 주고 싶어? 나한테 멋있는 답 해 주려고 고르진 말고."
    menu:
        "들어오고 나가는 사람 사이에 남는 소리를 적어 둔다.":
            "도현은 문 여닫는 소리와 탁자에 컵을 내려놓는 소리를 메모했다."
            d "사람이 안 보여도 누가 잠깐 다녀갔는지는 남는 것 같아서요."
            s "나는 잠깐 혼자 남은 자리가 먼저 생각나네. 같은 소리인데."
            $ remember("seoyun_r05_subject", "사람이 다녀간 뒤 남는 작은 소리")
            $ remember("seoyun_r05_impression", "소리 뒤에 잠깐 혼자 남은 자리")
        "그늘과 빛이 갈리는 자리를 사진 후보로 메모한다.":
            "도현은 빛이 걸린 모서리를 손으로 가리켰다. 아직 사진은 찍지 않았다."
            d "다 밝은 데보다 여기부터 보고 싶어요. 다음에 카메라 들고 오고 싶고요."
            s "난 그늘 쪽에 앉은 사람이 어디 보는지 궁금해질 것 같아."
            $ remember("seoyun_r05_subject", "그늘과 빛이 만나는 모서리, 촬영 전 후보")
            $ remember("seoyun_r05_impression", "그늘 쪽에 앉은 사람의 시선이 궁금함")
        "다시 와서 앉고 싶은 이유를 짧게 메모한다.":
            d "‘한 번 더 앉아도 되는 곳.’ 지금은 이렇게 남길래요."
            s "허락받는 느낌보다, 스스로 다시 오고 싶은 느낌이 나. 나는 그게 좋아."
            $ remember("seoyun_r05_subject", "한 번 더 앉아도 되는 곳이라는 메모")
            $ remember("seoyun_r05_impression", "스스로 다시 오고 싶은 느낌")
    "도현이 노트를 넣자 서윤이 접시의 마지막 과자를 가리켰다."
    s "아까부터 저거 양보하는 중이었어?"
    d "아뇨. 서윤 씨 드시는 속도 보고 있었어요. 제 차례 오나 해서."
    s "그럼 서로 먹고 싶었던 거네~ 반 나눌까?"
    "반으로 가르자 한쪽이 훨씬 커졌다. 서윤이 큰 쪽을 집으려다 멈췄다."
    d "그거 드세요. 방금은 진짜 양보예요."
    s "...이렇게 말하면 작은 쪽 집으려고 했다는 변명도 못 하겠네."
    "서윤이 큰 조각을 먹었다. 도현도 제 몫을 집자 이번엔 말 대신 접시를 가까이 밀어 줬다."
    $ award_once("seoyun_R05", "seoyun", 4)
    return

label seoyun_r06:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 R06 · 우리 얘기부터 정하자"
    $ location = "다음 주 수요일 저녁 · 동네 식당"
    s "너한테 무슨 호칭 듣고 싶은지 생각해 봤어. 연애 몇 번 해 봤다고 이런 게 익숙해지진 않네."
    d "저는 더 골라야겠는데요. 그래도 먼저 불러 보고 싶어요."
    menu:
        "둘만 있을 때 ‘서윤 누나’라고 불러도 되는지 묻는다.":
            d "서윤 누나. 둘이 있을 때는 이렇게 불러도 돼요?"
            s "응. 방금 대답 한 번 더 하게 만들고 싶은데?"
            $ remember("seoyun_private_name", "서윤 누나")
        "이름을 부르는 ‘서윤 씨’가 지금은 좋다고 한다.":
            d "저는 서윤 씨라고 부르는 게 좋아요. 이름 먼저 생각하고 부르는 느낌이라서요."
            s "좋아. 네가 그런 뜻으로 부르면 나도 다시 돌아보게 되겠네."
            $ remember("seoyun_private_name", "서윤 씨")
        "아직은 ‘서윤 선배’가 편하지만, 사적인 마음도 따로 표현한다.":
            d "아직은 서윤 선배가 좀 편해요. 보고 싶어서 부르는 말이라는 것도 같이 말할게요."
            s "응. 호칭 하나로 전부 알아맞히려고 하진 않을게."
            $ remember("seoyun_private_name", "서윤 선배")
    s "나는 둘이 있을 땐 도현아, 하고 부르고 싶어. 회사에서는 도현 씨고."
    d "좋아요. 지금 한번 불러 주세요. 메뉴판 말고 저 볼 때요."
    s "도현아."
    "도현이 대답하자 서윤은 주문하려던 메뉴 이름을 잠깐 잊었다."
    s "...이상하네. 부르는 쪽이 덜 떨릴 줄 알았는데."
    menu:
        "장난은 좋아하지만 중요한 마음은 직접 말해 달라고 한다.":
            d "장난 주고받는 건 좋아요. 좋아한다는 말은 진심인 걸 알게 해 주세요."
            s "응. 받아치기 전에 진짜 대답부터 해 볼게."
            $ remember("seoyun_expression", "sincere_first")
        "사람 많은 곳의 애정 표현은 조금 조용히 하고 싶다고 한다.":
            d "둘만 있을 땐 괜찮아요. 사람 많을 때는 조금 조용히 표현하고 싶어요."
            s "알겠어. 지금 말한 걸 내 마음이 싫다는 뜻으로 듣진 않을게."
            $ remember("seoyun_expression", "quiet_public")
        "그때마다 편한 장난과 애정 표현을 말하며 맞추자고 한다.":
            d "제가 웃었다고 전부 괜찮다고 생각하진 말아 주세요. 좋은 것도 불편한 것도 말할게요."
            s "좋아. 나도 웃어넘긴 다음 혼자 끙끙대진 말고 말해 볼게."
            $ remember("seoyun_expression", "say_each_time")
    s "회사엔 아직 둘만 아는 걸로. 누가 물으면 네 얘기까지 먼저 하진 않을게."
    $ remember("seoyun_publicity", "private")
    $ remember("seoyun_public_boundary", "교제 공개는 나중에 두 사람이 합의, 사적인 내용은 공유하지 않음")
    d "고마워요. 다음 토요일 저녁은 제가 먼저 만나자고 할게요."
    s "응. 이번에는 내가 기다렸다는 말부터 할 수 있겠네."
    $ award_once("seoyun_R06", "seoyun", 6)
    return

label seoyun_private_evening(slot, outfit):
    menu:
        "나도 같이 밤을 보내고 싶다고 답한다 — 친밀한 장면으로 이어짐.":
            d "저도 같은 마음이에요. 오늘은 더 같이 있고 싶어요."
            s "응. 이 대답은 장난 없이 들을게. 나도 원하니까."
            call event_sequence("seoyun_" + slot, outfit)
            if not event_main_reached:
                "(거사 — 장면 생략)"
            $ remember("seoyun_" + slot + "_pace", "shared")
            s "지금은 말 잘하려는 것보다 옆에 있는 게 좋네."
            d "저도요. 잠깐 조용해져도 그 마음은 같아요."
        "오늘은 귀가하고 다음 만남도 기대한다고 말한다.":
            d "오늘은 집에서 쉬고 싶어요. 다음에도 보고 싶다는 마음은 같아요."
            s "응. 오늘 네가 고른 답을 다음 기대까지 없어진 말로 듣진 않을게."
            "현관에서 인사를 나누고 도현은 집으로 돌아갔다."
            $ remember("seoyun_" + slot + "_pace", "deferred")
        "마음을 조금 더 나눈 뒤 오늘은 각자 쉬자고 한다.":
            d "오늘은 마음 얘기를 더 하고 돌아가고 싶어요. 같이 있고 싶은 마음도 말하고요."
            s "좋아. 농담 붙이지 않고 나도 이야기할게."
            if slot == "r07":
                d "아까 편하게 있다 가라고 하셨을 때, 저는 안 들켰다고 생각했어요."
                s "가기 싫은 거? 탁자부터 당겼잖아."
                d "그 전에요. 식당에서 후식 메뉴 또 펼쳤을 때부터요."
                s "그건 못 봤네. 난 내가 늦게 먹어서 기다리는 줄 알았는데."
                "서윤이 다 마신 잔을 보더니 조금만 더 따라 줬다. 도현은 차를 마저 마시고 일어났다."
            else:
                "둘은 긴장된 순간과 좋았던 말을 나눴다."
            "도현은 늦지 않게 귀가했다."
            $ remember("seoyun_" + slot + "_pace", "talk")
    return

label seoyun_r07:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 R07 · 농담을 멈춘 저녁"
    $ location = "토요일 저녁 · 서윤의 집"
    "함께 저녁을 먹고 서윤이 먼저 집에 초대했다. 평소의 사복 차림으로 책장 아래 독서 자리를 보여 줬다."
    s "여긴 커피 놓고 책 안 읽어도 되는 자리. 네가 오면 조금 좁아질 것 같긴 해."
    d "그럼 오늘은 책 말고 제가 옆에 앉아도 돼요?"
    s "응. 그 말 들으려고 한 칸 비워 놨나 봐."
    "서윤은 책을 덮고 도현을 보았다. 뒤에 붙이려던 장난은 말하지 않았다."
    s "오늘은 같이 밤을 보내고 싶어. 도현아, 너도 그래?"
    call seoyun_private_evening("r07", "casual")
    $ award_once("seoyun_R07", "seoyun", 0)
    return

label seoyun_r08:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 R08 · 보고 싶다는 한 문장"
    if memory.get("seoyun_r07_pace") == "shared":
        $ location = "다음 날 일요일 아침 · 서윤의 집"
        "같이 아침을 먹으며 창가의 책 두 권을 옮겼다. 서윤이 다음에는 도현이 고른 책도 놓아 달라고 했다. 도현은 집에 돌아가 오후를 보냈다."
        $ remember("seoyun_shared_morning")
    $ location = "일요일 오후 · 각자의 집, 개인 메시지"
    if memory.get("seoyun_r07_pace") == "shared":
        call phone_deliver("seoyun_r08_memory", "seoyun", "아침에 책 옮겨 놓은 자리 보이네. 지금은 다시 혼자 읽는데, 네 다음 말이 더 궁금해.", contact="seoyun")
    elif memory.get("seoyun_r07_pace") == "talk":
        call phone_deliver("seoyun_r08_memory", "seoyun", "어제 후식 메뉴 다시 보던 거 이제 알았네. 다음엔 나도 다 먹었다고 바로 덮진 않을게~", contact="seoyun")
    else:
        call phone_deliver("seoyun_r08_memory", "seoyun", "어제 보여 준 독서 자리, 오늘도 한 칸 비어 있네. 다음에 또 앉아 줬으면 좋겠어.", contact="seoyun")
    call phone_deliver("seoyun_r08_direct", "seoyun", "보고 싶어. 오늘은 이 말 뒤에 농담 안 붙일래. 다음 수요일 저녁 일곱 시에 밥 먹자. 네 시간은 어때?", contact="seoyun", important=True)
    $ phone_context = "seoyun_r08_reply"
    call screen office_phone(replies=[("miss", "나도 보고 싶다고 직접 답하고 수요일 약속을 확인한다."), ("story", "수요일에 들려주고 싶은 오늘의 작은 일을 보낸다."), ("invite", "수요일엔 내가 식당을 골라 초대하고 싶다고 한다.")])
    $ remember("seoyun_r08_reply", _return)
    $ phone_context = None
    if memory["seoyun_r08_reply"] == "miss":
        call phone_deliver("seoyun_r08_reply", "dohyun", "저도 보고 싶어요. 수요일 일곱 시에 만나요. 이번에는 제가 먼저 기다릴게요.", contact="seoyun")
        call phone_deliver("seoyun_r08_confirm", "seoyun", "응. 네가 기다리는 얼굴은 나도 먼저 보고 싶네. 수요일 일곱 시!", contact="seoyun", important=True)
    elif memory["seoyun_r08_reply"] == "story":
        call phone_deliver("seoyun_r08_reply", "dohyun", "오늘은 빨래 널고 창가에 좀 앉아 있었어요. 별일 없어도 서윤 씨한테 얘기하고 싶더라고요. 수요일 일곱 시 좋아요.", contact="seoyun")
        call phone_deliver("seoyun_r08_confirm", "seoyun", "별일 없는 얘기는 자주 해도 돼~ 수요일 일곱 시엔 얼굴 보면서 더 듣자.", contact="seoyun")
    else:
        call phone_deliver("seoyun_r08_reply", "dohyun", "수요일 일곱 시 괜찮아요. 이번엔 제가 따뜻한 거 먹을 식당 골라서 초대할래요.", contact="seoyun")
        call phone_deliver("seoyun_r08_confirm", "seoyun", "좋아. 이번엔 내가 초대받는 쪽으로. 수요일 일곱 시에 보자.", contact="seoyun")
    $ remember("seoyun_r09_appointment", "수요일 저녁 일곱 시 함께 식사")
    $ award_once("seoyun_R08", "seoyun", 4)
    return

label seoyun_r09:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 R09 · 웃으면서도 분명하게"
    $ location = "수요일 오후 · 협업 테이블"
    s "‘전체적으로 빨리’는 오늘 일정에 못 넣어. 제목 후보 두 개와 설명 한 개, 내일 오전까지. 범위부터 이렇게 확인할게."
    d "남은 요청은 다음 검토로 나누는 거죠?"
    s "응. 아직 못 정한 걸 내가 된다고 말하면, 나중엔 그게 약속이 되거든."
    menu:
        "기존 요청과 추가 요청을 나란히 정리한다.":
            "도현이 요청이 늘어난 지점을 표시했다. 서윤은 이번에 확인받을 범위만 답장에 담았다."
            $ remember("seoyun_r09_support", "scope")
        "내가 준비할 자료와 서윤이 확인할 문구를 나눈다.":
            d "현장 자료는 제가요. 표현 후보는 선배 쪽에서 부탁드려요."
            "서윤은 두 사람의 담당과 확인 시각을 답장에 적었다."
            $ remember("seoyun_r09_support", "roles")
        "받는 사람처럼 읽고 애매하게 남은 부분을 묻는다.":
            d "여기 ‘내일까지’는 전달인지 확인까지인지 헷갈릴 것 같아요."
            s "좋아. 오전 열 시 초안 전달, 피드백은 따로 조율이라고 쓸게."
            $ remember("seoyun_r09_support", "reader")
    "잠시 뒤 답장이 왔다. 제시한 범위와 초안 전달 시각대로 진행하자는 말이었다. 서윤이 화면을 닫고 먼저 자리에서 일어났다."
    $ location = "같은 수요일 저녁 일곱 시 · 식당"
    if memory.get("seoyun_r08_reply") == "invite":
        "도현이 고른 식당에서 만났다. 서윤은 문 앞에서 도현을 보고 먼저 손을 흔들었다."
        s "오늘은 초대받는 사람답게 따라왔어. 메뉴 설명은 조금 기대하고 있고~"
    elif memory.get("seoyun_r08_reply") == "story":
        s "빨래 널고 앉아 있던 창가 얘기, 오늘은 어디부터 들려줄래?"
    else:
        s "오늘은 먼저 기다리겠다고 했지. 진짜 네가 먼저 와 있었네."
    d "오늘 일할 때, 웃으면서도 안 되는 건 분명히 말하시는 게 좋았어요. 지금은 웃는 쪽을 더 오래 보고 싶고요."
    s "칭찬 뒤에 그런 말 붙이면, 밥 먹다 말고 너만 보게 되잖아."
    "저녁을 먹고 각자 집으로 돌아갔다. 토요일에는 추천한 책 이야기를 더 나누기로 했다."
    $ award_once("seoyun_R09", "seoyun", 6)
    return

label seoyun_r10:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 R10 · 추천한 책의 이유"
    $ location = "토요일 오후 · 단골 북카페"
    "서윤이 『느린 모퉁이』를 펼쳤다. 둘은 책 속에서 인물이 아무것도 해결하지 않고 귀가하는 짧은 대목을 읽었다."
    s "이 부분 때문에 좋아했어. 오늘 다 답 안 나와도, 집에 가는 길은 남아 있잖아."
    if memory.get("seoyun_o01_status") == "completed":
        s "전에 서로 다르게 읽은 데도 좋았고. 네 감상 듣고 다시 펼친 부분이야."
    elif memory.get("seoyun_r02_response") == "wait":
        s "너도 내 대답 기다려 줬지. 다 읽은 말만 들으려는 사람은 아니구나 싶었어."
    else:
        s "잘 정리된 얘기만 들려줘야 할 것 같을 때 이 책을 펼치거든. 오늘 네 앞에서도 조금 덜 고르고 싶었고."
    d "그럼 제 문장도 먼저 읽어 주세요. 여길 좋아하는 이유, 제가 한 줄 골라 볼게요."
    menu:
        "‘오늘은 돌아갈 길을 조금 늦게 골랐다.’라고 쓴다.":
            d "집에 가기 싫다기보다 여기 좀 더 있고 싶어서요."
            s "누가 붙잡지 않아도 네가 남은 시간 같아. 나는 그게 좋아."
            $ remember("seoyun_booklet_sentence", "오늘은 돌아갈 길을 조금 늦게 골랐다.")
            $ remember("seoyun_booklet_impression", "스스로 조금 더 남은 시간")
        "‘한 잔이 식는 동안 이 골목이 익숙해졌다.’라고 쓴다.":
            d "다 알아서 익숙한 건 아니고, 다시 와도 되겠다 싶어졌어요."
            s "다음에 마실 한 잔도 생각나네. 끝난 얘기인데 다음 자리가 있고."
            $ remember("seoyun_booklet_sentence", "한 잔이 식는 동안 이 골목이 익숙해졌다.")
            $ remember("seoyun_booklet_impression", "다음 한 잔의 자리가 남는 문장")
        "‘다음에 올 이유는 아직 적지 않았다.’라고 쓴다.":
            d "지금 다 정리 안 해도 또 오고 싶어서요. 이유는 다음에 더 알겠죠."
            s "빈칸인데 밀어낸 느낌은 아니네. 다시 올 마음은 들려."
            $ remember("seoyun_booklet_sentence", "다음에 올 이유는 아직 적지 않았다.")
            $ remember("seoyun_booklet_impression", "빈칸에도 다시 오고 싶은 마음이 들림")
    "도현은 자신이 쓴 문장 옆에 서윤의 감상을 메모했다. 최종 글은 직접 더 고르기로 했다."
    $ remember("seoyun_booklet_state", "직접 쓴 문장과 독자 감상이 있는 초안, 인쇄 완성 전")
    menu:
        "둘이 합의해 유진에게 교제 사실만 알리자고 한다.":
            d "유진 씨에게는 저희 만나는 것만 말씀드릴까요? 둘이 괜찮다면요."
            s "응. 사적인 얘기는 우리한테 두고. 내일 같이 보내자."
            $ remember("seoyun_publicity", "agreed_yujin")
        "당분간 둘만 알고 지내고 싶다고 한다.":
            d "아직은 둘만 알고 싶어요. 바뀌면 먼저 이야기할게요."
            s "응. 누가 묻더라도 내가 먼저 답 정해 보내진 않을게."
            $ remember("seoyun_publicity", "private")
        "알릴 범위만 정하고 시점은 더 생각하자고 한다.":
            d "말하게 되면 교제 사실만요. 언제인지는 더 생각할래요."
            s "좋아. ‘언젠가’라고 했다고 내일 발송 예약 걸지는 않기~"
            $ remember("seoyun_publicity", "discuss_later")
    $ award_once("seoyun_R10", "seoyun", 4)
    return

label seoyun_r10_after:
    if not dating or active_route != "seoyun" or "seoyun_R10" not in completed:
        return
    $ location = "같은 토요일 밤 · 서윤의 집 — 서윤 시점"
    "서윤은 책 사이에서 오늘 쓴 메모를 꺼냈다. 도현의 문장은 고치지 않고 자기 감상만 다시 읽었다."
    sn "농담 안 붙여도 다음 말 기다려 주네. 나도 보고 싶다는 말부터 꺼내면 되는데."
    "휴대폰에 적던 ‘심심하면’을 지우고 메시지를 보냈다."
    call phone_deliver("seoyun_r10_after", "seoyun", "내일도 보고 싶어. 저녁 먹고 같이 걸을래? 여섯 시 반, 서점 앞에서.", contact="seoyun", important=True)
    call phone_deliver("seoyun_r10_accept", "dohyun", "좋아요. 여섯 시 반에 서점 앞에서 봐요. 걷고 싶은 길은 그때 같이 골라요.", contact="seoyun")
    return

label seoyun_r11:
    if not dating or active_route != "seoyun":
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
    s "오늘은 늘 가던 골목도 좋고, 네가 보여 주고 싶은 길도 좋아. 먼저 골라 볼래?"
    menu:
        "서윤이 자주 걷는 서점 뒤 골목을 함께 걷는다.":
            "서점 뒤 골목에서 화분이 늘어난 작은 계단을 봤다. 서윤도 새 화분 하나는 처음 알아봤다."
            s "익숙하다고 안 보던 게 있네. 오늘은 네가 먼저 멈췄고."
            $ remember("seoyun_walk_route", "familiar")
            $ remember("seoyun_walk_detail", "서점 뒤 계단에 늘어난 작은 화분")
        "내가 궁금했던 강변의 조용한 다리 쪽을 제안한다.":
            "도현이 고른 다리 아래로 걸었다. 난간 사이로 바람이 들어와 둘은 잠깐 멈췄다."
            d "여기 오면 말소리가 조금 작아져요. 그게 좋아서 같이 오고 싶었어요."
            $ remember("seoyun_walk_route", "riverside")
            $ remember("seoyun_walk_detail", "난간 사이 바람 때문에 목소리를 낮춘 다리")
        "골목 그늘과 강변 입구를 반씩 이어 걷자고 한다.":
            "그늘진 골목을 먼저 걷고 강변 입구에서 돌아왔다. 돌아갈 지점은 둘이 바람을 맞으며 골랐다."
            s "반씩 고르니까 돌아오는 지점도 얘기하게 되네. 오늘은 여기까지?"
            $ remember("seoyun_walk_route", "both")
            $ remember("seoyun_walk_detail", "그늘 골목 뒤 강변 입구에서 함께 고른 귀가 지점")
    s "다음 주엔 월요일부터 목요일까지 외근이 잡혔어. 금요일 저녁 일곱 시는 비워 둘 수 있어."
    d "저도 금요일 좋아요. 중간에도 연락해요. 잘 끝났다는 얘기만 아니어도요."
    s "응. 금요일 일곱 시에 이 앞에서. 못 본 얘기 쌓아 놓고 올게."
    $ remember("seoyun_reunion_plan", "금요일 저녁 일곱 시, 서점 앞 재회")
    $ award_once("seoyun_R11", "seoyun", 0)
    return

label seoyun_r12:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 R12 · 이번엔 날짜까지 말할게"
    $ location = "화요일 저녁 · 각자의 자리, 개인 메시지"
    call phone_deliver("seoyun_r12_tuesday", "seoyun", "오늘은 이동이 길었어. 책은 두 장 읽고 덮었고. 그래도 자기 전에 네 다음 말은 듣고 싶더라~", contact="seoyun")
    $ location = "목요일 퇴근 후 · 개인 메시지"
    call phone_deliver("seoyun_r12_thursday", "seoyun", "외근 끝났어. 내일 일곱 시 서점 앞 약속 그대로야. 내일은 얼굴 보고 보고 싶었다고 말할래.", contact="seoyun", important=True)
    call phone_deliver("seoyun_r12_reply", "dohyun", "저도요. 내일 일곱 시 서점 앞에서 봬요. 오늘은 푹 쉬세요.", contact="seoyun")
    $ location = "금요일 저녁 일곱 시 · 서점 앞"
    "금요일 약속한 시간에 서윤이 걸어왔다. 메시지 화면 대신 서로의 얼굴을 보고 인사했다."
    s "보고 싶었어. 이번 주는 짧게 보내고도 더 말하고 싶더라."
    d "저도요. 일요일에 걸었던 데 생각도 났고요."
    s "[memory['seoyun_walk_detail']], 그거? 나도 생각났어."
    "함께 저녁을 먹었다. 서윤은 오늘 만나려고 골랐다는 옷의 소매를 정리했다."
    d "다음 계절에도 이렇게 같이 다니고 싶어요. 언젠가는 같이 사는 얘기도 해 보고 싶고요."
    s "벌써 집 계약하는 사이야? 진도가 빠른데~"
    d "지금 계약하자는 건 아니에요. 나중에 서로 어떻게 생각하는지 이야기하고 싶다는 거요."
    s "응. 그 얘기도 남겨 두자. 오늘은 네 얼굴부터 조금 더 보고 싶어."
    $ remember("seoyun_future_question", "언젠가 함께 사는 생각을 서로 이야기해 보고 싶다고 도현이 제안, 동거 합의 아님")
    $ remember("seoyun_future_question_status", "아직 제대로 답하지 않은 질문")
    "저녁 뒤 서윤의 집에 들러 차를 마셨다. 서윤은 둘이 고른 오늘의 약속부터 이야기했다."
    s "오늘 다시 만나서 좋아. 그건 지금 분명히 말할 수 있어. 오늘은 여기서 같이 밤을 보내고 싶어. 너도 괜찮으면."
    call seoyun_private_evening("r12", "special")
    $ award_once("seoyun_R12", "seoyun", 4)
    return

```
