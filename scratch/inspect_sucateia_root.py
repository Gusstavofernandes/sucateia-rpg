with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
root_nodes = re.findall(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?\s+parent="\."[^\]]*\]\s*([^\[]*)', text)
print(f"Top-level districts and nodes in sucateia.tscn ({len(root_nodes)}):")
for name, ntype, props in root_nodes:
    pos = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
    z = re.search(r'z_index\s*=\s*([-\d]+)', props)
    print(f"- {name} ({ntype}) | pos={pos.group(1) if pos else '0,0'} | z={z.group(1) if z else 0}")
