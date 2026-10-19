from pathlib import Path
import ast,json,re,difflib,shutil
P=Path(__file__).resolve().parents[1]; S=P.parent; proof=P/'testing/immersion-v1'; H=S/'afterwork-immersion-handoff-v1'
for d in ('docs','source/game','validation','screenshots'): (H/d).mkdir(parents=True,exist_ok=True)
changed=json.loads((proof/'changed-files.json').read_text(encoding='utf-8'))
def structure(text):
    rows=[]
    for row in text.splitlines():
        if not row.strip() or re.match(r'^\s*(?:[a-z]+\s+)?"',row) or row.startswith('define config.version'): continue
        if row.strip().startswith('call phone_deliver('):
            call=ast.parse(row.strip()[5:],mode='eval'); call.body.args[2]=ast.Constant('<dialogue>')
            rows.append(ast.dump(call,include_attributes=False))
        else: rows.append(row.rstrip())
    return rows
def blocks(text):
    positions=list(re.finditer(r'^label (\w+)(?:\(|:)',text,re.M))
    return {m[1]:text[m.start():positions[i+1].start() if i+1<len(positions) else len(text)] for i,m in enumerate(positions)}
scenes=[]; delta=0
for n in changed:
    before=(proof/(n+'.before')).read_text(encoding='utf-8'); after=(P/'game'/n).read_text(encoding='utf-8')
    assert structure(before)==structure(after),('Changed state/flow/call metadata',n)
    assert [s.strip() for s in before.splitlines() if s.strip().startswith('"') and s.rstrip().endswith(':')]==[s.strip() for s in after.splitlines() if s.strip().startswith('"') and s.rstrip().endswith(':')],('Changed choices',n)
    old=blocks(before); new=blocks(after)
    scenes.extend(dict(file=n,label=k) for k in old if old[k]!=new[k])
    delta+=len(after)-len(before)
    shutil.copy2(P/'game'/n,H/'source/game'/n)
    (H/'validation'/(n+'.diff')).write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=n+' 0.20.1',tofile=n+' 0.21.0')),encoding='utf-8')
