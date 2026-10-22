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

# Load high quality frames from user's animation
f1 = load_frame(42)
f2 = load_frame(128)

w, h = 512, 1024
y_grid, x_grid = np.mgrid[0:h, 0:w]
cx = w / 2.0

# Extract a tall vertical stream texture directly from the user's water frame
# Rotating 90 degrees or scaling vertically aligns the swirling flow with the downward stream!
water_crop1 = f1.crop((120, 60, 1160, 660)).resize((w, h), Image.Resampling.LANCZOS)
water_crop2 = f2.crop((120, 60, 1160, 660)).resize((w, h), Image.Resampling.LANCZOS)
water_arr = np.array(water_crop1).astype(np.float32) * 0.6 + np.array(water_crop2).astype(np.float32) * 0.4

# Smooth stream envelope without ANY synthetic sine grating:
y_norm = y_grid / float(h)

# Stream width in pixels across height:
# Top (under bueiro arch): width ~ 180px
# Middle chute: gentle natural width ~ 160-200px
# Bottom splash apron into canal: widens smoothly to ~ 360px
w_top = 180.0
w_mid = 175.0
w_bot = 380.0

# Smooth cubic hermite interpolation for the width profile:
t_top = np.clip(y_norm / 0.25, 0.0, 1.0)
s_top = t_top * t_top * (3.0 - 2.0 * t_top)
stream_w1 = w_top * (1.0 - s_top) + w_mid * s_top

t_bot = np.clip((y_norm - 0.70) / 0.30, 0.0, 1.0)
s_bot = t_bot * t_bot * (3.0 - 2.0 * t_bot)
stream_width = stream_w1 * (1.0 - s_bot) + w_bot * s_bot

# Gentle organic meandering (centerline drift of only +/- 15px over 1024px)
center_drift = 12.0 * np.sin(y_norm * np.pi * 1.5) + 6.0 * np.cos(y_norm * np.pi * 3.5)

dist_from_axis = np.abs(x_grid - (cx + center_drift))
half_w = stream_width / 2.0

# Calculate natural feathered alpha mask:
# Deep core (dist < 0.65 * half_w) is fully opaque.
# Outer rim (0.65 * half_w to half_w) smoothly fades out with water froth.
inner_w = half_w * 0.65
alpha = np.zeros_like(dist_from_axis, dtype=np.float32)

core_mask = dist_from_axis <= inner_w
edge_mask = (dist_from_axis > inner_w) & (dist_from_axis <= half_w)

alpha[core_mask] = 1.0
t_edge = (half_w[edge_mask] - dist_from_axis[edge_mask]) / (half_w[edge_mask] - inner_w[edge_mask] + 1e-4)
alpha[edge_mask] = t_edge * t_edge * (3.0 - 2.0 * t_edge)

# Top fade-in (coming from darkness beneath the arch):
top_fade = np.clip(y_norm / 0.06, 0.0, 1.0)
# Bottom fade into canal water:
bot_fade = np.clip((1.0 - y_norm) / 0.015, 0.0, 1.0) * 0.2 + 0.8
alpha = alpha * top_fade * bot_fade

# Foam edge highlights from the user's actual texture:
# Detect bright foam pixels already present in the user's art:
lum = np.dot(water_arr[..., :3], [0.299, 0.587, 0.114])
is_natural_foam = np.clip((lum - 55.0) / 45.0, 0.0, 1.0)

# Boost foam along the edges and in the plunge pool
edge_proximity = np.clip((dist_from_axis - inner_w * 0.5) / (half_w - inner_w * 0.5 + 1e-4), 0.0, 1.0)
foam_boost = is_natural_foam * edge_proximity * 35.0
# Plunge pool extra foam at bottom
plunge_foam = is_natural_foam * t_bot * 45.0

water_arr_boosted = water_arr + (foam_boost + plunge_foam)[..., None] * np.array([0.7, 1.0, 0.8])

# Final RGBA assembly
rgba = np.dstack([
    np.clip(water_arr_boosted, 0, 255).astype(np.uint8),
    (np.clip(alpha, 0.0, 1.0) * 255.0).astype(np.uint8)
])

img = Image.fromarray(rgba)
# Subtle 1px gaussian blur on alpha channel only to make contact with stone look wet and soft
alpha_pil = Image.fromarray(rgba[..., 3]).filter(ImageFilter.GaussianBlur(radius=1.2))
img.putalpha(alpha_pil)

target_path = os.path.join(output_dir, 'bueiro_cascade_stream.png')
img.save(target_path)
print("Saved clean cascade stream:", target_path)
