import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_node = None
current_type = None
current_parent = None
current_props = {}

nodes = []

for line in lines:
    m = re.match(r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]+)"', line)
    if not m:
        m = re.match(r'\[node name="([^"]+)" type="([^"]+)"', line)
        if m:
            current_node = m.group(1)
            current_type = m.group(2)
            current_parent = ""
            current_props = {}
            nodes.append((current_node, current_type, current_parent, current_props))
            continue
    if m:
        current_node = m.group(1)
        current_type = m.group(2)
        current_parent = m.group(3)
        current_props = {}
        nodes.append((current_node, current_type, current_parent, current_props))
        continue
    
    if current_node:
        pm = re.match(r'position = Vector2\(([^,]+),\s*([^)]+)\)', line)
        if pm:
            current_props['pos'] = (float(pm.group(1)), float(pm.group(2)))
        tm = re.match(r'texture = ExtResource\("([^"]+)"\)', line)
        if tm:
            current_props['tex'] = tm.group(1)
        sm = re.match(r'scale = Vector2\(([^,]+),\s*([^)]+)\)', line)
        if sm:
            current_props['scale'] = (float(sm.group(1)), float(sm.group(2)))

print(f"Total parsed nodes: {len(nodes)}")

# Find nodes around Alto-Lixo southwest: x around -400..400, y around -100..400
for n, t, p, props in nodes:
    pos = props.get('pos')
    if pos:
        x, y = pos
        if -500 <= x <= 500 and -100 <= y <= 500:
            print(f"{p}/{n} ({t}) pos={pos} tex={props.get('tex')}")
