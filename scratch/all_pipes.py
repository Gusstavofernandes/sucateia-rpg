import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Primeiro descobre qual ExtResource é pipe.png
pipe_res_ids = []
for m in re.finditer(r'\[ext_resource\s+type="Texture2D"\s+path="res://assets/generated/props/pipe\.png"\s+id="([^"]+)"\]', text):
    pipe_res_ids.append(m.group(1))

# Também se houver outros pipes em assets/
for m in re.finditer(r'\[ext_resource\s+type="Texture2D"\s+path="([^"]*pipe[^"]*)"\s+id="([^"]+)"\]', text):
    pipe_res_ids.append(m.group(2))
    print(f"Resource {m.group(2)}: {m.group(1)}")

pipe_res_ids = list(set(pipe_res_ids))
print("Pipe resource IDs:", pipe_res_ids)

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

print("\n--- ALL PIPE SPRITES IN SCENE ---")
for path, data in nodes.items():
    tex = data['props'].get('texture', '')
    for pid in pipe_res_ids:
        if f'ExtResource("{pid}")' in tex or f'ExtResource(\'{pid}\')' in tex:
            gx, gy = get_global_pos(path)
            rot = data['props'].get('rotation', '0')
            sc = data['props'].get('scale', '1,1')
            if 1000 <= gx <= 2500 and 1000 <= gy <= 2000:
                print(f"PIPE: {path} | pos=({gx:.1f}, {gy:.1f}) | rot={rot} | scale={sc}")
