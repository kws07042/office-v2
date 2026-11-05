label jihyun_r13:
    $ progression_enter("jihyun_r13")
    $ progression_checkpoint("jihyun_r13")
    if not dating or active_route != "jihyun":
        $ progression_note_ending()
        return
    $ chapter = "지현 R13 · 널 위해 철회했어"
    $ location = "다음 월요일 오전 · 협업 회의실"
    "발표 순서표에서 도현의 현장 운영 제안이 빠져 있었다. 대신 지현이 정리한 축소안이 올라가 있었다."
    d "제 안은 검토 뒤에 결정하기로 했잖아요. 순서표에서 빠진 이유부터 듣고 싶어요."
    j "외부 보고 때 비용 질문이 많았어. 네가 그 부담까지 질 필요는 없다고 봤어. 내가 대체안으로 정리했고."
    d "저한테는 한 번도 안 물으셨어요. 제가 어느 위험까지 확인했는지도요."
    "지현이 답하려다 순서표를 다시 보았다. 수정자는 자기 이름이었다."
    j "비용 질문까지 네가 받으면..."
    "지현이 말을 멈췄다. 도현은 가져온 자료를 펼치지 않았다."
    j "...금요일에도 먼저 물어봐 달라고 했지. 응. 들었어."
    $ remember("jihyun_conflict", "open")
    $ remember("jihyun_unilateral_change", "도현의 근거를 듣기 전 발표 안건에서 제외하고 축소안으로 교체")
    $ progression_enter("jihyun_r13.choice01")
    $ progression_checkpoint("jihyun_r13.choice01")
    menu:
        "어떤 위험을 확인했는지 내 근거부터 설명한다.":
            d "설치 시간은 확인했고, 인원 한 명이 더 필요한 조건도 적었어요. 이 조건을 보고 반대하셨으면 그 의견을 듣고 싶었어요."
            j "그 조건, 어느 장이야?"
            "도현이 표시한 장을 펼쳤다. 지현은 자기 축소안 밑에 놓으려던 손을 거두고 두 자료를 나란히 뒀다."
            j "여기부터 볼게. 설명해 줘."
            $ remember("jihyun_r13_response", "reasons")
        "내가 설명할 책임과 지현이 검토할 책임을 나누자고 한다.":
            d "제 안이 틀렸으면 듣고 고칠게요. 그런데 말해 볼 차례도 없이 빠지는 건 싫어요."
            j "반대 의견은 그대로야. ...그렇다고 네 설명을 빼면 안 됐어."
            d "네. 반대하시는 이유도 듣고 싶어요. 제 얘기한 다음에요."
            $ remember("jihyun_r13_response", "roles")
        "서운해서 지금은 말이 어렵다고 하고 오후 네 시 재논의를 잡는다.":
            d "지금은 제가 많이 서운해요. 바로 괜찮다고 못 하겠어요. 오후 네 시에 근거 들고 다시 이야기하고 싶어요."
            j "알겠어. 그 전까지 내 축소안도 확정으로 돌리지 않을게. 네 시에 기다릴게."
            "오후 네 시에 다시 만났다. 도현은 빠진 발표 순서와 확인한 조건을 나란히 놓았다."
            $ remember("jihyun_r13_response", "pause_then_return")
    "지현이 순서표에서 제 축소안 옆을 짚었다. 도현의 안이 있던 빈칸으로 손가락이 옮겨 갔다."
    j "미안해. 네 안을 빼기 전에 물었어야 했어. 검토 순서부터 되돌릴게."
    d "네. 제 안이 통과할지는 몰라도, 설명은 제가 하고 싶어요."
    "발표 운영 담당자에게 도현의 안을 다시 검토 안건으로 넣어 달라고 함께 요청했다. 수요일에 비교 검토할 시간을 받았다."
    $ remember("jihyun_agenda_restored", "수요일 비교 검토 안건으로 복구, 제안 채택 여부는 미정")
    $ remember("jihyun_conflict", "agreed_pending_action")
    $ award_once("jihyun_R13", "jihyun", 0)
    $ progression_note_ending()
    return

