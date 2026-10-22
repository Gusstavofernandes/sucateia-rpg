import os
import re

for name in ['alto.tscn', 'fundo.tscn', 'forjas.tscn', 'coroa.tscn', 'docas.tscn']:
    p = os.path.join(r'c:\Users\Usuario\Documents\jogo\maps\ferrugem_baixa', name)
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            text = f.read()
        texts = re.findall(r'text = "([^"]+)"', text)
        print(f"=== {name} ===")
        for t in texts:
            if 'FERRUGEM' in t or '—' in t or '–' in t:
                print("  ", t)
