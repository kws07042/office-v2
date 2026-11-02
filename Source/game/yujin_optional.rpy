label yujin_o01_offer:
    if not dating or active_route != "yujin" or memory.get("yujin_o01_status"):
        return
    menu:
        "잠깐 더 이야기하기 — 전시가 끝난 뒤의 감상 (선택 일상)":
            call yujin_o01
        "본편 계속 — 다음 연인 만남으로":
            $ remember("yujin_o01_status", "skipped")
        "전시 얘기는 다음에 더 듣고 싶다고 짧게 말하고 본편 계속":
            d "오늘 고른 말은 다음에도 듣고 싶어요. 지금 다 적지 않고 남겨 둬도 되겠네요."
            y "네. 전시 끝났다고 감상까지 끝난 건 아니니까요~"
            $ remember("yujin_o01_status", "brief")
    return

label yujin_o01:
    if not dating or active_route != "yujin":
        return
    $ chapter = "유진 O01 · 전시가 끝난 뒤의 감상"
    $ location = "연인 첫 주말의 늦은 오후 · 공원 벤치"
    y "그 전시의 첫 그림요. 저는 혼자 남은 방 같다고 했는데, 도현 씨는 누가 돌아올 것 같다고 하셨잖아요."
    d "네. 의자가 조금 비뚤어져 있어서요. 유진 씨가 다르게 보신 것도 기억나요."
    y "오늘 다시 말하면 어느 쪽이세요? 제 쪽으로 와 달라는 질문은 아니고요~"
    menu:
        "아직 누군가 돌아올 방처럼 보인다고 내 감상을 말한다.":
            d "저는 아직 돌아올 것 같아요. 기다리는 쪽 이야기가 더 궁금해서요."
            "유진이 빈 벤치 한쪽에 잠깐 시선을 줬다."
            y "지금 이 의자도 누가 금방 돌아올 것 같아요?"
            d "저쪽은 가방 자리로 놔둬요. 유진 씨는 계속 제 옆에 계시고요."
            y "...이 자리는 제가 먼저 골랐는데요~"
            $ remember("yujin_o01_impression", "returning")
        "유진의 설명을 듣고 빈 방의 고요도 궁금해졌다고 한다.":
            d "생각해 보니 빈 방의 소리도 궁금해졌어요. 유진 씨는 조용한 쪽부터 보셨겠네요."
            "유진이 입을 다물자 벤치 뒤 나뭇잎 소리가 들렸다."
            y "저는 이런 조용함이면 좋겠어요. 빈 방보다 덜 쓸쓸해서요."
            d "저는 옆에서 노트 넘기는 소리도 하나 넣을래요."
            $ remember("yujin_o01_impression", "quiet_room")
        "같은 그림을 다르게 본 시간이 더 기억난다고 말한다.":
            d "저는 그림 다음에 유진 씨 대답 기다린 게 남았어요. 같은 걸 보고도 다음 말은 몰라서요."
            y "...그 감상은 노트에 적으면 제가 자꾸 다시 볼 텐데요."
            $ remember("yujin_o01_impression", "different_answers")
    "유진은 서로 다른 두 감상을 줄을 바꿔 적었다. 답을 하나로 고치지 않고 노트를 덮는다."
    $ remember("yujin_o01_status", "completed")
    $ award_once("yujin_O01", "yujin", 2)
    return

label yujin_o02_offer:
    if not dating or active_route != "yujin" or memory.get("yujin_o02_status"):
        return
    menu:
        "잠깐 더 보기 — 작은 스케치 한 장 (선택 일상)":
            call yujin_o02
        "본편 계속 — 일요일 음악 약속으로":
            $ remember("yujin_o02_status", "skipped")
        "다음에도 개인 그림을 보여 달라고 짧게 말하고 본편 계속":
            d "일로 그린 것 말고, 유진 씨가 그냥 남기고 싶었던 그림도 다음에 보고 싶어요."
            y "네. 꼭 완성한 것만 골라 오지는 않을게요."
            $ remember("yujin_o02_status", "brief")
    return