report=dict(version='0.21.0-immersive-dialogue',changed_files=changed,changed_scene_blocks=len(scenes),scenes=scenes,net_source_characters=delta,branches_choices_flags_awards_unchanged=True,phone_ids_contacts_attachments_timing_unchanged=True)
(proof/'source-contract.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(proof/'source-contract.json',H/'validation/source-contract.json')

source=(P/'tools/prepare_full_editorial_handoff.py').read_text(encoding='utf-8')
exec(compile(source[source.index('groups='):source.index('\nprefix=')].replace('0.20.0','0.21.0'),'current_dialogue_documents','exec'))
md=f'''# 몰입·말맛 재집필 — 0.21.0 / 기획 v2.94

## 작업과 판정

공통과 네 개인 루트의 현재 대본을 다시 대조하고 실제 {len(scenes)}개 장면 블록을 재집필했다. 기존 잘 살아 있던 첫 만남·고백·요리 장난은 필요한 부분을 남겼다. 모든89개 슬롯을 새로 썼다는 뜻은 아니다. 변경 목록과 실제 원문 비교는 validation/source-contract.json 및 각 *.diff에 있다.

기존에는 ‘다음 말·먼저 말하기·함께 정하기·다음 초안’으로 비슷하게 끝나는 대화가 많았다. 이번에는 기존 취미와 장소 안에서 손이 움직이고, 상대가 장난을 되받고, 선택 뒤 반응이 달라지는 부분을 만들었다. 문장부호 일괄 치환은 하지 않았다. 바뀐 소스의 순증은 {delta:+,}자다. 지루한 설명을 덜고 행동과 응수를 늘린 결과이며 전체 분량이 줄었다거나 실제 읽기 시간을 달성했다고 주장하지 않는다.

새 사건·인물·CG·음성·외부 이모티콘은 추가하지 않았다. 친밀한 본장면의 기존 생략/자리 표시, 연애와 애정 표현의 동의·미룸, 호감도와 해금 조건을 유지했다. 선택지 문구·분기·상태 갱신·보상 및 메신저 ID/상대/첨부/입력 중 설정이 이전과 같은지도 원문 비교로 확인했다.

## 대표 수정 전후

### 공통 C05 — 취미 소개를 작은 소동으로

이전: ‘제목 몇 개요. 집에 가면 또 마음에 안 들지만요’ 뒤에 인물들이 차례로 보여 달라고 했다.

현재: 도현이 가제 ‘퇴근도 기획 중’을 말하자 지현은 ‘퇴근하고도 기획해야 해?’, 유진은 ‘제목만 봐도 아직 집에 못 갈 것 같아요’, 서윤은 ‘첫 독자 네 명을 야근시켰네~’로 다르게 받는다. 도현이 제목을 퇴근시키겠다고 받아치고 리아만 아직 표를 안 냈다며 편을 든다. 제목은 가제이며 최종 책 제목을 고정한 것은 아니다.

### 리아 R06·R10·O03 — 동갑 장난과 서로의 고집

R06의 ‘다음 코스 기다리는 게 아니라 네 말 듣는 중’이라는 설명을 바보 같은 일 하나 들려주겠다는 제안으로 바꿨다. 듣는 선택에서는 도현이 유리문에 비친 자신에게 길을 양보한 이야기를 실제로 하고 리아가 유리문 쪽을 보며 받아친다. 말을 꺼내기만 하고 다음 장면으로 넘어가지 않는다.

R10의 ‘나는 장소 안내 담당, 마지막 결정은 작가님’을 ‘빵집 빼라고 하면 한 번은 항의할 거야!’로 바꿨다. 공원은 빵집도 보인다며 항의를 아끼고, 빵집은 자기도 느려지는 사람에 포함한다. 장소 선택·촬영 전 후보 상태는 그대로다. O03의 각자 보기/한 장 같이 보기/하나씩 보고 덮기는 곁눈질 들킴·관찰 승부·다음 화 예고라는 다른 반응을 유지한다. 특정 R05 선택에서만 보았던 화분을 모든 경로의 회상에 넣지 않도록 다시 고쳤다.

### 지현 R02·R11 — 단정함 안의 승부욕

R02에서 차를 고르면 도현이 차보다 지현을 먼저 보고 있다는 응수, 산책이면 갈림길에서 망설였던 도현을 알아채고 돌아가는 반응, 서점이면 예쁜 책등부터 보고 싶었다고 먼저 인정하는 말로 갈라진다. 귀가 네 시 조건은 지켰다.

R11의 ‘같은 편 하고 싶어진다’는 설명을 실제 카드와 점수 앞의 대화로 바꿨다. 대결에서는 도현이 한 점 차이를 다시 세고 지현은 세 번째엔 두 점이 되겠느냐고 받아친다. 협동에서는 도현이 칭찬을 한 번 더 청하고, 점수 없는 놀이에서는 지현이 잼을 고집한다. 승패와 각 모드의 기억은 그대로 후반에 회수한다.

### 유진 R05·R06·O02 — 말보다 먼저 움직이는 관찰

R05의 세 구성 후보를 감상 문장만 다르게 말하던 방식에서 바람에 넘겨진 노트를 잡고, 사진을 가리며 기다리거나, 글로 상상한 길과 사진을 비교하거나, 손가락으로 간격을 재는 행동으로 나눴다. 사진·글·나란한 구성 값과 미완성 상태는 유지했다.

R06은 이전 추가 대사와 원래 약속 확인이 중복되던 부분의 호흡을 정리했다. 토요일15시 서점 약속은 상호 확인하고, 첫 입맞춤/손/말 인사는 여전히 별도 선택이다. O02는 컵 그림 감상 뒤 실제 잔을 들어 각도를 바꾸며 장난한다. 특정 감상 분기에서만 들은 ‘차가 식을 때까지 그렸다’는 설명을 다른 선택에서도 들었다고 쓰지 않았다.

### 서윤 R02·R05·R11 — 여유가 잠깐 늦어지는 순간

R02는 단골이어도 책 속 대목은 되돌아 찾는 행동을 넣었다. 질문을 기다려 주면 책을 덮고, 도현이 관심을 직구로 말하면 표정을 숨기지 못하고, 덜 골라도 된다고 하면 도현의 뜻밖의 답 앞에서 말을 고른다.

R05는 문/컵 소리, 그림자, 다시 올 이유의 선택에 컵을 내려놓기·손의 그림자 바꾸기·다음 잔 고르기라는 행동을 붙였다. 그림자 선택에서도 아직 촬영하지 않은 후보라는 조건을 지켰다. R11은 익숙한 계단의 새 화분을 늦게 알아채거나, 바람 핑계로 말을 꺼낸 도현에게 본인이 되묻거나, 반씩 고른 길에서 오늘만 돌아가고 싶었다는 답을 듣는 식으로 갈라진다.

## 말투와 문장부호 적용 기준

- 리아: 짧은 응수와 ~·!·가끔!!, 직구 앞에서는 짧아지는 말끝. 반말·존댓말 둘 다 실제 문장으로 편집한다.
- 지현: 간결한 마침표를 기본으로 사적 장난과 승부에만 ~, 칭찬 앞에는 짧은 ...를 사용한다. 항상 상사처럼 설명하지 않는다.
- 유진: 부드러운 존댓말을 유지하면서 먼저 제안하고 조용히 놀린다. 수줍다는 이유로 모든 대사를 ...로 시작하거나 허락만 구하게 하지 않는다.
- 서윤: 여유 있는 되묻기와 ~를 쓰되, 도현의 직구 뒤에는 컵·책·시선의 동작과 짧은 대답을 남긴다.
- 도현: 자기 고집·재치·작은 실수도 가진다. 매번 동의나 칭찬으로만 답하지 않는다. 진심은 짧게 말한다.
- 쉼표는 실제 숨을 쉬는 곳, 느낌표는 순간적인 감정 상승, 물음표는 상대가 답할 자리에 사용한다. !!!·~~를 사용량 목표로 삼지 않는다. 부호만으로 인물을 구별하지 않는다.

메신저10개 본문도 직접 대화와 구분했다. 리아는 한 줄을 세 번 읽고 휴대폰 탓을 하고, 지현은 실제 함께 보낸 아침의 접시를 떠올리거나 국수에 드문 :)를 붙인다. 유진은 노트 없이 와도 된다고 짧게 말하고, 서윤은 굳이 ‘농담 안 붙인다’고 설명하던 말을 덜었다. 기존 :)와 텍스트 기호만 사용했다. 답장을 재촉하거나 실제 시간 벌점을 만들지 않았다.

## 다시 읽으며 확인한 것

자기 편집 문장도 재검토했다. 물을 받기 전 받은 것처럼 말한 문장, 특정 분기에서만 나온 화분을 공통 기억처럼 말한 문장, 서술 전에 한 번 더 페이지를 넘기는 중복, 한 선택에서만 들은 스케치 이야기를 다른 선택에 붙인 문장, 아직 처음 받은 완성본을 전부 읽었다고 단정한 서술을 수정했다.

새 동작은 대본 지문이다. 실제 손·표정·입상 애니메이션을 이번에 제작한 것은 아니다. UI가 해당 행동을 모두 그려 보여 준다고 하지 않는다.

## 아직 약한 부분

R13~R14의 갈등 해결은 조건과 실제 행동을 확인해야 하므로 비교적 설명이 많다. 일부 비문·반복은 줄였지만 모두 웃긴 장면으로 바꾸지 않았다. 기록집을 공통 목표로 가진 탓에 R10·R16의 골격은 여전히 닮아 있다. 소재를 완전히 교체하려면 기존 사건 명세와 후반 기억까지 함께 바꾸는 별도 판단이 필요하다.

정확히6주 달력, 고백 도달60~90분, 업무 체감10~20%는 실측 읽기 목표로 남긴다. 자동 검사는 실행과 분기 안정성을 확인한다. 실제 플레이어가 계속 읽고 싶어 하는지, 웃음과 설렘이 살아나는지는 실속도로 읽는 평가가 필요하다. 이번 판정은 ‘활동과 응수가 있는 장면이 늘고 말투 대비가 나아짐’이며, 재미 완성·상품 완성 선언이 아니다.
'''
(H/'docs/몰입과말맛_재집필_검수기록_v1.md').write_text(md,encoding='utf-8')
(P/'story/immersion_editorial_v1.md').write_text(md,encoding='utf-8')
prefix=f'''> 현행 갱신: 기획 v2.94 / Windows 0.21.0-immersive-dialogue — 2026-10-19
> 실제 {len(scenes)}개 장면 블록을 재집필했다. 기존 장소·취미 안의 행동과 장난, 선택별 응수, 인물별 말투·문장부호 및 메신저 본문을 다듬었다. 현행은 ‘몰입과말맛_재집필_검수기록_v1.md’와 인물별 ‘검수후_현행대본.md’를 우선한다.
> 사건 수·CG 계획·핵심 분기·선택지·호감도·교제·애정 표현 조건은 유지했다. 새 그림·음성·외부 이모티콘은 추가하지 않았다. 실제 재미·읽기 시간과 실행 검사는 구분한다.

'''
for n in ('퇴근 후 우리_v2_통합 기획서.md','퇴근 후 우리_95개 사건 명세_v1.md','기획_질문및결정대장.md','게임개발_완료까지_전체작업계획_v1.md'):
    (H/'docs'/n).write_text(prefix+(S/'afterwork-romance-lines-handoff-v1/docs'/n).read_text(encoding='utf-8'),encoding='utf-8')
installed_docs=Path('C:/Users/user/Desktop/건/오피스 V2/개발자료/docs')
style_update='''> 현행 말투 기준 — 기획 v2.94 / Windows 0.21.0
> `, . ~ ! !! ? ?! ...`를 실제 호흡과 감정에 맞게 적극 활용한다. `~~`·`!!!` 이상은 드문 예외로 둔다. 일괄 덧붙임이나 인물별 사용량 할당은 하지 않는다. 부호와 함께 어휘·문장 길이·응수·행동을 편집한다.
> 리아는 빠른 동갑 장난과 짧은 직구, 지현은 간결한 문장 안의 승부욕과 사적 머뭇거림, 유진은 존댓말을 유지한 조용한 도발과 적극성, 서윤은 여유 있는 되묻기 뒤 예상이 빗나간 짧은 답을 쓴다. 도현도 자기 취향·실수·재치로 대화를 움직인다.
> 직접 대화는 행동과 표정 지문을 활용한다. 메신저는 짧은 본문과 기존 :) 등으로 구분하고, 모든 답장에 하트·말줄임표·입력 중 표시를 넣지 않는다. 외부 이모티콘·폰트·플러그인을 이번에 추가하지 않았다.
> 실제 적용 예시와 판정은 ‘몰입과말맛_재집필_검수기록_v1.md’를 우선한다. 아래 과거 버전의 미구현/폐기된 장면 배치는 역사 기록이며 현행 실행 범위는 최신 통합 기획서와 시작안내를 따른다.

'''
(H/'docs/대사_감정기호와메신저이모티콘_기준_v1.md').write_text(style_update+(installed_docs/'대사_감정기호와메신저이모티콘_기준_v1.md').read_text(encoding='utf-8-sig'),encoding='utf-8')
character_update='''> 현행 대본 보강 — 기획 v2.94 / Windows 0.21.0
> 연령·직무·이전 연애·핵심 성격·기존 사적 취향 설정은 유지한다. 말투를 구분하기 위해 리아의 지도·요리 장난, 지현의 취미 고집·카드 놀이 승부욕, 유진의 관찰과 작은 제안, 서윤의 되묻기와 예상 밖 답 앞의 망설임을 기존 장면에서 보강했다. 도현은 듣기만 하지 않고 자기 취향·작은 실수·받아치기로 관계를 움직인다.
> 각 특징을 매 장면 되풀이하는 공식으로 쓰지 않는다. 실제 상태·선택 기억과 상대의 거절은 유지한다. 새 동작은 현재 대본 지문이며 최종 표정·리깅·시점 CG까지 구현된 뜻은 아니다. 현행 대본과 변경 근거는 각 인물 ‘검수후_현행대본.md’와 ‘몰입과말맛_재집필_검수기록_v1.md’를 우선한다.

'''
(H/'docs/퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md').write_text(character_update+(installed_docs/'퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md').read_text(encoding='utf-8-sig'),encoding='utf-8')
guide='''퇴근 후, 우리 — Windows 대본 재집필판 0.21.0-immersive-dialogue

afterwork_script_prototype.exe 실행. 처음부터 또는 시작 화면의 개인 대본 확인으로 진행합니다.
공통·네 개인 루트의 반복 설명을 줄이고 기존 활동 안의 장난·선택 반응·인물별 말투를 보강했습니다.
자세한 전후 예시와 남은 약점은 개발자료/docs/몰입과말맛_재집필_검수기록_v1.md를 보세요.
각 인물의 검수후 현행대본 MD도 실제 소스로 갱신했습니다.
공통8·개인20×4·동료 결말1=89개 기본 텍스트 슬롯. 전체95계획의 별도 업무 미니6개와 일부 편의 기능·최종 아트·영상·음성·음원·Steam 기능은 별도입니다.
친밀한 본장면은 기존 생략·자리 표시입니다. 이번에 지문에 추가한 동작이 실제 그림·리깅으로 모두 재현되는 것은 아닙니다.
기존 그림·리깅·저장은 보존합니다. 모든 과거 중간 저장의 호환성을 보장한 것은 아니므로 새 루트는 처음부터 확인하는 것을 권장합니다.
로컬 개발용. GitHub 업로드·Steam 출시·외부 배포를 하지 않습니다.
'''
(P/'WINDOWS-README.txt').write_text(guide,encoding='utf-8'); (H/'시작안내.txt').write_text(guide,encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='scenes'},ensure_ascii=False))
