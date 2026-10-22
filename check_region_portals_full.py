with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

m = re.search(r'\[node name="RegionPortals"[^\n]*\n.*?(?=\n\[node name="[^"]+" type="[^"]+" parent="\."|\Z)', text, re.DOTALL)
if m:
    print(m.group(0)[:1500])
