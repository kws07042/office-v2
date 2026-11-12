# Save-local messaging. No network, persistent unlocks, or real-time penalties.
default phone_threads = {"ria": [], "jihyun": [], "yujin": [], "seoyun": []}
default phone_read_ids = []
default phone_photo_opened = []
default phone_photo_previews = []
default phone_context = None
default phone_active_contact = "ria"
default persistent.phone_typing_enabled = True

init python:
    PHONE_CONTACTS = [("ria", "강리아", "R"), ("jihyun", "백지현", "J"), ("yujin", "차유진", "Y"), ("seoyun", "한서윤", "S")]
    PHONE_MEDIA = {"ria_r08_breakfast": {"path": "images/messages/ria/r08_breakfast.png", "title": "일요일 아침 식탁", "caption": "리아가 보낸 아침 식탁 사진"}}

    def phone_add(mid, sender, text, media=None, contact="ria"):
        rows = renpy.store.phone_threads.get(contact, [])
        if any(row["id"] == mid for row in rows):
            return
        row = {"id": mid, "sender": sender, "text": text, "media": media, "moment": renpy.store.location.split(" · ")[0]}
        renpy.store.phone_threads = dict(renpy.store.phone_threads, **{contact: rows + [row]})
        phone_mark_read(contact)

    def phone_mark_read(contact):
        ids = [row["id"] for row in renpy.store.phone_threads.get(contact, []) if row["sender"] != "dohyun"]
        renpy.store.phone_read_ids = list(dict.fromkeys(renpy.store.phone_read_ids + ids))

    def phone_media_ready(media):
        return media in PHONE_MEDIA and renpy.loadable(PHONE_MEDIA[media]["path"])

    def phone_note_photo(media):
        attr = "phone_photo_opened" if phone_media_ready(media) else "phone_photo_previews"
        setattr(renpy.store, attr, list(dict.fromkeys(getattr(renpy.store, attr) + [media])))

    def phone_names(contact):
        return dict((key, name) for key, name, initial in PHONE_CONTACTS).get(contact, contact)

    def phone_unread(contact):
        return sum(row["sender"] != "dohyun" and row["id"] not in renpy.store.phone_read_ids for row in renpy.store.phone_threads.get(contact, []))

# Shared cream/lavender presentation; message IDs, replies and state are unchanged.
init -5 python:
    def phone_surface(kind):
        aliases = {"panel": "paper", "soft": "soft", "peer": "peer", "mine": "mine",
                   "selected": "selected", "button": "paper", "hover": "choice_hover"}
        return office_ui_surface(aliases[kind], radius=18)

style phone_text is default:
    font "fonts/Pretendard-Regular.otf"
    color "#3d3345"
    outlines []
style phone_button is button:
    background phone_surface("button")
    hover_background phone_surface("hover")
    selected_background phone_surface("selected")
    padding (15, 10)
    keyboard_focus True
style phone_button_text is phone_text:
    size 18
    hover_color "#644675"
    line_spacing 4
style phone_reply_button is phone_button:
    xfill True
    yminimum 42
    padding (16, 9)
    background phone_surface("peer")
style phone_reply_button_text is phone_button_text:
    size 18
    text_align 0.0
    xalign 0.0

screen office_phone(replies=None, waiting=False):
    modal not cream_menu_open()
    zorder 40
    if not cream_menu_open():
        use office_phone_contents(replies, waiting, False)
    if waiting and not cream_menu_open():
        timer 0.9 action Return("next")

screen office_phone_archive():
    modal not cream_menu_open()
    zorder 40
    key "game_menu" action Hide("office_phone_archive")
    if not cream_menu_open():
        use office_phone_contents(None, False, True)

