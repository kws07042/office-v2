from pathlib import Path
import hashlib
import json
import re
import shutil

P = Path(__file__).resolve().parents[1]
S = P.parent
proof = P / 'testing/integrated-review-v1'
H = S / 'afterwork-integrated-review-handoff-v1'
pkg = json.loads((proof / 'package-verification.json').read_text(encoding='utf-8'))
contract = json.loads((proof / 'source-contract.json').read_text(encoding='utf-8'))
native = Path(pkg['validation'])
clean = Path(pkg['clean_release'])
version = '0.28.0-integrated-review'
assert pkg['version'] == contract['version'] == version
for name, expected in pkg['game_file_hashes'].items():
    assert hashlib.sha256((clean / 'game' / name).read_bytes()).hexdigest() == expected, name
    expected_native = pkg['installed_unchanged_modules'].get(name, expected)
    assert hashlib.sha256((native / 'game' / name).read_bytes()).hexdigest() == expected_native, name
for name, expected in contract['source_sha256'].items():
    assert hashlib.sha256((P / 'game' / name).read_bytes()).hexdigest() == expected
    assert (P / 'game' / name).read_bytes() == (H / 'source/game' / name).read_bytes()

suites = 'ria12,integrated_story_checks,ria08,ria16_flow,jihyun_final_checks,yujin08_checks,yujin12_checks,yujin_final_checks,seoyun_checks,office_phone_checks,full_editorial_checks,five_asset_checks'.split(',')
details = []
for suite in suites:
    path = proof / ('final-' + suite + '.log')
    log = path.read_text(encoding='utf-8-sig')
    assert '[rpytest] Status: PASSED' in log, suite
    details.append({'suite': suite, 'cases': int(re.search(r'Test cases\s*:\s*\d+\s*\|\s*(\d+) passed', log)[1]), 'assertions': int(re.search(r'Assertions\s*:\s*\d+\s*\|\s*(\d+) passed', log)[1])})
    shutil.copy2(path, H / 'validation' / path.name)

trace_dir = native / 'review-output/integrated-v1'
trace_stats = []
for route in ('ria', 'jihyun', 'yujin', 'seoyun'):
    for variant in (0, 1):
        path = trace_dir / f'{route}-{variant}.json'
        trace = json.loads(path.read_text(encoding='utf-8'))
        assert trace['memory'][route + '_route_completed']
        assert trace['route'] == route
        assert trace['memory'][route + '_confession_accepted']
        assert not any('[memory' in row['text'] or '[ri(' in row['text'] for row in trace['rows'])
        chapters = list(dict.fromkeys(row['chapter'] for row in trace['rows']))
        assert any('E01' in x for x in chapters)
        assert all(any(x.startswith('C0' + str(i)) for x in chapters) for i in range(1, 9))
        for contact, rows in trace['messages'].items():
            assert len(rows) == len({r['id'] for r in rows}), (route, contact)
        trace_stats.append({'route': route, 'variant': variant, 'dialogue_rows': len(trace['rows']), 'choices': len(trace['choices']), 'messages': sum(len(rows) for rows in trace['messages'].values())})
        (H / 'validation/traces').mkdir(exist_ok=True)
        shutil.copy2(path, H / 'validation/traces' / path.name)

stats = {'version': version, 'native_status': 'passed', 'native_cases': sum(d['cases'] for d in details), 'native_assertions': sum(d['assertions'] for d in details), 'complete_common_to_epilogue_paths': 8, 'edited_story_labels': contract['edited_story_labels'], 'changed_runtime_files': len(contract['changed_files']), 'game_files_verified': len(pkg['game_file_hashes']), 'suites': details, 'traces': trace_stats, 'images_fonts_unchanged': True, 'human_reader_fun_or_time_measured': False, 'github_updated': False}
(proof / 'final-validation.json').write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding='utf-8')
for name in ('final-validation.json', 'source-contract.json', 'package-verification.json', 'edits.json', 'baseline.json'):
    shutil.copy2(proof / name, H / 'validation' / name)
shutil.copy2(P / '.renpy-agent/logs/20261021T083300-cc28cd63-lint.log', H / 'validation/lint.log')
for filename in ('integrated_story_tests.rpy', 'ria12_tests.rpy'):
    shutil.copy2(P / 'game' / filename, H / 'source/game' / filename)
for filename in ('prepare_integrated_tests.py', 'prepare_integrated_handoff.py', 'verify_integrated_package.py', 'modernize_ria12_tests.py', 'refresh_integrated_guides.py', 'finish_integrated_review.py'):
    shutil.copy2(P / 'tools' / filename, H / 'validation/tools' / filename)
failed = proof / 'native-ria12.log'
if failed.exists():
    shutil.copy2(failed, H / 'validation/legacy-ria12-failed-before-modernization.log')
for name in ('integrated-ria-early-date.png', 'integrated-yujin-early-date.png', 'integrated-jihyun-epilogue.png', 'integrated-seoyun-epilogue.png'):
    (H / 'validation/screenshots').mkdir(exist_ok=True)
    shutil.copy2(native / 'tests/screenshots' / name, H / 'validation/screenshots' / name)

