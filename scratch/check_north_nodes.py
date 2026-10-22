import re

with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Find any position with y < -1400
matches = re.findall(r'position = Vector2\(([^,]+),\s*([^)]+)\)', text)
north_nodes = []
for x, y in matches:
    fx, fy = float(x), float(y)
    if fy < -1400:
        north_nodes.append((fx, fy))

print(f"Nodes with Y < -1400 in sucateia.tscn: {len(north_nodes)}")
for n in north_nodes[:20]:
    print(" ", n)
