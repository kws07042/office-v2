from pathlib import Path
import difflib
import hashlib
import json
import re
import shutil

P = Path(__file__).resolve().parents[1]
S = P.parent
D = Path('C:/Users/user/Desktop/건/오피스 V2')
proof = P / 'testing/integrated-review-v1'
H = S / 'afterwork-integrated-review-handoff-v1'
version = '0.28.0-integrated-review'
for folder in ('docs', 'source/game', 'validation/tools'):
    (H / folder).mkdir(parents=True, exist_ok=True)
baseline = json.loads((proof / 'baseline.json').read_text(encoding='utf-8'))
changed = json.loads((proof / 'edits.json').read_text(encoding='utf-8'))

def logic(text):
    rows = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith(('define config.version', '$ location =')):
            continue
        if re.match(r'^(?:\w+\s+)?"', stripped):
            continue
        if stripped == 'if not memory.get("choice_third_r02_affection"):' or stripped.startswith('call phone_deliver('):
            if stripped.startswith('call phone_deliver('):
                rows.append(re.match(r'call phone_deliver\("([^"]+)",\s*"([^"]+)"', stripped).groups())
            continue
        rows.append(stripped)
    return rows

scenes = set()
for name in changed:
    old = (proof / (name + '.before')).read_text(encoding='utf-8-sig')
    new = (P / 'game' / name).read_text(encoding='utf-8-sig')
    assert old != new, name
    if name.endswith('.rpy'):
        assert logic(old) == logic(new), name
        assert len(re.findall(r'^\s+".*":\s*$', old, re.M)) == len(re.findall(r'^\s+".*":\s*$', new, re.M)), name
        old_lines = old.splitlines()
        for tag, first, last, _, _ in difflib.SequenceMatcher(a=old_lines, b=new.splitlines()).get_opcodes():
            if tag == 'equal':
                continue
            labels = re.findall(r'^label ([\w]+)', '\n'.join(old_lines[:first + 1]), re.M)
            if labels:
                scenes.add(labels[-1])
    else:
        a, b = json.loads(old), json.loads(new)
        assert a.keys() == b.keys()
        for event in a:
            assert a[event].keys() == b[event].keys()
            for variant in a[event]:
                assert len(a[event][variant]) == len(b[event][variant])
                assert all(x.keys() == y.keys() for x, y in zip(a[event][variant], b[event][variant]))
    diff = ''.join(difflib.unified_diff(old.splitlines(True), new.splitlines(True), fromfile=name + ' 0.27', tofile=name + ' 0.28'))
    (proof / (name + '.diff')).write_text(diff, encoding='utf-8')
    shutil.copy2(proof / (name + '.diff'), H / 'validation' / (name + '.diff'))
    shutil.copy2(P / 'game' / name, H / 'source/game' / name)
contract = {'version': version, 'changed_files': list(changed), 'edited_story_labels': sorted(scenes), 'story_flags_calls_awards_unchanged': True, 'menu_counts_unchanged': True, 'display_location_updated': '유진 R05 서점에서 공원 벤치로 이동한 뒤 HUD 장소 갱신', 'only_new_story_condition': '리아 R02 세 번째 느린 걸음 선택 직후 일반 대사 중복 생략', 'previous_runtime_hashes': {n.replace('.rpy', '.rpyc'): baseline['runtime'][n.replace('.rpy', '.rpyc')] for n in changed}, 'source_sha256': {n: hashlib.sha256((P / 'game' / n).read_bytes()).hexdigest() for n in changed}}
(proof / 'source-contract.json').write_text(json.dumps(contract, ensure_ascii=False, indent=2), encoding='utf-8')
shutil.copy2(proof / 'source-contract.json', H / 'validation/source-contract.json')

