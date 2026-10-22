with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

nodes = re.split(r'\n\[node ', text)
ext_map = {}
for line in text.split('\n'):
    if line.startswith('[ext_resource'):
        m_id = re.search(r'id="([^"]+)"', line)
        m_path = re.search(r'path="([^"]+)"', line)
        if m_id and m_path:
            ext_map[m_id.group(1)] = m_path.group(1)

for n in nodes:
    header = n.split('\n')[0]
    pos = re.search(r'position = Vector2\(([^\)]+)\)', n)
    if pos:
        parts = [float(p.strip()) for p in pos.group(1).split(',')]
        if len(parts) == 2:
            x, y = parts
            if 300 <= x <= 1600 and 300 <= y <= 850:
                tex_m = re.search(r'texture = ExtResource\("([^"]+)"\)', n)
                tex_path = ext_map.get(tex_m.group(1), 'no tex') if tex_m else 'no tex'
                if 'house' in tex_path or 'house' in header or 'Structures' in header:
                    print(f'{header} | ({x}, {y}) | {tex_path}')
