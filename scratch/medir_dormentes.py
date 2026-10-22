from PIL import Image
import numpy as np

im_ponte = Image.open("assets/rails/trilho_reto_vertical_v1.png").convert("RGBA")
arr_ponte = np.array(im_ponte)
h, w, _ = arr_ponte.shape

# Vamos analisar o perfil de luminancia vertical na coluna central do trilho (onde ficam os dormentes e o lastro)
col_lum = 0.299 * arr_ponte[:, w//2, 0] + 0.587 * arr_ponte[:, w//2, 1] + 0.114 * arr_ponte[:, w//2, 2]
alpha_col = arr_ponte[:, w//2, 3]

# Achar os picos (dormentes de madeira clara/escura vs vaos escuros)
# Vamos detectar onde ha madeira de dormente
import scipy.signal
# Como nao sabemos se scipy esta instalado, vamos fazer deteccao simples de picos locais
peaks = []
for y in range(20, h - 20):
    if alpha_col[y] > 100:
        if col_lum[y] > col_lum[y-1] and col_lum[y] > col_lum[y+1] and col_lum[y] > 70:
            if not peaks or (y - peaks[-1]) > 40:
                peaks.append(y)

print(f"Total de dormentes detectados: {len(peaks)}")
print("Posições Y dos dormentes (textura):", peaks)
steps = np.diff(peaks)
print("Passos entre dormentes (textura):", steps)
print(f"Passo médio na textura: {np.mean(steps):.1f} px (no mundo escala 0.25: {np.mean(steps)*0.25:.1f} px)")

# Largura dos dormentes (extensão transversal X)
widths = []
thicknesses = []
for p in peaks[:5]:
    row_a = arr_ponte[p, :, 3]
    op = np.where(row_a > 100)[0]
    if len(op) > 0:
        widths.append(op[-1] - op[0])

print(f"Largura média dos dormentes na textura: {np.mean(widths):.1f} px (no mundo: {np.mean(widths)*0.25:.1f} px)")
