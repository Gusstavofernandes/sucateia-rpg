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

# Load frames with high turbulent detail and foam
f1 = load_frame(35)
f2 = load_frame(85)
f3 = load_frame(145)

# We want a vertical cascade of width 512, height 1024.
w, h = 512, 1024
y_grid, x_grid = np.mgrid[0:h, 0:w]
cx = w / 2.0

# 1. Base water texture aligned with vertical flow
# Take a slice from f1, f2, f3 and blend
crop1 = f1.crop((180, 80, 1100, 640)).resize((w, h), Image.Resampling.LANCZOS)
crop2 = f2.crop((180, 80, 1100, 640)).resize((w, h), Image.Resampling.LANCZOS)
arr1 = np.array(crop1).astype(np.float32)
arr2 = np.array(crop2).astype(np.float32)

# Flow lines: apply slight directional stretch along Y to mimic downward rushing current
flow_bg = arr1 * 0.6 + arr2 * 0.4

# 2. Organic chute contour
# Profile: width is ~130px at top (Y=0..150), narrows slightly in the chute (~110px at Y=400),
# then widens at the bottom plunge pool (~260px at Y=900..1024)
y_norm = y_grid / float(h)

# Smooth chute envelope:
top_width = 140.0
mid_width = 110.0
bot_width = 240.0

# Interpolate profile with smooth spline-like transitions
profile = np.zeros_like(y_norm, dtype=np.float32)
mask_top = y_norm < 0.2
mask_mid = (y_norm >= 0.2) & (y_norm < 0.75)
mask_bot = y_norm >= 0.75

profile[mask_top] = top_width + (mid_width - top_width) * ((y_norm[mask_top]) / 0.2)
profile[mask_mid] = mid_width + (mid_width * 0.15) * np.sin((y_norm[mask_mid] - 0.2) * np.pi * 3.0)
t_bot = (y_norm[mask_bot] - 0.75) / 0.25
profile[mask_bot] = mid_width + (bot_width - mid_width) * (t_bot ** 1.6)

# Add organic jaggedness / turbulence noise to stream boundary
np.random.seed(1337)
# Perlin-like low frequency noise along stream length
noise_1d = np.convolve(np.random.randn(h + 40), np.hamming(35), mode='same')[20:h+20] * 12.0
noise_2d = noise_1d[:, None]

# Distance from center with noise
dist_from_axis = np.abs(x_grid - (cx + noise_2d * 0.6))
half_w = profile / 2.0

# 3. Calculate Alpha Mask
# Solid core in center, frothy falloff at edges
edge_dist = (half_w - dist_from_axis) / (half_w * 0.28 + 4.0)
alpha_map = np.clip(edge_dist, 0.0, 1.0)
# Smooth step for crisp yet organic water edges
alpha_map = alpha_map * alpha_map * (3.0 - 2.0 * alpha_map)

# Fade in top entrance (coming from under arch tunnel)
top_alpha_fade = np.clip(y_norm / 0.04, 0.0, 1.0)
# At the bottom (Y=1024), it plunges into the canal, so keep strong alpha with splashing tendrils
bot_alpha = np.clip(1.0 - (y_norm - 0.96) / 0.04, 0.0, 1.0) * 0.3 + 0.7
alpha_final = alpha_map * top_alpha_fade * bot_alpha

# 4. Enhance foam highlights along stream borders and bottom splash
# Edge frothing: where edge_dist is between 0.05 and 0.5
edge_foam = np.clip(np.sin(edge_dist * np.pi), 0.0, 1.0) * 70.0
# Add bottom splash frothing
bottom_splash_foam = np.clip((y_norm - 0.75) / 0.25, 0.0, 1.0) * 85.0 * (1.0 - dist_from_axis / (half_w + 1e-4))

# Boost brightness at foam regions
foam_color = np.array([85.0, 130.0, 95.0]) # greenish yellow sewage foam
color_final = flow_bg + foam_color * ((edge_foam[:, :, None] + bottom_splash_foam[:, :, None]) / 100.0)

# Add extra foam streaks in the core (turbulent rapids)
core_foam_streaks = np.clip(np.sin(x_grid * 0.12 + y_grid * 0.05 + noise_2d * 0.1), 0.0, 1.0) ** 4.0
color_final += (foam_color * 0.6) * (core_foam_streaks[:, :, None] * alpha_map[:, :, None])

color_final = np.clip(color_final, 0, 255).astype(np.uint8)
alpha_uint8 = (np.clip(alpha_final, 0.0, 1.0) * 255.0).astype(np.uint8)

stream_rgba = np.dstack([color_final, alpha_uint8])
img_stream = Image.fromarray(stream_rgba)
target_path = os.path.join(output_dir, 'bueiro_cascade_stream.png')
img_stream.save(target_path)
print("Saved cascade stream:", target_path, "Size:", img_stream.size)
