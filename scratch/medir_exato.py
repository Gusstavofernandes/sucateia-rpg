from PIL import Image
import numpy as np
import json

# Carregar imagens
img_est = Image.open("assets/rails/estacao_trilho_v2.png").convert("RGBA")
img_ponte = Image.open("assets/rails/trilho_reto_vertical_v1.png").convert("RGBA")

arr_est = np.array(img_est)
arr_ponte = np.array(img_ponte)

# Vamos inspecionar estacao_trilho_v2.png na base (onde ela encontra a ponte)
# A base do sprite é Y = 810 (na textura). Vamos olhar Y = 780 a 808
# E na ponte, o topo do trilho (onde encontra a estação) é Y = 0 a 30
# E na ponta sul da ponte (onde ela vai receber a estação de descarga), é Y = 950 a 980

def get_exact_rail_metrics(arr, y, is_bridge=False):
    row_rgb = arr[y, :, :3]
    row_a = arr[y, :, 3]
    lum = 0.299 * row_rgb[:, 0] + 0.587 * row_rgb[:, 1] + 0.114 * row_rgb[:, 2]
    
    # Achar colunas com opacidade
    opaque = np.where(row_a > 120)[0]
    if len(opaque) == 0:
        return None
        
    # Vamos achar o perfil do trilho esquerdo e direito
    # Em trilho_reto_vertical_v1.png: trilhos ficam ao redor de X=150-250 (esq) e X=500-600 (dir)
    # Em estacao_trilho_v2.png: trilhos ficam ao redor de X=380-480 (esq) e X=820-920 (dir)
    if is_bridge:
        x_esq_range = range(100, 320)
        x_dir_range = range(450, 680)
    else:
        x_esq_range = range(360, 520)
        x_dir_range = range(780, 950)
        
    # Procurar borda externa da sapata: transição onde o pé de ferro do trilho começa
    # A sapata de ferro tem textura metálica e sombreamento característico sobre o lastro
    # Vamos identificar o gradiente de transição do lastro para a sapata do trilho esquerdo:
    # Para o trilho esquerdo, a borda externa da sapata é o ponto mais à esquerda (menor X) da sapata.
    # A cabeça do trilho é o ponto mais alto/brilhante (pico de reflexo do boleto).
    # Para o trilho direito, a borda externa da sapata é o ponto mais à direita (maior X) da sapata.
    
    # Vamos imprimir detalhadamente a linha
    return {
        "y": y,
        "lum": lum,
        "alpha": row_a
    }

print("Script de métricas preparado.")
