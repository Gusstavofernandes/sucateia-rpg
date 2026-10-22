with open('maps/fundo_ferro/fundo_ferro.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

lines = text.splitlines()
for line in lines[:40]:
    if line.startswith('[ext_resource'):
        print(line)
