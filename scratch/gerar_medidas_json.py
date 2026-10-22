from PIL import Image
import numpy as np
import json

# Carregar imagens
img_est = Image.open("assets/rails/estacao_trilho_v2.png").convert("RGBA")
img_ponte = Image.open("assets/rails/trilho_reto_vertical_v1.png").convert("RGBA")

arr_est = np.array(img_est)
arr_ponte = np.array(img_ponte)

# Escalas no Godot
scale_est = 0.20
scale_ponte = 0.25 # calibrada na sessao anterior com fator 1.25 uniforme (0.20 * 1.25)

# Posições no Godot (mundo):
# Estacao: position = Vector2(-215.9, 325)
#   largura = 1008, altura = 810
#   centro = (-215.9, 325)
#   topo = 325 - 810*0.2/2 = 244.0
#   base = 325 + 810*0.2/2 = 406.0
#
# Cavalete/Trilhos:
#   CavaleteElevadoCanal: position = Vector2(-188, 593.5)
#   TrilhosSobreCavalete: position = Vector2(0, -93.75), scale = Vector2(0.25, 0.25)
#   centro mundo = (-188.0, 593.5 - 93.75) = (-188.0, 499.75)
#   largura = 745, altura = 982
#   topo mundo = 499.75 - 982*0.25/2 = 377.0
#   base mundo = 499.75 + 982*0.25/2 = 622.5
#   Na linha de emenda exata Y = 406.0:
#     Y_local_ponte = (406.0 - 499.75) / 0.25 = -93.75 / 0.25 = -375.0
#     Y_texture_ponte = 982/2 + (-375.0) = 491.0 - 375.0 = 116.0 px

print("Calculando medições precisas...")

# Função para inspecionar linha da ponte
def measure_bridge_line(y_tex):
    row_rgb = arr_ponte[y_tex, :, :3]
    row_a = arr_ponte[y_tex, :, 3]
    lum = 0.299 * row_rgb[:, 0] + 0.587 * row_rgb[:, 1] + 0.114 * row_rgb[:, 2]
    
    # Encontrar picos de aço e bordas de sapata
    # Trilho esquerdo fica em torno de 150-250
    # Trilho direito fica em torno de 500-600
    # Sapata externa esquerda: transição para o metal na esquerda
    # Cabeça do trilho: pico de luminância
    p_esq_range = range(100, 320)
    p_dir_range = range(450, 680)
    
    # Gradiente
    grad = np.diff(lum)
    
    # Pico de brilho (cabeça do boleto)
    head_esq_x = p_esq_range[0] + np.argmax(lum[p_esq_range])
    head_dir_x = p_dir_range[0] + np.argmax(lum[p_dir_range])
    
    # Largura da cabeça (faixa de luminância > 70% do pico)
    th_esq = lum[head_esq_x] * 0.70
    th_dir = lum[head_dir_x] * 0.70
    head_esq_w = np.sum((lum[head_esq_x-25:head_esq_x+25] >= th_esq))
    head_dir_w = np.sum((lum[head_dir_x-25:head_dir_x+25] >= th_dir))
    
    # Sapata externa (base do trilho):
    # A sapata se estende cerca de 8 a 15 px para fora do centro da cabeça
    # Procuramos o ponto onde a cor de metal/ferro transiciona para o dormente/lastro
    # No trilho esquerdo: menor X com presença de sapata
    flange_left = head_esq_x - 12
    # No trilho direito: maior X com presença de sapata
    flange_right = head_dir_x + 14
    
    gauge_flange = flange_right - flange_left
    center_flange = (flange_left + flange_right) / 2.0
    
    return {
        "y_tex": y_tex,
        "flange_left": int(flange_left),
        "flange_right": int(flange_right),
        "gauge_flange": int(gauge_flange),
        "center_flange": float(center_flange),
        "head_left": int(head_esq_x),
        "head_right": int(head_dir_x),
        "head_width_avg": float((head_esq_w + head_dir_w) / 2.0)
    }

# Medir a ponte em diferentes alturas Y
m_ponte_top = measure_bridge_line(20)
m_ponte_emenda = measure_bridge_line(116) # Y=406 no mundo
m_ponte_mid = measure_bridge_line(500)
m_ponte_bottom = measure_bridge_line(960) # Ponta sul que receberá a estação

print("Ponte no topo (Y=20):", m_ponte_top)
print("Ponte na emenda (Y=116, mundo Y=406):", m_ponte_emenda)
print("Ponte no meio (Y=500):", m_ponte_mid)
print("Ponte na base sul (Y=960, mundo Y=622.5):", m_ponte_bottom)

# Função para inspecionar linha da estação
def measure_station_line(y_tex):
    row_rgb = arr_est[y_tex, :, :3]
    row_a = arr_est[y_tex, :, 3]
    lum = 0.299 * row_rgb[:, 0] + 0.587 * row_rgb[:, 1] + 0.114 * row_rgb[:, 2]
    
    p_esq_range = range(370, 480)
    p_dir_range = range(780, 900)
    
    head_esq_x = p_esq_range[0] + np.argmax(lum[p_esq_range])
    head_dir_x = p_dir_range[0] + np.argmax(lum[p_dir_range])
    
    th_esq = lum[head_esq_x] * 0.70
    th_dir = lum[head_dir_x] * 0.70
    head_esq_w = np.sum((lum[head_esq_x-25:head_esq_x+25] >= th_esq))
    head_dir_w = np.sum((lum[head_dir_x-25:head_dir_x+25] >= th_dir))
    
    flange_left = head_esq_x - 12
    flange_right = head_dir_x + 14
    
    gauge_flange = flange_right - flange_left
    center_flange = (flange_left + flange_right) / 2.0
    
    return {
        "y_tex": y_tex,
        "flange_left": int(flange_left),
        "flange_right": int(flange_right),
        "gauge_flange": int(gauge_flange),
        "center_flange": float(center_flange),
        "head_left": int(head_esq_x),
        "head_right": int(head_dir_x),
        "head_width_avg": float((head_esq_w + head_dir_w) / 2.0)
    }

m_est_top = measure_station_line(20)
m_est_bottom = measure_station_line(800)

print("\nEstação no topo (Y=20):", m_est_top)
print("Estação na base (Y=800, mundo Y=406):", m_est_bottom)
