import re

with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]*)"\]([^\[]*)'
matches = re.findall(pattern, text)

print("=== NÓS NO CANTO SUPERIOR ESQUERDO (X < 400, Y < 350) ===")
for name, ntype, parent, body in matches:
    pos_m = re.search(r'position\s*=\s*Vector2\(([^)]+)\)', body)
    if pos_m:
        try:
            px, py = [float(x.strip()) for x in pos_m.group(1).split(',')]
            if -500 <= px <= 400 and -100 <= py <= 350:
                print(f"Node: {name} ({ntype}, parent={parent}) at ({px}, {py})")
                for l in body.splitlines():
                    if any(k in l for k in ['texture', 'scale', 'z_index']):
                        print(f"    {l.strip()}")
        except:
            pass
