import re

with open(r'maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# AncoragemDaCarga ports:
# position = (4060, -10)
# chain_e_upper = (4060 + 61.26, -10 - 65.88) = (4121.26, -75.88)
# chain_e_lower = (4060 + 29.77, -10 - 45.93) = (4089.77, -55.93)

for block in text.split('[node '):
    if not block.strip():
        continue
    header = block.split('\n')[0]
    if 'Line2D' in header:
        m = re.search(r'name="([^"]+)"', header)
        p = re.search(r'parent="([^"]+)"', header)
        name = m.group(1) if m else '?'
        parent = p.group(1) if p else '?'
        if '4121' in block or '4089' in block or '4060' in block or '4120' in block:
            print(f'Node: {name} in {parent}')
            for line in block.split('\n'):
                if 'points =' in line:
                    print('   ' + line[:140])
