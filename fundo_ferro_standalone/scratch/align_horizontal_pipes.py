import os
from PIL import Image, ImageFilter
import numpy as np

def create_aligned_modules():
    src_dir = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes"
    target_dirs = [
        src_dir,
        r"c:\Users\Usuario\Documents\jogo\assets\pipes"
    ]

    # 1. Cano Reto Horizontal: rotacionar +21.6 graus para que o cilindro fique perfeitamente horizontal
    im_pipe = Image.open(os.path.join(src_dir, "cano_reto_horizontal.png")).convert("RGBA")
    # Rotacao com expansao e filtro bicubico de alta qualidade
    pipe_rot = im_pipe.rotate(21.57, resample=Image.Resampling.BICUBIC, expand=True)
    pipe_rot = pipe_rot.crop(pipe_rot.getbbox())
    
    # 2. Valvula Horizontal: rotacionar +21.6 graus para alinhar o corpo do tubo na horizontal
    im_valv = Image.open(os.path.join(src_dir, "cano_valvula_registro.png")).convert("RGBA")
    valv_rot = im_valv.rotate(21.57, resample=Image.Resampling.BICUBIC, expand=True)
    valv_rot = valv_rot.crop(valv_rot.getbbox())

    # 3. Gerar sombras suaves para ambos
    def make_shadow(img, h_factor=0.38):
        w, h = img.size
        proj_h = max(10, int(h * h_factor))
        alpha = img.split()[-1].resize((w, proj_h), Image.Resampling.BILINEAR)
        sh_arr = np.array(alpha, dtype=np.float32) * 0.50
        zeros = np.zeros_like(sh_arr, dtype=np.uint8)
        sh_img = Image.fromarray(np.dstack([zeros, zeros, zeros, sh_arr.astype(np.uint8)])).filter(ImageFilter.GaussianBlur(radius=4.0))
        return sh_img

    pipe_rot_sh = make_shadow(pipe_rot)
    valv_rot_sh = make_shadow(valv_rot)

    for td in target_dirs:
        pipe_rot.save(os.path.join(td, "cano_modulo_horizontal.png"))
        pipe_rot_sh.save(os.path.join(td, "cano_modulo_horizontal_sombra.png"))
        valv_rot.save(os.path.join(td, "cano_valvula_horizontal.png"))
        valv_rot_sh.save(os.path.join(td, "cano_valvula_horizontal_sombra.png"))

    print("Cano horizontal e valvula horizontal alinhados com sucesso!")
    print("Dimensoes cano:", pipe_rot.size)
    print("Dimensoes valvula:", valv_rot.size)

if __name__ == "__main__":
    create_aligned_modules()
