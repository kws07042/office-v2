default event_cut_active = False
default event_cut_cursor = 0
default event_presentations = {}
default event_intro_expression_ready = False
default event_main_reached = False
default event_line = 0
# 검사에서는 본장면 대사를 한 줄씩 넘기지 않는다(기존 컷 이동 검사 유지). 대사 검사는 이 값을 켠다.
default event_text_in_test = False

init python:
    # R15 코스프레: 공통 두 벌(바니걸·간호사) + 히로인 전용 한 벌(리아 치어리더, 지현 차이나드레스, 유진 메이드, 서윤 여경찰)
    COSTUME_NAMES = {"bunny": "바니걸", "nurse": "간호사", "cheer": "치어리더", "qipao": "차이나드레스", "maid": "메이드", "police": "여경찰"}
    import json
    with renpy.file("event_assets.json") as event_manifest_file:
        event_assets = json.load(event_manifest_file)
    with renpy.file("event_story.json") as event_story_file:
        event_story = json.load(event_story_file)
    # 본장면(CG1~3) 대사: Docs/adult/grok-adult-scenes-v003b.json을 그대로 복사한 파일.
    # 리아 장면은 [반말, 존댓말] 두 벌, '도현'은 화면에 나갈 때 플레이어 이름으로 바뀐다.
    with renpy.file("event_main_text.json") as event_main_file:
        event_main_text = {s["id"]: s for s in json.load(event_main_file)}

    def event_main_key(event_id, variant):
        if variant == "cosplay":
            return "%s:cosplay:%s" % (event_id, renpy.store.memory.get(event_id.split("_")[0] + "_r15_costume"))
        return event_id + ":" + variant

    def event_main_lines(event_id, variant, page):
        if page["kind"] != "main":
            return []
        if renpy.is_in_test() and not renpy.store.event_text_in_test:
            return []
        scene = event_main_text.get(event_main_key(event_id, variant))
        if not scene or page["part_index"] > len(scene["main"]):
            return []
        return scene["main"][page["part_index"] - 1]["lines"]

    def event_play_text_scene(key, heroine):
        """대본 안에서 이어지는 본장면(리아 모텔): 대사창으로 한 줄씩 보여 준다."""
        if renpy.is_in_test() and not renpy.store.event_text_in_test:
            return
        scene = event_main_text.get(key)
        if not scene:
            return
        for part in scene["main"]:
            for kind, value in part["lines"]:
                who = {"heroine": heroine, "dohyun": renpy.store.d}.get(kind)
                renpy.say(who, event_line_text(value).replace("[", "[["))

    def event_line_text(value):
        # JSON 목록은 Ren'Py의 list(되돌리기용)와 다른 형이라 문자열 여부로 가른다.
        return value if isinstance(value, str) else ri(*value)

    def event_finish(event_id, variant, status):
        key = event_id + ":" + variant
        previous = event_presentations.get(key, {})
        renpy.store.event_presentations = dict(event_presentations, **{key: dict(previous, status=status)})

label event_sequence(event_id, variant):
    $ dialogue_cg_begin()
    $ event_cut_cursor = 0
    $ event_cut_active = True
    $ event_line = 0
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
            $ event_line = max(0, len(event_main_lines(event_id, variant, event_pages(event_id, variant)[event_cut_cursor])) - 1)
        else:
            $ event_cut_cursor += 1
            $ event_line = 0
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
    $ after_path = event_after_path(event_id, variant) if page["kind"] == "after" else None
    if after_path:
        $ resolved = dict(resolved or {}, path=after_path)
    $ has_art = bool(resolved and resolved["path"])
    $ part_name = {"intro": "도입", "main": "본장면", "after": "이후 대화"}[page["kind"]]
    $ outfit_name = {"casual": "익숙한 사복", "special": "특별한 날의 옷", "home": "편한 생활복", "cosplay": "선택한 특별 의상"}[variant]
    if variant == "cosplay":
        $ outfit_name = COSTUME_NAMES.get(memory.get(event_id.split("_")[0] + "_r15_costume"), outfit_name)
    if page["kind"] == "intro" and cursor == 2 and not event_intro_expression_ready:
        timer 0.65 action Function(event_show_intro_expression, event_id, variant, cursor)
    add Solid("#292326")
    if page["kind"] == "main" and not event_resolve_cg(event_id, variant, page["asset_id"])["path"]:
        $ backdrop = event_after_path(event_id, variant) or event_intro_asset(event_id, variant)["path"]
        if backdrop:
            add Transform(backdrop, xysize=(1280, 720), blur=28, matrixcolor=BrightnessMatrix(-0.32) * SaturationMatrix(0.7))
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
    $ mlines = event_main_lines(event_id, variant, page)
    $ line_i = min(event_line, len(mlines) - 1) if mlines else 0
    $ next_action = SetVariable("event_line", line_i + 1) if mlines and line_i < len(mlines) - 1 else Return("next")
    $ prev_action = SetVariable("event_line", line_i - 1) if mlines and line_i > 0 else (Return("previous") if cursor > 0 else NullAction())
    if page["kind"] == "main":
        use event_main_panel(event_id, variant, page)
    if mlines:
        $ kind, value = mlines[line_i]
        frame:
            id "event_main_line"
            xpos 60 ypos 430 xsize 1160 ysize 150 padding (28, 16)
            background Solid("#120c10e0")
            vbox:
                spacing 8
                if kind == "narration":
                    text event_line_text(value) size 23 color "#e4cfc9" italic True substitute False
                else:
                    text (phone_names(event_id.split("_")[0]) if kind == "heroine" else "도현") size 22 color ("#f3a7bb" if kind == "heroine" else "#a9c8f0") substitute False
                    text event_line_text(value) size 26 color "#FFFFFF" substitute False
            text (str(line_i + 1) + " / " + str(len(mlines))) size 16 color "#b9a5aa" xalign 1.0 yalign 1.0
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
        textbutton ("이전 대사" if line_i > 0 else "이전 컷") id "cut_previous" action prev_action sensitive (cursor > 0 or line_i > 0) text_size 23
        textbutton ("다음 대사" if mlines and line_i < len(mlines) - 1 else ("다음 컷" if cursor < len(pages) - 1 else "장면 마치기")):
            id "cut_next"
            action next_action
            text_size 23
        textbutton "연출 건너뛰기" id "cut_skip" action Return("skip") text_size 23
    text "좌우 화살표로 이동 · Enter로 다음 · 위 메뉴에서 저장 가능" xpos 60 ypos 683 size 18 color "#cdb7b9"
    key "K_LEFT" action prev_action
    key "K_RIGHT" action next_action
    key "K_RETURN" action next_action
    key "K_SPACE" action next_action
