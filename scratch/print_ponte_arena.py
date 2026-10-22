with open('scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

for label in ['PonteServicoArena', 'PassarelaTravessiaCano_4']:
    start = text.find(f'[node name="{label}"')
    if start != -1:
        # print up to 1500 chars
        print(f"=== {label} ===")
        print(text[start:start+1800])
