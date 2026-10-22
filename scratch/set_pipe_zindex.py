import re

for path in [r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn', r'c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    for group in ['TuboParedeOesteModular', 'CanoOesteManifoldBomba', 'CanoBombaCaldeiraModular', 'CanoLesteModular', 'FiacaoIndustrialCabos']:
        target = f'[node name="{group}" type="Node2D" parent="RedeIndustrialMaquinas"]\ny_sort_enabled = true'
        repl = f'[node name="{group}" type="Node2D" parent="RedeIndustrialMaquinas"]\nz_index = -1\ny_sort_enabled = true'
        if target in c:
            c = c.replace(target, repl)
            print(f'Atualizado {group} em {path}')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