label yujin_o02:
    if not dating or active_route != "yujin":
        return
    $ chapter = "유진 O02 · 작은 스케치 한 장"
    $ location = "기록집을 함께 본 토요일 오후 · 같은 카페"
    "유진이 개인 노트의 뒷장을 펼쳤다. 창가 빛이 겹친 작은 컵 그림 옆으로 탁자에 있던 잔을 옮겼다. 두 잔의 손잡이 방향이 달랐다."
    y "이건 집에서 그린 거예요. 지금 컵하고 닮았다고 바꿔 그려 온 건 아니고요~"
    menu:
        "겹친 빛이 눈에 들어온다고 구체적인 감상을 말한다.":
            d "저는 컵보다 겹친 빛이 먼저 보여요. 같은 물건인데 두 번 보는 것 같네요."
            y "저도 그 빛을 남기고 싶어서 그렸어요. 물 마시면 잔에 비친 모양이 달라지니까요."
            $ remember("yujin_o02_impression", "overlapping_light")
        "어떤 순간 그리기 시작했는지 묻는다.":
            d "그리기 시작한 순간이 궁금해요. 컵 들기 전에 멈추신 거예요?"
            y "네. 마시면 빛이 달라질까 봐요. 그래서 조금 미지근해진 다음에 마셨어요."
            $ remember("yujin_o02_impression", "stopped_before_drinking")
        "내가 남기는 사진과 다른 점을 이야기한다.":
            d "저는 먼저 찍고 나중에 왜 멈췄는지 고를 것 같아요. 유진 씨는 그리면서 고르시는 거네요."
            y "네. 대신 찍은 다음에 찾는 것도 궁금해요. 같은 컵으로 한번 비교해 보고 싶어요."
            $ remember("yujin_o02_impression", "drawing_and_photo")
    "유진이 그림을 덮고 실제 잔을 들었다. 도현도 자기 잔을 들다가 한 번 더 그림 쪽을 봤다."
    y "다음 그림도 컵일까 봐 걱정되세요?"
    d "아뇨. 제 잔도 좀 있어 보이게 들어 볼까 했어요."
    y "어떻게 들어도 같은 잔인데요~ ...손잡이 왼쪽으로 돌려 봐 주세요. 그 각도는 조금 좋네요."
    $ remember("yujin_o02_subject", "창가 빛이 겹친 작은 컵")
    $ remember("yujin_o02_status", "completed")
    $ award_once("yujin_O02", "yujin", 2)
    return

label yujin_o03_offer:
    if not dating or active_route != "yujin" or not memory.get("yujin_r15_complete") or memory.get("yujin_o03_status"):
        return
    menu:
        "일요일 오후에 잠깐 만나기 — 이번엔 도현 씨 취향 (선택 일상)":
            call yujin_o03
        "본편 계속 — 일요일 저녁의 두 초안으로":
            $ remember("yujin_o03_status", "skipped")
        "오후는 각자 쉬고 저녁에 만나자고 짧게 전한 뒤 본편 계속":
            $ location = "일요일 오전 · 각자의 집, 개인 메시지"
            call phone_deliver("yujin_o03_brief_d", "dohyun", "오후에는 제 노트 정리하고 쉴게요. 저녁에 같이 보기로 한 건 그대로예요. 보고 싶어요, 유진 씨.", contact="yujin")
            call phone_deliver("yujin_o03_brief_y", "yujin", "네. 저도 오후엔 제 것 정리할게요. 저녁에는 노트 말고 얼굴부터 보여 주세요~", contact="yujin")
            $ remember("yujin_o03_status", "brief")
    return

