from PIL import Image

img_tunel = Image.open('fundo_ferro_standalone/assets/rails/boca_tunel_v2.png').convert("RGBA")
img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png').convert("RGBA")

# Vamos testar valores de pos_y para o túnel:
# 128.34, 138.34, 145.0, 150.0, 155.0
escala_tun = 0.39021
tun_pos_x = -190.41
est_pos_x = -215.9
est_pos_y = 325.0
escala_est = 0.20

zoom = 2.0
vp_w, vp_h = 400, 500

for test_y in [128.34, 135.0, 142.0, 148.0, 155.0]:
    canvas = Image.new("RGBA", (vp_w, vp_h), (35, 35, 40, 255))
    cam_x, cam_y = -190.0, 244.0
    
    def w2s(wx, wy):
        return int((wx - cam_x) * zoom + vp_w / 2.0), int((wy - cam_y) * zoom + vp_h / 2.0)
        
    # Colar túnel primeiro (z-order inferior)
    tw = int(img_tunel.width * escala_tun * zoom)
    th = int(img_tunel.height * escala_tun * zoom)
    t_res = img_tunel.resize((tw, th), Image.Resampling.LANCZOS)
    tsx, tsy = w2s(tun_pos_x - img_tunel.width * escala_tun / 2.0, test_y - img_tunel.height * escala_tun / 2.0)
    canvas.paste(t_res, (tsx, tsy), t_res)
    
    # Colar estação por cima (z-order superior na junção)
    ew = int(img_est.width * escala_est * zoom)
    eh = int(img_est.height * escala_est * zoom)
    e_res = img_est.resize((ew, eh), Image.Resampling.LANCZOS)
    esx, esy = w2s(est_pos_x - img_est.width * escala_est / 2.0, est_pos_y - img_est.height * escala_est / 2.0)
    canvas.paste(e_res, (esx, esy), e_res)
    
    out_name = f"scratch/teste_emenda_y_{int(test_y)}.png"
    canvas.save(out_name)
    print(f"Salvo {out_name} para test_y = {test_y}")
