with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    content = f.read()

import re
node_blocks = re.split(r'\n(?=\[node )', content)

for b in node_blocks:
    for name in ['Structures/barrel', 'Structures/crate', 'Structures/@Node2D@79', 'Structures/@Node2D@84', 'Structures/@Node2D@102', 'Structures/@Node2D@105']:
        if f'name="{name.split("/")[-1]}"' in b and 'parent="Structures"' in b:
            header = b.split('\n')[0]
            pos_m = re.search(r'position = Vector2\(([^,]+),\s*([^)]+)\)', b)
            pos = pos_m.group(0) if pos_m else 'no pos'
            print(f'{header} | {pos}')
