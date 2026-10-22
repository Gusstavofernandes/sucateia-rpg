import os
import re

with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'text = "([^"]+)"', text)
for m in matches:
    if any(k in m for k in ['SUCATEIA', 'FERRUGEM', 'Lixo', 'Mercado', 'Distrito', '—', '–']):
        print(m)
