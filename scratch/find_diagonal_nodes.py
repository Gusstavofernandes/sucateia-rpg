import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

ext_map = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_map[m.group(3)] = m.group(2)

node_pattern = re.compile(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)')
matches = node_pattern.findall(text)

print(f"Total nodes: {len(matches)}")

# Let's search for nodes with rotation between 0.3 and 1.2 or -1.2 and -0.3
for name, ntype, parent, props in matches:
    rot_m = re.search(r'rotation\s*=\s*([-\d.]+)', props)
    if rot_m:
        rot = float(rot_m.group(1))
        # 30 deg is 0.52 rad, 45 deg is 0.78 rad
        if (0.3 <= abs(rot) <= 1.2) or (2.0 <= abs(rot) <= 2.8):
            pos_m = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
            tex_m = re.search(r'texture\s*=\s*ExtResource\("([^"]+)"\)', props)
            tex = ext_map.get(tex_m.group(1), '') if tex_m else ''
            if 'walkway' in tex or 'deck' in tex or 'stairs' in tex or 'bridge' in tex or 'platform' in tex or not tex:
                print(f"Parent: {parent} | Node: {name} | type={ntype} | rot={rot} | pos={pos_m.group(1) if pos_m else None} | tex={tex}")
