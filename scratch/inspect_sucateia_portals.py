import os
import re

with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's check RegionPortals in sucateia.tscn
pattern = re.compile(r'\[node name="([^"]+)"(?:\s+type="([^"]+)")?(?:\s+parent="([^"]+)")?[^\]]*\](?:\s+position = Vector2\(([^)]+)\))?', re.MULTILINE)
matches = pattern.findall(text)

for name, ntype, parent, pos in matches:
    if 'portal' in parent.lower() or 'regionportals' in parent.lower():
        print(f"Portal: {name:<25} in {parent:<25} at pos={pos}")
