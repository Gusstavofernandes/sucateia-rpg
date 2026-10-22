import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
nodes = {}
current_node_name = None
current_node_parent = None
current_node_type = None
current_props = {}

for line in lines:
    if line.startswith('[node name='):
        m = re.search(r'\[node name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?', line)
        if m:
            name, ntype, parent = m.group(1), m.group(2), m.group(3)
            if parent:
                full_path = f"{parent}/{name}"
            else:
                full_path = name
            current_node_name = full_path
            nodes[full_path] = {'name': name, 'type': ntype, 'parent': parent, 'props': {}, 'raw_node_line': line}
    elif current_node_name and line.startswith('['):
        current_node_name = None
    elif current_node_name and '=' in line:
        k, v = line.split('=', 1)
        nodes[current_node_name]['props'][k.strip()] = v.strip()

def get_global_pos(path):
    parts = path.split('/')
    cur = ''
    total_x, total_y = 0.0, 0.0
    for p in parts:
        cur = f"{cur}/{p}" if cur else p
        if cur in nodes:
            pos_str = nodes[cur]['props'].get('position', None)
            if pos_str:
                m = re.search(r'Vector2\(([^)]+)\)', pos_str)
                if m:
                    coords = [float(c.strip()) for c in m.group(1).split(',')]
                    total_x += coords[0]
                    total_y += coords[1]
    return total_x, total_y

print("=== PIPES IN CHANNEL SOUTH REGION ===")
found = []
for path, data in nodes.items():
    tex = data['props'].get('texture', '')
    if '5_fo6ws' in tex or 'pipe' in tex.lower() or 'pipe' in path.lower():
        gx, gy = get_global_pos(path)
        if 1300 <= gx <= 2100 and 1200 <= gy <= 1900:
            rot = data['props'].get('rotation', '0')
            sc = data['props'].get('scale', '1,1')
            found.append((path, gx, gy, rot, sc, tex, data['raw_node_line']))
            print(f"{path} -> GLOBAL: ({gx:.1f}, {gy:.1f}) | rot: {rot} | scale: {sc} | tex: {tex}")

print(f"Total found: {len(found)}")
