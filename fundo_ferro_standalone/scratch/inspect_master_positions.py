with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

lines = text.splitlines()
for i, line in enumerate(lines):
    if line.startswith('[node '):
        for k in range(i+1, min(len(lines), i+8)):
            if lines[k].startswith('[node '):
                break
            if 'position = Vector2(' in lines[k]:
                name = line.split('name="')[1].split('"')[0] if 'name="' in line else line
                print(f"{name} -> {lines[k].strip()}")
                break
