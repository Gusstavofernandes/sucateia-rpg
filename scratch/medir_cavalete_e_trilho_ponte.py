from PIL import Image
import numpy as np

cavalete = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png').convert("RGBA")
trilho_ponte = Image.open('fundo_ferro_standalone/assets/rails/trilho_reto_vertical_v1.png').convert("RGBA")
estacao = Image.open('fundo_ferro_standalone/assets/rails/estacao_trilho_v2.png').convert("RGBA")

print("Cavalete size:", cavalete.size)
print("Trilho Ponte size:", trilho_ponte.size)
print("Estação size:", estacao.size)

# Vamos analisar o topo de cavalete_alto_v1.png (linhas 0 a 300) para ver se há trilhos desenhados nele
crop_top = cavalete.crop((0, 0, cavalete.size[0], 350))
crop_top.save('scratch/cavalete_top_crop.png')
print("Salvo scratch/cavalete_top_crop.png")
