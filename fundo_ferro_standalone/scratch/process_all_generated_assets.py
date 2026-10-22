import os
import numpy as np
from PIL import Image, ImageFilter

brain_dir = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b'
dest_dirs = [
    r'c:\Users\Usuario\Documents\jogo\assets\machines',
    r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\machines'
]
for d in dest_dirs:
    os.makedirs(d, exist_ok=True)

def chroma_key_magenta(img):
    arr = np.array(img).astype(np.float32)
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Excess of magenta components over green
    rb_excess = ((r + b) / 2.0) - g
    
    # Magenta background mask
    is_bg = (rb_excess > 125.0) & (g < 95.0)
    
    # Smooth alpha falloff
    alpha_raw = np.clip((125.0 - (rb_excess - g * 0.5)) / 35.0, 0.0, 1.0)
    alpha_raw[is_bg] = 0.0
    
    # Defringe / clean edges
    clean_rgb = arr.copy()
    edge_pixels = (alpha_raw > 0.0) & (alpha_raw < 0.98)
    clean_rgb[edge_pixels, 0] = np.minimum(clean_rgb[edge_pixels, 0], clean_rgb[edge_pixels, 1] * 1.25 + 35.0)
    clean_rgb[edge_pixels, 2] = np.minimum(clean_rgb[edge_pixels, 2], clean_rgb[edge_pixels, 1] * 1.15 + 35.0)
    
    rgba = np.dstack([
        np.clip(clean_rgb, 0, 255).astype(np.uint8),
        (alpha_raw * 255.0).astype(np.uint8)
    ])
    
    res = Image.fromarray(rgba)
    bbox = res.getbbox()
    if bbox:
        pad = 8
        crop_box = (
            max(0, bbox[0] - pad),
            max(0, bbox[1] - pad),
            min(res.width, bbox[2] + pad),
            min(res.height, bbox[3] + pad)
        )
        res = res.crop(crop_box)
    return res

def make_contact_shadow(clean_img):
    sw, sh = clean_img.size
    m_alpha = np.array(clean_img)[:, :, 3]
    y_ramp = np.linspace(0, 1, sh)[:, None]
    base_mask = (m_alpha.astype(np.float32) * np.clip((y_ramp - 0.58) / 0.32, 0.0, 1.0)).astype(np.uint8)
    base_shadow = Image.fromarray(base_mask).filter(ImageFilter.GaussianBlur(radius=16))
    
    shadow_arr = np.zeros((sh, sw, 4), dtype=np.uint8)
    shadow_arr[:, :, 3] = (np.array(base_shadow).astype(np.float32) * 0.65).astype(np.uint8)
    return Image.fromarray(shadow_arr)

# Catalog of generated images to process
machines_to_process = [
    {
        "file": "maquina_caldeira_vapor_v1_1791261301562.jpg",
        "name": "maquina_caldeira_vapor_v1",
        "size": 768,
        "prompt": "Caldeira industrial de vapor vertical com fornalha inferior brilhante, chamine curvada, valvula de alivio, manometro, conexao de entrada inferior e saida de vapor superior flangeada."
    },
    {
        "file": "maquina_manifold_valvulas_v1_1791261487373.jpg",
        "name": "maquina_manifold_valvulas_v1",
        "size": 768,
        "prompt": "Estacao de valvulas e manifold com tubo barrilete principal, 3 ramais de distribuicao com volantes de registro, manometros e conexoes flangeadas abertas."
    },
    {
        "file": "maquina_tanque_decantador_v1_1791261657291.jpg",
        "name": "maquina_tanque_decantador_v1",
        "size": 768,
        "prompt": "Tanque decantador cilindrico com visor de nivel de liquido verde toxico, agitador mecanico superior, bocal de entrada superior e saida inferior com calha de rejeito."
    },
    {
        "file": "maquina_gerador_dinamo_v1_1791261812923.jpg",
        "name": "maquina_gerador_dinamo_v1",
        "size": 768,
        "prompt": "Gerador dinamo de forca eletrica com bobinas de cobre aparentes com fasca azul, eixo com engrenagem denteada, caixa de bornes e conduites reforçados."
    },
    {
        "file": "maquina_motor_desmontado_v1_1791261972903.jpg",
        "name": "maquina_motor_desmontado_v1",
        "size": 768,
        "prompt": "Motor gerador em ruinas e desmontado com carcaca rachada, engrenagens quebradas, toco de tubo rompido vazando lodo verde e tampa de acesso no chao."
    }
]

for m in machines_to_process:
    p = os.path.join(brain_dir, m["file"])
    if os.path.exists(p):
        print(f"Processando {m['name']}...")
        raw = Image.open(p).convert('RGB')
        cleaned = chroma_key_magenta(raw)
        
        # Scale normalize
        target_w = m["size"]
        target_h = int(target_w * cleaned.height / cleaned.width)
        final_img = cleaned.resize((target_w, target_h), Image.Resampling.LANCZOS)
        shadow_img = make_contact_shadow(final_img)
        
        for d in dest_dirs:
            final_img.save(os.path.join(d, f"{m['name']}.png"))
            shadow_img.save(os.path.join(d, f"{m['name']}_sombra.png"))
            with open(os.path.join(d, f"{m['name']}_prompt.txt"), 'w', encoding='utf-8') as f:
                f.write(f"PROMPT NANO BANANA:\n{m['prompt']}\nEstado: Aprovado e recortado com canal alfa transparente e sombra de contato.")
        print(f"Salvo: {m['name']}.png ({final_img.size})")

# Process Modular Pipes
pipes_file = os.path.join(brain_dir, "kit_tubulacao_modular_v1_1791262140518.jpg")
if os.path.exists(pipes_file):
    print("Processando kit_tubulacao_modular_v1...")
    raw = Image.open(pipes_file).convert('RGB')
    cleaned = chroma_key_magenta(raw)
    for d in dest_dirs:
        cleaned.save(os.path.join(d, "kit_tubulacao_modular_v1.png"))
        with open(os.path.join(d, "kit_tubulacao_modular_v1_prompt.txt"), 'w', encoding='utf-8') as f:
            f.write("Kit de tubulacao modular: retos, cotovelo 90, juncao T, valvula de registro e suporte de piso com flanges parafusadas.")

# Process Puddles
puddles_file = os.path.join(brain_dir, "sprites_pocas_esgoto_v1_1791262309820.jpg")
if os.path.exists(puddles_file):
    print("Processando sprites_pocas_esgoto_v1...")
    raw = Image.open(puddles_file).convert('RGB')
    cleaned = chroma_key_magenta(raw)
    for d in dest_dirs:
        cleaned.save(os.path.join(d, "sprites_pocas_esgoto_v1.png"))
        with open(os.path.join(d, "sprites_pocas_esgoto_v1_prompt.txt"), 'w', encoding='utf-8') as f:
            f.write("Conjunto de pocas de esgoto: oleo escuro com brilho ambar, toxica verde com limo, esgoto cinza com detritos e vazamento ferrugem.")

print("Todos os assets processados com sucesso!")
