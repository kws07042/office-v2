from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]
for filename in ('event_assets.json','event_story.json','event_cg_plan.json'):
    f=P/'game'/filename
    data=json.loads(f.read_text(encoding='utf-8'))
    if filename=='event_assets.json':
        data['yujin_r15']={'title':'다음에도 제가 말할게요','variants':{}}
        for variant in ('home','cosplay'):
            data['yujin_r15']['variants'][variant]=['images/events/yujin/r15_'+variant+'_intro.png','images/events/yujin/r15_'+variant+'_intro_shy.png',*['images/event_cg/yujin/r15_'+variant+'_base0'+str(i)+'.png' for i in (1,2,3)]]
    elif filename=='event_cg_plan.json':
        for group in data['sets']:
            if group['heroine']=='yujin' and group['event']=='R15':
                group['runtime_connected']=True
    else:
        data['yujin_r15']={}
        for variant in ('home','cosplay'):
            beats=[('먼저 고른 마음','유진이 문가에서 돌아와 도현과 마주 앉는다.','오늘은 제가 먼저 같이 있고 싶다고 말했네요.','저도 같은 마음으로 답한 거예요.'),
                   ('지금의 모습','유진이 잠깐 웃고 옆자리 쪽으로 몸을 돌린다.','다음 말은 적어 오지 않았어요. 지금 고르고 싶어서요.','그럼 저도 지금 듣고 답할게요.'),
                   ('나란한 시간','두 사람이 같은 자리에 가까이 머물며 잠깐 말을 쉰다.','말이 없어도 기다리는 느낌은 아니네요.','네. 같이 있는 쪽으로 남겨 둬요.'),
                   ('다음에도 먼저','유진이 도현을 바라보며 작게 웃는다.','다음에도 제가 먼저 고를래요. 같이 하고 싶은 말이요.','저도 제 마음 먼저 말할게요. 오늘처럼요.')]
            if variant=='cosplay':
                beats[1]=('함께 고른 모습','함께 고른 특별 의상 차림으로 유진이 잠깐 자세를 고친다.','어울린다는 말은 한 번 더 들어도 괜찮을 것 같아요.','잘 어울려요. 직접 골라 보여 주시는 것도 좋아요.')
            data['yujin_r15'][variant]=[dict(title=t,narration=n,heroine=y,dohyun=[d,d]) for t,n,y,d in beats]
    f.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
f=P/'game/yujin_tests.rpy'
s=f.read_text(encoding='utf-8')
start=s.index('    testcase common_to_yujin_route:')
end=s.index('        assert eval yujin_test_menu_end()',start)
block=s[start:end]
step=block[block.index('        if not eval'):]
step=step[:step.index('        if not eval',1)]
s=s[:start]+'    testcase common_to_yujin_route:\n        parameter epilogue = list(range(3))\n        $ yujin_fixture["epilogue"] = epilogue\n        run Start()\n'+step*100+s[end:]
s=s.replace('assert eval memory.get("yujin_r12_complete")','assert eval bool(memory.get("yujin_epilogue_completed")) == (epilogue != 1)').replace('assert eval memory.get("yujin_epilogue_completed")','assert eval bool(memory.get("yujin_epilogue_completed")) == (epilogue != 1)').replace('"yujin_R12" in completed','"yujin_R16" in completed').replace('assert eval ending == "yujin_r12_segment_complete"','assert eval ending == "yujin_good"')
if 'return captions[yujin_fixture.get("epilogue", 0)]' not in s:
    s=s.replace('        return captions[0]', '        if captions[0].startswith("후일담 읽기"):\n            return captions[yujin_fixture.get("epilogue", 0)]\n        return captions[0]')
