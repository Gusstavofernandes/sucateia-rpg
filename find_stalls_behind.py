with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find nodes around x=900-1400, y=100-500
nodes = re.split(r'\n\[node ', text)
for n in nodes:
    pos_m = re.search(r'position = Vector2\(\s*([-\d\.]+),\s*([-\d\.]+)\s*\)', n)
    if pos_m:
        x, y = float(pos_m.group(1)), float(pos_m.group(2))
        if 900 <= x <= 1400 and 100 <= y <= 550:
            header = n.split('\n')[0]
            tex_m = re.search(r'texture = ExtResource\("([^"]+)"\)', n)
            tex_id = tex_m.group(1) if tex_m else ''
            print(f"({x:6.1f}, {y:6.1f}) | {header} | {tex_id}")
