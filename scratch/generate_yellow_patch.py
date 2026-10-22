from PIL import Image
import numpy as np

im = Image.open('assets/reconstruction/red_soil_transition_patch.png').convert("RGBA")
arr = np.array(im, dtype=np.float32)
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

# The original has high R and lower G and low B (red rust)
# We want warm yellowish ochre coastal soil: R high (~200), G medium-high (~175), B medium (~110)
# Let's adjust G and B:
# increase G significantly, increase B slightly
g_new = np.clip(g * 1.55 + 20, 0, 255)
b_new = np.clip(b * 1.25 + 10, 0, 255)
r_new = np.clip(r * 0.95 + 10, 0, 255)

out_arr = np.dstack([
    r_new.astype(np.uint8),
    g_new.astype(np.uint8),
    b_new.astype(np.uint8),
    a.astype(np.uint8)
])

out_img = Image.fromarray(out_arr)
dst = 'assets/reconstruction/yellow_coastal_soil_patch.png'
out_img.save(dst)
print("Salvo:", dst)
