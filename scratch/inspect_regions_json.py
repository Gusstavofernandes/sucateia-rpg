import json

with open(r'c:\Users\Usuario\Documents\jogo\maps\ferrugem_baixa\region.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, v in data.items():
    print(f"Region: {k:<15} | Name: {v.get('name', ''):<35} | Scene: {v.get('scene', '')}")
