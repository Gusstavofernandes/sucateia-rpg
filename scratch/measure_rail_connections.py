from PIL import Image
import numpy as np

# Carregar imagens
img_tunel = Image.open('fundo_ferro_standalone/assets/rails/tunel_mina_norte_v1.png')
img_trilho_vert = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png')
img_cavalete = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png')

print("Dimensões brutas:")
print("Túnel:", img_tunel.size)
print("Trilho Vertical:", img_trilho_vert.size)
print("Cavalete:", img_cavalete.size)