groups = {'공통': ['common.rpy', 'core.rpy'], '강리아': ['ria_r01.rpy', 'ria_r02_r04.rpy', 'ria_r05_r08.rpy', 'ria_r09_r12.rpy', 'ria_r13_e01.rpy'], '백지현': ['jihyun_r01_r04.rpy', 'jihyun_r05_r12.rpy', 'jihyun_r13_e01.rpy', 'jihyun_optional.rpy'], '차유진': ['yujin_r01_r04.rpy', 'yujin_r05_r08.rpy', 'yujin_r09_r12.rpy', 'yujin_r13_e01.rpy', 'yujin_optional.rpy'], '한서윤': ['seoyun_r01_r04.rpy', 'seoyun_r05_r12.rpy', 'seoyun_r13_e01.rpy', 'seoyun_optional.rpy']}
events = json.loads((P / 'game/event_story.json').read_text(encoding='utf-8'))
keys = {'강리아': 'ria', '백지현': 'jihyun', '차유진': 'yujin', '한서윤': 'seoyun'}
for who, names in groups.items():
    md = f'# {who} 검수 후 현행 대본 — {version}\n\n2026-10-21. 실제 실행 소스에서 추출했다. 조건·선택과 대사를 함께 보존한다. 본장면은 기존 자리 표시이며 아트·음성 최종본이 아니다.\n'
    for name in names:
        md += f'\n## {name}\n\n```renpy\n' + (P / 'game' / name).read_text(encoding='utf-8') + '\n```\n'
    if who in keys:
        md += '\n## 이벤트 전후 대화\n\n```json\n' + json.dumps({k: v for k, v in events.items() if k.startswith(keys[who] + '_')}, ensure_ascii=False, indent=2) + '\n```\n'
    (H / 'docs' / (who + '_검수후_현행대본.md')).write_text(md, encoding='utf-8')

