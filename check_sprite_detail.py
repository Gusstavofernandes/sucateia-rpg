with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for name in ['house_3', '@Node2D@72']:
    m = re.search(r'\[node name="[^"]+" type="Sprite2D" parent="Structures/' + re.escape(name) + r'"[^\n]*\n([^\n]+\n){1,10}', text)
    if m:
        print(f"=== {name} sprite ===")
        print(m.group(0))
