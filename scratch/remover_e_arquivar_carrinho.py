import os
import shutil
import re

print("--- 1. CRIANDO PASTAS _ARQUIVO E PRESERVANDO ASSETS DO CARRINHO ---")

pastas_arquivo = [
    'fundo_ferro_standalone/assets/rails/_arquivo',
    'assets/rails/_arquivo'
]

for p in pastas_arquivo:
    os.makedirs(p, exist_ok=True)
    print(f"Diretório garantido: {p}")

# Lista de arquivos do carrinho para preservar em _arquivo/
carrinho_files = [
    'carrinho_mina_vertical_v1.png',
    'carrinho_mina_vertical_v1.png.import',
    'carrinho_mina_vertical_v1.txt',
    'carrinho_mina_vertical_v1_sombra.png',
    'carrinho_mina_vertical_v1_sombra.png.import',
    'carrinho_cheio_v1.png',
    'carrinho_cheio_v1.png.import',
    'carrinho_cheio_v1.txt',
    'carrinho_cheio_v1_sombra.png',
    'carrinho_cheio_v1_sombra.png.import'
]

for base in ['fundo_ferro_standalone/assets/rails', 'assets/rails']:
    dst_dir = os.path.join(base, '_arquivo')
    for f in carrinho_files:
        src = os.path.join(base, f)
        dst = os.path.join(dst_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copiado para preservação: {src} -> {dst}")

# Preservar também o script do carrinho
script_src = 'fundo_ferro_standalone/scripts/carrinho_mina.gd'
if os.path.exists(script_src):
    shutil.copy2(script_src, 'fundo_ferro_standalone/assets/rails/_arquivo/carrinho_mina.gd')
    shutil.copy2(script_src, 'assets/rails/_arquivo/carrinho_mina.gd')
    print("Script do carrinho preservado em _arquivo/!")

print("\n--- 2. REMOVENDO NÓ DO CARRINHO DAS CENAS MASTER ---")
def remover_carrinho_da_cena(scene_path):
    print(f"Limpando {scene_path}...")
    with open(scene_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    # Remover nó CarrinhoMinerio e todos os seus filhos (Sombra, Sprite, Luz)
    # Padrão: de [node name="CarrinhoMinerio" até o próximo nó de nível superior ou final de RedeFerroviariaMina
    pattern = r'\[node name="CarrinhoMinerio" type="Node2D" parent="RedeFerroviariaMina"\][\s\S]*?(?=\[node name="Player")'
    if re.search(pattern, text):
        text = re.sub(pattern, '', text)
        print("Nó CarrinhoMinerio e filhos removidos com sucesso!")
    else:
        print("Aviso: CarrinhoMinerio não encontrado com regex padrão, verificando...")
        
    with open(scene_path, 'w', encoding='utf-8') as f:
        f.write(text)

remover_carrinho_da_cena('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn')
remover_carrinho_da_cena('scenes/fundo_ferro_master.tscn')
