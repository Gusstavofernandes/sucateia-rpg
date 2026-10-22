import os, sys
from PIL import Image
import numpy as np

target_dirs = [
    r"c:\Users\Usuario\Documents\jogo\assets\machines",
    r"c:\Users\Usuario\Documents\jogo\assets\pipes",
    r"c:\Users\Usuario\Documents\jogo\assets\puddles",
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\machines",
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes",
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\puddles"
]

total_checked = 0
failures = []

for d in target_dirs:
    if not os.path.exists(d):
        continue
    for f in os.listdir(d):
        if not f.endswith(".png") or f.endswith("_sombra.png") or f == "sprites_pocas_esgoto_v1.png" or f == "kit_tubulacao_modular_v1.png":
            continue
        fp = os.path.join(d, f)
        img = Image.open(fp).convert("RGBA")
        arr = np.array(img)
        r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
        
        # Check strict magenta condition:
        # Alpha is visible, R and B are high, G is noticeably lower, and (R+B)/2 exceeds G by > 40
        magenta = (a > 10) & (r > 120) & (b > 120) & (g < 100) & (((r.astype(int) + b.astype(int)) / 2) - g.astype(int) > 40)
        count = np.sum(magenta)
        total_checked += 1
        if count > 0:
            failures.append((fp, count))
            print(f"FALHA [P0.1]: {f} contem {count} pixels magenta residuais!")
        else:
            print(f"OK [P0.1]: {f} - ZERO pixels magenta.")

print(f"\nTotal verificado: {total_checked} arquivos.")
if len(failures) > 0:
    print(f"ERRO: {len(failures)} arquivos falharam no teste de sanidade magenta!")
    sys.exit(1)
else:
    print("SUCESSO: Todos os assets passaram no teste de sanidade [P0.1]! Zero franjas magenta.")
    sys.exit(0)
