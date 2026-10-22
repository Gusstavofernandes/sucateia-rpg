import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Vamos procurar todas as casas ou construções ou sprites com nomes interessantes
for block in text.split('\n['):
    if not block.startswith('node'):
        continue
    header = block.split('\n')[0]
    if any(k in block.lower() for k in ['house', 'cabana', 'pesca', 'fisherman', 'workshop', 'coastal', 'pier']):
        pos = re.search(r'position = Vector2\(([^)]+)\)', block)
        tex = re.search(r'texture = ([^\n]+)', block)
        if pos:
            print(f"{header} -> pos: {pos.group(1)} | tex: {tex.group(1) if tex else 'none'}")
