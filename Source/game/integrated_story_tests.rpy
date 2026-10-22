# Integrated native playthroughs. Not shipped in the playable package.
init python:
    integrated_fixture = {"active": False, "case": 0, "rows": [], "choices": [], "shots": set()}
    def integrated_record(h):
        if integrated_fixture["active"] and h.kind == "adv":
            integrated_fixture["rows"].append({"chapter": chapter, "who": h.who, "text": renpy.substitute(h.what)})
    config.history_callbacks.append(integrated_record)
    def integrated_done():
        sc = renpy.get_screen("choice")
        return bool(sc and any("수록 구간을 마쳤습니다" in i.caption for i in sc.scope["items"]))
    def integrated_caption():
        caps = [renpy.substitute(i.caption) for i in renpy.get_screen("choice").scope["items"]]
        v = integrated_fixture["case"] % 2
        route = ["ria", "jihyun", "yujin", "seoyun"][integrated_fixture["case"] // 2]
        i = len(caps) - 1 if v and len(caps) == 3 else 0
        if chapter.startswith("C08"):
            i = ["ria", "jihyun", "yujin", "seoyun"].index(route)
        elif chapter.startswith(("C06", "C07")) and len(caps) == 4:
            i = (["ria", "jihyun", "yujin", "seoyun"].index(route) + (1 if v else 0)) % 4
        elif chapter.startswith("C01") and any("같이 놓죠" in c for c in caps):
            i = v
        elif "R04" in chapter and not dating:
            prepared_now = {"ria": prepared, "jihyun": jihyun_prepared, "yujin": yujin_prepared, "seoyun": seoyun_prepared}[route]
            i = 1 if v and not prepared_now else 0
        elif "(선택 일상)" in caps[0]:
            i = 2 if v else 0
        elif caps[0].startswith("후일담 읽기"):
            i = 0
        elif any("친밀한 장면" in c for c in caps):
            i = 1 if v else 0
        elif any("관계 종료" in c or "관계를 끝" in c for c in caps):
            i = 0
        elif "R13" in chapter or "R14" in chapter:
            i = 0
        row = {"chapter": chapter, "caption": caps[i]}
        if not integrated_fixture["choices"] or integrated_fixture["choices"][-1] != row:
            integrated_fixture["choices"].append(row)
        return caps[i]
    def integrated_dump():
        import os, json
        out = os.path.join(config.basedir, "review-output", "integrated-v1")
        os.makedirs(out, exist_ok=True)
        payload = {"route": active_route, "variant": integrated_fixture["case"] % 2, "rows": integrated_fixture["rows"], "choices": integrated_fixture["choices"], "messages": phone_threads, "memory": dict(memory), "completed": completed, "ending": ending, "first_kiss": first_kiss, "speech_informal": speech_informal}
        with open(os.path.join(out, active_route + "-" + str(payload["variant"]) + ".json"), "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

testsuite integrated_story_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)

    testcase opening_through_epilogue:
        parameter case = list(range(8))
        $ integrated_fixture.update(active=True, case=case, rows=[], choices=[], shots=set())
        run Start("start")
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        if not eval integrated_done():
            advance until eval integrated_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "office_phone":
                if eval "phone" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-phone.png")
                    $ integrated_fixture["shots"].add("phone")
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_" + renpy.get_screen("office_phone").scope["replies"][case % 2][0])
                    click id "phone_next" until not screen "office_phone"
            elif screen "event_cut":
                click id "cut_skip"
            elif not eval integrated_done():
                if eval "R05" in chapter and "early" not in integrated_fixture["shots"] and case % 2 == 0:
                    if eval active_route == "yujin":
                        assert eval location == "같은 토요일 오후 · 작은 공원 벤치"
                    screenshot ("integrated-" + active_route + "-early-date.png")
                    $ integrated_fixture["shots"].add("early")
                if eval "E01" in chapter and "epilogue" not in integrated_fixture["shots"] and case % 2 == 0:
                    screenshot ("integrated-" + active_route + "-epilogue.png")
                    $ integrated_fixture["shots"].add("epilogue")
                click expression integrated_caption()
        assert eval integrated_done() and dating
        assert eval active_route == ["ria", "jihyun", "yujin", "seoyun"][case // 2]
        assert eval memory.get(active_route + "_confession_accepted")
        assert eval memory.get(active_route + "_route_completed")
        assert eval memory.get(active_route + "_epilogue_completed") or (active_route == "ria" and "ria_E01" in completed)
        assert eval memory.get("c05_shared_table") and persistent.common_seen
        assert eval (c06_person == active_route) == (case % 2 == 0)
        assert eval (c07_person == active_route) == (case % 2 == 0)
        assert eval all(sum(1 for r in phone_threads[k] if r["id"] == row["id"]) == 1 for k in phone_threads for row in phone_threads[k])
        if eval active_route == "ria":
            assert eval speech_informal == (case % 2 == 0)
            assert eval all(memory.get(k) != "shared" for k in ("ria_r07_intimacy", "ria_r12_intimacy", "ria_r15_intimacy")) == bool(case % 2)
        else:
            assert eval all(memory.get(active_route + "_" + slot + "_pace", memory.get(active_route + "_" + slot + "_intimacy")) != "shared" for slot in ("r07", "r12", "r15")) == bool(case % 2)
        $ integrated_dump()
        $ integrated_fixture["active"] = False

    teardown:
        exit
