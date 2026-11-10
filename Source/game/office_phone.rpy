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

# Presentation helpers for the window-themed messenger.
init -5 python:
    def phone_surface(kind):
        aliases = {"panel": "paper", "soft": "soft", "peer": "peer", "mine": "mine",
                   "selected": "selected", "button": "paper", "hover": "choice_hover"}
        return office_ui_surface(aliases[kind], radius=6)

    def phone_status_time(moment):
        if any(word in moment for word in ("아침", "오전")):
            return "오전 9:41"
        if any(word in moment for word in ("저녁", "밤", "퇴근")):
            return "오후 7:24"
        return "오후 2:16"

style phone_text is default:
    font "fonts/Pretendard-Regular.otf"
    color "#27252c"
    outlines []
style phone_button is button:
    background phone_surface("button")
    hover_background phone_surface("hover")
    selected_background phone_surface("selected")
    padding (15, 10)
    keyboard_focus True
style phone_button_text is phone_text:
    size 18
    hover_color "#864940"
    line_spacing 4
style phone_reply_button is phone_button:
    xfill True
    yminimum 32
    padding (10, 5)
    background phone_surface("peer")
style phone_reply_button_text is phone_button_text:
    size 16
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
    $ message_height = 298 if choosing_reply else 356
    $ contact_rows = phone_threads.get(selected, [])
    add Solid("#18171da6")

    frame:
        xalign 0.5 yalign 0.5 xsize 380 ysize 652 padding (8, 8)
        background CreamRoundedPanel("#25232a", "#55505a", radius=29)
        frame:
            xsize 364 ysize 636 padding (0, 0)
            background CreamRoundedPanel("#f6f7fa", "#f6f7fa", radius=22)
            text phone_status_time(location) xpos 19 ypos 12 size 15
            add "gui/window/phone_status.svg" xpos 269 ypos 13 xysize (74, 15)
            add CreamRoundedPanel("#27242f", "#27242f", radius=5) xalign 0.5 ypos 13 xysize (9, 9)
            text phone_names(selected) xalign 0.5 ypos 47 size 24
            if archive:
                textbutton "닫기" id "phone_archive_close" xpos 13 ypos 43 action Hide("office_phone_archive") text_size 15 padding (8, 7)
            use window_phone_avatar(23, 323, 48)
            hbox:
                xpos 16 ypos 85 spacing 4
                for contact, name, initial in PHONE_CONTACTS:
                    textbutton (name + (" •" if phone_unread(contact) else "")):
                        id ("phone_contact_" + contact)
                        xsize 80 text_size 13 text_xalign 0.5 padding (3, 7)
                        background (Solid("#fff0b8") if selected == contact else Solid("#edf0f4"))
                        hover_background Solid("#fff0b8")
                        action [SetLocalVariable("selected", contact), Function(phone_mark_read, contact)]
            add Solid("#ccdeed") xpos 8 ypos 120 xsize 348 ysize message_height
            viewport:
                id "phone_messages"
                xpos 21 ypos 129 xsize 314 ysize (message_height - 17)
                mousewheel True draggable True
                yinitial 1.0
                vbox:
                    xsize 314 spacing 12
                    if not contact_rows:
                        text "아직 주고받은 메시지가 없어요." size 17 color "#425768" xalign 0.5
                    $ previous_moment = None
                    for row in contact_rows:
                        $ moment = row.get("moment", "이전 대화")
                        if moment != previous_moment:
                            text moment size 13 color "#425768" xalign 0.5 xmaximum 288 text_align 0.5
                        $ previous_moment = moment
                        $ mine = row["sender"] in ("dohyun", "ria_shared")
                        hbox:
                            xalign (1.0 if mine else 0.0)
                            spacing 7
                            if not mine:
                                use window_phone_avatar(29)
                            vbox:
                                spacing 3
                                if not mine or row["sender"] == "ria_shared":
                                    text ("리아 · 함께 보낸 메시지" if mine else phone_names(selected)) size 13 color "#425768"
                                frame:
                                    xmaximum 264 padding (10, 8)
                                    background phone_surface("mine" if mine else "peer")
                                    vbox:
                                        spacing 6
                                        text row["text"] substitute False size 17 xmaximum 244 line_spacing 3
                                        if row.get("media"):
                                            $ media = row["media"]
                                            button:
                                                id ("phone_photo_" + media)
                                                padding (8, 6)
                                                action [Function(phone_note_photo, media), Show("office_phone_photo", media=media)]
                                                if phone_media_ready(media):
                                                    add Transform(PHONE_MEDIA[media]["path"], xysize=(208, 116), fit="contain")
                                                else:
                                                    text "사진 준비 중 · 눌러서 확대" size 14 color "#864940"
            vbar value YScrollValue("phone_messages") style "office_scrollbar" xpos 341 ypos 129 ysize (message_height - 17)

            if archive:
                $ photos = [row["media"] for row in contact_rows if row.get("media")]
                text "이 회차에서 받은 메시지만 표시합니다." xpos 21 ypos 501 size 14 color "#62545c"
                if photos:
                    textbutton "최근 사진 다시 보기":
                        id "phone_archive_photo"
                        xpos 21 ypos 534 text_size 16
                        action [Function(phone_note_photo, photos[-1]), Show("office_phone_photo", media=photos[-1])]
            elif selected != phone_active_contact:
                text (phone_names(phone_active_contact) + " 대화가 기다리고 있어요.") xpos 21 ypos 501 size 16 xmaximum 318
                textbutton "진행 중인 대화로 돌아가기" xpos 21 ypos 535 action SetLocalVariable("selected", phone_active_contact) text_size 16
            elif waiting:
                text (phone_names(phone_active_contact) + " 님이 입력 중…") xpos 21 ypos 501 size 16
                textbutton "바로 보기" id "phone_next" xpos 21 ypos 535 action Return("next") text_size 17
            elif replies:
                text "답장 선택" xpos 21 ypos 430 size 14 color "#62545c"
                viewport:
                    id "phone_replies"
                    xpos 21 ypos 454 xsize 314 ysize 155
                    mousewheel True draggable True arrowkeys True
                    vbox:
                        xsize 312 spacing 5
                        for value, caption in replies:
                            textbutton caption:
                                id ("phone_reply_" + value)
                                action Return(value)
                                style "phone_reply_button"
                vbar value YScrollValue("phone_replies") style "office_scrollbar" xpos 341 ypos 454 ysize 155
            else:
                textbutton "다음 메시지" id "phone_next" xpos 21 ypos 518 action Return("next") text_size 17
            add CreamRoundedPanel("#292631", "#292631", radius=2) xalign 0.5 ypos 621 xysize (100, 4)

    vbox:
        xpos 851 ypos 56 spacing 5
        if not archive:
            textbutton "되돌리기" action Rollback() style "cream_quick_button"
        textbutton "저장" action ShowMenu("save") style "cream_quick_button"
        textbutton "불러오기" action ShowMenu("load") style "cream_quick_button"
        textbutton "설정" action ShowMenu("preferences") style "cream_quick_button"

