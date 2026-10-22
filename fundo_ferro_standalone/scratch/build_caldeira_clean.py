import numpy as np
from PIL import Image, ImageDraw, ImageFilter


# 1. Carregar caldeira original e tubo industrial
cal_orig = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\machines\maquina_caldeira_vapor_v1.png').convert('RGBA')
pipe = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes\cano_longo_industrial.png').convert('RGBA')

W, H = cal_orig.size
cal_np = np.array(cal_orig)

# 2. Remover toco diagonal antigo no lado esquerdo da fornalha
# O toco diagonal esta na regiao x: 0..220, y: 350..580
# Vamos limpar essa regiao com cuidado para nao afetar a borda redonda da fornalha
# A fornalha tem seu anel de rebites centrado em torno de (380, 690)
for y in range(350, 600):
    for x in range(0, 230):
        # Medir distancia do centro do anel da fornalha
        dist_ring = np.hypot(x - 390, y - 690)
        # O anel da fornalha tem raio exterior de ~225px
        if dist_ring > 228 and x < 210:
            cal_np[y, x] = [0, 0, 0, 0]

# 3. Remover a boca aberta inclinada antiga no lado direito
# A gola de latao termina em x ≈ 635. O flange inclinado antigo vai de x: 635..768, y: 320..500
for y in range(320, 520):
    for x in range(635, W):
        cal_np[y, x] = [0, 0, 0, 0]

cal_clean = Image.fromarray(cal_np)

# 4. Preparar bocal do tubo escalado
# Tubo no Godot tem scale 0.11 em imagem de 1376x316 (altura tubo = 230).
# Na caldeira (scale 0.24), a altura proporcional eh 230 * 0.11 / 0.24 = 105.4px
target_h = 105
scale_factor = target_h / 230.0
scaled_w = int(pipe.width * scale_factor)
scaled_h = int(pipe.height * scale_factor)
scaled_pipe = pipe.resize((scaled_w, scaled_h), Image.Resampling.LANCZOS)

# Achar centro vertical do tubo escalado
sp_arr = np.array(scaled_pipe)
sp_alpha = sp_arr[:, :, 3]
y_pts = np.where(sp_alpha[:, 50] > 50)[0]
center_y = int(np.mean(y_pts))

# 5. Criar bocal direito (saida de vapor)
# Centro na caldeira em y = 399
# Vamos pegar uma fatia do cano com flange: flange na ponta e corpo cilindrico
# Em pipe, temos anel com rebites em x ≈ 250..350
# Vamos recortar um trecho de x=150 a x=420 de scaled_pipe
nozzle_right = scaled_pipe.crop((int(200 * scale_factor), 0, int(650 * scale_factor), scaled_h))

# 6. Criar bocal esquerdo (entrada de fluido)
# Centro na caldeira em y = 482
# Vamos recortar e espelhar horizontalmente para o flange ficar na ponta esquerda
nozzle_left = nozzle_right.transpose(Image.FLIP_LEFT_RIGHT)

# 7. Criar caldeira v2 com os bocais montados
result = Image.new('RGBA', (W, H), (0, 0, 0, 0))

# Colar bocal esquerdo em y_center = 482, x terminando em 220
# nozzle_left tem largura nozzle_left.width (~200px)
# Queremos que ele encoste na fornalha/corpo (x ≈ 210) e va para a esquerda ate a borda
paste_y_left = 482 - center_y
result.paste(nozzle_left, (10, paste_y_left), nozzle_left)

# Colar corpo limpo da caldeira
result.paste(cal_clean, (0, 0), cal_clean)

# Colar bocal direito em y_center = 399, saindo da gola em x ≈ 630
paste_y_right = 399 - center_y
result.paste(nozzle_right, (625, paste_y_right), nozzle_right)

# 8. Blending suave e retoque das emendas
res_arr = np.array(result)
# Aplicar despill suave
# Salvar caldeira_v2.png
result.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\caldeira_v2_clean.png')
print('caldeira_v2_clean.png gerada com sucesso!')
