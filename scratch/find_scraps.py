import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
nodes = {}
current_node_name = None

for line in lines:
    if line.startswith('[node name='):
        m = re.search(r'\[node name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?', line)
        if m:
            name, ntype, parent = m.group(1), m.group(2), m.group(3)
            full_path = f"{parent}/{name}" if parent else name
            current_node_name = full_path
            nodes[full_path] = {'name': name, 'type': ntype, 'parent': parent, 'props': {}, 'raw': line}
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

for path, data in nodes.items():
    tex = data['props'].get('texture', '')
    if 'scrap.png' in tex or 'walkway.png' in tex:
        gx, gy = get_global_pos(path)
        print(f"{path} -> pos=({gx:.1f}, {gy:.1f}) | tex={tex}")
