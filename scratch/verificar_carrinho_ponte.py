import os
from PIL import Image

# 1. Inspecionar cena
scene_path = 'fundo_ferro_standalone/scenes/fundo_ferro_master.tscn'
with open(scene_path, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
in_rede = False
ponte_lines = []
carrinho_lines = []

curr_target = None
for l in lines:
    if 'name="CavaleteElevadoCanal"' in l:
        curr_target = 'ponte'
    elif 'name="CarrinhoMinerio"' in l:
        curr_target = 'carrinho'
    elif curr_target and l.startswith('[node name="') and 'parent="RedeFerroviariaMina/' not in l:
        curr_target = None
        
    if curr_target == 'ponte':
        ponte_lines.append(l)
    elif curr_target == 'carrinho':
        carrinho_lines.append(l)

print("--- NÓS DA PONTE NA CENA ---")
print("\n".join(ponte_lines))

print("\n--- NÓS DO CARRINHO NA CENA ---")
print("\n".join(carrinho_lines))

# 2. Inspecionar texturas da ponte
print("\n--- TEXTURAS DA PONTE ---")
for t in ['cavalete_alto_v1.png', 'trilho_vertical.png', 'trilho_reto_vertical_v1.png', 'cavalete_alto.png']:
    for base in ['fundo_ferro_standalone/assets/rails', 'assets/rails', 'fundo_ferro_standalone/assets', 'assets']:
        p = os.path.join(base, t)
        if os.path.exists(p):
            im = Image.open(p)
            print(f"Encontrado {p}: tamanho {im.size}, modo {im.mode}")
