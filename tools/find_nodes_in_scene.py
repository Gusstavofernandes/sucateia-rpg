import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Procurar nós no MarketDistrict ou com Market/Restos
print("Procurando nós relevantes...")
for m in re.finditer(r'\[node name="([^"]+)" [^\]]*\]\s*(?:position = Vector2\(([^,]+),\s*([^)]+)\))?', text):
    name = m.group(1)
    pos = (m.group(2), m.group(3))
    if any(k in name.lower() for k in ['bench', 'bancada', 'table', 'market', 'portal', 'gate', 'muralha', 'wall', 'pinnacle', 'chain']):
        print(f"Node: {name} pos: {pos}")
