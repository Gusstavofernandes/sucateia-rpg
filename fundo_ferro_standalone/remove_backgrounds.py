import os
from PIL import Image
from rembg import remove

assets_dir = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets"

files = ["reator_arcano.jpg", "bomba_esgoto.jpg", "poco_velho.jpg"]

print("Iniciando remoção automatizada de fundo dos assets...")

for fname in files:
    in_path = os.path.join(assets_dir, fname)
    out_name = os.path.splitext(fname)[0] + ".png"
    out_path = os.path.join(assets_dir, out_name)
    
    print(f"Processando {fname} -> {out_name}...")
    with Image.open(in_path) as input_img:
        output_img = remove(input_img)
        output_img.save(out_path, format="PNG")
    print(f"✓ Salvo com sucesso: {out_path}")

print("Todos os assets foram convertidos para PNG transparente!")
