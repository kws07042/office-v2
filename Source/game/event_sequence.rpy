default event_cut_active = False
default event_cut_cursor = 0
default event_line_cursor = 0
default event_presentations = {}
default event_intro_expression_ready = False
default event_main_reached = False

init python:
    import json
    with renpy.file("event_assets.json") as event_manifest_file:
        event_assets = json.load(event_manifest_file)
    with renpy.file("event_story.json") as event_story_file:
        event_story = json.load(event_story_file)
    with renpy.file("ria_event_dialogue.json") as ria_event_dialogue_file:
        ria_event_dialogue = json.load(ria_event_dialogue_file)

    def event_dialogue_lines(event_id, variant, cursor):
        pages = ria_event_dialogue.get(event_id + ":" + variant)
        return pages[cursor] if pages else ()

    def event_finish(event_id, variant, status):
        key = event_id + ":" + variant
        previous = event_presentations.get(key, {})
        renpy.store.event_presentations = dict(event_presentations, **{key: dict(previous, status=status)})

label event_sequence(event_id, variant):
    $ event_cut_cursor = 0
    $ event_line_cursor = 0
    $ event_cut_active = True
    $ event_intro_expression_ready = False
    $ event_main_reached = False
    $ renpy.config.skipping = None
    while event_cut_cursor < len(event_pages(event_id, variant)):
        $ event_record_current(event_id, variant, event_cut_cursor)
        if event_pages(event_id, variant)[event_cut_cursor]["kind"] == "main":
            $ event_main_reached = True
        call screen event_cut(event_id, variant, event_cut_cursor)
        if _return == "skip":
            $ progression_observe_cut(event_id, variant, event_cut_cursor)
            $ event_finish(event_id, variant, "skipped_presentation")
            $ event_cut_cursor = len(event_pages(event_id, variant))
        elif _return == "previous":
            if event_line_cursor > 0:
                $ event_line_cursor -= 1
            elif event_cut_cursor > 0:
                $ progression_observe_cut(event_id, variant, event_cut_cursor)
                $ event_cut_cursor -= 1
                $ event_line_cursor = max(0, len(event_dialogue_lines(event_id, variant, event_cut_cursor)) - 1)
        elif event_line_cursor + 1 < len(event_dialogue_lines(event_id, variant, event_cut_cursor)):
            $ event_line_cursor += 1
        else:
            $ progression_observe_cut(event_id, variant, event_cut_cursor)
            $ event_line_cursor = 0
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
    $ lines = event_dialogue_lines(event_id, variant, cursor)
    $ line_index = min(event_line_cursor, len(lines) - 1) if lines else 0
    $ has_previous = cursor > 0 or line_index > 0
    $ has_next_line = line_index + 1 < len(lines)
    $ beat = event_story[event_id][variant][page["story_index"]] if page["story_index"] is not None else None
    $ expression = page["kind"] == "intro" and cursor == 2 and event_intro_expression_ready
    $ resolved = event_intro_asset(event_id, variant, expression) if beat else None
    $ has_art = bool(resolved and resolved["path"])
    $ part_name = {"intro": "도입", "main": "본장면", "after": "이후 대화"}[page["kind"]]
    $ outfit_name = {"casual": "익숙한 사복", "special": "특별한 날의 옷", "home": "편한 생활복", "cosplay": "선택한 특별 의상"}[variant]
    if page["kind"] == "intro" and cursor == 2 and not event_intro_expression_ready:
        timer 0.65 action Function(event_show_intro_expression, event_id, variant, cursor)
    add Solid("#151d30")
    text (event["title"] + "  ·  " + part_name + " " + str(page["part_index"]) + " / " + str(page["part_count"])):
        xpos 60 ypos 80 size 30 color "#f1c590"
    text outfit_name xpos 60 ypos 124 size 21 color "#bac4d8"
    if lines:
        $ dialogue_art = event_resolve_cg(event_id, variant, page["asset_id"]) if page["kind"] == "main" else resolved
        use event_dialogue_panel(lines[line_index], line_index, len(lines), dialogue_art["path"])
    elif page["kind"] == "main":
        use event_main_panel(event_id, variant, page)
    elif has_art:
        add resolved["path"] xpos 60 ypos 174 xysize (520, 405) fit "contain"
    if beat and not lines:
        frame:
            xpos (600 if has_art else 60) ypos 174 xsize (620 if has_art else 1160) ysize 405
            background Solid("#202a40") padding (30, 25)
            vbox:
                spacing 15
                text beat["title"] size 30 color "#e4c397" substitute False
                text beat["narration"] size 23 color "#bac4d8" substitute False
                text (phone_names(event_id.split("_")[0]) + "  " + (beat["heroine"] if "heroine" in beat else ri(*beat["ria"]))) size 26 substitute False
                text ("도현  " + ri(*beat["dohyun"])) size 26 substitute False
                if not has_art:
                    text ("표정 변화 자리 · 그림 준비 중" if expression else "장면 대본 미리보기 · 그림 준비 중") size 18 color "#8d9bb5"
    hbox:
        xpos 60 ypos 610 spacing 20
        textbutton ("이전 문장" if line_index else "이전 컷") id "cut_previous" action Return("previous") sensitive has_previous text_size 23
        textbutton ("계속" if has_next_line else "다음 컷" if cursor < len(pages) - 1 else "장면 마치기"):
            id "cut_next"
            action Return("next")
            text_size 23
        textbutton "연출 건너뛰기" id "cut_skip" action Return("skip") text_size 23
    text "좌우 화살표로 이동 · Enter로 다음 · 위 메뉴에서 저장 가능" xpos 60 ypos 683 size 18 color "#8d9bb5"
    key "K_LEFT" action (Return("previous") if has_previous else NullAction())
    key "K_RIGHT" action Return("next")
    key "K_RETURN" action Return("next")
    key "K_SPACE" action Return("next")

screen event_dialogue_panel(line, index, total, art_path):
    $ speaker, informal, formal = line
    $ shy_portrait = "images/characters/ria/portraits/shy.png"
    $ art_path = art_path or (shy_portrait if renpy.loadable(shy_portrait) else None)
    if art_path:
        frame:
            xpos 60 ypos 174 xsize 500 ysize 405
            background Solid("#202a40")
            add art_path xalign 0.5 yalign 1.0 xysize (480, 405) fit "contain"
    frame:
        xpos (584 if art_path else 60) ypos 174 xsize (636 if art_path else 1160) ysize 405
        background Solid("#202a40") padding (36, 30)
        text ("{:02d} / {:02d}".format(index + 1, total)) size 19 color "#bac4d8" xalign 1.0
        vbox:
            xfill True yalign 0.5 spacing 18
            if speaker:
                text speaker size 23 color "#f1c590" substitute False
            text ri(informal, formal) size (30 if speaker else 26) color ("#ffffff" if speaker else "#d5ddeb") substitute False
