import os
from PIL import Image, ImageFilter
import numpy as np
from scipy.ndimage import binary_fill_holes, binary_dilation

def clean_cutout(input_path, output_path, shadow_path=None, fade_edges=False):
    img = Image.open(input_path).convert("RGB")
    arr = np.array(img, dtype=np.float32)
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    
    # 1. Detecção rigorosa de magenta/roxo de fundo
    # Magenta puro ou variantes geradas por IA: R e B são ambos altos, G é baixo
    # Em rochas (mesmo escuras ou claras), G é maior ou muito próximo de B (arenito é quente/ocre: R > G >= B)
    # Portanto, em magenta: (b - g) é significativamente positivo!
    is_magenta = (b - g > 18.0) & (r - g > 25.0) & (g < 140.0)
    
    # 2. Calcular alfa suave
    # Fora do magenta, alfa = 1.0; no magenta, alfa = 0.0
    # Na borda (antialiasing):
    rb_excess = np.minimum(b - g, r - g)
    # Se rb_excess <= 8, é objeto sólido (alpha=1)
    # Se rb_excess >= 22, é magenta puro (alpha=0)
    alpha = np.clip(1.0 - (rb_excess - 8.0) / 14.0, 0.0, 1.0)
    alpha[is_magenta] = 0.0
    
    # 3. Remover pequenos ruídos isolados de magenta dentro de fendas ou na borda
    # Descontaminação de cor: onde o pixel é semitransparente, neutralizar excesso de magenta
    semi = (alpha > 0.0) & (alpha < 0.98) & (b > g)
    if np.any(semi):
        # Reduzir B para que fique próximo de G nos pixels de borda
        arr[:,:,2][semi] = np.clip(g[semi] * 0.95, 0, 255)
        # Reduzir excesso de R arroxeado
        arr[:,:,0][semi] = np.clip((arr[:,:,0][semi] + g[semi]) * 0.5, 0, 255)
        
    # 4. Se o objeto tocar as bordas retangulares (como topo ou lados retos), aplicar fade suave
    h, w = arr.shape[:2]
    if fade_edges:
        # Fade nas margens de 30px se encostar na borda
        y_coords, x_coords = np.mgrid[0:h, 0:w]
        edge_dist_x = np.minimum(x_coords, w - 1 - x_coords)
        edge_dist_y = np.minimum(y_coords, h - 1 - y_coords)
        edge_dist = np.minimum(edge_dist_x, edge_dist_y)
        edge_fade = np.clip(edge_dist / 25.0, 0.0, 1.0)
        alpha = alpha * edge_fade
        
    # Zera bordas extremas de 2px para garantir zero sangramento
    alpha[:2, :] = 0.0
    alpha[-2:, :] = 0.0
    alpha[:, :2] = 0.0
    alpha[:, -2:] = 0.0
    
    # 5. Criar imagem RGBA final
    out_arr = np.dstack([np.clip(arr, 0, 255).astype(np.uint8), (alpha * 255.0).astype(np.uint8)])
    clean_img = Image.fromarray(out_arr, "RGBA")
    
    # Bounding box crop
    bbox = clean_img.getbbox()
    if bbox:
        pad = 2
        box = (max(0, bbox[0] - pad), max(0, bbox[1] - pad), min(w, bbox[2] + pad), min(h, bbox[3] + pad))
        clean_img = clean_img.crop(box)
    
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    clean_img.save(output_path, "PNG")
    print(f"Salvo: {output_path} | Dimensões: {clean_img.size}")
    
    # 6. Sombra suave (apenas se solicitada)
    if shadow_path:
        # A sombra deve ser uma silhueta elíptica ou achatada na base do objeto, NUNCA uma placa quadrada!
        sw, sh = clean_img.size
        sh_arr = np.array(clean_img, dtype=np.float32)
        sh_alpha = sh_arr[:, :, 3] / 255.0
        
        # Manter sombra apenas na metade inferior do objeto (onde o objeto encosta no chão)
        y_weight = np.linspace(0.0, 1.0, sh)[:, None]
        # Apenas na base inferior (y_weight > 0.4)
        base_weight = np.clip((y_weight - 0.40) / 0.50, 0.0, 1.0)
        
        final_sh_alpha = sh_alpha * base_weight * 95.0 # ~37% opacidade
        
        shadow_out = np.zeros((sh, sw, 4), dtype=np.uint8)
        shadow_out[:, :, 0] = 0
        shadow_out[:, :, 1] = 0
        shadow_out[:, :, 2] = 0
        shadow_out[:, :, 3] = final_sh_alpha.astype(np.uint8)
        
        sh_img = Image.fromarray(shadow_out, "RGBA")
        sh_img = sh_img.filter(ImageFilter.GaussianBlur(radius=6))
        
        os.makedirs(os.path.dirname(os.path.abspath(shadow_path)), exist_ok=True)
        sh_img.save(shadow_path, "PNG")
        print(f"Sombra salva: {shadow_path}")
        
    return True

if __name__ == "__main__":
    brain = "C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b/"
    
    # 1. Falésia marítima amarelada
    clean_cutout(brain + "falesia_maritima_amarelada_1792604845461.jpg", 
                 "assets/reconstruction/falesia_maritima_amarelada.png", 
                 "assets/reconstruction/falesia_maritima_amarelada_sombra.png", fade_edges=True)
                 
    # 2. Rochas marítimas recife costeiro
    clean_cutout(brain + "rochas_maritimas_recife_costeiro_1792604880281.jpg", 
                 "assets/reconstruction/rochas_maritimas_recife_costeiro.png", 
                 "assets/reconstruction/rochas_maritimas_recife_costeiro_sombra.png", fade_edges=True)
                 
    # 3. Areia praia litorânea
    clean_cutout(brain + "areia_praia_litoranea_1792608177823.jpg", 
                 "assets/reconstruction/areia_praia_litoranea.png", fade_edges=False)
                 
    # 4. Rochedos praia marítima
    clean_cutout(brain + "rochedos_praia_maritima_1792608291294.jpg", 
                 "assets/reconstruction/rochedos_praia_maritima.png", 
                 "assets/reconstruction/rochedos_praia_maritima_sombra.png", fade_edges=False)
                 
    # 5. Falésia promontório costeiro
    clean_cutout(brain + "falesia_promontorio_costeiro_1792608168238.jpg", 
                 "assets/reconstruction/falesia_promontorio_costeiro.png", 
                 "assets/reconstruction/falesia_promontorio_costeiro_sombra.png", fade_edges=True)
