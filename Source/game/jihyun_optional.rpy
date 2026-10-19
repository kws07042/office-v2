label jihyun_o01_offer:
    if not dating or active_route != "jihyun" or memory.get("jihyun_o01_status"):
        return
    menu:
        "잠깐 만나기 — 일정표의 빈칸 하나 (선택 일상)":
            call jihyun_o01
        "본편 계속 — 다음 수요일의 만남으로":
            $ remember("jihyun_o01_status", "skipped")
        "다음에도 빈 시간을 남겨 두자고 짧게 말하고 본편 계속":
            d "다음에는 계획 안 세운 시간도 같이 보내 봐요."
            j "응. 뭘 할지부터 정해 오지 않을게."
            $ remember("jihyun_o01_status", "brief")
    return

label jihyun_o01:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 O01 · 일정표의 빈칸 하나"
    $ location = "같은 토요일 늦은 오후 · 강변 가게 앞"
    "걷다가 들르려던 작은 가게가 닫혀 있었다. 빗방울까지 떨어지자 지현이 휴대폰을 꺼내려다 멈췄다."
    j "다른 데 세 군데쯤 찾아 버릴 뻔했네. 지금 뭐 하고 싶어?"
    menu:
        "처마 아래에서 비를 구경하며 잠깐 머문다.":
            "둘은 처마 밑으로 들어가 바닥에 생기는 작은 물자국을 봤다."
            d "어디 안 찾아도 지금은 괜찮네요."
            "처마 끝에서 빗방울이 튀자 지현이 구두 앞코를 한 발 물렸다."
            j "저 선까지만 비 안 오는 줄 알았는데."
            d "조금 더 안쪽으로 오세요. 여긴 제가 먼저 확인했어요."
            j "응. 그건 믿고 갈게."
            $ remember("jihyun_o01_activity", "처마 아래 비 구경")
        "가까운 카페에서 따뜻한 차를 마신다.":
            "가까운 카페에서 젖은 소매를 털고 차를 주문했다."
            "지현이 젖은 소매를 한 번 더 털었다. 도현이 건넨 냅킨은 컵보다 소매 쪽으로 갔다."
            j "차는 따뜻한데 나는 아직 좀 축축하네."
            d "여기 오래 앉아 있을 이유는 생겼네요."
            j "말은 잘하네. 냅킨 하나 더 부탁해."
            $ remember("jihyun_o01_activity", "비 피한 카페에서 차")
        "우산을 사서 정류장까지 천천히 같이 걷는다.":
            "편의점에서 우산을 골라 정류장까지 걸었다. 급히 뛰지 않아도 버스는 다음 차가 있었다."
            d "오늘 계획은 바뀌었는데, 같이 걷는 건 남았네요."
            j "응. 다음 차까지 여기 같이 있자."
            $ remember("jihyun_o01_activity", "우산 쓰고 정류장까지 걷기")
    $ remember("jihyun_o01_status", "completed")
    $ award_once("jihyun_O01", "jihyun", 2)
    return

label jihyun_o02_offer:
    if not dating or active_route != "jihyun" or memory.get("jihyun_o02_status"):
        return
    menu:
        "잠깐 더 보기 — 완성하지 않아도 되는 취미 (선택 일상)":
            call jihyun_o02
        "본편 계속 — 일요일 놀이 약속으로":
            $ remember("jihyun_o02_status", "skipped")
        "다음에도 만들던 중간 모습을 보여 달라고 하고 본편 계속":
            d "다음에도 완성 전부터 보여 주세요. 변한 데 찾는 것도 좋아요."
            j "응. 다 만들 때까지 기다리게 하지는 않을게."
            $ remember("jihyun_o02_status", "brief")
    return

