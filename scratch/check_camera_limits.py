import re

with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for line in lines:
    if 'limit_left' in line or 'limit_right' in line or 'Camera' in line:
        print(line[:100])
