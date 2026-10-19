from pathlib import Path
import json, hashlib, shutil

P = Path(__file__).resolve().parents[1]
proof = P / 'testing/full-editorial-v1'
proof.mkdir(parents=True, exist_ok=True)
assert not (proof / 'edit-log.json').exists(), 'Already applied'
files = [p for p in (P/'game').glob('*.rpy') if '_tests' not in p.name and p.name != 'testcases.rpy']
files += [P/'game/event_story.json']
for p in files:
    shutil.copy2(p, proof/(p.name+'.before'))
installed = Path('C:/Users/user/Desktop/건/오피스 V2/game')
old = {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in installed.iterdir() if p.is_file()}
(proof/'previous-runtime-hashes.json').write_text(json.dumps(old,indent=2),encoding='utf-8')
edits=[]
def replace(name, before, after):
    p=P/'game'/name
    t=p.read_text(encoding='utf-8')
    assert t.count(before)==1,(name,before,t.count(before))
    p.write_text(t.replace(before,after),encoding='utf-8')
    edits.append(dict(file=name,before=before,after=after))

# Keep evidence in state rather than narrating implementation rules to players.
replace('common.rpy', '지현은 \'출근길 중심\' 옆에 확인 날짜를 적는다. 도현이 근거를 제출한 것으로 처리하지 않는다.', '지현은 \'출근길 중심\' 옆에 내일 날짜를 적고 도현의 메모를 돌려준다.')
replace('common.rpy', '도현은 골목의 위치를 메모한다. 아직 방문하거나 사진을 찍은 기록은 없다.', '도현은 골목의 위치를 메모한다. 길보다 추천해 준 사람의 표정이 먼저 기억에 남았다.')
replace('common.rpy', '서윤이 덜어 낼 문장을 표시한 뒤 자료를 덮는다. 최종 시안은 아직 확정하지 않는다.', '서윤이 덜어 낼 문장을 표시한 뒤 자료를 덮는다. 남은 검토는 내일 하자며 펜도 내려놓는다.')
replace('common.rpy', "지난번처럼 잠깐 같이 나갈래? 이번엔 퇴근하고.', '지난번처럼 잠깐 같이 나갈래요? 이번엔 퇴근하고요.", "지난번엔 짧아서 아쉬웠어. 다음엔 좀 더 같이 있을래?', '지난번엔 짧아서 아쉬웠어요. 다음엔 좀 더 같이 있을래요.")

# Same-age warmth: the straight answer lands after the joke, not a lesson.
replace('ria_r13_e01.rpy', "r \"[ri('...그럼 나도 좀 정독해야겠네!', '...그럼 저도 좀 정독해야겠네요!')]\"", "r \"[ri('...그럼 나도 좀 정독해야겠네!', '...그럼 저도 좀 정독해야겠네요!')]\"\n    \"리아가 노트 쪽으로 고개를 기울였다가 가까워진 거리를 알아채고 웃는다.\"\n    r \"[ri('글씨가 작아서 가까이 온 건데. 네가 보니까 좀 다른 핑계 같네~', '글씨가 작아서 가까이 온 건데요. 도현 씨가 보시니까 좀 다른 핑계 같네요~')]\"\n    d \"[ri('그 핑계는 다음 장에서도 써.', '그 핑계는 다음 장에서도 써 주세요.')]\"")
replace('ria_r13_e01.rpy', '$ location = "같은 날 저녁 · 각자의 집, 메시지"', '$ location = "그다음 화요일 저녁 · 각자의 집, 메시지"')

# Yujin's shyness and playful initiative coexist; no sudden personality switch.
replace('yujin_r05_r08.rpy', '...그럼 제가 졌네요. 점심 먹고 달력부터 봤는데.', '...그럼 제가 이겼네요. 점심 먹고 달력부터 봤는데.')
replace('yujin_r05_r08.rpy', '기다리기 시합이었어요? 제가 조금 일찍 말씀드릴걸~', '기다리기 시합이었어요? 다음엔 제가 먼저 말씀드릴걸~')
replace('yujin_r09_r12.rpy', 'y "그 말은 지금도 좋아요. 오늘은 조금 더 같이 있고 싶어요. 집에 들르실래요?"', '"유진은 소매를 만지던 손을 내려놓고 도현의 눈을 마주 봤다."\n    y "그 말은 지금도 좋아요. ...이번엔 제가 안 피했네요. 도현 씨가 먼저 보셨는데~"\n    d "졌네요. 그런데 다시 봐도 돼요?"\n    y "네. 오늘은 저도 더 보고 싶어요. 집에 들르실래요?"')
replace('yujin_r13_e01.rpy', 'y "그럼 다음에는 기다리지만 말고 먼저 해 주세요. 저도 제 말 고르고 있을 테니까."', 'y "그럼 다음에는 먼저 해 주세요. 오늘은 제가 먼저 불렀으니까, 다음엔 도현 씨 차례요~"\n    "유진이 차를 도현 쪽으로 밀었다. 웃는 얼굴은 여전히 붉었지만 시선은 피하지 않았다."')
replace('yujin_r13_e01.rpy', 'y "다음에 하고 싶은 말도 제가 먼저 할 수 있을 것 같아요. 오늘처럼 도현 씨 마음도 듣고요."', 'y "오늘 먼저 말한 건 저예요. ...그렇게 웃으시면 다음에도 제가 먼저 하고 싶어지잖아요."')

