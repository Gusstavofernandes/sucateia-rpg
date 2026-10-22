import re

with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

matches = re.findall(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)', text)

pipe_nodes = []
for name, ntype, parent, props in matches:
    if 'tubo' in name.lower() or 'pipe' in name.lower() or 'duto' in name.lower():
        if 'Col' not in name:
            z = re.search(r'z_index\s*=\s*([-\d]+)', props)
            pos = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
            pipe_nodes.append((parent, name, pos.group(1) if pos else None, z.group(1) if z else 0))

print(f"Total pipe visual nodes: {len(pipe_nodes)}")
for p in pipe_nodes[:15]:
    print(p)
