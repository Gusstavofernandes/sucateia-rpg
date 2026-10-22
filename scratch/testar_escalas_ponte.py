from PIL import Image, ImageDraw, ImageFont
import numpy as np

img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png').convert("RGBA")
img_trilho_ponte = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")
img_cavalete = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png').convert("RGBA")

# Posição da estação (fixa):
# Vector2(-215.9, 325.0), scale = 0.20
# A base da estação no mundo é Y = 325.0 + 810*0.20/2 = 406.0 px

zoom = 2.0
vp_w, vp_h = 500, 600

# Vamos testar fatores de escala sobre a escala base 0.20:
# Fator 1.1315 -> escala = 0.20 * 1.1315 = 0.2263
# Fator 1.18 -> escala = 0.236
# Fator 1.25 -> escala = 0.250

escalas_para_testar = [1.00, 1.1315, 1.18, 1.25]

for fator in escalas_para_testar:
    canvas = Image.new("RGBA", (vp_w, vp_h), (35, 35, 40, 255))
    cam_x, cam_y = -190.0, 406.0
    
    def w2s(wx, wy):
        return int((wx - cam_x) * zoom + vp_w / 2.0), int((wy - cam_y) * zoom + vp_h / 2.0)
        
    escala_trilho = 0.20 * fator
    escala_cavalete = 0.32 * fator # escala uniforme do conjunto da ponte
    
    # Queremos que o centro dos trilhos da ponte caia exatamente no mesmo X do centro da estação!
    # Centro da estação no mundo = -190.5 px
    # Centro do trilho da ponte na textura = 368.5 px (meio da textura 745 px, offset = 368.5 - 372.5 = -4.0 px)
    # Offset no mundo = -4.0 * escala_trilho
    # pos_x_trilho_mundo = -190.5 - (-4.0 * escala_trilho) = -190.5 + 4.0 * escala_trilho
    pos_x_ponte = -190.5 + 4.0 * escala_trilho
    
    # Posição Y da ponte:
    # A estação termina em Y = 406.0 px.
    # O topo dos trilhos da ponte (primeira linha opaca na textura = 2, meio da textura = 491)
    # Distância do centro da textura ao topo = (491 - 2) * escala_trilho = 489 * escala_trilho
    # Para o topo dos trilhos da ponte encostar exatamente em Y = 406.0 px:
    # pos_y_trilho = 406.0 + 489 * escala_trilho
    # E vamos permitir uma sobreposição de 1-2 dormentes para ritmo contínuo se necessário:
    # Vamos posicionar de modo que as pontas de ferro encostem suavemente
    pos_y_trilho = 406.0 + 475 * escala_trilho
    
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
    
    out_name = f"scratch/teste_ponte_fator_{int(fator*100)}.png"
    canvas.save(out_name)
    print(f"Salvo {out_name} para fator {fator}")