# Jihyun: retain competence, show the private response to being cherished.
replace('jihyun_r01_r04.rpy', 'j "응. 나도 도현 씨랑 연인으로 만나고 싶어. 오늘 대답은 일 잘하라는 뜻이 아니야. 나도 그냥 보고 싶어서 하는 말이고."', 'j "응. 나도 좋아해. 오늘은 답을 준비해 왔다고 생각했는데... 네가 먼저 말하니까 다 잊었네."')
replace('jihyun_r01_r04.rpy', 'd "네. 저도 평가받으러 나온 게 아니에요. 좋아하는 분께 답 들으러 왔어요."', 'd "잊으셔도 돼요. 방금 대답은 제가 오래 기억할게요."')
replace('jihyun_r05_r12.rpy', '지운 얘기도 해 달고 하셨죠?', '지운 얘기도 해 달라고 하셨죠?')
replace('jihyun_r05_r12.rpy', 'j "응. 놀라게 하는 걸 설렘으로 정하진 않을게."', 'j "응. 지금처럼 보면 되지? ...말하고 나니까 내가 더 떨리네."')
replace('jihyun_r05_r12.rpy', 'j "알겠어. 장소를 바꿔 달라는 말하고, 하고 싶지 않다는 말은 따로 들을게."', 'j "알겠어. 둘이 있을 때는 내가 먼저 손 내밀 수도 있어. 그때도 네 마음은 말해 줘."')
# Split departure/POV from the afternoon so the optional scene cannot rewind time.
name='jihyun_r05_r12.rpy'
p=P/'game'/name; t=p.read_text(encoding='utf-8')
a=t.index('    "도현이 돌아간 뒤, 지현은'); b=t.index('\nlabel jihyun_r11:',a)
oldblock=t[a:b]
newblock='''    $ award_once("jihyun_R10", "jihyun", 4)
    return

label jihyun_r10_after:
    if not dating or active_route != "jihyun" or "jihyun_R10" not in completed:
        return
    $ location = "같은 토요일 밤 · 지현의 집 — 지현 시점"
    "도현이 돌아간 뒤, 지현은 조립품 옆에 노트를 두던 자리를 한 번 보았다."
    jn "다음 판도 보고 싶다고 했지. ...그냥 다음에도 보고 싶다는 말을 먼저 해도 됐는데."
    "지현은 다음 날 약속 메시지에 ‘노트 없어도 와’를 덧붙여 보냈다."
    call phone_deliver("jihyun_r10_after", "jihyun", "내일은 노트 없어도 와. 같이 놀고 싶어서 부르는 거야~", contact="jihyun")
    $ remember("jihyun_r10_after_completed")
    return
'''
p.write_text(t[:a]+newblock+t[b:],encoding='utf-8'); edits.append(dict(file=name,before=oldblock,after=newblock))
replace('jihyun_r01_r04.rpy', '        call jihyun_o02_offer\n        call jihyun_r11', '        call jihyun_o02_offer\n        call jihyun_r10_after\n        call jihyun_r11')
replace('jihyun_r05_r12.rpy', 'j "이 옷은 보고하러 입은 거 아니야. 오늘 너 만나려고 골랐어. ...오늘도 같이 있고 싶고."', 'j "오늘 너 만나려고 골랐어. 어때? ...그냥 예쁘다고 해 줘도 돼. 오늘은 그 말 듣고 싶어."\n    d "예뻐요. 들어오실 때부터 자꾸 봤어요."\n    "지현이 소매를 놓고 웃었다. 이번에는 눈을 마주치는 쪽이 조금 늦었다."\n    j "응. 한 번 더 듣고 싶었는데 먼저 말해 줬네. 오늘도 같이 있고 싶어."')