label jihyun_r14:
    $ progression_enter("jihyun_r14")
    $ progression_checkpoint("jihyun_r14")
    if not dating or active_route != "jihyun" or memory.get("jihyun_conflict") != "agreed_pending_action":
        $ progression_note_ending()
        return
    $ chapter = "지현 R14 · 네가 설명해, 나는 옆에"
    $ location = "수요일 오전 · 비교 검토 직전"
    $ progression_enter("jihyun_r14.choice01")
    $ progression_checkpoint("jihyun_r14.choice01")
    menu:
        "내 설명 뒤 지현이 비용·위험을 검토하도록 역할을 확인한다.":
            d "제안 이유와 시험 범위는 제가 먼저요. 그다음 비용 검토 부탁드릴게요."
            j "응. 내 반대 의견도 네 설명을 들은 뒤에 말할게."
            $ remember("jihyun_r14_choice", "ready")
        "서툴게 ‘이젠 전부 제가 할게요’라고 말하고, 반응을 본 뒤 다시 나눈다.":
            d "이번엔 그냥 전부 제가 할게요. 그러면 대신 정하실 일도 없겠죠."
            j "그 말이 나올 만큼 서운했던 건 알아. 그래도 검토 책임까지 네가 가져갈 필요는 없어. 내가 맡을 걸 다시 정하고 싶어."
            d "...그건 저도 무리네요. 제가 먼저 설명할게요. 비용 쪽은 여전히 봐주셨으면 해요."
            j "알겠어. 네 설명 먼저 듣고 내가 비용 얘기할게. 끝나고 잠깐 봐."
            $ remember("jihyun_r14_choice", "repair_after_blunt")
        "연애를 마치고 동료로 지내고 싶다고 말한다 — 관계 종료 확인.":
            $ progression_enter("jihyun_r14.choice02")
            $ progression_checkpoint("jihyun_r14.choice02")
            menu:
                "관계 종료를 확정한다. 업무 검토는 예정대로 진행한다.":
                    d "일은 예정대로 함께할게요. 다만 연인으로는 더 만나지 않겠어요."
                    j "알겠어. 오늘 검토에서 네 차례를 되돌리는 건 그 대답과 상관없이 해야 할 일이야."
                    $ dating = False
                    $ remember("jihyun_relationship_closed")
                "결정을 취소하고 역할을 다시 확인한다.":
                    d "끝내겠다는 결정은 취소할게요. 오늘은 제가 먼저 설명하는 걸 지켜봐 주세요."
                    j "응. 그다음 내 검토를 말할게."
                    $ remember("jihyun_r14_choice", "reconsidered")
                "종료 결정은 보류하고, 오늘 행동을 본 뒤 마음을 이야기한다.":
                    d "지금 바로 결정하지 않을래요. 발표 끝나고 다시 이야기해요."
                    j "응. 답을 재촉하진 않을게. 오늘 맡은 것부터 지킬게."
                    $ remember("jihyun_r14_choice", "wait_for_action")
    "첫 질문은 ‘전부 바꾸자는 겁니까?’였다. 도현은 현장 사진에서 한 장소만 짚었다."
    d "여기만 먼저 해 보자는 안입니다. 설치 시간은 확인했고요. 다음 주말에 사람이 더 몰려도 되는지는 아직 몰라요."
    "지현이 펜을 들었다가 내려놓았다. 도현이 질문에 끝까지 답한 뒤에야 자기 자료를 펼쳤다."
    j "전부 바꾸는 비용은 여전히 어렵습니다. 이 한 곳은 가능합니다. 한도를 넘으면 멈추는 조건은 제가 붙이겠습니다."
    "한 장소의 시험이 승인됐다. 도현은 현장, 지현은 비용과 중단 조건을 맡았다."
    $ remember("jihyun_r14_performed", "도현이 제안·한계를 직접 설명, 지현이 비용·중단 조건을 별도로 검토")
    $ remember("jihyun_conflict", "resolved")
    $ remember("jihyun_pilot_result", "한 장소 시험 승인, 전면 시행 결정은 보류")
    $ award_once("jihyun_R14", "jihyun", 8)
    if not dating:
        $ ending = "jihyun_relationship_closed"
        "검토를 마친 뒤 두 사람은 동료로 인사를 나눴다. 연인으로 이어지는 다음 약속은 잡지 않았다."
        $ progression_note_ending()
        return
    $ location = "같은 수요일 퇴근 후 · 회사 앞 벤치"
    "지현이 벤치 한쪽에 자료를 내려놓았다. 도현도 가방을 발치에 뒀다."
    j "아까 두 번째 질문 때, 내가 먼저 답할 뻔했어."
    d "저는 그때 팀장님 쪽 볼까 하다가 말았어요."
    j "응. 네가 설명하니까 내가 보던 조건하고 조금 다르더라. ...기다리길 잘했어."
    d "반대 의견은 여전히 매웠고요."
    j "그건 봐주면 안 되잖아."
    d "네. 제 설명 듣고 반대하신 건 괜찮아요."
    if memory.get("jihyun_r14_choice") == "wait_for_action":
        d "저는 계속 만나고 싶어요. 오늘처럼 같이 바꿀 수 있다면요. 미뤄 둔 대답은 지금 할게요."
        j "응. 나도 계속 만나고 싶어. 같은 일로 혼자 결론 내리지 않게 행동할게."
        $ remember("jihyun_continuation_reconfirmed")
    elif memory.get("jihyun_r14_choice") == "repair_after_blunt":
        d "아침엔 저도 날카롭게 말했어요. 서운한 건 말하되, 다음에 필요한 도움도 말해 볼게요."
        j "들어 줄게. 오늘 차례 돌려준 걸로 다 괜찮아졌다고 혼자 정하지도 않을게."
    else:
        j "오늘 일 끝났으니까 괜찮냐고 물으려다가 말았어. ...아직 화나?"
        d "조금 남아 있어요. 그래도 토요일에는 만나고 싶어요. 일 말고 같이 저녁 먹어요."
    j "토요일 저녁은 나도 좋아. 자료는 놓고 와."
    d "이번엔 제가 먼저 알아서 해도 되는 거네요."
    "지현이 바로 답하지 않았다. 도현이 빈손을 펴 보이자 그제야 짧게 웃었다."
    j "응. 그건 네가 골라. 같이 먹고 싶은 건 물어봐도 되고."
    $ remember("jihyun_r15_appointment", "토요일 저녁 사적인 만남")
    $ progression_note_ending()
    return

