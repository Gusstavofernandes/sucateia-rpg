import os
from PIL import Image

assets_dir = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets"

def process_image(fname, threshold=45):
    in_path = os.path.join(assets_dir, fname)
    out_name = os.path.splitext(fname)[0] + ".png"
    out_path = os.path.join(assets_dir, out_name)
    
    img = Image.open(in_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    # Sample corner pixel colors as background sample
    corner_colors = [pixels[0,0], pixels[width-1, 0], pixels[0, height-1], pixels[width-1, height-1]]
    bg_r = sum(c[0] for c in corner_colors) / 4.0
    bg_g = sum(c[1] for c in corner_colors) / 4.0
    bg_b = sum(c[2] for c in corner_colors) / 4.0
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            dist = ((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)**0.5
            brightness = (r + g + b) / 3.0
            
            if dist < threshold or brightness < 32:
                alpha = int(max(0, min(255, (dist - 15) * 8)))
                pixels[x, y] = (r, g, b, alpha)
            else:
                pixels[x, y] = (r, g, b, 255)
                
    img.save(out_path, "PNG")
    print(f"Fundo removido: {out_name}")

process_image("reator_arcano.jpg", threshold=35)
process_image("bomba_esgoto.jpg", threshold=40)
process_image("poco_velho.jpg", threshold=42)

print("Processamento concluido!")
