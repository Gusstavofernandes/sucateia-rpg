with open('scripts/world/sucateia.gd', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i in range(130, 160):
    print(f"{i+1}: {lines[i]}")
