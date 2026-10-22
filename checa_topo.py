from PIL import Image
import numpy as np

im = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_coliseu_imponente_completo_v3.png')
arr = np.array(im)
print('Shape:', arr.shape)
top_row = arr[0, :, 3]
print('Pixels nao transparentes na linha 0:', np.sum(top_row > 0))
for y in range(15):
    print(f'Linha {y}:', np.sum(arr[y, :, 3] > 0))
