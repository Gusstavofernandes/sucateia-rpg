import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

ext_map = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_map[m.group(3)] = m.group(2)

node_pattern = re.compile(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)')
matches = node_pattern.findall(text)

print("--- Nodes under CabosDistrict/ElevatedDecks ---")
for name, ntype, parent, props in matches:
    if parent == "CabosDistrict/ElevatedDecks" or parent.startswith("CabosDistrict/ElevatedDecks/"):
        pos_m = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
        rot_m = re.search(r'rotation\s*=\s*([-\d.]+)', props)
        tex_m = re.search(r'texture\s*=\s*ExtResource\("([^"]+)"\)', props)
        tex = ext_map.get(tex_m.group(1), '') if tex_m else ''
        print(f"{name} ({ntype}): pos={pos_m.group(1) if pos_m else None}, rot={rot_m.group(1) if rot_m else 0}, tex={tex}")
