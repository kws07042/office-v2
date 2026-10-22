# Internal path trace; excluded from the production package.
init python:
    opening_fixture = {"case": 0, "route": "ria", "active": False, "rows": [], "decisions": []}
    def opening_record(h):
        if opening_fixture["active"] and h.kind == "adv":
            opening_fixture["rows"].append({"chapter": chapter, "who": h.who, "text": renpy.substitute(h.what)})
    config.history_callbacks.append(opening_record)
    def opening_done():
        return bool(memory.get("opening_test_done"))
    def opening_caption():
        caps=[renpy.substitute(x.caption) for x in renpy.get_screen("choice").scope["items"]]
        route=opening_fixture["route"]; variant=opening_fixture["case"]%3
        if chapter.startswith("C08"):
            idx=["ria","jihyun","yujin","seoyun"].index(route)
        elif chapter.startswith("C06") and len(caps)==4:
            idx=["ria","jihyun","yujin","seoyun"].index(route)
        elif chapter.startswith("C07") and len(caps)==4:
            idx=(["ria","jihyun","yujin","seoyun"].index(route)+(1 if variant==2 else 0))%4
        elif chapter.startswith("C01") and "같이 놓죠" in caps[0]:
            idx=1 if variant==1 else 0
        elif chapter.startswith(("리아 R04","지현 R04","유진 R04","서윤 R04")):
            already={"ria":prepared,"jihyun":jihyun_prepared,"yujin":yujin_prepared,"seoyun":seoyun_prepared}[route]
            if not already and variant==2 and len(caps)==3 and not dating:
                idx=1
            elif not dating:
                idx=0
            else:
                idx=variant%len(caps)
        else:
            idx=variant%len(caps)
        row={"chapter": chapter,"caption":caps[idx]}
        if not opening_fixture["decisions"] or opening_fixture["decisions"][-1] != row:
            opening_fixture["decisions"].append(row)
        return caps[idx]
    def opening_dump():
        import os,json
        out=os.path.join(config.basedir,"opening-traces")
        os.makedirs(out,exist_ok=True)
        payload={"route":opening_fixture["route"],"variant":opening_fixture["case"]%3,"rows":opening_fixture["rows"],"decisions":opening_fixture["decisions"],"messages":phone_threads,"memory":dict(memory),"dating":dating,"first_kiss":first_kiss,"speech_informal":speech_informal}
        with open(os.path.join(out,"%s-%s.json"%(payload["route"],payload["variant"])),"w",encoding="utf-8") as f:json.dump(payload,f,ensure_ascii=False,indent=2)

label test_opening_entry:
    scene bg plain
    $ opening_fixture["rows"] = []
    $ opening_fixture["decisions"] = []
    $ opening_fixture.pop("opening_prepared_checked", None)
    $ opening_fixture["active"] = True
    call c01
    call c02
    call c03
    call c04
    call c05
    call c06
    call c07
    call c08
    if active_route == "ria":
        call ria_r01
        call ria_r02
        call ria_r03
        call ria_r04
    elif active_route == "jihyun":
        call jihyun_r01
        call jihyun_r02
        call jihyun_r03
        call jihyun_r04
    elif active_route == "yujin":
        call yujin_r01
        call yujin_r02
        call yujin_r03
        call yujin_r04
    else:
        call seoyun_r01
        call seoyun_r02
        call seoyun_r03
        call seoyun_r04
    $ opening_fixture["active"] = False
    $ remember("opening_test_done")
    $ opening_dump()
    menu:
        "검사 종료":
            pass
    return

label test_opening_rest_entry:
    $ active_route = "seoyun"
    $ memory = {"seoyun_promise":"rest", "seoyun_r02_response":"wait"}
    $ _history_list = []
    call seoyun_r03
    $ remember("opening_test_done")
    menu:
        "검사 종료":
            pass
    return

testsuite opening_review:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent,"phone_typing_enabled",False)

    testcase common_to_four_confessions:
        parameter case = list(range(12))
        $ opening_fixture["case"] = case
        $ opening_fixture["route"] = ["ria","jihyun","yujin","seoyun"][case//3]
        run Start("test_opening_entry")
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        if not eval opening_done():
            advance until eval opening_done() or renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None
            if screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][opening_fixture["case"]%3][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval opening_done():
                click expression opening_caption()
        assert eval opening_done() and dating
        assert eval active_route == opening_fixture["route"]
        assert eval set(x for x in completed if x.startswith("C")) == {"C01","C02","C03","C04","C06","C07"}
        assert eval memory.get("c05_shared_table") and memory.get("c08_route") == active_route
        assert eval memory.get(active_route+"_confession_accepted")
        assert eval bool(memory.get(active_route+"_prepared_conversation")) == (case%3==2)
        assert eval first_kiss == (active_route=="ria" and case%3==0 or active_route=="seoyun" and case%3==0)
        assert eval bool(memory.get("ria_hand")) == (active_route=="ria" and case%3==0)
        assert eval not any("메모를 다시 집었다" in row["text"] for row in opening_fixture["rows"] if row["chapter"].startswith("서윤 R03"))
        assert eval all(not phone_threads[k] for k in ("ria","jihyun","yujin","seoyun") if k!=active_route)
        if eval case==0:
            screenshot "opening-ria-complete.png"
        if eval case==3:
            screenshot "opening-jihyun-complete.png"
        if eval case==6:
            screenshot "opening-yujin-complete.png"
        if eval case==9:
            screenshot "opening-seoyun-complete.png"

    testcase rest_path_has_no_written_prop:
        parameter choice = list(range(3))
        run Start("test_opening_rest_entry")
        advance until screen "choice"
        click expression yujin_test_choice(1)
        advance until screen "choice"
        click expression yujin_test_choice(choice)
        advance until eval opening_done()
        assert eval memory["seoyun_promise"] == "rest"
        assert eval memory["seoyun_r03_meaning"] == "small_promise"
        assert eval any("결과물 검사하는 사람" in h.what for h in _history_list)
        assert eval not any("메모를 다시 집었다" in h.what or "네가 고른 한 줄" in h.what for h in _history_list)
        assert eval memory["seoyun_r03_affection"] == ["hug","hand","words"][choice]
        assert eval not first_kiss

    teardown:
        exit
