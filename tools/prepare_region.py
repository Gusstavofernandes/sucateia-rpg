from pathlib import Path
from PIL import Image,ImageOps
import sys
root=Path(__file__).resolve().parents[1]
for p in (root/'assets/region/source').glob('*.png'):
    if len(sys.argv)>1 and p.stem not in sys.argv[1:]: continue
    if p.stem=='salvage_ground': continue
    image=Image.open(p).convert('RGBA')
    assert image.getchannel('A').getextrema()[0]<255,p
    image=image.crop(image.getchannel('A').point(lambda a:255 if a>8 else 0).getbbox())
    size=(1024,1024) if p.stem in ['crown','ruined_engine'] else (768,768)
    fitted=ImageOps.contain(image,(size[0]-8,size[1]-8),Image.Resampling.LANCZOS)
    output=Image.new('RGBA',size)
    output.alpha_composite(fitted,((size[0]-fitted.width)//2,(size[1]-fitted.height)//2))
    output.save(root/'assets/region'/p.name)
    print(p.stem,fitted.size)
