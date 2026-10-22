import os
import shutil
from PIL import Image, ImageFilter

src_dir = r'c:\Users\Usuario\Documents\jogo\assets\reconstruction'
dst_dir = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\reconstruction'

fname = 'forjas_boiler_hall.png'
src_path = os.path.join(src_dir, fname)
dst_path = os.path.join(dst_dir, fname)

shutil.copy2(src_path, dst_path)

img = Image.open(src_path).convert("RGBA")
w, h = img.size
alpha = img.split()[3]
bbox = img.getbbox()

base_top = int(bbox[1] + (bbox[3] - bbox[1]) * 0.65)
base_mask = Image.new("L", (w, h), 0)
base_alpha = alpha.crop((0, base_top, w, h))
base_mask.paste(base_alpha, (0, base_top))

shadow_base = Image.new("RGBA", (w, h), (0, 0, 0, 160))
shadow_base.putalpha(base_mask)

squish_h = int(h * 0.4)
squished = shadow_base.resize((w, squish_h), Image.Resampling.BILINEAR)
squished = squished.filter(ImageFilter.GaussianBlur(radius=14))

final_shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
paste_y = bbox[3] - squish_h + 10
final_shadow.paste(squished, (10, paste_y), squished)

sombra_name = 'forjas_boiler_hall_sombra.png'
final_shadow.save(os.path.join(src_dir, sombra_name))
final_shadow.save(os.path.join(dst_dir, sombra_name))
print(f"Gerado {sombra_name} com sucesso! BBox={bbox}")
