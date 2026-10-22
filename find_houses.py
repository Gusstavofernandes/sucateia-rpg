with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find buildings/houses around x=1800-2400, y=500-1200
nodes = re.split(r'\n\[node ', text)
ext_map = {}
for line in text.split('\n'):
    if line.startswith('[ext_resource'):
        m_id = re.search(r'id="([^"]+)"', line)
        m_path = re.search(r'path="([^"]+)"', line)
        if m_id and m_path:
            ext_map[m_id.group(1)] = m_path.group(1)

for n in nodes:
    if any(k in n for k in ['house', 'casa', 'dwelling', 'cabin', 'workshop', 'building', 'shack']):
        pos_m = re.search(r'position = Vector2\(\s*([-\d\.]+),\s*([-\d\.]+)\s*\)', n)
        if pos_m:
            x, y = float(pos_m.group(1)), float(pos_m.group(2))
            if 1500 <= x <= 2500 and 300 <= y <= 1500:
                header = n.split('\n')[0]
                tex_m = re.search(r'texture = ExtResource\("([^"]+)"\)', n)
                tex_id = tex_m.group(1) if tex_m else None
                tex_path = ext_map.get(tex_id, 'no tex')
                print(f"({x:6.1f}, {y:6.1f}) | {header} | {tex_path}")
