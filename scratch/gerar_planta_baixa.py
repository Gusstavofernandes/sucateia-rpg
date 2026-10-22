from PIL import Image, ImageDraw, ImageFont
import json

# Gerar imagem gráfica da Planta Baixa da Estação (Escala 1:1 do Mundo)
# Área: X de -400 a +300 (W=700), Y de 550 a 950 (H=400)
w_img, h_img = 700, 400
offset_x, offset_y = 400, -550

img_planta = Image.new("RGB", (w_img, h_img), (25, 25, 30)) # Piso de pedra escura
draw = ImageDraw.Draw(img_planta)

def world_to_img(wx, wy):
    return int(round(wx + offset_x)), int(round(wy + offset_y))

# 1. Desenhar Canal de Esgoto (ao norte, Y < 570)
c_x0, c_y0 = world_to_img(-400, 550)
c_x1, c_y1 = world_to_img(300, 570)
draw.rectangle([c_x0, c_y0, c_x1, c_y1], fill=(20, 45, 30), outline=(50, 70, 50)) # Água verde/esgoto
draw.text((c_x0 + 20, c_y0 + 5), "CANAL DE ESGOTO (Y=525 a 570)", fill=(100, 180, 120))

# Mureta do canal em Y=570
m_x0, m_y0 = world_to_img(-400, 568)
m_x1, m_y1 = world_to_img(300, 572)
draw.rectangle([m_x0, m_y0, m_x1, m_y1], fill=(70, 65, 60))

# 2. Ponte do Trilho descendo até Y=617
p_x0, p_y0 = world_to_img(-255, 550)
p_x1, p_y1 = world_to_img(-133, 617)
draw.rectangle([p_x0, p_y0, p_x1, p_y1], fill=(50, 40, 35), outline=(140, 110, 80))
draw.text((p_x0 + 10, p_y0 + 20), "PONTE DO TRILHO (Y->617)", fill=(200, 180, 140))
# Linhas dos trilhos na ponte
t_esq_0 = world_to_img(-247, 550)
t_esq_1 = world_to_img(-255, 617)
t_dir_0 = world_to_img(-140, 550)
t_dir_1 = world_to_img(-133, 617)
draw.line([t_esq_0, t_esq_1], fill=(0, 255, 255), width=2)
draw.line([t_dir_0, t_dir_1], fill=(0, 255, 255), width=2)

# 3. Peça A: Descarga Basculante (X: -307 a -83, Y: 617 a 745)
a_p0 = world_to_img(-307, 617)
a_p1 = world_to_img(-83, 745)
draw.rectangle([a_p0, a_p1], fill=(60, 45, 40), outline=(220, 160, 60), width=2)
draw.text((a_p0[0] + 15, a_p0[1] + 10), "DESCARGA BASCULANTE", fill=(255, 220, 100))
draw.text((a_p0[0] + 15, a_p0[1] + 25), "Boca Integrada + Para-Choque", fill=(200, 180, 150))
# Trilhos dentro da descarga até o batente Y=700
t_in_esq_0 = world_to_img(-255, 617)
t_in_esq_1 = world_to_img(-265, 700)
t_in_dir_0 = world_to_img(-133, 617)
t_in_dir_1 = world_to_img(-127, 700)
draw.line([t_in_esq_0, t_in_esq_1], fill=(0, 255, 255), width=2)
draw.line([t_in_dir_0, t_in_dir_1], fill=(0, 255, 255), width=2)
# Batente em Y=700
bat_0 = world_to_img(-270, 700)
bat_1 = world_to_img(-122, 704)
draw.rectangle([bat_0, bat_1], fill=(200, 50, 50))
draw.text((bat_0[0] + 20, bat_0[1] - 12), "BATENTE (Y=700)", fill=(255, 100, 100))