# Seoyun: let an assured adult choose to be looked after; no workplace caricature.
replace('seoyun_r05_r12.rpy', 's "응. 오늘 네가 고른 답을 다음 기대까지 없어진 말로 듣진 않을게."', 's "응. 집에 가서 푹 쉬어. 다음엔 내가 먼저 보고 싶다고 연락할게~"')
replace('seoyun_r05_r12.rpy', 's "칭찬 뒤에 그런 말 붙이면, 밥 먹다 말고 너만 보게 되잖아."', 's "칭찬 뒤에 그런 말 붙이면, 밥 먹다 말고 너만 보게 되잖아."\n    "서윤이 웃으며 메뉴판을 도현 쪽으로 돌렸다. 평소와 달리 이번에는 설명을 덧붙이지 않았다."\n    s "오늘은 네 추천 들을래. 내가 늘 먼저 고르는 사람인 건 좀 쉬고 싶어서."\n    d "그럼 두 개만 골라 볼게요. 마음에 드는 쪽은 같이 정해요."\n    s "응. 나 지금 은근히 기대하는 중이야~"')
replace('seoyun_r13_e01.rpy', 's "나도 계속 만나고 싶어. 지금 할 수 있는 말하고 싶은 약속을 구분해서 말할게."', 's "나도 계속 만나고 싶어. 지금 지킬 수 있는 약속부터 할게. 바라는 건 바라는 대로 말하고."')
replace('seoyun_r13_e01.rpy', 's "오늘 이 옆에 더 있고 싶어. 같이 밤을 보내고 싶은데, 너는 어때?"', '"서윤이 달력을 덮어 멀리 놓았다. 도현을 돌아보며 웃다가 이번에는 먼저 눈을 내린다."\n    s "나 오늘은 잘 받아치는 사람 좀 쉬어도 돼? 네가 먼저 나 보고 싶었다고 말해 줬으면 좋겠어."\n    d "보고 싶었어요. 지금도 더 같이 있고 싶고요."\n    s "...응. 그 한마디 듣는데 이렇게 오래 걸리네. 오늘은 같이 밤을 보내고 싶어. 너는 어때?"')
replace('options.rpy', '0.19.0-all-routes-text', '0.20.0-dialogue-review')

# Only non-graphic lead-in/afterglow text. Keep the 3 main asset slots untouched.
p=P/'game/event_story.json'; events=json.loads(p.read_text(encoding='utf-8'))
def beat(e,v,i,n,h,d,formal=None):
    b=events[e][v][i]; before=dict(b)
    b['narration']=n
    if 'ria' in b: b['ria']=[h,formal[0]]; b['dohyun']=[d,formal[1]]
    else: b['heroine']=h; b['dohyun']=[d,d]
    edits.append(dict(file='event_story.json',event=e,variant=v,beat=i,before=before,after=dict(b)))
