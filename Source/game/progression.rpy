# Optional systems candidate. Existing story gates, trust_ria and save signing remain.
default progression_state = {"schema": 1, "bonus": {"ria": 0, "jihyun": 0, "yujin": 0, "seoyun": 0}, "ledger": [], "visited": [], "current": None}
default progression_checkpoint_warning = False
default persistent.progression_seen_nodes = []
default persistent.progression_seen_assets = []
default persistent.progression_endings = []
default persistent.progression_replays = []
default persistent.progression_checkpoints = {}
default persistent.progression_checkpoint_enabled = True
default persistent.progression_show_numbers = True

init -10 python:
    import json
    import progression_model as pm
    with renpy.file("progression_nodes.json") as progression_nodes_file:
        PROGRESSION_NODES = json.load(progression_nodes_file)
    PROGRESSION_BUILD = "d1f212f-seoyun-v002"
    PROGRESSION_NODE_MAP = {row["id"]: row for row in PROGRESSION_NODES}
    PROGRESSION_CATALOG = []
    PROGRESSION_SPRITES = {}
    for field in ("progression_seen_nodes", "progression_seen_assets", "progression_endings", "progression_replays"):
        renpy.register_persistent(field, pm.merge_unlocked)

init 10 python:
    PROGRESSION_CATALOG = pm.asset_catalog(event_cg_plan)

    def progression_in_replay():
        return bool(getattr(renpy.store, "_in_replay", None))

    def progression_relation(who):
        return pm.relation_value(memory, progression_state, who)

    def progression_apply(choice_id, who, affection_delta=0, relation_delta=0):
        if progression_in_replay():
            return
        state, points = pm.apply_choice(progression_state, affinity, choice_id, who, affection_delta, relation_delta)
        renpy.store.progression_state = state
        renpy.store.affinity = points

    def progression_enter(node_id):
        if progression_in_replay() or node_id not in PROGRESSION_NODE_MAP:
            return
        who = PROGRESSION_NODE_MAP[node_id]["heroine"]
        if who != "common" and active_route != who:
            return
        if who != "common" and not dating and any(("_r" + str(n).zfill(2)) in node_id for n in range(5, 17)):
            return
        renpy.store.progression_state = pm.visit(progression_state, node_id)
        persistent.progression_seen_nodes = pm.merge_unlocked(persistent.progression_seen_nodes, [node_id], [])

    def progression_checkpoint(node_id):
        # Full native engine save, not a hand-maintained subset of variables.
        # One fixed reserved slot per known node, never manual save slots 1..4.
        if (progression_in_replay() or not persistent.progression_checkpoint_enabled
                or node_id not in PROGRESSION_NODE_MAP or renpy.in_rollback()
                or progression_state.get("current") != node_id):
            return
        slot = "flow-" + node_id
        try:
            renpy.save(slot, extra_info="스토리 기록 · " + node_id,
                       extra_json={"progression_build": PROGRESSION_BUILD, "node": node_id})
        except Exception:
            # Failure must not interrupt the story or publish a broken checkpoint.
            if not progression_checkpoint_warning:
                renpy.notify("스토리 기록 저장 실패 · 일반 저장은 별도로 이용해 주세요.")
                renpy.store.progression_checkpoint_warning = True
            return
        marks = dict(persistent.progression_checkpoints or {})
        marks[node_id] = PROGRESSION_BUILD
        persistent.progression_checkpoints = marks

    def progression_loadable(node_id):
        if node_id not in PROGRESSION_NODE_MAP:
            return False
        if (persistent.progression_checkpoints or {}).get(node_id) != PROGRESSION_BUILD:
            return False
        return renpy.can_load("flow-" + node_id)

    def progression_note_ending():
        if progression_in_replay():
            return
        if ending in pm.ENDINGS:
            persistent.progression_endings = pm.merge_unlocked(persistent.progression_endings, [ending], [])

    def progression_ending_ids():
        result = list(persistent.progression_endings or [])
        legacy = {"colleague": "local_colleague_ending", "ria_good": "local_ria_ending", "jihyun_good": "local_jihyun_ending", "yujin_good": "local_yujin_ending", "seoyun_good": "local_seoyun_ending"}
        for ending_id, field in legacy.items():
            if getattr(persistent, field, False):
                result = pm.merge_unlocked(result, [ending_id], [])
        return result

    def progression_observe_cut(event_id, variant, cursor):
        if progression_in_replay():
            return
        page = event_pages(event_id, variant)[cursor]
        if page["kind"] == "main":
            resolved = event_resolve_cg(event_id, variant, page["asset_id"])
        else:
            expression = page["kind"] == "intro" and cursor == 2 and event_intro_expression_ready
            resolved = event_intro_asset(event_id, variant, expression)
        if resolved["path"]:
            persistent.progression_seen_assets = pm.observed_asset(
                persistent.progression_seen_assets, PROGRESSION_CATALOG,
                resolved["displayed_id"], resolved["path"],
                renpy.loadable(resolved["path"]))
        if page["kind"] == "after":
            key = event_id + ":" + variant
            persistent.progression_replays = pm.merge_unlocked(persistent.progression_replays, [key], [])

    def progression_gallery_rows(who, category):
        return [row for row in PROGRESSION_CATALOG
                if row["heroine"] == who and (category == "all" or row["category"] == category
                or (category == "special" and row["category"] == "adult" and row["stage"] == "special"))]

    def progression_asset_ready(row):
        return renpy.loadable(row["path"])

    def progression_asset_unlocked(row):
        return row["id"] in persistent.progression_seen_assets and progression_asset_ready(row)

    def progression_collection(who, category):
        rows = progression_gallery_rows(who, category)
        ready = [row["id"] for row in rows if progression_asset_ready(row)]
        return pm.collection(rows, persistent.progression_seen_assets, ready)

    def progression_route_progress(who):
        ids = [row["id"] for row in PROGRESSION_NODES if row["heroine"] == who and row["kind"] == "event"]
        return (sum(node in progression_state.get("visited", []) for node in ids), sum(node in persistent.progression_seen_nodes for node in ids), len(ids))

    def progression_replay_ready(event_id, variant):
        key = event_id + ":" + variant
        return key in persistent.progression_replays and key in event_cg_sets

    def progression_replay_scope(event_id, variant):
        return {"progression_replay_id": event_id, "progression_replay_variant": variant,
                "event_presentations": {}, "event_cut_active": False,
                "event_cut_cursor": 0, "event_intro_expression_ready": False,
                "event_main_reached": False, "speech_informal": speech_informal}

    def progression_after_load():
        updated = pm.migrate_state(progression_state)
        if updated != progression_state:
            renpy.store.progression_state = updated
            renpy.block_rollback()
        if (active_route == "seoyun" and not seoyun_revision_notice_shown
                and (memory.get("seoyun_marriage_revealed")
                     or memory.get("seoyun_marriage_state") == "married_cohabiting")):
            renpy.notify("서윤의 설정과 후반 이야기가 변경됐습니다. 새 흐름은 R02부터 읽어 주세요.")
            renpy.store.seoyun_revision_notice_shown = True
        # No CG or ending inference from affinity or legacy local_* flags.

    config.after_load_callbacks.append(progression_after_load)

