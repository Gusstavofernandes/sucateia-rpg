import os
from PIL import Image, ImageFilter
import numpy as np

# 1. Carregar pipe para extrair boca_bocal_conexao
pipe_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes\cano_longo_industrial.png'
pipe = Image.open(pipe_path).convert('RGBA')

# Em pipe (1376x316), o anel com parafusos sextavados esta em x=205..345, y=30..286
# Vamos recortar com um pouco de tubo dos dois lados para formar a uniao flangeada perfeita
flange_crop = pipe.crop((180, 20, 360, 296))

# Criar bordas suaves transparentes
flange_w, flange_h = flange_crop.size
flange_clean = flange_crop.copy()

out_dir = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes'
flange_clean.save(os.path.join(out_dir, 'boca_bocal_conexao.png'))
print('boca_bocal_conexao.png salva!')

# Criar sombra correspondente para a boca_bocal_conexao
sombra = Image.new('RGBA', (flange_w, flange_h), (0, 0, 0, 0))
f_arr = np.array(flange_clean)
s_arr = np.array(sombra)

# A sombra eh a silhueta preta suave deslocada
alpha = f_arr[:, :, 3]
s_arr[:, :, 0] = 0
s_arr[:, :, 1] = 0
s_arr[:, :, 2] = 0
s_arr[:, :, 3] = (alpha * 0.45).astype(np.uint8)

sombra = Image.fromarray(s_arr).filter(ImageFilter.GaussianBlur(radius=3))
sombra.save(os.path.join(out_dir, 'boca_bocal_conexao_sombra.png'))
print('boca_bocal_conexao_sombra.png salva!')
