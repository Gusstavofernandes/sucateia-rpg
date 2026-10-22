with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    content = f.read()

import re
node_blocks = re.split(r'\n(?=\[node )', content)

for b in node_blocks:
    if '@Node2D@102' in b or '@Node2D@105' in b:
        print("------------------------------------------")
        print(b.strip())
