from pathlib import Path
import json
import numpy as np
from PIL import Image, ImageDraw

P = Path(__file__).resolve().parents[1]
shots = P.parent/'afterwork-windows-builds/native-validation-ria-expressions/tests/screenshots'
proof = P/'testing/ria-expressions'
points = {
    'forehead_skin': (491,178), 'nose_lower': (480,252), 'chin_skin': (490,289),
    'neck_skin': (514,300), 'left_shoulder': (395,351), 'right_upper_arm': (645,430),
    'left_cheek': (437,254), 'right_cheek': (554,244),
}
report = {}
for mode in ['day','night']:
    base = np.asarray(Image.open(shots/f'ria-expression-{mode}-base.png').convert('RGB'))
    assert base.shape[:2] == (720,1280)
    result = {}
    for mood in ['smile','shy','serious']:
        arr = np.asarray(Image.open(shots/f'ria-expression-{mode}-{mood}.png').convert('RGB'))
        diff = np.any(base[20:490,430:850] != arr[20:490,430:850], axis=2)
        y,x = np.where(diff)
        samples = {}
        for key,(sx,sy) in points.items():
            px,py = round(340.75+(sx-190)*.95), round(28+(sy-40)*.95)
            same = bool(np.array_equal(base[py,px],arr[py,px]))
            samples[key] = {'pixel':[px,py], 'base':base[py,px].tolist(), 'expression':arr[py,px].tolist(), 'same':same}
            if not (mood == 'shy' and key.endswith('cheek')):
                assert same, (mode,mood,key,samples[key])
        body_same = bool(np.array_equal(base[315:488,445:840], arr[315:488,445:840]))
        assert body_same, (mode,mood,'body')
        result[mood] = {'changed_bbox':[int(x.min()+430),int(y.min()+20),int(x.max()+431),int(y.max()+21)],
                        'body_comparison_pixels_identical':body_same, 'skin_samples':samples}
    report[mode] = result
(proof/'native-rendered-skin-and-body-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
# Inspection-only face comparisons from actual game screenshots, not replacement artwork.
sheet = Image.new('RGB',(1440,692),'#343549')
draw = ImageDraw.Draw(sheet)
for row,mode in enumerate(['day','night']):
    for col,mood in enumerate(['base','smile','shy','serious']):
        im = Image.open(shots/f'ria-expression-{mode}-{mood}.png').convert('RGB').crop((530,135,710,295)).resize((360,320))
        draw.text((col*360+8,row*346+6),mode+' / '+mood,fill='white')
        sheet.paste(im,(col*360,row*346+26))
sheet.save(proof/'expression-skin-comparison.jpg',quality=95)
print(json.dumps({'modes':2,'expressions':3,'body_regions_identical':True,
                  'non_blush_skin_control_samples_unchanged':True,'cheek_blush_only_allowed_for_shy':True,
                  'proof':str(proof/'native-rendered-skin-and-body-check.json')}))
