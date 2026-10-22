import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Map ext_resources
ext_map = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_map[m.group(3)] = m.group(2)

# Find all nodes with their properties
node_pattern = re.compile(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)')

matches = node_pattern.findall(text)
print(f"Total nodes: {len(matches)}")

for name, ntype, parent, props in matches:
    pos_m = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
    if pos_m:
        coords = [float(c.strip()) for c in pos_m.group(1).split(',')]
        x, y = coords[0], coords[1]
        # In screenshot, the player is at cabos junction or near it
        # Let's inspect x in [600, 900], y in [-650, -450]
        if 650 <= x <= 850 and -650 <= y <= -450:
            rot_m = re.search(r'rotation\s*=\s*([-\d.]+)', props)
            tex_m = re.search(r'texture\s*=\s*ExtResource\("([^"]+)"\)', props)
            scale_m = re.search(r'scale\s*=\s*Vector2\(([^)]+)\)', props)
            z_m = re.search(r'z_index\s*=\s*([-\d]+)', props)
            tex = ext_map.get(tex_m.group(1), '') if tex_m else ''
            print(f"PATH: {parent}/{name} | type={ntype} | pos=({x}, {y}) | rot={rot_m.group(1) if rot_m else 0} | z={z_m.group(1) if z_m else 0} | tex={tex}")
