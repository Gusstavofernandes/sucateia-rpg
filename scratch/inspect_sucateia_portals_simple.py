with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    lines = f.readlines()

in_portals = False
for i, line in enumerate(lines):
    if 'name="RegionPortals"' in line:
        in_portals = True
        print(line.strip())
        continue
    if in_portals:
        if line.startswith('[node name=') and 'parent="."' in line:
            break
        if line.startswith('[node name=') or 'destination' in line or 'position' in line or 'text' in line:
            print("  ", line.strip())
