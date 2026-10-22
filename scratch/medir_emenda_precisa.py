from PIL import Image
import numpy as np

# Vamos carregar as duas texturas
img_est = Image.open("assets/rails/estacao_trilho_v2.png").convert("RGBA")
img_ponte = Image.open("assets/rails/trilho_reto_vertical_v1.png").convert("RGBA")

arr_est = np.array(img_est)
arr_ponte = np.array(img_ponte)

# Na cena do Godot:
# Estacao: position = Vector2(-215.9, 325), scale = Vector2(0.20, 0.20)
#   W = 1008, H = 810
#   Y_base = 325 + 810*0.2/2 = 406.0 px (linha exata onde o sprite da estacao termina!)
#   Y=406.0 no mundo corresponde exatamente à última linha do sprite da estação: Y_tex = 809 (ou 808)!

# Ponte: CavaleteElevadoCanal pos = Vector2(-188, 593.5)
#   TrilhosSobreCavalete pos = Vector2(0, -93.75), scale = Vector2(0.25, 0.25)
#   W = 745, H = 982
#   Y_centro = 593.5 - 93.75 = 499.75 px
#   Na linha Y_mundo = 406.0:
#   Y_rel = 406.0 - 499.75 = -93.75 px
#   Y_tex_ponte = 982/2 + (-93.75 / 0.25) = 491.0 - 375.0 = 116.0 px!

print("=== INSPEÇÃO DETALHADA DA LINHA DE EMENDA Y_mundo = 406.0 ===")

# Vamos examinar a linha 808 da estação:
row_est = arr_est[808, :, :]
# E a linha 116 da ponte:
row_ponte = arr_ponte[116, :, :]

# Vamos inspecionar onde os trilhos estão em cada imagem
# Vamos imprimir as colunas onde há pixels de trilho
print("\n--- ESTAÇÃO (Y_tex = 808) ---")
# O trilho tem dormentes de madeira e duas barras de ferro
# Vamos imprimir todos os X onde alfa > 50
op_est = np.where(row_est[:, 3] > 50)[0]
print(f"Faixa opaca da estação: [{op_est[0]} .. {op_est[-1]}]")

# Na estação em Y=808:
# Onde estão os dois trilhos?
# Vamos olhar a imagem estacao_trilho_v2.png em torno de Y=800
# Vamos salvar um recorte ampliado de 50px de altura de cada um para inspecionar visualmente
crop_est = img_est.crop((350, 780, 900, 810))
crop_est.save("scratch/crop_estacao_base.png")

crop_ponte = img_ponte.crop((100, 95, 650, 140))
crop_ponte.save("scratch/crop_ponte_emenda.png")

print("Crops salvos em scratch/")
