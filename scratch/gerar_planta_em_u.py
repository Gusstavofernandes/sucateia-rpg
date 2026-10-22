from PIL import Image, ImageDraw

w_img, h_img = 700, 420
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
p_x0, p_y0 = world_to_img(-257, 550)
p_x1, p_y1 = world_to_img(-135, 617)
draw.rectangle([p_x0, p_y0, p_x1, p_y1], fill=(50, 40, 35), outline=(140, 110, 80))
draw.text((p_x0 + 10, p_y0 + 20), "PONTE (Y->617)", fill=(200, 180, 140))
draw.line([world_to_img(-250, 550), world_to_img(-257, 617)], fill=(0, 255, 255), width=2)
draw.line([world_to_img(-142, 550), world_to_img(-135, 617)], fill=(0, 255, 255), width=2)

# 3. Peça A: DESCARGA BASCULANTE (X: -280 a -112, Y: 617 a 745)
desc_0 = world_to_img(-280, 617)
desc_1 = world_to_img(-112, 745)
draw.rectangle([desc_0, desc_1], fill=(60, 45, 40), outline=(220, 160, 60), width=2)
draw.text((desc_0[0] + 10, desc_0[1] + 10), "DESCARGA BASCULANTE", fill=(255, 220, 100))
draw.text((desc_0[0] + 10, desc_0[1] + 25), "Trilho + Moega + Batente", fill=(200, 180, 150))
# Trilhos internos
draw.line([world_to_img(-257, 617), world_to_img(-266, 710)], fill=(0, 255, 255), width=2)
draw.line([world_to_img(-135, 617), world_to_img(-126, 710)], fill=(0, 255, 255), width=2)
# Batente em Y=710
draw.rectangle([world_to_img(-270, 710), world_to_img(-120, 715)], fill=(220, 50, 50))
draw.text((world_to_img(-270, 710)[0] + 15, world_to_img(-270, 710)[1] - 12), "BATENTE (Y=710)", fill=(255, 100, 100))

# 4. Peça B: BRITADEIRA A VAPOR (X: -90 a +38, Y: 625 a 725)
b_p0 = world_to_img(-90, 625)
b_p1 = world_to_img(38, 725)
draw.rectangle([b_p0, b_p1], fill=(55, 55, 65), outline=(100, 150, 220), width=2)
draw.text((b_p0[0] + 10, b_p0[1] + 15), "BRITADEIRA A VAPOR", fill=(140, 190, 255))
draw.text((b_p0[0] + 10, b_p0[1] + 30), "Mandíbulas + Volante", fill=(180, 180, 200))
# Calha de minério bruto Descarga -> Britadeira (VÃO ZERO)
draw.rectangle([world_to_img(-114, 660), world_to_img(-88, 672)], fill=(180, 140, 50))
draw.text((world_to_img(-114, 660)[0] - 5, world_to_img(-114, 660)[1] - 12), "Calha (Vão 0)", fill=(255, 200, 100))

# 5. Peça C: LAVADOR-DECANTADOR CONJUGADO (X: -90 a +50, Y: 735 a 835) [ABAIXO DA BRITADEIRA!]
c_p0 = world_to_img(-90, 735)
c_p1 = world_to_img(50, 835)
draw.rectangle([c_p0, c_p1], fill=(40, 60, 50), outline=(80, 220, 140), width=2)
draw.text((c_p0[0] + 10, c_p0[1] + 15), "LAVADOR-DECANTADOR (EM 'U')", fill=(120, 255, 180))
draw.text((c_p0[0] + 10, c_p0[1] + 30), "Grelha + Cone Decantador", fill=(160, 220, 190))
# Acoplamento vertical direto Britadeira -> Lavador (VÃO ZERO)
draw.rectangle([world_to_img(-35, 723), world_to_img(-15, 737)], fill=(120, 160, 80))
draw.text((world_to_img(-35, 723)[0] + 25, world_to_img(-35, 723)[1] - 2), "Queda Vertical 0", fill=(200, 255, 100))

# 6. Peça D: PILHAS DE MINÉRIO E REJEITO (X: -90 a +50, Y: 845 a 895)
d_p0 = world_to_img(-90, 845)
d_p1 = world_to_img(50, 895)
draw.rectangle([d_p0, d_p1], fill=(30, 45, 35), outline=(160, 160, 120), width=1)
draw.text((d_p0[0] + 10, d_p0[1] + 15), "PILHAS NO SOLO: Minério Lavado e Rejeito", fill=(210, 210, 160))
# Prolongadores fechados descendo nas pilhas
draw.line([world_to_img(-30, 835), world_to_img(-30, 845)], fill=(160, 220, 140), width=3)
draw.line([world_to_img(10, 835), world_to_img(10, 845)], fill=(160, 220, 140), width=3)

# 7. Cano Modular e ChapaMetal_7 na Parede Leste
# Cano Modular em X=110 para leste
draw.rectangle([world_to_img(110, 640), world_to_img(300, 646)], fill=(120, 90, 40), outline=(200, 160, 80))
draw.text((world_to_img(110, 640)[0] + 10, world_to_img(110, 640)[1] - 14), "CANO MODULAR (X=110)", fill=(255, 200, 100))
# ChapaMetal_7 em X=200, Y=680
draw.rectangle([world_to_img(180, 665), world_to_img(220, 695)], fill=(80, 80, 90), outline=(180, 180, 200))
draw.text((world_to_img(180, 665)[0] - 10, world_to_img(180, 665)[1] + 35), "ChapaMetal_7 (X=200)", fill=(200, 200, 220))

# Duto de interligação de efluente do Lavador-Decantador até o Cano Modular
draw.line([world_to_img(50, 750), world_to_img(110, 750)], fill=(0, 255, 0), width=3)
draw.line([world_to_img(110, 750), world_to_img(110, 643)], fill=(0, 255, 0), width=3)
draw.text((world_to_img(50, 750)[0] + 15, world_to_img(50, 750)[1] - 12), "Duto Efluente", fill=(0, 255, 0))

# 8. Corredores de Manutenção (Linhas amarelas)
# Corredor Oeste (100 px)
draw.rectangle([world_to_img(-380, 615), world_to_img(-280, 750)], outline=(255, 255, 0), width=1)
draw.text((world_to_img(-380, 615)[0] + 5, world_to_img(-380, 615)[1] + 50), "CORREDOR OESTE (100 px)", fill=(255, 255, 0))

# Corredor Norte (47 px)
draw.rectangle([world_to_img(-90, 572), world_to_img(50, 617)], outline=(255, 255, 0), width=1)
draw.text((world_to_img(-90, 572)[0] + 15, world_to_img(-90, 572)[1] + 15), "CORREDOR NORTE (47 px)", fill=(255, 255, 0))

# Corredor Leste (60 px entre decantador e cano)
draw.rectangle([world_to_img(50, 625), world_to_img(110, 835)], outline=(255, 255, 0), width=1)
draw.text((world_to_img(50, 625)[0] + 5, world_to_img(50, 625)[1] + 80), "CORREDOR (60 px)", fill=(255, 255, 0))

# Corredor Sul (55 px)
draw.rectangle([world_to_img(-350, 895), world_to_img(150, 950)], outline=(255, 255, 0), width=1)
draw.text((world_to_img(-350, 895)[0] + 150, world_to_img(-350, 895)[1] + 20), "CORREDOR SUL LIVRE (55 px)", fill=(255, 255, 0))

img_planta.save("scratch/planta_baixa_estacao_mundo.png")
img_planta.save("C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/planta_baixa_estacao_mundo.png")
print("Planta baixa em U salva com sucesso!")
