from pathlib import Path
source = Path(__file__).with_name('verify_yujin_r04_package.py').read_text(encoding='utf-8')
source = source.replace('0.13.0-yujin-r04', '0.14.0-yujin-r08').replace('yujin-r04', 'yujin-r08')
source = source.replace("'yujin_r01_r04.rpyc', 'fonts", "'yujin_r01_r04.rpyc', 'yujin_r05_r08.rpyc', 'images/characters/yujin/ui_temp_v001.png', 'fonts")
source = source.replace("('yujin_tests.rpyc', 'office_phone_tests.rpyc', 'cream_tests.rpyc')", "('yujin_tests.rpyc', 'yujin08_tests.rpyc', 'office_phone_tests.rpyc', 'cream_tests.rpyc')")
exec(compile(source, str(Path(__file__)), 'exec'))
