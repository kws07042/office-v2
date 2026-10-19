from pathlib import Path
import json, re, shutil
P=Path(__file__).resolve().parents[1]
S=P.parent
proof=P/'testing/yujin-r08-v1'
H=S/'afterwork-yujin-r08-handoff-v1'
def totals(prefix):
    logs=list(proof.glob(prefix+'-*.log'))
    expected=5 if prefix=='source' else 4
    assert len(logs)==expected,(prefix,len(logs))
    count=checks=0
    for f in logs:
        t=f.read_text(encoding='utf-8-sig')
        assert '[rpytest] Status: PASSED' in t,f
        count+=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])
        checks+=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])
        shutil.copy2(f,H/'validation'/f.name)
    return count,checks
sc,sa=totals('source')
nc,na=totals('native')
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'))
report=dict(version='0.14.0-yujin-r08',source_cases=sc,source_assertions=sa,native_cases=nc,native_assertions=na,source_status='passed',native_status='passed',package_files_verified=len(pkg['game_file_hashes']),new_generated_art=False,user_supplied_temporary_portrait=1,rigging_changed=False,github_updated=False)
(H/'validation/final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(proof/'package-verification.json',H/'validation/package-verification.json')
md=f'''# 유진 R01~R08 검증 결과 — 0.14.0-yujin-r08

- 소스 실행: {sc}개 사례 / {sa}개 확인 통과.
- 별도 Windows 패키지 실행: {nc}개 사례 / {na}개 확인 통과.
- 유진 R01~R04 대표 분기, 공통 C08→R08 연결, R05~R08 12개 조합, 저장 후 약속 변경, 연출 건너뛰기 후 이야기 기억, 호감도와 중복 없는 메시지를 확인했다.
- 메신저·크림 UI를 재검사하고 소스 실행에서 리아 전체 진행 8개 사례도 통과했다. 초기 검사에서 이벤트 이름을 문장 전체가 아닌 독립 텍스트로 찾던 검사문 오류가 있었으며 수정 후 통과했다.
- 패키지 {len(pkg['game_file_hashes'])}개 게임 파일이 검사한 소스의 최종 파일과 일치한다. 배포용 폴더에서 테스트·소스 대본·저장 파일을 제외했다. 패키지 검사는 격리된 복사본에서만 실행했다.
- 일반 대화 낮/밤, 선택지와 입상 배치, 유진 이벤트의 이름과 준비 중 표시를 캡처로 확인했다. 실제 최종 그림·표정 차분·음성의 품질을 검증한 결과는 아니다.
- 사용자 제공 이미지는 원본 그대로 게임에 복사하고 엔진으로만 상체를 잘랐다. 소스 외곽 잔여 픽셀과 고정된 수줍은 표정은 임시 자산의 알려진 한계다.
- 모든 선택 조합을 전수 조사한 것은 아니다. R09 이후와 최종 아트, 전체 상품 완성도는 이번 검사 범위 밖이다.

다음 구현은 R09~R12다. R08에서 선택한 실제 약속 요일·시각을 먼저 회수하고, 유진의 의견을 도현이 대신 말하지 않는 선택을 후속 갈등에 연결해야 한다. 새 그림 제작은 뒤로 둔다.
'''
(H/'docs/유진_R01-R08_검증결과_v1.md').write_text(md,encoding='utf-8')
# Retain the proven backup/hash workflow, with a narrow new runtime allowlist.
s=(S/'update_office_v2_yujin_r04.ps1').read_text(encoding='utf-8-sig')
s=s.replace('0.13.0-yujin-r04','0.14.0-yujin-r08').replace('yujin-r04','yujin-r08').replace('이전버전_0.12.1_유진초반적용전','이전버전_0.13.0_유진R08적용전')
s=s.replace('$validation.native_cases -ne 38',f'$validation.native_cases -ne {nc}')
s=s.replace("$modules=@('core.rpyc','cream_ui.rpyc','screens.rpyc','office_phone.rpyc','options.rpyc','yujin_r01_r04.rpyc')", "$modules=@('core.rpyc','cream_ui.rpyc','screens.rpyc','options.rpyc','yujin_r01_r04.rpyc','yujin_r05_r08.rpyc','event_sequence.rpyc','event_assets.json','event_story.json','event_cg_plan.json','images/characters/yujin/ui_temp_v001.png')")
s=s.replace("if($name -eq 'yujin_r01_r04.rpyc')", "if($name -in @('yujin_r05_r08.rpyc','images/characters/yujin/ui_temp_v001.png'))")
s=s.replace('A Yujin runtime already exists; inspect before overwrite','A new target already exists; inspect before overwrite')
s=s.replace('유진초반_v1','유진R08_v1').replace('유진초반_업데이트확인.json','유진R08_업데이트확인.json')
s=s.replace("foreach($f in Get-ChildItem -LiteralPath (Join-Path $handoff 'source\\game') -File){$writes.Add(@{Source=$f.FullName;Relative=('개발자료\\source\\game\\'+$f.Name)})}", "foreach($f in Get-ChildItem -LiteralPath (Join-Path $handoff 'source\\game') -File -Recurse){$rel=$f.FullName.Substring((Join-Path $handoff 'source\\game').Length+1);$writes.Add(@{Source=$f.FullName;Relative=('개발자료\\source\\game\\'+$rel)})}")
s=s.replace('CharacterAndRiggingFilesChanged=0','TemporaryPortraitAdded=1;RiggingFilesChanged=0').replace('SourceCases=46;NativeCases=38',f'SourceCases={sc};NativeCases={nc}')
(S/'update_office_v2_yujin_r08.ps1').write_text(s,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