screen window_phone_avatar(diameter, left=0, top=0):
    fixed:
        xpos left ypos top
        xysize (diameter, diameter)
        add CreamRoundedPanel("#e6edf4", "#c1cfdb", radius=diameter // 2)

screen office_phone_photo(media):
    style_prefix "phone"
    modal True
    zorder 150
    key "game_menu" action Hide("office_phone_photo")
    add Solid("#211927ed")
    frame:
        xalign 0.5 yalign 0.5 xsize 940 ysize 640 padding (24, 22)
        background phone_surface("panel")
        vbox:
            spacing 14
            text PHONE_MEDIA[media]["title"] size 24 color "#864940"
            fixed:
                xsize 892 ysize 487
                if phone_media_ready(media):
                    add Transform(PHONE_MEDIA[media]["path"], xysize=(892, 487), fit="contain") xalign 0.5 yalign 0.5
                else:
                    add Solid("#f2e5de")
                    vbox:
                        xalign 0.5 yalign 0.5 spacing 16
                        text "사진 준비 중" size 34 xalign 0.5 color "#864940"
                        text "실제 이미지가 들어오면 이 자리에서 확대됩니다." size 21 color "#62545c"
                        text "빈 자리는 사진 감상 완료로 기록하지 않습니다." size 17 color "#62545c"
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
