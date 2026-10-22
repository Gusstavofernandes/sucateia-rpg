from PIL import Image
import numpy as np

# Na imagem medicao_recorte_sem_tunel.png:
# Câmera configurada com:
# player.position = Vector2(-20, 380)
# cam.position = Vector2(-190 - player.position.x, 180 - player.position.y)
# Ou seja: cam.global_position = (-190, 180)
# cam.zoom = Vector2(1.5, 1.5)
# Viewport size = 1280 x 720
#
# Com zoom 1.5, a largura visível no mundo é: 1280 / 1.5 = 853.33 px
# A altura visível no mundo é: 720 / 1.5 = 480.0 px
#
# Centro da tela é o ponto de mundo (-190, 180).
# Logo, para qualquer pixel (px, py) na imagem 1280x720:
# world_x = -190.0 + (px - 640.0) / 1.5
# world_y =  180.0 + (py - 360.0) / 1.5

img = Image.open('fundo_ferro_standalone/medicao_recorte_sem_tunel.png')
print("Tamanho da imagem de medição:", img.size)

def screen_to_world(sx, sy):
    wx = -190.0 + (sx - 640.0) / 1.5
    wy =  180.0 + (sy - 360.0) / 1.5
    return wx, wy

def world_to_screen(wx, wy):
    sx = 640.0 + (wx - (-190.0)) * 1.5
    sy = 360.0 + (wy - 180.0) * 1.5
    return int(round(sx)), int(round(sy))

print(f"Limites de mundo cobertos na imagem:")
print(f"  X: {screen_to_world(0, 0)[0]:.1f} a {screen_to_world(1280, 0)[0]:.1f}")
print(f"  Y: {screen_to_world(0, 0)[1]:.1f} a {screen_to_world(0, 720)[1]:.1f}")

# Vamos inspecionar linhas horizontais e verticais para encontrar as bordas do recorte!
# O centro dos trilhos está em X = -190.0 de mundo -> na tela: sx = 640
print(f"Centro dos trilhos na tela: sx = 640 (world X = -190.0)")
