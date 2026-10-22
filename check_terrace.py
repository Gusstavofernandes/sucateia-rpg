with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

m = re.search(r'\[node name="TerraceFloor"[^\n]*\n([^\n]+\n){1,25}', text)
if m:
    print(m.group(0))