review = '''# 공통·네 루트 통합 검수와 수정 — v3.01 / Windows 0.28.0

2026-10-21. 0.27.0을 기준으로 공통 C01~C08→R01~R16→선택 일상→후일담의 대본·연결·메신저를 검수했다. 기존 사건 수, 핵심 분기, 동의·거절, 복장·CG 배정은 유지한다. 새 그림·음성은 제작하지 않았다. 구현된 텍스트 슬롯은 89개이며 전체 95개 계획의 별도 업무 미니 6개는 이번 작업에 포함하지 않는다.

## 이어 읽을 때 발견한 문제

문장을 따로 읽으면 자연스럽지만, 이전 장면을 기억하며 읽으면 맞지 않는 대사가 남아 있었다. 삭제한 독서 장면을 다음 날 메시지가 회상하고, 이미 가방에 넣은 노트를 다시 건네며, 손님이 떠난 뒤 집주인까지 귀가하는 식이다. 대사 재집필 때 장면 전후와 선택 가지를 함께 갱신하지 못한 결과다. 이번에는 대본 원문뿐 아니라 이벤트 전후 JSON도 함께 대조했다.

| 대상 | 실제 수정 | 보존한 재미 |
|---|---|---|
| 공통 | C06 서윤 대화의 ‘아까 보낸 질문’을 ‘첫날 같이 쓴 답장’으로 수정. C04와 며칠 떨어진 시간에 맞춤. | C01 의자 없는 첫 출근, C05 기록집 가제에 대한 네 사람의 서로 다른 반응. |
| 리아 | R01 음료를 고르는 행동을 명시해 입가 거품 장난의 근거를 만듦. R02 세 번째 선택 직후 같은 요청을 반복하지 않게 함. R03 모든 자리 경로에 음료가 놓인 뒤 빈 컵 장난이 나오게 함. R15 무승부/패배 혼동, 귀가 방향을 고침. R16 ‘오늘 오라’는 말을 ‘다음 만남’으로 고침. E01은 도현만 귀가하고 리아는 배웅함. R08의 사전 허락 회상은 일부 경로에만 있었으므로 현재 먼저 연락하는 마음으로 씀. | R02 ‘그럼 내가 아는 네가 하나 더 생기는 거지’, R03 빈 컵으로 더 머물려는 장난, R11 실제 요리 담당 바꾸기. |
| 지현 | R15·O02 사적인 호칭에 R06에서 실제 선택한 이름을 사용. 오래된 단독 확인 경로도 오류가 나지 않도록 기본 호칭을 둠. E01은 O01에 없던 ‘둘 다 가방 닫기’를 회상하지 않고 실제 비로 계획이 바뀐 만남을 기억함. | R05 냅킨으로 만드는 축소 카페, R09 세 입 규칙을 도현에게 돌려주는 장난, R11 카드 게임의 작은 승부욕. |
| 유진 | R03 사진 한 장→두 장을 실제 보여 주는 흐름으로 맞춤. R05 보관한 노트를 다시 주고받지 않게 하고, 공원 이동 뒤에도 서점으로 남던 HUD 장소를 고침. R07에는 차를 내오는 행동을 넣어 이후 대사·메시지와 연결. R11 자기 집에서 ‘내가 먼저 왔다’는 말은 기다리는 쪽으로 정리. R15는 도현 자리를 빼앗아 앉는 지문을 자신의 옆자리로 바로잡고 과자 먹기→접시 치우기를 연결. R16은 실제 지현 답장만 회상. 생활복 이벤트에 없던 문가 이동·차 권하기도 수정. | R02 다른 감상을 끝까지 고집하는 반응, R06 꽃 그림 정체를 양보하지 않는 장난, R15 먼저 옆자리로 부르는 적극성. |
| 서윤 | R08은 사라진 책·독서 자리가 아니라 실제 빵 나누기/소파를 회상. R07 이벤트의 책·책갈피를 소파 옆자리로 맞춤. R12 이벤트 찻잔을 본편과 같은 물잔으로 통일. R15는 음식 선택의 뜻을 분명히 하고 ‘바꾸지 않겠다’는 말이 실제 나온 뒤 장난을 회수. E01 O01 회상은 실제 서로 다르게 읽은 경험으로 수정하고, 맞은편/옆자리 응수와 동거 기대·세 선택을 생활 언어로 압축. | R01 설탕 취향 예측이 빗나가는 순간, R09 도현의 파스타와 서윤의 리소토 고집, R15 음식 교환과 위스키 취향. |

## 대표 수정 전후

- 리아 E01: 리아 집에서 ‘각자의 집으로 돌아갔다’ → 도현이 귀가 준비를 하고 리아가 현관까지 배웅한다.
- 지현 E01: ‘우리 둘 다 가방부터 닫았지’ → ‘가려던 데 못 가고도 같이 있었지.’ 실제 O01의 세 행동 경로와 모두 양립한다.
- 유진 R15: ‘도현이 옮겨 앉은 자리에 앉았다’ → 도현 옆, 자신이 비워 둔 자리에 앉는다. 과자 접시도 먹은 뒤 치운다.
- 서윤 E01: ‘비용이랑 출퇴근, 각자 쓸 자리... 언제 같이 볼까?’ → ‘네가 먼저 열쇠 돌리는 소리 같은 게 좀 궁금해졌어.’ 이후 선택에서는 현실적인 항목을 이야기하되 기존 세 약속 날짜·기억은 그대로 남긴다.

## 선택과 상태

호감도 보상·교제·관계 종료·애정 표현 여부·복장·약속 기억값과 모든 메뉴의 선택 수를 대조한다. 새 기억 변수를 만들지 않는다. 리아 R02에서만 기존 세 번째 선택 플래그를 읽어 이미 한 말을 되풀이하지 않는 조건을 추가한다. 지현의 사적 호칭은 기존 선택을 읽고, 회사에서의 팀장 호칭은 그대로 둔다. 회상은 실제 진행 경로를 기준으로 한다. 본장면 진행/귀가/대화, 생활복/코스튬은 기존 선택과 CG 계획을 유지한다.

## 편집자의 판단과 남은 약점

리아는 말의 속도와 생활 속 웃음이 가장 안정적이다. 지현은 능숙함과 칭찬받고 싶은 마음의 대비가 강점이다. 유진은 먼저 고르고 부르는 행동이 매력인데 R05/R10/O01/O02의 노트·감상 소재가 여전히 가까워 연속 플레이에서는 비슷하게 느낄 수 있다. 서윤은 취향을 잘못 짚고 말을 고치는 장면이 살아 있지만 서점·카페 방문 비중은 높다. 기존 장소·기억을 전부 바꾸는 대규모 재설계는 이번 검수에서 하지 않았다.

R13~R14 갈등의 역할 조율과 후반의 미래 선택은 주제상 비슷한 문장이 일부 남는다. 핵심 갈등·실제 선택의 의미를 보존한 상태이며 완전히 다른 사건으로 바꾸진 않았다. 네 루트 모두 연애 대화만 길게 늘리면 리듬이 떨어지므로, 다음 단계에서는 화면·표정·짧은 행동 연출과 함께 템포를 확인해야 한다.

자동 실행은 선택과 화면을 진행하며 상태를 확인한다. 로그를 편집자가 이어 읽는 판단, 실제 독자의 재미·몰입·읽기 시간 측정은 별개다. 60~90분 고백 목표와 업무 비중 10~20%는 아직 실제 독자 측정값이 아니다. 현재 고정 입상과 임시 배경은 모든 지문을 시각적으로 재현하지 않으므로 최종 연출 완성 판정도 보류한다.

최종 실행·화면 검증 결과는 ‘통합검수_실행검증_v1.md’에 기록한다. 이 문서와 인물별 ‘검수후_현행대본.md’가 이번 수정의 기준이다. 0.27.0 이하 단계별 연결 대본은 당시 이력이다.
'''
(H / 'docs/공통과네루트_통합검수와수정_v1.md').write_text(review, encoding='utf-8')
(P / 'story/integrated_review_v1.md').write_text(review, encoding='utf-8')
prefix = '''> 현행 갱신: 기획 v3.01 / Windows 0.28.0-integrated-review — 2026-10-21
> 공통·네 루트·메신저·이벤트 전후의 소품·시간·회상·사적 호칭·동선을 검수했다. 서윤 E01은 기존 세 계획과 날짜를 유지하며 짧은 생활 대화로 편집했다.
> 이번 기준은 ‘공통과네루트_통합검수와수정_v1.md’ 및 인물별 ‘검수후_현행대본.md’다. 새 아트·음성·CG는 제작하지 않았다. 실제 재미·독자 읽기 시간과 자동 분기 검증을 구분한다. 이전 갱신은 이력이다.

'''
for name in ('퇴근 후 우리_v2_통합 기획서.md', '퇴근 후 우리_95개 사건 명세_v1.md', '기획_질문및결정대장.md', '게임개발_완료까지_전체작업계획_v1.md', '퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md', '대사_감정기호와메신저이모티콘_기준_v1.md'):
    (H / 'docs' / name).write_text(prefix + (D / '개발자료/docs' / name).read_text(encoding='utf-8-sig'), encoding='utf-8')
