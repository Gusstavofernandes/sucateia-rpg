import os, zipfile, io
import numpy as np
from PIL import Image, ImageFilter

def load_frame(idx):
    zip_idx = (idx - 1) // 30 + 1
    zip_name = rf'c:\Users\Usuario\Documents\jogo\frames_{(zip_idx-1)*30+1:03d}-{zip_idx*30:03d}.zip'
    frame_name = f'frame_{idx:04d}.png'
    with zipfile.ZipFile(zip_name) as z:
        return Image.open(io.BytesIO(z.read(frame_name)))

output_dir = rf'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets'

# Impact pool size: 384 x 192 (an ellipse of splashing foam and ripples in the canal)
w, h = 384, 192
y_grid, x_grid = np.mgrid[0:h, 0:w]
cx, cy = w / 2.0, h / 2.0

# Normalized ellipse coordinates:
dx = (x_grid - cx) / (w * 0.46)
dy = (y_grid - cy) / (h * 0.42)
r = np.sqrt(dx**2 + dy**2)

# Load water frame with bright foam and bubbles
f_foam = load_frame(95).crop((200, 150, 1080, 600)).resize((w, h), Image.Resampling.LANCZOS)
f_arr = np.array(f_foam).astype(np.float32)

# Multiple concentric ripple rings:
ripples = np.cos(r * np.pi * 5.0) * 0.5 + 0.5
# Ring wave envelope (stronger in middle, fading to 0 at edge):
envelope = np.clip(1.0 - r, 0.0, 1.0)
ring_alpha = envelope * (0.4 + 0.6 * ripples)

# Edge falloff
alpha = np.clip((1.0 - r) * 2.5, 0.0, 1.0) * ring_alpha

# Foam coloration:
lum = np.dot(f_arr[..., :3], [0.299, 0.587, 0.114])
is_foam = np.clip((lum - 50.0) / 50.0, 0.0, 1.0)

foam_tint = np.array([110.0, 160.0, 120.0]) # bright bubbling sewer froth
final_rgb = f_arr * 0.7 + foam_tint * (is_foam * 0.6 + ripples * 0.4)[..., None]

rgba = np.dstack([
    np.clip(final_rgb, 0, 255).astype(np.uint8),
    (np.clip(alpha, 0.0, 1.0) * 255.0).astype(np.uint8)
])

img = Image.fromarray(rgba)
# Soften outer edge slightly
alpha_blur = Image.fromarray(rgba[..., 3]).filter(ImageFilter.GaussianBlur(radius=1.5))
img.putalpha(alpha_blur)

target_path = os.path.join(output_dir, 'bueiro_impact_foam.png')
img.save(target_path)
print("Saved impact foam:", target_path)
