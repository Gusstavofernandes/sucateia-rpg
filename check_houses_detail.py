with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for name in ['house_0', 'house_1', 'house_2', 'house_3', '@Node2D@72']:
    m = re.search(r'\[node name="' + re.escape(name) + r'"[^\n]*\n([^\n]+\n){1,25}', text)
    if m:
        print(f"=== {name} ===")
        print(m.group(0))
