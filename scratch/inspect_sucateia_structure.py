import os

scene_path = r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn'
with open(scene_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines in sucateia.tscn: {len(lines)}")
root_children = []
for line in lines:
    line_s = line.strip()
    if line_s.startswith('[node name=') and 'parent="."' in line_s:
        root_children.append(line_s)

print(f"Direct children of Sucateia root ({len(root_children)}):")
for c in root_children:
    print("  ", c)
