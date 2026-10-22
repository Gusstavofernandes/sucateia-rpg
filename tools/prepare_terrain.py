from pathlib import Path
from PIL import Image, ImageOps, ImageFilter
import json, shutil
root=Path(__file__).resolve().parents[1]
records=json.loads((root/'tools/terrain_prompts.json').read_text())
for item in records:
    path=root/'assets/terrain/source'/(item['name']+'.png')
    if not path.exists():shutil.copy2(item['source'],path)
raw=Image.open(root/'assets/terrain/source/terrain.png').convert('RGB').resize((384,384),Image.Resampling.LANCZOS)
# Mirror-wrap once at a broad scale: exact matching borders, no square seams.
atlas=Image.new('RGB',(768,768));atlas.paste(raw,(0,0));atlas.paste(ImageOps.mirror(raw),(384,0));atlas.paste(ImageOps.flip(raw),(0,384));atlas.paste(ImageOps.flip(ImageOps.mirror(raw)),(384,384));atlas.save(root/'assets/terrain/floor_atlas.png')
image=Image.open(root/'assets/terrain/source/decals.png').convert('RGBA');w,h=image.size
for name,box in zip(['foundation','metal_repair','oil_hatch','market_dirt'],[(0,0,w//2,h//2),(w//2,0,w,h//2),(0,h//2,w//2,h),(w//2,h//2,w,h)]):
    part=image.crop(box);bounds=part.getchannel('A').point(lambda a:255 if a>12 else 0).getbbox();part=part.crop(bounds)
    fitted=ImageOps.contain(part,(250,250),Image.Resampling.LANCZOS)
    canvas=Image.new('RGBA',(256,256));canvas.alpha_composite(fitted,((256-fitted.width)//2,(256-fitted.height)//2));canvas.save(root/'assets/terrain'/(name+'.png'))
(root/'assets/terrain/source/.gdignore').write_text('')
print('Terrain atlas: 768px / 48px cells; four alpha stamps prepared')
