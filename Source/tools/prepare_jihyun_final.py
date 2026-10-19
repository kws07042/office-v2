from pathlib import Path
import json,re
P=Path(__file__).resolve().parents[1]
G=P/'game'
def load(n): return json.loads((G/n).read_text(encoding='utf-8'))
def save(n,v): (G/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
a=load('event_assets.json'); story=load('event_story.json'); plan=load('event_cg_plan.json')
dialogue={
 'r07':[
 ('다 마시지 않아도', '지현이 찻잔을 내려놓고 도현을 본다.', '차는 나중에 더 마셔도 돼. 지금은 네 얘기 듣고 싶어.', '저도 지금은 여기 앉아 있고 싶어요.'),
 ('평소보다 느린 말', '말을 꺼내려던 지현이 잠깐 웃는다.', '부탁은 했는데, 이렇게 가까이 앉으니까 다음 말이 잘 안 나오네.', '저도요. 조금 기다려도 괜찮아요.'),
 ('같은 옆자리', '지현이 도현의 눈을 보고 손을 내민다.', '손잡고 조금 더 가까이 있어도 돼?', '네. 저도 그러고 싶어요.'),
 ('다시 건네는 차', '잠시 뒤 두 사람은 탁자에 둔 찻잔을 다시 들었다.', '이번에는 네가 고른 차도 같이 마셔 보고 싶어.', '다음에 가져올게요. 오늘 고른 것도 좋아요.')],
 'r12':[
 ('약속한 저녁 뒤', '지현이 오늘 고른 옷의 소매를 정리하고 앉는다.', '오늘 오기로 한 건 나도 지키고 싶었어.', '저도 오늘 만나서 좋아요.'),
 ('기다린 만큼', '둘은 엇갈렸던 일주일의 작은 얘기를 나눈다.', '한꺼번에 다 말하려니까 순서가 안 정해지네.', '그럼 지금 먼저 생각난 것부터요.'),
 ('가까워진 대답', '지현이 도현을 바라보고 조용히 웃는다.', '...지금은 다음 일정 말고 네가 더 가까이 있었으면 좋겠어.', '저도 같은 마음이에요.'),
 ('남겨 둔 말', '잠시 뒤 지현이 먼저 도현의 이름을 불렀다.', '내가 바쁜 날에도 보고 싶다는 말은 남겨 볼게.', '저도요. 답 기다리는 동안 혼자 결론 내리진 않을게요.')],
 'home':[
 ('편한 옷, 같은 마음', '지현이 편한 생활복으로 돌아와 옆에 앉는다.', '오늘은 이게 제일 편해. 이렇게 옆에 있는 것도.', '저도 좋아요. 오늘 얘기 더 듣고 싶어요.'),
 ('나눠 둔 시간', '덮어 둔 일정표 위로 시선이 잠깐 갔다가 돌아온다.', '아까 정한 약속은 내일도 기억할게. 지금은 여기부터.', '네. 지금은 같이 있는 시간이요.'),
 ('먼저 바라보기', '지현은 도현과 눈을 맞추고 손을 내민다.', '오늘도 같이 있고 싶어. 가까이 와 줄래?', '저도요. 이쪽으로 갈게요.'),
 ('내일의 작은 부탁', '잠시 뒤 두 사람은 함께 앉아 물을 마셨다.', '내일 아침 메뉴는 같이 고르자. 내가 먼저 다 정하지 않고.', '좋아요. 제가 먹고 싶은 것도 먼저 말할게요.')],
 'cosplay':[
 ('보여 주고 싶었던 옷', '지현이 탐정 재킷의 단추를 정리하고 돌아온다.', '생각보다 보여 주는 게 더 긴장되네. 내가 꺼낸 옷인데도.', '잘 어울려요. 먼저 보여 주고 싶다고 말해 주신 것도 좋고요.'),
 ('가벼운 장난', '지현이 모자를 탁자에 내려놓고 웃는다.', '표정 보니 감상은 물어볼 필요 없겠는데?', '그래도 말할래요. 오늘 자꾸 보게 돼요.'),
 ('장난 다음의 진심', '지현이 장난을 멈추고 도현의 눈을 본다.', '옷 구경 말고도 조금 더 가까이 있고 싶어. 너도 그래?', '네. 지금 같은 마음이에요.'),
 ('편하게 돌아온 자리', '잠시 뒤 지현이 재킷을 의자에 걸고 물을 가져왔다.', '이 옷은 오늘 보여 주길 잘했어. 이제 편하게 좀 더 앉아 있을까?', '좋아요. 저도 물잔 하나 가져올게요.')]
}
for slot,title,variants in [('r07','부탁해도 되는 저녁',['casual']),('r12','일정표에 남긴 자리',['special']),('r15','같은 편의 다른 의견',['home','cosplay'])]:
    key='jihyun_'+slot
    a[key]={'title':title,'variants':{}}
    story[key]={}
    for v in variants:
        a[key]['variants'][v]=[f'images/events/jihyun/{slot}_{v}_intro.png',f'images/events/jihyun/{slot}_{v}_intro_shy.png']+[f'images/event_cg/jihyun/{slot}_{v}_base{i:02}.png' for i in range(1,4)]
        story[key][v]=[dict(title=t,narration=n,heroine=j,dohyun=[d,d]) for t,n,j,d in dialogue[slot if slot!='r15' else v]]
for s in plan['sets']:
    if s['heroine']=='jihyun': s['runtime_connected']=True
plan.update(planning_revision='2.90',runtime_version='0.18.0-jihyun-complete-text',runtime_status='ria_yujin_jihyun_slots_connected_all_final_images_pending_seoyun_unimplemented')
save('event_assets.json',a); save('event_story.json',story); save('event_cg_plan.json',plan)
f=G/'five_asset_tests.rpy'; t=f.read_text(encoding='utf-8')
t=t.replace('("yujin_r15", "cosplay")]','("yujin_r15", "cosplay"), ("jihyun_r07", "casual"), ("jihyun_r12", "special"), ("jihyun_r15", "home"), ("jihyun_r15", "cosplay")]').replace('parameter case = list(range(16))','parameter case = list(range(24))')
f.write_text(t,encoding='utf-8')
# Retain the partial R04 fixtures, but exercise the full route from common C08.
f=G/'jihyun_tests.rpy'; t=f.read_text(encoding='utf-8')
a=t.index('    testcase common_to_jihyun:'); b=t.index('\n    teardown:',a)
head=t[a:b]; before=head[:head.index('        if not eval yujin_test_menu_end():')]
block='''        if not eval yujin_test_menu_end():
            advance until eval renpy.get_screen("choice") is not None or renpy.get_screen("office_phone") is not None or renpy.get_screen("event_cut") is not None
            if screen "event_cut":
                click id "cut_next" until not screen "event_cut"
            elif screen "office_phone":
                click id "phone_next" until eval not renpy.get_screen("office_phone") or bool(renpy.get_screen("office_phone").scope.get("replies"))
                if screen "office_phone":
                    click id ("phone_reply_"+renpy.get_screen("office_phone").scope["replies"][0][0])
                    click id "phone_next" until not screen "office_phone"
            elif not eval yujin_test_menu_end():
                click expression jihyun_test_common_caption()
'''
tail='''        assert eval yujin_test_menu_end()
        assert eval active_route == "jihyun" and memory["jihyun_intro"] == "evidence"
        assert eval memory["jihyun_r04_complete"] and dating
        assert eval ending == "jihyun_good" and memory["jihyun_route_completed"] and memory["jihyun_epilogue_completed"]
        assert eval not any(k.startswith("yujin_r") for k in memory)
'''
t=t[:a]+before+block*100+tail+t[b:]; f.write_text(t,encoding='utf-8')
print('Jihyun narrative slots and full common route test connected; no images generated.')
