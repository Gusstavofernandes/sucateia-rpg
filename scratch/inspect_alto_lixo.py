import os

scene_path = r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn'
with open(scene_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_alto = False
alto_nodes = []
for line in lines:
    line_s = line.strip()
    if 'name="AltoLixoDistrict"' in line_s:
        in_alto = True
        alto_nodes.append(line_s)
        continue
    if in_alto:
        if line_s.startswith('[node name=') and 'parent="."' in line_s:
            # Reached next top level node
            break
        if line_s.startswith('[node name='):
            alto_nodes.append(line_s)

print(f"Nodes under AltoLixoDistrict ({len(alto_nodes)}):")
for n in alto_nodes[:30]:
    print("  ", n)
if len(alto_nodes) > 30:
    print(f"  ... and {len(alto_nodes) - 30} more")