label jihyun_r15:
    $ progression_enter("jihyun_r15")
    $ progression_checkpoint("jihyun_r15")
    if not dating or active_route != "jihyun" or memory.get("jihyun_conflict") != "resolved":
        $ progression_note_ending()
        return
    $ chapter = "지현 R15 · 같은 편의 다른 의견"
    $ location = "토요일 저녁 · 지현의 집"
    "저녁을 마친 뒤 지현이 접시를 거두려다 도현이 내민 손을 봤다. 접시를 내려놓고 그 손을 마주 잡았다."
    d "[memory.get('jihyun_private_name', '지현 씨')], 저녁 다 먹었는데도 그냥 옆에 있고 싶네요."
    j "나도. 치울 건 조금 뒤에 치우자."
    "지현은 맞은편으로 돌아와 앉으면서도 도현의 손을 천천히 놓았다. 휴대폰의 빈 토요일 칸을 보여 줬다."
    j "이날은 같이 걷고 싶어. 길은 아직 안 골랐고."
    d "안 고르셨어요, 안 보여 주시는 거예요?"
    j "안 골랐어. ...후보가 조금 있을 뿐이지."
    $ progression_enter("jihyun_r15.choice01")
    $ progression_checkpoint("jihyun_r15.choice01")
    menu:
        "같이 산책하되, 오전의 혼자 쓸 시간도 남기자고 한다.":
            d "오전엔 각자 쉬고, 오후 네 시부터 걸을까요?"
            j "네 시. 나는 늦게 일어나 볼게. 알람도 안 맞추고."
            $ remember("jihyun_future_promise", "토요일 오전 각자 시간, 오후 네 시 산책")
        "힘든 날엔 혼자 견디기 전에 서로 부탁부터 해 보자고 한다.":
            d "바쁜 날엔 저도 먼저 부탁할게요. 오늘은 조금 더 앉아 계셔 주세요. 아직 혼자 가긴 싫어서."
            "지현이 식탁의 마지막 컵에서 손을 뗐다."
            j "응. 이건 나도 좋아. 설거지는 조금 늦게 하지 뭐."
            $ remember("jihyun_future_promise", "힘든 날 원하는 도움과 가능한 범위를 먼저 말하기")
        "다른 의견이어도, 연인으로 좋아한다는 말은 따로 전하자고 한다.":
            d "그 길 말고 다른 데 고를 수도 있어요. 그래도 [memory.get('jihyun_private_name', '지현 씨')] 보러 온 건 같은 거고요."
            j "그럼 다른 길도 가져와. 내 후보가 이기면 좋은 거고."
            d "지면요?"
            j "...같이 걷는 건 안 취소해."
            $ remember("jihyun_future_promise", "의견 차이와 애정 표현을 따로 말하기")
    j "오늘은 어떤 옷이 편할까? 생활복도 있고, 전에 취미 행사에서 입으려고 사 둔 탐정 재킷도 있어. 그건 한번 보여 주고 싶었어."
    $ progression_enter("jihyun_r15.choice02")
    $ progression_checkpoint("jihyun_r15.choice02")
    menu:
        "지현이 편한 생활복으로 쉬자고 한다.":
            d "오늘은 편하게요. 제가 옆자리 비워 둘게요."
            $ remember("jihyun_r15_outfit", "home")
        "보여 주고 싶었다는 탐정 의상을, 지현도 원하면 보고 싶다고 한다.":
            d "지금 입고 싶으시면 저도 보고 싶어요. 억지로 맞춰 주시는 건 말고요."
            j "나도 보여 주고 싶어서 꺼냈어. 추리 정답까지 준비한 건 아니고~"
            $ remember("jihyun_r15_outfit", "cosplay")
        "지현이 오늘 더 입고 싶은 쪽을 골라 달라고 한다.":
            j "그럼 오늘은 생활복. 재킷은 다음에 구경해도 되겠지."
            d "그럼요. 탐정님 등장하는 날엔 제가 용의자 표정부터 준비할게요~"
            $ remember("jihyun_r15_outfit", "home")
    "지현이 고른 옷으로 갈아입고 돌아왔다. 도현이 옆자리를 두드리자 이번에는 지현이 먼저 다가와 앉았다."
    j "이제 옷 얘기 말고 부탁. 오늘은 같이 밤을 보내고 싶어. 너도 괜찮으면."
    call jihyun_private_evening("r15", memory["jihyun_r15_outfit"])
    $ award_once("jihyun_R15", "jihyun", 5)
    $ progression_note_ending()
    return

