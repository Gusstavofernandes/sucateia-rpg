import re

with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

print("=== LIMITES DE CÂMERA ===")
for m in re.finditer(r'limit_(left|right|top|bottom)\s*=\s*([^\n]+)', text):
    print(m.group(0))

print("\n=== COLISÕES E LIMITES DE CENÁRIO ===")
nodes = text.split('[node name=')
for n in nodes[1:]:
    header = n.split(']')[0]
    body = n[len(header)+1:].split('\n[')[0]
    name_m = re.match(r'"([^"]+)"\s+type="([^"]+)"(?:\s+parent="([^"]*)")?', header)
    if name_m:
        name = name_m.group(1)
        ntype = name_m.group(2)
        parent = name_m.group(3) or ""
        if any(k in name.lower() for k in ['colis', 'limit', 'borda', 'parede', 'wall', 'muralha']):
            pos_m = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', body)
            shape_m = re.search(r'shape\s*=\s*([^\n]+)', body)
            pos_str = pos_m.group(1) if pos_m else "None"
            shape_str = shape_m.group(1) if shape_m else "None"
            print(f"Node: {name} (parent={parent}) pos={pos_str} shape={shape_str}")
