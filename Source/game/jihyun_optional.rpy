label jihyun_o01_offer:
    $ progression_enter("jihyun_o01_offer")
    $ progression_checkpoint("jihyun_o01_offer")
    if not dating or active_route != "jihyun" or memory.get("jihyun_o01_status"):
        $ progression_note_ending()
        return
    $ progression_enter("jihyun_o01_offer.choice01")
    $ progression_checkpoint("jihyun_o01_offer.choice01")
    menu:
        "잠깐 만나기 — 일정표의 빈칸 하나 (선택 일상)":
            call jihyun_o01
        "본편 계속 — 다음 수요일의 만남으로":
            $ remember("jihyun_o01_status", "skipped")
        "다음에도 빈 시간을 남겨 두자고 짧게 말하고 본편 계속":
            d "다음엔 뭐 할지 비워 두고 만나요."
            j "알았어. 일정표는 안 짤게. ...메모 한 줄 정도는 봐줘."
            $ remember("jihyun_o01_status", "brief")
    $ progression_note_ending()
    return

label jihyun_o01:
    $ progression_enter("jihyun_o01")
    $ progression_checkpoint("jihyun_o01")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 O01 · 일정표의 빈칸 하나"
    $ location = "같은 토요일 늦은 오후 · 강변 가게 앞"
    "들르려던 작은 가게는 문이 닫혀 있었다. 빗방울이 떨어지자 지현은 휴대폰을 꺼내려다 손을 멈췄다."
    dn "계획이 틀어졌다. 지현 씨가 화부터 낼 줄 알았는데."
    j "하마터면 세 군데 더 찾을 뻔했네. 넌 지금 뭐 하고 싶어?"
    $ progression_enter("jihyun_o01.choice01")
    $ progression_checkpoint("jihyun_o01.choice01")
    menu:
        "처마 밑에서 비 구경을 한다.":
            "처마 밑으로 들어가 바닥에 번지는 빗자국을 봤다."
            d "어디 안 찾아도 지금 괜찮네요."
            "처마 끝에서 빗방울이 튀자 지현이 구두 앞코를 한 발 물렸다."
            j "저 선까지만 비 안 오는 줄 알았는데."
            d "좀 더 안으로 들어오세요. 여긴 제가 미리 봤어요."
            j "그래. 한 발만 더 안쪽으로 갈게."
            $ remember("jihyun_o01_activity", "처마 아래 비 구경")
        "근처 카페로 피한다.":
            "가까운 카페에서 젖은 소매를 털고 차를 주문했다."
            "지현이 젖은 소매를 한 번 더 털었다. 도현이 건넨 냅킨은 컵보다 소매 쪽으로 갔다."
            j "차는 따뜻하네. 난 아직 축축한데."
            d "여기 오래 앉아 있을 이유는 생겼네요."
            j "말은 잘하네. 냅킨 하나 더 부탁해."
            $ remember("jihyun_o01_activity", "비 피한 카페에서 차")
        "우산 하나 사서 같이 쓴다.":
            "편의점에서 우산을 사 정류장까지 걸었다. 뛰지 않아도 다음 버스가 있었다."
            d "가려던 덴 못 갔어도 같이 걷기는 하네요."
            j "그럼 다음 차까지는 여기 같이 있자."
            $ remember("jihyun_o01_activity", "우산 쓰고 정류장까지 걷기")
    $ remember("jihyun_o01_status", "completed")
    dn "가게 문이 닫혀 있었는데도 서둘러 헤어지지 않았다. 오늘 비는 좀 더 와도 괜찮겠다."
    $ award_once("jihyun_O01", "jihyun", 2)
    $ progression_note_ending()
    return

