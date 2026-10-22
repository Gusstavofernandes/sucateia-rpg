from PIL import Image
import numpy as np

def clean_and_separate():
    raw_path = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_mureta_sul_baixa_raw_1792527098381.jpg'
    im = Image.open(raw_path).convert("RGBA")
    arr = np.array(im, dtype=np.float32)
    
    r = arr[:, :, 0]
    g = arr[:, :, 1]
    b = arr[:, :, 2]
    
    # Deteccao precisa de magenta
    diff_rg = r - g
    diff_bg = b - g
    magenta_intensity = np.minimum(diff_rg, diff_bg)
    
    # Mascara de transparencia
    threshold = 55.0
    alpha = np.clip(1.0 - (magenta_intensity - 25.0) / (threshold - 25.0 + 1e-5), 0.0, 1.0)
    
    # Despill (neutralizacao de qualquer halo magenta nas bordas)
    despill_mask = magenta_intensity > 8.0
    arr[:, :, 0] = np.where(despill_mask, np.minimum(r, np.maximum(g * 1.1, b * 0.5)), r)
    arr[:, :, 2] = np.where(despill_mask, np.minimum(b, np.maximum(g * 1.1, r * 0.5)), b)
    
    arr[:, :, 3] = arr[:, :, 3] * alpha
    
    clean_im = Image.fromarray(np.uint8(np.clip(arr, 0, 255)), mode="RGBA")
    clean_arr = np.array(clean_im)
    
    # Salvar versao completa limpa
    clean_im.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_muralha_coliseu_completa_v1.png')
    
    # Agora vamos separar em Norte (fundo) e Sul (frente)
    h, w, _ = clean_arr.shape
    y_indices, x_indices = np.indices((h, w))
    
    # O corte entre norte e sul:
    # A mureta frontal comeca na esquerda e direita onde o arco frontal se apoia nas paredes laterais (y ~ 570)
    # E o portao central sobe ate y ~ 510
    # Vamos analisar a mureta frontal:
    # A mureta frontal comeca em y >= 510 na regiao do portao e y >= 570 nas laterais
    # Vamos criar a mascara da mureta sul:
    # Portao central: x de 550 a 820, y de 500 a 750
    # Mureta esquerda: x de 200 a 580, y de 560 a 730
    # Mureta direita: x de 790 a 1180, y de 560 a 730
    # Arco do portao sobe ate y = 510
    
    mask_sul = np.zeros((h, w), dtype=bool)
    for y in range(h):
        for x in range(w):
            if clean_arr[y, x, 3] > 0:
                # Regiao do portao
                if 555 <= x <= 820 and y >= 508:
                    mask_sul[y, x] = True
                # Regiao das muretas laterais frontais
                elif 235 <= x < 555 and y >= 565:
                    mask_sul[y, x] = True
                elif 820 < x <= 1140 and y >= 565:
                    mask_sul[y, x] = True
                # Pilares das pontas frontais
                elif (x < 235 or x > 1140) and y >= 640:
                    mask_sul[y, x] = True

    # 1. PECA NORTE: tudo que NAO e mask_sul
    arr_norte = clean_arr.copy()
    arr_norte[mask_sul, 3] = 0
    im_norte = Image.fromarray(arr_norte)
    im_norte.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_muralha_coliseu_norte_v1.png')
    
    # 2. PECA SUL: apenas mask_sul
    arr_sul = clean_arr.copy()
    arr_sul[~mask_sul, 3] = 0
    im_sul = Image.fromarray(arr_sul)
    im_sul.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_muralha_coliseu_sul_v1.png')
    
    print("Muralha Norte salva:", im_norte.size)
    print("Muralha Sul salva:", im_sul.size)
    
    # Testar composicao com o chao de sangue/ferro
    chao_fosso = Image.open(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\props\arena_piso_fosso_completo_robusto_v1.png').convert("RGBA")
    
    # A regiao do fosso aberta no meio da imagem e de aproximadamente x: 260 a 1120 (largura 860) e y: 260 a 600 (altura 340)
    # Vamos redimensionar o chao com preservacao dos detalhes
    chao_scaled = chao_fosso.resize((880, 360), Image.Resampling.LANCZOS)
    
    comp = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    # 1. Norte
    comp.paste(im_norte, (0, 0), im_norte)
    # 2. Chao dentro do fosso
    chao_x = (w - 880) // 2
    chao_y = 260
    comp.paste(chao_scaled, (chao_x, chao_y), chao_scaled)
    # Mas como o chao e retangular, vamos garantir que ele fique SOB a parede norte nas bordas:
    comp_final = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    comp_final.paste(chao_scaled, (chao_x, chao_y), chao_scaled)
    # Agora cola o norte por cima das bordas da base do chao se necessario, ou chao sobre o norte:
    # A base interna da parede norte e onde o chao encosta.
    # Vamos colar Norte -> Chao -> Sul
    comp_correta = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    comp_correta.paste(chao_scaled, (chao_x, chao_y), chao_scaled)
    comp_correta.paste(im_norte, (0, 0), im_norte)
    comp_correta.paste(im_sul, (0, 0), im_sul)
    
    comp_correta.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_arena_montagem_final.png')
    print("Montagem final salva com sucesso!")

clean_and_separate()
