from pathlib import Path
import json,hashlib,shutil
P=Path(__file__).resolve().parents[1]; S=P.parent; proof=P/'testing/romance-lines-v1'
proof.mkdir(parents=True,exist_ok=True)
assert not (proof/'changed-files.json').exists()
names=['ria_r09_r12.rpy','jihyun_r05_r12.rpy','yujin_r05_r08.rpy','seoyun_r05_r12.rpy','options.rpy']
for n in names: shutil.copy2(P/'game'/n,proof/(n+'.before'))
target=Path('C:/Users/user/Desktop/건/오피스 V2/game')
(proof/'previous-runtime-hashes.json').write_text(json.dumps({p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in target.iterdir() if p.is_file()},indent=2),encoding='utf-8')
def edit(n,old,new):
    p=P/'game'/n; t=p.read_text(encoding='utf-8'); assert t.count(old)==1,(n,old); p.write_text(t.replace(old,new),encoding='utf-8')
edit(names[0], '    if memory.get("ria_o02_status") == "completed":\n        if memory.get("ria_o02_name")', '''    "리아가 장바구니를 식탁 아래로 밀어 두고 도현을 보며 웃는다."
    r "[ri('오늘은 새로 찾은 데 없어.', '오늘은 새로 찾은 데 없어요.')]"
    d "[ri('네가 먼저 보자고 했잖아.', '리아 씨가 먼저 보자고 하셨잖아요.')]"
    r "[ri('응. 장소 말고 네가 보고 싶어서. ...이런 말은 두 번 시키지 마~', '네. 장소 말고 도현 씨가 보고 싶어서요. ...이런 말은 두 번 시키지 마세요~')]"
    d "[ri('나는 한 번 더 듣고 싶은데.', '저는 한 번 더 듣고 싶은데요.')]"
    r "[ri('그럼 너도 하나 해. 나만 용감한 거 억울하니까.', '그럼 도현 씨도 하나 해 주세요. 저만 용감한 거 억울하니까요.')]"
    d "[ri('나도 보고 싶었어. 오늘은 네 옆에서 밥 먹고 싶어서 왔어.', '저도 보고 싶었어요. 오늘은 리아 씨 옆에서 밥 먹고 싶어서 왔어요.')]"
    r "[ri('좋아~ 그럼 배고프기 전에 시작하자!', '좋아요~ 그럼 배고프기 전에 시작해요!')]"
    if memory.get("ria_o02_status") == "completed":
        if memory.get("ria_o02_name")''')
edit(names[1], '''    j "오늘 너 만나려고 골랐어. 어때? ...그냥 예쁘다고 해 줘도 돼. 오늘은 그 말 듣고 싶어."
    d "예뻐요. 들어오실 때부터 자꾸 봤어요."
    "지현이 소매를 놓고 웃었다. 이번에는 눈을 마주치는 쪽이 조금 늦었다."
    j "응. 한 번 더 듣고 싶었는데 먼저 말해 줬네. 오늘도 같이 있고 싶어."''', '''    j "오늘 너 만나려고 골랐어. 오늘은 잘했다는 말 말고."
    d "예쁘다는 말이요?"
    j "...응. 알아들었으면 그렇게 웃지만 말고."
    d "예뻐요. 들어오실 때부터 말씀드리고 싶었어요."
    "지현이 소매를 놓고 웃었다. 도현을 마주 보는 쪽이 평소보다 조금 늦었다."
    j "그럼 조금 일찍 해 주지. 나 아까부터 소매만 만지고 있었잖아."
    d "다음에는 눈 마주치면 바로 말할게요. 지금도 예뻐요."
    j "...응. 오늘도 같이 있고 싶어."''')
edit(names[2], '    menu:\n        "입맞춤해도 괜찮을지 먼저 묻는다.":', '''    y "다음에 만날 곳은 제가 골라도 돼요?"
    d "벌써 정해 두셨어요?"
    y "네. 도현 씨가 좋아하실지도 궁금하지만... 제가 같이 가고 싶어서요."
    d "그럼 따라갈게요."
    "유진이 작은 웃음을 삼키며 가방 끈을 고쳐 잡았다."
    y "...그렇게 바로 대답하시면 제가 더 떨리는데요. 그래도 취소는 안 할래요~ 토요일 세 시에 동네 서점 앞, 괜찮으세요?"
    d "네. 토요일 세 시에 봬요. 유진 씨가 고른 곳에서요."
    $ remember("yujin_r07_appointment", "토요일 오후 세 시, 동네 서점 앞")
    menu:
        "입맞춤해도 괜찮을지 먼저 묻는다.":''')
edit(names[3], '    s "오늘은 늘 가던 골목도 좋고, 네가 보여 주고 싶은 길도 좋아. 먼저 골라 볼래?"', '''    s "오늘은 네가 먼저 골라 줘. 나 좀 따라가 보고 싶어."
    d "마음에 안 들면 말씀하셔야 해요."
    s "그건 잘하지~ 그런데 지금은 기대하는 중이야."
    d "그럼 천천히 가요. 오늘은 제가 안내할게요."
    "서윤이 웃으며 도현 옆으로 한 걸음 다가왔다. 먼저 방향을 짚던 손은 가방 끈 위에 얹었다."
    s "...응. 그 말 들으니까 맡기길 잘했네. 늘 가던 골목도 좋고, 네가 보여 주고 싶은 길도 좋아."''')
edit('options.rpy','0.20.0-dialogue-review','0.20.1-romance-lines')
(proof/'changed-files.json').write_text(json.dumps(names,indent=2),encoding='utf-8')
guide=(P/'WINDOWS-README.txt').read_text(encoding='utf-8').replace('0.20.0-dialogue-review','0.20.1-romance-lines')
guide+='\n추가 반영: 승인한 연애 대사4묶음. 리아R11·지현R12·유진R06·서윤R11. 유진의 다음 서점 약속을 실제 대화에서 확인합니다.\n'
(P/'WINDOWS-README.txt').write_text(guide,encoding='utf-8')
print(names)
