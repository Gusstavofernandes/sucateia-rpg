import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

nodes = {}
for m in re.finditer(r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]+)"\](.*?)(?=\n\[node|\Z)', text, re.DOTALL):
    name, ntype, parent, body = m.group(1), m.group(2), m.group(3), m.group(4)
    pos_m = re.search(r'position = Vector2\(([^,]+),\s*([^)]+)\)', body)
    tex_m = re.search(r'texture = ExtResource\("([^"]+)"\)', body)
    pos = (float(pos_m.group(1)), float(pos_m.group(2))) if pos_m else (0.0, 0.0)
    full_path = name if parent == "." else parent + "/" + name
    nodes[full_path] = {'type': ntype, 'pos': pos, 'parent': parent, 'tex': tex_m.group(1) if tex_m else ''}

def get_gpos(path):
    cur = path
    gx, gy = 0.0, 0.0
    while cur and cur != ".":
        if cur not in nodes:
            break
        x, y = nodes[cur]['pos']
        gx += x
        gy += y
        cur = nodes[cur]['parent']
    return gx, gy

print("Nodes around x in [0, 400], y in [300, 800]:")
found = []
for p, d in nodes.items():
    gx, gy = get_gpos(p)
    if -100 <= gx <= 400 and 300 <= gy <= 800:
        found.append((gx, gy, p, d['type'], d['tex']))

found.sort(key=lambda item: item[1])
for f in found:
    print(f"  ({f[0]:.1f}, {f[1]:.1f}) {f[2]} ({f[3]}) tex={f[4]}")