screen office_phone_contents(replies, waiting, archive):
    default selected = phone_active_contact
    if not archive and not replies:
        key "dismiss" action Return("next")
    style_prefix "phone"
    $ choosing_reply = bool(replies and selected == phone_active_contact and not archive and not waiting)
    add Solid("#f3eff6")
    frame:
        xpos 32 ypos 24 xsize 1216 ysize 80 padding (0, 0)
        background phone_surface("panel")
    text "퇴근 후, 우리" xpos 57 ypos 37 size 27 font "fonts/GowunDodum-Regular.ttf" color "#65446e"
    text ("개인 메시지 · 대화 기록" if archive else ("개인 메시지 · " + location.split(" · ")[0])) xpos 58 ypos 77 size 14 color "#766b7e"
    hbox:
        xpos 1220 xanchor 1.0 ypos 44 spacing 8
        if not archive:
            textbutton "되돌리기" action Rollback() text_size 16 padding (14, 9)
        textbutton "저장" action ShowMenu("save") text_size 16 padding (14, 9)
        textbutton "불러오기" action ShowMenu("load") text_size 16 padding (14, 9)
        textbutton "설정" action ShowMenu("preferences") text_size 16 padding (14, 9)
        if archive:
            textbutton "닫기" action Hide("office_phone_archive") id "phone_archive_close" text_size 16 padding (14, 9)

    frame:
        xpos 32 ypos 120 xsize 272 ysize 576 padding (18, 20)
        background phone_surface("panel")
        vbox:
            spacing 14
            text "함께 나눈 대화" size 17 color "#766b7e"
            for contact, name, initial in PHONE_CONTACTS:
                $ count = len(phone_threads.get(contact, []))
                button:
                    id ("phone_contact_" + contact)
                    xsize 236 padding (12, 16)
                    background (phone_surface("selected") if selected == contact else None)
                    hover_background phone_surface("hover")
                    action [SetLocalVariable("selected", contact), Function(phone_mark_read, contact)]
                    hbox:
                        spacing 12
                        fixed:
                            xsize 36 ysize 36
                            add CreamRoundedPanel("#e6dced", "#e6dced", radius=18)
                            text initial xalign 0.5 yalign 0.5 size 17 color "#705080"
                        vbox:
                            spacing 5
                            text name size 21 font "fonts/GowunDodum-Regular.ttf" color "#594361"
                            text (("메시지 " + str(count) + "개") if count else "아직 대화가 없어요") size 13 color "#766b7e"
                            if phone_unread(contact):
                                text ("새 메시지 " + str(phone_unread(contact))) size 13 color "#87587f"
            null height 14
            text "이번 회차에 주고받은 이야기가\n여기에 차곡차곡 남아요." size 14 line_spacing 5 color "#766b7e"

    frame:
        xpos 320 ypos 120 xsize 928 ysize 576 padding (0, 0)
        background phone_surface("panel")
    text phone_names(selected) xpos 348 ypos 143 size 27 font "fonts/GowunDodum-Regular.ttf" color "#594361"
    text ("교제 중 · 개인 대화" if selected == active_route and dating else ("함께 확인한 동료 연락" if any(row["sender"] == "ria_shared" for row in phone_threads.get(selected, [])) else "개인 대화")) xpos 475 ypos 153 size 15 color "#766b7e"
    add Solid("#e4dce9") xpos 348 ypos 191 xsize 872 ysize 1
    viewport:
        id "phone_messages"
        xpos 348 ypos 211 xsize 872 ysize (278 if choosing_reply else (386 if archive else 352))
        mousewheel True draggable True
        scrollbars "vertical"
        vscrollbar_xsize 6 vscrollbar_base_bar Solid("#eae3ee") vscrollbar_thumb Solid("#bca4ca") vscrollbar_unscrollable "hide"
        yinitial 1.0
        vbox:
            xsize 844 spacing 15
            if not phone_threads.get(selected):
                text "아직 주고받은 메시지가 없어요." size 20 color "#766b7e"
            $ previous_moment = None
            for row in phone_threads.get(selected, []):
                $ moment = row.get("moment", "이전 대화")
                if moment != previous_moment:
                    frame:
                        xalign 0.5 padding (12, 5)
                        background phone_surface("soft")
                        text moment size 13 color "#766b7e"
                $ previous_moment = moment
                frame:
                    xalign (1.0 if row["sender"] in ("dohyun", "ria_shared") else 0.0)
                    xmaximum 640 padding (18, 14)
                    background phone_surface("mine" if row["sender"] in ("dohyun", "ria_shared") else "peer")
                    vbox:
                        spacing 7
                        text ("리아 · 함께 보낸 메시지" if row["sender"] == "ria_shared" else ("나" if row["sender"] == "dohyun" else phone_names(selected))) size 13 color "#705080"
                        text row["text"] substitute False size 20 xmaximum 598 line_spacing 5 color "#3d3345"
                        if row.get("media"):
                            $ media = row["media"]
                            button:
                                id ("phone_photo_" + media)
                                padding (12, 9)
                                action [Function(phone_note_photo, media), Show("office_phone_photo", media=media)]
                                if phone_media_ready(media):
                                    add Transform(PHONE_MEDIA[media]["path"], xysize=(240, 125), fit="contain")
                                else:
                                    vbox:
                                        spacing 5
                                        text "사진 준비 중" size 19 color "#705080"
                                        text "아침 식탁 · 눌러서 확대" size 14 color "#766b7e"

    if archive:
        add Solid("#e4dce9") xpos 348 ypos 616 xsize 872 ysize 1
        text "이 회차에서 받은 메시지만 표시합니다." xpos 350 ypos 642 size 16 color "#766b7e"
        $ photos = [row["media"] for row in phone_threads.get(selected, []) if row.get("media")]
        if photos:
            textbutton "최근 사진 다시 보기":
                id "phone_archive_photo"
                xpos 1000 ypos 632 text_size 16 padding (14, 10)
                action [Function(phone_note_photo, photos[-1]), Show("office_phone_photo", media=photos[-1])]
    elif selected != phone_active_contact:
        text (phone_names(phone_active_contact) + " 대화가 기다리고 있어요.") xpos 350 ypos 601 size 19 color "#766b7e"
        textbutton "진행 중인 대화로 돌아가기" xpos 350 ypos 636 action SetLocalVariable("selected", phone_active_contact) text_size 18
    elif waiting:
        text (phone_names(phone_active_contact) + " 님이 입력 중…") xpos 350 ypos 605 size 20 color "#705080"
        textbutton "바로 보기" id "phone_next" xpos 1090 ypos 626 action Return("next") text_size 18
    elif replies:
        add Solid("#e4dce9") xpos 348 ypos 503 xsize 872 ysize 1
        text "어떤 마음을 전할까요?" xpos 350 ypos 515 size 15 color "#766b7e"
        viewport:
            id "phone_replies"
            xpos 348 ypos 544 xsize 872 ysize 150
            mousewheel True draggable True arrowkeys True
            scrollbars "vertical"
            vscrollbar_xsize 6 vscrollbar_base_bar Solid("#eae3ee") vscrollbar_thumb Solid("#bca4ca") vscrollbar_unscrollable "hide"
            vbox:
                xsize 846 spacing 7
                for value, caption in replies:
                    textbutton caption:
                        id ("phone_reply_" + value)
                        action Return(value)
                        style "phone_reply_button"
    else:
        text "대화를 읽고 편할 때 이어가세요." xpos 350 ypos 606 size 18 color "#766b7e"
        textbutton "다음 메시지" id "phone_next" xpos 1060 ypos 626 action Return("next") text_size 18
    if not archive and not choosing_reply:
        text "답장은 편할 때 · 실제 시간에 따른 벌점 없음" xpos 350 ypos 674 size 12 color "#766b7e"

