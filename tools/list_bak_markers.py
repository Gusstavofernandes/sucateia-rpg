import re

with open('maps/sucateia/sucateia.tscn.bak', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'\[node name="([^"]+)" type="Marker2D" parent="RouteMarkers"[^\]]*\](?:\s*position = Vector2\(([^,]+),\s*([^)]+)\))?')
matches = pattern.findall(text)
for name, x, y in matches:
    print(f"Marker: {name} at ({x}, {y})")
