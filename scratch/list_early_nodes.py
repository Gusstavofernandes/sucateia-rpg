with open('scenes/fundo_ferro_master.tscn', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines[:120]):
    if l.startswith('[node name=') or 'position = ' in l:
        print(f"{i+1}: {l}")
