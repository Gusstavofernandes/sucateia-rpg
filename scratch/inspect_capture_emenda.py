from PIL import Image
import numpy as np

img = Image.open('C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/captura_boca_tunel_v2_closeup_emenda.png')
print("Tamanho captura 2:", img.size)

# Vamos recortar o centro da tela onde estão os trilhos
# Se a câmera está em Vector2(-190, 244), o centro da tela (w/2, h/2) é exatamente (-190, 244) no mundo!
# Vamos recortar um retângulo de 200px de largura e 400px de altura em torno do centro da tela:
cx = img.width // 2
cy = img.height // 2
crop = img.crop((cx - 150, cy - 200, cx + 150, cy + 200))
crop.save('scratch/crop_emenda_inengine.png')
print("Salvo scratch/crop_emenda_inengine.png")
