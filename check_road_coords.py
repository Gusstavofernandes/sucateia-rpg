with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# find nodes around x=800-1300, y=300-600
nodes = re.split(r'\n\[node ', text)
for n in nodes:
    pos_m = re.search(r'position = Vector2\(\s*([-\d\.]+),\s*([-\d\.]+)\s*\)', n)
    if pos_m:
        x, y = float(pos_m.group(1)), float(pos_m.group(2))
        if 800 <= x <= 1300 and 300 <= y <= 600:
            header = n.split('\n')[0]
            print(f"({x:6.1f}, {y:6.1f}) | {header}")
