with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

m = re.search(r'\[node name="house_3" type="Node2D" parent="Structures"[^\n]*\n.*?(?=\n\[node name="[^"]+" type="Node2D" parent="Structures"|\Z)', text, re.DOTALL)
if m:
    print(m.group(0)[:1500])
