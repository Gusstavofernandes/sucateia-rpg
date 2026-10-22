with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
in_rede = False
for i, l in enumerate(lines):
    if 'name="RedeFerroviariaMina"' in l:
        in_rede = True
    elif in_rede and l.startswith('[node name="') and 'parent="RedeFerroviariaMina' not in l and not l.startswith('[node name="RedeFerroviariaMina"'):
        in_rede = False
    elif in_rede:
        print(f"{i+1}: {l}")
