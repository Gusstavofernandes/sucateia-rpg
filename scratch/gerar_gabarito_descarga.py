from PIL import Image, ImageDraw, ImageFont

# Canvas oficial da estacao_descarga_basculante_v1: 896 x 512 px
w_canv, h_canv = 896, 512
img_gabarito = Image.new("RGB", (w_canv, h_canv), (255, 0, 255)) # Fundo Magenta #FF00FF
draw = ImageDraw.Draw(img_gabarito)

# Cota topo (Y=0, mundo Y=617):
# Bitola no topo: 489.0 px (Sapata Esq: X=203.5, Sapata Dir: X=692.5, Centro: X=448.0)
# Cota batente (Y=372, mundo Y=710):
# Bitola no batente: 559.4 px (Sapata Esq: X=161.9, Sapata Dir: X=721.3, Centro: X=441.6)
# Cota base (Y=512, mundo Y=745):
# Bitola na base: 585.92 px (Sapata Esq: X=146.1, Sapata Dir: X=732.1, Centro: X=439.1)

# 1. Eixo Central (Amarelo, 1px)
draw.line([(448, 0), (439, 512)], fill=(255, 255, 0), width=1)

# 2. Trilhos / Sapatas Externas (Ciano #00FFFF, 1px)
# Trilho Esquerdo
draw.line([(203, 0), (162, 372)], fill=(0, 255, 255), width=1)
draw.line([(162, 372), (146, 512)], fill=(0, 255, 255), width=1)
# Trilho Direito
draw.line([(693, 0), (721, 372)], fill=(0, 255, 255), width=1)
draw.line([(721, 372), (732, 512)], fill=(0, 255, 255), width=1)

# Cabeças dos trilhos (linhas pontilhadas ou azul-claro a 10px para dentro da sapata)
draw.line([(213, 0), (172, 372)], fill=(100, 200, 255), width=1)
draw.line([(683, 0), (711, 372)], fill=(100, 200, 255), width=1)

# 3. Linha de Emenda de Topo (Verde #00FF00, 1px em Y=0 / Y=1)
draw.line([(0, 1), (895, 1)], fill=(0, 255, 0), width=1)

# 4. Linha do Batente / Fim de Curso do Carrinho (Vermelho #FF0000 em Y=372)
draw.line([(150, 372), (730, 372)], fill=(255, 0, 0), width=2)

# 5. Saída da Calha de Minério Bruto na Borda Direita (Laranja #FFA500, X=895, Y=220 a 300)
draw.line([(895, 220), (895, 300)], fill=(255, 165, 0), width=4)

# 6. Passo dos Dormentes (Guias cinzas horizontais a cada 46.6 px a partir de Y=0)
# A fase em Y=0: o primeiro dormente fica a 46.6 px do último dormente da ponte.
# Como o último dormente da ponte estava a 49 px antes de Y=0, o primeiro dormente fica exatamente em Y=0 a Y=10!
for y_dorm in [10, 56, 103, 150, 196, 243, 289, 336, 383, 429, 476]:
    if y_dorm < 512:
        # dormente entre as sapatas
        # interpolar X esquerdo e direito
        t = y_dorm / 512.0
        x_e = int(203 + (146 - 203) * t) - 30
        x_d = int(693 + (732 - 693) * t) + 30
        draw.line([(x_e, y_dorm), (x_d, y_dorm)], fill=(180, 180, 180), width=1)

# 7. Legenda no canto superior esquerdo (fora da área dos trilhos)
draw.rectangle([(10, 10), (190, 120)], fill=(0, 0, 0))
draw.text((15, 15), "GABARITO: DESCARGA", fill=(255, 255, 255))
draw.text((15, 30), "Canvas: 896x512 px", fill=(200, 200, 200))
draw.text((15, 45), "- Ciano: Sapatas Trilho", fill=(0, 255, 255))
draw.text((15, 60), "- Amarelo: Eixo Central", fill=(255, 255, 0))
draw.text((15, 75), "- Verde: Emenda Topo", fill=(0, 255, 0))
draw.text((15, 90), "- Vermelho: Batente", fill=(255, 50, 50))
draw.text((15, 105), "- Laranja: Calha Minerio", fill=(255, 165, 0))

# Salvar gabarito
img_gabarito.save("scratch/gabarito_estacao_descarga_basculante_v1.png")
img_gabarito.save("C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/gabarito_estacao_descarga_basculante_v1.png")
print("Gabarito oficial de estacao_descarga_basculante_v1 gerado com sucesso!")
