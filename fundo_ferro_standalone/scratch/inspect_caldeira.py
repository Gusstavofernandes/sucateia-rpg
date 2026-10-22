import re
from PIL import Image

tscn_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn'
with open(tscn_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Procura CaldeiraVaporLeste e seus filhos
m = re.search(r'(\[node name="CaldeiraVaporLeste"[\s\S]*?)(?=\n\[node name="[A-Z]|\Z)', text)
if m:
    print("=== NÓ CALDEIRA VAPOR LESTE ===")
    print(m.group(1)[:1500])

with open(tscn_path, 'r', encoding='utf-8') as f:
    text = f.read()

for m in re.finditer(r'\[node name="CanoOeste[^"]*"[^\]]*\][\s\S]*?(?=\n\[node|\Z)', text):
    print(m.group(0).strip())
    print("---")




