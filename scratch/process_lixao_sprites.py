import os
from PIL import Image, ImageFilter
import numpy as np

images_to_process = [
    {
        'src': r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\lixao_montanha_sucata_principal_1792583213407.jpg',
        'out_name': 'lixao_montanha_sucata_principal.png'
    },
    {
        'src': r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\lixao_duna_tubos_engrenagens_1792583409726.jpg',
        'out_name': 'lixao_duna_tubos_engrenagens.png'
    },
    {
        'src': r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\lixao_guindaste_eletroima_1792583574809.jpg',
        'out_name': 'lixao_guindaste_eletroima.png'
    }
]

out_dirs = [
    r'c:\Users\Usuario\Documents\jogo\assets\props',
    r'c:\Users\Usuario\Documents\jogo\assets\reconstruction'
]

for item in images_to_process:
    src_path = item['src']
    out_name = item['out_name']
    sombra_name = out_name.replace('.png', '_sombra.png')
    
    img = Image.open(src_path).convert("RGBA")
    arr = np.array(img, dtype=np.float32)
    
    # Magenta keying: Magenta is R ~ 255, G ~ 0, B ~ 255
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    # Calculate distance to pure magenta (255, 0, 255)
    magenta_dist = np.sqrt((r - 255.0)**2 + (g - 0.0)**2 + (b - 255.0)**2)
    
    # Calculate alpha based on magenta distance
    # Near magenta (< 60): alpha = 0
    # Blend zone (60 to 110): smooth step
    alpha = np.clip((magenta_dist - 55.0) / 45.0, 0.0, 1.0)
    
    # Desaturate any magenta fringing on semi-transparent edge pixels
    edge_mask = (alpha > 0.0) & (alpha < 0.98)
    # If a pixel has high R and B and low G, pull R and B towards G/neutral
    is_pink = (r > 150) & (b > 150) & (g < 100) & edge_mask
    arr[is_pink, 0] = arr[is_pink, 1] * 0.8 + 40
    arr[is_pink, 2] = arr[is_pink, 1] * 0.8 + 40
    
    arr[:, :, 3] = (alpha * 255.0).astype(np.uint8)
    clean_img = Image.fromarray(arr.astype(np.uint8), mode="RGBA")
    
    # Trim empty borders slightly if needed
    bbox = clean_img.getbbox()
    if bbox:
        # keep margin
        pass
        
    w, h = clean_img.size
    
    # Generate Contact Shadow
    alpha_chan = clean_img.split()[3]
    base_top = int(bbox[1] + (bbox[3] - bbox[1]) * 0.70) if bbox else int(h * 0.7)
    base_mask = Image.new("L", (w, h), 0)
    base_alpha = alpha_chan.crop((0, base_top, w, h))
    base_mask.paste(base_alpha, (0, base_top))
    
    shadow_base = Image.new("RGBA", (w, h), (0, 0, 0, 170))
    shadow_base.putalpha(base_mask)
    squish_h = int(h * 0.35)
    squished = shadow_base.resize((w, squish_h), Image.Resampling.BILINEAR)
    squished = squished.filter(ImageFilter.GaussianBlur(radius=16))
    
    final_shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    paste_y = bbox[3] - squish_h + 8 if bbox else h - squish_h
    final_shadow.paste(squished, (8, paste_y), squished)
    
    # Save to all destination directories
    for od in out_dirs:
        os.makedirs(od, exist_ok=True)
        clean_img.save(os.path.join(od, out_name))
        final_shadow.save(os.path.join(od, sombra_name))
        
    print(f"Salvo {out_name} e {sombra_name} com sucesso! BBox={bbox}")

print("Todos os sprites foram processados e limpos!")
