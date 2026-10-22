import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Let's extract all ext_resources to see textures
ext_resources = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_resources[m.group(3)] = m.group(2)

nodes = re.findall(r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]+)"[^\]]*\]\s*([^\[]*)', text)
cabos_nodes = [n for n in nodes if n[2].startswith('CabosDistrict')]
print(f'Total cabos nodes: {len(cabos_nodes)}')

for name, ntype, parent, props in cabos_nodes:
    if 'position' in props:
        pos_match = re.search(r'position = Vector2\(([^)]+)\)', props)
        rot_match = re.search(r'rotation = ([-\d.]+)', props)
        tex_match = re.search(r'texture = ExtResource\("([^"]+)"\)', props)
        if pos_match:
            coords = [float(x.strip()) for x in pos_match.group(1).split(',')]
            # Let's filter around 600..900, -650..-350
            if 600 <= coords[0] <= 900 and -650 <= coords[1] <= -350:
                tex_id = tex_match.group(1) if tex_match else None
                tex_path = ext_resources.get(tex_id, 'None')
                rot = rot_match.group(1) if rot_match else '0'
                print(f'{parent}/{name} ({ntype}): pos={coords}, rot={rot}, tex={tex_path}')
