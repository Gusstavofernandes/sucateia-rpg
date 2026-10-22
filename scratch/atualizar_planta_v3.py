from PIL import Image, ImageDraw

# Gerar imagem gráfica da Planta Baixa da Estação (Escala 1:1 do Mundo)
# Área: X de -400 a +300 (W=700), Y de 550 a 950 (H=400)
w_img, h_img = 700, 400
offset_x, offset_y = 400, -550

img_planta = Image.new("RGB", (w_img, h_img), (25, 25, 30))
draw = ImageDraw.Draw(img_planta)

def world_to_img(wx, wy):
    return int(round(wx + offset_x)), int(round(wy + offset_y))

# 1. Canal de Esgoto
c_x0, c_y0 = world_to_img(-400, 550)
c_x1, c_y1 = world_to_img(300, 570)
draw.rectangle([c_x0, c_y0, c_x1, c_y1], fill=(20, 45, 30), outline=(50, 70, 50))
draw.text((c_x0 + 20, c_y0 + 5), "CANAL DE ESGOTO (Y=525 a 570)", fill=(100, 180, 120))

# Mureta do canal
m_x0, m_y0 = world_to_img(-400, 568)
m_x1, m_y1 = world_to_img(300, 572)
draw.rectangle([m_x0, m_y0, m_x1, m_y1], fill=(70, 65, 60))

# 2. Ponte do Trilho descendo até Y=617
p_x0, p_y0 = world_to_img(-255, 550)
p_x1, p_y1 = world_to_img(-133, 617)
draw.rectangle([p_x0, p_y0, p_x1, p_y1], fill=(50, 40, 35), outline=(140, 110, 80))
draw.text((p_x0 + 10, p_y0 + 20), "PONTE DO TRILHO (Y->617)", fill=(200, 180, 140))
t_esq_0 = world_to_img(-247, 550)
t_esq_1 = world_to_img(-255, 617)
t_dir_0 = world_to_img(-140, 550)
t_dir_1 = world_to_img(-133, 617)
draw.line([t_esq_0, t_esq_1], fill=(0, 255, 255), width=2)
draw.line([t_dir_0, t_dir_1], fill=(0, 255, 255), width=2)

# 3. Peça 1: BOCA DE TRILHO (X: -307 a -83, Y: 617 a 681)
boca_0 = world_to_img(-307, 617)
boca_1 = world_to_img(-83, 681)
draw.rectangle([boca_0, boca_1], fill=(70, 50, 45), outline=(220, 180, 80), width=2)
draw.text((boca_0[0] + 15, boca_0[1] + 10), "BOCA DE TRILHO (Y=617 a 681)", fill=(255, 220, 120))
draw.text((boca_0[0] + 15, boca_0[1] + 25), "Moldura de Cantaria e Ferro", fill=(200, 180, 150))
t_boca_esq_0 = world_to_img(-255, 617)
t_boca_esq_1 = world_to_img(-263, 681)
t_boca_dir_0 = world_to_img(-133, 617)
t_boca_dir_1 = world_to_img(-128, 681)
draw.line([t_boca_esq_0, t_boca_esq_1], fill=(0, 255, 255), width=2)
draw.line([t_boca_dir_0, t_boca_dir_1], fill=(0, 255, 255), width=2)

# 4. Peça 2: DESCARGA BASCULANTE (X: -307 a -83, Y: 681 a 809)
desc_0 = world_to_img(-307, 681)
desc_1 = world_to_img(-83, 809)
draw.rectangle([desc_0, desc_1], fill=(55, 40, 35), outline=(220, 140, 50), width=2)
draw.text((desc_0[0] + 15, desc_0[1] + 10), "DESCARGA BASCULANTE (Y=681 a 809)", fill=(255, 180, 90))
draw.text((desc_0[0] + 15, desc_0[1] + 25), "Tombamento + Moega", fill=(200, 160, 130))
t_desc_esq_0 = world_to_img(-263, 681)
t_desc_esq_1 = world_to_img(-270, 745)
t_desc_dir_0 = world_to_img(-128, 681)
t_desc_dir_1 = world_to_img(-123, 745)
draw.line([t_desc_esq_0, t_desc_esq_1], fill=(0, 255, 255), width=2)
draw.line([t_desc_dir_0, t_desc_dir_1], fill=(0, 255, 255), width=2)
# Batente em Y=745
bat_0 = world_to_img(-275, 745)
bat_1 = world_to_img(-118, 750)
draw.rectangle([bat_0, bat_1], fill=(220, 50, 50))
draw.text((bat_0[0] + 20, bat_0[1] - 12), "BATENTE (Y=745)", fill=(255, 100, 100))

