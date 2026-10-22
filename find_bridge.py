with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find nodes with texture containing 'bridge' or 'suspension' or 'walkway' or 'ponte'
nodes = re.split(r'\n\[node ', text)
for n in nodes:
    if any(k in n.lower() for k in ['bridge', 'suspension', 'ponte']):
        header = n.split('\n')[0]
        pos = re.search(r'position = Vector2\([^\)]+\)', n)
        tex = re.search(r'texture = [^\n]+', n)
        pos_str = pos.group(0) if pos else 'no pos'
        tex_str = tex.group(0) if tex else 'no tex'
        print(f"[{header}] | {pos_str} | {tex_str}")
