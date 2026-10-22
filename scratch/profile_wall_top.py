from PIL import Image
import numpy as np

wall = Image.open('fundo_ferro_standalone/assets/fundo_wall.png').convert("RGBA")
arr = np.array(wall)

# Encontrar o primeiro pixel opaco em cada coluna de 0 a 1500
first_y = []
for x in range(0, 1500, 50):
    col = arr[:, x, 3]
    op = np.where(col > 50)[0]
    first_y.append((x, op[0] if len(op) > 0 else -1))

print("Primeiro pixel opaco em fundo_wall:")
for x, y in first_y:
    print(f"  x={x:4d} -> y={y:3d}")
