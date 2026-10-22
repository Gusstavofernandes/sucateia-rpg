from pathlib import Path
import json, shutil
from PIL import Image, ImageOps, ImageDraw
ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'tools/art_manifest.json').read_text(encoding='utf8'))
targets={'house':('structures',(320,320)),'house_stack':('structures',(320,320)),'workshop':('structures',(416,368)),'reactor':('structures',(256,296)),'market_stall':('props',(208,152)),'bridge':('props',(384,124)),'pipe':('props',(128,36)),'skyline':('structures',(1200,360))}
contact=Image.new('RGB',(1200,((len(manifest)+3)//4)*330),(31,38,38));draw=ImageDraw.Draw(contact)
for i,record in enumerate(manifest):
    name=record['name'];raw=ROOT/'assets/generated/source'/f'{name}.png'
    if not raw.exists(): shutil.copy2(record['source'],raw)
    image=Image.open(raw).convert('RGBA');alpha=image.getchannel('A')
    if alpha.getextrema()[0]==255:raise ValueError(f'{name}: sem transparência real')
    bbox=alpha.point(lambda a:255 if a>8 else 0).getbbox()
    if not bbox:raise ValueError(name+': sprite vazio')
    image=image.crop(bbox)
    folder,(w,h)=targets[name]
    # Preserve alpha, proportions and a bottom-centered base anchor. 2x runtime resolution.
    padding=max(4,min(20,int(min(w,h)*.1)))
    fitted=ImageOps.contain(image,(w*2-padding,h*2-padding),Image.Resampling.LANCZOS)
    output=Image.new('RGBA',(w*2,h*2));output.alpha_composite(fitted,((w*2-fitted.width)//2,h*2-padding//2-fitted.height))
    dest=ROOT/'assets/generated'/folder/(name+'.png');output.save(dest,optimize=True)
    record.update({'sprite':str(dest.relative_to(ROOT)).replace('\\','/'),'canvas':[w,h],'alpha_bbox':list(output.getchannel('A').getbbox()),'method':'built-in image_gen; alpha trim and proportional 2x preparation only'})
    thumb=ImageOps.contain(image,(280,285),Image.Resampling.LANCZOS);x=(i%4)*300;y=(i//4)*330
    contact.paste(thumb,(x+(300-thumb.width)//2,y+20),thumb);draw.text((x+15,y+310),name,fill=(220,211,181))
    print(name,image.size,'->',output.size)
contact.save(ROOT/'tools/generated_contact.png')
(ROOT/'tools/art_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
