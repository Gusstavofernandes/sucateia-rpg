with open('scenes/fundo_ferro_master.tscn', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
for i in range(208, 235):
    print(f"{i+1}: {lines[i]}")
