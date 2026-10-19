from pathlib import Path
import shutil, json, hashlib, re
P = Path(__file__).resolve().parents[1]
S = P.parent
H = S / 'afterwork-yujin-r08-handoff-v1'
proof = P / 'testing/yujin-r08-v1'
for sub in ('docs','source/game','validation','screenshots'):
    (H/sub).mkdir(parents=True, exist_ok=True)
status = '''> 2026-10-19 현행 갱신 · 기획 v2.86 / Windows 0.14.0-yujin-r08
> 차유진 임시 입상과 R05~R08 대화를 연결했다. R01~R04는 기억 누락 대응과 고백 동기를 보완했다.
> 현행 구현은 공통 C01~C08, 리아 R01~R16·O01~O03·E01, 유진 R01~R08이다. 유진 R09~R16·선택 일상·후일담, 지현·서윤 개인 루트는 미구현이다.
> 아래 과거 이력의 ‘유진 R04까지’는 당시 범위다. 현행은 별도 ‘유진_R05-R08_현행명세_v1.md’를 우선한다.
> 전체 95사건·일반 CG18개 계획은 유지한다. 최종 그림·이벤트 CG·동영상·음성 제작은 뒤로 둔다. 이번 사용자 제공 이미지는 일반 대화용 임시 입상만 예외다.

'''
for name in ('퇴근 후 우리_v2_통합 기획서.md','게임개발_완료까지_전체작업계획_v1.md','기획_질문및결정대장.md'):
    old = S/'afterwork-yujin-r04-handoff-v1/docs'/name
    (H/'docs'/name).write_text(status+old.read_text(encoding='utf-8-sig'),encoding='utf-8')
spec = '''# 차유진 R05~R08 현행 명세 — 기획 v2.86 / 0.14.0-yujin-r08

기존 사건을 구현했다. 새 루트·사건·CG 수를 추가하지 않는다. 어른 두 사람의 첫 연애이며 존댓말·‘도현 씨’를 유지한다. 장난 뒤 짧은 직구, 행동 뒤 한 줄 설명을 기준으로 썼다. 취향·스킨십 속도를 정답/오답으로 채점하지 않는다.

| 사건 | 실제 진행 | 선택과 후속 기억 |
|---|---|---|
| R05 둘이 고른 주말 | R04의 제안 주체를 반영해 서점·공원에서 도현의 기록집 구성 후보를 함께 봄. 유진이 먼저 첫 입맞춤을 제안 | 구성 3개와 입맞춤/손잡기/산책 3개. 구성은 후보이지 기록집 완성이 아님. 입맞춤을 선택한 경우에만 첫 입맞춤 기록 |
| R06 제가 먼저 말해도 되죠 | 수요일 카페에서 기다린 마음과 먼저 표현하는 방식을 나눔. 토요일 오후 3시 만남 확정 | 서로 먼저/생각할 시간/번갈아 제안. 입맞춤/손잡기/말로 인사. 앞선 입맞춤을 실제로 했는지 구분 |
| R07 둘이 선택한 속도 | 약속대로 책·저녁 뒤 유진 집에서 창가 그림을 봄. 유진이 함께 머물고 싶다는 마음을 표현 | 함께 밤 보내기/귀가/마음 이야기 후 귀가. 앞선 구성 후보를 회수. 세 선택 모두 같은 본편으로 이어짐 |
| R08 다음 약속은 제가 | 함께 머문 경로에만 다음 아침 빛·식사. 다른 경로는 실제 그림·차 대화를 메시지로 회수. 유진이 다음 약속 제안 | 수요일 19시/목요일 19시/수요일 19시30분. 실제 날짜·시간·제안 주체 저장. 생각할 시간을 요청했던 경우의 초대 문구도 다름 |

R05 +4 / R06 +6 / R07 +0 / R08 +4. R04까지 호감도 24로 시작한 확인 경로는 R08 뒤 38이다. 공통 구간의 기존 호감도가 있으면 그 값은 별도로 남는다. 교제는 기존 R04의 상호 동의로 성립하며 30점 문턱을 새로 넣지 않는다.

## R01~R04 검수 및 수정

- R01에 짧은 유진 시점 삽입: 전시 초대 후 상대의 첫 감상을 기다리는 기대를 보여 준다.
- R03의 접촉 기억이 비어 있으면 하지 않은 말을 회상하지 않고 새 작업 확인으로 시작한다.
- R04는 전시를 핑계로 만나야 한다는 설명보다 ‘전시가 끝나도 도현을 보고 싶다’는 개인적 끌림을 분명히 한다.
- R06의 기다려 준 행동에 대한 감사는 해당 선택이 있었을 때만 사용한다.

## 임시 이미지

사용자 제공 PNG를 색·선화·손·표정·알파 수정 없이 그대로 복사했다. `ui_temp_v001.png`를 엔진에서 (230, 0, 570, 850) 범위로 잘라 중앙 상체 입상으로 보여 준다. 원본 파일은 보존한다. 메시지와 도현 혼자 있는 장면에는 입상을 띄우지 않는다.

현재 한 장의 수줍은 표정이 모든 일반 대화에 쓰이는 임시 상태다. 평온한 업무·진지한 대사와 완전히 맞는 최종 연기는 아니다. 외곽 빨강·노랑 잔여 픽셀, 기본 표정과 자세 차분, 평상복의 리본/단추 일관성은 최종 아트 때 검수한다. 이 파일로 기존 예비 마스터를 덮어쓰지 않는다. 피부색 변경·귀걸이 추가·손 합성·새 생성은 하지 않았다.

## 이벤트 연결

Yujin R07만 기존 이벤트 화면에 연결했다. 도입 3페이지(3번째에서 기본→표정 전환 자리), 본장면 3개 자산 자리, 이후 대화 1페이지 구조다. 준비된 최종 CG·영상은 0개다. 현재는 비노골적인 대사와 ‘그림 준비 중’ 자리만 보여 준다. R12·R15는 아직 연결하지 않았다. 연출 건너뛰기는 시청 생략이며 함께 머물기로 한 이야기 선택을 취소하지 않는다. 귀가를 고르면 R08에 함께 잔 기억이 생기지 않는다.

## 다음 작업 계약

R09는 `yujin_r08_next_appointment`의 실제 요일·시각을 사용해야 한다. 무조건 수요일 19시로 쓰면 안 된다. `yujin_r06_expression`, `yujin_r05_layout`, 실제 접촉·밤의 선택을 이후에 회수한다. R08 완료는 전체 루트 엔딩·업적이 아니다. 이후 R09~R16·O01~O03·E01을 이어 쓰고, 최종 사진·CG·영상은 그 뒤 제작한다.
'''
(H/'docs/유진_R05-R08_현행명세_v1.md').write_text(spec,encoding='utf-8')
for name in ('yujin_r01_r04.rpy','yujin_r05_r08.rpy'):
    text=(P/'game'/name).read_text(encoding='utf-8')
    # Source-linked dialogue transcription retains choice branches and flags.
    out='# '+name+' 연결 대본\n\n실제 구현의 분기·선택·기억을 함께 보존한 대본이다. 최종 음성·CG는 포함하지 않는다.\n\n```renpy\n'+text+'\n```\n'
    (H/'docs'/('유진_'+('R01-R04' if '01' in name else 'R05-R08')+'_연결대본_v2.md')).write_text(out,encoding='utf-8')
