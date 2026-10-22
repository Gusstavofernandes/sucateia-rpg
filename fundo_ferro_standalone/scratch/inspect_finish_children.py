import os

with open('maps/fundo_ferro/fundo_ferro.tscn', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

in_finish = False
for line in text.splitlines():
    if 'name="FundoFunctionalFinish"' in line:
        in_finish = True
    elif in_finish and line.startswith('[node ') and 'parent="FundoFunctionalFinish' not in line and 'parent="."' in line:
        in_finish = False
    elif in_finish and line.startswith('[node '):
        print(line.strip())
