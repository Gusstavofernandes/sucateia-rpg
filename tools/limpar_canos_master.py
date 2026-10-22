import re

FILES = [
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn",
    r"c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn"
]

for p in FILES:
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()

    # Remove CanoLeste_8 e CanoLeste_9
    pattern = r'\[node name="CanoLesteSombra_8"[\s\S]*?\[node name="CanoLeste_9"[\s\S]*?texture = ExtResource\("50_cano_longo"\)\n'
    c = re.sub(pattern, '', c)

    with open(p, "w", encoding="utf-8") as f:
        f.write(c)
    print("Canos soltos removidos de:", p)
