import os
from PIL import Image

p = r'c:\Users\Usuario\Documents\jogo\assets\reconstruction'
files = [
    'forjas_recycler.png',
    'cloth_stall.png',
    'market_salvage_cart.png',
    'forjas_workshop.png',
    'exchange_pavilion.png',
    'wholesale_arcade.png',
    'fundo_sorting_bank.png',
    'fundo_abandoned_engine.png',
    'fundo_collapsed_corner.png'
]

for f in files:
    fp = os.path.join(p, f)
    if os.path.exists(fp):
        img = Image.open(fp)
        bbox = img.getbbox() # (left, top, right, bottom)
        bw = bbox[2] - bbox[0]
        bh = bbox[3] - bbox[1]
        print(f"{f:<28} | Img: {img.size} | BBox: ({bbox[0]}, {bbox[1]}, {bbox[2]}, {bbox[3]}) -> {bw}x{bh}")
    else:
        print(f"{f} NOT FOUND")
