from PIL import Image
import numpy as np

# 1. Analisar estacao_trilho_v2.png (Trilho de Ligação)
# Escala no jogo: 0.20
# Posição global no mundo: (-215.9, 325.0)
# Topo Y no mundo: 244.0, Base Y no mundo: 406.0

im_estacao = Image.open("assets/rails/estacao_trilho_v2.png").convert("RGBA")
arr_est = np.array(im_estacao)
w_est, h_est = im_estacao.size

print("=== MEDIÇÃO ESTACAO_TRILHO_V2 (TRILHO DE LIGAÇÃO) ===")
print(f"Canvas: {w_est}x{h_est}, Escala no Godot: 0.20")

# Vamos inspecionar linhas próximas à base (Y = h_est - 10, Y = h_est - 20) onde ocorre a emenda com a ponte!
# Em Y = 800 do sprite (que no mundo corresponde a 325 - 81 + 800*0.2 = 325 - 81 + 160 = 404.0)
# A base exata é Y = 810 (no mundo Y = 406.0)

for y in [10, 100, 200, 400, 600, 750, 790, 800, 808]:
    if y >= h_est: continue
    row_rgb = arr_est[y, :, :3]
    row_a = arr_est[y, :, 3]
    opaque = np.where(row_a > 100)[0]
    # Encontrar trilhos
    # Trilhos são duas linhas de aço verticais
    # Vamos escanear a linha e achar os picos de gradiente/luminância
    print(f"Y={y:3d} (mundo Y={244.0 + y*0.20:5.1f}): faixa opaca [{opaque[0] if len(opaque) else 0} .. {opaque[-1] if len(opaque) else 0}]")
