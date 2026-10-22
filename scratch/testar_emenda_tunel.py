from PIL import Image, ImageDraw
import numpy as np

img_tunel = Image.open('scratch/boca_tunel_v2_raw_cut.png').convert("RGBA")
img_estacao = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png').convert("RGBA")

# Escalas:
scale_tunel = 60.40 / 143.0 # = 0.4223776
scale_estacao = 0.20

print(f"Escala Túnel: {scale_tunel:.6f}")
print(f"Escala Estação: {scale_estacao:.6f}")

# Montar canvas de teste da emenda em escala 2x do mundo
scale_canvas = 2.0
world_origin_x = -350.0
world_origin_y = 50.0

canvas_w = int((0.0 - world_origin_x) * scale_canvas)
canvas_h = int((450.0 - world_origin_y) * scale_canvas)
canvas = Image.new("RGBA", (canvas_w, canvas_h), (20, 22, 26, 255))

def w2c(wx, wy):
    return int((wx - world_origin_x) * scale_canvas), int((wy - world_origin_y) * scale_canvas)

# 1. Colar Estação
# pos no mundo = (-215.9, 325.0)
pos_est_x, pos_est_y = -215.9, 325.0
w_e = int(img_estacao.width * scale_estacao * scale_canvas)
h_e = int(img_estacao.height * scale_estacao * scale_canvas)
e_resized = img_estacao.resize((w_e, h_e), Image.Resampling.BILINEAR)
cx_e, cy_e = w2c(pos_est_x, pos_est_y)
canvas.paste(e_resized, (cx_e - w_e//2, cy_e - h_e//2), e_resized)

# 2. Colar Túnel
# Base do túnel deve casar com topo da estação (Y = 244.0)
# Altura do túnel no mundo:
h_tunel_world = img_tunel.height * scale_tunel
# Para a base casar em 244.0:
pos_tunel_y = 244.0 - (h_tunel_world / 2.0)
# Para o centro dos trilhos casar em X = -190.0:
# Offset do centro dos trilhos na textura:
center_offset_tex = 501.5 - (img_tunel.width / 2.0) # = -0.5
pos_tunel_x = -190.0 - (center_offset_tex * scale_tunel)

w_t = int(img_tunel.width * scale_tunel * scale_canvas)
h_t = int(img_tunel.height * scale_tunel * scale_canvas)
t_resized = img_tunel.resize((w_t, h_t), Image.Resampling.BILINEAR)
cx_t, cy_t = w2c(pos_tunel_x, pos_tunel_y)
canvas.paste(t_resized, (cx_t - w_t//2, cy_t - h_t//2), t_resized)

# 3. Desenhar linhas guias de alinhamento
draw = ImageDraw.Draw(canvas)
# Centro: X = -190.0
cx_mid, _ = w2c(-190.0, 0)
# Trilho esquerdo: X = -190.0 - 30.2 = -220.2
cx_left, _ = w2c(-220.2, 0)
# Trilho direito: X = -190.0 + 30.2 = -159.8
cx_right, _ = w2c(-159.8, 0)

y_start = w2c(0, 100)[1]
y_end = w2c(0, 400)[1]

draw.line([(cx_mid, y_start), (cx_mid, y_end)], fill=(255, 50, 50, 255), width=2)
draw.line([(cx_left, y_start), (cx_left, y_end)], fill=(0, 255, 255, 255), width=2)
draw.line([(cx_right, y_start), (cx_right, y_end)], fill=(0, 255, 255, 255), width=2)

# Linha da emenda horizontal (Y = 244.0)
_, y_seam = w2c(0, 244.0)
draw.line([(w2c(-260, 0)[0], y_seam), (w2c(-120, 0)[0], y_seam)], fill=(255, 255, 0, 255), width=2)

canvas.save('scratch/teste_emenda_tunel_estacao.png')
print(f"Salvo scratch/teste_emenda_tunel_estacao.png!")
print(f"Parâmetros calculados do nó Tunel:")
print(f"  position = Vector2({pos_tunel_x:.2f}, {pos_tunel_y:.2f})")
print(f"  scale = Vector2({scale_tunel:.6f}, {scale_tunel:.6f})")