f.write_text(s,encoding='utf-8')
tests='''init python:
    yujin_final_fixture = {"case":0}

label test_yujin_final_setup:
    $ active_route = "yujin"
    $ dating = True
    $ affinity = {"ria":0,"jihyun":0,"yujin":52,"seoyun":0}
    $ cream_focus = "yujin"
    $ memory = {"yujin_r12_complete":True, "yujin_r10_page":["entrance_bench","one_sentence","open_space"][yujin_final_fixture["case"] % 3], "yujin_r11_music":["yujin_calm","dohyun_bright","both"][yujin_final_fixture["case"] % 3]}
    if yujin_final_fixture["case"] % 5 != 4:
        $ remember("yujin_support_action", ["materials","self_summary","self_summary","agreed_summary"][yujin_final_fixture["case"] % 5])
        $ remember("yujin_support_overstep", yujin_final_fixture["case"] % 5 in (1,2))
        $ remember("yujin_support_repair_status", ["not_needed","open","agreed_pending_action","not_needed"][yujin_final_fixture["case"] % 5])
    if yujin_final_fixture["case"] == 24:
        $ remember("yujin_support_action", "self_summary")
        $ remember("yujin_support_overstep")
        $ remember("yujin_support_repair_status", "resolved")
        $ remember("yujin_support_repair_action_verified")
    return

label test_yujin_final_entry:
    call test_yujin_final_setup
    call yujin_o01_offer
    call yujin_o02_offer
    call yujin_r13
    call yujin_r14
    call yujin_r15
    call yujin_o03_offer
    call yujin_r16
    call yujin_e01
    $ remember("yujin_final_test_done")
    menu:
        "검사 종료":
            pass
    return

label test_yujin_close_entry:
    call test_yujin_final_setup
    call yujin_r13
    call yujin_r14
    call yujin_r15
    call yujin_r16
    $ remember("yujin_final_test_done")
    menu:
        "검사 종료":
            pass
    return

testsuite yujin_final_checks:
    before testcase:
        if not screen "main_menu":
            run MainMenu(confirm=False)
        run SetField(persistent, "phone_typing_enabled", False)
        run SetField(persistent, "local_yujin_ending", False)

    testcase supported_finale_and_optional_memories:
        parameter case = list(range(25))
        $ yujin_final_fixture["case"] = case
        run Start("test_yujin_final_entry")
        advance until screen "choice"
        click expression yujin_test_choice(case % 3)
        if eval case % 3 == 0:
            advance until screen "choice"
            click expression yujin_test_choice((case // 3) % 3)
        advance until screen "choice"
        click expression yujin_test_choice(case % 3)
        if eval case % 3 == 0:
            advance until screen "choice"
            click expression yujin_test_choice((case // 3) % 3)
        advance until screen "choice"
        assert eval memory["yujin_r13_path"] == ("check_agreement" if case == 24 or case % 5 == 2 else ("repair_open" if case % 5 == 1 else ("ask_current" if case % 5 == 4 else "new_scope")))
        assert eval not memory.get("yujin_support_alignment_verified")
        if eval case == 1:
            screenshot "yujin-r13-repair-plan.png"
        if eval case == 0:
            run FileSave("42", confirm=False)
            click expression yujin_test_choice(2)
            advance until screen "choice"
            assert eval memory["yujin_r13_support_plan"] == "requested_summary"
            run FileLoad("42", confirm=False)
        click expression yujin_test_choice(case % 3)
        advance until screen "choice"
        assert eval not memory.get("yujin_support_alignment_verified")
        click expression yujin_test_choice(case % 2)
        advance until screen "choice"
        assert eval memory["yujin_support_alignment_verified"]
        assert eval memory["yujin_r14_performed_plan"] == ["slides","questions","requested_summary"][case % 3]
        assert eval bool(memory.get("yujin_support_repair_action_verified")) == (case == 24 or case % 5 in (1,2))
        assert eval memory.get("yujin_support_repair_status") == ("resolved" if case == 24 or case % 5 in (1,2) else (None if case % 5 == 4 else "not_needed"))
        click expression yujin_test_choice((case // 3) % 3)
        advance until screen "choice"
        click expression yujin_test_choice((case // 5) % 3)
        if eval (case // 5) % 3 == 0:
            advance until screen "choice"
            click expression yujin_test_choice(case % 3)
            advance until screen "event_cut"
            assert eval renpy.get_screen("event_cut").scope["event_id"] == "yujin_r15"
            assert eval renpy.get_screen("event_cut").scope["variant"] == ("cosplay" if case % 3 == 1 else "home")
            if eval case == 1:
                screenshot "yujin-r15-cosplay-slot.png"
            if eval case == 3:
                click id "cut_skip"
            else:
                click id "cut_next" until not screen "event_cut"
        advance until screen "choice"
        assert eval memory["yujin_r15_intimacy"] == ["shared","deferred","talk"][(case // 5) % 3]
        assert eval ("yujin_r15_outfit" in memory) == ((case // 5) % 3 == 0)
        click expression yujin_test_choice(case % 3)
        if eval case % 3 == 0:
            advance until screen "choice"
            click expression yujin_test_choice((case // 3) % 3)
        elif eval case % 3 == 2:
            advance until screen "office_phone"
            click id "phone_next" until not screen "office_phone"
        advance until screen "choice"
        assert eval not memory.get("yujin_route_completed") and not persistent.local_yujin_ending
        assert eval memory["yujin_o01_status"] == ["completed","skipped","brief"][case % 3]
        assert eval memory["yujin_o02_status"] == ["completed","skipped","brief"][case % 3]
        assert eval memory["yujin_o03_status"] == ["completed","skipped","brief"][case % 3]
        assert eval bool(memory.get("yujin_o03_photo_taken")) == (case % 3 == 0 and (case // 3) % 3 == 0)
        click expression yujin_test_choice(case % 3)
        advance until screen "choice"
        assert eval ending == "yujin_good" and persistent.local_yujin_ending and memory["yujin_route_completed"]
        assert eval not memory.get("yujin_epilogue_completed")
        if eval case == 0:
            screenshot "yujin-epilogue-plans.png"
        click expression yujin_test_choice((case // 3) % 3)
        advance until eval memory.get("yujin_final_test_done")
        assert eval memory["yujin_epilogue_completed"]
        assert eval memory["yujin_e01_plan"] == ["exhibition_first","holiday_first","bring_candidates"][(case // 3) % 3]
        assert eval "예약·참가·여행 완료 아님" in memory["yujin_e01_travel_state"]
        assert eval affinity["yujin"] == 77 + (6 if case % 3 == 0 else 0)
        assert eval all("yujin_" + v in completed for v in ("R13","R14","R15","R16","E01"))
        assert eval all(("yujin_O0" + str(i) in completed) == (case % 3 == 0) for i in (1,2,3))
        assert eval len(completed) == len(set(completed))
        assert eval not any(k.startswith("ria_") for k in memory)

    testcase close_or_reconsider:
        parameter response = list(range(3))
        $ yujin_final_fixture["case"] = 1
        run Start("test_yujin_close_entry")
        advance until screen "choice"
        click expression yujin_test_choice(0)
        advance until screen "choice"
        click expression yujin_test_choice(2)
        advance until screen "choice"
        assert eval dating and not persistent.local_yujin_ending
        click expression yujin_test_choice(response)
        if eval response != 0:
            advance until screen "choice"
            assert eval memory["yujin_r14_relationship_talk_completed"]
            click expression yujin_test_choice(0)
            advance until screen "choice"
            click expression yujin_test_choice(1)
            advance until screen "choice"
            click expression yujin_test_choice(0)
        advance until eval memory.get("yujin_final_test_done")
        assert eval dating == (response != 0)
        assert eval persistent.local_yujin_ending == (response != 0)
        assert eval memory.get("yujin_relationship_closed",False) == (response == 0)
        assert eval ending == ("yujin_relationship_closed" if response == 0 else "yujin_good")
        assert eval ("yujin_R15" in completed) == (response != 0)

    teardown:
        exit
'''
(P/'game/yujin_final_tests.rpy').write_text(tests,encoding='utf-8')
print('Finale manifests and tests prepared')
