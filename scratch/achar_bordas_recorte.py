from PIL import Image
import numpy as np

img = Image.open('fundo_ferro_standalone/medicao_recorte_sem_tunel.png').convert("RGB")
arr = np.array(img)

def screen_to_world(sx, sy):
    wx = -190.0 + (sx - 640.0) / 1.5
    wy =  180.0 + (sy - 360.0) / 1.5
    return wx, wy

def world_to_screen(wx, wy):
    sx = 640.0 + (wx - (-190.0)) * 1.5
    sy = 360.0 + (wy - 180.0) * 1.5
    return int(round(sx)), int(round(sy))

# Na altura de mundo Y = 100 (dentro da parede norte, acima do piso)
_, sy_wall = world_to_screen(0, 100)
print(f"Y de mundo 100 corresponde a sy = {sy_wall}")

# Amostrar uma faixa em sy_wall de sx=400 a sx=900 (world X de -350 a -23)
for sx in range(500, 950, 20):
    wx, _ = screen_to_world(sx, sy_wall)
    r, g, b = arr[sy_wall, sx]
    print(f"sx={sx:3d} (wx={wx:6.1f} px) -> RGB=({r:3d}, {g:3d}, {b:3d})")
