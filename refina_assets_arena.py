from PIL import Image
import numpy as np

def refine_arena_assets():
    # 1. Carregar imagem base da arena (muralha arredondada)
    im2 = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_muralha_sul_clean.png').convert("RGBA")
    w, h = im2.size
    arr2 = np.array(im2)
    
    # 2. Carregar o chao robusto
    chao_fosso = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props\arena_piso_fosso_completo_robusto_v1.png').convert("RGBA")
    
    cx = 688
    cy = 300
    rx = 525
    ry = 155
    
    y_indices, x_indices = np.indices((h, w))
    dist_elipse = ((x_indices - cx) / rx) ** 2 + ((y_indices - cy) / ry) ** 2
    
    # 3. Tratar a regiao interna do portao (x de 460 a 916, y de 380 a 745)
    # Queremos identificar onde e terra entre as barras do portao e remover!
    # A terra tem tom marrom claro/bege:
    r = arr2[:, :, 0].astype(float)
    g = arr2[:, :, 1].astype(float)
    b = arr2[:, :, 2].astype(float)
    
    mask_portao_interior = (x_indices >= 515) & (x_indices <= 865) & (y_indices >= 445) & (y_indices <= 710)
    
    # O ferro do portao e bem escuro e tem rebites:
    # A terra tem R > 85 e G > 75 e B > 60
    # O ferro tem R < 75 ou G < 70 ou B < 65
    is_terra_no_portao = mask_portao_interior & (r > 88) & (g > 78) & (b > 65) & (r - b < 45)
    
    # Remover a terra no portao tornando transparente
    arr2[is_terra_no_portao, 3] = 0
    
    # A regiao superior do portao (laje/fechamento y entre 375 e 445):
    # O topo do portao tem uma viga de ferro horizontal rebitada em y ~ 420-445
    # e uma laje de fechamento em y 375-420.
    
    # 4. Separacao das pecas para Godot:
    # A) MURALHA NORTE (FUNDO): tudo no hemisferio norte (fora da elipse da arena)
    mask_norte = (dist_elipse >= 0.94) & (y_indices < cy + 20) & (arr2[:, :, 3] > 0)
    # Incluir os cantos superiores laterais
    mask_norte |= (y_indices < 330) & (arr2[:, :, 3] > 0)
    
    arr_norte = arr2.copy()
    arr_norte[~mask_norte, 3] = 0
    
    # B) MURETA SUL (FRENTE): mureta de pedra frontal + portao
    mask_sul = (y_indices >= cy - 10) & (dist_elipse >= 0.92) & (arr2[:, :, 3] > 0)
    # Incluir portao inteiro
    mask_sul |= (x_indices >= 460) & (x_indices <= 916) & (y_indices >= 370) & (arr2[:, :, 3] > 0)
    # Remover o que for do norte
    mask_sul &= ~mask_norte
    
    arr_sul = arr2.copy()
    arr_sul[~mask_sul, 3] = 0
    
    # C) PISO FOSSO ELIPTICO:
    # Redimensionar o chao robusto para preencher a elipse interna com perfeicao
    chao_w = int(rx * 2 * 1.05)
    chao_h = int(ry * 2 * 1.05)
    chao_resized = chao_fosso.resize((chao_w, chao_h), Image.Resampling.LANCZOS)
    chao_arr = np.array(chao_resized)
    
    arr_piso = np.zeros((h, w, 4), dtype=np.uint8)
    x0 = cx - chao_w // 2
    y0 = cy - chao_h // 2
    for y in range(chao_h):
        for x in range(chao_w):
            out_y = y0 + y
            out_x = x0 + x
            if 0 <= out_y < h and 0 <= out_x < w:
                # O chao se estende ate onde comeca a face interna da mureta sul
                if dist_elipse[out_y, out_x] <= 0.97:
                    arr_piso[out_y, out_x] = chao_arr[y, x]
                # E se estende um pouco sob o portao para que o chao apareca atras das grades!
                elif 515 <= out_x <= 865 and 445 <= out_y <= 720:
                    arr_piso[out_y, out_x] = chao_arr[y, x]

    # Salvar as 3 imagens geradas
    im_norte = Image.fromarray(arr_norte)
    im_sul = Image.fromarray(arr_sul)
    im_piso = Image.fromarray(arr_piso)
    
    dest_dirs = [
        r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props',
        r'c:\Users\Usuario\Documents\jogo\assets\props',
        r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b'
    ]
    
    filenames = {
        'arena_coliseu_muralha_norte_arredondada_v1.png': im_norte,
        'arena_coliseu_muralha_sul_arredondada_v1.png': im_sul,
        'arena_coliseu_piso_arredondado_v1.png': im_piso
    }
    
    for d in dest_dirs:
        for fname, img in filenames.items():
            out_path = f"{d}\\{fname}"
            img.save(out_path)
            
    # Gerar composicao final para inspecao
    comp = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    comp.paste(im_norte, (0, 0), im_norte)
    comp.paste(im_piso, (0, 0), im_piso)
    comp.paste(im_sul, (0, 0), im_sul)
    
    comp_path = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\captura_arena_arredondada_refinada.png'
    comp.save(comp_path)
    print("Assets salvos e composicao gerada com sucesso!")

refine_arena_assets()
