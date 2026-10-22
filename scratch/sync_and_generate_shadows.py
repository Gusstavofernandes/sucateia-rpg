import os
import shutil
from PIL import Image, ImageFilter, ImageOps

src_dir = r'c:\Users\Usuario\Documents\jogo\assets\reconstruction'
dst_dir = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\reconstruction'
os.makedirs(dst_dir, exist_ok=True)

files = [
    'forjas_recycler.png',
    'cloth_stall.png',
    'market_salvage_cart.png',
    'forjas_workshop.png',
    'exchange_pavilion.png',
    'wholesale_arcade.png',
    'fundo_sorting_bank.png',
    'fundo_abandoned_engine.png',
    'fundo_collapsed_corner.png',
    'alto_cistern.png'
]

print("=== COPIANDO E GERANDO SOMBRAS DE CONTATO ===")
for fname in files:
    src_path = os.path.join(src_dir, fname)
    dst_path = os.path.join(dst_dir, fname)
    
    # 1. Copiar imagem principal para standalone
    shutil.copy2(src_path, dst_path)
    
    # Se existir .import na raiz, copiar também
    src_import = src_path + '.import'
    if os.path.exists(src_import):
        shutil.copy2(src_import, dst_path + '.import')
        
    # 2. Gerar sombra de contato
    img = Image.open(src_path).convert("RGBA")
    w, h = img.size
    
    # Extrair canal alpha
    alpha = img.split()[3]
    
    # Criar imagem preta com o alpha
    black = Image.new("RGBA", (w, h), (0, 0, 0, 255))
    black.putalpha(alpha)
    
    # Isolar a base (últimos 35% de altura do objeto)
    bbox = img.getbbox()
    base_top = int(bbox[1] + (bbox[3] - bbox[1]) * 0.65)
    base_mask = Image.new("L", (w, h), 0)
    base_alpha = alpha.crop((0, base_top, w, h))
    base_mask.paste(base_alpha, (0, base_top))
    
    # Criar sombra oval/achatada na base
    shadow_raw = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    # Colocar a forma da base com opacidade moderada
    shadow_base = Image.new("RGBA", (w, h), (0, 0, 0, 160))
    shadow_base.putalpha(base_mask)
    
    # Achatar verticalmente e borrar
    squish_h = int(h * 0.4)
    squished = shadow_base.resize((w, squish_h), Image.Resampling.BILINEAR)
    squished = squished.filter(ImageFilter.GaussianBlur(radius=14))
    
    # Reposicionar na base da imagem original
    final_shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    paste_y = bbox[3] - squish_h + 10
    final_shadow.paste(squished, (10, paste_y), squished)
    
    # Salvar sombra tanto em assets/reconstruction quanto em standalone
    sombra_name = fname.replace('.png', '_sombra.png')
    sombra_src = os.path.join(src_dir, sombra_name)
    sombra_dst = os.path.join(dst_dir, sombra_name)
    
    final_shadow.save(sombra_src)
    final_shadow.save(sombra_dst)
    print(f"Processado: {fname} -> Sombra gerada: {sombra_name}")

print("Concluído com sucesso!")
