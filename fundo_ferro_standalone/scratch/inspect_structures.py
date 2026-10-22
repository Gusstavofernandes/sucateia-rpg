with open('maps/fundo_ferro/fundo_ferro.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

for line in text.splitlines():
    if 'parent="Structures"' in line:
        print(line.strip())
