from pathlib import Path
import json,shutil
from PIL import Image,ImageOps
root=Path(__file__).resolve().parents[1]
for entry in json.loads((root/'tools/vhal_art.json').read_text(encoding='utf-8')):
    name=entry['name'];source=root/f'assets/vhal/source/{name}.png'
    shutil.copy2(entry['path'],source)
    image=Image.open(source).convert('RGBA')
    if name=='stone_ground':
        output=ImageOps.fit(image,(768,768),Image.Resampling.LANCZOS)
    else:
        assert image.getchannel('A').getextrema()[0]<255,name
        image=image.crop(image.getchannel('A').point(lambda a:255 if a>8 else 0).getbbox())
        size=1024 if name=='twin_towers' else 768
        fitted=ImageOps.contain(image,(size-12,size-12),Image.Resampling.LANCZOS)
        output=Image.new('RGBA',(size,size));output.alpha_composite(fitted,((size-fitted.width)//2,(size-fitted.height)//2))
    output.save(root/f'assets/vhal/{name}.png')
    print(name,output.size)
