import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect GoblinIndustrialQuay nodes
quay_nodes = []
for m in re.finditer(r'\[node name="([^"]+)" type="([^"]+)" parent="GoblinIndustrialQuay"\](.*?)(?=\n\[node|\Z)', text, re.DOTALL):
    name, ntype, body = m.group(1), m.group(2), m.group(3)
    pos_m = re.search(r'position = Vector2\(([^,]+),\s*([^)]+)\)', body)
    tex_m = re.search(r'texture = ExtResource\("([^"]+)"\)', body)
    if pos_m:
        x, y = float(pos_m.group(1)), float(pos_m.group(2))
        quay_nodes.append((name, ntype, x, y, tex_m.group(1) if tex_m else None))

quay_nodes.sort(key=lambda item: item[3])
print(f"GoblinIndustrialQuay total nodes: {len(quay_nodes)}")
print("Northernmost nodes in GoblinIndustrialQuay:")
for n in quay_nodes[:25]:
    print(f"  pos=({n[2]}, {n[3]}) {n[0]} ({n[1]}) tex={n[4]}")
