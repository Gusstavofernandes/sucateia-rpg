import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

ext_map = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_map[m.group(3)] = m.group(2)

matches = re.findall(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)', text)

print("Nodes around x: -1400..-600, y: -200..400:")
for name, ntype, parent, props in matches:
    pos = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
    if pos:
        coords = [float(c.strip()) for c in pos.group(1).split(',')]
        if -1400 <= coords[0] <= -600 and -200 <= coords[1] <= 450:
            tex_m = re.search(r'texture\s*=\s*ExtResource\("([^"]+)"\)', props)
            tex = ext_map.get(tex_m.group(1), '') if tex_m else ''
            print(f"{parent}/{name} ({ntype}): pos={coords} | tex={tex}")
