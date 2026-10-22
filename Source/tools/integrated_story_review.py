"""Apply the 0.28 integrated continuity pass, preserving existing choices/state."""
from pathlib import Path
import hashlib
import json

P = Path(__file__).resolve().parents[1]
D = Path('C:/Users/user/Desktop/건/오피스 V2')
proof = P / 'testing/integrated-review-v1'
proof.mkdir(parents=True, exist_ok=True)
names = ['common.rpy', 'core.rpy', 'options.rpy', 'office_phone.rpy']
names += [f.name for f in (P / 'game').glob('*.rpy') if f.name.startswith(('ria_r', 'jihyun_r', 'yujin_r', 'seoyun_r')) or f.name.endswith('_optional.rpy')]
names.append('event_story.json')
if not (proof / 'baseline.json').exists():
    baseline = {'version': '0.27.0-romance-focus', 'files': {}, 'runtime': {}}
    for name in names:
        src = P / 'game' / name
        installed = D / '개발자료/source/game' / name
        assert src.read_text(encoding='utf-8-sig') == installed.read_text(encoding='utf-8-sig'), name
        (proof / (name + '.before')).write_bytes(src.read_bytes())
        baseline['files'][name] = hashlib.sha256(src.read_bytes()).hexdigest()
        compiled = name.replace('.rpy', '.rpyc')
        baseline['runtime'][compiled] = hashlib.sha256((D / 'game' / compiled).read_bytes()).hexdigest()
    (proof / 'baseline.json').write_text(json.dumps(baseline, ensure_ascii=False, indent=2), encoding='utf-8')
baseline = json.loads((proof / 'baseline.json').read_text(encoding='utf-8'))
for name in names:
    if name not in baseline['files']:
        src = P / 'game' / name
        assert src.read_bytes() == (D / 'game' / name).read_bytes()
        (proof / (name + '.before')).write_bytes(src.read_bytes())
        baseline['files'][name] = hashlib.sha256(src.read_bytes()).hexdigest()
        baseline['runtime'][name] = hashlib.sha256((D / 'game' / name).read_bytes()).hexdigest()
(proof / 'baseline.json').write_text(json.dumps(baseline, ensure_ascii=False, indent=2), encoding='utf-8')
texts = {n: (proof / (n + '.before')).read_text(encoding='utf-8-sig') for n in names}
current = {n: (P / 'game' / n).read_bytes() for n in names}

changed = {}
def replace(name, old, new):
    path = P / 'game' / name
    text = texts[name]
    assert text.count(old) == 1, (name, old[:100], text.count(old))
    texts[name] = text.replace(old, new)
    changed[name] = changed.get(name, 0) + 1

replace('common.rpy', 'd "아까 보낸 확인 질문에는 답이 왔나요?"', 'd "첫날 같이 쓴 답장, 그 뒤엔 어떻게 됐어요?"')
replace('ria_r01.rpy', '리아가 자기 컵을 든 채 회사 앞에서 잠깐 기다리고 있다.', '리아가 휴대폰을 든 채 회사 앞에서 잠깐 기다리고 있다.')
replace('ria_r01.rpy', '리아는 컵을 내려놓고 옆 의자를 당긴다.', '리아는 가방을 내려놓고 옆 의자를 당긴다.')
replace('ria_r01.rpy', '리아는 자기 컵을 테이블에 내려놓는다.', '리아는 가방을 옆 의자에 내려놓는다.')
replace('ria_r01.rpy', '    $ location = "둘이 앉은 자리"', '    $ location = "둘이 앉은 자리"\n    "도현은 따뜻한 라테를, 리아는 마시고 싶은 음료를 골랐다. 음료가 나온 뒤에도 둘은 자리를 뜨지 않았다."')
replace('ria_r02_r04.rpy', '''    else:
        d "[ri('걷면서 얘기 좀 더 하자.', '걸으면서 얘기 좀 더 해요.')]"
        if r02_plan''', '''    else:
        if not memory.get("choice_third_r02_affection"):
            d "[ri('걷면서 얘기 좀 더 하자.', '걸으면서 얘기 좀 더 해요.')]"
        if r02_plan''')
