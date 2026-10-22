from PIL import Image, ImageFilter, ImageDraw
import numpy as np
import os
import shutil

BRAIN_DIR = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b"
DEST_STANDALONE = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\rails"
DEST_ROOT = r"c:\Users\Usuario\Documents\jogo\assets\rails"

print("--- PIPELINE DE ENGENHARIA: TÚNEL V2 + ESTAÇÃO V2 ALINHADOS ---")

# 1. CARREGAR PEÇAS BASE
img_trilho_base = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")
# Dimensões do trilho vertical base: 745x982. Centro dos trilhos: X=371.0, Bitola: 302.0 px.

img_tunel_base = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png').convert("RGBA")
# Dimensões: 1024x1024. Centro do portal de pedra: X=518.0.

# Carregar candidato 3 da estação gerado pelo Nano Banana
cand3_path = os.path.join(BRAIN_DIR, "estacao_trilho_v2_cand3_1791580289327.jpg")
img_cand3 = Image.open(cand3_path).convert("RGBA")

# Pós-processar Candidato 3 (despill e transparência)
arr_c3 = np.array(img_cand3, dtype=np.float32)
r, g, b = arr_c3[:, :, 0], arr_c3[:, :, 1], arr_c3[:, :, 2]
dist_mag = np.sqrt((r - 255)**2 + g**2 + (b - 255)**2)
is_magenta = (dist_mag < 155) | ((r > 160) & (b > 160) & (g < 110))
alpha_c3 = np.where(is_magenta, 0, 255).astype(np.uint8)
mask_c3 = Image.fromarray(alpha_c3, mode="L").filter(ImageFilter.MinFilter(3))

# Despill
is_fringe = (r > g + 20) & (b > g + 20)
arr_c3[:, :, 0][is_fringe] = np.minimum(r[is_fringe], g[is_fringe] + 15)
arr_c3[:, :, 2][is_fringe] = np.minimum(b[is_fringe], g[is_fringe] + 15)
arr_c3[:, :, 3] = np.array(mask_c3)
clean_cand3 = Image.fromarray(arr_c3.astype(np.uint8), mode="RGBA")
clean_cand3.save('scratch/cand3_clean.png')

# 2. ISOLAR A PLATAFORMA LATERAL DO CANDIDATO 3
# No candidato 3, a plataforma está do lado esquerdo (X de 0 até ~480)
# Vamos recortar apenas a plataforma lateral (com o guincho, coluna de pedra, lanterna e para-choque)
arr_clean = np.array(clean_cand3)
# O trilho do candidato 3 começa em torno de X ~ 460
# Vamos pegar a plataforma de X=0 a X=485
platform_arr = arr_clean[:, :485, :].copy()
platform_img = Image.fromarray(platform_arr, mode="RGBA")
platform_img.save('scratch/platform_isolated.png')
print("Plataforma lateral isolada com sucesso.")

# 3. CONSTRUIR ESTACAO_TRILHO_V2 (MÓDULO DE LIGAÇÃO PERFEITO)
# Vamos usar o trilho reto vertical mestre como espinha dorsal!
# O trilho tem largura 745 e altura 982.
# Vamos pegar uma seção de trilho ou o trilho completo redimensionado para a escala exata da estação.
# No mundo do jogo:
# O vão livre vertical é de 161.8 px de mundo.
# Com escala de 0.20 (igual à da ponte do trilho):
# Altura em pixels de imagem necessária = 161.8 / 0.20 = 809 px!
# Vamos compor a estação com o trilho mestre cortado exatamente no ciclo dos dormentes (altura ~810 px),
# e acoplar a plataforma lateral ao lado esquerdo do trilho!

# Trilho mestre: recortar fatia contínua de 810 px de altura
# O trilho tem dormentes periódicos a cada ~120 px.
# 810 px = exatamente ~7 dormentes!
crop_rail = img_trilho_base.crop((0, 0, 745, 810))

# Redimensionar a plataforma lateral para altura de 810 px
w_plat = int(platform_img.width * (810 / platform_img.height))
platform_scaled = platform_img.resize((w_plat, 810), Image.Resampling.BILINEAR)

