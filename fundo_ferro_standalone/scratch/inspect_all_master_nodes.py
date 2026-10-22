with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

print("Nodes in fundo_ferro_master.tscn:")
for line in text.splitlines():
    if line.startswith('[node '):
        print(line)
