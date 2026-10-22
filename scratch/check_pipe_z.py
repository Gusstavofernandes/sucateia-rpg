with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)', text)

for name, ntype, parent, props in matches:
    if any(k in name.lower() for k in ['tubo', 'pipe', 'duto']):
        z = re.search(r'z_index\s*=\s*([-\d]+)', props)
        pos = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
        print(f"Node: {name} | pos: {pos.group(1) if pos else None} | z: {z.group(1) if z else 0}")
