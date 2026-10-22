import os
from PIL import Image

assets_dir = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets"

files_to_clean = ["parede_rocha_ferro.jpg", "tanque_quimico.jpg", "ponte_grade_metal.jpg"]

for fname in files_to_clean:
    in_path = os.path.join(assets_dir, fname)
    out_name = os.path.splitext(fname)[0] + ".png"
    out_path = os.path.join(assets_dir, out_name)
    
    img = Image.open(in_path).convert("RGBA")
    pixels = img.load()
    width, height = img.size
    
    corner_colors = [pixels[0,0], pixels[width-1, 0], pixels[0, height-1], pixels[width-1, height-1]]
    bg_r = sum(c[0] for c in corner_colors) / 4.0
    bg_g = sum(c[1] for c in corner_colors) / 4.0
    bg_b = sum(c[2] for c in corner_colors) / 4.0
    
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            dist = ((r - bg_r)**2 + (g - bg_g)**2 + (b - bg_b)**2)**0.5
            brightness = (r + g + b) / 3.0
            
            if dist < 42 or brightness < 30:
                alpha = int(max(0, min(255, (dist - 14) * 8)))
                pixels[x, y] = (r, g, b, alpha)
            else:
                pixels[x, y] = (r, g, b, 255)
                
    img.save(out_path, "PNG")
    print("Salvo PNG transparente:", out_name)

print("Processamento concluido!")
