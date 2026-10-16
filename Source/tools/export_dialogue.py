"""Export the implemented script as reviewable Markdown; never modifies game state."""
import ast
import re
import sys
from pathlib import Path

PROJECT = Path(__file__).resolve().parents[1]
SPEAKERS = {"d":"도현", "r":"강리아", "j":"백지현", "y":"차유진", "s":"한서윤", "dn":"도현 독백", "rn":"리아 단독 시점", "msgd":"도현 메시지", "msgr":"리아 메시지"}

def unpack(text):
    value = ast.literal_eval(text)
    if value.startswith("[ri(") and value.endswith(")]" ):
        call = ast.parse(value[1:-1], mode="eval").body
        return [ast.literal_eval(arg) for arg in call.args]
    return [value]

def display(values):
    if len(values) == 2:
        return values[0] + " / **존댓말:** " + values[1]
    return values[0]

def render(source):
    output = []
    for raw in source.splitlines():
        line = raw.strip()
        if line.startswith("label "):
            output += ["", "## " + line[6:-1], ""]
        elif re.match(r'\$ (chapter|location) = ', line):
            key, value = line[2:].split(" = ", 1)
            output += ["", "**" + ("장면" if key == "chapter" else "시간·장소") + ":** " + ast.literal_eval(value), ""]
        elif line.startswith(("if ","elif ","else:","while ")):
            output += ["", "*분기 조건: `" + line.rstrip(":") + "`*", ""]
        elif line == "menu:":
            output += ["", "**플레이어 선택 — 한 항목만 진행**", ""]
        elif line.startswith("call "):
            output += ["", "*연결 장면: `" + line[5:] + "`*", ""]
        else:
            match = re.fullmatch(r'(\w+) (".*")', line)
            if match and match[1] in SPEAKERS:
                output += ["**" + SPEAKERS[match[1]] + ":** " + display(unpack(match[2])), ""]
            elif line.startswith('"'):
                is_option = line.endswith(":")
                literal = line[:-1] if is_option else line
                try:
                    values = unpack(literal)
                except (ValueError, SyntaxError):
                    continue
                output += [("- 선택: " if is_option else "*지문:* ") + display(values), ""]
    return "\n".join(output).strip() + "\n"

def main():
    destination = Path(sys.argv[1])
    common = (PROJECT/"game/common.rpy").read_text(encoding="utf-8")
    ending = (PROJECT/"game/core.rpy").read_text(encoding="utf-8").split("label end_common:",1)[1]
    header = """# 「퇴근 후, 우리」 공통 C01~C08 연결 대본 v1

작성·구현: 2026년 10월 14일. 통합 기획서 v2.67 기준. C05~C07 공동 행동·상호 관심 보강과 C08 다음 약속 문구를 반영했다. 일반 대화의 ~·~~·!·!!·... 감정 기호 편집을 반영했다. 현재 Ren’Py 시험판의 실행 소스에서 추출한 검토본이다. C01의 존댓말 유지, C02~C08 전체 선택, C06의 인물×화제 12가지 공동 행동, C07의 짧은 업무 접근·퇴근 후 만남, END_COMMON을 포함한다. 사건 95개·일반 CG 18개 배정은 유지한다.

리아 대사는 말 놓기 합의 뒤 반말, 합의 전 존댓말로 진행한다. 두 말투를 함께 적은 행에서는 해당 회차의 하나만 표시된다. 코드 조건은 편집자가 분기를 찾기 위한 표기이며 게임 대사창에 출력되지 않는다. 각 선택 아래 대사는 해당 선택의 가지이고, 합류 뒤에는 공통 대사로 이어진다.

## 분기와 기억을 읽는 기준

| 구간 | 실제 진행·기억 |
|---|---|
| C01 | 현장 대응 한 가지와 말투 합의를 기록. 연애가 확정되는 장면은 아님 |
| C02~C04 | 네 인물의 판단·질문·요청 방식 구분. 지현에게 추가 확인을 약속하면 C05에서 결과 전달 |
| C05 | 퇴근 취향 하나를 말하고 네 인물에게 기록집 취미를 소개. 사진 파일을 보여 준 것으로 기록하지 않음 |
| C06 | 인물 한 명·화제 하나만 경험. 선택한 화제와 해당 `personal_moment`만 기록 |
| C07 | 같은 인물이면 실제 C06 화제를 회수. 다른 인물이면 첫 개인 대화로 연결. 접근 하나를 실제로 실행한 뒤 둘만의 퇴근 후 만남을 기록 |
| C08 | 이전 만남 상대·호감도와 관계없이 네 루트 선택 가능. 교제는 개인 R04에서 상호 확인 |
| END_COMMON | C08 또는 리아 R04에서 동료 선택을 확인하면 같은 결말로 합류. Steam 업적은 아직 연동하지 않음 |

시험판은 공통과 리아 R01~R04까지만 수록한다. 다른 개인 루트는 선택 확인 뒤 종료한다. 실제 읽기 시간·최종 그림·음성·최종 UI·본편 전체 검수는 남아 있다.

"""
    (destination/"공통_C01-C08_연결대본_v1.md").write_text(header + render(common) + "\n" + render("label end_common:"+ending), encoding="utf-8")
    ria_header = """# 「퇴근 후, 우리」 리아 R01 현행 연결 대본 v3

작성·구현: 2026년 10월 14일. 통합 기획서 v2.67 기준. C05~C07 공동 행동·상호 관심 보강과 C08 다음 약속 문구를 반영했다. 일반 대화의 ~·~~·!·!!·... 감정 기호 편집을 반영했다. 기존 v2의 검토용 자료를 실제 실행 대본으로 연결하고 모든 리아·도현 대사를 반말·존댓말 두 경로로 완성했다. 아래는 시험판 소스에서 추출한 현행 검토본이다.

C07 리아 만남을 우선 회수하고, 없으면 실제 C06 리아 화제, 둘 다 없으면 C01 현장 행동으로 연결한다. C05에서 소개한 취미는 유지한다. quiet는 조용한 자리, meal은 식사, suggestion은 리아가 원하는 장소를 듣는 선택이다. 세 선택은 모두 개인 만남을 이어 가며 교제나 손잡기를 자동 확정하지 않는다. 인물이 든 컵은 장면 끝까지 일관되게 취급한다.

한 행의 반말·존댓말 중 현재 회차의 말투 하나만 게임에서 출력된다. 분기 조건은 검토용이며 실제 대사창에 표시되지 않는다. 리아 이미지는 사용자 제작본 대기 상태이며 이 대본에 이미지 파일을 연결하지 않았다.

"""
    (destination/"리아_R01_현행대본_v3.md").write_text(ria_header+render((PROJECT/"game/ria_r01.rpy").read_text(encoding="utf-8")), encoding="utf-8")

if __name__ == "__main__":
    main()
