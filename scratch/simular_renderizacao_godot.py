from PIL import Image

img_tunel = Image.open('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png').convert("RGBA")
img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png').convert("RGBA")

# Posições no Godot:
# Tunel: pos = (-190.41, 128.34), scale = 0.39021
# Estacao: pos = (-215.9, 325.0), scale = 0.20

# Vamos criar uma imagem de canvas em escala do mundo (ex: 2x para nitidez)
zoom = 2.5
# Origem da câmera de captura: (-190, 244)
# Tamanho da viewport: 1280 x 720
vp_w, vp_h = 1280, 720
canvas = Image.new("RGBA", (vp_w, vp_h), (50, 50, 50, 255))

cam_x, cam_y = -190.0, 244.0

def world_to_screen(wx, wy):
    sx = int((wx - cam_x) * zoom + vp_w / 2.0)
    sy = int((wy - cam_y) * zoom + vp_h / 2.0)
    return sx, sy

# 1. Colar Estação
# Estação nó em (-215.9, 325.0), sprite escala 0.20
# Sprite top-left no mundo: (-215.9 - 1008*0.20/2, 325.0 - 810*0.20/2) = (-316.7, 244.0)
est_resized = img_est.resize((int(img_est.width * 0.20 * zoom), int(img_est.height * 0.20 * zoom)), Image.Resampling.LANCZOS)
est_sx, est_sy = world_to_screen(-215.9 - img_est.width * 0.20 / 2.0, 325.0 - img_est.height * 0.20 / 2.0)
canvas.paste(est_resized, (est_sx, est_sy), est_resized)

# 2. Colar Túnel
# Tunel nó em (-190.41, 128.34), sprite escala 0.39021
tun_resized = img_tunel.resize((int(img_tunel.width * 0.39021 * zoom), int(img_tunel.height * 0.39021 * zoom)), Image.Resampling.LANCZOS)
tun_sx, tun_sy = world_to_screen(-190.41 - img_tunel.width * 0.39021 / 2.0, 128.34 - img_tunel.height * 0.39021 / 2.0)
canvas.paste(tun_resized, (tun_sx, tun_sy), tun_resized)

canvas.save('scratch/simulacao_godot.png')
print(f"Estação screen top: {est_sy}")
print(f"Túnel screen bottom: {tun_sy + tun_resized.height}")
print(f"Diferença na tela: {est_sy - (tun_sy + tun_resized.height)} px")
