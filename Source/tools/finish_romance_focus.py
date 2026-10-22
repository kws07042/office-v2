from pathlib import Path
import hashlib
import json
import re
import shutil

P = Path(__file__).resolve().parents[1]
S = P.parent
proof = P / "testing/romance-focus-v1"
handoff = S / "afterwork-romance-focus-handoff-v1"
contract = json.loads((proof / "source-contract.json").read_text(encoding="utf-8"))
package = json.loads((proof / "package-verification.json").read_text(encoding="utf-8"))
clean = Path(package["clean_release"])
assert package["version"] == contract["version"] == "0.27.0-romance-focus"
for name, digest in package["game_file_hashes"].items():
    assert hashlib.sha256((clean / "game" / name).read_bytes()).hexdigest() == digest, name
assert all("맥주" not in (handoff / "docs" / name).read_text(encoding="utf-8") for name in
           ("연애중심_대사편집과서윤술데이트_v1.md", "한서윤_검수후_현행대본.md"))
for name in contract["changed_files"]:
    assert (P / "game" / name).read_bytes() == (handoff / "source/game" / name).read_bytes(), name
    assert (P / "game" / name).read_text(encoding="utf-8") != (proof / (name + ".before")).read_text(encoding="utf-8")

suites = (
    "ria16_flow", "jihyun_final_checks", "yujin08_checks",
    "yujin_final_checks", "seoyun_checks",
)
details = []
for suite in suites:
    log = proof / ("native-whisky-" + suite + ".log")
    data = log.read_text(encoding="utf-8-sig")
    assert "[rpytest] Status: PASSED" in data, suite
    cases = int(re.search(r"Test cases\s*:\s*\d+\s*\|\s*(\d+) passed", data).group(1))
    assertions = int(re.search(r"Assertions\s*:\s*\d+\s*\|\s*(\d+) passed", data).group(1))
    details.append({"suite": suite, "cases": cases, "assertions": assertions})
    shutil.copy2(log, handoff / "validation" / log.name)

