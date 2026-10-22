import re

with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

matches = re.findall(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)', text)

print("Collisions / blockers near x: 3500..3850, y: 450..700:")
for name, ntype, parent, props in matches:
    if 'Collision' in ntype or 'StaticBody' in ntype or 'Col' in name:
        pos = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
        if pos:
            coords = [float(c.strip()) for c in pos.group(1).split(',')]
            if 3400 <= coords[0] <= 3900 and 400 <= coords[1] <= 750:
                print(f"Parent: {parent} | Node: {name} ({ntype}) | pos: {coords}")
