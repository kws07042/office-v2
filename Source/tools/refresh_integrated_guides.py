from pathlib import Path
import hashlib
import json
import sys
import zipfile

P = Path(__file__).resolve().parents[1]
S = P.parent
proof = P / 'testing/integrated-review-v1'
guide = (S / 'afterwork-integrated-review-handoff-v1/시작안내.txt').read_bytes()
if sys.argv[1] == 'prepare':
    for name in ('README.md', 'WINDOWS-README.txt'):
        backup = proof / (name + '.before')
        if not backup.exists():
            backup.write_bytes((P / name).read_bytes())
        (P / name).write_bytes(guide)
else:
    path = proof / 'package-verification.json'
    package = json.loads(path.read_text(encoding='utf-8'))
    zip_path = S / 'afterwork-windows-builds/afterwork_script_prototype-0.28.0-integrated-review-win.zip'
    prefix = 'afterwork_script_prototype-0.28.0-integrated-review-win/'
    clean = Path(package['clean_release'])
    for name, expected in package['game_file_hashes'].items():
        assert hashlib.sha256((clean / 'game' / name).read_bytes()).hexdigest() == expected, name
    for name in ('README.md', 'WINDOWS-README.txt'):
        (clean / name).write_bytes(guide)
        (Path(package['validation']) / name).write_bytes(guide)
    # Package the already verified official Windows build, preserving its ZIP
    # member metadata and executable/runtime files. Do not substitute recompiled
    # script bytes produced while compiling the refreshed diagnostic tests.
    temporary = zip_path.with_suffix('.guides.tmp')
    assert temporary.resolve().parent == zip_path.resolve().parent
    with zipfile.ZipFile(zip_path) as original, zipfile.ZipFile(temporary, 'w') as output:
        for info in original.infolist():
            assert info.filename.startswith(prefix), info.filename
            rel = info.filename[len(prefix):]
            source = (clean / rel).resolve()
            assert source.is_relative_to(clean.resolve()), rel
            output.writestr(info, b'' if info.is_dir() else source.read_bytes())
    with zipfile.ZipFile(temporary) as archive:
        assert archive.testzip() is None
        for name, expected in package['game_file_hashes'].items():
            assert hashlib.sha256(archive.read(prefix + 'game/' + name)).hexdigest() == expected, name
    temporary.replace(zip_path)
    package['zip_sha256'] = hashlib.sha256(zip_path.read_bytes()).hexdigest()
    package['zip_bytes'] = zip_path.stat().st_size
    package['guides_refreshed_without_game_file_changes'] = True
    path.write_text(json.dumps(package, ensure_ascii=False, indent=2), encoding='utf-8')
    print('Updated release guides; all 54 game files unchanged.')
