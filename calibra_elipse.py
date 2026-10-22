from PIL import Image
import numpy as np

im2 = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_muralha_sul_clean.png').convert("RGBA")
arr = np.array(im2)

# Vamos analisar as cores e posicoes da imagem 2
# Vamos fazer uma copia para a mureta frontal sul
arr_sul = arr.copy()

# A mureta frontal e o portao:
# Na parte superior de Y, tudo acima da borda interna da parede frontal e traseira
# Vamos ver onde esta o horizonte do anel:
# O topo do anel norte comeca em Y=24 e a base interna do anel norte termina em Y~230 onde a terra comeca.
# A terra vai de Y~230 ate onde a face interna da parede sul comeca (Y~360-440).
# Mas no portao (X entre 460 e 915), o portao comeca em Y~380 e tem grades verticais transparentes nos vaos!

# Vamos testar salvar a parte norte e a parte sul da imagem 2 separadas
# Para a parte sul:
# Queremos a mureta frontal completa (desde onde a curvatura atinge a frente).
# Vamos ver: se cortarmos por uma elipse que define a borda interna da mureta frontal:
print("Gerando visualizacao da mureta sul...")

# Vamos criar uma imagem apenas com a mureta frontal sul:
# Pontos da borda interna superior da mureta frontal:
# X vai de 45 a 1330
# Y da face interna da mureta sul varia em arco de ~330 (nas pontas) ate ~420 (no centro)
# E o portao tem altura que sobe ate Y~380
h, w, _ = arr.shape
y_indices, x_indices = np.indices((h, w))

# Elipse interna da arena aproximada:
# Centro da elipse: cx = 688, cy = 295
# Raios: rx = 520, ry = 160
# Equacao da elipse: ((x - cx)/rx)^2 + ((y - cy)/ry)^2 <= 1
cx = 688
cy = 305
rx = 520
ry = 160

dist_elipse = ((x_indices - cx) / rx) ** 2 + ((y_indices - cy) / ry) ** 2

# Dentro da elipse (dist_elipse < 1.0) e terra!
# Mas atencao: o portao esta na frente (y > 380) e as barras do portao estao dentro dessa regiao se olhado em projecao!
# Vamos salvar uma imagem de teste com dist_elipse desenhada para calibrar com perfeicao:
teste_mask = arr.copy()
# Destacar onde dist_elipse < 1.0 em azul semitransparente
mask_terra = (dist_elipse <= 1.0) & (teste_mask[:, :, 3] > 50)
teste_mask[mask_terra, 0] = 0
teste_mask[mask_terra, 1] = 100
teste_mask[mask_terra, 2] = 255

Image.fromarray(teste_mask).save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_elipse_calibracao.png')
print("Calibracao salva.")
