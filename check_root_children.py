with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for m in re.finditer(r'\[node name="([^"]+)" type="[^"]+" parent="\."[^\n]*\]', text):
    print(m.group(1))
