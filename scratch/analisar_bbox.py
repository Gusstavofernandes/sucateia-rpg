from PIL import Image
import numpy as np

def analyze_rails(image_path, name):
    im = Image.open(image_path).convert("RGBA")
    arr = np.array(im)
    alpha = arr[:, :, 3]
    h, w = alpha.shape
    
    # Non-empty rows
    row_sums = np.sum(alpha > 20, axis=1)
    non_empty_rows = np.where(row_sums > 0)[0]
    if len(non_empty_rows) == 0:
        print(f"{name}: completely empty")
        return
    min_y, max_y = non_empty_rows[0], non_empty_rows[-1]
    
    col_sums = np.sum(alpha > 20, axis=0)
    non_empty_cols = np.where(col_sums > 0)[0]
    min_x, max_x = non_empty_cols[0], non_empty_cols[-1]
    
    print(f"=== {name} ===")
    print(f"Image Size: W={w}, H={h}")
    print(f"Bounding Box: X=[{min_x}, {max_x}] (W={max_x-min_x+1}), Y=[{min_y}, {max_y}] (H={max_y-min_y+1})")

analyze_rails("assets/rails/estacao_trilho_v2.png", "Estacao")
analyze_rails("assets/rails/trilho_reto_vertical_v1.png", "Trilho Vertical")
analyze_rails("assets/rails/cavalete_alto_v1.png", "Cavalete Alto")
analyze_rails("assets/rails/boca_tunel_v2.png", "Boca Tunel")
