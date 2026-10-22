import os
from PIL import Image

for name in ['alto_cistern.png', 'forjas_boiler_hall.png']:
    fp = os.path.join(r'c:\Users\Usuario\Documents\jogo\assets\reconstruction', name)
    im = Image.open(fp)
    print(f"=== {name} ===")
    bbox = im.getbbox()
    print(f"Size: {im.size}, BBox: {bbox}")
    # Inspect bottom 50 pixels of bbox
    cropped = im.crop((bbox[0], bbox[3]-60, bbox[2], bbox[3]))
    print(f"Bottom crop size: {cropped.size}")
