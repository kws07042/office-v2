from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]; G=P/'game'
def load(n): return json.loads((G/n).read_text(encoding='utf-8'))
def save(n,v): (G/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
a=load('event_assets.json'); story=load('event_story.json'); plan=load('event_cg_plan.json')
beats={
'r07':[
('책을 덮은 자리','서윤이 책을 덮고 옆자리를 비운다.','여긴 책보다 네 다음 말 기다리는 자리 됐네.','저도 오늘은 옆에 더 앉아 있고 싶어요.'),
('먼저 하는 말','서윤은 컵을 내려놓고 도현을 바라본다.','잘 말하려고 하니까 자꾸 장난부터 떠올라. 오늘은 그냥 보고 싶었다고 할게.','저도요. 그 말 듣고 싶었어요.'),
('다시 보는 눈','서윤이 도현의 눈을 보고 손을 내민다.','조금 더 가까이 있어도 돼?','네. 저도 같은 마음이에요.'),
('같은 책갈피','잠시 뒤, 서윤은 탁자 위 책갈피를 집어 책 사이에 넣었다.','오늘 읽던 데는 여기였네. 다음에는 이다음부터 같이 볼래?','좋아요. 오늘 얘기도 그 옆에 기억해 둘게요.')],
'r12':[
('다시 만난 저녁','서윤은 오늘 고른 옷의 소매를 정리하며 앉는다.','이번 주 내내 오늘 만나면 무슨 말 할지 생각했어.','저도요. 얼굴 보니까 준비한 말부터 잊었네요.'),
('놓지 않은 시선','둘은 짧게 보냈던 메시지 뒤의 하루를 나눈다.','짧게 보내 놓고도 네 답은 오래 기다렸어.','그 말은 만나서 들으니까 더 좋네요.'),
('가까운 대답','서윤이 도현을 보며 손을 내민다.','지금은 네가 더 가까이 있었으면 좋겠어.','저도 그러고 싶어요.'),
('아직 남은 말','잠시 뒤 두 사람은 찻잔을 들고 나란히 앉았다.','다음 얘기할 게 남았네. 모르는 것도 그때 제대로 말해 볼게.','네. 오늘 다 답해야 한다는 뜻은 아니었어요.')],
'home':[
('편하게 돌아온 자리','서윤이 편한 생활복으로 돌아와 옆에 앉는다.','이 옷은 오늘 하루 끝에 입고 싶었어. 네가 옆에 있는 것도 좋고.','저도 오늘은 여기 더 있고 싶어요.'),
('적어 둔 약속','덮어 둔 달력 옆에 두 사람의 찻잔이 놓인다.','다음 약속 적으니까 오늘은 조금 덜 서두르게 되네.','지금은 같이 있는 시간부터 쓸래요.'),
('장난을 멈추고','서윤은 도현의 눈을 보고 손을 내민다.','이 말은 그냥 할게. 더 가까이 있고 싶어.','저도 같은 마음이에요.'),
('다음 잔','잠시 뒤 서윤이 빈 물잔을 보고 웃었다.','다음 잔은 네가 고른 차로 마셔 보고 싶어.','좋아요. 제가 먼저 골라 볼게요.')],
'cosplay':[
('보여 주고 싶던 옷','서윤이 마술사 재킷을 정리하고 돌아온다.','꽃은 못 꺼내도 네 표정은 좀 바꿨나 봐?','잘 어울려요. 자꾸 보게 되는 건 맞아요.'),
('가벼운 장난 뒤','서윤이 모자를 탁자에 내려놓고 앉는다.','여유 있게 나올 줄 알았는데 문 앞에서 좀 망설였어.','먼저 보여 주고 싶다고 말해 주셔서 좋았어요.'),
('같은 마음','장난을 멈춘 서윤이 도현을 바라본다.','옷 얘기 뒤로 숨기진 않을게. 네가 더 가까이 있었으면 좋겠어.','네. 저도 지금 그러고 싶어요.'),
('편한 다음 말','잠시 뒤 서윤이 재킷을 의자에 걸고 물을 가져왔다.','이제 평소처럼 앉을까? 오늘 보여 준 건 나도 좋았어.','좋아요. 다음 말도 편하게 들려주세요.')]
}
for slot,title,variants in [('r07','농담을 멈춘 저녁',['casual']),('r12','이번엔 날짜까지 말할게',['special']),('r15','다음 금요일은 우리 약속',['home','cosplay'])]:
    k='seoyun_'+slot; a[k]={'title':title,'variants':{}}; story[k]={}
    for v in variants:
        a[k]['variants'][v]=[f'images/events/seoyun/{slot}_{v}_intro.png',f'images/events/seoyun/{slot}_{v}_intro_shy.png']+[f'images/event_cg/seoyun/{slot}_{v}_base{i:02}.png' for i in range(1,4)]
        story[k][v]=[dict(title=t,narration=n,heroine=s,dohyun=[d,d]) for t,n,s,d in beats[slot if slot!='r15' else v]]
for s in plan['sets']:
    if s['heroine']=='seoyun': s['runtime_connected']=True
plan.update(planning_revision='2.91',runtime_version='0.19.0-all-routes-text',runtime_status='four_heroine_event_slots_connected_all_final_images_pending')
save('event_assets.json',a); save('event_story.json',story); save('event_cg_plan.json',plan)
f=G/'five_asset_tests.rpy'; t=f.read_text(encoding='utf-8')
t=t.replace('("jihyun_r15", "cosplay")]','("jihyun_r15", "cosplay"), ("seoyun_r07", "casual"), ("seoyun_r12", "special"), ("seoyun_r15", "home"), ("seoyun_r15", "cosplay")]').replace('parameter case = list(range(24))','parameter case = list(range(32))')
f.write_text(t,encoding='utf-8')
print('All 16 planned event sets connected; no new art created.')
