import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Procurar nós em Structures entre y=500 e y=700
pattern = re.compile(r'\[node name="([^"]+)" type="Node2D" parent="Structures"[^\]]*\]\s*position = Vector2\(([^,]+),\s*([^)]+)\)', re.DOTALL)
for m in pattern.finditer(text):
    name = m.group(1)
    x = float(m.group(2))
    y = float(m.group(3))
    if 400 <= y <= 800:
        print(f"Node: {name} at ({x}, {y})")
