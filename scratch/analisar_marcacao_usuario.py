from PIL import Image
import numpy as np

img_path = 'C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/.user_uploaded/media_1791631572526.png'
img = Image.open(img_path).convert("RGBA")
arr = np.array(img)

print(f"Tamanho da imagem do usuário: {img.size}")

# Detectar os pixels verdes/cianoc (alto G, alto B, baixo R)
r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
# O verde marcado é em torno de R < 50, G > 200, B > 100
mask = (g > 200) & (b > 100) & (r < 80)
y_pts, x_pts = np.where(mask)

print(f"Total de pixels verdes encontrados: {len(y_pts)}")

if len(y_pts) > 0:
    # Agrupar os 4 pontos (dois superiores, dois inferiores)
    # y divide entre superiores (y < 280) e inferiores (y >= 280)
    # x divide entre esquerdos (x < 250) e direitos (x >= 250)
    
    top_left = (mask & (np.arange(arr.shape[0])[:, None] < 270) & (np.arange(arr.shape[1])[None, :] < 250))
    top_right = (mask & (np.arange(arr.shape[0])[:, None] < 270) & (np.arange(arr.shape[1])[None, :] >= 250))
    bot_left = (mask & (np.arange(arr.shape[0])[:, None] >= 270) & (np.arange(arr.shape[1])[None, :] < 250))
    bot_right = (mask & (np.arange(arr.shape[0])[:, None] >= 270) & (np.arange(arr.shape[1])[None, :] >= 250))
    
    def get_centroid(m):
        ys, xs = np.where(m)
        if len(ys) == 0: return None, None
        return np.mean(xs), np.mean(ys)
        
    tl_x, tl_y = get_centroid(top_left)
    tr_x, tr_y = get_centroid(top_right)
    bl_x, bl_y = get_centroid(bot_left)
    br_x, br_y = get_centroid(bot_right)
    
    print(f"Ponto Topo Esquerdo (Trilho Ligação Esq): x = {tl_x:.1f}, y = {tl_y:.1f}")
    print(f"Ponto Topo Direito (Trilho Ligação Dir):  x = {tr_x:.1f}, y = {tr_y:.1f}")
    print(f"Bitola Trilho Ligação na Emenda: {tr_x - tl_x:.1f} px")
    print(f"Centro Trilho Ligação na Emenda: {(tl_x + tr_x)/2.0:.1f} px")
    
    print(f"\nPonto Base Esquerdo (Ponte Esq): x = {bl_x:.1f}, y = {bl_y:.1f}")
    print(f"Ponto Base Direito (Ponte Dir):  x = {br_x:.1f}, y = {br_y:.1f}")
    print(f"Bitola Ponte na Emenda: {br_x - bl_x:.1f} px")
    print(f"Centro Ponte na Emenda: {(bl_x + br_x)/2.0:.1f} px")
    
    fator_escala = (tr_x - tl_x) / (br_x - bl_x)
    print(f"\n---> FATOR DE ESCALA EXATO SUGERIDO PELA MARCAÇÃO DO USUÁRIO: {fator_escala:.4f}")
    print(f"Desvio do centro X entre as duas peças: {((bl_x + br_x)/2.0) - ((tl_x + tr_x)/2.0):.1f} px")
