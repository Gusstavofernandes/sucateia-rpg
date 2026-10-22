from PIL import Image
import numpy as np

img = Image.open('scratch/boca_tunel_v2_raw_cut.png')
print(f"Dimensões de boca_tunel_v2_raw_cut: {img.size}")
arr = np.array(img)

# Amostrar a linha da base opaca (y = 580)
row = arr[580, :, :]
# Posições onde alpha > 100
op_cols = np.where(row[:, 3] > 100)[0]
print(f"Trilhos na linha 580: de coluna {op_cols[0]} a {op_cols[-1]} (largura: {op_cols[-1] - op_cols[0]} px)")

# Vamos encontrar os dois picos do aço dos trilhos nessa linha
# Os trilhos de ferro fundido têm luminância/reflexo
col_means = []
for x in range(op_cols[0], op_cols[-1]):
    val = np.mean(arr[570:595, x, :3])
    col_means.append((x, val))

mid = len(col_means) // 2
left_peak = max(col_means[:mid], key=lambda i: i[1])
right_peak = max(col_means[mid:], key=lambda i: i[1])

print(f"Trilho Esquerdo: x = {left_peak[0]}")
print(f"Trilho Direito: x = {right_peak[0]}")
gauge = right_peak[0] - left_peak[0]
center = (left_peak[0] + right_peak[0]) / 2.0
print(f"Bitola na textura bruta: {gauge} px")
print(f"Centro do par de trilhos na textura: {center:.1f} px (largura={img.size[0]}, meio={img.size[0]/2:.1f})")
print(f"Offset em relação ao centro exato da textura: {center - img.size[0]/2:.1f} px")

# Analisar onde a moldura de pedra termina verticalmente
# A moldura de pedra tem largura ~1000 px (vai de x=0 a x=1000)
# Vamos encontrar até que linha Y a moldura de pedra se estende
left_pillar_base = np.where(arr[:, 50, 3] > 50)[0][-1]
right_pillar_base = np.where(arr[:, img.size[0]-50, 3] > 50)[0][-1]
print(f"Base do pilar esquerdo de pedra: y = {left_pillar_base}")
print(f"Base do pilar direito de pedra: y = {right_pillar_base}")
print(f"Base dos trilhos que saem para fora: y = {img.size[1]-1}")
