from pathlib import Path
import json,shutil,hashlib,re,sys
P=Path(__file__).resolve().parents[1]; S=P.parent
proof=P/'testing/romance-lines-v1'; H=S/'afterwork-romance-lines-handoff-v1'
if sys.argv[1]=='verify':
    base=(P/'tools/verify_yujin_r04_package.py').read_text(encoding='utf-8')
    base=base.replace('0.13.0-yujin-r04','0.20.1-romance-lines').replace('playable-yujin-r04-release','playable-lines').replace('native-validation-yujin-r04','native-lines').replace('testing/yujin-r04-v1','testing/romance-lines-v1')
    base=base.replace("('yujin_tests.rpyc', 'office_phone_tests.rpyc', 'cream_tests.rpyc')", "('ria16_tests.rpyc','three_choice_tests.rpyc','office_phone_tests.rpyc','yujin_tests.rpyc','yujin08_tests.rpyc','jihyun_tests.rpyc','jihyun_final_tests.rpyc','seoyun_tests.rpyc')")
    exec(compile(base,str(Path(__file__)),'exec'))
    shutil.copy2(P/'game/three_choice_cases.json',validation/'game/three_choice_cases.json')
    old=json.loads((P/'testing/full-editorial-v1/package-verification.json').read_text(encoding='utf-8'))
    assert all(hashes[n]==old['game_file_hashes'][n] for n in hashes if n.startswith('images/'))
    sys.exit(0)

for folder in ('docs','source/game','validation'): (H/folder).mkdir(parents=True,exist_ok=True)
details=[]
for suite in ('ria16_flow','yujin08_checks','jihyun_final_checks','seoyun_checks'):
    f=proof/('native-'+suite+'.log'); t=f.read_text(encoding='utf-8-sig'); assert '[rpytest] Status: PASSED' in t,f
    details.append(dict(suite=suite,cases=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]),assertions=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])))
    shutil.copy2(f,H/'validation'/f.name)
total=sum(x['cases'] for x in details); checks=sum(x['assertions'] for x in details)
report=dict(version='0.20.1-romance-lines',native_status='passed',native_cases=total,native_assertions=checks,suites=details)
(H/'validation/final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(proof/'package-verification.json',H/'validation/package-verification.json')
changed=json.loads((proof/'changed-files.json').read_text(encoding='utf-8'))
for n in changed: shutil.copy2(P/'game'/n,H/'source/game'/n)

# Regenerate the four full current dialogue documents from actual game sources.
source=(P/'tools/prepare_full_editorial_handoff.py').read_text(encoding='utf-8')
block=source[source.index('groups='):source.index('\nprefix=')].replace('0.20.0','0.20.1')
exec(compile(block,'current_dialogue_documents','exec'))
md=f'''# 연애 대사4묶음 적용 — 0.20.1 / 기획 v2.93

사용자가 승인한 비노골적인 연애 대사 초안을 기존 장면 안에 연결했다. 새 사건·선택지·CG를 늘리지 않았다.

| 인물 | 위치 | 연결 내용 |
|---|---|---|
| 강리아 | R11, 요리 전 집 데이트 | 새 장소보다 보고 싶은 사람이 이유였다는 직구. ‘나만 용감한 거 억울하다’는 장난에 도현도 자기 마음을 답하고 요리로 연결. 반말·존댓말 모두 반영. |
| 백지현 | R12, 식사 뒤 집에서 차 | ‘잘했다’보다 ‘예쁘다’는 말을 듣고 싶은 기대. 소매를 만지다 칭찬받고 시선을 늦게 마주하는 반응. 기존 비슷한 대사는 교체해 중복을 줄임. |
| 차유진 | R06, 다음 약속 제안 | 수줍지만 다음 만날 장소는 자기가 고르고 싶은 적극성. 다음 R07의 토요일15시 동네 서점 앞 약속까지 실제로 상호 확인. 기억 yujin_r07_appointment에 기록. |
| 한서윤 | R11, 산책 경로 선택 전 | 도현이 먼저 고르는 길을 기대하며 따라가고 싶은 마음. 바로 뒤 기존 경로 선택3개로 이어짐. |

서윤은 이미 식사를 시작한 R09보다 실제 길을 고르는 R11에 배치했다. 유진은 이미 자리를 옮긴 뒤 ‘오늘 다음 장소’를 새로 고르게 하지 않고 다음 만남의 약속으로 맞췄다. 호감도 벌점·첫 입맞춤·친밀한 장면의 동의 조건은 바꾸지 않았다. 동작은 대본 지문이며 새 표정·입상·리깅을 만든 것은 아니다.

문법 검사와 최종 Windows 실행본의 관련4검사 묶음 {total}사례/{checks}확인을 통과했다. 기존 리아 전체, 유진R05~R08, 지현R05~후일담, 서윤 전체의 대표 분기를 확인한 것으로 모든 조합 전수 검사는 아니다. 이전0.20의 전체 검수245사례와 구분한다. 패키지 게임 파일54개가 소스와 일치하고 인물 이미지는0.20과 동일하다. 외부 배포·GitHub 업로드는 하지 않았다.

인물별 ‘검수후_현행대본.md’도 실제 게임 원문으로 다시 생성했다. 이번 변경은 이 문서를 우선하며, 이전 전체 검수표는0.20 당시의 평가 기록이다.
'''
(H/'docs/연애대사4묶음_적용기록_v1.md').write_text(md,encoding='utf-8')
(P/'story/romance_lines_applied_v1.md').write_text(md,encoding='utf-8')
prefix='''> 현행 갱신: 기획 v2.93 / Windows 0.20.1-romance-lines — 2026-10-19
> 승인한 연애 대사4묶음을 리아R11·지현R12·유진R06·서윤R11에 적용했다. 유진은 다음 토요일15시 서점 약속을 실제 대화로 확인한다. 새 사건·CG·선택지는 늘리지 않았다. 현행은 ‘연애대사4묶음_적용기록_v1.md’ 및 인물별 ‘검수후_현행대본.md’를 우선한다.

'''
for n in ('퇴근 후 우리_v2_통합 기획서.md','퇴근 후 우리_95개 사건 명세_v1.md','기획_질문및결정대장.md','게임개발_완료까지_전체작업계획_v1.md'):
    (H/'docs'/n).write_text(prefix+(S/'afterwork-full-editorial-handoff-v1/docs'/n).read_text(encoding='utf-8'),encoding='utf-8')
shutil.copy2(P/'WINDOWS-README.txt',H/'시작안내.txt')
text=(S/'update_office_v2_full_editorial.ps1').read_text(encoding='utf-8-sig')
text=text.replace('0.20.0-dialogue-review','0.20.1-romance-lines').replace('playable-edit','playable-lines').replace('afterwork-full-editorial-handoff-v1','afterwork-romance-lines-handoff-v1').replace('full-editorial-v1','romance-lines-v1').replace('이전버전_0.19.0_전체대본검수적용전','이전버전_0.20.0_연애대사추가전').replace('전체대본검수_v1','연애대사추가_v1').replace('전체대본검수_업데이트확인.json','연애대사추가_업데이트확인.json').replace('245',str(total))
start=text.index('$modules=@('); end=text.index('\n',start)
text=text[:start]+'$modules=@('+','.join("'"+n[:-4]+".rpyc'" for n in changed)+')'+text[end:]
(S/'update_office_v2_romance_lines.ps1').write_text(text,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
