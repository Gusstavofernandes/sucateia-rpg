import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

ext_map = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_map[m.group(3)] = m.group(2)

matches = re.findall(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)', text)

print("Nodes with Polygon2D, Water, Soil, Floor, or Background:")
for name, ntype, parent, props in matches:
    if any(k in name.lower() or k in ntype.lower() for k in ['polygon2d', 'water', 'ocean', 'mar', 'soil', 'floor', 'terra', 'chao']):
        col = re.search(r'color\s*=\s*Color\(([^)]+)\)', props)
        z = re.search(r'z_index\s*=\s*([-\d]+)', props)
        print(f"Parent: {parent} | Node: {name} ({ntype}) | z: {z.group(1) if z else 0} | col: {col.group(1) if col else None}")
