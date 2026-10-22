import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    lines = f.readlines()

nodes = {} # path -> {'type': t, 'pos': (x,y), 'parent': p, 'tex': tex, 'line': idx}
last_path = None

for idx, line in enumerate(lines):
    m = re.match(r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]+)"', line)
    if not m:
        m = re.match(r'\[node name="([^"]+)" type="([^"]+)"', line)
        if m:
            nname = m.group(1)
            ntype = m.group(2)
            nodes[nname] = {'type': ntype, 'pos': (0.0, 0.0), 'parent': None, 'line': idx}
            last_path = nname
            continue
    if m:
        nname = m.group(1)
        ntype = m.group(2)
        nparent = m.group(3)
        path = nparent + "/" + nname
        nodes[path] = {'type': ntype, 'pos': (0.0, 0.0), 'parent': nparent, 'line': idx}
        last_path = path
        continue
    
    if last_path:
        pm = re.match(r'position = Vector2\(([^,]+),\s*([^)]+)\)', line)
        if pm:
            nodes[last_path]['pos'] = (float(pm.group(1)), float(pm.group(2)))
        tm = re.match(r'texture = ExtResource\("([^"]+)"\)', line)
        if tm:
            nodes[last_path]['tex'] = tm.group(1)

def get_global_pos(path):
    cur = path
    gx, gy = 0.0, 0.0
    while cur:
        info = nodes.get(cur)
        if not info:
            break
        x, y = info['pos']
        gx += x
        gy += y
        cur = info['parent']
    return gx, gy

print("Searching nodes with global_y between -300 and 600, global_x between -600 and 600...")
results = []
for p, data in nodes.items():
    gx, gy = get_global_pos(p)
    if -800 <= gx <= 400 and -200 <= gy <= 500:
        results.append((p, data['type'], gx, gy, data.get('tex', '')))

# Sort by gy
results.sort(key=lambda item: item[3])
for r in results:
    print(f"GPos=({r[2]:.1f}, {r[3]:.1f}) {r[0]} ({r[1]}) tex={r[4]}")