files=['core.rpy','cream_ui.rpy','screens.rpy','options.rpy','yujin_r01_r04.rpy','yujin_r05_r08.rpy','event_sequence.rpy','event_assets.json','event_story.json','event_cg_plan.json']
for name in files:
    shutil.copy2(P/'game'/name,H/'source/game'/name)
asset='images/characters/yujin/ui_temp_v001.png'
(H/'source/game'/asset).parent.mkdir(parents=True,exist_ok=True)
shutil.copy2(P/'game'/asset,H/'source/game'/asset)
shutil.copy2(proof/'image-provenance.json',H/'validation/image-provenance.json')
for name in ('yujin-r05-portrait.png','yujin-r07-night-portrait.png','yujin-r07-placeholder.png'):
    if (P/'tests/screenshots'/name).exists():
        shutil.copy2(P/'tests/screenshots'/name,H/'screenshots'/name)
guide='''퇴근 후, 우리 — Windows 대본 개발판 0.14.0-yujin-r08

afterwork_script_prototype.exe를 실행하세요.
시작 화면의 ‘유진 R01~R08 확인’에서 유진 대화를 바로 확인할 수 있습니다.
‘처음부터’로 공통 C08에서 차유진을 골라도 이어집니다.

이번 추가: 사용자 제공 유진 임시 입상, R01~R04 검수, R05~R08 대사·선택·메신저·기억 연결.
최종 그림/이벤트 CG/영상/음성은 준비 중이며, 한 장의 임시 표정은 최종 연기가 아닙니다.
유진 R09 이후·선택 일상·후일담, 지현·서윤 개인 루트는 아직 미구현입니다.
기존 리아 루트와 저장 파일은 유지합니다. 수정 전 파일은 개발자료의 별도 백업에 남깁니다.
이 폴더는 로컬 개발판입니다. GitHub 업로드나 외부 배포는 이번 작업에 포함하지 않습니다.
'''
(H/'시작안내.txt').write_text(guide,encoding='utf-8')
print(H)
