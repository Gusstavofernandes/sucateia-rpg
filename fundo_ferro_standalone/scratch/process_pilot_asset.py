import os
import numpy as np
from PIL import Image, ImageFilter

src_path = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\bomba_hidraulica_v1_1791259218163.jpg'
dest_dir = r'c:\Users\Usuario\Documents\jogo\assets\machines'
standalone_dest_dir = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\machines'
os.makedirs(dest_dir, exist_ok=True)
os.makedirs(standalone_dest_dir, exist_ok=True)

img = Image.open(src_path).convert('RGB')
arr = np.array(img).astype(np.float32)

r = arr[:, :, 0]
g = arr[:, :, 1]
b = arr[:, :, 2]

# Magenta detection: Pure magenta is R=255, G=0, B=255.
# In generated images, magenta background has R > 200, G < 60, B > 200.
# Let's compute color distance from magenta (255, 0, 255)
# In normalized space:
magenta_diff = np.sqrt((r - 255.0)**2 + (g - 0.0)**2 + (b - 255.0)**2)
# Also check ratio: (R + B) / 2 - G
rb_excess = ((r + b) / 2.0) - g

# Create smooth alpha matte
# Foreground has rb_excess much lower (since machine has green patina, brown rust, brass).
# Background has rb_excess > 180 and magenta_diff < 100.
is_bg = (rb_excess > 120.0) & (g < 95.0)

# Soft boundary with smoothstep
alpha_raw = np.clip((120.0 - (rb_excess - g * 0.5)) / 40.0, 0.0, 1.0)
alpha_raw[is_bg] = 0.0

# Refine with morphological cleanup
alpha_uint8 = (alpha_raw * 255.0).astype(np.uint8)
alpha_pil = Image.fromarray(alpha_uint8)

# Defringe / remove magenta halo from edges:
# Where alpha is between 1 and 254 and R/B is higher than G, replace edge tint with neutral/green patina
clean_rgb = arr.copy()
edge_pixels = (alpha_raw > 0.0) & (alpha_raw < 0.98)
clean_rgb[edge_pixels, 0] = np.minimum(clean_rgb[edge_pixels, 0], clean_rgb[edge_pixels, 1] * 1.2 + 40.0)
clean_rgb[edge_pixels, 2] = np.minimum(clean_rgb[edge_pixels, 2], clean_rgb[edge_pixels, 1] * 1.1 + 40.0)

rgba = np.dstack([
    np.clip(clean_rgb, 0, 255).astype(np.uint8),
    alpha_uint8
])

clean_img = Image.fromarray(rgba)

# Find bounding box
bbox = clean_img.getbbox()
print("Original bbox:", bbox)
# Add small 8px margin
w, h = clean_img.size
pad = 8
crop_box = (
    max(0, bbox[0] - pad),
    max(0, bbox[1] - pad),
    min(w, bbox[2] + pad),
    min(h, bbox[3] + pad)
)
cropped = clean_img.crop(crop_box)
print("Cropped size:", cropped.size)

# Resize to standardized game resolution (768x768 or 512x512)
final_machine = cropped.resize((768, int(768 * cropped.size[1] / cropped.size[0])), Image.Resampling.LANCZOS)

# Create contact shadow (separate sprite, multiplied)
# Shadow is a soft flattened diamond matching the base plate, offset down-right
sw, sh = final_machine.size
shadow_canvas = Image.new('RGBA', (sw, sh), (0, 0, 0, 0))
# Create shadow mask by thresholding bottom part of machine alpha, blurring, and tinting black
m_alpha = np.array(final_machine)[:, :, 3]
base_mask = m_alpha.copy()
# Only keep bottom 45% (where base plate touches ground)
y_ramp = np.linspace(0, 1, sh)[:, None]
base_mask = (base_mask.astype(np.float32) * np.clip((y_ramp - 0.55) / 0.35, 0.0, 1.0)).astype(np.uint8)

base_shadow = Image.fromarray(base_mask).filter(ImageFilter.GaussianBlur(radius=14))
shadow_arr = np.zeros((sh, sw, 4), dtype=np.uint8)
# Dark contact shadow with 65% opacity
shadow_arr[:, :, 3] = (np.array(base_shadow).astype(np.float32) * 0.70).astype(np.uint8)
shadow_img = Image.fromarray(shadow_arr)

# Save files
for target_folder in [dest_dir, standalone_dest_dir]:
    machine_path = os.path.join(target_folder, 'maquina_bomba_funcional_v1.png')
    shadow_path = os.path.join(target_folder, 'maquina_bomba_funcional_v1_sombra.png')
    prompt_path = os.path.join(target_folder, 'maquina_bomba_funcional_v1_prompt.txt')
    
    final_machine.save(machine_path)
    shadow_img.save(shadow_path)
    
    prompt_text = """PROMPT NANO BANANA:
Game asset, isometric 3/4 top-down view, same camera angle and painted style as the reference images. A hydraulic pump machine with heavy cast-iron base in a steampunk goblin underground sewer. Heavily detailed hand-painted texture: rusted cast iron, oxidized copper, turquoise green patina, iron rivets, brass fittings, flanged pipes, small brass pressure gauge with needle. Warm amber lighting from the upper left, subtle green ambient bounce from toxic sewer fluid. Visible open pipe stubs and flanged ports: 1 inlet flanged pipe on left side, 1 outlet flanged pipe on right side, 1 maintenance hand-wheel valve on front. Sits flat on a diamond shaped riveted iron base plate. State: functional. Isolated on a flat solid magenta (#FF00FF) background, no floor, no cast shadow on the background, no text, no UI, no characters, no watermark, sharp edges, centered, full object visible with margin.

ESPECIFICAÇÕES TÉCNICAS:
- Tipo: Bomba Hidráulica Principal
- Estado: Funcional
- Entradas/Saídas: Flange aberta à esquerda (sucção), flange aberta à direita (recalque), volante frontal (registro)
- Base: Losango rebitado de ferro fundido apoiado no piso
- Iluminação: Âmbar superior-esquerda, bounce verde tóxico
- Dimensões: 768px (escala operável por goblin)
"""
    with open(prompt_path, 'w', encoding='utf-8') as pf:
        pf.write(prompt_text)

print("Processamento concluído com sucesso!")