beat('ria_r07','casual',1,'리아가 빈 찻잔을 가지런히 놓다가 도현을 올려다본다. 평소의 빠른 말끝이 잠깐 느려졌다.','나 오늘 말 별로 없지? 네 앞에서 조용한 거, 좀 어색해.','난 그 모습도 보고 싶었어. 억지로 얘기 안 찾아도 돼.',('저 오늘 말 별로 없죠? 도현 씨 앞에서 조용한 거, 조금 어색해요.','저는 그 모습도 보고 싶었어요. 억지로 얘기 안 찾으셔도 돼요.'))
beat('ria_r12','special',1,'리아가 도현을 마주 보더니 웃으며 가방을 멀리 놓는다. 이번에는 금세 시선을 돌리지 않았다.','아까 역에선 내가 먼저 찾았잖아. 지금은 네가 나 좀 봐 줘.','보고 있었어. 오늘 예쁘다는 말부터 해야 했는데.',('아까 역에선 제가 먼저 찾았잖아요. 지금은 도현 씨가 저 좀 봐 주세요.','보고 있었어요. 오늘 예쁘다는 말부터 해야 했는데요.'))
beat('ria_r15','home',1,'리아가 쿠션을 고쳐 놓고 먼저 옆자리를 가리킨다. 도현이 앉자 장난스럽게 웃는다.','오늘은 길 안내 안 해. 그래도 내 옆자리는 바로 찾네~','여긴 지도 없어도 와.',('오늘은 길 안내 안 해요. 그래도 제 옆자리는 바로 찾으시네요~','여긴 지도 없어도 와요.'))
beat('ria_r15','cosplay',1,'리아는 문가에 서서 반응을 기다리다 웃음을 터뜨렸다. 준비해 둔 인사말은 꺼내지 못했다.','잘 어울린다는 말은 들었는데. 네가 웃으니까 나도 자꾸 웃게 되잖아!','옷도 좋은데, 신나서 보여 주는 네가 더 좋아.',('잘 어울린다는 말은 들었는데요. 도현 씨가 웃으시니까 저도 자꾸 웃게 되잖아요!','옷도 좋은데, 신나서 보여 주시는 리아 씨가 더 좋아요.'))
beat('yujin_r07','casual',1,'유진이 숨을 한번 고르고 먼저 시선을 맞춘다. 얼굴이 붉어져도 이번에는 고개를 돌리지 않았다.','저 부끄러운 건 맞아요. 그래도 오늘 먼저 부른 건 저니까... 조금 더 봐 주세요.','네. 저도 피하지 않을게요. 유진 씨 보고 싶어서 왔어요.')
beat('yujin_r12','special',1,'유진이 옷소매를 정리하고 도현 쪽으로 몸을 돌렸다. 작게 웃으며 대답을 기다린다.','옷 오래 골랐다고 말씀드렸잖아요. 오늘은 제가 어떤 표정인지도 봐 주세요~','아까보다 덜 긴장하신 것 같은데요. 저는 반대고요.')
beat('yujin_r15','home',1,'유진이 먼저 옆자리에 앉았다. 차를 권하던 목소리 끝에 작은 웃음이 붙는다.','지금도 제가 먼저 말할 때까지 기다리시는 거예요? 오늘은 도현 씨 말도 듣고 싶은데요~','좋아해요. 그 말은 기다리게 하지 않을게요.')
beat('yujin_r15','cosplay',1,'유진은 함께 고른 의상의 소매를 펴고 도현을 바라본다. 웃는 얼굴은 조금 붉었다.','어울린다는 말, 한 번 더 듣고 싶어요. ...오늘은 제가 욕심 좀 내도 되죠?','잘 어울려요. 오늘 자꾸 보게 되는 것도 진심이고요.')
beat('jihyun_r07','casual',1,'지현이 준비한 말을 고르다 작게 웃었다. 평소처럼 또렷하게 이어지지 않는 말끝을 도현에게 내보인다.','회사에선 말 잘한다고들 하는데. 너 앞에서는 다음 말이 잘 안 나와.','지금도 좋아요. 정리 안 된 말도 제가 듣고 싶어요.')
beat('jihyun_r12','special',1,'지현이 소매에서 손을 떼고 도현의 눈을 본다. 잠깐 내려갔던 입꼬리가 다시 올라간다.','아까 예쁘다는 말. 나 오늘 그거 한 번 더 듣고 싶어.','예뻐요. 오늘 만나길 잘했다고 계속 생각하고 있어요.')
beat('jihyun_r15','home',1,'지현이 덮어 둔 일정표를 옆으로 밀었다. 도현 쪽으로 고개를 기울이며 낮게 웃는다.','오늘은 내가 다 챙기기 전에 네가 먼저 불러 줘. 그게 좀 좋더라.','지현 씨. 오늘도 같이 있어서 좋아요.')
beat('jihyun_r15','cosplay',1,'지현이 재킷의 단추를 만지다 손을 내린다. 도현의 시선을 알아채고 먼저 웃었다.','감상은 들었는데. 오늘은 조금 더 칭찬받고 싶네. 이런 말 내가 먼저 할 줄은 몰랐어.','멋있고, 지금 웃으실 때는 귀여워요. 둘 다 말씀드려도 되죠?')
beat('seoyun_r07','casual',1,'서윤이 말을 꺼내려다 웃었다. 이번에는 익숙한 농담을 붙이지 않고 도현의 대답을 기다린다.','나 원래 조용해지면 무슨 말부터 할지 찾거든. 지금은 네가 먼저 해 줬으면 좋겠어.','보고 싶었어요. 오늘은 옆에서 더 오래 얘기하고 싶고요.')
beat('seoyun_r12','special',1,'서윤이 가방을 옆으로 밀어 놓았다. 휴대폰 대신 도현을 바라보는 시간이 조금 길어진다.','오늘은 네가 말 좀 골라 줘. 나 계속 네 얼굴 보느라 아까 생각한 걸 잊었어.','그럼 예쁘다는 말부터요. 다음 말은 저도 조금 기다려 주세요.')
beat('seoyun_r15','home',1,'서윤이 달력을 멀리 놓고 도현 쪽으로 몸을 돌린다. 웃으며 내놓는 말이 평소보다 짧았다.','나 오늘은 멋있는 대답 안 해도 돼? 그냥 네가 좋다고 하고 싶어서.','네. 저도 그 대답이 제일 좋아요.')
beat('seoyun_r15','cosplay',1,'서윤이 재킷 소매를 펴다가 도현과 눈이 마주쳐 웃었다. 준비한 장난은 잠깐 미뤄 둔다.','네 표정 바꿔 보려고 입었는데. 지금은 내 쪽이 더 들킨 것 같네.','보여 주고 싶다고 하실 때부터 반가웠어요. 지금 웃으시는 것도요.')
p.write_text(json.dumps(events,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(proof/'edit-log.json').write_text(json.dumps(edits,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(edits=len(edits),files=sorted({e['file'] for e in edits})),ensure_ascii=False))
