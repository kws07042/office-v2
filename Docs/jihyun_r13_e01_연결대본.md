> 현행 갱신: 기획 v3.05 / Windows 0.32.0-dialogue-clarity — 2026-10-21
> 뜻을 짐작해야 하는 농담·혼합 비유·대답의 연결·화자와 소품 불일치를 정리했다. 대사이해도_전체검수_보고서_v1.md와 현행 실행 대본을 우선한다. 사건·선택 기억·인물 설정·자산 계획은 유지한다. 아래 이전 갱신은 이력이다.

# 지현 구현 대본 — jihyun_r13_e01.rpy

```renpy
label jihyun_r13:
    if not dating or active_route != "jihyun":
        return
    $ chapter = "지현 R13 · 널 위해 철회했어"
    $ location = "다음 월요일 오전 · 협업 회의실"
    "발표 순서표에서 도현의 현장 운영 제안이 빠져 있었다. 대신 지현이 정리한 축소안이 올라가 있었다."
    d "제 안은 검토 뒤에 결정하기로 했잖아요. 순서표에서 빠진 이유부터 듣고 싶어요."
    j "외부 보고 때 비용 질문이 많았어. 네가 그 부담까지 질 필요는 없다고 봤어. 내가 대체안으로 정리했고."
    d "저한테는 한 번도 안 물으셨어요. 제가 어느 위험까지 확인했는지도요."
    "지현이 답하려다 순서표를 다시 보았다. 수정자는 자기 이름이었다."
    j "금요일에도 먼저 물어봐 달라고 했지. ...내가 그 말을 듣고도 오늘 먼저 정했네."
    $ remember("jihyun_conflict", "open")
    $ remember("jihyun_unilateral_change", "도현의 근거를 듣기 전 발표 안건에서 제외하고 축소안으로 교체")
    menu:
        "어떤 위험을 확인했는지 내 근거부터 설명한다.":
            d "설치 시간은 확인했고, 인원 한 명이 더 필요한 조건도 적었어요. 이 조건을 보고 반대하셨으면 그 의견을 듣고 싶었어요."
            j "네 자료에 있는 조건도 확인하기 전에 발표 기회부터 없앴어. 지금 자료부터 같이 보자."
            $ remember("jihyun_r13_response", "reasons")
        "내가 설명할 책임과 지현이 검토할 책임을 나누자고 한다.":
            d "제안한 이유와 감당할 범위는 제가 설명할게요. 검토 결과는 팀장님이 다른 의견으로 말씀해 주세요. 제 설명까지 없애진 말아 주세요."
            j "응. 반대할 수 있는 것과 네 차례를 없애는 건 달랐어."
            $ remember("jihyun_r13_response", "roles")
        "서운해서 지금은 말이 어렵다고 하고 오후 네 시 재논의를 잡는다.":
            d "지금은 제가 많이 서운해요. 바로 괜찮다고 못 하겠어요. 오후 네 시에 근거 들고 다시 이야기하고 싶어요."
            j "알겠어. 그 전까지 내 축소안도 확정으로 돌리지 않을게. 네 시에 기다릴게."
            "오후 네 시에 다시 만났다. 도현은 빠진 발표 순서와 확인한 조건을 나란히 놓았다."
            $ remember("jihyun_r13_response", "pause_then_return")
    j "미안해. 보호한다고 생각하고 네 선택까지 가져왔어. 말만 고치고 같은 순서표로 들어가면 안 되겠지."
    d "네. 사과는 들었어요. 발표에서 어떻게 바꿀지도 보고 싶어요."
    "발표 운영 담당자에게 도현의 안을 다시 검토 안건으로 넣어 달라고 함께 요청했다. 수요일에 비교 검토할 시간을 받았다."
    $ remember("jihyun_agenda_restored", "수요일 비교 검토 안건으로 복구, 제안 채택 여부는 미정")
    $ remember("jihyun_conflict", "agreed_pending_action")
    $ award_once("jihyun_R13", "jihyun", 0)
    return

label jihyun_r14:
    if not dating or active_route != "jihyun" or memory.get("jihyun_conflict") != "agreed_pending_action":
        return
    $ chapter = "지현 R14 · 네가 설명해, 나는 옆에"
    $ location = "수요일 오전 · 비교 검토 직전"
    menu:
        "내 설명 뒤 지현이 비용·위험을 검토하도록 역할을 확인한다.":
            d "제안 이유와 시험 범위는 제가 먼저요. 그다음 비용 검토 부탁드릴게요."
            j "응. 내 반대 의견도 네 설명을 들은 뒤에 말할게."
            $ remember("jihyun_r14_choice", "ready")
        "서툴게 ‘이젠 전부 제가 할게요’라고 말하고, 반응을 본 뒤 다시 나눈다.":
            d "이번엔 그냥 전부 제가 할게요. 그러면 대신 정하실 일도 없겠죠."
            j "그 말이 나올 만큼 서운했던 건 알아. 그래도 검토 책임까지 네가 가져갈 필요는 없어. 내가 맡을 걸 다시 정하고 싶어."
            d "...제가 설명할 차례를 지키려다 도움까지 다 밀어냈네요. 제안 설명은 저, 비용 검토는 팀장님으로 나눠요."
            j "응. 그 범위 지킬게. 오늘 끝나고도 이야기하자."
            $ remember("jihyun_r14_choice", "repair_after_blunt")
        "연애를 마치고 동료로 지내고 싶다고 말한다 — 관계 종료 확인.":
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
    "도현이 현장 사진과 설치 시간표를 먼저 보여 주었다. 인원을 늘려 전면 시행하는 대신 한 장소에서 시험하는 안이었다."
    d "이 조건이면 시험할 수 있다고 봤어요. 아직 확인하지 못한 건 두 번째 주말의 유입량이에요."
    "질문이 끝날 때까지 지현은 도현 대신 대답하지 않았다. 도현의 설명 뒤 자기 검토 자료를 띄웠다."
    j "비용 때문에 전면 시행에는 반대합니다. 다만 지금 설명한 한 장소의 시험은 한도 안에 들어옵니다. 검토 창구와 중단 조건은 제가 정리하겠습니다."
    "운영 담당자가 한 장소의 시험 진행에 동의했다. 도현은 현장 확인, 지현은 비용 한도와 중단 조건 확인을 맡았다."
    $ remember("jihyun_r14_performed", "도현이 제안·한계를 직접 설명, 지현이 비용·중단 조건을 별도로 검토")
    $ remember("jihyun_conflict", "resolved")
    $ remember("jihyun_pilot_result", "한 장소 시험 승인, 전면 시행 결정은 보류")
    $ award_once("jihyun_R14", "jihyun", 8)
    if not dating:
        $ ending = "jihyun_relationship_closed"
        "검토를 마친 뒤 두 사람은 동료로 인사를 나눴다. 연인으로 이어지는 다음 약속은 잡지 않았다."
        return
    $ location = "같은 수요일 퇴근 후 · 회사 앞 벤치"
    j "오늘 네가 설명할 때 끼어들고 싶었던 순간이 있었어. 기다려 보니 내가 못 본 조건도 들리더라."
    d "제 안이 그대로 통과한 것보다, 제가 설명하고 다른 의견도 들을 수 있던 게 좋았어요."
    if memory.get("jihyun_r14_choice") == "wait_for_action":
        d "저는 계속 만나고 싶어요. 오늘처럼 같이 바꿀 수 있다면요. 미뤄 둔 대답은 지금 할게요."
        j "응. 나도 계속 만나고 싶어. 같은 일로 혼자 결론 내리지 않게 행동할게."
        $ remember("jihyun_continuation_reconfirmed")
    elif memory.get("jihyun_r14_choice") == "repair_after_blunt":
        d "아침엔 저도 날카롭게 말했어요. 서운한 건 말하되, 다음에 필요한 도움도 말해 볼게요."
        j "들어 줄게. 오늘 차례 돌려준 걸로 다 괜찮아졌다고 혼자 정하지도 않을게."
    else:
        j "아직 서운한 것도 말해 줘. 오늘 끝냈다고 감정까지 내가 마감할 일은 아니니까."
        d "조금 남아 있어요. 그래도 토요일에는 만나고 싶어요. 일 말고 같이 저녁 먹어요."
    $ remember("jihyun_r15_appointment", "토요일 저녁 사적인 만남")
    return

label jihyun_r15:
    if not dating or active_route != "jihyun" or memory.get("jihyun_conflict") != "resolved":
        return
    $ chapter = "지현 R15 · 같은 편의 다른 의견"
    $ location = "토요일 저녁 · 지현의 집"
    "저녁을 먹고 다음 달 일정표를 펼쳤다. 지현이 빈 토요일 한 칸을 가리켰다."
    j "여긴 같이 걷고 싶은 날. 아직 내 제안이야. 네 것도 듣고 싶어."
    menu:
        "같이 산책하되, 오전의 혼자 쓸 시간도 남기자고 한다.":
            d "오전에는 기록집 정리하고 싶어요. 오후 네 시부터 걸을까요?"
            j "응. 네 시부터. 하루 전체가 내 약속인 것처럼 잡지 않을게."
            $ remember("jihyun_future_promise", "토요일 오전 각자 시간, 오후 네 시 산책")
        "힘든 날엔 혼자 견디기 전에 서로 부탁부터 해 보자고 한다.":
            d "바쁜 날에는 저도 먼저 부탁해 볼게요. 뭘 해 줄지 혼자 맞히게 두지 않고요."
            j "나도. ‘괜찮아’부터 대답하지 않고, 같이 있어 달라고도 해 볼게."
            $ remember("jihyun_future_promise", "힘든 날 원하는 도움과 가능한 범위를 먼저 말하기")
        "다른 의견이어도, 연인으로 좋아한다는 말은 따로 전하자고 한다.":
            d "같은 생각을 해야만 좋아하는 건 아니잖아요. 반대할 때도 보고 싶다는 말은 따로 할래요."
            j "좋아. 오늘 내 제안하고 달라도, 네가 와 준 건 계속 기뻐할 수 있겠네."
            $ remember("jihyun_future_promise", "의견 차이와 애정 표현을 따로 말하기")
    j "오늘은 어떤 옷이 편할까? 생활복도 있고, 전에 취미 행사에서 입으려고 사 둔 탐정 재킷도 있어. 그건 한번 보여 주고 싶었어."
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
            d "그럼요. 오늘 안 본 걸 다음 약속으로 강제로 잡지는 말고요~"
            $ remember("jihyun_r15_outfit", "home")
    "지현이 고른 옷으로 갈아입고 돌아왔다. 둘은 나란히 앉아 조금 전 일정표를 덮었다."
    j "이제 일정 말고 부탁. 오늘은 같이 밤을 보내고 싶어. 너도 괜찮으면."
    call jihyun_private_evening("r15", memory["jihyun_r15_outfit"])
    $ award_once("jihyun_R15", "jihyun", 5)
    return

label jihyun_r16:
    if not dating or active_route != "jihyun" or memory.get("jihyun_conflict") != "resolved" or "jihyun_R15" not in completed:
        return
    $ chapter = "지현 R16 · 책임을 나누는 사람"
    $ location = "일요일 저녁 · 동네 카페"
    "지현은 월요일에 공유할 시험 진행표를 가방에 넣었다. 운영 담당의 현장 판단, 도현의 확인, 자신의 비용 검토가 각각 표시돼 있었다."
    j "내 승인 하나로 다 모으지 않으려고 정리했어. 내일 담당자들이 확인하고, 실제 시험은 그 뒤야."
    d "제 확인 범위도 봤어요. 모르는 게 나오면 먼저 물어볼게요."
    "도현도 기록집의 새 초안을 꺼냈다. 함께 골라 본 내용을 실제 페이지 한 자리에 남겼다."
    d "[memory['jihyun_private_name']], [memory['jihyun_booklet_subject']]은 이번 초안에 남겼어요. 해 주신 감상도 옆에 메모했고요."
    j "내 말은 메모고 네 책이야. 다음에 고쳐도, 이 판을 본 건 기쁠 것 같아."
    $ remember("jihyun_booklet_state", "직접 고른 내용이 들어간 새 초안, 인쇄 완성은 아직")
    menu:
        "앞으로도 혼자 쉴 시간과 함께 있는 시간을 같이 고르자고 한다.":
            d "계속 같이 고르고 싶어요. 비워 둔 칸도 서로의 것으로 남기고요."
            j "응. 같이 있는 시간은 부탁하고, 혼자 있는 시간은 빼앗지 않을게."
            $ remember("jihyun_ending_promise", "own_time")
        "내가 힘들 때도 먼저 기대고 싶다고 말한다.":
            d "저도 다음엔 힘들다고 더 일찍 말할게요. 오늘은 조금 더 같이 걸어 주실래요?"
            j "응. 오늘 그 부탁부터 듣고 싶었어. 먼저 집에 가야 한다고 짐작하던 참이었거든."
            $ remember("jihyun_ending_promise", "ask_help")
        "서로의 다음 초안을 처음 보는 사람으로 계속 만나자고 한다.":
            d "다음에 만든 것도 보고 싶어요. 그때도 다 아는 사람처럼 말하지 않고 볼게요."
            j "나도 네 다음 페이지가 궁금해. ...책 안 가져오는 날도 물론 보고 싶고."
            $ remember("jihyun_ending_promise", "next_draft")
    "카페를 나와 잠깐 나란히 섰다. 지현이 먼저 손을 내밀다가 도현의 눈을 보았다."
    if memory.get("jihyun_affection_scope") == "private_place":
        j "조용한 길로 돌아갈까? 그쪽에서 손잡고 싶어."
        d "네. 거기서 제가 먼저 잡을게요."
    else:
        j "손잡고 걸어도 돼? 오늘도 먼저 묻고 싶어서."
        d "네. 저도 지금 그러고 싶어요."
    "손을 잡고 집으로 가는 길을 조금 돌아 걸었다. 다음에 바뀔 일정은 다음에 같이 이야기하기로 했다."
    $ remember("jihyun_route_completed")
    $ persistent.local_jihyun_ending = True
    $ ending = "jihyun_good"
    $ award_once("jihyun_R16", "jihyun", 4)
    "지현 본편 결말 · 책임을 나누는 사람"
    return

label jihyun_e01:
    if not dating or active_route != "jihyun" or not memory.get("jihyun_route_completed"):
        return
    $ chapter = "지현 E01 · 쉬는 날의 부탁"
    $ location = "약 반년 뒤, 쉬는 날 오후 · 지현의 집"
    "작은 조립집의 지붕은 붙어 있었다. 그 옆에는 도현이 직접 사진과 글을 정리해 인쇄한 동네 기록집이 놓였다."
    j "그때 시험은 담당자들이 나눠서 마쳤어. 이번엔 내 휴가에도 내 확인을 기다리는 일이 줄었고."
    d "저도 기록집 다 만들었어요. [memory['jihyun_booklet_subject']], 인쇄본에도 남겼어요."
    $ remember("jihyun_pilot_result", "이후 담당별 확인으로 시험 완료, 휴가 중 상시 승인 대기 감소")
    $ remember("jihyun_booklet_state", "이후 직접 촬영·글 정리를 마친 인쇄 기록집 완성")
    if memory.get("jihyun_game_mode") == "competitive":
        j "오늘 한 판 할까? 한 점 차이였던 건 아직 기억하지?"
    elif memory.get("jihyun_game_mode") == "cooperative":
        j "오늘도 같은 편 해 줘. 마지막 차례 기다리던 거 재밌었어."
    else:
        j "오늘도 점수 없이 골라 볼까? 잼은 이번에도 내가 챙겼어."
    if memory.get("jihyun_o01_status") == "completed":
        j "비 와서 바꿨던 그날도 좋았지. 같이 쓸 시간은 꼭 계획대로가 아니어도 남더라."
    if memory.get("jihyun_o02_status") == "completed":
        j "그날은 지붕 안 붙이고 같이 들여다본 게 좋았어. 이렇게 닫은 것도 오늘 같이 보고."
    if memory.get("jihyun_o03_status") == "completed":
        d "지난번 서로 부탁해 본 뒤로, 저도 말이 조금 빨라진 것 같아요."
    j "오늘은 게임 전에 부탁 말고 제안 하나. 같이 사는 걸 이야기해 보고 싶어. 지금 답 정해 달라는 뜻은 아니고."
    menu:
        "함께 사는 날에도 각자 혼자 있을 공간부터 이야기한다.":
            d "저도 생각해 보고 싶어요. 각자 혼자 쓸 책상하고 조용히 쉬는 자리부터요."
            j "응. 같은 집이면 모든 시간을 같이 써야 하는 건 아니니까."
            $ remember("jihyun_cohabitation_topic", "각자의 책상과 혼자 쉬는 공간")
        "생활 시간과 집안일 분담을 먼저 맞춰 보자고 한다.":
            d "퇴근 시간 다른 날 저녁하고, 청소 같은 것부터요. 당연히 제가 하겠지 하고 넘기지 않게요."
            j "좋아. 잘하는 사람이 계속 맡는 방식 말고, 할 수 있는 날도 같이 적자."
            $ remember("jihyun_cohabitation_topic", "퇴근·휴식 시간과 집안일 분담")
        "같이 살 마음은 있지만 집을 정하기 전 따로 생각할 시간을 갖자고 한다.":
            d "같이 살고 싶은 마음은 있어요. 조건은 각자 생각해 오고 다음 주에 더 이야기해요."
            j "응. 오늘 말 꺼낸 걸로 집까지 고르지는 않을게. 다음 주에도 여기서 얘기하자."
            $ remember("jihyun_cohabitation_topic", "각자 조건을 생각한 뒤 다음 주 재논의")
    j "...오늘은 네가 조금 더 있다 갔으면 좋겠어. 이건 오늘 부탁."
    d "좋아요. 대신 차는 제가 타도 돼요? 마시고 싶은 걸 저도 하나 골라 왔어요."
    j "응. 오늘은 나도 네가 고른 걸로."
    $ remember("jihyun_cohabitation_status", "동거 논의 시작, 계약·입주·동거 완료 아님")
    $ remember("jihyun_epilogue_completed")
    $ award_once("jihyun_E01", "jihyun", 8)
    return

```
