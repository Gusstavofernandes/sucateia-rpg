from PIL import Image
import numpy as np

img = Image.open('C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/.user_uploaded/media_1791602107053.jpg').convert("RGBA")
arr = np.array(img)

# Amostrar linha 600 (base dos trilhos)
# Procurar os dois picos de ferro dos trilhos
row = arr[600, :, :]
# Os trilhos de ferro têm cor de aço marrom/metálico com brilho
# Vamos inspecionar os pixels entre x=400 e x=620
for x in range(410, 615):
    r, g, b = row[x, :3]
    # Se não for magenta
    if not (r > 200 and g < 50 and b > 200):
        # intensidade / contraste
        pass

# Vamos encontrar as colunas dos trilhos de aço (os dois trilhos de metal)
# Vamos plotar/analisar a luminância ao longo da linha 600
lum = np.mean(row[:, :3], axis=1)
# Onde não é magenta
is_not_magenta = ~((row[:, 0] > 200) & (row[:, 1] < 50) & (row[:, 2] > 200))
# Vamos encontrar os centros dos dois trilhos de aço
# Linha do trilho esquerdo e direito
# No olho humano: o trilho esquerdo está por volta de x=440-450, o direito por volta de x=570-580
# Vamos fazer uma busca precisa do aço reflexivo
slice_x = np.where(is_not_magenta)[0]
print(f"Trilhos + dormentes na linha 600: de x={slice_x[0]} a x={slice_x[-1]}")

# Na imagem bruta 1024x682:
# Dormentes têm largura de ~230-245 px
# Bitola dos trilhos (distância entre o topo do trilho esquerdo e o direito):
# Vamos calcular por análise de coluna
col_means = []
for x in range(420, 605):
    # média na coluna vertical entre y=580 e y=640
    strip = arr[580:640, x, :3]
    # trilho de ferro é mais claro/brilhante que a madeira escura
    col_means.append((x, np.mean(strip)))

# Encontrar os 2 picos locais
# Pico esquerdo e pico direito
left_peak = max(col_means[:len(col_means)//2], key=lambda item: item[1])
right_peak = max(col_means[len(col_means)//2:], key=lambda item: item[1])

print(f"Pico Trilho Esquerdo: x = {left_peak[0]}")
print(f"Pico Trilho Direito: x = {right_peak[0]}")
gauge_raw = right_peak[0] - left_peak[0]
center_rails = (left_peak[0] + right_peak[0]) / 2.0
print(f"Bitola bruta na imagem: {gauge_raw} px")
print(f"Centro do par de trilhos: {center_rails:.1f} px (offset: {center_rails - 512.0:.1f} px)")
