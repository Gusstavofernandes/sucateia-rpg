with open('scripts/world/alto_west_cais.gd', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i in range(430, 452):
    print(f"{i+1}: {lines[i]}")