md = f'''# 통합 검수 실행 결과 — {version}

2026-10-21. Ren’Py 구문 검사와 Windows 빌드를 통과했다. 최종 게임 파일 {stats['game_files_verified']}개를 원본과 대조했고 ZIP CRC·경로·개발 대본/검사/저장/측정 로그 제외·기존 폰트와 이미지 일치를 확인했다.

바탕화면 설치본에 실제 적용할 구성으로 검증했다. 이번에 바꾸는 15개 실행 파일은 새 빌드에서 가져오고, 수정하지 않는 기존 모듈 15개는 현재 바탕화면 파일을 진단 사본에도 그대로 넣었다. 사용자 그림·리깅 변경을 새 빌드로 덮어쓰지 않기 위한 구성이다.

최종 사본에서 {stats['native_cases']}사례 / {stats['native_assertions']}확인 통과. 재실행한 이전 성공 수를 중복 합산하지 않았다. 공통에서 후일담까지 네 루트×두 경로를 새 게임으로 진행해 대사·선택·메시지 기록 8개를 남겼다. 애정 표현·친밀 전환을 미루는 경로도 끝까지 이어진다. 기존 검사로 관계 종료/취소/보류, 실제 선택 일상과 기억, 저장/불러오기, 메신저 답장·사진 자리·기록, 이벤트 5자산 구조를 함께 확인했다. 모든 선택 조합의 전수 검사는 아니다.

| 검사 | 사례 | 확인 |
|---|---:|---:|
''' + ''.join(f"| {d['suite']} | {d['cases']} | {d['assertions']} |\n" for d in details) + '''
## 최초 실패와 조치

처음 실행한 과거 ria12 검사에서는 24사례가 실패했다. 메신저 전환을 일반 선택지로 기다려 시간 초과하거나, 축하 메시지를 메신저 기록 대신 대사 기록에서 찾던 검사였다. 현재 UI를 클릭해 진행하고 실제 `phone_threads`를 확인하도록 검사를 갱신했다. 현재 메신저 저장 구조에 맞춰 전환·대화 기록·복원 검증을 다시 작성했다. 공개 메시지를 보낸 뒤 저장을 불러오면 공개 여부·대화 기록이 함께 복원되는지, 친밀한 진행을 택했다가 불러오면 선택/표시 기록도 복원되는지 확인한다. 최종 ria12의 32분기+진입 가드 2개는 통과했다. 최초 실패 로그도 보존한다.

화면 검수에서 유진 R05가 공원으로 이동해도 HUD가 서점으로 남는 것을 찾아 수정했다. 마지막 빌드와 연속 실행에서 공원 장소 표시를 다시 확인했다. 확인한 리아·유진 초기 데이트, 지현·서윤 후일담 화면의 선택지·대사에 잘림은 없었다. 지현·서윤 최종 입상과 배경은 아직 준비 전이므로 그림 품질 완료 판정은 아니다.

자동 실행과 편집자의 이어 읽기는 실제 독자의 재미·몰입·읽기 시간을 측정한 결과가 아니다. 초반 고백 60~90분 목표도 아직 실측값이 아니다. 반복 소재와 남은 편집 약점은 ‘공통과네루트_통합검수와수정_v1.md’에 별도로 남겼다.
'''
(H / 'docs/통합검수_실행검증_v1.md').write_text(md, encoding='utf-8')
(P / 'story/integrated_review_validation_v1.md').write_text(md, encoding='utf-8')

installer = (S / 'update_office_v2_romance_focus.ps1').read_text(encoding='utf-8-sig')
installer = installer.replace("$release=Join-Path $stage 'afterwork-windows-builds\\playable-romance-focus\\afterwork_script_prototype-0.27.0-romance-focus-win'", "$release='" + str(clean).replace("'", "''") + "'")
installer = installer.replace('afterwork-romance-focus-handoff-v1', 'afterwork-integrated-review-handoff-v1')
installer = installer.replace('이전버전_0.26.0_연애편집전', '이전버전_0.27.0_통합검수전')
installer = installer.replace('testing\\romance-focus-v1', 'testing\\integrated-review-v1')
installer = re.sub(r'\$modules=@\([^\n]+\)', "$modules=@(" + ','.join("'" + n.replace('.rpy', '.rpyc') + "'" for n in contract['changed_files']) + ")", installer)
installer = installer.replace(' -ne 91)', ' -ne ' + str(stats['native_cases']) + ')')
installer = installer.replace('NativeCases=91;', 'NativeCases=' + str(stats['native_cases']) + ';')
installer = installer.replace('0.27.0-romance-focus', version)
installer = installer.replace('연애중심편집_v1', '통합검수_v1').replace('연애중심편집_업데이트확인.json', '통합검수_업데이트확인.json')
check = r'''$package=Get-Content -LiteralPath (Join-Path $handoff 'validation\package-verification.json') -Raw | ConvertFrom-Json
foreach($property in $package.installed_unchanged_modules.PSObject.Properties){
 $path=Join-Path $target ('game\'+$property.Name)
 if((Get-FileHash -LiteralPath $path).Hash.ToLowerInvariant() -ne $property.Value){throw ('Concurrent dependency edit: '+$property.Name)}
}
'''
installer = installer.replace('$writes=[Collections.Generic.List[object]]::new()', check + '$writes=[Collections.Generic.List[object]]::new()')
assert '$release=Join-Path' not in installer and 'romance-focus' not in installer
assert not any(ord(c) < 32 and c not in '\n\r\t' for c in installer)
(S / 'update_office_v2_integrated_review.ps1').write_text(installer, encoding='utf-8-sig')
print(json.dumps({'cases': stats['native_cases'], 'assertions': stats['native_assertions'], 'complete_paths': 8, 'installer': str(S / 'update_office_v2_integrated_review.ps1')}, ensure_ascii=False))
