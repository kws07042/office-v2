from pathlib import Path
import difflib
import hashlib
import json
import re
import shutil

P = Path(__file__).resolve().parents[1]
S = P.parent
desktop = Path("C:/Users/user/Desktop/건/오피스 V2")
installed = desktop / "개발자료/docs"
source = desktop / "개발자료/source/game"
proof = P / "testing/romance-focus-v1"
handoff = S / "afterwork-romance-focus-handoff-v1"
H = handoff
changed = [
    "ria_r13_e01.rpy",
    "jihyun_r13_e01.rpy",
    "yujin_r05_r08.rpy",
    "yujin_r13_e01.rpy",
    "seoyun_r01_r04.rpy",
    "seoyun_r05_r12.rpy",
    "seoyun_r13_e01.rpy",
    "options.rpy",
]
for folder in (proof, handoff / "docs", handoff / "source/game", handoff / "validation"):
    folder.mkdir(parents=True, exist_ok=True)
assert "0.26.0-finale-daily" in (source / "options.rpy").read_text(encoding="utf-8-sig")
assert "0.27.0-romance-focus" in (P / "game/options.rpy").read_text(encoding="utf-8")


def code_flow(text):
    result = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or line.startswith("define config.version"):
            continue
        if re.match(r'^\s*(?:[a-z]+\s+)?"', line):
            continue
        if stripped.startswith("call phone_deliver("):
            result.append(re.match(r'\s*call phone_deliver\("([^"]+)",\s*"([^"]+)"', line).groups())
            continue
        result.append(line)
    return result


contract = {
    "version": "0.27.0-romance-focus",
    "baseline": "Desktop/건/오피스 V2 0.26.0-finale-daily",
    "changed_files": changed,
    "previous_runtime_hashes": {},
    "menu_counts": {},
}
for name in changed:
    old = (source / name).read_text(encoding="utf-8-sig")
    new = (P / "game" / name).read_text(encoding="utf-8")
    assert old != new, name
    assert code_flow(old) == code_flow(new), name
    menu_re = re.compile(r'^\s+"[^"]+":\s*$', re.M)
    old_menus = len(menu_re.findall(old))
    new_menus = len(menu_re.findall(new))
    assert old_menus == new_menus, (name, old_menus, new_menus)
    contract["menu_counts"][name] = old_menus
    (proof / (name + ".before")).write_text(old, encoding="utf-8")
    diff = "".join(
        difflib.unified_diff(
            old.splitlines(True), new.splitlines(True),
            fromfile=name + " 0.26", tofile=name + " 0.27",
        )
    )
    (proof / (name + ".diff")).write_text(diff, encoding="utf-8")
    (handoff / "validation" / (name + ".diff")).write_text(diff, encoding="utf-8")
    shutil.copy2(P / "game" / name, handoff / "source/game" / name)
    runtime = desktop / "game" / name.replace(".rpy", ".rpyc")
    contract["previous_runtime_hashes"][runtime.name] = hashlib.sha256(runtime.read_bytes()).hexdigest()

(proof / "source-contract.json").write_text(json.dumps(contract, ensure_ascii=False, indent=2), encoding="utf-8")
shutil.copy2(proof / "source-contract.json", handoff / "validation/source-contract.json")

generator = (P / "tools/prepare_full_editorial_handoff.py").read_text(encoding="utf-8")
snippet = generator[generator.index("groups="):generator.index("\nprefix=")]
exec(compile(snippet.replace("0.20.0", "0.27.0-romance-focus"), "current-dialogue", "exec"))

