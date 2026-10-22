from PIL import Image
import numpy as np

def track_rails(img_path, name):
    im = Image.open(img_path).convert("RGBA")
    arr = np.array(im)
    h, w, _ = arr.shape
    
    print(f"\n==========================================")
    print(f"RASTREAMENTO DE TRILHOS: {name} ({img_path})")
    print(f"Canvas: W={w}, H={h}")
    print(f"==========================================")
    
    # Vamos rastrear a cada 100 pixels de Y
    results = []
    for y in range(20, h, 80):
        row_rgb = arr[y, :, :3]
        row_a = arr[y, :, 3]
        lum = 0.299 * row_rgb[:, 0] + 0.587 * row_rgb[:, 1] + 0.114 * row_rgb[:, 2]
        
        # Filtrar apenas onde alfa > 150
        valid = np.where(row_a > 150)[0]
        if len(valid) < 50:
            continue
            
        # O trilho tem contraste alto de aço (lum > 80 ou picos de reflexo)
        # Vamos achar os dois picos de brilho principais ou a sapata externa
        # Dividir a faixa em metade esquerda e metade direita
        mid = (valid[0] + valid[-1]) // 2
        left_valid = valid[valid < mid]
        right_valid = valid[valid >= mid]
        
        if len(left_valid) == 0 or len(right_valid) == 0:
            continue
            
        # Picos de aço
        left_peaks = left_valid[lum[left_valid] > 70]
        right_peaks = right_valid[lum[right_valid] > 70]
        
        if len(left_peaks) > 0 and len(right_peaks) > 0:
            # borda externa esquerda = menor X com cor de metal
            # borda externa direita = maior X com cor de metal
            x_esq_ext = left_peaks[0]
            x_esq_int = left_peaks[-1]
            x_dir_int = right_peaks[0]
            x_dir_ext = right_peaks[-1]
            gauge_ext = x_dir_ext - x_esq_ext
            center_x = (x_esq_ext + x_dir_ext) / 2.0
            results.append((y, x_esq_ext, x_esq_int, x_dir_int, x_dir_ext, gauge_ext, center_x))
            print(f"Y={y:3d} | Trilho Esq: [{x_esq_ext:3d}..{x_esq_int:3d}] | Trilho Dir: [{x_dir_int:3d}..{x_dir_ext:3d}] | Bitola Ext={gauge_ext:3d} px | Centro X={center_x:5.1f}")

    return results

res_estacao = track_rails("assets/rails/estacao_trilho_v2.png", "Estacao de Carga")
res_ponte = track_rails("assets/rails/trilho_reto_vertical_v1.png", "Trilho da Ponte")