label yujin_o03:
    if not dating or active_route != "yujin":
        return
    $ chapter = "유진 O03 · 이번엔 도현 씨 취향"
    if memory.get("yujin_r10_page") == "entrance_bench":
        $ location = "일요일 오후 · 전시 공간 입구의 긴 의자"
        y "촬영 후보로 남겨 두셨잖아요. 오늘 다시 와 보고 싶을 것 같아서요. 앉는 쪽부터 해도 좋고요."
        $ remember("yujin_o03_prepared", "기록집 후보였던 전시 입구 긴 의자에 다시 오기")
    elif memory.get("yujin_r10_page") == "one_sentence":
        $ location = "일요일 오후 · 조용한 동네 카페"
        y "한 문장으로 한 페이지 고르셨잖아요. 오늘은 말 적을 자리부터 골라 봤어요. 도현 씨가 더 쓰고 싶은지 궁금해서요."
        $ remember("yujin_o03_prepared", "한 문장을 적을 수 있는 조용한 카페 자리")
    elif memory.get("yujin_r10_page") == "open_space":
        $ location = "일요일 오후 · 동네 산책길"
        y "다음 만남 뒤에 채울 칸 남겨 두셨죠? 오늘은 계획 너무 채우지 않고 걷자고 하고 싶었어요."
        $ remember("yujin_o03_prepared", "빈칸을 남긴 기록집 취향에 맞춰 목적지를 비운 짧은 산책")
    else:
        $ location = "일요일 오후 · 동네 카페"
        y "오늘은 도현 씨가 남기고 싶은 것부터 고르면 좋겠어요. 이 자리 괜찮으세요?"
        $ remember("yujin_o03_prepared", "현재 취향을 직접 묻는 짧은 카페 만남")
    d "제 얘기로 먼저 골라 주셨네요. 오늘은 제가 천천히 봐도 되겠어요."
    menu:
        "인물은 담지 않고 지금 장소를 사진 한 장으로 남긴다.":
            "도현이 인물 없이 장소를 한 장 찍었다. 유진은 촬영이 끝난 뒤 같은 방향을 바라봤다."
            d "오늘은 이 한 장이요. 제목은 조금 더 있다가 고를래요."
            y "저는 왼쪽 끝이 좋은데, 도현 씨는 가운데만 보시네요?"
            "유진이 화면에 손을 대지 않고 사진의 끝부분을 가리켰다. 도현은 전체가 보이게 화면을 돌려 줬다."
            d "찍은 사람보다 먼저 찾으시면 어떡해요."
            y "제목 정하실 때 얘기하려고 했는데요. 너무 오래 가운데만 보셔서~"
            d "그럼 그쪽도 좀 볼게요. 유진 씨가 본 쪽."
            "유진은 이번엔 사진을 보지 않았다. 도현이 고개를 들자 그제야 화면 끝으로 시선을 내렸다."
            $ remember("yujin_o03_action", "photo")
            $ remember("yujin_o03_photo_taken")
        "오늘 떠오른 짧은 문장을 적고 유진에게 읽어 준다.":
            d "‘기다리던 사람이 먼저 내 자리를 골라 뒀다.’ 오늘은 이렇게 남길래요."
            y "잠깐만요. ‘기다리던 사람’은 저예요, 도현 씨예요?"
            d "쓰면서는 저였는데요."
            y "저도 먼저 와서 기다렸는데. 제 자리도 한 칸 주세요~"
            "도현이 문장 끝에 붙이려던 마침표 앞에서 펜을 멈췄다."
            d "그럼 ‘서로 기다리던 사람들’... 너무 설명 같아요."
            y "그냥 두세요. 읽을 때마다 제가 제 쪽으로 읽을래요."
            "유진이 문장을 다시 읽었다. 이번에는 ‘기다리던’ 앞에서 짧게 웃었다."
            $ remember("yujin_o03_action", "sentence")
        "기록은 잠깐 쉬고 유진과 같은 곳을 바라본다.":
            d "오늘은 기록 쉬어요. 적으려고 보면 자꾸 제목부터 찾게 돼서요."
            y "그럼 저도 감상 안 고를래요. 방금 하나 생각했는데요."
            d "그건 더 궁금한데요?"
            y "쉬자고 하신 분이 먼저 물어보시면 어떡해요~"
            "도현이 노트를 가방에 넣었다. 유진도 입을 다물었다가 먼저 웃음을 터뜨렸다."
            y "아, 이렇게 안 말하려고 하니까 더 말하고 싶네요. 도현 씨 오늘 머리, 여기 조금 떴어요."
            d "그건 제목보다 먼저 알려 주셔야죠!"
            $ remember("yujin_o03_action", "stay")
    $ remember("yujin_o03_status", "completed")
    $ award_once("yujin_O03", "yujin", 2)
    return
