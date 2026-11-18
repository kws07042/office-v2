# Save-local messaging. No network, persistent unlocks, or real-time penalties.
default phone_threads = {"ria": [], "jihyun": [], "yujin": [], "seoyun": []}
default phone_read_ids = []
default phone_photo_opened = []
default phone_photo_previews = []
default phone_context = None
default phone_active_contact = "ria"
default persistent.phone_typing_enabled = True

init python:
    def phone_follow_adjustment():
        # 내용 높이(range)가 바뀔 때마다 값을 끝으로 맞춘다. 직접 위로 올려 읽는 동안에는
        # 새 메시지가 오기 전까지 그 자리를 유지한다.
        return ui.adjustment(ranged=lambda adj: adj.change(adj.range))

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
    hover_color "#69424b"
    line_spacing 4
screen office_phone(replies=None, waiting=False):
    modal not cream_menu_open()
    zorder 40
    if not cream_menu_open():
        use office_phone_contents(replies, waiting, False)
    # 자동 검사에서는 '입력 중' 화면이 저절로 닫히지 않게 한다. 검사가 화면을 확인하는 사이에
    # 닫히면 다음 단계가 어긋난다. 검사는 '바로 보기' 버튼으로 넘긴다.
    if waiting and not cream_menu_open() and not renpy.is_in_test():
        timer 0.9 action Return("next")

screen office_phone_archive():
    modal not cream_menu_open()
    zorder 40
    key "game_menu" action Hide("office_phone_archive")
    if not cream_menu_open():
        use office_phone_contents(None, False, True)

# ── 메신저 화면 (실크 테마) ─────────────────────────────────────
# 버튼 id와 동작은 예전과 같다. 모양만 바꿨다.
transform phone_dot(delay=0.0):
    yoffset 0 alpha 0.45
    pause delay
    block:
        ease 0.22 yoffset -5 alpha 1.0
        ease 0.22 yoffset 0 alpha 0.45
        pause 0.5
        repeat

style phone_chip_button is button:
    background None
    hover_background silk("flat", "#F3E7EA", 14)
    selected_background silk("flat", "#F3E7EA", 14)
    padding (6, 4, 8, 4)
    keyboard_focus True
style phone_send_button is button:
    background silk("pill", "#B3123F", "#3B0B22", "#3B0B22", None, 3, 4)
    hover_background silk("pill", "#3B0B22", "#3B0B22", "#B3123F", None, 3, 4)
    padding (20, 9, 24, 14)
    keyboard_focus True
style phone_send_button_text is phone_text:
    size 16
    color "#FFFDFB"
    font "fonts/Jua-Regular.ttf"
style phone_reply_button is button:
    background silk("pill", "#FFFDFB", "#3B0B22", "#3B0B22", 18, 3, 4)
    hover_background silk("pill", "#3B0B22", "#3B0B22", "#B3123F", 18, 3, 4)
    xfill True
    yminimum 44
    padding (16, 9, 20, 14)
    keyboard_focus True
style phone_reply_button_text is phone_text:
    size 16
    color "#3B0B22"
    hover_color "#FFFDFB"
    text_align 0.0
    xalign 0.0
    line_spacing 3
style phone_side_button is silk_small_button
style phone_side_button_text is silk_small_button_text

