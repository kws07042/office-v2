from pathlib import Path
import re,json,shutil,difflib
P=Path(__file__).resolve().parents[1];S=P.parent;proof=P/'testing/opening-v1';H=S/'afterwork-opening-handoff-v1'
for d in ('docs','source/game','validation','screenshots'):(H/d).mkdir(parents=True,exist_ok=True)
changed=json.loads((proof/'changed-files.json').read_text(encoding='utf-8'))
scenes=[];delta=0
def blocks(t):
 m=list(re.finditer(r'^label (\w+)(?:\(|:)',t,re.M));return {v[1]:t[v.start():m[i+1].start() if i+1<len(m) else len(t)] for i,v in enumerate(m)}
for n in changed:
 before=(proof/(n+'.before')).read_text(encoding='utf-8');after=(P/'game'/n).read_text(encoding='utf-8')
 if n!='options.rpy':
  for pattern in (r'^\s*\$.*$',r'^\s*(?:call|jump|return).*$',r'^\s*".*":\s*$'):
   compared=after.replace('가까운 곳을 찾아보고 다음 후보는 리아에게 부탁한다.','내가 가까운 곳을 하나 찾아볼게. 다음 후보는 네가 골라 줘.') if n=='ria_r02_r04.rpy' else after
   assert re.findall(pattern,before,re.M)==re.findall(pattern,compared,re.M),(n,pattern)
 old,new=blocks(before),blocks(after)
 scenes.extend({'file':n,'label':k} for k in old if old[k]!=new[k]);delta+=len(after)-len(before)
 shutil.copy2(P/'game'/n,H/'source/game'/n)
 (H/'validation'/(n+'.diff')).write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile=n+' 0.21.0',tofile=n+' 0.22.0')),encoding='utf-8')
