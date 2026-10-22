from PIL import Image

img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png').convert("RGBA")
img_trilho_ponte = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")
img_cavalete = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png').convert("RGBA")

zoom = 2.0
vp_w, vp_h = 500, 600

fator = 1.25
escala_trilho = 0.20 * fator
escala_cavalete = 0.32 * fator

# Posição base anterior da ponte: pos_x_ponte = -190.5 + 4.0 * escala_trilho = -189.5 px
# No canvas do teste (zoom 2.0x), cada 1 px no mundo são 2 px na tela.
# O usuário pediu "coloque mais 3px".
# Vamos testar shifts em X na tela de +2px, +3px, +4px (equivalente a +1.0px, +1.5px, +2.0px no mundo)
# E em Y, fechar a emenda (offset_y em torno de 22 a 28 px no mundo)

for shift_screen_x in [2, 3, 4]:
    shift_world_x = shift_screen_x / zoom
    pos_x_ponte = (-190.5 + 4.0 * escala_trilho) + shift_world_x
    
    for offset_y in [22, 25, 28]:
        canvas = Image.new("RGBA", (vp_w, vp_h), (35, 35, 40, 255))
        cam_x, cam_y = -190.0, 406.0
        
        def w2s(wx, wy):
            return int((wx - cam_x) * zoom + vp_w / 2.0), int((wy - cam_y) * zoom + vp_h / 2.0)
            
        pos_y_trilho = 406.0 + 475 * escala_trilho - offset_y
        
        # 1. Cavalete da ponte (fundo)
        cw = int(img_cavalete.width * escala_cavalete * zoom)
        ch = int(img_cavalete.height * escala_cavalete * zoom)
        c_res = img_cavalete.resize((cw, ch), Image.Resampling.LANCZOS)
        csx, csy = w2s(pos_x_ponte - img_cavalete.width * escala_cavalete / 2.0, pos_y_trilho + 75.0*fator - img_cavalete.height * escala_cavalete / 2.0)
        canvas.paste(c_res, (csx, csy), c_res)
        
        # 2. Trilho da ponte
        pw = int(img_trilho_ponte.width * escala_trilho * zoom)
        ph = int(img_trilho_ponte.height * escala_trilho * zoom)
        p_res = img_trilho_ponte.resize((pw, ph), Image.Resampling.LANCZOS)
        psx, psy = w2s(pos_x_ponte - img_trilho_ponte.width * escala_trilho / 2.0, pos_y_trilho - img_trilho_ponte.height * escala_trilho / 2.0)
        canvas.paste(p_res, (psx, psy), p_res)
        
        # 3. Estação (topo)
        ew = int(img_est.width * 0.20 * zoom)
        eh = int(img_est.height * 0.20 * zoom)
        e_res = img_est.resize((ew, eh), Image.Resampling.LANCZOS)
        esx, esy = w2s(-215.9 - img_est.width * 0.20 / 2.0, 325.0 - img_est.height * 0.20 / 2.0)
        canvas.paste(e_res, (esx, esy), e_res)
        
        out_name = f"scratch/calibrado_x{shift_screen_x}_y{offset_y}.png"
        canvas.save(out_name)

print("Imagens de calibração geradas com sucesso!")
