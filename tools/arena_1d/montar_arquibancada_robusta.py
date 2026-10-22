"""Montagem da Arquibancada Norte Robusta e Antiga (Fase 1D).
Usa texturas pintadas reais do jogo:
  - Espelhos dos degraus: blocos de pedra antiga esculpida e chapas de ferro rebitadas (de fundo_wall.png e test_muro_cut.png).
  - Assentos e pranchas: tábuas de madeira maciça envelhecida e cantoneiras de ferro (de short_service_catwalk.png e bench.png).
  - 3 degraus escalonados (cotas +96, +112, +128).
  - Módulo de 256 x 384 px com tiling horizontal perfeito (0 px de descontinuidade).
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

DIR_ASSETS = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets"
OUT_STANDALONE = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props\arena_plateia_bancada_modulo_v1.png"
OUT_ROOT       = r"c:\Users\Usuario\Documents\jogo\assets\props\arena_plateia_bancada_modulo_v1.png"

# Carregar imagens fonte com texturas pintadas de alta resolução
im_wall = Image.open(os.path.join(DIR_ASSETS, "fundo_wall.png")).convert("RGBA")
im_catwalk = Image.open(os.path.join(DIR_ASSETS, "short_service_catwalk.png")).convert("RGBA")
im_bench = Image.open(os.path.join(DIR_ASSETS, "bench.png")).convert("RGBA")
im_muro = Image.open(r"c:\Users\Usuario\Documents\jogo\tools\arena_1c\test_muro_cut.png").convert("RGBA")

# Recortes de textura
# 1. Pedra antiga e ferro do muro (espelho vertical do degrau)
stone_riser = im_muro.crop((280, 250, 800, 450)).resize((256, 48), Image.LANCZOS)
# 2. Prancha de madeira grossa do catwalk (assento do degrau)
wood_seat = im_catwalk.crop((300, 200, 900, 450)).resize((256, 80), Image.LANCZOS)
# 3. Cantoneira com rebites
angle_iron = im_muro.crop((260, 52, 900, 110)).resize((256, 16), Image.LANCZOS)

# Criar imagem final da arquibancada (256 x 384 px)
im_bleacher = Image.new("RGBA", (256, 384), (0, 0, 0, 0))

# 3 degraus escalonados:
# Degrau 3 (ao fundo, cota +128): Y = 0..128 (assento 0..80, espelho 80..128)
# Degrau 2 (meio, cota +112): Y = 128..256 (assento 128..208, espelho 208..256)
# Degrau 1 (frente, cota +96): Y = 256..384 (assento 256..336, espelho 336..384)

tiers = [
    (0, 80, 128, 0.75),    # Degrau 3 (+128) - mais escuro / fundo
    (128, 208, 256, 0.88), # Degrau 2 (+112)
    (256, 336, 384, 1.0)   # Degrau 1 (+96) - iluminação plena
]

for seat_y0, seat_y1, riser_y1, bright in tiers:
    # Espelho de pedra e ferro
    riser = ImageEnhance.Brightness(stone_riser).enhance(bright * 0.9)
    im_bleacher.alpha_composite(riser.resize((256, riser_y1 - seat_y1)), (0, seat_y1))
    
    # Assento de tábuas de madeira maciça
    seat = ImageEnhance.Brightness(wood_seat).enhance(bright)
    im_bleacher.alpha_composite(seat.resize((256, seat_y1 - seat_y0)), (0, seat_y0))
    
    # Borda de cantoneira metálica com parafusos entre o assento e o espelho
    edge = ImageEnhance.Brightness(angle_iron).enhance(bright * 1.1)
    im_bleacher.alpha_composite(edge, (0, seat_y1 - 8))
    
    # Suportes verticais de ferro rebitado cravados na pedra
    d = ImageDraw.Draw(im_bleacher)
    for bx in (24, 128, 232):
        d.rectangle([bx - 6, seat_y0 + 10, bx + 6, riser_y1 - 2], fill=(30, 24, 18, 220), outline=(15, 12, 10, 255), width=1)
        d.ellipse([bx - 3, seat_y1 - 4, bx + 3, seat_y1 + 2], fill=(140, 110, 80, 255))
        d.ellipse([bx - 3, riser_y1 - 12, bx + 3, riser_y1 - 6], fill=(140, 110, 80, 255))

# Tiling horizontal perfeito (mistura suave de 16 px nas bordas)
arr = np.array(im_bleacher).astype(np.float32)
seam = 16
for i in range(seam):
    alpha = i / float(seam)
    avg = arr[:, i, :] * (1 - alpha) + arr[:, 255 - seam + i, :] * alpha
    arr[:, i, :] = avg
    arr[:, 255 - seam + i, :] = avg

im_final = Image.fromarray(arr.clip(0, 255).astype(np.uint8))

# Salvar nas pastas
im_final.save(OUT_STANDALONE)
im_final.save(OUT_ROOT)

# Gerar sombra de contato
sh = Image.new("RGBA", (256, 384), (0, 0, 0, 0))
d_sh = ImageDraw.Draw(sh)
d_sh.rectangle([0, 368, 255, 382], fill=(10, 8, 6, 130))
sh = sh.filter(ImageFilter.GaussianBlur(radius=4))
sh.save(OUT_STANDALONE.replace(".png", "_sombra.png"))
sh.save(OUT_ROOT.replace(".png", "_sombra.png"))

print("Nova arquibancada robusta salva com sucesso em:")
print("  -", OUT_STANDALONE)
print("  -", OUT_ROOT)
