from PIL import Image, ImageFilter
import numpy as np

src_path = 'C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/.user_uploaded/media_1791602107053.jpg'
img = Image.open(src_path).convert("RGBA")
arr = np.array(img, dtype=np.float32)

r = arr[:, :, 0]
g = arr[:, :, 1]
b = arr[:, :, 2]

# Chroma key para magenta (#FF00FF)
# Magenta tem R e B altos, G baixo.
# Distância euclidiana em relação a pure magenta (255, 0, 255):
dist_magenta = np.sqrt((r - 255)**2 + (g - 0)**2 + (b - 255)**2)

# Critério de magenta:
# G < 70 e (r > 180) e (b > 180) e (r - g > 100) e (b - g > 100)
is_magenta = (g < 65) & (r > 180) & (b > 180) & ((r - g) > 100) & ((b - g) > 100)

# Criar máscara alfa inicial
alpha = np.where(is_magenta, 0, 255).astype(np.uint8)

# Despill: remover sangramento de magenta nas bordas semi-transparentes
# Onde a cor tinha excesso de magenta (r > g e b > g), atenuar o componente magenta residual
excess_magenta = np.maximum(0, np.minimum(r - g, b - g))
r_clean = r - excess_magenta * 0.4
b_clean = b - excess_magenta * 0.4
r_clean = np.clip(r_clean, 0, 255).astype(np.uint8)
g_clean = np.clip(g, 0, 255).astype(np.uint8)
b_clean = np.clip(b_clean, 0, 255).astype(np.uint8)

clean_rgba = np.stack([r_clean, g_clean, b_clean, alpha], axis=2)
result_img = Image.fromarray(clean_rgba, mode="RGBA")

# Aplicar suave erosão de 1 pixel na máscara para garantir zero halos
alpha_pil = Image.fromarray(alpha, mode="L")
alpha_eroded = alpha_pil.filter(ImageFilter.MinFilter(3)) # erosão de 1px
result_img.putalpha(alpha_eroded)

# Cortar o bounding box opaco real (remover margens transparentes externas desnecessárias)
bbox = result_img.getbbox()
print("Bounding box opaco:", bbox)
cropped_img = result_img.crop(bbox)
print(f"Nova resolução após crop de bordas: {cropped_img.size}")

# Salvar boca_tunel_v2.png temporária para medições
cropped_img.save('scratch/boca_tunel_v2_raw_cut.png')
print("Salvo scratch/boca_tunel_v2_raw_cut.png!")
