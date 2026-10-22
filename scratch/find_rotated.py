import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Map ext_resources
ext_map = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_map[m.group(3)] = m.group(2)

# Find all nodes
nodes = re.findall(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)', text)

print(f"Total nodes found: {len(nodes)}")

for name, ntype, parent, props in nodes:
    has_rot = 'rotation' in props
    has_pier = 'wood_pier' in props or any(k in props for k in ext_map if 'wood_pier' in ext_map[k])
    
    pos_m = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
    rot_m = re.search(r'rotation\s*=\s*([-\d.]+)', props)
    tex_m = re.search(r'texture\s*=\s*ExtResource\("([^"]+)"\)', props)
    
    tex_path = ext_map.get(tex_m.group(1), '') if tex_m else ''
    
    if has_pier or (has_rot and rot_m and abs(float(rot_m.group(1))) > 0.05):
        print(f"Node: {parent}/{name} | type={ntype} | pos={pos_m.group(1) if pos_m else None} | rot={rot_m.group(1) if rot_m else 0} | tex={tex_path}")