screen office_phone_photo(media):
    style_prefix "phone"
    modal True
    zorder 150
    key "game_menu" action Hide("office_phone_photo")
    add Solid("#30263ddd")
    frame:
        xalign 0.5 yalign 0.5 xsize 940 ysize 640 padding (24, 22)
        background phone_surface("panel")
        vbox:
            spacing 14
            text PHONE_MEDIA[media]["title"] size 24 color "#705080"
            fixed:
                xsize 892 ysize 487
                if phone_media_ready(media):
                    add Transform(PHONE_MEDIA[media]["path"], xysize=(892, 487), fit="contain") xalign 0.5 yalign 0.5
                else:
                    add Solid("#f3eff6")
                    vbox:
                        xalign 0.5 yalign 0.5 spacing 16
                        text "사진 준비 중" size 34 xalign 0.5 color "#705080"
                        text "실제 이미지가 들어오면 이 자리에서 확대됩니다." size 21 color "#766b7e"
                        text "빈 자리는 사진 감상 완료로 기록하지 않습니다." size 17 color "#766b7e"
            textbutton "대화로 돌아가기" id "phone_photo_close" action Hide("office_phone_photo") text_size 20 xalign 0.5

label phone_deliver(mid, sender, body, media=None, important=False, contact="ria"):
    $ phone_active_contact = contact
    if important and persistent.phone_typing_enabled and not getattr(_preferences, "reduced_motion", False) and not renpy.is_skipping():
        call screen office_phone(waiting=True)
    $ phone_add(mid, sender, body, media, contact)
    call screen office_phone
    return

