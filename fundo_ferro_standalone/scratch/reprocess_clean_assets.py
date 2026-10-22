import os, sys
from PIL import Image, ImageFilter
import numpy as np
from scipy import ndimage

brain_dir = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b"
dest_dirs = [
    r"c:\Users\Usuario\Documents\jogo\assets\machines",
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\machines"
]
pipe_dirs = [
    r"c:\Users\Usuario\Documents\jogo\assets\pipes",
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes"
]
puddle_dirs = [
    r"c:\Users\Usuario\Documents\jogo\assets\puddles",
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\puddles"
]

def clean_chroma_and_despill(img_rgb, erode_iters=2):
    arr = np.array(img_rgb).astype(float)
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    
    # Magenta metric: high R, high B, low G
    # Chroma key mask where background is magenta
    magenta_diff = ((r + b) / 2.0) - g
    bg_mask = (magenta_diff > 45) & (r > 120) & (b > 120)
    
    # Object mask
    fg_mask = ~bg_mask
    
    # Erode foreground mask by erode_iters to eat the fringe
    if erode_iters > 0:
        fg_mask = ndimage.binary_erosion(fg_mask, iterations=erode_iters)
    
    # Alpha channel from eroded mask
    alpha = np.zeros_like(r, dtype=np.uint8)
    alpha[fg_mask] = 255
    
    # Smooth edges slightly for clean antialiasing
    alpha_img = Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(radius=0.7))
    alpha_clean = np.array(alpha_img)
    
    # Aggressive Despill Filter:
    # If a foreground pixel still has excess magenta ((R+B)/2 > G), neutralize it
    excess = ((r + b) / 2.0) - (g + 5.0)
    has_spill = (excess > 0) & (alpha_clean > 0)
    
    r_corr = r.copy()
    b_corr = b.copy()
    
    # Pull R and B down to eliminate magenta hue entirely
    r_corr[has_spill] = np.clip(r[has_spill] - excess[has_spill] * 1.25, 0, 255)
    b_corr[has_spill] = np.clip(b[has_spill] - excess[has_spill] * 1.25, 0, 255)
    
    # Output RGBA
    out = np.dstack([
        r_corr.astype(np.uint8),
        g.astype(np.uint8),
        b_corr.astype(np.uint8),
        alpha_clean
    ])
    return Image.fromarray(out)

def create_smooth_isometric_shadow(width, height, footprint_ratio=0.55):
    # Generates a smooth, textureless contact shadow in isometric perspective
    sw = int(width * 0.95)
    sh = int(height * footprint_ratio)
    
    # Create coordinate grid centered at (sw/2, sh/2)
    y, x = np.ogrid[-sh/2:sh/2, -sw/2:sw/2]
    
    # Isometric diamond metric: (|x| / (sw/2)) + (|y| / (sh/2))
    # with elliptical smoothing
    norm_x = (x / (sw * 0.46)) ** 2
    norm_y = (y / (sh * 0.46)) ** 2
    dist_sq = norm_x + norm_y
    
    # Smooth Gaussian falloff from 1.0 down to 0.0
    alpha_map = np.exp(-dist_sq * 2.2) * 255.0
    alpha_map[dist_sq > 1.3] = 0.0
    alpha_map = np.clip(alpha_map * 0.58, 0, 255).astype(np.uint8)
    
    # Gaussian blur for soft shadow edge
    alpha_img = Image.fromarray(alpha_map).filter(ImageFilter.GaussianBlur(radius=10))
    alpha_arr = np.array(alpha_img)
    
    # Pure black RGB
    shadow = np.zeros((sh, sw, 4), dtype=np.uint8)
    shadow[:, :, 3] = alpha_arr
    return Image.fromarray(shadow)

# Process Machines
machines = [
    ("maquina_bomba_funcional_v1_1791259218163.jpg", "maquina_bomba_funcional_v1"),
    ("maquina_caldeira_vapor_v1_1791261301562.jpg", "maquina_caldeira_vapor_v1"),
    ("maquina_manifold_valvulas_v1_1791261487373.jpg", "maquina_manifold_valvulas_v1"),
    ("maquina_tanque_decantador_v1_1791261657291.jpg", "maquina_tanque_decantador_v1"),
    ("maquina_gerador_dinamo_v1_1791261812923.jpg", "maquina_gerador_dinamo_v1"),
    ("maquina_motor_desmontado_v1_1791261972903.jpg", "maquina_motor_desmontado_v1")
]

print("=== REPROCESSANDO MAQUINAS COM DESPILL E EROSAO ===")
for raw_name, clean_name in machines:
    raw_path = os.path.join(brain_dir, raw_name)
    if not os.path.exists(raw_path):
        print(f"AVISO: {raw_name} nao encontrado!")
        continue
    raw_img = Image.open(raw_path).convert('RGB')
    cleaned = clean_chroma_and_despill(raw_img, erode_iters=2)
    
    # Tight crop
    bbox = cleaned.getbbox()
    if bbox:
        cleaned = cleaned.crop(bbox)
        
    # Normalized scale (width 768)
    w, h = cleaned.size
    target_w = 768
    target_h = int(h * (target_w / float(w)))
    cleaned = cleaned.resize((target_w, target_h), Image.Resampling.LANCZOS)
    
    # Generate smooth isometric contact shadow (P0.2)
    shadow = create_smooth_isometric_shadow(target_w, int(target_w * 0.48))
    
    for d in dest_dirs:
        os.makedirs(d, exist_ok=True)
        cleaned.save(os.path.join(d, f"{clean_name}.png"))
        shadow.save(os.path.join(d, f"{clean_name}_sombra.png"))
    print(f"Processado: {clean_name}.png ({cleaned.size}) e sombra ({shadow.size})")

