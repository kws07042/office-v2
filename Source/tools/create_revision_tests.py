from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]
G=P/'game'
changes=json.loads((P/'story/three_choice_changes_v1.json').read_text(encoding='utf-8'))
(G/'three_choice_cases.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2),encoding='utf-8')
source='''init python:
    import json
    with renpy.file("three_choice_cases.json") as choice_case_file:
        choice_cases = json.load(choice_case_file)
    choice_fixture = {}

    def choice_target_visible():
        screen = renpy.get_screen("choice")
        return screen and any(renpy.substitute(i.caption) == choice_case["new_option"][1:-2] for i in screen.scope["items"])

    def choice_first_caption():
        return renpy.substitute(renpy.get_screen("choice").scope["items"][0].caption)

label test_three_choice_entry:
    scene bg plain
    $ choice_case = choice_cases[choice_fixture["case"] // 2]
    $ speech_informal = bool(choice_fixture["case"] & 1)
    $ active_route = "ria"
    $ dating = choice_case["label"] != "ria_r04"
    $ affinity = {"ria": 0, "jihyun": 0, "yujin": 0, "seoyun": 0}
    $ completed = ["ria_R%02d" % i for i in range(1,17)]
    $ memory = {"ria_core_understanding": True, "ria_confession_accepted": True, "ria_conflict": "discussing" if choice_case["label"] == "ria_r14" else "resolved", "ria_r13_response": "cover", "ria_r15_future_agreed": True, "ria_route_completed": True, "ria_r12_next_appointment_status": "scheduled"}
    call expression choice_case["label"]
    $ remember("choice_test_returned")
    menu:
        "선택지 검사 종료":
            pass
    return

testsuite three_choice_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase every_new_choice_both_speech_styles:
        parameter case = list(range(64))
        $ choice_fixture["case"] = case
        run Start("test_three_choice_entry")
        advance until screen "choice"
'''
source+='''        if not eval choice_target_visible():
            click expression choice_first_caption() until not screen "choice"
            advance until screen "choice"
'''*4
source+='''        assert eval choice_target_visible()
        assert eval len(renpy.get_screen("choice").scope["items"]) == 3
        if eval case in (0, 16, 46):
            screenshot ("three-choice-" + str(case) + ".png")
        click expression choice_case["new_option"][1:-2] until not screen "choice"
        advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
        assert eval memory.get("choice_third_" + choice_case["key"]) is True
'''
source+='''        if not eval memory.get("choice_test_returned"):
            if screen "event_cut":
                click id "cut_skip" until not screen "event_cut"
                advance until screen "choice"
            if not eval memory.get("choice_test_returned"):
                click expression choice_first_caption() until not screen "choice"
                advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
'''*8
source+='''        assert eval memory.get("choice_test_returned") is True
        assert eval dating is True
        assert eval ending != "ria_relationship_closed"
        if eval choice_case["key"] in ("o01_offer", "o02_offer", "o03_offer"):
            assert eval memory["ria_" + choice_case["key"][:3] + "_status"] == "brief"
            assert eval "ria_" + choice_case["key"][:3].upper() not in completed
        if eval choice_case["key"] in ("r04_affection", "r06_affection"):
            assert eval first_kiss is False
        if eval choice_case["key"] in ("r07_pace", "r12_pace", "r15_pace"):
            assert eval memory["ria_" + choice_case["key"][:3] + "_intimacy"] == "deferred"
            assert eval event_presentations == {}
        if eval choice_case["key"] == "r14_relationship":
            assert eval memory["ria_conflict"] == "resolved"
            assert eval memory["ria_r14_action_confirmed"] is True

    teardown:
        exit
'''
(G/'three_choice_tests.rpy').write_text(source,encoding='utf-8')

# Update full-route expectations and add a route selecting the new alternatives.
generator=P/'tools/create_ria16_flow_tests.py'
s=generator.read_text(encoding='utf-8').replace('"no_epilogue", "cosplay"]','"no_epilogue", "cosplay", "third"]')
s=s.replace('("ria", "deferred", "no_epilogue", "cosplay")','("ria", "deferred", "no_epilogue", "cosplay", "third")')
s=s.replace('list(range(1, 11))','list(range(1, 8))').replace('== [1, 2, 3, 4, 5]','== [1, 2, 3]')
s=s.replace('Authored seven complete-flow cases.','Authored eight complete-flow cases.')
generator.write_text(s,encoding='utf-8')
path=G/'ria16_tests.rpy'
s=path.read_text(encoding='utf-8')
needle='        if route == "deferred":\n'
insert='''        if route == "third":
            new_options = {c["new_option"][1:-2] for c in choice_cases}
            for caption in captions:
                if caption in new_options:
                    return caption
'''
assert needle in s
path.write_text(s.replace(needle,insert+needle,1),encoding='utf-8')
exec(compile(generator.read_text(encoding='utf-8'),str(generator),'exec'),{'__file__':str(generator)})

# Keep historical focused tests, but author a new suite for the changed layout.
flow='''init python:
    layout_fixture = {}
    layout_variants = [("ria_r07", "casual"), ("ria_r12", "special"), ("ria_r15", "home"), ("ria_r15", "cosplay")]

label test_layout_entry:
    scene bg plain
    $ active_route = "ria"
    $ dating = True
    $ speech_informal = bool(layout_fixture.get("case", 0) & 1)
    $ layout_event, layout_variant = layout_variants[layout_fixture.get("case", 0) // 2]
    call event_sequence(layout_event, layout_variant)
    if not event_main_reached:
        "(장면 생략 · 시간이 흐릅니다.)"
        $ remember("layout_time_transition")
    menu:
        "화면 검사 종료":
            pass
    return

testsuite five_asset_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase four_sets_two_speech_styles:
        parameter case = list(range(8))
        $ layout_fixture["case"] = case
        run Start("test_layout_entry")
        advance until screen "event_cut"
        assert eval event_cut_cursor == 0
        assert eval event_intro_expression_ready is False
        assert eval [p["kind"] for p in event_pages(layout_event,layout_variant)] == ["intro"]*3 + ["main"]*3 + ["after"]
        assert eval len(event_cg_sets) == 16
        assert eval sum(s["runtime_connected"] for s in event_cg_sets.values()) == 4
        assert eval all(len(s["event_asset_order"]) == 5 and len(s["base_cg"]) == 3 and not s["expression_variants"] for s in event_cg_sets.values())
        click id "cut_next"
        click id "cut_next"
        pause 0.8
        assert eval event_cut_cursor == 2
        assert eval event_intro_expression_ready is True
        if eval case == 0:
            screenshot "intro-expression-placeholder.png"
        run FileSave("8", confirm=False)
        click id "cut_next"
        assert eval event_main_reached is True
        click id "cut_previous"
        assert eval event_cut_cursor == 2
        assert eval event_intro_expression_ready is True
        run FileLoad("8", confirm=False)
        assert screen "event_cut" timeout 10.0
        assert eval event_cut_cursor == 2
        assert eval event_intro_expression_ready is True
        assert eval event_main_reached is False
        click id "cut_next"
        assert eval event_cut_cursor == 3
        assert eval event_main_reached is True
        click id "cut_next"
        assert eval event_cut_cursor == 4
        click id "cut_next"
        assert eval event_cut_cursor == 5
        click id "cut_next"
        assert eval event_cut_cursor == 6
        assert eval renpy.get_screen("event_cut").scope["page"]["kind"] == "after"
        assert eval renpy.get_screen("event_cut").scope["expression"] is False
        click id "cut_next" until not screen "event_cut"
        advance until screen "choice"
        assert eval "layout_time_transition" not in memory
        assert eval event_presentations[layout_event+":"+layout_variant]["visited_slots"] == list(range(1,8))
        assert eval event_presentations[layout_event+":"+layout_variant]["main_frames_seen"] == [1,2,3]
        assert eval event_presentations[layout_event+":"+layout_variant]["loaded_asset_ids"] == []
        assert eval len(event_presentations[layout_event+":"+layout_variant]["missing_asset_ids"]) == 5
        assert eval event_presentations[layout_event+":"+layout_variant]["status"] == "completed"
        assert eval sum(affinity.values()) == 0
        assert eval first_kiss is False

    testcase skip_without_forced_wait:
        parameter reached = [False,True]
        $ layout_fixture["case"] = 0
        run Start("test_layout_entry")
        advance until screen "event_cut"
        if eval reached:
            click id "cut_next"
            click id "cut_next"
            click id "cut_next"
        click id "cut_skip" until not screen "event_cut"
        advance until screen "choice"
        assert eval ("layout_time_transition" in memory) == (not reached)
        assert eval event_presentations["ria_r07:casual"]["status"] == "skipped_presentation"

    teardown:
        exit

testsuite five_asset_fixture_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase synthetic_intro_and_three_main_images:
        $ layout_fixture["case"] = 0
        run Start("test_layout_entry")
        advance until screen "event_cut"
        assert eval event_intro_asset("ria_r07","casual")["path"] is not None
        click id "cut_next"
        click id "cut_next"
        pause 0.8
        assert eval event_intro_expression_ready is True
        assert eval event_intro_asset("ria_r07","casual",True)["fallback"] == (not renpy.loadable(event_cg_sets["ria_r07:casual"]["intro_expression"]["planned_path"]))
        screenshot "synthetic-intro-expression.png"
        click id "cut_next"
        assert eval event_resolve_cg("ria_r07","casual","ria_R07_casual_base01")["path"] is not None
        click id "cut_next"
        click id "cut_next"
        screenshot "synthetic-third-main.png"
        click id "cut_next" until not screen "event_cut"
        advance until screen "choice"
        assert eval event_presentations["ria_r07:casual"]["loaded_images"] == list(range(1,8))
        assert eval len(event_presentations["ria_r07:casual"]["loaded_asset_ids"]) == (5 if renpy.loadable(event_cg_sets["ria_r07:casual"]["intro_expression"]["planned_path"]) else 4)
        assert eval len(event_presentations["ria_r07:casual"]["missing_asset_ids"]) == (0 if renpy.loadable(event_cg_sets["ria_r07:casual"]["intro_expression"]["planned_path"]) else 1)
        assert eval first_kiss is False

    teardown:
        exit
'''
(G/'five_asset_tests.rpy').write_text(flow,encoding='utf-8')
print('Authored 64 new-choice cases, 8 full paths, 10 layout cases, and an isolated synthetic-media case.')
