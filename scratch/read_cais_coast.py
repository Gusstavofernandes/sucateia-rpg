with open('scripts/world/alto_west_cais.gd', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i in range(440, min(len(lines), 490)):
    print(f"{i+1}: {lines[i]}")
