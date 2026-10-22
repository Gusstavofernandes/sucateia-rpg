import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Parse all collision shapes and their positions
nodes = {}
for m in re.finditer(r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]+)"\](.*?)(?=\n\[node|\Z)', text, re.DOTALL):
    name, ntype, parent, body = m.group(1), m.group(2), m.group(3), m.group(4)
    pos_m = re.search(r'position = Vector2\(([^,]+),\s*([^)]+)\)', body)
    pos = (float(pos_m.group(1)), float(pos_m.group(2))) if pos_m else (0.0, 0.0)
    nodes[parent + "/" + name] = {'type': ntype, 'pos': pos, 'parent': parent, 'body': body}

def get_gpos(path):
    cur = path
    gx, gy = 0.0, 0.0
    while cur in nodes:
        x, y = nodes[cur]['pos']
        gx += x
        gy += y
        cur = nodes[cur]['parent']
    return gx, gy

print("Checking collisions in corridor x in [-100, 250], y in [150, 360]...")
for path, data in nodes.items():
    if 'Collision' in data['type'] or 'Body' in data['type']:
        gx, gy = get_gpos(path)
        if -100 <= gx <= 250 and 150 <= gy <= 360:
            print(f"  {path} ({data['type']}) at ({gx}, {gy})")
