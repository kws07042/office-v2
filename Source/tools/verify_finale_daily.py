from pathlib import Path
src=Path(__file__).with_name('verify_click_interest.py').read_text(encoding='utf-8')
for a,b in [('0.25.0-click-interest','0.26.0-finale-daily'),('playable-click-interest','playable-finale-daily'),('native-click-interest','native-finale-daily'),('testing/click-interest-v1','testing/finale-daily-v1'),('testing/date-experience-v1/package-verification.json','testing/click-interest-v1/package-verification.json'),('0.24.0-date-experience','0.25.0-click-interest')]:src=src.replace(a,b)
exec(compile(src,str(Path(__file__)),'exec'))