# 자동 검사는 버튼의 현재 위치를 누른다. 휴대폰이 올라오는 도중에 누르면 가상 마우스가 아래쪽
# 빠른 메뉴 위에 남아 이후 Enter가 대사로 가지 않으므로, 검사 중에는 올라오는 연출을 끈다.
screen office_phone_contents(replies, waiting, archive):
    # 새 메시지로 대화 내용이 길어지면 자동으로 맨 아래(최신 대화)로 내려간다.
    default phone_messages_adj = phone_follow_adjustment()
    default selected = phone_active_contact
    if not archive and not replies:
        key "dismiss" action Return("next")
    style_prefix "phone"
    $ choosing_reply = bool(replies and selected == phone_active_contact and not archive and not waiting)
    $ message_height = 292 if choosing_reply else (410 if archive else 398)
    $ contact_rows = phone_threads.get(selected, [])
    $ chat_top = 150
    $ below = chat_top + message_height
    add Solid("#1B0F16b8")

    frame:
        at (silk_phone_rise if (silk_motion_on() and silk_phone_fresh_now and not archive and not renpy.is_in_test()) else silk_still)
        xalign 0.5 yalign 0.5 xsize 404 ysize 684 padding (9, 9)
        background silk("flat", "#1B0F16", 38)
        frame:
            xsize 386 ysize 666 padding (0, 0)
            background silk("flat", "#FFFDFB", 30)
            # 상태 표시줄
            text phone_status_time(location) xpos 24 ypos 13 size 14 color "#3B0B22"
            add "gui/window/phone_status.svg" xpos 290 ypos 14 xysize (74, 15)
            add silk("flat", "#1B0F16", 6) xalign 0.5 ypos 12 xysize (64, 16)
            # 대화 상대
            use window_phone_avatar(44, 18, 42, selected)
            text phone_names(selected) xpos 72 ypos 43 size 21 font "fonts/Jua-Regular.ttf" color "#3B0B22"
            text ("지난 대화" if archive else ("입력 중…" if (waiting and selected == phone_active_contact) else "대화 중")) xpos 73 ypos 70 size 12 color ("#B3123F" if (waiting and not archive) else "#8A6B76")
            if archive:
                textbutton "닫기" id "phone_archive_close" xanchor 1.0 xpos 368 ypos 46 action Hide("office_phone_archive") style "phone_side_button"
            # 대화방 바꾸기
            hbox:
                xpos 14 ypos 100 spacing 2
                for contact, name, initial in PHONE_CONTACTS:
                    button:
                        id ("phone_contact_" + contact)
                        style "phone_chip_button"
                        xsize 88
                        selected (selected == contact)
                        action [SetLocalVariable("selected", contact), Function(phone_mark_read, contact)]
                        alt name
                        hbox:
                            spacing 5 xalign 0.5
                            use window_phone_avatar(22, 0, 0, contact)
                            text name size 13 yalign 0.5 color ("#3B0B22" if selected == contact else "#8A6B76")
                            if phone_unread(contact):
                                add silk("flat", "#B3123F", 4) xysize (7, 7) yalign 0.2
            add Solid("#E9DEE1") xpos 0 ypos (chat_top - 1) xysize (386, 1)
            # 대화 내용
            add Solid("#DFE8EE") xpos 0 ypos chat_top xsize 386 ysize message_height
            viewport:
                id "phone_messages"
                xpos 16 ypos (chat_top + 10) xsize 346 ysize (message_height - 20)
                mousewheel True draggable True
                yadjustment phone_messages_adj
                vbox:
                    xsize 346 spacing 10
                    if not contact_rows:
                        null height 60
                        text "아직 주고받은 메시지가 없어요." size 15 color "#5E7482" xalign 0.5
                    $ previous_moment = None
                    for row_index, row in enumerate(contact_rows):
                        $ moment = row.get("moment", "이전 대화")
                        if moment != previous_moment:
                            frame:
                                xalign 0.5 padding (12, 3)
                                background silk("flat", "#C9D6DE", 11)
                                text moment size 12 color "#4A5F6C" xmaximum 260 text_align 0.5
                        $ previous_moment = moment
                        $ mine = row["sender"] in ("dohyun", "ria_shared")
                        hbox:
                            at ((silk_bubble_pop if (row_index == len(contact_rows) - 1 and not archive and silk_motion_on()) else silk_still))
                            xalign (1.0 if mine else 0.0)
                            spacing 7
                            if not mine:
                                use window_phone_avatar(30, 0, 0, selected)
                            vbox:
                                spacing 3
                                if not mine or row["sender"] == "ria_shared":
                                    text ("리아 · 함께 보낸 메시지" if mine else phone_names(selected)) size 12 color "#5E7482" xalign (1.0 if mine else 0.0)
                                frame:
                                    xmaximum 262 padding (13, 9, 13, 10)
                                    background silk("flat", ("#FFE25A" if mine else "#FFFFFF"), 16)
                                    vbox:
                                        spacing 6
                                        text row["text"] substitute False size 16 xmaximum 236 line_spacing 4 color "#2A2025"
                                        if row.get("media"):
                                            $ media = row["media"]
                                            button:
                                                id ("phone_photo_" + media)
                                                padding (8, 6)
                                                background silk("flat", "#F3E7EA", 10)
                                                hover_background silk("flat", "#E9D3D9", 10)
                                                action [Function(phone_note_photo, media), Show("office_phone_photo", media=media)]
                                                if phone_media_ready(media):
                                                    add Transform(PHONE_MEDIA[media]["path"], xysize=(208, 116), fit="contain")
                                                else:
                                                    text "사진 준비 중 · 눌러서 확대" size 13 color "#B3123F"
                    if waiting and selected == phone_active_contact and not archive:
                        hbox:
                            spacing 7
                            use window_phone_avatar(30, 0, 0, selected)
                            frame:
                                padding (14, 13)
                                background silk("flat", "#FFFFFF", 16)
                                hbox:
                                    spacing 5
                                    for d in range(3):
                                        add silk("flat", "#8A6B76", 4) xysize (8, 8) at (phone_dot(0.15 * d) if silk_motion_on() else silk_still)
            vbar value YScrollValue("phone_messages") style "office_scrollbar" xpos 372 ypos (chat_top + 10) ysize (message_height - 20)
            add Solid("#E9DEE1") xpos 0 ypos below xysize (386, 1)

            # 아래쪽: 답장 / 다음 / 안내
            if archive:
                $ photos = [row["media"] for row in contact_rows if row.get("media")]
                text "이 회차에서 받은 메시지만 표시합니다." xpos 22 ypos (below + 16) size 13 color "#8A6B76"
                if photos:
                    textbutton "최근 사진 다시 보기":
                        id "phone_archive_photo"
                        xpos 20 ypos (below + 44) style "phone_side_button"
                        action [Function(phone_note_photo, photos[-1]), Show("office_phone_photo", media=photos[-1])]
            elif selected != phone_active_contact:
                text (phone_names(phone_active_contact) + " 대화가 기다리고 있어요.") xpos 22 ypos (below + 16) size 14 xmaximum 340 color "#8A6B76"
                textbutton "진행 중인 대화로 돌아가기" xpos 20 ypos (below + 44) action SetLocalVariable("selected", phone_active_contact) style "phone_send_button"
            elif waiting:
                frame:
                    xpos 18 ypos (below + 22) xsize 232 ysize 42 padding (16, 0)
                    background silk("flat", "#F3ECEE", 21)
                    text (phone_names(phone_active_contact) + " 님이 입력 중…") size 14 color "#8A6B76" yalign 0.5
                textbutton "바로 보기" id "phone_next" xanchor 1.0 xpos 370 ypos (below + 20) action Return("next") style "phone_send_button"
            elif replies:
                text "답장 고르기" xpos 22 ypos (below + 10) size 13 color "#B3123F" font "fonts/Jua-Regular.ttf"
                viewport:
                    id "phone_replies"
                    xpos 18 ypos (below + 34) xsize 346 ysize 170
                    mousewheel True draggable True arrowkeys True
                    vbox:
                        xsize 344 spacing 6
                        for value, caption in replies:
                            textbutton caption:
                                id ("phone_reply_" + value)
                                action Return(value)
                                style "phone_reply_button"
                vbar value YScrollValue("phone_replies") style "office_scrollbar" xpos 372 ypos (below + 34) ysize 170
            else:
                frame:
                    xpos 18 ypos (below + 22) xsize 232 ysize 42 padding (16, 0)
                    background silk("flat", "#F3ECEE", 21)
                    text "눌러서 다음 메시지" size 14 color "#A3959B" yalign 0.5
                textbutton "다음 ▸" id "phone_next" xanchor 1.0 xpos 370 ypos (below + 20) action Return("next") style "phone_send_button"
            add silk("flat", "#1B0F16", 2) xalign 0.5 ypos 651 xysize (110, 4)

    vbox:
        xpos 862 ypos 470 spacing 8
        if not archive:
            textbutton "되돌리기" action Rollback() style "phone_side_button"
        textbutton "저장" action ShowMenu("save") style "phone_side_button"
        textbutton "불러오기" action ShowMenu("load") style "phone_side_button"
        textbutton "설정" action ShowMenu("preferences") style "phone_side_button"

