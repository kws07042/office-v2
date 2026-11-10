# Generic media slots. No character art or explicit dialogue is supplied.
init python:
    import json
    with renpy.file("event_cg_plan.json") as cg_plan_file:
        event_cg_plan = json.load(cg_plan_file)
    event_cg_sets = {s["heroine"] + "_" + s["event"].lower() + ":" + s["outfit"]: s for s in event_cg_plan["sets"]}

    def event_pages(event_id, variant):
        group = event_cg_sets[event_id + ":" + variant]
        if not group["runtime_connected"]:
            raise Exception("This personal route is not implemented.")
        pages = [{"kind": "intro", "part_index": i + 1, "part_count": 3, "story_index": i} for i in range(3)]
        pages += [{"kind": "main", "part_index": i + 1, "part_count": 3, "story_index": None, "asset_id": a["id"]} for i, a in enumerate(group["base_cg"])]
        return pages + [{"kind": "after", "part_index": 1, "part_count": 1, "story_index": 3}]

    def event_resolve_cg(event_id, variant, asset_id):
        group = event_cg_sets[event_id + ":" + variant]
        originals = {a["id"]: a for a in group["base_cg"] + [group["intro_cg"]]}
        expression = group["intro_expression"]
        requested = expression if asset_id == expression["id"] else originals[asset_id]
        base_id = requested.get("base_id", asset_id)
        base = originals[base_id]
        base_ids = [a["id"] for a in group["base_cg"]]
        result = {"requested_id": asset_id, "base_id": base_id, "base_index": base_ids.index(base_id) + 1 if base_id in base_ids else 0, "is_expression": asset_id == expression["id"], "requested_path": requested["planned_path"], "displayed_id": None, "path": None, "fallback": False}
        if renpy.loadable(requested["planned_path"]):
            result.update(displayed_id=asset_id, path=requested["planned_path"])
        elif result["is_expression"] and renpy.loadable(base["planned_path"]):
            result.update(displayed_id=base_id, path=base["planned_path"], fallback=True)
        return result

    def event_intro_asset(event_id, variant, expression=False):
        group = event_cg_sets[event_id + ":" + variant]
        return event_resolve_cg(event_id, variant, group["intro_expression" if expression else "intro_cg"]["id"])

    def event_record_current(event_id, variant, cursor):
        key = event_id + ":" + variant
        page = event_pages(event_id, variant)[cursor]
        previous = renpy.store.event_presentations.get(key, {})
        if previous.get("layout_version") != 3:
            previous = {"layout_version": 3}
        current = dict(previous)
        for name in ("loaded_images", "main_frames_seen", "base_slots_seen", "loaded_asset_ids", "missing_asset_ids"):
            current[name] = list(previous.get(name, []))
        current["visited_slots"] = sorted(set(previous.get("visited_slots", []) + [cursor + 1]))
        if page["kind"] == "main":
            resolved = event_resolve_cg(event_id, variant, page["asset_id"])
            current["main_frames_seen"] = sorted(set(current["main_frames_seen"] + [page["part_index"]]))
            current["base_slots_seen"] = sorted(set(current["base_slots_seen"] + [resolved["base_index"]]))
        else:
            expression = page["kind"] == "intro" and cursor == 2 and renpy.store.event_intro_expression_ready
            resolved = event_intro_asset(event_id, variant, expression)
        if resolved["path"]:
            current["loaded_images"] = sorted(set(current["loaded_images"] + [cursor + 1]))
            current["loaded_asset_ids"] = sorted(set(current["loaded_asset_ids"] + [resolved["displayed_id"]]))
        missing = set(current["missing_asset_ids"])
        if resolved["displayed_id"] == resolved["requested_id"]:
            missing.discard(resolved["requested_id"])
        else:
            missing.add(resolved["requested_id"])
        current["missing_asset_ids"] = sorted(missing)
        renpy.store.event_presentations = dict(renpy.store.event_presentations, **{key: current})

    def event_show_intro_expression(event_id, variant, cursor):
        renpy.retain_after_load()
        renpy.store.event_intro_expression_ready = True
        event_record_current(event_id, variant, cursor)

screen event_main_panel(event_id, variant, page):
    style_prefix "event"
    $ resolved = event_resolve_cg(event_id, variant, page["asset_id"])
    $ cg_caption = "CG " + str(resolved["base_index"]) + " / 3"
    if resolved["path"]:
        add resolved["path"] xpos 60 ypos 174 xysize (1160, 405) fit "contain"
        frame:
            xpos 60 ypos 174 padding (15, 10) background Solid("#211a29e8")
            text cg_caption size 22
    else:
        frame:
            xpos 60 ypos 174 xsize 1160 ysize 405 padding (30, 25) background Solid("#382b3b")
            vbox:
                spacing 22
                text cg_caption size 34 color "#f3bca9"
                text "이미지 준비 중" size 28
                text "그림이 등록되면 이 자리에 표시됩니다." size 24 color "#e4cfc9"
                text "현재는 화면 이동을 확인하는 개발용 자리입니다." size 21 color "#e4cfc9"
