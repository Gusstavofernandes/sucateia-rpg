import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

ext_map = {}
for m in re.finditer(r'\[ext_resource\s+type="([^"]+)"\s+path="([^"]+)"\s+id="([^"]+)"\]', text):
    ext_map[m.group(3)] = m.group(2)

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

print("=== NODES IN AREA X: 1550..1850, Y: 1400..1650 ===")
for path, data in nodes.items():
    gx, gy = get_global_pos(path)
    if 1550 <= gx <= 1850 and 1400 <= gy <= 1650:
        tex_str = data['props'].get('texture', '')
        res = ''
        m_ext = re.search(r'ExtResource\("([^"]+)"\)', tex_str)
        if m_ext:
            res = ext_map.get(m_ext.group(1), m_ext.group(1))
        rot = data['props'].get('rotation', '0')
        sc = data['props'].get('scale', '1,1')
        print(f"{path} | pos=({gx:.1f}, {gy:.1f}) | rot={rot} | sc={sc} | res={res}")
