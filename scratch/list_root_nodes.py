with open('scenes/fundo_ferro_master.tscn', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i, l in enumerate(lines):
    if l.startswith('[node name="') and 'parent=".' in l:
        print(f"{i+1}: {l}")
