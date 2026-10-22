from PIL import Image
import numpy as np

def export_godot_layers():
    # Carregar imagem final refinada
    im_final = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\captura_arena_arredondada_obra_prima.png').convert("RGBA")
    w, h = im_final.size
    arr = np.array(im_final)
    
    y_indices, x_indices = np.indices((h, w))
    cx = 688
    cy = 300
    rx = 525
    ry = 155
    dist_elipse = ((x_indices - cx) / rx) ** 2 + ((y_indices - cy) / ry) ** 2
    
    # 1. PISO ROBUSTO ELIPTICO
    # A regiao do piso esta dentro da elipse (dist_elipse <= 0.96)
    # e dentro do portao (x de 490 a 890, y de 445 a 730)
    mask_piso = (dist_elipse <= 0.96) & (arr[:, :, 3] > 0)
    arr_piso = np.zeros_like(arr)
    arr_piso[mask_piso] = arr[mask_piso]
    
    # 2. MURALHA NORTE (Fundo): tudo fora do piso no hemisferio norte
    mask_norte = (y_indices < 340) & (~mask_piso) & (arr[:, :, 3] > 0)
    arr_norte = np.zeros_like(arr)
    arr_norte[mask_norte] = arr[mask_norte]
    
    # 3. MURALHA SUL (Frente): mureta de pedra frontal + portao
    mask_sul = (arr[:, :, 3] > 0) & (~mask_piso) & (~mask_norte)
    arr_sul = np.zeros_like(arr)
    arr_sul[mask_sul] = arr[mask_sul]
    
    # Criar imagens
    im_norte = Image.fromarray(arr_norte)
    im_piso = Image.fromarray(arr_piso)
    im_sul = Image.fromarray(arr_sul)
    
    # Salvar sombras de contato suaves
    # Sombra da muralha norte sobre o topo do piso
    arr_sombra = np.zeros_like(arr)
    mask_sombra = (dist_elipse <= 0.96) & (y_indices < 300) & (arr[:, :, 3] > 0)
    arr_sombra[mask_sombra, 3] = 90 # 35% opacidade preta
    im_sombra = Image.fromarray(arr_sombra)
    
    # Diretorios de destino
    dest_dirs = [
        r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props',
        r'c:\Users\Usuario\Documents\jogo\assets\props',
        r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b'
    ]
    
    files = {
        'arena_coliseu_arredondado_muralha_norte_v2.png': im_norte,
        'arena_coliseu_arredondado_piso_v2.png': im_piso,
        'arena_coliseu_arredondado_muralha_sul_v2.png': im_sul,
        'arena_coliseu_arredondado_sombra_v2.png': im_sombra,
        'arena_coliseu_arredondado_completo_v2.png': im_final
    }
    
    for d in dest_dirs:
        for fname, img_obj in files.items():
            path = f"{d}\\{fname}"
            img_obj.save(path)
            
    print("Todas as camadas foram exportadas com sucesso!")

export_godot_layers()
