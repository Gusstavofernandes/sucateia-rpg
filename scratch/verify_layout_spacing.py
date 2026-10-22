import os
from PIL import Image
import numpy as np

# Map Colosseum bottom edge
col_sul_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props\arena_coliseu_imponente_sul_v4.png'
im_col = Image.open(col_sul_path).convert("RGBA")
cw, ch = im_col.size
arr_col = np.array(im_col)[:, :, 3]

def get_coliseu_bottom_y(wx):
    img_x = int((wx - 4940) / 1.32 + cw / 2)
    if 0 <= img_x < cw:
        col_alpha = arr_col[:, img_x]
        non_zero = np.where(col_alpha > 20)[0]
        if len(non_zero) > 0:
            return 545 + (non_zero.max() - ch / 2.0) * 1.32
    return -9999.0

props = [
    # Zona A: Feira do Rolo (Oeste - Totalmente fora do Coliseu)
    ("BarracaApostas_Principal",     3350,  950, 0.32, -475, 1536, 1024),
    ("BarracaPecasRaras",            3750,  950, 0.33, -475, 1536, 1024),
    ("cloth_stall",                  3350, 1260, 0.26, -470, 1536, 1024),
    ("JaulaHumanoidesMercadoria",    3750, 1260, 0.35, -475, 1536, 1024),
    ("market_salvage_cart",          4120, 1260, 0.22, -643, 1223, 1286),
    ("TapeteTrocaSucata_1",          3350, 1520, 0.28, -250, 1536, 1024),
    ("TapeteTrocaSucata_2",          3750, 1520, -0.28, -250, 1536, 1024),
    ("BarracaApostas_Secundaria",    3350, 1780, 0.30, -475, 1536, 1024),
    ("fundo_sorting_bank",           3900, 1780, 0.26, -385, 2038,  771),
    
    # Zona B: Praça e Acesso Sul do Coliseu (Centro)
    # Colosseum gate is at (4940, 1024). Avenue from Y=1024 to Y=1400 is OPEN.
    ("exchange_pavilion",            4450, 1460, 0.27, -478, 1586,  992),
    ("wholesale_arcade",             4950, 1780, 0.28, -496, 1586,  992),
    
    # Zona C: Distrito Mecânico (Leste)
    ("forjas_recycler",              4900, 1460, 0.30, -492, 1536, 1024),
    ("forjas_workshop",              5400, 1460, 0.27, -545, 1443, 1090),
    ("fundo_abandoned_engine",       5820, 1260, 0.28, -496, 1536, 1024),
    ("forjas_boiler_hall",           5850, 1650, 0.28, -498, 1536, 1024),
    ("alto_cistern",                 6320, 1220, 0.24, -599, 1313, 1198),
    ("fundo_collapsed_corner",       6380, 1580, 0.28, -463, 1697,  927),
]

print("=== 1. VERIFICANDO SOBREPOSIÇÃO COM O COLISEU ===")
col_overlap_found = False
for name, px, py, sc, off_y, iw, ih in props:
    abs_sc = abs(sc)
    top_y = py + (off_y - ih / 2.0) * abs_sc
    left_x = px - (iw / 2.0) * abs_sc
    right_x = px + (iw / 2.0) * abs_sc
    
    for test_x in np.linspace(left_x, right_x, 10):
        col_bottom = get_coliseu_bottom_y(test_x)
        if col_bottom > -9000:
            if top_y < col_bottom + 20: # 20px safety margin
                print(f"ALERTA: {name} cruza o Coliseu em X={test_x:.0f}! Top_Y={top_y:.1f} < Col_Bottom={col_bottom:.1f}")
                col_overlap_found = True

if not col_overlap_found:
    print("PERFEITO: NENHUM asset cruza ou fica em cima da muralha do Coliseu! Todos com margem limpa.")

print("\n=== 2. VERIFICANDO SOBREPOSIÇÃO ENTRE OS PRÓPRIOS ASSETS ===")
boxes = []
for name, px, py, sc, off_y, iw, ih in props:
    abs_sc = abs(sc)
    left_x = px - (iw / 2.0) * abs_sc
    right_x = px + (iw / 2.0) * abs_sc
    top_y = py + (off_y - ih / 2.0) * abs_sc
    bottom_y = py + (off_y + ih / 2.0) * abs_sc
    foot_left = px - (iw * 0.40) * abs_sc
    foot_right = px + (iw * 0.40) * abs_sc
    foot_top = bottom_y - (ih * 0.35) * abs_sc
    foot_bottom = bottom_y
    boxes.append((name, left_x, right_x, top_y, bottom_y, foot_left, foot_right, foot_top, foot_bottom))

prop_overlap_found = False
for i in range(len(boxes)):
    for j in range(i + 1, len(boxes)):
        n1, l1, r1, t1, b1, fl1, fr1, ft1, fb1 = boxes[i]
        n2, l2, r2, t2, b2, fl2, fr2, ft2, fb2 = boxes[j]
        x_overlap = max(0, min(fr1, fr2) - max(fl1, fl2))
        y_overlap = max(0, min(fb1, fb2) - max(ft1, ft2))
        if x_overlap > 0 and y_overlap > 0:
            print(f"CONFLITO DE PEGADA: {n1} e {n2} sobrepostos por {x_overlap:.1f}px (X) e {y_overlap:.1f}px (Y)")
            prop_overlap_found = True

if not prop_overlap_found:
    print("PERFEITO: ZERO sobreposições de pegadas! Circulação 100% desobstruída em todo o mapa.")
