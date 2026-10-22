import re

with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

matches = re.findall(r'\[node\s+name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\]\s*([^\[]*)', text)

print("Nodes related to stalls, bridges, or around y: 400..800:")
for name, ntype, parent, props in matches:
    if any(k in name.lower() or (parent and k in parent.lower()) for k in ['barraca', 'feira', 'ponte', 'passarela', 'apostas']):
        pos = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', props)
        print(f"{parent}/{name}: pos={pos.group(1) if pos else None}")
