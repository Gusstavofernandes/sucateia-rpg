import re

with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

ext_map = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_map[m.group(3)] = m.group(2)

matches = re.findall(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)', text)
print(f"Total nodes in fundo_ferro_master: {len(matches)}")

for name, ntype, parent, props in matches:
    if any(k in name.lower() or (parent and k in parent.lower()) or k in props.lower() for k in ['passarela', 'ponte', 'bridge']):
        pos = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
        scale = re.search(r'scale\s*=\s*Vector2\(([^)]+)\)', props)
        rot = re.search(r'rotation\s*=\s*([-\d.]+)', props)
        tex_m = re.search(r'texture\s*=\s*ExtResource\("([^"]+)"\)', props)
        tex = ext_map.get(tex_m.group(1), '') if tex_m else ''
        print(f"Parent: {parent} | Node: {name} ({ntype}) | pos: {pos.group(1) if pos else None} | rot: {rot.group(1) if rot else 0} | tex: {tex}")
