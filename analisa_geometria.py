from PIL import Image
import numpy as np

# Vamos analisar a imagem 2
im2 = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_muralha_sul_clean.png')
w, h = im2.size
arr = np.array(im2)

print("Tamanho Img 2:", w, h)

# O portao fica na parte inferior, centrado horizontalmente
# Vamos encontrar os limites do portao e da parede frontal
# O portao esta entre x ~ 460 e x ~ 915, e y de ~ 380 a 730
# Vamos recortar a parte frontal sul da arena
# A linha do chão de terra vs parede frontal:
# A borda interna da parede frontal fica aproximadamente onde a terra encontra o topo da parede frontal interna
