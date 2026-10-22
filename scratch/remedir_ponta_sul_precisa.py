from PIL import Image
import numpy as np

# Carregar imagem nativa do trilho
img_ponte = Image.open("assets/rails/trilho_reto_vertical_v1.png").convert("RGBA")
arr_ponte = np.array(img_ponte)
h_tex, w_tex, _ = arr_ponte.shape

# Posição global da ponte: X = -189.85, Y = 593.5
# Posição relativa dos trilhos: X = 0, Y = -93.75 -> Y_centro = 499.75
# Escala: 0.25

def tex_to_world(x_tex, y_tex):
    x_w = -189.85 + (x_tex - 372.5) * 0.25
    y_w = 499.75 + (y_tex - 491.0) * 0.25
    return x_w, y_w

def world_to_tex_y(y_w):
    return int(round(491.0 + (y_w - 499.75) / 0.25))

print("=== REMEDIÇÃO RIGOROSA DA PONTE (PERFIL DE SAPATA DE FERRO) ===")

# Vamos inspecionar as linhas em torno de Y_mundo = 406, 500, 540, 580, 617
test_points = [406.0, 500.0, 540.0, 580.0, 617.0]

measurements = []

for yw in test_points:
    y_tex = world_to_tex_y(yw)
    if y_tex >= h_tex:
        y_tex = h_tex - 1
    
    # Vamos pegar a fatia Y_tex da textura
    # Para evitar ruído de um único pixel, analisamos a média de 3 linhas [y_tex-1, y_tex, y_tex+1]
    slice_rgb = arr_ponte[max(0, y_tex-1):min(h_tex, y_tex+2), :, :3].mean(axis=0)
    slice_a = arr_ponte[max(0, y_tex-1):min(h_tex, y_tex+2), :, 3].mean(axis=0)
    lum = 0.299 * slice_rgb[:, 0] + 0.587 * slice_rgb[:, 1] + 0.114 * slice_rgb[:, 2]
    
    # Os trilhos de ferro tem:
    # Cabeça: pico alto de luminância e cor cinza/aço (R ~ G ~ B)
    # Sapata: base plana de aço que se estende para fora da cabeça
    # Lastro/fundo: escuro ou dormente de madeira marrom (R >> B)
    # A sapata de ferro termina onde a cor metálica de base do trilho encontra o lastro/dormente
    
    # Trilho esquerdo fica em X_tex entre 120 e 260
    # Trilho direito fica em X_tex entre 480 e 620
    
    # Vamos encontrar o pico da cabeça (boleto)
    head_esq = 120 + np.argmax(lum[120:260])
    head_dir = 480 + np.argmax(lum[480:620])
    
    # Sapata externa esquerda:
    # Caminha para a esquerda a partir da cabeça até a transição da sapata de aço
    # O metal da sapata tem luminância e tom cinza característico
    # Vamos encontrar onde a derivada de luminância/cor indica a borda da base de aço:
    # A borda da sapata é o ponto de inflexão/corte da base metálica
    flange_esq = head_esq
    for x in range(head_esq, 80, -1):
        # A sapata de ferro tem textura metálica (R, G, B próximos, lum > 40)
        # Quando sai da sapata, cai no dormente escuro ou lastro
        if lum[x] < 35 or abs(slice_rgb[x, 0] - slice_rgb[x, 2]) > 25:
            flange_esq = x + 1
            break
            
    # Sapata externa direita:
    # Caminha para a direita a partir da cabeça
    flange_dir = head_dir
    for x in range(head_dir, 680):
        if lum[x] < 35 or abs(slice_rgb[x, 0] - slice_rgb[x, 2]) > 25:
            flange_dir = x - 1
            break
            
    gauge_tex = flange_dir - flange_esq
    center_tex = (flange_esq + flange_dir) / 2.0
    
    # Converter para o mundo com X = -189.85
    x_esq_w, _ = tex_to_world(flange_esq, y_tex)
    x_dir_w, _ = tex_to_world(flange_dir, y_tex)
    gauge_w = x_dir_w - x_esq_w
    center_w = (x_esq_w + x_dir_w) / 2.0
    
    measurements.append({
        "y_mundo": yw,
        "y_tex": y_tex,
        "flange_esq_tex": flange_esq,
        "flange_dir_tex": flange_dir,
        "gauge_tex": gauge_tex,
        "center_tex": center_tex,
        "flange_esq_mundo": x_esq_w,
        "flange_dir_mundo": x_dir_w,
        "gauge_mundo": gauge_w,
        "center_mundo": center_w,
        "head_esq_tex": head_esq,
        "head_dir_tex": head_dir
    })
    
    print(f"Y_mundo={yw:5.1f} (Y_tex={y_tex:3d}):")
    print(f"   Sapata Esq: tex={flange_esq:3d} -> mundo={x_esq_w:7.2f} px")
    print(f"   Sapata Dir: tex={flange_dir:3d} -> mundo={x_dir_w:7.2f} px")
    print(f"   Bitola Ext: tex={gauge_tex:3d} -> mundo={gauge_w:7.2f} px")
    print(f"   Centro X  : tex={center_tex:5.1f} -> mundo={center_w:7.2f} px")

# FASE DO DORMENTE EM Y = 617 (Y_tex = 960)
print("\n=== ANÁLISE DE FASE DO DORMENTE EM Y_mundo = 617 (Y_tex = 960) ===")
# Detectar dormentes na região Y_tex entre 800 e 980
# Dormentes tem cor marrom de madeira (R alto, B baixo) e luminancia média entre os trilhos
col_central = arr_ponte[:, w_tex//2, :3]
col_lum = 0.299 * col_central[:, 0] + 0.587 * col_central[:, 1] + 0.114 * col_central[:, 2]

# Picos de dormentes na coluna central
sleepers_near_end = []
for y in range(800, 975):
    if col_lum[y] > col_lum[y-1] and col_lum[y] > col_lum[y+1] and col_lum[y] > 60:
        if not sleepers_near_end or (y - sleepers_near_end[-1]) > 30:
            sleepers_near_end.append(y)

print("Dormentes próximos ao fim da ponte (Y_tex):", sleepers_near_end)
for s in sleepers_near_end:
    _, s_yw = tex_to_world(w_tex//2, s)
    dist_to_617 = 617.0 - s_yw
    print(f"   Dormente Y_tex={s:3d} -> Y_mundo={s_yw:6.2f} px | Distância até Y=617: {dist_to_617:5.2f} px")

# Passo local
local_steps = np.diff(sleepers_near_end)
print("Passos locais na textura:", local_steps)
local_passo_mundo = np.mean(local_steps) * 0.25
print(f"Passo local no mundo: {local_passo_mundo:.2f} px")

# Último dormente antes de Y=617:
last_sleeper_y_tex = sleepers_near_end[-1]
_, last_sleeper_y_mundo = tex_to_world(w_tex//2, last_sleeper_y_tex)
fase_ao_617 = 617.0 - last_sleeper_y_mundo
print(f"Fase em Y=617 (distância do fim da ponte ao centro do último dormente): {fase_ao_617:.2f} px de mundo ({fase_ao_617*4:.1f} px de arquivo)")
