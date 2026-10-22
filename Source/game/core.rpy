# Internal text prototype. All cast members are adults.
define d = Character("도현", callback=renpy.curry(cream_note_speaker)("dohyun"))
define r = Character("강리아", callback=renpy.curry(cream_note_speaker)("ria"))
define j = Character("백지현", callback=renpy.curry(cream_note_speaker)("jihyun"))
define jn = Character("백지현", what_prefix="『", what_suffix="』", callback=renpy.curry(cream_note_speaker)("jihyun"))
define y = Character("차유진", callback=renpy.curry(cream_note_speaker)("yujin"))
define s = Character("한서윤", callback=renpy.curry(cream_note_speaker)("seoyun"))
define dn = Character("도현", what_prefix="『", what_suffix="』", callback=renpy.curry(cream_note_speaker)("dohyun"))
define yn = Character("차유진", what_prefix="『", what_suffix="』", callback=renpy.curry(cream_note_speaker)("yujin"))

define rn = Character("강리아", what_prefix="『", what_suffix="』", callback=renpy.curry(cream_note_speaker)("ria"))
define msgd = Character("도현 · 보낸 메시지", callback=renpy.curry(cream_note_speaker)("message"))
define msgr = Character("리아 · 답장", callback=renpy.curry(cream_note_speaker)("message"))

default speech_informal = False
default first_approach = "observe"
default afterwork_preference = None
default active_route = None
default chapter = ""
default location = ""
default ending = ""
default memory = {}
default affinity = {"ria":0, "jihyun":0, "yujin":0, "seoyun":0}
default completed = []
default trust_ria = 0
default selected_person = None
default c06_person = None
default c06_topic = None
default c07_person = None
default c07_method = None
default downtime = None
default r02_plan = None
default r02_expression = None
default r03_reply = None
default prepared = False
default dating = False
default first_kiss = False
default kiss_proposed = False
default result_choice = None
default line_text = ""
default persistent.common_seen = False
default persistent.local_colleague_ending = False
default persistent.local_ria_ending = False

image bg plain = Solid("#151d30")

init python:
    def ri(informal, formal):
        return informal if speech_informal else formal

    def remember(key, value=True):
        renpy.store.memory = dict(renpy.store.memory, **{key:value})

    def award_once(event, who, amount, trust=0):
        if event in renpy.store.completed:
            return
        renpy.store.affinity = dict(renpy.store.affinity, **{
            who: min(100, renpy.store.affinity.get(who, 0) + amount)})
        renpy.store.completed = renpy.store.completed + [event]
        if who == "ria":
            renpy.store.trust_ria = min(3, max(0, renpy.store.trust_ria + trust))

label start:
    scene bg plain
    "대본 개발판 · 공통 C01~C08, 네 히로인의 개인 대본을 읽을 수 있습니다."
    "최종 배경·표정·이벤트 CG·영상·음성은 제작 중입니다. 실제 플레이 길이와 대사의 통합 편집도 남아 있습니다."
    call c01
    call c02
    call c03
    call c04
    call c05
    call c06
    call c07
    call c08
    if active_route == "ria":
        call ria_r01
        call ria_r02
        call ria_r03
        call ria_r04
        if dating:
            call ria_r05
            call ria_o01_offer
            call ria_r06
            call ria_r07
            call ria_r08
            call ria_r09
            call ria_r10
            call ria_o02_offer
            call ria_r11
            call ria_r12
            call ria_r13
            call ria_r14
            if dating and memory.get("ria_conflict") == "resolved":
                call ria_r15
                call ria_o03_offer
                call ria_r16
                if memory.get("ria_route_completed"):
                    menu:
                        "후일담 읽기 — 약 반년 뒤의 두 사람":
                            call ria_e01
                        "본편 결말에서 마치기 — 후일담은 이번에 읽지 않음":
                            $ remember("ria_epilogue_skipped")
            $ chapter = "리아 · 수록 구간 종료"
            "이번 개발판의 리아 이야기는 여기까지입니다. 유진·지현·서윤 대본도 수록되어 있으며, 최종 그림·음성·UI와 전체 읽기 편집은 준비 중입니다."
    elif active_route == "yujin":
        call yujin_early_route(full_route=True)
    elif active_route == "jihyun":
        call jihyun_early_route(full_route=True)
    elif active_route == "seoyun":
        call seoyun_route
    elif active_route == "colleague":
        call end_common
    else:
        $ ending = "prototype_route_selected"
        "선택한 개인 루트는 아직 수록되지 않았습니다. 이 회차의 공통 만남 기록은 저장할 수 있습니다."
    menu:
        "수록 구간을 마쳤습니다. 처음 화면으로 돌아가기.":
            return

label end_common:
    $ chapter = "END_COMMON · 좋은 동료로, 우리"
    $ location = "온빛브랜딩 · 몇 주 뒤"
    "각자의 일정이 조금씩 익숙해질 무렵, 캠페인 시안의 첫 검토가 끝났다."
    j "한꺼번에 다 바꾸지 말자. 이번에 확인한 것부터 반영하면 돼."
    y "문구 크기는 제가 다시 볼게요. 실제로 읽히는지도 확인하고 싶어요."
    s "그럼 전달할 내용은 내가 정리할게. 오늘은 '알아서 예쁘게' 같은 말 없이."
    d "현장에서는 사람들이 어디서 멈추는지 볼게요."
    if active_route == "ria":
        r "[ri('이번엔 내가 옆에서 같이 볼게.', '이번엔 제가 옆에서 같이 볼게요.')]"
    elif active_route == "yujin":
        y "다음 시안도 실제로 읽히는지 같이 봐 주세요. 처음 본 감상부터 듣고 싶어요."
    else:
        r "[ri('첫날 생각나네. 이번엔 의자도 있어.', '첫날 생각나네요. 이번엔 의자도 있어요.')]"
    "회의가 끝나자 하나둘 자리를 정리했다. 누군가는 더 남고, 누군가는 먼저 퇴근했다."
    if downtime == "walk":
        dn "오늘은 집까지 조금 돌아갈 생각이다. 기록집에 남기고 싶은 길이 있었다."
    elif downtime == "rest":
        dn "오늘은 곧장 집에 가서 쉬기로 했다. 이 동네도 이제 조금 익숙해졌다."
    else:
        dn "퇴근 전에 근처 가게를 하나 찾아 뒀다. 오늘 저녁은 거기서 먹기로 했다."
    dn "누군가의 연인이 되지는 않았다. 그래도 다음 출근이 아주 낯설지는 않았다."
    $ ending = "colleague"
    $ persistent.local_colleague_ending = True
    "동료 결말 · 좋은 동료로, 우리"
    return

