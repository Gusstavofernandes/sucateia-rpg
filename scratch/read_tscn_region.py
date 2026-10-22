with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i in range(10220, 10245):
    print(f"{i+1}: {lines[i]}")