replace('ria_r02_r04.rpy', '    "대화가 잠깐 끊긴다. 리아는 휴대폰을 가방에 넣고 편하게 기대 앉는다."', '    "각자 고른 음료를 앞에 두고 이야기를 나눴다. 대화가 잠깐 끊기자 리아는 휴대폰을 가방에 넣고 편하게 기대 앉는다."')
replace('ria_r13_e01.rpy', "오는 길에는 도착하면 한 번만 알려 줘~', '알겠어요. 도착하면 한 번만 알려 주세요~", "가는 길 조심하고, 도착하면 한 번만 알려 줘~', '알겠어요. 가시는 길 조심하시고, 도착하시면 한 번만 알려 주세요~")
replace('ria_r13_e01.rpy', "좋아. 아까 진 가게 찾기 승부는 여기서 다시 할까?', '좋아요. 아까 진 가게 찾기 승부는 여기서 다시 할까요?", "좋아. 아까 무승부였던 가게 찾기, 여기서 결판낼까?', '좋아요. 아까 무승부였던 가게 찾기, 여기서 결판낼까요?")
replace('ria_r13_e01.rpy', "응. 오늘은 빈손으로 와도 돼. 내가 먼저 손 흔들 테니까~', '네. 오늘은 빈손으로 오셔도 돼요. 제가 먼저 손 흔들 테니까요~", "응. 다음엔 빈손으로 와. 내가 먼저 손 흔들 테니까~', '네. 다음엔 빈손으로 오세요. 제가 먼저 손 흔들 테니까요~")
replace('ria_r13_e01.rpy', '약속한 시각에 인사하고 각자의 집으로 돌아갔다.', '약속한 시각에 도현이 돌아갈 준비를 했다. 리아는 현관까지 배웅한 뒤 문 앞에서 손을 흔들었다.')
replace('office_phone.rpy', '응! 별일 없어도 연락해도 된다고 했잖아. 바로 해 봤지~", "네! 별일 없어도 연락해도 된다고 하셨잖아요. 바로 해 봤죠~', '응! 별일은 없는데 네 생각이 나서. 오늘은 내가 먼저~", "네! 별일은 없는데 도현 씨 생각이 나서요. 오늘은 제가 먼저예요~')
replace('jihyun_r13_e01.rpy', '오늘 옷, 지현 씨가 골랐죠? 잘 어울려요.', "오늘 옷, 잘 어울려요. [memory.get('jihyun_private_name', '지현 씨')]한테 그 말부터 해야 했는데.")
replace('jihyun_r13_e01.rpy', '그 길 말고 다른 데 고를 수도 있어요. 그래도 지현 씨 보러 온 건 같은 거고요.', "그 길 말고 다른 데 고를 수도 있어요. 그래도 [memory.get('jihyun_private_name', '지현 씨')] 보러 온 건 같은 거고요.")
replace('jihyun_r13_e01.rpy', '비 오던 날은 우리 둘 다 가방부터 닫았지. 오늘은 비도 없는데 네가 또 멀어지면 내가 잡을 거야.', '비 오던 날엔 가려던 데 못 가고도 같이 있었지. 오늘도 다른 데 찾느라 먼저 일어나진 마.')
replace('jihyun_optional.rpy', '의자가 창가를 보네요. 지현 씨가 그렇게 두신 거예요?', "의자가 창가를 보네요. [memory.get('jihyun_private_name', '지현 씨')], 이건 직접 고르신 자리예요?")
replace('yujin_r01_r04.rpy', '오늘 퇴근길에 한 장 찍어 왔어요.', '오늘 퇴근길에 몇 장 찍어 왔어요.')
replace('yujin_r01_r04.rpy', '도현이 카페로 오며 찍은 골목 사진을 보여 줬다.', '도현이 카페로 오며 찍은 골목 사진 두 장을 차례로 보여 줬다.')
replace('yujin_r05_r08.rpy', '네. 그럼 오늘은 이쪽 손을 주실래요? 노트는 제가 들고 있을게요.', '네. 그럼 오늘은 이쪽 손을 주실래요? 가방은 옆에 두시고요.')
replace('yujin_r05_r08.rpy', '유진이 노트를 돌려주고 도현과 걸음을 맞췄다.', '유진이 벤치에서 일어나 도현과 걸음을 맞췄다.')
replace('yujin_r05_r08.rpy', '    "밖으로 나와 작은 공원 벤치에 앉았다. 도현은 사진과 글을 묶어 보던 노트를 잠깐 펼쳤다."', '    $ location = "같은 토요일 오후 · 작은 공원 벤치"\n    "밖으로 나와 작은 공원 벤치에 앉았다. 도현은 사진과 글을 묶어 보던 노트를 잠깐 펼쳤다."')
replace('yujin_r05_r08.rpy', '노트를 덮은 뒤에도 둘은 자리를 바로 옮기지 않았다.', '유진이 그림을 책상에 세워 두고 차를 내왔다. 도현 쪽 잔의 손잡이를 돌려 놓다가 눈이 마주치자, 이번에는 먼저 웃었다.')
replace('yujin_r09_r12.rpy', '제가 먼저 왔는데요? 오늘은요.', '오늘은 제가 집에서 기다렸는데요? 다음엔 제가 찾아갈게요~')
replace('yujin_r13_e01.rpy', '아, 잠깐만요. 아까는 제가 먼저 웃겠다고 했는데.', '아, 잠깐만요. 끝나면 제가 먼저 웃어 드리려고 했는데.')
replace('yujin_r13_e01.rpy', '유진은 빈 접시를 치우고 돌아와 아까 도현이 옮겨 앉은 자리에 그대로 앉았다.', '과자를 다 먹은 뒤 유진이 접시를 치웠다. 돌아와서는 도현 옆, 아까 자기가 비워 둔 자리에 앉았다.')
replace('yujin_r13_e01.rpy', '팀장님이 두 사람 다음에도 같이 보자고 하셨어요. 아직 다른 분들께는 말씀 안 하셨대요.', '팀장님 답장 기억나요? 수정 의견 안 보태신다고요. 축하한다는 말만 들으니까 기분 좋았어요~')
replace('seoyun_r05_r12.rpy', '아침에 책 옮겨 놓은 자리 보이네. 지금은 다시 혼자 읽는데, 네 다음 말이 더 궁금해.', '아침에 네가 반 나눠 준 거, 점심에도 또 생각났어. 내 접시에 있던 걸 도로 받았는데 이상하게 더 맛있더라~')
replace('seoyun_r05_r12.rpy', '같이 아침을 먹었다. 서윤이 도현의 접시로 잘 익은 쪽을 밀어 주자,', '같이 아침을 먹었다. 서윤이 도현의 접시로 잘 구워진 빵을 밀어 주자,')
replace('seoyun_r05_r12.rpy', '어제 보여 준 독서 자리, 오늘도 한 칸 비어 있네. 다음에 또 앉아 줬으면 좋겠어.', '어제 네가 앉았던 소파 자리, 오늘은 내가 차지했어. 다음엔 또 옆으로 비켜 줄게~')
replace('seoyun_r13_e01.rpy', '네. 한 잔만요. 대신 서윤 씨가 추천한 음식은 제가 고를게요.', '네. 한 잔만요. 술은 추천받았으니까 음식은 제가 골라도 돼요?')
replace('seoyun_r13_e01.rpy', '오, 교환 조건이 생겼네? 좋아. 오늘은 네가 고른 걸 먹어 볼게.', '오, 교환 조건이 생겼네? 좋아. 오늘은 네가 고른 걸 먹어 볼게. 중간에 바꿔 달라고는 안 할게~')
replace('seoyun_r13_e01.rpy', '나머지는 같이 있을 때 읽을래. 오늘은 네가 자꾸 멀리 앉는 게 더 궁금해.', '나머지는 조금 있다 읽을래. 오늘은 네가 맞은편에 앉은 게 더 신경 쓰여서.')
replace('seoyun_r13_e01.rpy', '방금은 제가 먼저 왔는데요.', '얼굴 잘 보이는 자리부터 골랐는데요.')
replace('seoyun_r13_e01.rpy', '그럼 한 칸 더.', '옆에서도 보여. 한 칸만 더 와~')
replace('seoyun_r13_e01.rpy', '전에 서로 다른 데서 읽다 말고 네 쪽으로 옮겨 갔었지. 오늘도 내가 먼저 갈까?', '같은 대목 읽고도 서로 다른 데서 멈췄지. 네 얘기 듣고 다시 읽던 게 좋았어.')
replace('seoyun_r13_e01.rpy', '같이 살 준비, 이제는 해 보고 싶어. 비용이랑 출퇴근, 각자 쓸 자리... 나도 적어 올래. 언제 같이 볼까?', '우리, 같은 집에 들어가는 날도 있었으면 좋겠어. ...당장 집 보러 가자는 건 아니고. 네가 먼저 열쇠 돌리는 소리 같은 게 좀 궁금해졌어.')
replace('seoyun_r13_e01.rpy', '''    menu:
        "다음 달 둘째 토요일 오후 두 시에 비용과 통근 조건을 맞춰 본다.":
            d "그날 서로 생활비랑 통근 조건 적어 와요. 가능한 범위를 같이 보죠."
            s "응. 다음 달 둘째 토요일 두 시, 여기서. 내 출퇴근 조건도 적어 올게."''', '''    menu:
        "같이 살 비용과 출퇴근부터 알아보자고 한다.":
            d "그럼 저도 계산 좀 해 올게요. 생활비랑 출퇴근부터요. 다음 달 둘째 토요일 두 시 어때요?"
            s "응. 그날 여기서 보자. 나도 알아보고 올게. 네가 집에 먼저 오는 날이 많을까, 그거부터 생각했네."''')
