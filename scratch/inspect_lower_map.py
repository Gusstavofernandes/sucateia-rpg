import os

with open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_node = ""
current_parent = ""
for line in lines:
    line_str = line.strip()
    if line_str.startswith('[node name='):
        # parse name and parent
        # e.g. [node name="BarracaApostas_Principal" type="Node2D" parent="FeiraClandestinaFundoFerro"]
        parts = line_str[6:-1].split()
        d = {}
        for p in parts:
            if '=' in p:
                k, v = p.split('=', 1)
                d[k] = v.strip('"')
        current_node = d.get('name', '')
        current_parent = d.get('parent', '')
    elif line_str.startswith('position = Vector2('):
        coords = line_str[19:-1].split(',')
        try:
            x = float(coords[0].strip())
            y = float(coords[1].strip())
            if x >= 3000 and y >= 650:
                print(f"Parent: {current_parent:<35} | Node: {current_node:<30} | Pos: ({x:6.1f}, {y:6.1f})")
        except:
            pass
