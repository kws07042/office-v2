from pathlib import Path

p = Path(__file__).resolve().parents[1] / 'game/ria16_tests.rpy'
source = p.read_text(encoding='utf-8').split('\ntestsuite ria16_flow:')[0]
flow = '''
testsuite ria16_flow:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        assert screen "main_menu" timeout 10.0

    testcase full_route:
        parameter route = ["ria", "deferred", "close", "colleague", "decline", "no_epilogue", "cosplay", "third"]
        click id "start_button" until not screen "main_menu"
'''
step = '''        if not eval ria16_final_menu():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
                advance until screen "choice"
            if not eval ria16_final_menu():
                click expression ria16_flow_caption(route) until not screen "choice"
'''
flow += step * 80
flow += '''        assert eval ria16_final_menu()
        if eval route in ("ria", "deferred", "no_epilogue", "cosplay", "third"):
            assert eval ending == "ria_good"
            assert eval dating is True
            assert eval memory["ria_conflict"] == "resolved"
            assert eval memory["ria_route_completed"] is True
            assert eval persistent.local_ria_ending is True
            assert eval all(k in completed for k in ("ria_R04", "ria_R13", "ria_R14", "ria_R15", "ria_R16"))
            if eval route == "no_epilogue":
                assert eval memory["ria_epilogue_skipped"] is True
                assert eval "ria_E01" not in completed
                assert eval "ria_epilogue_completed" not in memory
                assert eval memory["ria_booklet_state"] == "rough_draft_shared"
            else:
                assert eval memory["ria_epilogue_completed"] is True
                assert eval memory["ria_booklet_state"] == "completed_two_copies"
            if eval route == "deferred":
                assert eval all(memory[k] == "deferred" for k in ("ria_r07_intimacy", "ria_r12_intimacy", "ria_r15_intimacy"))
                assert eval all(memory[k] == "skipped" for k in ("ria_o01_status", "ria_o02_status", "ria_o03_status"))
                assert eval memory["ria_publicity"] == "private"
                assert eval "ria_known_colleagues" not in memory
                assert eval memory["ria_r13_response"] == "cover"
                assert eval memory["ria_r14_understanding_confirmed"] is True
                assert eval first_kiss is False
                assert eval speech_informal is False
            assert eval not any(k in memory for k in ("ria_r09_intimacy", "ria_r11_intimacy", "ria_e01_intimacy"))
            if eval route == "deferred":
                assert eval event_presentations == {}
                assert eval "ria_r15_outfit" not in memory
            if eval route in ("ria", "cosplay", "no_epilogue"):
                assert eval len(event_presentations) == 3
                assert eval all(v["visited_slots"] == list(range(1, 8)) and v["loaded_images"] == [] and v["main_frames_seen"] == [1, 2, 3] and v["base_slots_seen"] == [1, 2, 3] and v["loaded_asset_ids"] == [] and v["status"] == "completed" for v in event_presentations.values())
                assert eval memory["ria_r15_outfit"] == ("cosplay" if route == "cosplay" else "home")
                assert eval "ria_r15:" + memory["ria_r15_outfit"] in event_presentations
            if eval route == "cosplay":
                assert eval any("문 앞에서 웃" in h.what for h in _history_list)
            if eval route == "ria":
                screenshot "ria16-full-route-end.png"
            if eval route == "no_epilogue":
                screenshot "ria16-base-ending.png"
        elif eval route == "close":
            assert eval ending == "ria_relationship_closed"
            assert eval dating is False
            assert eval memory["ria_conflict"] == "closed_without_repair"
            assert eval "ria_route_completed" not in memory
            assert eval not any(k in completed for k in ("ria_R14", "ria_R15", "ria_R16", "ria_E01"))
            screenshot "ria16-relationship-closed.png"
        else:
            assert eval ending == "colleague"
            assert eval dating is False
            assert eval "ria_route_completed" not in memory
            assert eval not any(k in completed for k in ("ria_R13", "ria_R14", "ria_R15", "ria_R16", "ria_E01"))

    teardown:
        exit
'''
p.write_text(source + flow, encoding='utf-8')
print('Authored eight complete-flow cases.')