contract={'version':'0.22.0-opening-review','changed_files':changed,'changed_scene_blocks':len(scenes),'scenes':scenes,'net_source_characters':delta,'state_calls_awards_unchanged':True,'choice_semantics_unchanged':True,'choice_wording_fix':'ria R02 third option neutral action caption','intentional_presentation_branches':['seoyun R03 prop follows selected promise','jihyun R04 address callback follows actual next-date choice'],'images_changed':0}
(proof/'source-contract.json').write_text(json.dumps(contract,ensure_ascii=False,indent=2),encoding='utf-8');shutil.copy2(proof/'source-contract.json',H/'validation/source-contract.json')
source=(P/'tools/prepare_full_editorial_handoff.py').read_text(encoding='utf-8')
exec(compile(source[source.index('groups='):source.index('\nprefix=')].replace('0.20.0','0.22.0'),'current_dialogue_documents','exec'))
md=f'''# 초반 연속 편집·네 루트 비교 — 0.22.0 / 기획 v2.95

2026-10-20. 공통 C01~C08, 리아 R01~R04를 먼저 이어 읽고, 지현·유진·서윤 R01~R04의 실제 원문·조건·선택 반응을 비교했다. 실제 {len(scenes)}개 장면 블록을 수정했다. 새 사건·CG·그림·음성·외부 자산은 추가하지 않았다. 현재 사건 수·애정 표현 동의/미룸·호감도·핵심 분기·날짜 약속과 기억 갱신은 유지했다. 서윤 R03 소품과 지현 R04 실제 호칭에 기존 선택 값을 읽는 표현 분기를 추가했다. 리아 R02의 세 번째 선택은 존댓말 경로에서도 반말로 보이던 문구를 중립적인 행동 설명으로 바꿨으며 결과는 같다.

## 1. 공통부터 리아 고백까지

C01: 세 업무 선택이 같은 마무리로 붙기 전에, 표지를 직접 조정하며 손으로 신호하기 / 담당자 말을 듣고 손님 자리에서 확인하기 / 둘이 다른 쪽에서 같은 문제를 찾기로 반응을 구분했다. 새 사건을 세 개 만든 것이 아니다. C02는 근거의 범위·미확인 상태를 보존하면서 의견을 내도 된다는 반복 설명을 줄였다. C03 색과 메시지 선택에는 도현의 실제 구매 관점과 유진의 짧은 응수를 넣었다. C04는 혼자 다 알아서 해결하지 않는다는 해설을 보내고도 답장 창을 다시 여는 서윤의 행동으로 바꿨다.

C05는 메뉴를 정하는 설명과 식사 완료 지문 중복을 줄였다. 네 사람이 서로 다른 취미를 가진다는 소개와 제목 장난은 살렸다. C06 리아는 매번 다음에 또 말 걸겠다는 약속 대신 서로 상대가 일어나기를 기다린 어긋남으로 끝낸다. C07 유진은 같은 취향을 존중한다는 추상적 대사보다 그늘로 의자를 옮기고도 자기 자리라고 주장하는 작은 장난을 남겼다.

리아 R01~R02: 취향 시험이 아니라는 설명을 창가를 같이 보고 싶다는 말로 바꿨다. 휴무 경로에서 다음 만남을 실패로 만들 필요 없다는 교훈 대신 휴무 안내 사진을 찍자는 응수를 넣었다. 사용자가 골랐던 R02의 ‘그럼 내가 아는 네가 하나 더 생기는 거지’는 유지했다.

리아 R03: 식사를 이미 주문한 뒤 ‘아직 주문 안 했다’고 말하던 순서 오류를 고쳤다. 메뉴는 먼저 펼치고, 주문은 뒤에 하도록 읽힌다. 혼자 걷기·같이 걷기·직접 말하기를 되풀이하던 설명을 덜었다. 빈 컵을 핑계로 더 머무는 장난과 실제 금요일 일곱 시 약속은 유지했다. 사진에 리아를 이미 찍었다는 회상은 없다. 사람 사진은 먼저 묻겠다고 말할 뿐이다.

리아 R04: 말로만 인사하는 선택 뒤에도 다음 약속을 또 정하던 대사 대신, 리아가 좋아한다는 말을 한 번 더 돌려주는 반응으로 바꿨다. 이 경로에서 입맞춤이나 포옹이 발생했다고 쓰지 않는다. 준비 대화는 첫 연애·혼자 끙끙대는 약점은 남기고 관계 운영 규칙의 중복을 압축했다.

## 2. 나머지 세 루트의 초반 밀도

지현: R01 국수를 앞에 두고도 뜨거워 바로 못 먹는 짧은 행동과 추천한 메뉴를 칭찬받고 싶은 마음을 더했다. R02는 조용한 장소·따뜻한 차·네 시 귀가를 지키면서 조건을 여러 번 확인하는 문장을 줄였다. R03은 업무 결과와 사적 호감을 분리하되, 업무 원리를 두 번 설명하지 않는다. 실제 미제출 경로의 ‘결과는 아직 못 봤으니까’는 보존했다.

유진: R02의 ‘설명 듣고 오길 잘했다’는 말은 설명자가 아닌 동행을 원한다는 R01과 어긋나므로 고쳤다. R03은 제목을 보여 주겠다고 해 놓고 후보를 실제로 말하지 않던 빈칸을 채웠다. 도현의 ‘한 번 더 돌아본 골목’ 후보와 지나가던 사람이 있는 사진, 그 사람이 지나간 뒤 찍은 사진 얘기를 읽고 유진이 자기 취향을 고른다. 후반 R05의 최종 첫 장/제목을 미리 확정한 것은 아니다.

서윤: R01의 화제 선택 뒤 한 문장으로 끝나던 반응을 늘렸다. 궁금한 점 묻기에서는 도현의 커피가 늦게 식는 이유, 쉬는 얘기에서는 사진 확대 때문에 진도가 안 나가는 도현과 책을 되읽는 서윤, 직구에서는 더 앉고 싶은 마음을 실제로 받는다. R02에서는 같은 산문집을 읽어도 도현은 새 가게를 찾는 순간, 서윤은 바로 들어가지 않는 부분에 멈춘다. 기존 책과 대화 안의 행동이며 새 장소·CG가 아니다.

서윤 R03 오류: ‘아무것도 만들지 않고 쉬었다’ 경로에서 ‘메모를 다시 집었다’, ‘네가 고른 한 줄’을 공통으로 쓰던 부분을 분리했다. rest는 책에서 손을 떼고 상대 이야기를 듣는다. photo/sound는 도현이 실제로 보여 준 휴대폰 화면을 다시 본다. 사진 경로도 종이 메모를 가져왔다고 바꾸지 않았다.

## 3. 고백 장면의 구분

| 인물 | 먼저 말하는 쪽 | 구체적 계기·반응 | 첫 애정 표현 |
|---|---|---|---|
| 리아 | 도현 | 친구처럼 편하지만 연애하고 싶다는 직구, 컵 없는 손 모양을 리아가 알아채는 장난 | R04 입맞춤/말/손·기대기 선택 유지 |
| 지현 | 도현 | 토요일에 마신 차 이름을 찾아본 마음, ‘지현 씨’라고 먼저 부름. 지현은 답이 너무 빨랐는지 신경 쓰다가 기다렸음을 인정 | R05로 미룸 유지 |
| 유진 | 유진 | 전시 노트에서 그림보다 도현의 말을 먼저 읽게 되는 구체적 이유. 스스로 고른 말로 고백 | R05로 미룸 유지 |
| 서윤 | 서윤 | 남의 좋은 문장 대신 자기 말로 짧게 고백. 도현은 오늘 보여 줄 결과물 없이 서윤만 보러 왔다고 답함 | R04 입맞춤/손/말 선택 유지 |

지현도 리아처럼 ‘준비한 답을 다 잊었다’고 말하던 중복을 없앴다. 지현의 공사 구분·사적 부탁 거절·초반 비공개는 분명히 남겼다. 이 장면에서 한 번 ‘지현 씨’를 부른 뒤 다시 팀장님 호칭으로 돌아온 사실도 대사가 알아차리게 했다. 이후 호칭 변화 전체를 이번에 새로 정한 것은 아니다.

## 분량과 읽기 판정

‘고백까지60~90분’은 기존 목표이지 실제 독자가 측정한 성적표가 아니다. 신규 연결 검사에서는 공통부터 R04까지 네 루트×세 대표 경로의 실제 표시 대사·지문과 메신저를 기록한다. 표시 중(current)과 확정 이력(adv)을 중복 집계하지 않는다. 검사 자동 클릭의 수십 초를 실제 플레이 시간으로 쓰지 않는다.

세부 수치·가정에 따른 예상 범위는 ‘초반_분량과읽기시간_검토_v1.md’를 본다. 느리게 읽거나 클릭 대기를 강제해 목표 시간을 채우지 않는다. 실제 사람의 첫 플레이를 확보하기 전에는60~90분 달성을 선언하지 않는다. 실제 소스 문자 수 순증은 {delta:+,}자이며, 말맛을 살리기 위한 활동 추가와 설명 압축이 함께 있다. 모든 대사가 줄어든 것은 아니다.

## 남은 약점

리아 초반은 다른 세 루트보다 여전히 길다. 유진·서윤도 기록집을 통해 도현의 취향을 알아가는 큰 골격은 공유한다. ‘먼저 말하기/다음 질문’이라는 어휘가 완전히 없어지지는 않았다. 핵심 고백과 애정 표현에서는 명확함을 위해 일부 남겼다. 그림·음성·표정 움직임이 없는 현행판에서 텍스트의 호흡을 본 것이므로 완성 연출의 몰입감은 별도로 검증해야 한다.

이번 편집 판단은 ‘빈 문답을 실제 취향과 응수로 바꾸고, 고백 반응의 복제를 줄였다’다. 독자가 웃거나 설렘을 느꼈다는 관찰 결과와 같은 말은 아니다. 자동 검사와 편집 평가를 구분한다.
'''
(H/'docs/초반_연속검수와네루트비교_v1.md').write_text(md,encoding='utf-8');(P/'story/opening_editorial_v1.md').write_text(md,encoding='utf-8')
installed=Path('C:/Users/user/Desktop/건/오피스 V2/개발자료/docs')
prefix=f'''> 현행 갱신: 기획 v2.95 / Windows 0.22.0-opening-review — 2026-10-20
> 공통 C01~C08과 네 히로인 R01~R04 연속 검수. {len(scenes)}개 장면 블록을 수정하고, 리아의 중복 설명·지현과 리아의 겹치는 고백 반응·유진의 미제시 제목·서윤의 휴식 경로 허구 메모를 고쳤다. 현행은 ‘초반_연속검수와네루트비교_v1.md’와 각 ‘검수후_현행대본.md’를 우선한다.
> 사건 수·CG·연애/애정 표현 분기·선택지·호감도는 유지했다. 추가 지문은 새 그림이나 애니메이션 제작 완료를 뜻하지 않는다. 고백60~90분은 독자 실측 미완료 목표이며, 자동 클릭 시간을 독서 시간으로 쓰지 않는다.

'''
for n in ('퇴근 후 우리_v2_통합 기획서.md','퇴근 후 우리_95개 사건 명세_v1.md','기획_질문및결정대장.md','게임개발_완료까지_전체작업계획_v1.md','퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md','대사_감정기호와메신저이모티콘_기준_v1.md'):
 (H/'docs'/n).write_text(prefix+(installed/n).read_text(encoding='utf-8-sig'),encoding='utf-8')