editorial = """# 연애 중심 대사 편집과 서윤의 술 데이트 — v3.00 / Windows 0.27.0

2026-10-20. 실제 게임 대본의 초반·후반을 함께 읽고 반영했다. 모든 인물은 성인이다. 공통 구간과 네 루트의 기존 사건 수, 메뉴 수, 선택 기억, 교제·거절·관계 종료, 보상, CG 위치는 유지한다. 친밀한 본장면은 기존 자리 표시·생략으로 둔다.

## 왜 고쳤나

이전 대본은 도현의 기록집을 네 히로인이 차례로 읽고, 책·차·날짜에 관한 대화를 반복했다. 도현의 취미 완성은 유지할 가치가 있지만, 데이트의 행동과 각 인물의 욕심을 밀어냈다. 이번에는 기록집이 꼭 필요한 첫 소개·초안·완성 확인만 짧게 남기고, 이어지는 대사는 두 사람이 지금 상대에게 바라는 행동으로 옮겼다. 책과 차는 서윤·지현 등의 개인 취향일 수 있어도 네 연애의 공통 종착점으로 쓰지 않는다.

## 실제 대본 반영

| 인물 | 바뀐 경험 | 남긴 연결 |
|---|---|---|
| 리아 | R15 길 찾기 승부가 실제 가게 선택으로 이어진다. R16은 초안을 잠깐 본 뒤 디저트를 고르고 서로의 것을 맛본다. E01은 완성본을 나눈 다음 집에서 함께 점심을 만든다. | R10 장소별 실제 사진, R15 세 미래 선택·친밀 선택, R16 초안 상태, E01 두 부·각자의 집·실제 O03/O02 회상. |
| 지현 | R15 평소보다 신경 쓴 옷을 알아봐 주길 바라는 마음이 드러난다. R16은 계획표를 접고 목적지 없이 걸어 보려 한다. E01은 조립집·인쇄본을 잠깐 확인한 뒤 카드 놀이와 같이 살 가능성을 말한다. | R15 세 미래 선택·복장·친밀 선택, R16 시험 업무·손잡기 범위, E01 동거 논의 세 갈래와 미입주 상태. |
| 유진 | R05 서점은 방문 장소로 두되 책의 구성 설명보다 먼저 같이 걷고 싶어 하는 반응을 앞세운다. R15는 스스로 옆자리를 권하고, R16은 노트를 덮고 도현에게 관심을 돌린다. E01은 완성본 확인 뒤 함께 여행을 상상한다. | R05 세 구성값·첫 입맞춤 선택, R15 친밀 선택, R16 디자인·초안 상태, E01 전시/휴가/후보 계획. |
| 서윤 | R01~R03 책을 매개로 한 긴 감상 대화를 줄이고 서로를 잘못 짚고도 궁금해하는 흐름으로 바꾼다. R07은 소파 옆자리, R15는 음식·위스키·말 바꾸는 순간을 데이트의 중심에 둔다. R16·E01은 책을 덮고 상대에게 다가간다. | R02 추천 책 제목·세 응답·R03 약속과 접촉 경계, R15 미래·복장·친밀 선택, E01 동거 계획 날짜와 미완료 상태. |

### 수정 전후 대표 예

- 리아: 초안의 첫 장을 끝까지 읽는 장면 → 첫 장만 보고 ‘지금은 나랑 디저트 고르기!’라며 도현을 끌어낸다.
- 지현: 완성본과 차를 놓고 관계를 논의 → 꾸민 옷을 알아봐 주길 바란 뒤, 후일담에는 카드를 섞다 같이 살 이야기를 꺼낸다.
- 유진: 차를 마시며 연습한 고백을 전달 → 도현이 맞은편에 앉자 옆자리를 짚으며 ‘오세요’라고 먼저 부른다.
- 서윤: 책의 같은 문장을 오래 읽고 감상을 나눔 → 서로 고른 음식과 위스키를 맛보고, 집에서는 ‘오늘은 같이 밤을 보내고 싶어’라고 따로 묻는다.

## 한서윤: 술 취향과 R15 연결

32세 성인 서윤은 퇴근 뒤 위스키의 향을 음식과 함께 소량 맛보는 것을 좋아한다. 기존 ‘재즈 바 단골’ 설정을 확장하되, 술이 심리의 비밀을 털어놓게 하는 장치나 연애의 필수 통과 의식이 되지 않게 한다. R12 메시지에 혼자 메뉴를 고르기보다 도현과 저녁을 먹고 싶다는 기대를 심어 놓고, R15 식당에서 각자 작은 잔 하나를 마신다. 취향의 충돌은 음식 교환과 서윤의 ‘말 바꿀게’로 회수한다. 이후 식사와 산책을 마치고 물을 마시며 충분히 대화한다. 집에서 서윤이 먼저 제안하고, 기존 세 선택 중 플레이어가 원할 때만 친밀한 자리 표시로 이어진다. 귀가·대화 선택에는 벌점이 없다. 추가 성인 CG·영상은 만들지 않았다.

술에 취해 판단이 흐려진 상태를 로맨틱한 계기로 사용하지 않는다. 한 잔의 풍미와 같이 식사하는 즐거움이 서윤의 사적 취향이며, 친밀한 선택의 근거는 나중에 주고받는 명료한 말이다. 실제 제작에서도 술 마시는 모습만으로 친밀 장면이 자동 실행되면 안 된다.

## 남은 약점과 검수 범위

도현의 기록집 목표와 서윤의 서점 취향은 기존 중반에도 남아 있다. R05의 세 구성 선택, R10의 장소·페이지 기억 같은 핵심 분기는 유지해서 모든 책 언급을 삭제하지는 않았다. 서윤 E01의 동거 조건·날짜 선택은 연애 장면의 속도를 잠깐 늦춘다. 이번엔 결과의 의미와 기억값을 우선 보존했다.

자동 검사는 분기·저장 상태·결말과 실행 오류를 확인한다. 대사가 실제 플레이어에게 재미있는지는 자동으로 증명하지 못한다. 이미지·표정·음성·CG가 비어 있는 현재 게임에서 연출의 최종 호흡도 아직 판단할 수 없다.
"""
(handoff / "docs/연애중심_대사편집과서윤술데이트_v1.md").write_text(editorial, encoding="utf-8")
(P / "story/romance_focus_editorial_v1.md").write_text(editorial, encoding="utf-8")
prefix = """> 현행 갱신: 기획 v3.00 / Windows 0.27.0-romance-focus — 2026-10-20
> 책·차·기록집 감상이 길어진 초반·후반 대사를 연애 행동 중심으로 바꿨다. 서윤은 음식과 위스키 작은 잔 하나를 즐기는 인물로 확정하고 R12 메시지→R15 식당→명료한 동의 뒤의 친밀 선택으로 연결했다. 기준은 ‘연애중심_대사편집과서윤술데이트_v1.md’와 각 ‘검수후_현행대본.md’다.
> 사건·선택 기억·성인 CG 계획은 유지한다. 이전 0.26.0 이하 편집 기록은 이력이며, 충돌하면 이 현행 갱신과 실제 게임 대본을 우선한다.

"""
for name in (
    "퇴근 후 우리_v2_통합 기획서.md",
    "퇴근 후 우리_95개 사건 명세_v1.md",
    "기획_질문및결정대장.md",
    "게임개발_완료까지_전체작업계획_v1.md",
    "퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md",
    "대사_감정기호와메신저이모티콘_기준_v1.md",
):
    (handoff / "docs" / name).write_text(prefix + (installed / name).read_text(encoding="utf-8-sig"), encoding="utf-8")
