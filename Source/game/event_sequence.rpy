default event_cut_active = False
default event_cut_cursor = 0
default event_presentations = {}
default event_intro_expression_ready = False
default event_main_reached = False

init python:
    # R15 코스프레: 공통 두 벌(바니걸·간호사) + 히로인 전용 한 벌(리아 치어리더, 지현 차이나드레스, 유진 메이드, 서윤 여경찰)
    COSTUME_NAMES = {"bunny": "바니걸", "nurse": "간호사", "cheer": "치어리더", "qipao": "차이나드레스", "maid": "메이드", "police": "여경찰"}
    import json
    with renpy.file("event_assets.json") as event_manifest_file:
        event_assets = json.load(event_manifest_file)
    with renpy.file("event_story.json") as event_story_file:
        event_story = json.load(event_story_file)

    def event_finish(event_id, variant, status):
        key = event_id + ":" + variant
        previous = event_presentations.get(key, {})
        renpy.store.event_presentations = dict(event_presentations, **{key: dict(previous, status=status)})

label event_sequence(event_id, variant):
    $ dialogue_cg_begin()
    $ event_cut_cursor = 0
    $ event_cut_active = True
    $ event_intro_expression_ready = False
    $ event_main_reached = False
    $ renpy.config.skipping = None
    while event_cut_cursor < len(event_pages(event_id, variant)):
        $ event_record_current(event_id, variant, event_cut_cursor)
        if event_pages(event_id, variant)[event_cut_cursor]["kind"] == "main":
            $ event_main_reached = True
        call screen event_cut(event_id, variant, event_cut_cursor)
        $ progression_observe_cut(event_id, variant, event_cut_cursor)
        if _return == "skip":
            $ event_finish(event_id, variant, "skipped_presentation")
            $ event_cut_cursor = len(event_pages(event_id, variant))
        elif _return == "previous":
            $ event_cut_cursor = max(0, event_cut_cursor - 1)
        else:
            $ event_cut_cursor += 1
            if event_cut_cursor == len(event_pages(event_id, variant)):
                $ event_finish(event_id, variant, "completed")
    $ event_cut_active = False
    return

screen event_cut(event_id, variant, cursor):
    style_prefix "event"
    modal True
    zorder 90
    $ event = event_assets[event_id]
    $ pages = event_pages(event_id, variant)
    $ page = pages[cursor]
    $ beat = event_story[event_id][variant][page["story_index"]] if page["story_index"] is not None else None
    $ expression = page["kind"] == "intro" and cursor == 2 and event_intro_expression_ready
    $ resolved = event_intro_asset(event_id, variant, expression) if beat else None
    $ has_art = bool(resolved and resolved["path"])
    $ part_name = {"intro": "도입", "main": "본장면", "after": "이후 대화"}[page["kind"]]
    $ outfit_name = {"casual": "익숙한 사복", "special": "특별한 날의 옷", "home": "편한 생활복", "cosplay": "선택한 특별 의상"}[variant]
    if variant == "cosplay":
        $ outfit_name = COSTUME_NAMES.get(memory.get(event_id.split("_")[0] + "_r15_costume"), outfit_name)
    if page["kind"] == "intro" and cursor == 2 and not event_intro_expression_ready:
        timer 0.65 action Function(event_show_intro_expression, event_id, variant, cursor)
    add Solid("#292326")
    $ full_art = has_art and page["kind"] != "main"
    if full_art:
        # 도입·이후 대화: 그림을 화면 가득, 글은 아래에 반투명 판으로 얹는다.
        add resolved["path"] xysize (1280, 720)
        add Solid("#120c10a8") xysize (1280, 280) ypos 440
        frame:
            xpos 40 ypos 26 padding (16, 8) background Solid("#120c10b0")
            hbox:
                spacing 14
                text (event["title"] + "  ·  " + part_name + " " + str(page["part_index"]) + " / " + str(page["part_count"])) size 20 color "#f0dccd" substitute False
                text outfit_name size 18 color "#e4cfc9" yalign 0.5
    else:
        text (event["title"] + "  ·  " + part_name + " " + str(page["part_index"]) + " / " + str(page["part_count"])):
            xpos 60 ypos 80 size 30 color "#e6cdb9"
        text outfit_name xpos 60 ypos 124 size 21 color "#e4cfc9"
    if page["kind"] == "main":
        use event_main_panel(event_id, variant, page)
    if beat:
        frame:
            xpos 60 ypos (454 if full_art else 174) xsize 1160 ysize (146 if full_art else 405)
            background (None if full_art else Solid("#382e34")) padding ((0, 0) if full_art else (30, 25))
            vbox:
                spacing (6 if full_art else 15)
                if not full_art:
                    text beat["title"] size 30 color "#e6cdb9" substitute False
                text beat["narration"] size (20 if full_art else 23) color "#e4cfc9" substitute False
                text (phone_names(event_id.split("_")[0]) + "  " + (beat["heroine"] if "heroine" in beat else ri(*beat["ria"]))) size (23 if full_art else 26) color "#FFFFFF" substitute False
                text ("도현  " + ri(*beat["dohyun"])) size (23 if full_art else 26) color "#FFFFFF" substitute False
                if not has_art:
                    text ("표정 변화 자리 · 그림 준비 중" if expression else "장면 대본 미리보기 · 그림 준비 중") size 18 color "#cdb7b9"
    hbox:
        xpos 60 ypos 610 spacing 20
        textbutton "이전 컷" id "cut_previous" action Return("previous") sensitive cursor > 0 text_size 23
        textbutton ("다음 컷" if cursor < len(pages) - 1 else "장면 마치기"):
            id "cut_next"
            action Return("next")
            text_size 23
        textbutton "연출 건너뛰기" id "cut_skip" action Return("skip") text_size 23
    text "좌우 화살표로 이동 · Enter로 다음 · 위 메뉴에서 저장 가능" xpos 60 ypos 683 size 18 color "#cdb7b9"
    key "K_LEFT" action (Return("previous") if cursor > 0 else NullAction())
    key "K_RIGHT" action Return("next")
    key "K_RETURN" action Return("next")
    key "K_SPACE" action Return("next")