label jihyun_r16:
    $ progression_enter("jihyun_r16")
    $ progression_checkpoint("jihyun_r16")
    if not dating or active_route != "jihyun" or memory.get("jihyun_conflict") != "resolved" or "jihyun_R15" not in completed:
        $ progression_note_ending()
        return
    $ chapter = "지현 R16 · 책임을 나누는 사람"
    $ location = "일요일 저녁 · 동네 카페"
    "지현이 담당별 확인란이 나뉜 시험 진행표를 가방에 넣었다. 월요일 공유 뒤 실제 시험을 시작할 자료였다."
    d "제 칸도 확인했어요. 오늘은 여기까지죠?"
    "지현은 가방 지퍼를 끝까지 닫고 고개를 끄덕였다."
    "도현은 [memory['jihyun_booklet_subject']]을 넣은 기록집 초안을 잠깐 보여 줬다. 지현은 종이 모서리를 맞추려다 손을 거뒀다."
    j "내용은 안 고칠게. 오늘은 남의 일정도 안 짤 거고."
    d "그럼 오늘은 뭘 하고 싶으세요?"
    j "...같이 나가고 싶어. 목적지는 아직 없어."
    d "제가 길을 고르면 따라오실래요?"
    j "오늘은 그럴래. 다만 내가 먼저 손잡을 수도 있어."
    $ remember("jihyun_booklet_state", "직접 고른 내용이 들어간 새 초안, 인쇄 완성은 아직")
    $ progression_enter("jihyun_r16.choice01")
    $ progression_checkpoint("jihyun_r16.choice01")
    menu:
        "앞으로도 혼자 쉴 시간과 함께 있는 시간을 같이 고르자고 한다.":
            d "같이 쉴 날은 고르고, 혼자 늦잠 잘 날도 남겨 둘래요."
            j "좋아. 그날은 점심 지나서 연락할게. 나는 일찍 깨도."
            d "일찍 깨서 뭐 하셨는지는 나중에 듣고요."
            j "응. 네가 깰 때까지 얘깃거리 모아 둘게."
            $ remember("jihyun_ending_promise", "own_time")
        "내가 힘들 때도 먼저 기대고 싶다고 말한다.":
            d "저도 다음엔 힘들다고 더 일찍 말할게요. 오늘은 조금 더 같이 걸어 주실래요?"
            j "응. 오늘 그 부탁부터 듣고 싶었어. 먼저 집에 가야 한다고 짐작하던 참이었거든."
            $ remember("jihyun_ending_promise", "ask_help")
        "서로의 다음 초안을 처음 보는 사람으로 계속 만나자고 한다.":
            d "다음에 만든 것도 보고 싶어요. 그때도 다 아는 사람처럼 말하지 않고 볼게요."
            j "나도 네 다음 게 궁금해. ...아무것도 안 가져오는 날도 만나자."
            $ remember("jihyun_ending_promise", "next_draft")
    "카페를 나와 잠깐 나란히 섰다. 지현이 먼저 손을 내밀다가 도현의 눈을 보았다."
    if memory.get("jihyun_affection_scope") == "private_place":
        j "조용한 길로 돌아갈까? 그쪽에서 손잡고 싶어."
        d "네. 거기서 제가 먼저 잡을게요."
    else:
        j "손잡고 걸어도 돼? 오늘도 먼저 묻고 싶어서."
        d "네. 저도 지금 그러고 싶어요."
    "집으로 가는 길에서 지현이 갈림길 앞에 멈췄다. 도현이 조금 긴 쪽을 가리키자 손을 놓지 않고 따라왔다."
    j "이쪽이면 좀 돌아가는데."
    d "알아요."
    "지현은 길 안내를 더 하지 않았다."
    $ remember("jihyun_route_completed")
    $ persistent.local_jihyun_ending = True
    $ ending = "jihyun_good"
    $ award_once("jihyun_R16", "jihyun", 4)
    "지현 본편 결말 · 책임을 나누는 사람"
    $ progression_note_ending()
    return

