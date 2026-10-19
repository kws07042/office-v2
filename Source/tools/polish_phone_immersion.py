from pathlib import Path
import json
P=Path(__file__).resolve().parents[1]; proof=P/'testing/immersion-v1'
edits=json.loads((proof/'changes.json').read_text(encoding='utf-8'))
changed=json.loads((proof/'changed-files.json').read_text(encoding='utf-8'))
def body(name,old,new,label):
    p=P/'game'/name; t=p.read_text(encoding='utf-8'); assert t.count(old)==1,(name,old)
    if name not in changed:
        (proof/(name+'.before')).write_text(t,encoding='utf-8'); changed.append(name)
    p.write_text(t.replace(old,new),encoding='utf-8')
    edits.append(dict(file=name,label=label,before=old,after=new))
body('office_phone.rpy','...그렇게 보내면 나 자꾸 휴대폰 보는데!','방금 세 번 읽었어. 네가 보낸 거 한 줄 맞지? 휴대폰 탓인가~','ria_r08_phone_conversation')
body('office_phone.rpy','...그렇게 보내시면 저 자꾸 휴대폰 보는데요!','방금 세 번 읽었어요. 보내신 거 한 줄 맞죠? 휴대폰 탓인가 봐요~','ria_r08_phone_conversation')
body('office_phone.rpy','좋아 :) 다음엔 덜 바쁘게 생각할게.','좋아 :) 다음엔 조용해졌다고 말 찾느라 컵만 돌리지는 않을게~','ria_r08_phone_conversation')
body('office_phone.rpy','좋아요 :) 다음엔 덜 바쁘게 생각할게요.','좋아요 :) 다음엔 조용해졌다고 말 찾느라 컵만 돌리지는 않을게요~','ria_r08_phone_conversation')
body('jihyun_r05_r12.rpy','어제 아침에 같이 접시 놓던 거 생각났어. 오늘은 나 혼자 꺼내려니 하나 더 찾게 되네.','접시 하나 꺼냈다가 또 찬장 열었어. 어제 네 몫 놓던 게 손에 남았나 봐.','jihyun_r08')
body('jihyun_r05_r12.rpy','그럼 따뜻한 국수. 결정 맡기는 척하고 고르기 어려운 건 아니야~ 수요일 일곱 시에 봐.','따뜻한 국수. 오늘은 내가 먼저 골랐어 :) 수요일 일곱 시에 봐.','jihyun_r08')
body('yujin_r05_r08.rpy','어제 차 마시면서 나눈 얘기, 오늘 노트 한쪽에 짧게 적었어요. 다음에도 제가 먼저 말해 보고 싶어요.','어제 차 마시면서 한 얘기, 오늘 노트에 적다가 혼자 웃었어요. 제목은 비밀이에요~','yujin_r08')
body('yujin_r05_r08.rpy','좋아요. 그날 제가 먼저 자리 보고 있을게요. 보여 주고 싶은 것 말고, 그냥 보고 싶은 사람도 적어 뒀어요 :)','좋아요. 그날 제가 먼저 자리 볼게요. 노트는 없어도 돼요. 도현 씨만 오시면요 :)','yujin_r08')
body('seoyun_r05_r12.rpy','보고 싶어. 오늘은 이 말 뒤에 농담 안 붙일래. 다음 수요일 저녁 일곱 시에 밥 먹자. 네 시간은 어때?','보고 싶어. 다음 수요일 저녁 일곱 시에 같이 밥 먹자. 책은 두고 갈게~ 네 시간은 어때?','seoyun_r08')
body('seoyun_r05_r12.rpy','별일 없는 얘기는 자주 해도 돼~ 수요일 일곱 시엔 얼굴 보면서 더 듣자.','창가에 혼자 앉은 얘기까지 들었네. 수요일엔 내 앞자리로 와~ 일곱 시에 봐.','seoyun_r08')
(proof/'changes.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2),encoding='utf-8')
(proof/'changed-files.json').write_text(json.dumps(changed,indent=2),encoding='utf-8')
print('Updated 10 messenger bodies; IDs, recipients, timing and replies preserved.')
