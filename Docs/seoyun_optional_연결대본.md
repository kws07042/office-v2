# 서윤 실제 구현 대본 — seoyun_optional.rpy

```renpy
label seoyun_o01_offer:
    if not dating or active_route != "seoyun" or memory.get("seoyun_o01_status"):
        return
    menu:
        "잠깐 책 읽기 — 책 제목을 기억하는 사람 (선택 일상)":
            call seoyun_o01
        "본편 계속 — 다음 수요일의 만남으로":
            $ remember("seoyun_o01_status", "skipped")
        "추천한 책은 다음에도 이야기하자고 짧게 말하고 본편 계속":
            d "그 책 제목 기억해 둘게요. 아직 안 읽은 데도 다음에 듣고 싶어요."
            s "좋아. 오늘 읽었다는 확인 도장부터 찍진 않을게~"
            $ remember("seoyun_o01_status", "brief")
    return

label seoyun_o01:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 O01 · 책 제목을 기억하는 사람"
    $ location = "같은 토요일 늦은 오후 · 북카페"
    if memory.get("seoyun_next_date_plan") != "bookcafe":
        "헤어지기 전 서윤의 단골 북카페로 자리를 옮겼다. 서윤이 추천했던 책을 선반에서 꺼냈다."
    "『느린 모퉁이』에서 돌아가는 길에 같은 창문을 한 번 더 보는 짧은 대목을 함께 읽었다. 처음 보는 부분은 서두르지 않았다."
    s "난 돌아가기 전에 한 번 더 확인하는 마음 같더라. 너는 어디서 멈췄어?"
    menu:
        "다시 보는 창문보다 돌아가는 발걸음이 남았다고 한다.":
            d "저는 돌아가는 쪽이요. 한번 봤다고 꼭 안에 들어가야 하는 건 아니니까요."
            s "나는 안쪽을 먼저 봤네. 네 말 듣고 밖의 발걸음도 궁금해졌어."
            $ remember("seoyun_o01_impression", "창문 밖으로 돌아가는 발걸음")
        "그 창문을 지나쳤던 다른 날들이 궁금하다고 한다.":
            d "이날만 다시 본 건 아닐 것 같아서요. 전에는 어떻게 지나갔을까요?"
            s "그 앞날들까지 읽는구나. 난 지금 돌아본 순간에만 있었네."
            $ remember("seoyun_o01_impression", "다시 보기 전 지나쳤던 다른 날들")
        "서로 다른 곳에서 멈춘 얘기가 더 기억난다고 말한다.":
            d "같이 읽고 대답 기다리는 게 좋아요. 어디가 좋으셨는지 제가 먼저 알 수 없어서요."
            s "그 말 들으니까 다음 장도 네 대답 기다려 보고 싶어지네."
            $ remember("seoyun_o01_impression", "같은 대목을 다르게 읽고 답을 기다린 시간")
    $ remember("seoyun_o01_read", "느린 모퉁이의 같은 창문을 다시 보는 대목, 전권 완독 아님")
    $ remember("seoyun_o01_status", "completed")
    $ award_once("seoyun_O01", "seoyun", 2)
    return

label seoyun_o02_offer:
    if not dating or active_route != "seoyun" or memory.get("seoyun_o02_status"):
        return
    menu:
        "잠깐 더 이야기하기 — 서로 실패한 농담 (선택 일상)":
            call seoyun_o02
        "본편 계속 — 일요일 산책 약속으로":
            $ remember("seoyun_o02_status", "skipped")
        "오늘 고른 문장도 다음에 다시 읽어 달라고 하고 본편 계속":
            d "다음 판도 읽어 주세요. 그때 감상은 지금하고 달라도 되고요."
            s "좋아. 다음 감상까지 미리 복사해 놓지는 않을게."
            $ remember("seoyun_o02_status", "brief")
    return

label seoyun_o02:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 O02 · 서로 실패한 농담"
    $ location = "같은 토요일 늦은 오후 · 북카페"
    s "이쯤이면 단골 포인트로 나도 한 번 무료 초대 가능한가?"
    "도현이 무슨 대답을 해야 할지 고르는 사이 서윤도 웃음을 조금 거뒀다."
    menu:
        "다음 데이트를 계산하라는 말로 들려 잠깐 헷갈렸다고 한다.":
            d "다음에 제가 전부 계산해야 하나 했어요. 초대하고 싶긴 한데, 포인트 결제는 좀 어렵네요~"
            s "아, 그 말은 아니었어. 네가 골라 부르는 데 또 가고 싶다는 뜻이었어."
            $ remember("seoyun_o02_boundary", "돈 계산과 초대를 농담 하나로 묶지 않기")
        "뜻을 한 번 더 말해 달라고 가볍게 묻는다.":
            d "손님이 메뉴 설명을 놓쳤는데요. 이번만 한 번 더 말해 주세요."
            s "네가 골라서 불러 주면 좋겠다고. ...이렇게 말하니 계산대 필요 없네."
            $ remember("seoyun_o02_boundary", "못 알아들은 농담은 뜻을 다시 묻고 말하기")
        "나도 받아치려다 실패했다며 먼저 직접 초대한다.":
            d "저도 재치 있게 답하려다가 다음 말이 안 나오네요. 다음엔 제가 고른 데 같이 가요."
            s "좋아. 우리 둘 다 실패하고 약속 하나는 얻었네~ 날짜는 다음 일정 보고 같이 고르자."
            $ remember("seoyun_o02_boundary", "장난이 막히면 원하는 말을 직접 꺼내기")
    "둘은 뜻을 다시 알고 나서 함께 웃었다. 구체적인 날짜는 다음 일정을 보고 같이 정하기로 했다."
    $ remember("seoyun_o02_status", "completed")
    $ award_once("seoyun_O02", "seoyun", 2)
    return

label seoyun_o03_offer:
    if not dating or active_route != "seoyun" or memory.get("seoyun_o03_status"):
        return
    menu:
        "잠깐 만나기 — 우리도 단골인가 (선택 일상)":
            call seoyun_o03
        "본편 계속 — 일요일 저녁 북카페로":
            $ remember("seoyun_o03_status", "skipped")
        "저녁에는 전에 쓴 문장도 가져가겠다고 하고 본편 계속":
            d "저녁엔 초안도 가져갈게요. 제가 남긴 문장부터 보여 드리고 싶어요."
            s "응. 내가 대신 쓴 말 아니니까 더 궁금하지."
            $ remember("seoyun_o03_status", "brief")
    return

label seoyun_o03:
    if not dating or active_route != "seoyun":
        return
    $ chapter = "서윤 O03 · 우리도 단골인가"
    $ location = "일요일 늦은 오후 · 다시 찾은 북카페"
    "각자 오전을 보낸 뒤 저녁 약속보다 조금 먼저 만났다. 도현은 지난번과 다른 자리의 작은 조명을 봤다."
    s "항상 같은 자리여야 단골인가 했는데. 오늘은 어디 앉아 볼래?"
    menu:
        "바뀐 조명이 가까운 자리에 앉아 전과 다른 점을 본다.":
            "탁자에 빛이 떨어지는 위치를 보며 둘은 조명을 옮기기 전의 자리를 떠올렸다."
            d "자리가 바뀌니까 같은 문장도 다른 데서 읽네요."
            $ remember("seoyun_o03_detail", "옮겨진 작은 조명 아래 새 자리")
        "처음 함께 봤던 책이 꽂힌 선반 가까이 앉는다.":
            "『느린 모퉁이』는 같은 선반에 있었다. 둘은 새로 읽겠다고 꺼내지 않고 오늘 가져온 노트를 놓았다."
            s "책이 있는 건 같은데, 오늘은 네 문장 기다리네."
            $ remember("seoyun_o03_detail", "같은 책 선반 앞에서 오늘의 노트를 놓은 자리")
        "익숙한 자리 대신 처음 앉는 창가를 같이 고른다.":
            "둘은 처음 앉는 창가를 골랐다. 밖을 지나는 사람 대신 유리에 비친 작은 식물 그림자를 함께 봤다."
            d "아는 곳이 많아져도 아직 처음 보는 자리가 있네요."
            $ remember("seoyun_o03_detail", "처음 고른 창가의 식물 그림자")
    $ remember("seoyun_o03_status", "completed")
    $ award_once("seoyun_O03", "seoyun", 2)
    return

```
