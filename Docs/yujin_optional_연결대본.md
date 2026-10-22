> 현행 갱신: 기획 v3.05 / Windows 0.32.0-dialogue-clarity — 2026-10-21
> 뜻을 짐작해야 하는 농담·혼합 비유·대답의 연결·화자와 소품 불일치를 정리했다. 대사이해도_전체검수_보고서_v1.md와 현행 실행 대본을 우선한다. 사건·선택 기억·인물 설정·자산 계획은 유지한다. 아래 이전 갱신은 이력이다.

# 유진 구현 대본 — yujin_optional.rpy

```renpy
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
            y "저는 빈 쪽을 먼저 봤는데. 다음엔 의자 가까이에서 한 번 더 볼래요."
            $ remember("yujin_o01_impression", "returning")
        "유진의 설명을 듣고 빈 방의 고요도 궁금해졌다고 한다.":
            d "생각해 보니 빈 방의 소리도 궁금해졌어요. 유진 씨는 조용한 쪽부터 보셨겠네요."
            y "네. 저는 그 조용한 쪽이 조금 쓸쓸했어요. 도현 씨는 어떤 소리일지 고르실 것 같고요."
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
    "유진이 개인 노트의 뒷장을 펼쳤다. 창가 빛이 겹쳐 보이는 작은 컵 그림이었다."
    y "이건 그냥 컵 보다가 그렸어요. 보여 드리려고 넘기니까 좀 거창해지네요."
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
    y "잘 그렸는지보다 어디부터 보셨는지 들으니까, 다음 것도 보여 드리고 싶어져요."
    d "그럼 다음에도 제 눈부터 빌려 드릴게요. 정답 맞히는 건 조금 자신 없어서요."
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
            y "네. 제 감상도 제목 정하실 때 같이 들려드릴게요."
            $ remember("yujin_o03_action", "photo")
            $ remember("yujin_o03_photo_taken")
        "오늘 떠오른 짧은 문장을 적고 유진에게 읽어 준다.":
            d "‘기다리던 사람이 먼저 내 자리를 골라 뒀다.’ 오늘은 이렇게 남길래요."
            y "...그러면 제가 다음 자리도 고르고 싶어지잖아요."
            $ remember("yujin_o03_action", "sentence")
        "기록은 잠깐 쉬고 유진과 같은 곳을 바라본다.":
            d "오늘은 기록 안 해도 괜찮을 것 같아요. 같이 있다는 쪽이 먼저여서요."
            y "좋아요. 그 말은 제가 조금 기억해 둘래요."
            $ remember("yujin_o03_action", "stay")
    $ remember("yujin_o03_status", "completed")
    $ award_once("yujin_O03", "yujin", 2)
    return

```
