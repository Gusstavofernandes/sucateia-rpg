from PIL import Image
import numpy as np

img_path = "fundo_ferro_standalone/debug_mundo_1to1.png"
im = Image.open(img_path)
arr = np.array(im)
h, w, c = arr.shape
print(f"debug_mundo_1to1.png: {w}x{h}, canais={c}")

# Mapeamento:
# X_mundo = X_img - 830  <=> X_img = X_mundo + 830
# Y_mundo = Y_img + 140  <=> Y_img = Y_mundo - 140

def analyze_world_y(y_world):
    y_img = int(round(y_world - 140))
    if y_img < 0 or y_img >= h:
        print(f"Y_world={y_world} fora do viewport (Y_img={y_img})")
        return
        
    row_rgb = arr[y_img, :, :3]
    lum = 0.299 * row_rgb[:, 0] + 0.587 * row_rgb[:, 1] + 0.114 * row_rgb[:, 2]
    
    # Faixa da ferrovia em torno de X_mundo = -190 (X_img = 640)
    # A ferrovia e dormentes ficam entre X_mundo = -270 e -110 (X_img = 560 a 720)
    x_range = range(540, 740)
    
    # Vamos imprimir os picos e transições
    grad = np.diff(lum)
    
    # Picos dos dois trilhos de metal (esq e dir)
    mid_img = 640
    esq_range = range(560, 630)
    dir_range = range(650, 720)
    
    peak_esq = esq_range[0] + np.argmax(lum[esq_range])
    peak_dir = dir_range[0] + np.argmax(lum[dir_range])
    
    # Sapatas externas (onde o metal/dormente transiciona para a mureta/chão)
    # Procurar a borda externa esquerda: gradiente acentuado ou limiar
    # Vamos inspecionar detalhadamente as colunas de 560 a 720
    print(f"\n==========================================")
    print(f"Y_mundo = {y_world:.1f} (Y_img = {y_img})")
    print(f"Pico Trilho Esq (cabeça): X_img={peak_esq} -> X_mundo={peak_esq - 830}")
    print(f"Pico Trilho Dir (cabeça): X_img={peak_dir} -> X_mundo={peak_dir - 830}")
    print(f"Bitola cabeças (mundo): {(peak_dir - peak_esq):.1f} px | Centro: {((peak_esq + peak_dir)/2.0 - 830):.2f}")
    
    # Mostrar pixels com lum alta nos dois trilhos
    for xi in range(peak_esq - 15, peak_esq + 15):
        if xi == peak_esq:
            print(f"  *ESQ* X_m={xi-830}: Lum={lum[xi]:.1f}, RGB={row_rgb[xi]}")
    for xi in range(peak_dir - 15, peak_dir + 15):
        if xi == peak_dir:
            print(f"  *DIR* X_m={xi-830}: Lum={lum[xi]:.1f}, RGB={row_rgb[xi]}")

# Analisar alturas-chave
for yw in [380.0, 400.0, 404.0, 405.0, 406.0, 407.0, 410.0, 450.0, 500.0, 525.0, 550.0, 600.0, 617.0, 622.0]:
    analyze_world_y(yw)
