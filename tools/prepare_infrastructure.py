from pathlib import Path
import json,shutil,hashlib
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).resolve().parents[1]
records=json.loads((root/'tools/infrastructure_prompts.json').read_text())
targets={'retaining_edge':(384,160),'stairs':(288,220),'walkway':(288,288),'service_arch':(200,190),'crane':(300,440),'lantern':(64,96),'scrap':(368,200)}
contact=Image.new('RGB',(1200,660),(32,39,37));draw=ImageDraw.Draw(contact)
for i,item in enumerate(records):
    name=item['name'];raw=root/'assets/infrastructure/source'/(name+'.png')
    if not raw.exists():shutil.copy2(item['source'],raw)
    image=Image.open(raw).convert('RGBA')
    if name=='channel':
        output=image.convert('RGB').resize((512,512),Image.Resampling.LANCZOS)
    else:
        if image.getchannel('A').getextrema()[0]==255:raise ValueError(name+': sem alpha')
        bbox=image.getchannel('A').point(lambda a:255 if a>8 else 0).getbbox();image=image.crop(bbox)
        width,height=targets[name];fitted=ImageOps.contain(image,(width-8,height-8),Image.Resampling.LANCZOS)
        output=Image.new('RGBA',(width,height));output.alpha_composite(fitted,((width-fitted.width)//2,(height-fitted.height)//2))
    output.save(root/'assets/infrastructure'/(name+'.png'))
    thumb=ImageOps.contain(image,(280,280),Image.Resampling.LANCZOS);x=(i%4)*300;y=(i//4)*330
    contact.paste(thumb,(x+(300-thumb.width)//2,y+10),thumb);draw.text((x+10,y+305),name,fill=(225,209,174))
    print(name,output.size)
contact.save(root/'tools/infrastructure_contact.png');(root/'assets/infrastructure/source/.gdignore').write_text('')
# Guard the existing approved building art against accidental edits.
paths=['house','house_stack','workshop','reactor'];guard={str(p.relative_to(root)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in [root/'assets/generated/structures'/(n+'.png') for n in paths]+[root/'assets/generated/props/market_stall.png']}
(root/'tools/approved_art_hashes.json').write_text(json.dumps(guard,indent=2))
