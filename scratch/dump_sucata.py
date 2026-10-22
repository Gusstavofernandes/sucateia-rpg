import re

with open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\[node name="EntulhoESucataNoChao".*?(?=\[node name="EstacaoBombeamento")', text, re.DOTALL)
if m:
    print(m.group(0))
