from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Carregar imagens
img_tunel = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png').convert("RGBA")
img_trilho = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")
img_cavalete = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png').convert("RGBA")

# Vamos montar um canvas no espaço de mundo do jogo:
# Coordenadas de mundo:
# X vai de -400 a 0 (largura 400 px de mundo)
# Y vai de 100 a 700 (altura 600 px de mundo)
# Vamos usar resolução 2x para visualização nítida (1 unidade de mundo = 2 pixels no canvas)
scale_canvas = 2

world_origin_x = -380.0
world_origin_y = 100.0

canvas_w = int((0.0 - world_origin_x) * scale_canvas)
canvas_h = int((700.0 - world_origin_y) * scale_canvas)

canvas = Image.new("RGBA", (canvas_w, canvas_h), (25, 25, 30, 255))

def world_to_canvas(wx, wy):
    cx = int((wx - world_origin_x) * scale_canvas)
    cy = int((wy - world_origin_y) * scale_canvas)
    return cx, cy

# 1. Desenhar o túnel no canvas:
# Tunel: pos=(-190, 150), scale=(0.26, 0.26), size=(1024, 1024)
w_t_scaled = int(1024 * 0.26 * scale_canvas)
h_t_scaled = int(1024 * 0.26 * scale_canvas)
tunel_resized = img_tunel.resize((w_t_scaled, h_t_scaled), Image.Resampling.BILINEAR)

cx_t, cy_t = world_to_canvas(-190.0, 150.0)
top_left_t = (cx_t - w_t_scaled // 2, cy_t - h_t_scaled // 2)
canvas.paste(tunel_resized, top_left_t, tunel_resized)

# 2. Desenhar o cavalete e trilhos da ponte no canvas:
# Cavalete: pos=(-190, 560), scale=(0.32, 0.32), size=(770, 995)
w_c_scaled = int(770 * 0.32 * scale_canvas)
h_c_scaled = int(995 * 0.32 * scale_canvas)
cavalete_resized = img_cavalete.resize((w_c_scaled, h_c_scaled), Image.Resampling.BILINEAR)
cx_c, cy_c = world_to_canvas(-190.0, 560.0)
top_left_c = (cx_c - w_c_scaled // 2, cy_c - h_c_scaled // 2)
canvas.paste(cavalete_resized, top_left_c, cavalete_resized)

# Trilhos da ponte: pos=(-190, 530), scale=(0.20, 0.20), size=(745, 982)
w_r_scaled = int(745 * 0.20 * scale_canvas)
h_r_scaled = int(982 * 0.20 * scale_canvas)
trilho_resized = img_trilho.resize((w_r_scaled, h_r_scaled), Image.Resampling.BILINEAR)
cx_r, cy_r = world_to_canvas(-190.0, 530.0)
top_left_r = (cx_r - w_r_scaled // 2, cy_r - h_r_scaled // 2)
canvas.paste(trilho_resized, top_left_r, trilho_resized)

# 3. Desenhar guias de debug:
draw = ImageDraw.Draw(canvas)

# Guia Túnel:
# Centro X túnel = -208.20
# Bitola túnel = 87.10 -> trilho esquerdo = -208.20 - 43.55 = -251.75, trilho direito = -164.65
# Y bottom túnel = 270.38
cx_tunel_center, cy_tunel_bottom = world_to_canvas(-208.20, 270.38)
cx_tunel_left, _ = world_to_canvas(-251.75, 270.38)
cx_tunel_right, _ = world_to_canvas(-164.65, 270.38)

# Linhas verticais do túnel projetadas para baixo:
draw.line([(cx_tunel_center, cy_tunel_bottom - 100), (cx_tunel_center, cy_tunel_bottom + 160)], fill=(255, 60, 60, 255), width=2)
draw.line([(cx_tunel_left, cy_tunel_bottom - 50), (cx_tunel_left, cy_tunel_bottom + 160)], fill=(0, 255, 255, 255), width=2)
draw.line([(cx_tunel_right, cy_tunel_bottom - 50), (cx_tunel_right, cy_tunel_bottom + 160)], fill=(0, 255, 255, 255), width=2)

# Guia Ponte:
# Centro X ponte = -190.30
# Bitola ponte = 60.40 -> trilho esquerdo = -190.30 - 30.20 = -220.50, trilho direito = -160.10
# Y top ponte = 432.20
cx_ponte_center, cy_ponte_top = world_to_canvas(-190.30, 432.20)
cx_ponte_left, _ = world_to_canvas(-220.50, 432.20)
cx_ponte_right, _ = world_to_canvas(-160.10, 432.20)

# Linhas verticais da ponte projetadas para cima:
draw.line([(cx_ponte_center, cy_ponte_top - 160), (cx_ponte_center, cy_ponte_top + 100)], fill=(255, 220, 0, 255), width=2)
draw.line([(cx_ponte_left, cy_ponte_top - 160), (cx_ponte_left, cy_ponte_top + 50)], fill=(50, 255, 50, 255), width=2)
draw.line([(cx_ponte_right, cy_ponte_top - 160), (cx_ponte_right, cy_ponte_top + 50)], fill=(50, 255, 50, 255), width=2)

# Legenda e medições no canvas
draw.text((20, 20), "DEBUG OVERLAY - ALINHAMENTO TUNEL VS PONTE", fill=(255, 255, 255, 255))
draw.text((20, 45), f"TUNEL (Topo): Centro X = -208.2 px | Bitola = 87.1 px (Linhas Ciano/Vermelho)", fill=(0, 255, 255, 255))
draw.text((20, 70), f"PONTE (Base): Centro X = -190.3 px | Bitola = 60.4 px (Linhas Verde/Amarelo)", fill=(50, 255, 50, 255))
draw.text((20, 95), f"DISCREPANCIA: Bitola difere em 26.7 px | Centro X difere em 17.9 px", fill=(255, 80, 80, 255))
draw.text((20, 120), f"VAO VERTICAL LIVRE = 161.8 px", fill=(200, 200, 200, 255))

out_path = 'fundo_ferro_standalone/assets/rails/debug_overlay_tunel_ponte_medicoes.png'
canvas.save(out_path)
canvas.save('C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/debug_overlay_tunel_ponte_medicoes.png')
print("Salvo debug overlay em:", out_path)
