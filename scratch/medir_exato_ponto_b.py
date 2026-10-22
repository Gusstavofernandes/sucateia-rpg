from PIL import Image
import numpy as np

# 1. TRILHO DE LIGAÇÃO (Estação v2)
# Como a estação v2 foi construída usando o trilho_reto_vertical_v1:
# Na imagem da estação v2 (1008x810):
# Plataforma à esquerda, trilho à direita.
# O trilho foi colado com offset.
# Vamos encontrar os dois trilhos (coordenadas X dos picos de aço dos trilhos)
img_est = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png').convert("RGBA")
arr_est = np.array(img_est)

# Amostrar linha 700 (perto da base da estação, onde ela conecta com a ponte)
# Procurar trilhos de ferro: ferro é cinza/azulado reflexivo
# Vamos plotar a intensidade para encontrar os picos exatos
row = arr_est[700, :, :]
# Os trilhos na imagem estão em X entre 400 e 900
# Vamos calcular os centros dos picos
# Linha do trilho esquerdo e direito

# 2. PONTE (cavalete e trilhos sobre cavalete)
img_cav = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png').convert("RGBA")
arr_cav = np.array(img_cav)
# Topo do cavalete: linha 150
# No topo do cavalete há vigas de ferro laterais com rebites
# Vamos encontrar a distância entre os trilhos/vigas do cavalete

# 3. TRILHO SOBRE CAVALETE (trilho_reto_vertical_v1)
img_tri = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")

print("--- ANÁLISE COMPLETA ---")
print("Textura estação:", img_est.size)
print("Textura cavalete:", img_cav.size)
print("Textura trilho_ponte:", img_tri.size)
