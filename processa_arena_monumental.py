from PIL import Image
import numpy as np

def process_monumental_arena():
    raw_path = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_mureta_sul_baixa_raw_1792527098381.jpg'
    im = Image.open(raw_path).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Chroma key
    diff_rg = r - g
    diff_bg = b - g
    magenta_intensity = np.minimum(diff_rg, diff_bg)
    
    threshold = 55.0
    alpha = np.clip(1.0 - (magenta_intensity - 25.0) / (threshold - 25.0 + 1e-5), 0.0, 1.0)
    
    # Despill
    despill_mask = magenta_intensity > 8.0
    arr[:, :, 0] = np.where(despill_mask, np.minimum(r, np.maximum(g * 1.1, b * 0.5)), r)
    arr[:, :, 2] = np.where(despill_mask, np.minimum(b, np.maximum(g * 1.1, r * 0.5)), b)
    
    arr[:, :, 3] = arr[:, :, 3] * alpha
    
    clean_arr = np.uint8(np.clip(arr, 0, 255))
    h, w, _ = clean_arr.shape
    y_indices, x_indices = np.indices((h, w))
    
    # Vamos analisar a mureta frontal (Sul):
    # O portao esta entre x: 550 e 825, e vai de y=510 a 768.
    # As muretas de pedra laterais comecam em y=565 e vao de x=240 a 560 e x=815 a 1135.
    # Os pilares laterais nas pontas descem ate y=730.
    
    mask_sul = np.zeros((h, w), dtype=bool)
    # 1. Portao em arco
    mask_sul[(x_indices >= 555) & (x_indices <= 820) & (y_indices >= 510) & (clean_arr[:, :, 3] > 0)] = True
    # 2. Mureta lateral esquerda
    mask_sul[(x_indices >= 240) & (x_indices < 555) & (y_indices >= 565) & (clean_arr[:, :, 3] > 0)] = True
    # 3. Mureta lateral direita
    mask_sul[(x_indices > 820) & (x_indices <= 1135) & (y_indices >= 565) & (clean_arr[:, :, 3] > 0)] = True
    
    # Peca Sul isolada
    arr_sul = clean_arr.copy()
    arr_sul[~mask_sul, 3] = 0
    # Cortar o bounding box da peca sul para economizar espaco e facilitar posicionamento
    # Bounding box sul: y de 510 a 768, x de 240 a 1135
    sul_crop = Image.fromarray(arr_sul).crop((230, 505, 1145, 768))
    
    # Peca Norte isolada (tudo exceto a mureta sul)
    arr_norte = clean_arr.copy()
    arr_norte[mask_sul, 3] = 0
    # Bounding box norte: y de 30 a 735, x de 35 a 1340
    norte_crop = Image.fromarray(arr_norte).crop((35, 30, 1340, 735))
    
    # Salvar nos diretorios do projeto
    dest_dirs = [
        r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props',
        r'c:\Users\Usuario\Documents\jogo\assets\props',
        r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b'
    ]
    
    for d in dest_dirs:
        norte_crop.save(f"{d}\\arena_muralha_norte_monumental_v1.png")
        sul_crop.save(f"{d}\\arena_mureta_sul_portao_aberto_v1.png")
        
    print("Norte crop size:", norte_crop.size)
    print("Sul crop size:", sul_crop.size)
    
    # Agora vamos testar a montagem no canvas expandido onde a mureta sul fica mais abaixo,
    # revelando o chão de combate de forma ampla e imponente!
    chao_fosso = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props\arena_piso_fosso_completo_robusto_v1.png').convert("RGBA")
    
    canvas_w = 1400
    canvas_h = 1000
    comp = Image.new("RGBA", (canvas_w, canvas_h), (0, 0, 0, 0))
    
    # 1. Chao robusto no centro (escala 0.75x = ~1250 x ~670)
    chao_scaled = chao_fosso.resize((1200, 640), Image.Resampling.LANCZOS)
    comp.paste(chao_scaled, ((canvas_w - 1200) // 2, 280), chao_scaled)
    
    # 2. Muralha Norte no topo (y = 20)
    comp.paste(norte_crop, ((canvas_w - norte_crop.width) // 2, 20), norte_crop)
    
    # 3. Mureta Sul na frente mais abaixo (y = 680)
    comp.paste(sul_crop, ((canvas_w - sul_crop.width) // 2, 680), sul_crop)
    
    comp.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_arena_expandida_ampla.png')
    print("Composicao expandida ampla salva!")

process_monumental_arena()
