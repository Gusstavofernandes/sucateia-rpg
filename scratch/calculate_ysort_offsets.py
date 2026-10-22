import os
from PIL import Image

src_dir = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\reconstruction'

files = [
    ('forjas_recycler.png', 0.26),
    ('cloth_stall.png', 0.26),
    ('market_salvage_cart.png', 0.22),
    ('exchange_pavilion.png', 0.27),
    ('forjas_workshop.png', 0.27),
    ('wholesale_arcade.png', 0.28),
    ('fundo_sorting_bank.png', 0.26),
    ('fundo_abandoned_engine.png', 0.28),
    ('fundo_collapsed_corner.png', 0.28),
    ('alto_cistern.png', 0.24)
]

for fname, scale in files:
    img = Image.open(os.path.join(src_dir, fname))
    w, h = img.size
    bbox = img.getbbox() # (left, top, right, bottom)
    # The foot of the object is bbox[3].
    # By default, a Sprite2D with offset=(0,0) centers the texture at (0,0), so top is -h/2, bottom is +h/2.
    # To place bbox[3] at local y = 0, we need offset_y = -(bbox[3] - h/2)
    offset_y = -(bbox[3] - h / 2.0)
    # Contact collision height: bottom 15% to 25% of the object
    col_w = (bbox[2] - bbox[0]) * 0.75
    col_h = (bbox[3] - bbox[1]) * 0.18
    # In local coordinates of the unscaled child, or child with scale = 1/scale:
    print(f"Asset: {fname:<26} | Size: {w}x{h} | BBox bottom: {bbox[3]} | Recommended offset_y: {offset_y:6.1f} | Scaled Footprint: {col_w*scale:.0f}x{col_h*scale:.0f} px")