replace('seoyun_r13_e01.rpy', '''        "두 주 뒤 일요일 오후 세 시에 각자의 공간과 생활 시간을 이야기한다.":
            d "책상하고 혼자 쉴 자리, 생활 시간부터요. 두 주 뒤 일요일 세 시 어때요?"
            s "좋아. 여기서 각자 적어 온 걸 놓고 보자. 아직 답 안 맞는 것도 같이."''', '''        "각자 쉴 자리와 하루의 생활부터 이야기해 보자고 한다.":
            d "제 책상 옆엔 아무것도 안 두는 의자가 있어요. 앉아서 멍하니 있으려고요. 그런 것부터 얘기해 봐요. 두 주 뒤 일요일 세 시에 여기서요."
            s "좋아. 그 의자도 적어 와. 내가 짐 올려놓으면 안 되는 자리네~"''')
replace('seoyun_r13_e01.rpy', '''        "다음 달 첫 토요일 오후 두 시에 준비 목록과 결정 순서부터 정한다.":
            d "뭐부터 알아볼지 같이 적어요. 결정이 필요한 날도 그때 정하고요."
            s "응. 첫 토요일 두 시. 내가 궁금한 것부터 적어 올게. 네 목록이랑 나란히 놓고 보자."''', '''        "서로 궁금한 것부터 적어 와 하나씩 알아보자고 한다.":
            d "저 지금 궁금한 게 너무 많아요. 다음 달 첫 토요일 두 시에 여기서 하나씩 골라 볼까요? 집은 그 뒤에 보고요."
            s "응. 나도 적어 올게. 첫 줄은 벌써 생각났어. ...그건 그날 보여 줄래."''')
