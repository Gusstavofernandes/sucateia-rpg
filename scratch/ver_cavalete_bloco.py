with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'\[node name="CavaleteElevadoCanal"[\s\S]*?(?=\[node name="Player")', text)
if m:
    print(m.group(0))