label progression_replay_event:
    if progression_replay_ready(progression_replay_id, progression_replay_variant):
        call event_sequence(progression_replay_id, progression_replay_variant)
    $ renpy.end_replay()
    return

screen progression_hub():
    tag menu
    default tab = "relations"
    default person = "ria"
    default category = "all"
    add Solid("#f6f1f5")
    frame:
        xpos 32 ypos 24 xsize 1216 ysize 672 padding (24, 20)
        background Solid("#fffafc")
        vbox:
            spacing 12
            hbox:
                spacing 18
                text "우리의 기록" size 32 color "#6d4162"
                textbutton "관계" action SetScreenVariable("tab", "relations")
                textbutton "이야기" action SetScreenVariable("tab", "story")
                textbutton "CG · 회상" action SetScreenVariable("tab", "gallery")
                textbutton "결말" action SetScreenVariable("tab", "endings")
                textbutton "돌아가기" action Return()
            hbox:
                spacing 10
                for who in pm.HEROES:
                    textbutton phone_names(who) action SetScreenVariable("person", who) selected person == who
            if tab == "relations":
                text (phone_names(person) + " · " + pm.STAT_NAMES[person]) size 27 color "#765784"
                if main_menu:
                    text "관계 상태는 게임을 진행하거나 저장을 불러온 뒤 확인할 수 있어요." size 22
                else:
                    if persistent.progression_show_numbers:
                        text ("호감도 " + str(affinity.get(person, 0)) + " / 100") size 25
                        text (pm.STAT_NAMES[person] + " " + str(progression_relation(person)) + " / 100") size 25
                    else:
                        text ("연인 관계" if dating and active_route == person else "서로 알아 가는 중") size 25
                        text (pm.STAT_NAMES[person] + " · " + pm.relation_phase(progression_relation(person))) size 22
                    $ current_count, total_count, route_count = progression_route_progress(person)
                    text ("이 회차 " + str(current_count) + " / " + str(route_count) + "장면 · 전체 방문 " + str(total_count)) size 18
                    text "함께 나눈 말과 실제 행동을 바탕으로 한 관계 기록이에요." size 18 color "#8a7987"
                    text "취향·의상·공개 여부·친밀한 장면을 미루는 선택에는 정답이 없어요." size 18 color "#8a7987"
                    if person == "seoyun" and memory.get("seoyun_marriage_revealed"):
                        text "알게 된 사실과 지금의 선택을 기록해요. 신뢰 회복이나 미래 약속을 뜻하지 않아요." size 19 xmaximum 1100
                textbutton "정확한 관계 수치 표시" action ToggleField(persistent, "progression_show_numbers") selected persistent.progression_show_numbers
                textbutton "이야기 재진입용 자동 기록" action ToggleField(persistent, "progression_checkpoint_enabled") selected persistent.progression_checkpoint_enabled
                text "자동 기록은 노드마다 최근 한 개를 보관해요. 수동 저장 슬롯과 별개예요." size 17 color "#8a7987"
            elif tab == "story":
                text "공통 이야기 → 개인 루트 · 선택 이전 기록으로 돌아가기" size 23 color "#765784"
                text "미발견 제목은 숨겨져요. 돌아가면 그 시점의 상태 전체를 불러와요." size 17
                viewport:
                    xsize 1140 ysize 410 mousewheel True draggable True scrollbars "vertical"
                    vbox:
                        spacing 6
                        for node in PROGRESSION_NODES:
                            if node["heroine"] in ("common", person) and node["kind"] in ("event", "choice"):
                                $ discovered = node["id"] in persistent.progression_seen_nodes
                                $ restorable = discovered and progression_loadable(node["id"])
                                textbutton (("    └ " if node["kind"] == "choice" else "→ ") + node["title"] if discovered else "잠김 · 아직 만나지 않은 이야기"):
                                    xsize 1090 text_size 18
                                    action FileLoad("flow-" + node["id"], confirm=True, slot=True)
                                    sensitive restorable
                                if discovered and not restorable:
                                    text "방문 기록만 있어요 · 이 버전의 재진입 저장 없음" size 14 color "#9b8c98"
            elif tab == "gallery":
                hbox:
                    spacing 9
                    textbutton "전체" action SetScreenVariable("category", "all")
                    textbutton "일반" action SetScreenVariable("category", "general")
                    textbutton "연애" action SetScreenVariable("category", "romance")
                    textbutton "성인" action SetScreenVariable("category", "adult")
                    textbutton "특별" action SetScreenVariable("category", "special")
                    textbutton "엔딩" action SetScreenVariable("category", "ending")
                $ summary = progression_collection(person, category)
                text ("감상 " + str(summary["seen"]) + " / 등록 " + str(summary["available"]) + " · 계획 " + str(summary["planned"])) size 20
                text (("수집률 " + str(summary["percent"]) + "%") if summary["percent"] is not None else "등록된 이미지가 아직 없어요. 빈 자리는 해금되지 않아요.") size 18
                viewport:
                    xsize 1140 ysize 300 mousewheel True draggable True scrollbars "vertical"
                    vpgrid:
                        cols 4 spacing 12
                        for row in progression_gallery_rows(person, category):
                            button:
                                xsize 260 ysize 112 padding (8, 6)
                                action Show("progression_cg_view", asset_id=row["id"])
                                sensitive progression_asset_unlocked(row)
                                vbox:
                                    spacing 5
                                    if progression_asset_unlocked(row):
                                        add row["path"] xysize (240, 72) fit "contain"
                                        text (row["event_id"].upper() + " · " + row["outfit"]) size 14
                                    else:
                                        text ("아직 미감상" if progression_asset_ready(row) else "이미지 준비 중") size 18
                hbox:
                    spacing 8
                    for key in persistent.progression_replays:
                        if key.split(":")[0].startswith(person + "_"):
                            $ eid, outfit = key.split(":")
                            textbutton (eid.upper() + " · " + outfit):
                                text_size 14
                                action Replay("progression_replay_event", scope=progression_replay_scope(eid, outfit), locked=not progression_replay_ready(eid, outfit))
            else:
                text "확인한 결말 · 기존 시나리오 기준" size 24 color "#765784"
                text (str(len(progression_ending_ids())) + " / " + str(len(pm.ENDINGS))) size 20
                for ending_id, info in pm.ENDINGS.items():
                    if info[0] in ("common", person):
                        text (info[1] if ending_id in progression_ending_ids() else "잠김 · 아직 확인하지 않은 결말") size 23
                text "새 진엔딩이나 12개 결말을 추가한 상태가 아니에요." size 17 color "#8a7987"

screen progression_cg_view(asset_id):
    modal True
    zorder 180
    $ row = next((item for item in PROGRESSION_CATALOG if item["id"] == asset_id), None)
    add Solid("#241d2bea")
    if row and progression_asset_unlocked(row):
        add row["path"] xysize (1180, 620) fit "contain" xalign 0.5 yalign 0.5
    else:
        text "아직 감상하지 않은 이미지예요." xalign 0.5 yalign 0.5
    textbutton "돌아가기" xpos 1040 ypos 650 action Hide("progression_cg_view")
    key "game_menu" action Hide("progression_cg_view")

screen progression_shortcuts():
    if not main_menu and not event_cut_active and not cream_menu_open() and not cream_preview_active and not renpy.get_screen("office_phone") and not renpy.get_screen("office_phone_archive") and not progression_in_replay():
        hbox:
            xpos 28 ypos 112 spacing 8
            textbutton "우리의 기록" action ShowMenu("progression_hub") text_size 16 padding (12, 7)
            textbutton "퀵저장" action QuickSave() text_size 16 padding (12, 7)
            textbutton "퀵로드" action QuickLoad(confirm=True) text_size 16 padding (12, 7)

init python:
    config.overlay_screens.append("progression_shortcuts")


