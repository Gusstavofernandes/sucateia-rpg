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
    if 'parent="Structures"' in header:
        pos_m = re.search(r'position = Vector2\(\s*([-\d\.]+),\s*([-\d\.]+)\s*\)', n)
        pos_str = pos_m.group(0) if pos_m else 'no pos'
        print(f"{header} | {pos_str}")
