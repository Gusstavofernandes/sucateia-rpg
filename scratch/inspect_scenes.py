import os

scenes = [
    r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn',
    r'c:\Users\Usuario\Documents\jogo\maps\ferrugem_baixa\alto.tscn',
    r'c:\Users\Usuario\Documents\jogo\maps\ferrugem_baixa\grande.tscn',
    r'c:\Users\Usuario\Documents\jogo\maps\ferrugem_baixa\fundo.tscn',
    r'c:\Users\Usuario\Documents\jogo\maps\fundo_ferro\fundo_ferro.tscn',
    r'c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn'
]

for s in scenes:
    if os.path.exists(s):
        size_kb = os.path.getsize(s) // 1024
        with open(s, 'r', encoding='utf-8', errors='ignore') as f:
            first_10 = [f.readline().strip() for _ in range(10)]
        print(f"=== {s} ({size_kb} KB) ===")
        for line in first_10[:5]:
            print("  ", line)
