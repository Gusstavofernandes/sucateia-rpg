import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'\[node name="([^"]+)" type="[^"]+" parent="MarketDistrict[^"]*"[^\]]*\](?:\s*position = Vector2\(([^,]+),\s*([^)]+)\))?')
matches = pattern.findall(text)
for name, x, y in matches:
    print(f"MarketDistrict node: {name} at ({x}, {y})")
