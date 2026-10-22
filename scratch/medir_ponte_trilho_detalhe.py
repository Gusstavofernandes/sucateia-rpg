from PIL import Image
import numpy as np

# Carregar imagens
img_estacao = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png').convert("RGBA")
img_trilho_ponte = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")
img_cavalete = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png').convert("RGBA")

print("--- MEDIÇÃO DO TRILHO DE LIGAÇÃO (NA ESTAÇÃO V2) ---")
# Escala na cena: scale = Vector2(0.20, 0.20)
# Nó EstacaoCarga: position = Vector2(-215.9, 325)
# Na imagem estacao_trilho_v2:
# Vamos encontrar a posição dos dois trilhos na textura da estação
arr_est = np.array(img_estacao)
# Amostrar linha y = 400 da estação (meio da textura)
row_est = arr_est[400, :, :]
# Procurar os trilhos (ferro/brilho)
print("Tamanho estação:", img_estacao.size)

# Vamos inspecionar exatamente onde os trilhos estão no trilho_reto_vertical_v1
# trilho_reto_vertical_v1 foi a base usada:
# No relatório anterior:
# Trilho Esquerdo: Centro X = 220.00 px na textura 745x982
# Trilho Direito: Centro X = 522.00 px na textura 745x982
# Bitola bruta na textura: 302.00 px
# Na escala 0.20:
# Bitola no mundo = 302.0 * 0.20 = 60.40 px!
# Passo dos dormentes na textura: ~120 px -> no mundo: 120 * 0.20 = 24.0 px!
# Largura dos dormentes na textura: ~645 px -> no mundo: 645 * 0.20 = 129.0 px!

print("No trilho_reto_vertical_v1 com escala 0.20:")
print("  Bitola no mundo = 60.40 px")
print("  Passo dos dormentes no mundo = 24.0 px")
print("  Largura dos dormentes no mundo = 129.0 px")

# E no cavalete_alto_v1?
# Vamos ver se cavalete_alto_v1 tem trilhos desenhados ou largura do vão:
print("Tamanho cavalete_alto_v1:", img_cavalete.size)
# Escala do cavalete na cena: 0.32!
