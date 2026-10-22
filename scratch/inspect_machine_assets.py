import os
from PIL import Image

dirs = [
    r'c:\Users\Usuario\Documents\jogo\assets\machines',
    r'c:\Users\Usuario\Documents\jogo\assets\infrastructure',
    r'c:\Users\Usuario\Documents\jogo\assets\region'
]

for d in dirs:
    print(f"=== {d} ===")
    for f in os.listdir(d):
        if f.endswith('.png') and not f.endswith('_sombra.png'):
            fp = os.path.join(d, f)
            try:
                im = Image.open(fp)
                print(f"  {f:<35} | {im.size} | {im.mode}")
            except:
                pass
