import rembg
from PIL import Image
import numpy as np

src_path = r"C:\Users\Usuario\.gemini\antigravity\brain\2b874476-d390-4406-8b89-b8e275f8f9f1\monumental_castle_facade_1792609083565.jpg"
out_path = r"assets\generated\structures\monumental_clock_castle.png"

print("Lendo imagem de origem...")
input_image = Image.open(src_path)

print("Processando remoção de fundo com rembg...")
output_image = rembg.remove(input_image)

# Salvar PNG com transparência
output_image.save(out_path, format="PNG")
print(f"Salvo com sucesso em: {out_path}")
print(f"Dimensões do castelo: {output_image.size}")
