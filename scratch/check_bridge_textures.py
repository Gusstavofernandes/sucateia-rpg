import os
from PIL import Image

for t in ['cavalete_alto_v1.png', 'trilho_reto_vertical_v1.png']:
    p = os.path.join('fundo_ferro_standalone/assets/rails', t)
    img = Image.open(p)
    print(f"{t}: size={img.size}")

# Vamos verificar ExtResource 73, 74, 75, 77, 78, 79 na cena
with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if any(k in line for k in ['73_cavalete', '74_cavalete', '75_trilho', '77_carrinho', '78_carrinho', '79_carrinho']):
        print(line)