label jihyun_o02_offer:
    $ progression_enter("jihyun_o02_offer")
    $ progression_checkpoint("jihyun_o02_offer")
    if not dating or active_route != "jihyun" or memory.get("jihyun_o02_status"):
        $ progression_note_ending()
        return
    $ progression_enter("jihyun_o02_offer.choice01")
    $ progression_checkpoint("jihyun_o02_offer.choice01")
    menu:
        "잠깐 더 보기 — 완성하지 않아도 되는 취미 (선택 일상)":
            call jihyun_o02
        "본편 계속 — 일요일 놀이 약속으로":
            $ remember("jihyun_o02_status", "skipped")
        "다음에도 만들던 중간 모습을 보여 달라고 하고 본편 계속":
            d "다음에도 완성 전부터 보여 주세요. 뭐가 바뀌었나 찾는 것도 재밌어요."
            j "그래. 다음엔 어디까지 했는지 내가 먼저 사진 보낼게."
            $ remember("jihyun_o02_status", "brief")
    $ progression_note_ending()
    return

label jihyun_o02:
    $ progression_enter("jihyun_o02")
    $ progression_checkpoint("jihyun_o02")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 O02 · 완성하지 않아도 되는 취미"
    $ location = "같은 토요일 오후 · 조립품 앞"
    j "다음 순서가 지붕이야. 근데 오늘은 이대로 좀 보자."
    dn "설명서 덮고 난 뒤 저 얼굴. 회사에선 한 번도 못 봤다."
    $ progression_enter("jihyun_o02.choice01")
    $ progression_checkpoint("jihyun_o02.choice01")
    menu:
        "창가 쪽 의자에 대해 묻는다.":
            d "의자가 창가를 보네요. [memory.get('jihyun_private_name', '지현 씨')], 이건 직접 고르신 자리예요?"
            j "응. 저 자리에서 차 마시면 좋겠다 싶어서. 그건 설명서에 없었어."
            $ remember("jihyun_o02_detail", "직접 창가로 돌려 둔 작은 의자")
        "안쪽 사진 한 장을 부탁한다.":
            d "이 안쪽 사진 한 장 남겨도 돼요? 밖에 올리지 않고 저만 볼게요."
            j "응. 지붕 닫기 전 모습은 그 사진으로 다시 보겠네."
            "허락받은 안쪽만 한 장 찍었다."
            $ remember("jihyun_o02_detail", "허락받아 찍은 지붕 닫기 전 안쪽 사진")
        "아무것도 안 하고 같이 들여다본다.":
            "도구를 내려놓고 차를 마셨다. 작은 창틀 사이로 들어오는 빛이 조금씩 옮겨 갔다."
            j "같이 조립하자고 불러 놓고 구경만 시키네, 내가."
            d "전 꽤 집중하고 있어요. 지붕 없는 집은 흔하지 않아서요."
            j "그럼 오늘까지만 특별 공개. 다음엔 좀 닫힐 수도 있어."
            $ remember("jihyun_o02_detail", "차 마시며 본 창틀의 빛")
    $ remember("jihyun_o02_status", "completed")
    dn "특별 공개라는 말, 농담이 아니네. 아직 덜 만든 걸 누구한테 보여 준 적이 없다더니."
    $ award_once("jihyun_O02", "jihyun", 2)
    $ progression_note_ending()
    return

label jihyun_o03_offer:
    $ progression_enter("jihyun_o03_offer")
    $ progression_checkpoint("jihyun_o03_offer")
    if not dating or active_route != "jihyun" or memory.get("jihyun_o03_status"):
        $ progression_note_ending()
        return
    $ progression_enter("jihyun_o03_offer.choice01")
    $ progression_checkpoint("jihyun_o03_offer.choice01")
    menu:
        "잠깐 만나기 — 부탁의 연습 (선택 일상)":
            call jihyun_o03
        "본편 계속 — 일요일 저녁 약속으로":
            $ remember("jihyun_o03_status", "skipped")
        "저녁에 내가 원하는 것도 먼저 말하겠다고 하고 본편 계속":
            d "저녁엔 저도 뭐 하고 싶은지 먼저 말해 볼게요."
            j "좋아. 오늘 저녁엔 네 얘기부터 듣고 싶어."
            $ remember("jihyun_o03_status", "brief")
    $ progression_note_ending()
    return