label ria_r08_phone_conversation:
    $ progression_enter("ria_r08_phone_conversation")
    $ progression_checkpoint("ria_r08_phone_conversation")
    $ phone_context = "r08_start"
    if memory.get("ria_r07_intimacy") != "shared":
        call phone_deliver("r08_morning_1", "ria", ri("일어났어? 나는 빵 먹는 중~ 오늘 추천 코스는 식탁!", "일어나셨어요? 저는 빵 먹는 중이에요~ 오늘 추천 코스는 식탁!"))
        call phone_deliver("r08_morning_2", "dohyun", ri("나도 이제 아침 먹으려고. 어제 차 잘 마셨어.", "저도 이제 아침 먹으려고요. 어제 차 잘 마셨어요."))
        call phone_deliver("r08_morning_3", "ria", ri("응! 별일은 없는데 네 생각이 나서. 오늘은 내가 먼저~", "네! 별일은 없는데 도현 씨 생각이 나서요. 오늘은 제가 먼저예요~"))
    if memory.get("ria_r07_intimacy") == "shared":
        call phone_deliver("r08_photo", "ria", ri("아침 사진 이제 보내네~ 잘 구운 쪽 줬으니까 다음엔 네가 골라 줘!", "아침 사진 이제 보내네요~ 잘 구운 쪽 드렸으니까 다음엔 도현 씨가 골라 주세요!"), media="ria_r08_breakfast")
    else:
        call phone_deliver("r08_photo", "ria", ri("오늘의 추천 코스 인증~ 빵은 내가 골랐어!", "오늘의 추천 코스 인증~ 빵은 제가 골랐어요!"), media="ria_r08_breakfast")
    call phone_deliver("r08_laundry_route", "ria", ri("지도에 그 세탁소 저장했어. 다음엔 길 아는데도 같이 돌자고 할게~", "지도에 그 세탁소 저장했어요. 다음엔 길 아는데도 같이 돌자고 할게요~"))
    call phone_deliver("r08_question", "ria", ri("오늘 뭐 해? 나는 빨래 돌리고 나면 특별한 일 없어.", "오늘 뭐 하세요? 저는 빨래 돌리고 나면 특별한 일 없어요."))
    $ phone_context = "r08_reply"
    $ progression_enter("ria_r08_phone_conversation.choice01")
    $ progression_checkpoint("ria_r08_phone_conversation.choice01")
    call screen office_phone(replies=[("miss", "보고 싶다고 짧게 답한다."), ("evening", "오늘 할 일을 나누고 저녁 연락을 제안한다."), ("small_memory", "어제 좋았던 작은 순간을 하나 골라 보낸다.")])
    $ remember("ria_r08_reply", _return)
    $ phone_context = "r08_response"
    if memory["ria_r08_reply"] == "miss":
        call phone_deliver("r08_reply", "dohyun", ri("기록 정리 중인데, 벌써 보고 싶네.", "기록 정리 중인데, 벌써 보고 싶네요."))
        call phone_deliver("r08_answer", "ria", ri("잠깐만, 방금 그거 세 번 읽었어. 네가 먼저 이러면 나 뭐라고 보내?", "잠깐만요, 방금 그거 세 번 읽었어요. 먼저 이러시면 저 뭐라고 보내요?"), important=True)
        call phone_deliver("r08_followup", "dohyun", ri("답은 나중에 해도 돼. 그냥 먼저 말하고 싶었어.", "답은 나중에 하셔도 돼요. 그냥 먼저 말하고 싶었어요."))
        call phone_deliver("r08_answer_2", "ria", ri("응. 나도 보고 싶어. 이건 지금 답할래 :)", "네. 저도 보고 싶어요. 이건 지금 답할래요 :)"), important=True)
    elif memory["ria_r08_reply"] == "evening":
        call phone_deliver("r08_reply", "dohyun", ri("기록 좀 정리하려고. 저녁에 끝나면 얘기할래?", "기록 좀 정리하려고요. 저녁에 끝나면 얘기하실래요?"))
        call phone_deliver("r08_answer", "ria", ri("좋아. 나는 빨래 산부터 넘을게. 이쪽도 꽤 큰 작업이야~", "좋아요. 저는 빨래 산부터 넘을게요. 이쪽도 꽤 큰 작업이에요~"))
        call phone_deliver("r08_followup", "dohyun", ri("먼저 끝난 사람이 전화하기. 빨래 다 개야 끝난 거다?", "먼저 끝난 사람이 전화해요. 빨래 다 개셔야 끝난 거예요."))
        call phone_deliver("r08_answer_2", "ria", ri("치사해. 그럼 넌 책상까지 치워야 끝이야~ 이따 전화해!", "치사해요. 그럼 도현 씨도 책상까지 치우셔야 돼요~ 이따 전화해요!"), important=True)
    else:
        $ remember("choice_third_r08_reply")
        call phone_deliver("r08_reply", "dohyun", ri("어제 나란히 앉아 있던 거 생각났어. 별말 안 해도 좋더라.", "어제 나란히 앉아 있던 거 생각났어요. 별말 안 해도 좋더라고요."))
        call phone_deliver("r08_answer", "ria", ri("나도! 사실 조용해질 때 무슨 얘기할지 찾고 있었는데~", "저도요! 사실 조용해질 때 무슨 얘기할지 찾고 있었는데요~"))
        call phone_deliver("r08_followup", "dohyun", ri("나도 컵만 봤어. 먼저 눈 마주치면 무슨 말 할지 까먹어서.", "저도 컵만 봤어요. 먼저 눈 마주치면 무슨 말 할지 까먹어서요."))
        call phone_deliver("r08_answer_2", "ria", ri("좋아 :) 다음엔 조용해졌다고 말 찾느라 컵만 돌리지는 않을게~", "좋아요 :) 다음엔 조용해졌다고 말 찾느라 컵만 돌리지는 않을게요~"), important=True)
    if memory.get("ria_o01_status") == "completed":
        call phone_deliver("r08_lunch", "ria", ri("참, 오늘 점심은 나도 국수! 지난번 네 거 보고 생각났어.", "참, 오늘 점심은 저도 국수요! 지난번 드시는 거 보고 생각났어요."))
        call phone_deliver("r08_lunch_reply", "dohyun", ri("오늘 메뉴 맞히기였으면 틀릴 뻔했네.", "오늘 메뉴 맞히기였으면 틀릴 뻔했네요."))
    else:
        call phone_deliver("r08_lunch", "ria", ri("점심은 국수 먹으려고. 너도 끼니는 챙겨!", "점심은 국수 먹으려고요. 도현 씨도 끼니는 챙기세요!"))
    $ phone_context = None
    $ progression_note_ending()
    return