screen window_phone_avatar(diameter, left=0, top=0, contact=None):
    # 승인된 프로필 그림이 생기기 전까지는 인물 색 동그라미에 이름 첫 글자.
    $ avatar_name = phone_names(contact) if contact else ""
    fixed:
        xpos left ypos top
        xysize (diameter, diameter)
        add silk("flat", (silk_tag_color(avatar_name) if contact else "#C1CFDB"), diameter // 2) xysize (diameter, diameter)
        if contact:
            text avatar_name[1:2] font "fonts/Jua-Regular.ttf" size int(diameter * 0.5) color "#FFFDFB" xalign 0.5 yalign 0.5 outlines []

screen office_phone_photo(media):
    style_prefix "phone"
    modal True
    zorder 150
    key "game_menu" action Hide("office_phone_photo")
    add Solid("#292326ed")
    frame:
        xalign 0.5 yalign 0.5 xsize 880 ysize 604 padding (28, 24)
        background Solid("#f0ebe2")
        vbox:
            spacing 14
            text PHONE_MEDIA[media]["title"] size 24 color "#69424b"
            fixed:
                xsize 824 ysize 442
                if phone_media_ready(media):
                    add Transform(PHONE_MEDIA[media]["path"], xysize=(824, 442), fit="contain") xalign 0.5 yalign 0.5
                else:
                    add Solid("#e5dcd1")
                    vbox:
                        xalign 0.5 yalign 0.5 spacing 16
                        text "사진 준비 중" size 34 xalign 0.5 color "#69424b"
                        text "실제 이미지가 들어오면 이 자리에서 확대됩니다." size 21 color "#62545c"
                        text "빈 자리는 사진 감상 완료로 기록하지 않습니다." size 17 color "#62545c"
            textbutton "대화로 돌아가기" id "phone_photo_close" action Hide("office_phone_photo") text_size 20 xalign 0.5

label phone_deliver(mid, sender, body, media=None, important=False, contact="ria"):
    $ phone_active_contact = contact
    if important and persistent.phone_typing_enabled and not getattr(_preferences, "reduced_motion", False) and not renpy.is_skipping():
        call screen office_phone(waiting=True)
    $ phone_add(mid, sender, body, media, contact)
    $ silk_sfx("phone")
    $ silk_phone_fresh_now = silk_phone_fresh()
    call screen office_phone
    $ silk_phone_mark()
    return

label ria_r08_phone_conversation:
    $ progression_enter("ria_r08_phone_conversation")
    $ progression_checkpoint("ria_r08_phone_conversation")
    $ phone_context = "r08_start"
    if memory.get("ria_r07_intimacy") != "shared":
        call phone_deliver("r08_morning_1", "ria", ri("일어났어? 나는 빵 먹는 중~ 오늘 추천 코스는 식탁!", "일어나셨어요? 저는 빵 먹는 중이에요~ 오늘 추천 코스는 식탁!"))
        call phone_deliver("r08_morning_2", "dohyun", ri("나도 이제 아침 먹으려고. 어제 차 잘 마셨어.", "저도 이제 아침 먹으려고요. 어제 차 잘 마셨어요."))
        call phone_deliver("r08_morning_3", "ria", ri("응! 별일은 없는데 그냥 네 생각 나서. 오늘은 내가 선빵~", "네! 별일은 없는데 그냥 도현 씨 생각 나서요. 오늘은 제가 선빵~"))
    if memory.get("ria_r07_intimacy") == "shared":
        call phone_deliver("r08_photo", "ria", ri("아침 사진 이제야 보내네~ 잘 구운 쪽 줬으니까 다음엔 네가 골라 줘!", "아침 사진 이제야 보내네요~ 잘 구운 쪽 드렸으니까 다음엔 도현 씨가 골라 주세요!"), media="ria_r08_breakfast")
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
        call phone_deliver("r08_answer", "ria", ri("잠깐만, 방금 그거 세 번 읽었어. 네가 이렇게 나오면 나 뭐라고 보내?", "잠깐만요, 방금 그거 세 번 읽었어요. 이렇게 나오시면 저 뭐라고 보내요?"), important=True)
        call phone_deliver("r08_followup", "dohyun", ri("답은 나중에 해도 돼. 그냥 말하고 싶었어.", "답은 나중에 하셔도 돼요. 그냥 말하고 싶었어요."))
        call phone_deliver("r08_answer_2", "ria", ri("응. 나도 보고 싶어. 이건 지금 답할래 :)", "네. 저도 보고 싶어요. 이건 지금 답할래요 :)"), important=True)
    elif memory["ria_r08_reply"] == "evening":
        call phone_deliver("r08_reply", "dohyun", ri("기록 좀 정리하려고. 저녁에 끝나면 얘기할래?", "기록 좀 정리하려고요. 저녁에 끝나면 얘기하실래요?"))
        call phone_deliver("r08_answer", "ria", ri("좋아. 나는 빨래 산부터 넘을게. 이쪽도 꽤 큰 작업이야~", "좋아요. 저는 빨래 산부터 넘을게요. 이쪽도 꽤 큰 작업이에요~"))
        call phone_deliver("r08_followup", "dohyun", ri("빨리 끝난 사람이 전화하기. 빨래 다 개야 끝난 거다?", "빨리 끝난 사람이 전화해요. 빨래 다 개셔야 끝난 거예요."))
        call phone_deliver("r08_answer_2", "ria", ri("치사해. 그럼 넌 책상까지 치워야 끝이야~ 이따 전화해!", "치사해요. 그럼 도현 씨도 책상까지 치우셔야 돼요~ 이따 전화해요!"), important=True)
    else:
        $ remember("choice_third_r08_reply")
        call phone_deliver("r08_reply", "dohyun", ri("어제 나란히 앉아 있던 거 생각났어. 별말 안 해도 좋더라.", "어제 나란히 앉아 있던 거 생각났어요. 별말 안 해도 좋더라고요."))
        call phone_deliver("r08_answer", "ria", ri("나도! 사실 조용해질 때 무슨 얘기할지 찾고 있었는데~", "저도요! 사실 조용해질 때 무슨 얘기할지 찾고 있었는데요~"))
        call phone_deliver("r08_followup", "dohyun", ri("나도 컵만 봤어. 눈 마주치면 무슨 말 할지 까먹을 것 같아서.", "저도 컵만 봤어요. 눈 마주치면 무슨 말 할지 까먹을 것 같아서요."))
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
    call phone_deliver("ria_disclosure_3", "seoyun", "리아야, 데이트 일정까지 캠페인처럼 빡빡하게 짜진 말고. 도현 씨도 즐거운 저녁 보내요 :)", contact="seoyun")
    call phone_deliver("ria_disclosure_4", "dohyun", "서윤 씨, 감사합니다. 오늘은 저녁만 같이 만들려고요.", contact="seoyun")
    $ phone_active_contact = "ria"
    return