guide = '''퇴근 후, 우리 — Windows 통합 검수판 0.28.0-integrated-review

afterwork_script_prototype.exe 실행. 공통 C01~C08, 네 루트 R01~R16, 선택 일상, 후일담을 확인할 수 있습니다.
이번 수정: 시간·소품·과거 회상·귀가 동선·사적 호칭의 연결 오류를 고치고 서윤 후일담 선택의 문구를 압축했습니다.
서윤의 위스키 취향과 식사 장면은 유지합니다. 친밀한 본장면은 기존 자리 표시입니다.
최종 그림·음성·배경·애니메이션·Steam 기능은 별도 작업이며 실제 독자 재미와 읽기 시간은 아직 측정하지 않았습니다.
개발자료/docs/공통과네루트_통합검수와수정_v1.md 및 통합검수_실행검증_v1.md 참고.
이미 지난 대사는 이전 저장 또는 새 회차에서 확인하세요. 현재 켜 둔 게임은 다시 실행해야 새 대본이 적용됩니다.
로컬 개발용. GitHub 업로드·외부 배포는 하지 않았습니다.
'''
(H / '시작안내.txt').write_text(guide, encoding='utf-8')
for name in ('integrated_story_review.py', 'prepare_integrated_tests.py', 'verify_integrated_package.py', 'prepare_integrated_handoff.py', 'run_revision_tests.ps1'):
    shutil.copy2(P / 'tools' / name, H / 'validation/tools' / name)
shutil.copy2(P / 'game/integrated_story_tests.rpy', H / 'source/game/integrated_story_tests.rpy')
print(json.dumps({'changed_files': len(changed), 'edited_story_labels': sorted(scenes), 'handoff': str(H)}, ensure_ascii=False))
