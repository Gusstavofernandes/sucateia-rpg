with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    content = f.read()

import re
ext_resources = {}
for m in re.finditer(r'\[ext_resource type="([^"]+)" path="([^"]+)" id="([^"]+)"\]', content):
    if m.group(2).endswith('.svg'):
        ext_resources[m.group(3)] = m.group(2)

node_blocks = re.split(r'\n(?=\[node )', content)
print('ALL Nodes using SVG props (crate/barrel/chest/etc):')
for b in node_blocks:
    if not b.startswith('[node '): continue
    for k, v in ext_resources.items():
        if f'ExtResource("{k}")' in b and 'light.svg' not in v:
            header = b.split('\n')[0]
            pos_m = re.search(r'position = Vector2\(([^,]+),\s*([^)]+)\)', b)
            pos = pos_m.group(0) if pos_m else 'no pos'
            print(f'  {header} | {pos} | {v}')