replace('seoyun_r13_e01.rpy', '두 사람은 각자 달력에 같은 약속을 적었다. 아직 계약한 집도, 정해 놓은 입주일도 없었다.', '두 사람은 달력에 다음 만남을 적었다. 서윤은 그 옆에 작은 열쇠를 그렸다가, 도현이 보자 펜으로 반쯤 가렸다.')
replace('event_story.json', '"title": "노트를 덮고",\n        "narration": "유진이 노트를 덮어 두고 도현과 마주 앉는다."', '"title": "잔을 내려놓고",\n        "narration": "유진이 찻잔을 내려놓고 옆에 앉은 도현을 본다."')
replace('event_story.json', '유진이 먼저 옆자리에 앉았다. 차를 권하던 목소리 끝에 작은 웃음이 붙는다.', '유진이 도현 옆에서 몸을 조금 돌렸다. 먼저 부르던 목소리 끝에 작은 웃음이 붙는다.')
replace('event_story.json', '''"yujin_r15": {
    "home": [
      {
        "title": "먼저 고른 마음",
        "narration": "유진이 문가에서 돌아와 도현과 마주 앉는다."''', '''"yujin_r15": {
    "home": [
      {
        "title": "먼저 고른 마음",
        "narration": "유진이 도현 옆에 편하게 앉아, 먼저 그의 얼굴을 바라본다."''')
replace('event_story.json', '"title": "책을 덮은 자리",\n        "narration": "서윤이 책을 덮고 옆자리를 비운다.",\n        "heroine": "여긴 책보다 네 다음 말 기다리는 자리 됐네."', '"title": "비워 둔 옆자리",\n        "narration": "소파에 나란히 앉은 서윤이 도현 쪽으로 몸을 조금 돌린다.",\n        "heroine": "아까는 멀리 서 있더니. 여기 앉으니까 어때?"')
replace('event_story.json', '''"title": "같은 책갈피",
        "narration": "잠시 뒤, 서윤은 탁자 위 책갈피를 집어 책 사이에 넣었다.",
        "heroine": "오늘 읽던 데는 여기였네. 다음에는 이다음부터 같이 볼래?",
        "dohyun": [
          "좋아요. 오늘 얘기도 그 옆에 기억해 둘게요.",
          "좋아요. 오늘 얘기도 그 옆에 기억해 둘게요."
        ]''', '''"title": "소파의 두 자리",
        "narration": "잠시 뒤 서윤이 도현을 보고 웃었다. 처음 비워 두었던 옆자리는 이제 비어 있지 않았다.",
        "heroine": "다음엔 내가 부를 때까지 거기 서 있지 마. 옆에 오고 싶으면 말해 줘.",
        "dohyun": [
          "네. 다음엔 제가 먼저 앉아도 되냐고 물을게요.",
          "네. 다음엔 제가 먼저 앉아도 되냐고 물을게요."
        ]''')
replace('event_story.json', '잠시 뒤 두 사람은 찻잔을 들고 나란히 앉았다.', '잠시 뒤 두 사람은 물잔을 들고 나란히 앉았다.')
replace('options.rpy', '0.27.0-romance-focus', '0.28.0-integrated-review')
for name in changed:
    assert (P / 'game' / name).read_bytes() == current[name], ('Concurrent source edit', name)
for name in changed:
    (P / 'game' / name).write_text(texts[name], encoding='utf-8')
(proof / 'edits.json').write_text(json.dumps(changed, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(changed, ensure_ascii=False))
