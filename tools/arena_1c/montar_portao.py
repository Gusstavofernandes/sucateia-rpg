"""Montagem do Portao dos Lutadores (Fase 1C).
Folha corrediça: 64x112 de mundo (256x448 px).
Trilho superior: 128x32 de mundo (512x128 px) cobrindo os módulos k=3 a 5.
Estados completos (512x512 px):
  - Fechado: folha em X=0..256, contrapeso em baixo (Y=260).
  - Abrindo: folha em X=128..384, contrapeso subindo (Y=196).
  - Aberto: folha em X=256..512 (vão 0..256 100% livre), contrapeso no topo (Y=132).
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SRC_CUT = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c\test_portao_cut.png"
OUT_DIR = r"c:\Users\Usuario\Documents\jogo\tools\arena_1c"

cut = Image.open(SRC_CUT)

# 1. Extração e ajuste da folha
leaf_crop = cut.crop((240, 220, 805, 1145))
leaf = leaf_crop.resize((256, 448), Image.LANCZOS)

# 2. Extração e ajuste do trilho superior
rail_crop = cut.crop((69, 31, 803, 220))
rail = rail_crop.resize((512, 112), Image.LANCZOS)

# 3. Extração e ajuste do contrapeso com corrente
cw_crop = cut.crop((100, 250, 260, 700))
cw = cw_crop.resize((48, 160), Image.LANCZOS)

# Salvar folha e trilho separados
leaf.save(os.path.join(OUT_DIR, "arena_portao_folha_v1.png"))
rail.save(os.path.join(OUT_DIR, "arena_portao_trilho_v1.png"))

def build_gate_state(leaf_x, cw_y, name):
    # Canvas de 512 x 512 px (128x128 de mundo)
    canvas = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    
    # 1. Contrapeso (atrás do trilho e folha)
    # Roldana no topo direito
    canvas.alpha_composite(cw, (456, cw_y))
    
    # 2. Folha do portão
    canvas.alpha_composite(leaf, (leaf_x, 64))
    
    # 3. Trilho superior (na frente, segurando as roldanas)
    canvas.alpha_composite(rail, (0, 0))
    
    # Garantir 0 resíduo de magenta
    arr = np.array(canvas).astype(np.float32)
    r, g, b, a = arr[...,0], arr[...,1], arr[...,2], arr[...,3]
    mag_mask = (r > 150) & (b > 150) & (g < 100) & (a > 0)
    arr[mag_mask, 0] = arr[mag_mask, 1] * 1.1
    arr[mag_mask, 2] = arr[mag_mask, 1] * 0.9
    canvas = Image.fromarray(arr.clip(0, 255).astype(np.uint8))
    
    canvas.save(os.path.join(OUT_DIR, f"{name}.png"))
    print(f"Estado salvo: {name}.png, bbox={canvas.getbbox()}")
    return canvas

# Fechado: folha no vão 0..256, contrapeso baixo (y=260)
build_gate_state(0, 260, "arena_portao_lutadores_fechado_v1")

# Abrindo: folha em 128..384, contrapeso médio (y=196)
build_gate_state(128, 196, "arena_portao_lutadores_abrindo_v1")

# Aberto: folha em 256..512, contrapeso alto (y=132)
build_gate_state(256, 132, "arena_portao_lutadores_aberto_v1")

print("Portao dos lutadores montado com sucesso!")