# Process Pipes
print("\n=== REPROCESSANDO KIT DE TUBULACAO MODULAR ===")
pipes_file = os.path.join(brain_dir, "kit_tubulacao_modular_v1_1791262140518.jpg")
if os.path.exists(pipes_file):
    raw_img = Image.open(pipes_file).convert('RGB')
    cleaned_pipes = clean_chroma_and_despill(raw_img, erode_iters=2)
    
    alpha = np.array(cleaned_pipes.split()[-1])
    mask = alpha > 30
    labeled, num_features = ndimage.label(mask)
    objects = ndimage.find_objects(labeled)
    
    valid = []
    for i, obj in enumerate(objects):
        area = np.sum(mask[obj])
        if area > 10000:
            valid.append((obj, area))
            
    valid.sort(key=lambda x: (x[0][0].start // 400, x[0][1].start))
    names = [
        'tubo_vertical_flange',
        'tubo_cotovelo_90',
        'tubo_t_juncao',
        'tubo_horizontal_valvula',
        'tubo_suporte_piso'
    ]
    for idx, (obj, area) in enumerate(valid):
        ymin, ymax = obj[0].start, obj[0].stop
        xmin, xmax = obj[1].start, obj[1].stop
        cropped = cleaned_pipes.crop((xmin, ymin, xmax, ymax))
        name = names[idx] if idx < len(names) else f'tubo_peca_{idx}'
        
        # Smooth shadow for pipe
        pw, ph = cropped.size
        pshadow = create_smooth_isometric_shadow(pw, int(ph * 0.40))
        
        for d in pipe_dirs:
            os.makedirs(d, exist_ok=True)
            cropped.save(os.path.join(d, f"{name}.png"))
            pshadow.save(os.path.join(d, f"{name}_sombra.png"))
        print(f"Tubo processado: {name}.png ({cropped.size})")

# Process Puddles
print("\n=== REPROCESSANDO POCAS COM DESPILL E RECOLORACAO DE CONDENSADO ===")
puddles_file = os.path.join(brain_dir, "sprites_pocas_esgoto_v1_1791262309820.jpg")
if os.path.exists(puddles_file):
    raw_img = Image.open(puddles_file).convert('RGB')
    cleaned_puddles = clean_chroma_and_despill(raw_img, erode_iters=2)
    
    alpha = np.array(cleaned_puddles.split()[-1])
    mask = alpha > 25
    labeled, num_features = ndimage.label(mask)
    objects = ndimage.find_objects(labeled)
    
    valid = []
    for i, obj in enumerate(objects):
        area = np.sum(mask[obj])
        if area > 15000:
            valid.append((obj, area))
            
    valid.sort(key=lambda x: (x[0][0].start // 300, x[0][1].start))
    pnames = [
        'poca_oleo_ambar',
        'poca_toxica_limo',
        'poca_esgoto_detritos',
        'poca_ferrugem_lodo'
    ]
    for idx, (obj, area) in enumerate(valid):
        ymin, ymax = obj[0].start, obj[0].stop
        xmin, xmax = obj[1].start, obj[1].stop
        cropped = cleaned_puddles.crop((xmin, ymin, xmax, ymax))
        name = pnames[idx] if idx < len(pnames) else f'poca_peca_{idx}'
        
        # P0.5 Fix: Recolor poca_ferrugem_lodo (the orange lava puddle) into warm dark condensate/hot oil
        if name == 'poca_ferrugem_lodo':
            arr = np.array(cropped).astype(float)
            r, g, b, a = arr[:,:,0], arr[:,:,1], arr[:,:,2], arr[:,:,3]
            # Convert vivid bright orange into deep dark amber/black industrial condensate
            # Reduce brightness and shift hue to dark oily amber
            dark_factor = 0.42
            r_new = np.clip(r * dark_factor * 1.3, 0, 255)
            g_new = np.clip(g * dark_factor * 0.8, 0, 255)
            b_new = np.clip(b * dark_factor * 0.4, 0, 255)
            arr[:,:,0] = r_new
            arr[:,:,1] = g_new
            arr[:,:,2] = b_new
            # Clean any corner artifacts
            edge_cut = (a > 0)
            cropped = Image.fromarray(arr.astype(np.uint8))
        
        # P0.2 Fix: Ensure poca_oleo_ambar is a natural puddle, not a hard-edged vortex disk
        if name == 'poca_oleo_ambar':
            arr = np.array(cropped).astype(float)
            # Soften outer edges
            a_img = Image.fromarray(arr[:,:,3].astype(np.uint8)).filter(ImageFilter.GaussianBlur(radius=2.5))
            arr[:,:,3] = np.array(a_img)
            cropped = Image.fromarray(arr.astype(np.uint8))
            
        for d in puddle_dirs:
            os.makedirs(d, exist_ok=True)
            cropped.save(os.path.join(d, f"{name}.png"))
        print(f"Poca processada: {name}.png ({cropped.size})")

print("\n=== REPROCESSAMENTO CONCLUIDO COM SUCESSO! ===")
