with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

nodes = re.split(r'\n\[node ', text)
print(f"Total nodes: {len(nodes)}")

found = []
for n in nodes:
    pos_m = re.search(r'position = Vector2\(\s*([-\d\.]+),\s*([-\d\.]+)\s*\)', n)
    if pos_m:
        x, y = float(pos_m.group(1)), float(pos_m.group(2))
        if 1600 <= x <= 2600 and 600 <= y <= 1200:
            header = n.split('\n')[0]
            tex_m = re.search(r'texture = ExtResource\("([^"]+)"\)', n)
            tex_id = tex_m.group(1) if tex_m else None
            found.append((x, y, header, tex_id))

# Also extract ext_resource paths
ext_map = {}
for line in text.split('\n'):
    if line.startswith('[ext_resource'):
        m_id = re.search(r'id="([^"]+)"', line)
        m_path = re.search(r'path="([^"]+)"', line)
        if m_id and m_path:
            ext_map[m_id.group(1)] = m_path.group(1)

for x, y, header, tex_id in sorted(found, key=lambda item: (item[1], item[0])):
    tex_path = ext_map.get(tex_id, 'no tex')
    print(f"({x:6.1f}, {y:6.1f}) | {header} | {tex_path}")
