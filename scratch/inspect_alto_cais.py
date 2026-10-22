import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

ext_map = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_map[m.group(3)] = m.group(2)

matches = re.findall(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)', text)

print("Nodes under AltoLixoCais or related to west coast:")
for name, ntype, parent, props in matches:
    if parent and ('AltoLixoCais' in parent or 'AltoLixo' in parent):
        pos = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
        tex_m = re.search(r'texture\s*=\s*ExtResource\("([^"]+)"\)', props)
        tex = ext_map.get(tex_m.group(1), '') if tex_m else ''
        if any(k in name.lower() or k in parent.lower() for k in ['cais', 'pier', 'wall', 'water', 'land', 'paving', 'barrier', 'coast']):
            print(f"{parent}/{name} ({ntype}): pos={pos.group(1) if pos else None} | tex={tex}")
