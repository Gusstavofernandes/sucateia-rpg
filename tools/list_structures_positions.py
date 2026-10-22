import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Procurar nós em Structures e suas posições
pattern = re.compile(r'\[node name="([^"]+)" type="Node2D" parent="Structures"[^\]]*\](?:\s*position = Vector2\(([^,]+),\s*([^)]+)\))?')
matches = pattern.findall(text)
for name, x, y in matches:
    print(f"Structure: {name} at ({x}, {y})")