label office_phone_preview:
    $ cream_preview_active = False
    $ active_route = "ria"
    $ dating = True
    $ speech_informal = True
    $ affinity = {"ria":58, "jihyun":0, "yujin":0, "seoyun":0}
    $ memory = {"ria_r07_intimacy":"deferred"}
    call ria_r08
    "메신저 확인을 마쳤습니다. 아래 ‘메신저’에서 이 회차의 대화를 다시 볼 수 있습니다."
    menu:
        "처음 화면으로":
            return

label ria_disclosure_phone:
    call phone_deliver("ria_disclosure_1", "ria_shared", "언니, 나 도현 씨랑 사귀어. 우리 둘이 같이 알려 주고 싶어서 보냈어! 다른 사람들한테는 아직 말하지 말아 줘~", contact="seoyun")
    call phone_deliver("ria_disclosure_2", "seoyun", "어머, 둘이 드디어 말해 주네~ 축하해. 다른 사람들한텐 너희가 얘기할 때까지 비밀로 할게.", contact="seoyun", important=True)
    call phone_deliver("ria_disclosure_3", "seoyun", "리아야, 데이트 일정까지 캠페인처럼 꽉 채우진 말고. 도현 씨도 즐거운 저녁 보내요 :)", contact="seoyun")
    call phone_deliver("ria_disclosure_4", "dohyun", "서윤 씨, 감사합니다. 오늘은 저녁만 같이 만들려고요.", contact="seoyun")
    $ phone_active_contact = "ria"
    return