guide='''퇴근 후, 우리 — Windows 초반 연속 편집판 0.22.0-opening-review

afterwork_script_prototype.exe 실행. 공통부터 시작해 C08에서 인물을 선택하거나 시작 화면에서 개인 대본을 확인합니다.
공통 C01~C08과 네 히로인의 R01~R04를 이어 읽고 반복 설명·선택 반응·고백 대비와 앞뒤 오류를 보강했습니다.
자세한 내용: 개발자료/docs/초반_연속검수와네루트비교_v1.md, 초반_분량과읽기시간_검토_v1.md 및 인물별 검수후 현행대본.md.
고백60~90분은 실제 독자의 플레이 시간으로 확인한 결과가 아닙니다. 자동 검사의 실행 시간과 구분합니다.
현재 텍스트89개 슬롯, 전체95계획 중 별도 업무 미니6개와 최종 그림·음성·영상·음원·Steam 기능은 별도입니다.
친밀한 본장면은 기존 생략·자리 표시이며, 새 지문이 현재 입상에서 모두 움직이는 것은 아닙니다.
기존 그림·리깅·저장은 유지합니다. 과거 중간 저장의 전체 호환성을 보장하지 않으므로 새 대본은 처음부터 확인하는 것을 권장합니다.
'''
(P/'WINDOWS-README.txt').write_text(guide,encoding='utf-8');(H/'시작안내.txt').write_text(guide,encoding='utf-8')
print(json.dumps({k:v for k,v in contract.items() if k!='scenes'},ensure_ascii=False))
