import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Procurar os nós que usam a textura da bancada (19_v1cvy) ou similares
lines = text.split('\n')
for i, line in enumerate(lines):
    if '19_v1cvy' in line:
        # Imprimir bloco ao redor
        start = max(0, i - 15)
        end = min(len(lines), i + 10)
        print("--- Encontrado 19_v1cvy ---")
        for j in range(start, end):
            print(f"{j}: {lines[j]}")
