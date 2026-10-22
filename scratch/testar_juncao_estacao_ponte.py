from PIL import Image

img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png').convert("RGBA")
img_trilho_ponte = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")
img_cavalete = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png').convert("RGBA")

# Posições atuais:
# Estacao: Vector2(-215.9, 325.0), scale = 0.20
# Cavalete: Vector2(-190, 560.0), scale = 0.32
# Trilho Ponte: Vector2(-190 + 0, 560 - 75) = Vector2(-190, 485.0), scale = 0.20

zoom = 2.0
vp_w, vp_h = 500, 600
canvas = Image.new("RGBA", (vp_w, vp_h), (35, 35, 40, 255))

# Câmera centrada na junção: (-190, 406.0)
cam_x, cam_y = -190.0, 406.0

def w2s(wx, wy):
    return int((wx - cam_x) * zoom + vp_w / 2.0), int((wy - cam_y) * zoom + vp_h / 2.0)

# 1. Cavalete da ponte (fundo)
cw = int(img_cavalete.width * 0.32 * zoom)
ch = int(img_cavalete.height * 0.32 * zoom)
c_res = img_cavalete.resize((cw, ch), Image.Resampling.LANCZOS)
csx, csy = w2s(-190.0 - img_cavalete.width * 0.32 / 2.0, 560.0 - img_cavalete.height * 0.32 / 2.0)
canvas.paste(c_res, (csx, csy), c_res)

# 2. Trilho da ponte
pw = int(img_trilho_ponte.width * 0.20 * zoom)
ph = int(img_trilho_ponte.height * 0.20 * zoom)
p_res = img_trilho_ponte.resize((pw, ph), Image.Resampling.LANCZOS)
psx, psy = w2s(-190.0 - img_trilho_ponte.width * 0.20 / 2.0, 485.0 - img_trilho_ponte.height * 0.20 / 2.0)
canvas.paste(p_res, (psx, psy), p_res)

# 3. Estação (topo)
ew = int(img_est.width * 0.20 * zoom)
eh = int(img_est.height * 0.20 * zoom)
e_res = img_est.resize((ew, eh), Image.Resampling.LANCZOS)
esx, esy = w2s(-215.9 - img_est.width * 0.20 / 2.0, 325.0 - img_est.height * 0.20 / 2.0)
canvas.paste(e_res, (esx, esy), e_res)

canvas.save('scratch/teste_juncao_estacao_ponte.png')
print("Salvo scratch/teste_juncao_estacao_ponte.png")
