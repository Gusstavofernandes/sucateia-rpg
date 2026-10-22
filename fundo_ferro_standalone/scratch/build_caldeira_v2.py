from PIL import Image, ImageDraw, ImageFilter
import numpy as np

# Carregar imagens
cal = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\machines\maquina_caldeira_vapor_v1.png').convert('RGBA')
pipe = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes\cano_longo_industrial.png').convert('RGBA')

# Extrair fatia do cano com flange e rebites
# Em pipe (1376x316), o tubo esta entre y=43 e y=273 (altura ~230px).
# Vamos extrair um trecho do tubo que tenha flange e cilindro continuo.
# Vamos ver onde estao os flanges em pipe
pipe_arr = np.array(pipe)
pipe_alpha = pipe_arr[:, :, 3]

# Altura proporcional para a caldeira:
target_pipe_h = 106
scale_factor = target_pipe_h / 230.0

# Redimensionar o tubo inteiro mantendo proporcao
new_pipe_w = int(pipe.width * scale_factor)
new_pipe_h = int(pipe.height * scale_factor)
scaled_pipe = pipe.resize((new_pipe_w, new_pipe_h), Image.Resampling.LANCZOS)

# Nova caldeira v2
cal_v2 = cal.copy()

# Vamos limpar na caldeira original o toco diagonal da fornalha a esquerda
# O toco diagonal fica na regiao x de 0 a 240, y de 350 a 550
# Vamos inspecionar e limpar com mascara suave
cal_arr = np.array(cal_v2)

# Criar mascara para apagar o toco diagonal esquerdo
mask_left = np.zeros((cal.height, cal.width), dtype=np.uint8)
# Regiao do toco diagonal
for y in range(350, 560):
    for x in range(0, 230):
        # A fornalha principal e sua base comecam a ter pixels mais densos a direita
        # Vamos proteger a fornalha circular
        # A porta da fornalha fica em torno de x=380, y=700 com raio ~250
        dist_fornalha = np.sqrt((x - 390)**2 + (y - 700)**2)
        if dist_fornalha > 260 and x < 210:
            cal_arr[y, x, 3] = 0

cal_v2 = Image.fromarray(cal_arr)

# Agora vamos colocar o bocal esquerdo perfeitamente horizontal em y_center = 482
# O trecho do tubo redimensionado tem altura de imagem new_pipe_h (~145px)
# e o centro do tubo esta em torno de 0.5 * new_pipe_h
scaled_arr = np.array(scaled_pipe)
scaled_alpha = scaled_arr[:, :, 3]
# Achar centro vertical do tubo escalado
y_indices = np.where(scaled_alpha[:, 50] > 50)[0]
scaled_center_y = int(np.mean(y_indices)) if len(y_indices) > 0 else new_pipe_h // 2

# Queremos que o centro do tubo fique em y = 482 na caldeira
paste_y_left = 482 - scaled_center_y

# Recortar um pedaco do tubo para a esquerda (comprimento ~220px com flange na ponta)
# Inverter horizontalmente se necessario para o flange ficar na ponta esquerda
piece_left = scaled_pipe.crop((50, 0, 280, new_pipe_h))
# Colocar de x=0 a x=230
cal_v2.paste(piece_left, (0, paste_y_left), piece_left)

# Agora para o lado direito:
# Queremos que o centro do tubo fique em y = 399 na caldeira
paste_y_right = 399 - scaled_center_y
# Recortar um pedaco do tubo para a direita
piece_right = scaled_pipe.crop((100, 0, 300, new_pipe_h))
# Na caldeira original, o flange direito vai ate x=725
# Vamos colar cobrindo de x=580 a x=768
# Mas vamos mesclar suavemente com o bocal existente
cal_v2.paste(piece_right, (560, paste_y_right), piece_right)

# Salvar caldeira_v2_test.png para inspecionar
cal_v2.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\caldeira_v2_test.png')
print('caldeira_v2_test.png salva com sucesso!')
