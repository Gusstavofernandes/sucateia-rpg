from PIL import Image
import numpy as np

# Carregar imagem 2 (anel arredondado de coliseu)
im2 = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_muralha_sul_clean.png').convert("RGBA")
w, h = im2.size
arr2 = np.array(im2)

# Carregar o chão robusto perfeito
chao_fosso = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props\arena_piso_fosso_completo_robusto_v1.png').convert("RGBA")

# Na Imagem 2:
# O interior da arena e delimitado pela elipse:
cx = 688
cy = 300
rx = 525
ry = 155

# Vamos redimensionar o chão de combate para cobrir essa elipse interna
chao_w = int(rx * 2 * 1.05) # ~1100
chao_h = int(ry * 2 * 1.05) # ~325
chao_resized = chao_fosso.resize((chao_w, chao_h), Image.Resampling.LANCZOS)

# Criar mascara da elipse interna suave
y_indices, x_indices = np.indices((h, w))
dist_elipse = ((x_indices - cx) / rx) ** 2 + ((y_indices - cy) / ry) ** 2

# Mascara da terra original a ser substituida:
# Queremos que o chao fique no interior (dist_elipse <= 1.0)
# E o muro norte de tras fica por tras do chao (ou a base do muro de tras encosta no chao)
# E o muro sul da frente fica POR CIMA do chao!

# Vamos separar a Imagem 2 em:
# 1. Muro Traseiro (Norte): pixels com y_indices < cy e onde nao e terra
# 2. Muro Frontal (Sul): pixels com y_indices >= cy
# Vamos ver a divisao exata:
# A mureta frontal comeca onde a borda interna da frente comeca (dist_elipse > 0.95 no hemisferio sul)
# e o portao frontal desce ate y=745.

mask_muro_frontal = (dist_elipse > 0.95) & (y_indices >= cy) & (arr2[:, :, 3] > 0)
# Alem disso, todo o portao central (x de 460 a 916, y >= 380) e parte frontal
mask_portao_estrutura = (x_indices >= 460) & (x_indices <= 916) & (y_indices >= 380) & (arr2[:, :, 3] > 0)

# Mascara completa da frente:
mask_frente = (y_indices >= cy) & (dist_elipse >= 0.90) | mask_portao_estrutura
# Muro de tras:
mask_tras = (~mask_frente) & (dist_elipse >= 0.92) & (arr2[:, :, 3] > 0)

arr_tras = arr2.copy()
arr_tras[~mask_tras, 3] = 0

arr_frente = arr2.copy()
arr_frente[~mask_frente, 3] = 0

# Chao recortado pela elipse interna suave
mask_chao_elipse = dist_elipse <= 1.0
arr_chao_canvas = np.zeros((h, w, 4), dtype=np.uint8)

# Colar chao_resized centralizado em (cx, cy)
x0 = cx - chao_w // 2
y0 = cy - chao_h // 2
chao_arr = np.array(chao_resized)
for y in range(chao_h):
    for x in range(chao_w):
        out_y = y0 + y
        out_x = x0 + x
        if 0 <= out_y < h and 0 <= out_x < w:
            if dist_elipse[out_y, out_x] <= 0.96:
                arr_chao_canvas[out_y, out_x] = chao_arr[y, x]

# Montagem: Tras -> Chao -> Frente
comp = Image.new("RGBA", (w, h), (0, 0, 0, 0))
comp.paste(Image.fromarray(arr_tras), (0, 0), Image.fromarray(arr_tras))
comp.paste(Image.fromarray(arr_chao_canvas), (0, 0), Image.fromarray(arr_chao_canvas))
comp.paste(Image.fromarray(arr_frente), (0, 0), Image.fromarray(arr_frente))

comp.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_arena_elipse_perfeita.png')
print("Teste elipse perfeita salvo!")