report = {
    "version": "0.27.0-romance-focus",
    "native_status": "passed",
    "native_cases": sum(item["cases"] for item in details),
    "native_assertions": sum(item["assertions"] for item in details),
    "scene_blocks_rewritten": 19,
    "game_files_verified": len(package["game_file_hashes"]),
    "source_files_changed": len(contract["changed_files"]),
    "choice_counts_control_flow_flags_awards_unchanged": True,
    "images_changed": 0,
    "human_fun_tested": False,
    "github_updated": False,
    "suites": details,
}
(proof / "final-validation.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
for name in ("final-validation.json", "source-contract.json", "unchanged-assets.json", "package-verification.json"):
    shutil.copy2(proof / name, handoff / "validation" / name)
lint = P / ".renpy-agent/logs/20261020T132637-dbb5607a-lint.log"
assert lint.exists()
shutil.copy2(lint, handoff / "validation/lint.log")
for name in ("prepare_romance_focus.py", "verify_romance_focus.py", "finish_romance_focus.py", "run_revision_tests.ps1"):
    (handoff / "validation/tools").mkdir(exist_ok=True)
    shutil.copy2(P / "tools" / name, handoff / "validation/tools" / name)
for name in ("ria16_tests.rpy", "jihyun_final_tests.rpy", "yujin08_tests.rpy", "yujin_final_tests.rpy", "seoyun_tests.rpy"):
    shutil.copy2(P / "game" / name, handoff / "source/game" / name)

validation_md = f"""# 연애 중심 편집 실행 검증 — Windows {report['version']}

Ren’Py 구문 검사와 Windows 빌드 완료. 기존 오피스 V2의 대본과 비교해 메뉴 개수, 조건, 호출, 상태 기록, 보상·호감도 처리의 구조를 대조했다. 서윤 R15는 위스키 식사 뒤 집에서 별도의 친밀 선택을 묻고, 기존 진행/귀가/대화 세 갈래로 이어진다.

실제 Windows 진단 사본에서 {report['native_cases']}사례·{report['native_assertions']}확인 통과. 검사한 경로는 아래와 같다.

| 검사 | 사례 | 확인 |
|---|---:|---:|
""" + "".join(f"| {item['suite']} | {item['cases']} | {item['assertions']} |\n" for item in details) + f"""
패키지 CRC, 상대 경로, 원문·테스트·저장 파일 제외, 게임 파일 {report['game_files_verified']}개의 빌드 전후 일치를 확인했다. 이미지는 이전 0.26.0과 같고 리깅·음성·CG는 수정하지 않았다. 자동 검사는 분기와 실행을 확인하며 실제 플레이어의 재미를 증명하지 않는다.
"""
(handoff / "docs/연애중심_실행검증_v1.md").write_text(validation_md, encoding="utf-8")
(P / "story/romance_focus_validation_v1.md").write_text(validation_md, encoding="utf-8")

stage = str(S).replace("'", "''")
target = "C:\\Users\\user\\Desktop\\건\\오피스 V2"
modules = [name.replace(".rpy", ".rpyc") for name in contract["changed_files"]]
modules_literal = ",".join("'" + name + "'" for name in modules)
installer = r"""$ErrorActionPreference='Stop'
$stage='STAGE'
$requested='TARGET'
$target=(Resolve-Path -LiteralPath $requested).Path
if($target -ne [IO.Path]::GetFullPath($requested)){throw 'Unexpected install target'}
$project=Join-Path $stage 'afterwork-prototype'
$release=Join-Path $stage 'afterwork-windows-builds\playable-romance-focus\afterwork_script_prototype-0.27.0-romance-focus-win'
$handoff=Join-Path $stage 'afterwork-romance-focus-handoff-v1'
$backup=Join-Path $target '개발자료\이전버전_0.26.0_연애편집전'
if(-not ([IO.Path]::GetFullPath($backup)).StartsWith($target+'\',[StringComparison]::OrdinalIgnoreCase)){throw 'Unsafe backup path'}
if(Test-Path -LiteralPath $backup){throw 'Backup exists'}
$proof=Join-Path $project 'testing\romance-focus-v1'
$validation=Get-Content -LiteralPath (Join-Path $handoff 'validation\final-validation.json') -Raw | ConvertFrom-Json
if($validation.native_status -ne 'passed' -or $validation.native_cases -ne CASES){throw 'Validation incomplete'}
$contract=Get-Content -LiteralPath (Join-Path $proof 'source-contract.json') -Raw | ConvertFrom-Json
$modules=@(MODULES)
foreach($name in $modules){
 $current=Join-Path $target ('game\'+$name)
 if((Get-FileHash -LiteralPath $current).Hash.ToLowerInvariant() -ne $contract.previous_runtime_hashes.$name){throw ('Concurrent runtime edit: '+$name)}
 $src=$name.Replace('.rpyc','.rpy')
 $installed=Join-Path $target ('개발자료\source\game\'+$src)
 $before=Join-Path $proof ($src+'.before')
 if([IO.File]::ReadAllText($installed).Replace("`r`n","`n") -cne [IO.File]::ReadAllText($before).Replace("`r`n","`n")){throw ('Concurrent source edit: '+$src)}
}
$writes=[Collections.Generic.List[object]]::new()
foreach($name in $modules){$writes.Add(@{Source=(Join-Path $release ('game\'+$name));Relative=('game\'+$name)})}
foreach($file in Get-ChildItem -LiteralPath $handoff -File -Recurse){
 $rel=$file.FullName.Substring($handoff.Length+1)
 $writes.Add(@{Source=$file.FullName;Relative=('개발자료\연애중심편집_v1\'+$rel)})
}
foreach($file in Get-ChildItem -LiteralPath (Join-Path $handoff 'docs') -File){$writes.Add(@{Source=$file.FullName;Relative=('개발자료\docs\'+$file.Name)})}
foreach($file in Get-ChildItem -LiteralPath (Join-Path $handoff 'source\game') -File){$writes.Add(@{Source=$file.FullName;Relative=('개발자료\source\game\'+$file.Name)})}
foreach($name in @('시작안내.txt','README.md','WINDOWS-README.txt')){$writes.Add(@{Source=(Join-Path $handoff '시작안내.txt');Relative=$name})}
$seen=[Collections.Generic.HashSet[string]]::new([StringComparer]::OrdinalIgnoreCase)
foreach($item in $writes){
 if(-not (Test-Path -LiteralPath $item.Source -PathType Leaf)){throw ('Missing source: '+$item.Source)}
 $dest=[IO.Path]::GetFullPath((Join-Path $target $item.Relative))
 if(-not $dest.StartsWith($target+'\',[StringComparison]::OrdinalIgnoreCase)){throw 'Path escaped install target'}
 if(-not $seen.Add($dest)){throw ('Duplicate target: '+$dest)}
}
New-Item -ItemType Directory -Path $backup | Out-Null
foreach($item in $writes){
 $dest=[IO.Path]::GetFullPath((Join-Path $target $item.Relative))
 if(Test-Path -LiteralPath $dest -PathType Leaf){
  $old=Join-Path $backup $item.Relative
  New-Item -ItemType Directory -Path (Split-Path -Parent $old) -Force | Out-Null
  Copy-Item -LiteralPath $dest -Destination $old
 }
 New-Item -ItemType Directory -Path (Split-Path -Parent $dest) -Force | Out-Null
 Copy-Item -LiteralPath $item.Source -Destination $dest -Force
 if((Get-FileHash -LiteralPath $dest).Hash -ne (Get-FileHash -LiteralPath $item.Source).Hash){throw ('Write mismatch: '+$item.Relative)}
}
$report=[pscustomobject]@{Version='0.27.0-romance-focus';Target=$target;VerifiedWrites=$writes.Count;Backup=$backup;NativeCases=CASES;CharacterAssetsChanged=0;RiggingFilesChanged=0;SaveFilesRemoved=0;GameProcessesTerminated=0;GitHubUpdated=$false}
$report | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $target '연애중심편집_업데이트확인.json') -Encoding UTF8
$report | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $proof 'desktop-installation.json') -Encoding UTF8
$report | ConvertTo-Json
""".replace("STAGE", stage).replace("TARGET", target).replace("MODULES", modules_literal).replace("CASES", str(report["native_cases"]))
(S / "update_office_v2_romance_focus.ps1").write_text(installer, encoding="utf-8-sig")
print(json.dumps(report, ensure_ascii=False))
