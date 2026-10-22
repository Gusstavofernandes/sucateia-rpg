with open('maps/fundo_ferro/fundo_ferro.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

nodes_to_check = [
    'MotorAbandonado',
    'BombasDeRefluxo',
    'ValvulasAntigas',
    'TornoDesativado',
    'CisternaDeRecalque',
    'RestosDaFundacao'
]

lines = text.splitlines()
for i, line in enumerate(lines):
    for n in nodes_to_check:
        if f'name="{n}"' in line:
            print(f"=== {n} ===")
            for k in range(i, min(len(lines), i + 25)):
                if lines[k].startswith('[node ') and k > i:
                    break
                print(lines[k])
