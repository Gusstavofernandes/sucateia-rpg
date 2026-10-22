from PIL import Image
import numpy as np

def process_grand_colosseum():
    raw_path = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_coliseu_imponente_meia_lua_raw_1792537581293.jpg'
    im = Image.open(raw_path).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Chroma key magenta preciso
    diff_rg = r - g
    diff_bg = b - g
    magenta_intensity = np.minimum(diff_rg, diff_bg)
    
    threshold = 55.0
    alpha = np.clip(1.0 - (magenta_intensity - 25.0) / (threshold - 25.0 + 1e-5), 0.0, 1.0)
    
    # Despill: neutraliza qualquer halo magenta nas bordas
    despill_mask = magenta_intensity > 8.0
    arr[:, :, 0] = np.where(despill_mask, np.minimum(r, np.maximum(g * 1.1, b * 0.5)), r)
    arr[:, :, 2] = np.where(despill_mask, np.minimum(b, np.maximum(g * 1.1, r * 0.5)), b)
    
    arr[:, :, 3] = arr[:, :, 3] * alpha
    clean_arr = np.uint8(np.clip(arr, 0, 255))
    h, w, _ = clean_arr.shape
    
    im_clean = Image.fromarray(clean_arr, mode="RGBA")
    
    # Vamos analisar a geometria interna da arena:
    # Centro da elipse do fosso rebaixado:
    # O fosso fica na parte inferior, sob a arquibancada em meia-lua.
    # Vamos localizar a elipse do chão do fosso:
    # A base da parede interna sob a arquibancada comeca em y ~ 420-440 no centro.
    # O fosso tem largura de x ~ 330 a 1050 (largura ~ 720 px)
    # e altura de y ~ 430 a 690 (altura ~ 260 px)
    cx = 688
    cy = 555
    rx = 365
    ry = 125
    
    y_indices, x_indices = np.indices((h, w))
    dist_elipse_fosso = ((x_indices - cx) / rx) ** 2 + ((y_indices - cy) / ry) ** 2
    
    # 1. PISO DO FOSSO REBAIXADO
    # O chão de combate rebaixado com marcas de sangue e drenos
    mask_piso = (dist_elipse_fosso <= 0.98) & (y_indices >= 430) & (y_indices <= 685) & (clean_arr[:, :, 3] > 0)
    
    # 2. MURETA FRONTAL SUL (Frente):
    # A mureta frontal com as ameias de ferro rebitadas e o grande portão frontal
    # Comeca nas laterais em y >= 340 (nos pilares mais externos) e na frente y >= 560
    # O portão central fica entre x: 535 e 845, y >= 540
    mask_sul = np.zeros((h, w), dtype=bool)
    # Portão frontal
    mask_sul[(x_indices >= 530) & (x_indices <= 845) & (y_indices >= 540) & (clean_arr[:, :, 3] > 0)] = True
    # Mureta frontal esquerda e direita
    mask_sul[(dist_elipse_fosso >= 0.94) & (y_indices >= 500) & (clean_arr[:, :, 3] > 0)] = True
    # Pilares externos das pontas que avançam para a frente
    mask_sul[(x_indices <= 330) & (y_indices >= 340) & (clean_arr[:, :, 3] > 0)] = True
    mask_sul[(x_indices >= 1045) & (y_indices >= 340) & (clean_arr[:, :, 3] > 0)] = True
    # Garantir que o chão do fosso nao seja pego na mureta sul
    mask_sul &= ~mask_piso
    
    # 3. CAMADA NORTE (FUNDO):
    # Grande Arquibancada em Meia-Lua + Parede de contenção interna do fosso com celas e tochas
    mask_norte = (clean_arr[:, :, 3] > 0) & (~mask_sul) & (~mask_piso)
    
    # Criar arrays das camadas
    arr_norte = np.zeros_like(clean_arr)
    arr_norte[mask_norte] = clean_arr[mask_norte]
    
    arr_piso = np.zeros_like(clean_arr)
    arr_piso[mask_piso] = clean_arr[mask_piso]
    
    arr_sul = np.zeros_like(clean_arr)
    arr_sul[mask_sul] = clean_arr[mask_sul]
    
    # Sombra profunda de oclusão do fosso (para reforçar que o chão está bem fundo!)
    # Sombra vertical descendo da parede norte da arquibancada sobre o chão
    arr_sombra = np.zeros_like(clean_arr)
    mask_sombra_profunda = mask_piso & (y_indices < cy - 10)
    arr_sombra[mask_sombra_profunda, 3] = 110 # 43% de sombra preta
    
    im_norte = Image.fromarray(arr_norte)
    im_piso = Image.fromarray(arr_piso)
    im_sul = Image.fromarray(arr_sul)
    im_sombra = Image.fromarray(arr_sombra)
    
    # Salvar em todos os diretórios do projeto
    dest_dirs = [
        r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props',
        r'c:\Users\Usuario\Documents\jogo\assets\props',
        r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b'
    ]
    
    files = {
        'arena_coliseu_imponente_completo_v3.png': im_clean,
        'arena_coliseu_imponente_norte_v3.png': im_norte,
        'arena_coliseu_imponente_piso_v3.png': im_piso,
        'arena_coliseu_imponente_sul_v3.png': im_sul,
        'arena_coliseu_imponente_sombra_v3.png': im_sombra
    }
    
    for d in dest_dirs:
        for fname, img_obj in files.items():
            path = f"{d}\\{fname}"
            img_obj.save(path)
            
    print("Camadas do Coliseu Imponente v3 exportadas com sucesso!")

process_grand_colosseum()
