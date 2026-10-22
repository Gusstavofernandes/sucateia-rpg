from PIL import Image
import numpy as np

# Carregar captura refinada anterior
im = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\captura_arena_arredondada_refinada.png').convert("RGBA")
arr = np.array(im)

# Vamos analisar a regiao do topo do portao:
# x: 450 a 920, y: 370 a 445
# Vamos pegar a textura das ameias de ferro (que estao logo ao lado em x: 300 a 440, y: 440 a 550)
# A textura do ferro rebitado tem tom marrom escuro com ferrugem e parafusos (r ~ 95, g ~ 65, b ~ 50)
# Enquanto a laje clara do topo do portao tem tom bege/cinza claro (r ~ 140, g ~ 130, b ~ 115)

mask_laje_topo = (arr[:, :, 0] > 105) & (arr[:, :, 1] > 95) & (arr[:, :, 2] > 80)
mask_topo_box = np.zeros(arr.shape[:2], dtype=bool)
mask_topo_box[370:445, 450:925] = True
alvo_laje = mask_laje_topo & mask_topo_box

# Transformar a laje clara em ferro oxidado escuro combinando com as ameias:
# Reduzir brilho e ajustar tom
arr[alvo_laje, 0] = (arr[alvo_laje, 0] * 0.65).astype(np.uint8)
arr[alvo_laje, 1] = (arr[alvo_laje, 1] * 0.52).astype(np.uint8)
arr[alvo_laje, 2] = (arr[alvo_laje, 2] * 0.45).astype(np.uint8)

# Agora para o portao (y de 445 a 730, x de 490 a 890):
# Os vaos entre as barras que estao brancos/claros:
# Em vez de vazios transparentes ou brancos, vamos colocar o piso de pedra escura do fosso/corredor!
chao_fosso = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props\arena_piso_fosso_completo_robusto_v1.png').convert("RGBA")
chao_resized = chao_fosso.resize((1100, 325), Image.Resampling.LANCZOS)
chao_arr = np.array(chao_resized)

# Para qualquer pixel dentro do portao que tenha alpha < 200 ou seja muito claro:
mask_portao_interior = np.zeros(arr.shape[:2], dtype=bool)
mask_portao_interior[445:730, 490:890] = True

# Onde dentro do portao esta claro/transparente (vaos):
# Vamos colocar a pedra escura de combate sombreada
mask_vaos_portao = mask_portao_interior & ((arr[:, :, 3] < 220) | ((arr[:, :, 0] > 110) & (arr[:, :, 1] > 100) & (arr[:, :, 2] > 90)))

# Preencher com pedra escura sombreada (sombra do portao e fosso)
arr[mask_vaos_portao, 0] = 38
arr[mask_vaos_portao, 1] = 36
arr[mask_vaos_portao, 2] = 34
arr[mask_vaos_portao, 3] = 255

im_refinada_final = Image.fromarray(arr)
im_refinada_final.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\captura_arena_arredondada_obra_prima.png')
print("Obra-prima salva com sucesso!")
