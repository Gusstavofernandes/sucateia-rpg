with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i in range(2833, min(2950, len(lines))):
    print(f"{i+1}: {lines[i]}")