label jihyun_o02:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 O02 · 완성하지 않아도 되는 취미"
    $ location = "같은 토요일 오후 · 조립품 앞"
    j "설명서대로면 지붕 붙일 차례인데. 오늘은 더 보고 싶어."
    menu:
        "작은 집 안에 놓인 의자가 왜 창가를 향하는지 묻는다.":
            d "의자가 창가를 보네요. 지현 씨가 그렇게 두신 거예요?"
            j "응. 저 자리에서 차 마시면 좋겠다 싶어서. 그건 설명서에 없었어."
            $ remember("jihyun_o02_detail", "직접 창가로 돌려 둔 작은 의자")
        "조립품의 안쪽을 기록용으로 찍어도 되는지 묻는다.":
            d "이 안쪽 사진 한 장 남겨도 돼요? 밖에 올리지 않고 저만 볼게요."
            j "응. 지붕 닫기 전 모습은 그 사진으로 다시 보겠네."
            "허락받은 안쪽만 한 장 찍었다."
            $ remember("jihyun_o02_detail", "허락받아 찍은 지붕 닫기 전 안쪽 사진")
        "아무것도 더 붙이지 않고 차 마시며 같이 들여다본다.":
            "둘은 도구를 내려놓고 차를 마셨다. 작은 창틀 사이로 들어오는 빛이 조금 옮겨 갔다."
            j "분명 같이 조립하려고 불렀는데 구경만 하고 있네."
            d "저는 꽤 집중하고 있어요. 지붕 없는 집은 흔하지 않아서요."
            j "그럼 오늘까지만 특별 공개. 다음엔 조금 닫힐 수도 있어."
            $ remember("jihyun_o02_detail", "차 마시며 본 창틀의 빛")
    $ remember("jihyun_o02_status", "completed")
    $ award_once("jihyun_O02", "jihyun", 2)
    return

label jihyun_o03_offer:
    if not dating or active_route != "jihyun" or memory.get("jihyun_o03_status"):
        return
    menu:
        "잠깐 만나기 — 부탁의 연습 (선택 일상)":
            call jihyun_o03
        "본편 계속 — 일요일 저녁 약속으로":
            $ remember("jihyun_o03_status", "skipped")
        "저녁에 내가 원하는 것도 먼저 말하겠다고 하고 본편 계속":
            d "저녁에는 제가 하고 싶은 것도 먼저 말해 볼게요."
            j "응. 먼저 물어보기 전에 들어 보고 싶어."
            $ remember("jihyun_o03_status", "brief")
    return

label jihyun_o03:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 O03 · 부탁의 연습"
    $ location = "일요일 오후 · 동네 공원 입구"
    "각자 집에서 오전을 보낸 뒤 공원에서 만났다. 지현은 벤치를 보고 먼저 도현을 불렀다."
    j "오늘은 그늘에서 조금 앉고 싶어. 대신 네가 집에 갈 시간도 먼저 듣고 싶고."
    menu:
        "벤치에서 쉰 뒤 내가 고른 빵집에 같이 가 달라고 한다.":
            d "좋아요. 쉰 다음에는 저 빵집 같이 가 주세요. 들어가 보고 싶었어요."
            "그늘에서 쉬고 빵집에 들렀다. 둘은 각자 먹고 싶은 빵 하나씩 골랐다."
            $ remember("jihyun_o03_request", "그늘 휴식 뒤 도현이 고른 빵집")
        "조금 피곤하니 삼십 분만 쉬고 각자 집에 들렀다 저녁에 만나자고 한다.":
            d "저도 좀 피곤해요. 삼십 분만 쉬고 집에 들렀다가 저녁에 다시 만나요."
            j "응. 더 있어 달라고 하고 싶어도 그 시간은 지킬게."
            "삼십 분을 함께 쉬고 헤어졌다. 저녁 약속은 그대로 남겨 뒀다."
            $ remember("jihyun_o03_request", "삼십 분 휴식 후 각자 귀가, 저녁 재회")
        "처음 보는 사람으로 내 기록집 한 줄만 읽어 달라고 부탁한다.":
            d "쉬는 동안 이 한 줄 읽어 주실래요? 고칠 곳보다 어떤 장면인지 듣고 싶어요."
            j "응. 나는 비 오기 직전 골목이 생각나. 너는 다른 날 썼을 수도 있겠지만."
            "도현은 지현이 떠올린 날씨를 메모했다. 부탁한 한 줄만 보고 노트를 덮었다."
            $ remember("jihyun_o03_request", "기록집 한 줄의 첫 감상 부탁")
    $ remember("jihyun_o03_status", "completed")
    $ award_once("jihyun_O03", "jihyun", 2)
    return
