import os

with open(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

found = []
for kw in ['grande', 'campos', 'campos_sucata', 'grande_ferrugem', 'lixao', 'scrap_colossus']:
    count = text.lower().count(kw)
    found.append((kw, count))

print("Mentions in sucateia.tscn:")
for kw, count in found:
    print(f"  {kw}: {count}")
