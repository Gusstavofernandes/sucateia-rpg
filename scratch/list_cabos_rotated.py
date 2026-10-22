import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

ext_map = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_map[m.group(3)] = m.group(2)

node_pattern = re.compile(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)')
matches = node_pattern.findall(text)

parents = set()
for name, ntype, parent, props in matches:
    if parent and 'Cabos' in parent:
        parents.add(parent)
print("Cabos parent groups:", sorted(list(parents)))

for name, ntype, parent, props in matches:
    if parent and 'Cabos' in parent:
        pos_m = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
        rot_m = re.search(r'rotation\s*=\s*([-\d.]+)', props)
        if rot_m and float(rot_m.group(1)) != 0:
            tex_m = re.search(r'texture\s*=\s*ExtResource\("([^"]+)"\)', props)
            tex = ext_map.get(tex_m.group(1), '') if tex_m else ''
            print(f"ROTATED in {parent}: {name} ({ntype}), pos={pos_m.group(1) if pos_m else None}, rot={rot_m.group(1)}, tex={tex}")
