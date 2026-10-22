with open('maps/fundo_ferro/fundo_ferro.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

lines = text.splitlines()
structures = ['MotorAbandonado', 'BombasDeRefluxo', 'ValvulasAntigas', 'TornoDesativado', 'CisternaDeRecalque', 'RestosDaFundacao']

for i, line in enumerate(lines):
    for s in structures:
        if f'parent="Structures/{s}"' in line:
            print(f"{s} child -> {line}")
            for k in range(i+1, min(len(lines), i+8)):
                if lines[k].startswith('['): break
                print(f"   {lines[k]}")