# 5. Peça 3: BRITADEIRA A VAPOR (X: -75 a +53, Y: 625 a 753)
b_p0 = world_to_img(-75, 625)
b_p1 = world_to_img(53, 753)
draw.rectangle([b_p0, b_p1], fill=(55, 55, 65), outline=(100, 150, 220), width=2)
draw.text((b_p0[0] + 10, b_p0[1] + 15), "BRITADEIRA A VAPOR", fill=(140, 190, 255))
draw.text((b_p0[0] + 10, b_p0[1] + 30), "Mandíbulas + Volante", fill=(180, 180, 200))
# Calha de minério bruto entre Descarga e Britadeira
c1_0 = world_to_img(-83, 695)
c1_1 = world_to_img(-75, 705)
draw.rectangle([c1_0, c1_1], fill=(180, 140, 50))

# 6. Peça 4: LAVADOR-DECANTADOR CONJUGADO (X: +65 a +193, Y: 615 a 743)
c_p0 = world_to_img(65, 615)
c_p1 = world_to_img(193, 743)
draw.rectangle([c_p0, c_p1], fill=(40, 60, 50), outline=(80, 220, 140), width=2)
draw.text((c_p0[0] + 8, c_p0[1] + 15), "LAVADOR-DECANTADOR", fill=(120, 255, 180))
draw.text((c_p0[0] + 8, c_p0[1] + 30), "Grelha + Tanque Cônico", fill=(160, 220, 190))
# Calha de minério britado entre Britadeira e Lavador
c2_0 = world_to_img(53, 685)
c2_1 = world_to_img(65, 695)
draw.rectangle([c2_0, c2_1], fill=(120, 160, 80))

# Tubulação modular existente na parede (X=110 para leste em Y=643)
pipe_0 = world_to_img(110, 640)
pipe_1 = world_to_img(300, 646)
draw.rectangle([pipe_0, pipe_1], fill=(120, 90, 40), outline=(200, 160, 80))
draw.text((pipe_0[0] + 20, pipe_0[1] - 14), "CANO MODULAR (PassagemParedeOeste X=110, Y=643)", fill=(255, 200, 100))

# Conexão de efluente
ef_0 = world_to_img(108, 635)
ef_1 = world_to_img(112, 645)
draw.rectangle([ef_0, ef_1], fill=(0, 255, 0), width=2)

# 7. Peça 5: PILHAS DE MINÉRIO E REJEITO (X: +60 a +220, Y: 765 a 829)
d_p0 = world_to_img(60, 765)
d_p1 = world_to_img(220, 829)
draw.rectangle([d_p0, d_p1], fill=(30, 45, 35), outline=(160, 160, 120), width=1)
draw.text((d_p0[0] + 10, d_p0[1] + 10), "PILHAS: Minério Lavado e Rejeito", fill=(210, 210, 160))

# 8. Corredores de Manutenção
cor_w_0 = world_to_img(-380, 600)
cor_w_1 = world_to_img(-307, 810)
draw.rectangle([cor_w_0, cor_w_1], outline=(255, 255, 0), width=1)
draw.text((cor_w_0[0] + 5, cor_w_0[1] + 50), "CORREDOR OESTE (73 px)", fill=(255, 255, 0))

cor_n_0 = world_to_img(-75, 572)
cor_n_1 = world_to_img(193, 615)
draw.rectangle([cor_n_0, cor_n_1], outline=(255, 255, 0), width=1)
draw.text((cor_n_0[0] + 40, cor_n_0[1] + 15), "CORREDOR NORTE (45 px)", fill=(255, 255, 0))

cor_s_0 = world_to_img(-350, 834)
cor_s_1 = world_to_img(250, 920)
draw.rectangle([cor_s_0, cor_s_1], outline=(255, 255, 0), width=1)
draw.text((cor_s_0[0] + 180, cor_s_0[1] + 35), "CORREDOR SUL LIVRE (86 px)", fill=(255, 255, 0))

# Salvar
img_planta.save("scratch/planta_baixa_estacao_mundo.png")
img_planta.save("C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/planta_baixa_estacao_mundo.png")
print("Nova planta baixa com peças separadas salva com sucesso!")