character_doc = handoff / "docs/퇴근 후 우리_캐릭터 보강 및 게임 시스템 설계안.md"
character_text = character_doc.read_text(encoding="utf-8")
anchor = "32세·브랜드전략팀 선임·입사 8년 차를 유지한다.\n\n"
assert character_text.count(anchor) == 1
character_text = character_text.replace(
    anchor,
    anchor + "**현행 확정 취향:** 서윤은 위스키의 향을 음식과 함께 작은 잔으로 맛보는 것을 좋아한다. 재즈 바 단골 설정과 이어지되 매번 술을 찾는 캐릭터로 만들지는 않는다. R12에서 도현과 저녁을 기대하고, R15에 함께 소량을 마신 후 식사·산책·물을 마시며 대화한다. 집에서 별도로 서로의 의사를 확인한 경우에만 기존 친밀 장면 선택으로 이어진다. 술이 동의의 이유가 되지 않는다.\n\n",
)
character_doc.write_text(character_text, encoding="utf-8")
guide = """퇴근 후, 우리 — Windows 연애 중심 대사 편집판 0.27.0-romance-focus

afterwork_script_prototype.exe를 실행합니다. 서윤은 식사에서 위스키를 조금씩 함께 맛보고, 이후 집에서 별도로 친밀한 선택을 확인합니다.
리아·지현·유진·서윤의 책·차·기록집 중심 대화 일부를 실제 데이트 행동과 서로를 향한 반응으로 바꿨습니다.
이미 지난 장면은 이전 저장 또는 새 회차로 확인하세요. 사용자 저장과 기존 이미지·리깅은 보존합니다.
개발자료/docs/연애중심_대사편집과서윤술데이트_v1.md에 수정 내용과 남은 약점이 있습니다.
자동 검사는 실행을 확인하며 실제 플레이어의 재미 평가는 아닙니다. 이번 작업은 로컬 반영입니다.
"""
(P / "WINDOWS-README.txt").write_text(guide, encoding="utf-8")
(handoff / "시작안내.txt").write_text(guide, encoding="utf-8")
print(json.dumps({"changed": changed, "menu_counts": contract["menu_counts"], "docs": len(list((handoff / "docs").glob("*.md")))}, ensure_ascii=False))
