with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'Collision' in line or 'StaticBody2D' in line:
        print(f"L{i+1}: {line.strip()}")
