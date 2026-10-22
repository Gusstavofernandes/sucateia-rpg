from PIL import Image
import numpy as np

def find_rails_in_image(img_path, y_list):
    im = Image.open(img_path).convert("RGBA")
    arr = np.array(im)
    print(f"\n==========================================")
    print(f"ANÁLISE DE TRILHOS: {img_path}")
    print(f"==========================================")
    for y in y_list:
        row_rgb = arr[y, :, :3]
        row_alpha = arr[y, :, 3]
        
        # Trilho de ferro geralmente tem brilho metálico ou contraste escuro/claro,
        # enquanto os dormentes são madeira escura/marrom.
        # Vamos inspecionar a fatia de alfa e as intensidades:
        active_x = np.where(row_alpha > 50)[0]
        if len(active_x) == 0:
            continue
        
        # Vamos imprimir a variação horizontal de luminância / canais
        lum = 0.299 * row_rgb[:, 0] + 0.587 * row_rgb[:, 1] + 0.114 * row_rgb[:, 2]
        
        # Encontrar picos ou transições
        print(f"--- Y = {y} --- (Faixa ativa: X={active_x[0]}..{active_x[-1]})")
        # Mostrar onde há presença de trilho
        # Vamos inspecionar blocos de 20 px
        for x_start in range(active_x[0], active_x[-1], 25):
            x_end = min(x_start + 25, active_x[-1] + 1)
            mean_lum = np.mean(lum[x_start:x_end])
            mean_a = np.mean(row_alpha[x_start:x_end])
            # print if meaningful
            if mean_a > 100:
                print(f"   X [{x_start:3d}-{x_end:3d}]: Lum={mean_lum:5.1f}, R={np.mean(row_rgb[x_start:x_end,0]):5.1f}, G={np.mean(row_rgb[x_start:x_end,1]):5.1f}, B={np.mean(row_rgb[x_start:x_end,2]):5.1f}")

find_rails_in_image("assets/rails/estacao_trilho_v2.png", [10, 400, 800])
find_rails_in_image("assets/rails/trilho_reto_vertical_v1.png", [10, 100, 500, 970])
