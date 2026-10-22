import os
from PIL import Image

assets_dir = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets"
files = ["reator_arcano.jpg", "bomba_esgoto.jpg", "poco_velho.jpg"]

for fname in files:
    in_path = os.path.join(assets_dir, fname)
    out_name = os.path.splitext(fname)[0] + ".png"
    out_path = os.path.join(assets_dir, out_name)
    
    img = Image.open(in_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            brightness = (r + g + b) / 3.0
            if brightness < 30:
                alpha = int(max(0, (brightness - 10) * 12))
                pixels[x, y] = (r, g, b, alpha)
            else:
                pixels[x, y] = (r, g, b, 255)
            
    img.save(out_path, "PNG")
    print(f"Processado: {out_name}")

print("Fast Alpha Process concluido!")
