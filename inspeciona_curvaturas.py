from PIL import Image
import numpy as np

# Carregar arquibancada limpa
im_bleachers = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_arquibancada_meia_lua_clean.png').convert("RGBA")

# Carregar arena circular anterior
im_arena = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\captura_arena_arredondada_obra_prima.png').convert("RGBA")

# Carregar chao robusto aprovado
im_chao = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props\arena_piso_fosso_completo_robusto_v1.png').convert("RGBA")

print("Bleachers size:", im_bleachers.size)
print("Arena size:", im_arena.size)
print("Chao size:", im_chao.size)

# Vamos analisar a borda inferior da arquibancada:
arr_b = np.array(im_bleachers)
# Onde termina a arquibancada na parte inferior (arco concavo):
# Vamos encontrar os pontos mais baixos (y maximo com alpha > 50) para cada coluna x
h_b, w_b, _ = arr_b.shape
bottom_curve = []
for x in range(0, w_b, 20):
    col = np.where(arr_b[:, x, 3] > 50)[0]
    if len(col) > 0:
        bottom_curve.append((x, col[-1]))

print("Amostra da curva inferior da arquibancada:")
for p in bottom_curve[::3]:
    print(p)
