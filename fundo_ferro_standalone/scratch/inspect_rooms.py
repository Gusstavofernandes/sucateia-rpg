import os

with open('maps/fundo_ferro/fundo_ferro.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Find all nodes under Rooms or FundoFunctionalFinish
for line in text.splitlines():
    if 'parent="Rooms"' in line or 'parent="FundoFunctionalFinish"' in line or 'parent="Routes"' in line:
        print(line.strip())