label jihyun_o03:
    $ progression_enter("jihyun_o03")
    $ progression_checkpoint("jihyun_o03")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 O03 · 부탁의 연습"
    $ location = "일요일 오후 · 동네 공원 입구"
    "각자 집에서 오전을 보낸 뒤 공원에서 만났다. 지현은 벤치를 보자 도현을 불렀다."
    dn "부탁하는 연습하자던 사람이 벤치 하나 고르는 데도 내 눈치를 본다."
    j "저기 그늘에 잠깐 앉을까? 너 오늘 몇 시쯤 들어가야 돼?"
    $ progression_enter("jihyun_o03.choice01")
    $ progression_checkpoint("jihyun_o03.choice01")
    menu:
        "내가 찾은 빵집에 같이 가자고 한다.":
            d "좋아요. 좀 쉬고 저 빵집 같이 가실래요? 한번 들어가 보고 싶었어요."
            "그늘에서 쉬고 빵집에 들렀다. 도현은 크림빵을, 지현은 소금빵을 집었다."
            j "들어올 때부터 그거 보고 있었지?"
            d "네. 근데 제가 가자고 한 가게라 다른 것도 둘러보는 척했어요."
            j "나한테 추천하려고?"
            d "그것도 있고, 마지막 하나라 빨리 집고 싶어서요."
            "지현이 비어 버린 크림빵 칸을 보고 자기 쟁반을 조금 들어 보였다."
            j "잘 집었네. 내 건 양보 안 해도 되고."
            d "크림빵도 안 뺏으실 거죠?"
            j "안 뺏어. 너 크림빵 앞에선 표정 관리 안 되는구나?"
            $ remember("jihyun_o03_request", "그늘 휴식 뒤 도현이 고른 빵집")
        "삼십 분만 쉬고 저녁에 다시 보자고 한다.":
            d "저도 좀 피곤해요. 삼십 분만 쉬고 집에 들렀다가 저녁에 다시 만나요."
            j "응. 저녁엔 피곤한 얼굴 말고 좀 잔 얼굴 보고 싶어."
            "휴대폰에 알람을 맞춰 놓고 벤치 등받이에 기댔다. 지현도 반듯하게 앉아 있던 등을 조금 풀었다."
            d "이 벤치는 합격이네요. 일어나기 싫어져서 문제지만."
            j "심사 끝났으면 눈 좀 감아. 내가 깨워 줄게."
            "알람이 울리자 도현이 일어났다. 지현은 잠깐 눈을 가늘게 떴다가 가방을 들었다."
            j "내가 깨워 준댔는데 네가 먼저 일어나네. ...저녁엔 나도 좀 기대고 싶어."
            "삼십 분을 함께 쉬고 헤어졌다. 저녁 약속은 그대로 남겨 뒀다."
            $ remember("jihyun_o03_request", "삼십 분 휴식 후 각자 귀가, 저녁 재회")
        "기록집 한 줄만 읽어 달라고 부탁한다.":
            d "쉬는 김에 이 한 줄만 봐 주실래요? 어떤 장면이 떠오르세요?"
            j "응. 난 비 오기 직전 골목이 생각나. 네가 쓴 날이랑은 다를 수도 있겠지만."
            "도현은 지현이 떠올린 날씨를 메모했다. 부탁한 한 줄만 보고 노트를 덮었다."
            $ remember("jihyun_o03_request", "기록집 한 줄의 첫 감상 부탁")
    $ remember("jihyun_o03_status", "completed")
    dn "한 줄이면 되는 부탁이다. 이 정도는 오래오래 들어주고 싶다."
    $ award_once("jihyun_O03", "jihyun", 2)
    $ progression_note_ending()
    return
