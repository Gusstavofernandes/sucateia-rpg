with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    if l.startswith('[node ') and 'Sprite2D' in l:
        name = l.split('name="')[1].split('"')[0] if 'name="' in l else l
        parent = l.split('parent="')[1].split('"')[0] if 'parent="' in l else ""
        tex = ""
        pos = ""
        for k in range(i+1, min(len(lines), i+8)):
            if lines[k].startswith('[node '): break
            if 'texture = ' in lines[k]: tex = lines[k].strip()
            if 'position = ' in lines[k]: pos = lines[k].strip()
        print(f"{name} (parent: {parent}) | {pos} | {tex}")
