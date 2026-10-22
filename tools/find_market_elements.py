import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Procurar nós perto de x entre 900 e 1300, y entre -600 e 200
pattern = re.compile(r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]+)"[^\]]*\](?:\s*position = Vector2\(([^,]+),\s*([^)]+)\))?', re.DOTALL)

for m in pattern.finditer(text):
    name = m.group(1)
    ntype = m.group(2)
    parent = m.group(3)
    # Ler as próximas linhas para pegar position e texture se tiver
    start = m.start()
    chunk = text[start:start+400]
    pos_m = re.search(r'position = Vector2\(([^,]+),\s*([^)]+)\)', chunk)
    tex_m = re.search(r'texture = ExtResource\("([^"]+)"\)', chunk)
    if pos_m:
        x, y = float(pos_m.group(1)), float(pos_m.group(2))
        if 800 <= x <= 1400 and -500 <= y <= 200:
            print(f"Parent: {parent} | Node: {name} ({ntype}) at ({x}, {y}) | tex: {tex_m.group(1) if tex_m else 'none'}")
