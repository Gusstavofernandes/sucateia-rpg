import math

# Coordenadas e geometrias exatas no mundo

# 1. Ponto de Parede Oeste: X = 120, Y = 680
# Manifold Oeste: X = 750, Y = 750.
# Bocal esquerdo do Manifold:
# Manifold sprite tem centro em 750, -68 -> centro y = 682.
# Na imagem de 768px com scale 0.24:
# Largura total = 184.3px. Metade = 92px.
# Bocal esquerdo na borda da imagem: X_mundo = 750 - 92 = 658.
# Bocal direito na borda da imagem: X_mundo = 750 + 92 = 842.

# Trecho 1: Parede Oeste -> Bocal esquerdo Manifold (120 a 658 = 538px)
# Com cano_longo_industrial de largura 154px (passo 150px):
# Segmento 1: centro = 120 + 75 = 195
# Segmento 2: centro = 195 + 150 = 345
# Segmento 3: centro = 345 + 150 = 495
# Segmento 4: centro = 495 + 120 = 615 (entra no bocal esquerdo do manifold em 658 com flange)

# Trecho 2: Bocal direito Manifold (842) -> Subida de cotovelos (1410 a 1470)
# Distância: 1410 - 842 = 568px em Y = 680.
# Segmento 1: centro = 842 + 75 = 917
# Segmento 2: centro = 917 + 150 = 1067
# Valvula: largura 105px. Centro = 1067 + (75 + 52 - 5) = 1189.
# Segmento 3: centro = 1189 + (52 + 75 - 5) = 1311.
# Segmento 4: centro = 1311 + 90 = 1401 (vai de 1324 a 1478).

# Trecho 3: Transição Cotovelos (1410..1460) e Boca Encaixe Oeste (1440..1580)
# Cotovelo 1 (sobe): pos X = 1435, Y = 665
# Cotovelo 2 (vira para leste): pos X = 1465, Y = 642
# BocaEncaixeBombaOeste (flip_h=True):
# Borda direita em 1580 (bocal da bomba).
# Centro X = 1580 - 72.6 = 1507. Centro Y = 642.
# Borda esquerda da boca em 1507 - 72.6 = 1435!
# Encaixe exato no cotovelo 2!

# Trecho 4: Bomba Central: X = 1750, Y = 740
# Bocal esquerdo: X = 1580, Y = 642 (recebe BocaEncaixeBombaOeste)
# Bocal direito: X = 1920, Y = 642 (recebe BocaEncaixeBombaLeste)

# Trecho 5: BocaEncaixeBombaLeste (sem flip)
# Borda esquerda em 1920.
# Centro X = 1920 + 72.6 = 1993. Centro Y = 642.
# Borda direita em 1993 + 72.6 = 2065.

# Trecho 6: Bomba -> Caldeira Leste
# Caldeira Leste: posição = (2650, 732).
# Imagem da caldeira tem 703px de largura. Com scale 0.24 = 168.7px.
# Metade = 84.4px.
# Bocal esquerdo da caldeira: X_mundo = 2650 - 84.4 = 2565.6 ≈ 2565. Centro Y = 645.
# Bocal direito da caldeira: X_mundo = 2650 + 84.4 = 2734.4 ≈ 2735. Centro Y = 645.
# Espaço a preencher entre Bomba (2065) e Caldeira (2565):
# Distância = 2565 - 2065 = 500px!
# Ponte de travessia do goblin: X = 2210.
# Segmento 1: centro = 2065 + 75 = 2140 (vai de 2063 a 2217)
# PonteTravessia: centro = 2210, Y = 642 (passa por cima do tubo)
# Valvula Leste: largura 105px. Centro = 2210 + 95 = 2305.
# Segmento 2: centro = 2305 + (52 + 75 - 5) = 2427 (vai de 2350 a 2504)
# Segmento 3: centro = 2427 + 100 = 2527 (vai de 2450 a 2604, entrando reto no bocal esquerdo da caldeira em 2565!)

# Trecho 7: Caldeira Leste (2735) -> Passagem Parede Leste (3440)
# Passagem Parede Leste: posição = (3440, 643).
# Toco de cano sai para a esquerda: na imagem de 859px, o centro X do toco na borda esquerda:
# com scale 0.12, alvenaria tem largura 103px (metade = 51.5px).
# Centro X da passagem = 3440. Extremo esquerdo do toco = 3440 - 51.5 = 3388.5 ≈ 3388.
# Espaço a preencher: de 2735 a 3388 = 653px!
# Com passo de 145px:
# Segmento Leste 1: centro = 2735 + 75 = 2810 (vai de 2733 a 2887)
# Segmento Leste 2: centro = 2810 + 145 = 2955 (vai de 2878 a 3032)
# Segmento Leste 3: centro = 2955 + 145 = 3100 (vai de 3023 a 3177)
# Segmento Leste 4: centro = 3100 + 145 = 3245 (vai de 3168 a 3322)
# Segmento Leste 5: centro = 3245 + 105 = 3350 (vai de 3273 a 3427, encaixando com perfeição no toco da parede em 3388!)

print("Cálculos de posicionamento contínuo finalizados!")