# 4. Peça B: Britadeira a Vapor (X: -75 a +53, Y: 625 a 753)
b_p0 = world_to_img(-75, 625)
b_p1 = world_to_img(53, 753)
draw.rectangle([b_p0, b_p1], fill=(55, 55, 65), outline=(100, 150, 220), width=2)
draw.text((b_p0[0] + 10, b_p0[1] + 15), "BRITADEIRA A VAPOR", fill=(140, 190, 255))
draw.text((b_p0[0] + 10, b_p0[1] + 30), "Mandíbulas + Volante", fill=(180, 180, 200))
# Calha de minério bruto entre A e B
c1_0 = world_to_img(-83, 675)
c1_1 = world_to_img(-75, 685)
draw.rectangle([c1_0, c1_1], fill=(180, 140, 50))

# 5. Peça C: Lavador-Decantador Conjugado (X: +65 a +193, Y: 615 a 743)
c_p0 = world_to_img(65, 615)
c_p1 = world_to_img(193, 743)
draw.rectangle([c_p0, c_p1], fill=(40, 60, 50), outline=(80, 220, 140), width=2)
draw.text((c_p0[0] + 8, c_p0[1] + 15), "LAVADOR-DECANTADOR", fill=(120, 255, 180))
draw.text((c_p0[0] + 8, c_p0[1] + 30), "Grelha + Tanque Cônico", fill=(160, 220, 190))
# Calha de minério britado entre B e C
c2_0 = world_to_img(53, 685)
c2_1 = world_to_img(65, 695)
draw.rectangle([c2_0, c2_1], fill=(120, 160, 80))

# Tubulação modular existente na parede (X=110 para leste em Y=643)
pipe_0 = world_to_img(110, 640)
pipe_1 = world_to_img(300, 646)
draw.rectangle([pipe_0, pipe_1], fill=(120, 90, 40), outline=(200, 160, 80))
draw.text((pipe_0[0] + 20, pipe_0[1] - 14), "CANO MODULAR (PassagemParedeOeste X=110, Y=643)", fill=(255, 200, 100))

# Conexão de efluente do Lavador-Decantador direto no cano modular!
ef_0 = world_to_img(108, 635)
ef_1 = world_to_img(112, 645)
draw.rectangle([ef_0, ef_1], fill=(0, 255, 0), width=2)

# 6. Peça D: Pilhas de Minério e Rejeito (X: +60 a +220, Y: 765 a 829)
d_p0 = world_to_img(60, 765)
d_p1 = world_to_img(220, 829)
draw.rectangle([d_p0, d_p1], fill=(30, 45, 35), outline=(160, 160, 120), width=1)
draw.text((d_p0[0] + 10, d_p0[1] + 10), "PILHAS: Minério Lavado e Rejeito", fill=(210, 210, 160))

# 7. Corredores de Manutenção (Linhas guias amarelas tracejadas)
# Corredor Oeste (largura 73 px)
cor_w_0 = world_to_img(-380, 600)
cor_w_1 = world_to_img(-307, 750)
draw.rectangle([cor_w_0, cor_w_1], outline=(255, 255, 0), width=1)
draw.text((cor_w_0[0] + 5, cor_w_0[1] + 50), "CORREDOR OESTE (73 px)", fill=(255, 255, 0))

# Corredor Norte (largura 45 px)
cor_n_0 = world_to_img(-75, 572)
cor_n_1 = world_to_img(193, 615)
draw.rectangle([cor_n_0, cor_n_1], outline=(255, 255, 0), width=1)
draw.text((cor_n_0[0] + 40, cor_n_0[1] + 15), "CORREDOR NORTE (45 px)", fill=(255, 255, 0))

# Corredor Sul (largura 91 px)
cor_s_0 = world_to_img(-350, 829)
cor_s_1 = world_to_img(250, 920)
draw.rectangle([cor_s_0, cor_s_1], outline=(255, 255, 0), width=1)
draw.text((cor_s_0[0] + 180, cor_s_0[1] + 35), "CORREDOR SUL LIVRE (91 px)", fill=(255, 255, 0))

# Salvar imagem da planta
img_planta.save("scratch/planta_baixa_estacao_mundo.png")
img_planta.save("C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/planta_baixa_estacao_mundo.png")
print("Planta baixa gerada e salva com sucesso!")