# Canvas da Estação V2:
# Largura = plataforma + trilho
station_canvas_w = w_plat + 745 - 120 # leve sobreposição na borda externa dos dormentes
station_canvas = Image.new("RGBA", (station_canvas_w, 810), (0, 0, 0, 0))

# Colar a plataforma à esquerda
station_canvas.paste(platform_scaled, (0, 0), platform_scaled)
# Colar o trilho à direita da plataforma
# Trilho começa em X = w_plat - 120
station_canvas.paste(crop_rail, (w_plat - 120, 0), crop_rail)

# Salvar Estação V2
station_canvas.save(os.path.join(DEST_STANDALONE, "estacao_trilho_v2.png"))
station_canvas.save(os.path.join(DEST_ROOT, "estacao_trilho_v2.png"))

# Gerar sombra suave da estação
s_arr = np.array(station_canvas)
s_alpha = Image.fromarray(s_arr[:, :, 3], mode="L").filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(8))
s_rgba = np.zeros_like(s_arr, dtype=np.uint8)
s_rgba[:, :, 3] = (np.array(s_alpha, dtype=np.float32) * 0.50).astype(np.uint8)
Image.fromarray(s_rgba, mode="RGBA").save(os.path.join(DEST_STANDALONE, "estacao_trilho_v2_sombra.png"))
Image.fromarray(s_rgba, mode="RGBA").save(os.path.join(DEST_ROOT, "estacao_trilho_v2_sombra.png"))
print("Estação V2 salva e sincronizada.")

# 4. CONSTRUIR TUNEL_MINA_NORTE_V2 (COM TRILHOS NO CENTRO EXATO)
# No túnel original:
# A alvenaria do portal e as vigas de madeira vão de Y=0 a Y=800.
# A escuridão interna fica no centro X=518.
# Vamos pegar a moldura de alvenaria e rocha do túnel (com a lanterna e a escuridão),
# e projetar os trilhos mestres saindo perfeitamente no centro X=518 com a mesma bitola (302 px):
tunel_v2 = img_tunel_base.copy()
# Na base (Y de 750 a 1024), substituir os trilhos tortos pelos trilhos mestres centralizados em X=518:
# Pegar ponta do trilho mestre:
rail_exit = img_trilho_base.crop((0, 0, 745, 274)) # 274 px de altura
# O trilho mestre tem centro em X=371.
# Queremos que o centro fique em X=518 no túnel (1024x1024):
# X_paste = 518 - 371 = 147!
# Mas antes de colar, vamos limpar a base do túnel antigo com máscara suave de sombra/rocha
# e colar o trilho de saída perfeitamente alinhado:
draw_mask = Image.new("L", (1024, 1024), 0)
draw_mask_d = ImageDraw.Draw(draw_mask)
draw_mask_d.rectangle([150, 750, 880, 1024], fill=255)

# Limpar área inferior do túnel antigo com a escuridão da mina e chão de rocha
arr_tv2 = np.array(tunel_v2)
# Colar trilho de saída com blending na escuridão
tunel_v2.paste(rail_exit, (147, 750), rail_exit)

tunel_v2.save(os.path.join(DEST_STANDALONE, "tunel_mina_norte_v2.png"))
tunel_v2.save(os.path.join(DEST_ROOT, "tunel_mina_norte_v2.png"))

# Sombra do túnel V2
t_arr = np.array(tunel_v2)
t_alpha = Image.fromarray(t_arr[:, :, 3], mode="L").filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(8))
t_rgba = np.zeros_like(t_arr, dtype=np.uint8)
t_rgba[:, :, 3] = (np.array(t_alpha, dtype=np.float32) * 0.50).astype(np.uint8)
Image.fromarray(t_rgba, mode="RGBA").save(os.path.join(DEST_STANDALONE, "tunel_mina_norte_v2_sombra.png"))
Image.fromarray(t_rgba, mode="RGBA").save(os.path.join(DEST_ROOT, "tunel_mina_norte_v2_sombra.png"))
print("Túnel V2 salvo e sincronizado.")
