import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# Procurar nós que tenham pináculo ou gótico ou corrente ou similar
for line in text.split('\n'):
    if any(k in line.lower() for k in ['pinaculo', 'pinnacle', 'gothic', 'cathedral', 'gate', 'portao', 'muralha', 'grade']):
        print(line)
