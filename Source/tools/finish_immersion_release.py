from pathlib import Path
import json,re,shutil
P=Path(__file__).resolve().parents[1]; S=P.parent; proof=P/'testing/immersion-v1'; H=S/'afterwork-immersion-handoff-v1'
suites='full_editorial_checks,common_romance,ria16_flow,yujin_early_checks,yujin08_checks,yujin12_checks,yujin_final_checks,jihyun04_checks,jihyun_final_checks,seoyun_checks,office_phone_checks,review_continuity_checks'.split(',')
details=[]
for suite in suites:
    f=proof/('native-'+suite+'.log'); text=f.read_text(encoding='utf-8-sig'); assert '[rpytest] Status: PASSED' in text,f
    details.append(dict(suite=suite,cases=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',text)[1]),assertions=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',text)[1])))
    shutil.copy2(f,H/'validation'/f.name)
total=sum(x['cases'] for x in details); checks=sum(x['assertions'] for x in details)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8')); contract=json.loads((proof/'source-contract.json').read_text(encoding='utf-8'))
report=dict(version='0.21.0-immersive-dialogue',native_status='passed',native_cases=total,native_assertions=checks,suites=details,scene_blocks_rewritten=contract['changed_scene_blocks'],game_files_verified=len(pkg['game_file_hashes']),images_changed=0,rigging_changed=False,saves_removed=0,github_updated=False)
(H/'validation/final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for n in ('package-verification.json','unchanged-assets.json','source-contract.json','changed-files.json'): shutil.copy2(proof/n,H/'validation'/n)
shutil.copy2(proof/'first-attempt-jihyun04_checks.log',H/'validation/first-attempt-jihyun04_checks.log')
shutil.copy2(P/'game/jihyun_tests.rpy',H/'source/game/jihyun_tests.rpy')
md=f'''# 몰입·말맛 재집필판 실행 검증 — 0.21.0

- Ren’Py 문법 검사 통과.
- 소스 대조: {contract['changed_scene_blocks']}개 장면 블록의 대사·지문을 수정했다. 선택지 문구·분기·기억 갱신·호감도·보상·메신저 ID/상대/첨부/입력 중 설정은0.20.1과 같다. source-contract.json과 실제 원문 diff를 확인할 수 있다.
- 최종 Windows 실행본 {len(suites)}개 검사 묶음, {total}사례/{checks}확인 통과. 공통, 리아 전체 대표 경로, 유진 초반/중반/후반, 지현 초반/후반, 서윤 전체, 메신저, 시간 순서와 관계 종료 확인, 실제 선택에 맞는 회상을 확인했다. 모든 조합 전수 검사는 아니다.
- 별도 검사 실행본·별도 저장 공간을 썼다. 기존 자동 검사로 애정 표현·친밀한 전환 미룸, 공개 합의와 실제 알림의 구분, 갈등의 약속과 행동 구분, 선택 복원·저장/불러오기, 실제 경험에 맞는 후속 반응 등을 확인했다.
- 최초 지현 검사3개는 ‘확인 결과가 있는 걸로 넘기지는’이라는 이전 문장을 그대로 찾던 항목에서 실패했다. 게임은 ‘결과는 아직 못 봤으니까’라는 새 대사로 같은 미제출 상황을 표현하고 있었다. 검사 문장을 갱신하고 실제 미제출 상태 확인도 추가해 재실행했다. 검사 원문은 진단용 실행 사본에만 넣었고, 최종 게임 패키지에는 포함하지 않았다. 최초 실패 로그도 보존했다.
- 패키지 게임 파일{len(pkg['game_file_hashes'])}개가 소스와 같고 압축 CRC와 경로를 확인했다. 원문·검사·저장은 실행 패키지에서 제외했다. 폰트 고지는 포함되어 있다. 이미지 파일은0.20.1 패키지와 같다. 리깅·이미지 생성·외부 배포·GitHub 업로드를 하지 않았다.
- 자동 검사는 재미의 점수를 증명하지 않는다. 실제로 읽는 속도와 여운·웃음·설렘에 대한 편집 판정은 ‘몰입과말맛_재집필_검수기록_v1.md’를 따로 본다. 순증 분량과 아직 설명이 많은 구간도 숨기지 않고 적었다.

| 검사 | 사례 | 확인 |
|---|---:|---:|
'''+''.join(f"| {x['suite']} | {x['cases']} | {x['assertions']} |\n" for x in details)
(H/'docs/몰입과말맛_재집필_실행검증_v1.md').write_text(md,encoding='utf-8'); (P/'story/immersion_validation_v1.md').write_text(md,encoding='utf-8')
shots=Path(pkg['validation'])/'tests/screenshots'
for n in ('romance-c07-history.png','yujin-r05-portrait.png','seoyun-phone-three-replies.png','jihyun-epilogue-cohabitation-choice.png'):
    if (shots/n).exists(): shutil.copy2(shots/n,H/'screenshots'/n)
changed=contract['changed_files']
installer=(S/'update_office_v2_romance_lines.ps1').read_text(encoding='utf-8-sig')
installer=installer.replace('0.20.1-romance-lines','0.21.0-immersive-dialogue').replace('playable-lines','playable-immers').replace('afterwork-romance-lines-handoff-v1','afterwork-immersion-handoff-v1').replace('romance-lines-v1','immersion-v1').replace('이전버전_0.20.0_연애대사추가전','이전버전_0.20.1_몰입재집필적용전').replace('연애대사추가_v1','몰입재집필_v1').replace('연애대사추가_업데이트확인.json','몰입재집필_업데이트확인.json').replace('63',str(total))
a=installer.index('$modules=@('); b=installer.index('\n',a)
installer=installer[:a]+'$modules=@('+','.join("'"+n[:-4]+".rpyc'" for n in changed)+')'+installer[b:]
(S/'update_office_v2_immersion.ps1').write_text(installer,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