label jihyun_e01:
    $ progression_enter("jihyun_e01")
    $ progression_checkpoint("jihyun_e01")
    if not dating or active_route != "jihyun" or not memory.get("jihyun_route_completed"):
        $ progression_note_ending()
        return
    $ chapter = "지현 E01 · 쉬는 날의 부탁"
    $ location = "약 반년 뒤, 쉬는 날 오후 · 지현의 집"
    "지현의 조립집은 지붕까지 완성돼 있었다. 도현이 직접 사진과 글을 정리한 기록집도 한쪽에 놓였다."
    "담당자들이 시험을 마친 뒤로, 휴일마다 지현의 확인을 기다리는 연락은 줄었다. 오늘 휴대폰은 조립집 뒤에 놓여 있었다."
    "도현이 [memory['jihyun_booklet_subject']]이 실린 쪽을 펼쳐 보였다. 지현은 잠깐 보고 책을 덮었다."
    j "완성한 건 축하해. 오늘은 나랑 놀아 줄 거지?"
    d "저는 그 말 기다렸어요."
    $ remember("jihyun_pilot_result", "이후 담당별 확인으로 시험 완료, 휴가 중 상시 승인 대기 감소")
    $ remember("jihyun_booklet_state", "이후 직접 촬영·글 정리를 마친 인쇄 기록집 완성")
    if memory.get("jihyun_game_mode") == "competitive":
        j "오늘 한 판 할까? 한 점 차이였던 건 아직 기억하지?"
    elif memory.get("jihyun_game_mode") == "cooperative":
        j "오늘도 같은 편 해 줘. 마지막 차례 기다리던 거 재밌었어."
    else:
        j "오늘도 점수 없이 골라 볼까? 잼은 이번에도 내가 챙겼어."
    if memory.get("jihyun_o01_status") == "completed":
        j "비 오던 날엔 가려던 데 못 가고도 같이 있었지. 오늘도 다른 데 찾느라 먼저 일어나진 마."
    if memory.get("jihyun_o02_status") == "completed":
        j "그날은 지붕 안 붙이고 같이 들여다본 게 좋았어. 이렇게 닫은 것도 오늘 같이 보고."
    if memory.get("jihyun_o03_status") == "completed":
        d "저 오늘도 부탁 하나 있어요. 게임 시작 전에 제 옆에 좀 앉아 주세요."
        j "들었어. 아직 카드도 안 꺼냈는데 벌써 붙잡히네."
    "지현이 게임 카드를 펼치려다 조립집을 옮겼다. 둘이 나란히 앉을 자리를 만들고도 손을 떼지 못했다."
    j "우리, 같은 집에서 쉬는 날도 있을까? ...장식 얘기 말고. 같이 사는 거. 얘기해 보고 싶어."
    $ progression_enter("jihyun_e01.choice01")
    $ progression_checkpoint("jihyun_e01.choice01")
    menu:
        "함께 사는 날에도 각자 혼자 있을 공간부터 이야기한다.":
            d "저도 생각해 보고 싶어요. 각자 혼자 쓸 책상하고 조용히 쉬는 자리부터요."
            j "좋아. 각자 책상 하나씩. 그리고 소파는 둘이 앉아도 남는 걸로."
            d "거기는 제가 먼저 고를래요."
            j "응. 나도 바로 옆에 앉을게."
            $ remember("jihyun_cohabitation_topic", "각자의 책상과 혼자 쉬는 공간")
        "생활 시간과 집안일 분담을 먼저 맞춰 보자고 한다.":
            d "퇴근 시간 다른 날 저녁하고, 청소 같은 것부터요. 당연히 제가 하겠지 하고 넘기지 않게요."
            j "좋아. 내가 먼저 청소기 잡았다고 평생 내 담당 되는 건 아니지?"
            d "그럼요. 저도 설거지 한 번 잘해 보려고요."
            j "한 번?"
            d "...시작을 잘해 보겠다는 뜻이었습니다."
            $ remember("jihyun_cohabitation_topic", "퇴근·휴식 시간과 집안일 분담")
        "같이 살 마음은 있지만 집을 정하기 전 따로 생각할 시간을 갖자고 한다.":
            d "같이 살고 싶은 마음은 있어요. 조건은 각자 생각해 오고 다음 주에 더 이야기해요."
            j "응. 오늘 말 꺼낸 걸로 집까지 고르지는 않을게. 다음 주에도 여기서 얘기하자."
            $ remember("jihyun_cohabitation_topic", "각자 조건을 생각한 뒤 다음 주 재논의")
    "지현이 카드를 섞다가 한 장을 도현 앞에 뒤집어 놓았다."
    j "오늘은 네가 먼저 골라. ...게임 끝나도 바로 가지 마."
    if memory.get("jihyun_game_mode") == "competitive":
        d "그럼 제가 이길 때까지 한 판 더 하죠."
    elif memory.get("jihyun_game_mode") == "cooperative":
        d "이번엔 제가 차 맞출게요. 빵은 먼저 골라 주세요."
    else:
        d "그럼 내일 아침도 골라 봐요. 이번엔 제 잼도 제가 고를래요."
    "지현은 대답 대신 도현이 고른 카드를 뒤집었다. 이번에는 누구도 시계를 보지 않았다."
    $ remember("jihyun_cohabitation_status", "동거 논의 시작, 계약·입주·동거 완료 아님")
    $ remember("jihyun_epilogue_completed")
    $ award_once("jihyun_E01", "jihyun", 8)
    $ progression_note_ending()
    return
