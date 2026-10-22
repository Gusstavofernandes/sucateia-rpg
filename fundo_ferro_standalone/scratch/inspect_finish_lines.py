with open('maps/fundo_ferro/fundo_ferro.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'FundoFunctionalFinish' in line:
        for j in range(max(0, i-5), min(len(lines), i+30)):
            print(f"{j}: {lines[j].strip()}")
        break
