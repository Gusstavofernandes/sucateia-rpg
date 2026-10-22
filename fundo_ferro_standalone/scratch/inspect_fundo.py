import os

with open('maps/fundo_ferro/fundo_ferro.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    for line in f:
        if line.startswith('[node ') and 'parent="."' in line:
            print(line.strip())
