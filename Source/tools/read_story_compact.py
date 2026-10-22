"""Read-only editorial view; retain conditions, dialogue, choices and phone text."""
import ast
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
root = Path(__file__).resolve().parents[1] / 'game'
for name in sys.argv[1:]:
    print('\nFILE', name)
    for number, raw in enumerate((root / name).read_text(encoding='utf-8-sig').splitlines(), 1):
        text = raw.strip()
        if not text or text.startswith('#'):
            continue
        if text.startswith('$') and not text.startswith(('$ chapter', '$ location')):
            continue
        if text.startswith(('show ', 'hide ', 'scene ', 'return', 'with ', 'pause', 'window ', 'define ', 'default ')):
            continue
        def informal(match):
            return ast.literal_eval(match.group(1))
        text = re.sub(r"\[ri\(('(?:[^'\\]|\\.)*'),\s*'(?:[^'\\]|\\.)*'\)\]", informal, text)
        print(f'{number}: {text}')
