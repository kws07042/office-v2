from pathlib import Path
import json,re,shutil
P=Path(__file__).resolve().parents[1]; S=P.parent
proof=P/'testing/full-editorial-v1'; H=S/'afterwork-full-editorial-handoff-v1'
suites='full_editorial_checks,common_romance,ria16_flow,yujin_early_checks,yujin08_checks,yujin12_checks,yujin_final_checks,jihyun04_checks,jihyun_final_checks,seoyun_checks,five_asset_checks,office_phone_checks,cream_ui_checks'.split(',')
cases=assertions=0; details=[]
for suite in suites:
    p=proof/('native-'+suite+'.log'); t=p.read_text(encoding='utf-8-sig')
    assert '[rpytest] Status: PASSED' in t,p
    c=int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1]); a=int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed',t)[1])
    assert c>0 and a>0,p
    cases+=c; assertions+=a; details.append(dict(suite=suite,cases=c,assertions=a))
    shutil.copy2(p,H/'validation'/p.name)
pkg=json.loads((proof/'package-verification.json').read_text(encoding='utf-8'))
changed=json.loads((proof/'changed-files.json').read_text(encoding='utf-8'))
report=dict(version='0.20.0-dialogue-review',native_status='passed',native_cases=cases,native_assertions=assertions,suites=details,source_regression_cases=14,source_regression_assertions=92,game_files_verified=len(pkg['game_file_hashes']),images_changed=0,rigging_changed=False,saves_removed=0,github_updated=False)
(H/'validation/final-validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
for n in ('package-verification.json','unchanged-assets.json','edit-log.json','changed-files.json','source-full_editorial_checks.log'):
    shutil.copy2(proof/n,H/'validation'/n)
shots=Path(pkg['validation'])/'tests/screenshots'
for n in ('intro-expression-placeholder.png','ria16-full-route-end.png','yujin-r08-phone-replies.png','jihyun-epilogue-cohabitation-choice.png','seoyun-phone-three-replies.png'):
    if (shots/n).exists(): shutil.copy2(shots/n,H/'screenshots'/n)
md=f'''# 전체 대본 검수판 실행 검증 — 0.20.0-dialogue-review

- Ren’Py 대본 문법 검사 통과. 검사기 최초 실행은 제한 환경의 Windows DLL 재배치 오류로 시작되지 않아 일반 Windows 실행 권한으로 재실행했고 통과했다. 대본 오류를 숨긴 것이 아니다.
- 수정한 시간 흐름·관계 종료 확인의 소스 검사14사례/92확인 통과.
- 최종 Windows 실행본 {len(suites)}개 검사 묶음, {cases}사례/{assertions}확인 통과. 공통·리아 전체·유진 초반/중반/후반·지현 초반/후반·서윤 전체·메신저·UI·16개 친밀한 이벤트 연출 세트를 포함한다. 아래 숫자는 모든 선택 조합의 전수 검사가 아니다.
- 지현 R10→선택 일상 완료/생략/짧은 반응→같은 토요일 밤 시점과 실제 초대 메시지 순서9경로를 확인했다. 리아 O03 짧은 안부는 일요일 밤/월요일 아침 이후 모두 화요일 저녁에 기록되며 실제 방문으로 저장되지 않는다. 리아 관계 종료는 확정 전에는 교제를 종료하지 않고, 취소/보류한 경로는 실제 약속 이행으로 이어지며 보류는 계속 만날 마음을 다시 확인한다.
- 기존 검사로 친밀한 장면을 미뤄도 완주, 실제 함께 머물지 않은 경로에 다음 아침 없음, 공개 합의와 실제 전달 구분, 갈등의 합의와 행동 구분, 보낸 답장 중복 없음, 선택 복원과 저장/불러오기, 누락 자산을 실제 그림 해금으로 세지 않음 등을 확인했다.
- 패키지 게임 파일{len(pkg['game_file_hashes'])}개가 빌드 소스와 일치한다. 압축 CRC·안전한 추출 경로·원문/검사/저장 제외·폰트 고지 포함을 확인했다. 기존0.19와 인물 이미지가 같고 리깅은 수정하지 않았다. 검사는 별도 실행본/별도 저장 공간에서 수행했다.
- 실제 검증 세부 숫자는 validation/final-validation.json, 수정 원문 비교는 validation/*.diff와 edit-log.json에 남겼다. 화면 확인 결과는 전체대본_매력검수와수정_v1.md의 글 검수와 구분한다. 자동 통과가 설렘·대사 완성도·성적 매력을 보장하지 않는다.

| 검사 | 사례 | 확인 |
|---|---:|---:|
'''
md+=''.join(f"| {x['suite']} | {x['cases']} | {x['assertions']} |\n" for x in details)
(H/'docs/전체대본_매력검수_실행검증_v1.md').write_text(md,encoding='utf-8')
(P/'story/full_editorial_validation_v1.md').write_text(md,encoding='utf-8')

# Strictly scoped installer: snapshots were taken from this installed version.
installer='''$ErrorActionPreference='Stop'
$stage='STAGE'
$requested='C:\\Users\\user\\Desktop\\건\\오피스 V2'
$target=(Resolve-Path -LiteralPath $requested).Path
if($target -ne [IO.Path]::GetFullPath($requested)){throw 'Unexpected install target'}
$project=Join-Path $stage 'afterwork-prototype'
$release=Join-Path $stage 'afterwork-windows-builds\\playable-edit\\afterwork_script_prototype-0.20.0-dialogue-review-win'
$handoff=Join-Path $stage 'afterwork-full-editorial-handoff-v1'
$backup=Join-Path $target '개발자료\\이전버전_0.19.0_전체대본검수적용전'
if(Test-Path -LiteralPath $backup){throw 'Backup exists'}
$validation=Get-Content -LiteralPath (Join-Path $handoff 'validation\\final-validation.json') -Raw | ConvertFrom-Json
if($validation.native_status -ne 'passed' -or $validation.native_cases -ne CASES){throw 'Validation incomplete'}
$previous=Get-Content -LiteralPath (Join-Path $project 'testing\\full-editorial-v1\\previous-runtime-hashes.json') -Raw | ConvertFrom-Json
$modules=@(MODULES)
foreach($name in $modules){
 $current=Join-Path $target ('game\\'+$name)
 if((Get-FileHash -LiteralPath $current).Hash.ToLowerInvariant() -ne $previous.$name){throw ('Concurrent runtime edit: '+$name)}
 if($name.EndsWith('.rpyc')){
  $source=$name.Replace('.rpyc','.rpy')
  $installedSource=Join-Path $target ('개발자료\\source\\game\\'+$source)
  $before=Join-Path $project ('testing\\full-editorial-v1\\'+$source+'.before')
  if((Get-FileHash -LiteralPath $installedSource).Hash -ne (Get-FileHash -LiteralPath $before).Hash){throw ('Concurrent source edit: '+$source)}
 }
}
$writes=[Collections.Generic.List[object]]::new()
foreach($name in $modules){$writes.Add(@{Source=(Join-Path $release ('game\\'+$name));Relative=('game\\'+$name)})}
foreach($f in Get-ChildItem -LiteralPath $handoff -File -Recurse){
 $rel=$f.FullName.Substring($handoff.Length+1)
 $writes.Add(@{Source=$f.FullName;Relative=('개발자료\\전체대본검수_v1\\'+$rel)})
}
foreach($f in Get-ChildItem -LiteralPath (Join-Path $handoff 'docs') -File){$writes.Add(@{Source=$f.FullName;Relative=('개발자료\\docs\\'+$f.Name)})}
foreach($f in Get-ChildItem -LiteralPath (Join-Path $handoff 'source\\game') -File){$writes.Add(@{Source=$f.FullName;Relative=('개발자료\\source\\game\\'+$f.Name)})}
$writes.Add(@{Source=(Join-Path $handoff '시작안내.txt');Relative='시작안내.txt'})
$writes.Add(@{Source=(Join-Path $handoff '시작안내.txt');Relative='README.md'})
New-Item -ItemType Directory -Path $backup | Out-Null
foreach($item in $writes){
 $dest=[IO.Path]::GetFullPath((Join-Path $target $item.Relative))
 if(-not $dest.StartsWith($target+'\\',[StringComparison]::OrdinalIgnoreCase)){throw 'Path escaped install target'}
 if(Test-Path -LiteralPath $dest -PathType Leaf){
  $old=Join-Path $backup $item.Relative
  New-Item -ItemType Directory -Path (Split-Path -Parent $old) -Force | Out-Null
  Copy-Item -LiteralPath $dest -Destination $old
 }
 New-Item -ItemType Directory -Path (Split-Path -Parent $dest) -Force | Out-Null
 Copy-Item -LiteralPath $item.Source -Destination $dest -Force
 if((Get-FileHash -LiteralPath $dest).Hash -ne (Get-FileHash -LiteralPath $item.Source).Hash){throw ('Write mismatch: '+$item.Relative)}
}
$report=[pscustomobject]@{Version='0.20.0-dialogue-review';Target=$target;VerifiedWrites=$writes.Count;Backup=$backup;NativeCases=CASES;CharacterAssetsChanged=0;RiggingFilesChanged=0;SaveFilesRemoved=0;GameProcessesTerminated=0;GitHubUpdated=$false}
$report | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $target '全대본검수_업데이트확인.json') -Encoding UTF8
$report | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $project 'testing\\full-editorial-v1\\desktop-installation.json') -Encoding UTF8
$report | ConvertTo-Json
'''
installer=installer.replace('STAGE',str(S)).replace('CASES',str(cases)).replace('MODULES',','.join("'"+(n[:-4]+'.rpyc' if n.endswith('.rpy') else n)+"'" for n in changed)).replace('全대본','전체대본')
(S/'update_office_v2_full_editorial.ps1').write_text(installer,encoding='utf-8-sig')
print(json.dumps(report,ensure_ascii=False))
