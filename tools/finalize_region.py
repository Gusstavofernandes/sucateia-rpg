from pathlib import Path
import json,hashlib,zipfile,shutil
from PIL import Image,ImageOps,ImageDraw,ImageFont
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'maps/ferrugem_baixa/region.json').read_text(encoding='utf-8'))
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',19)
atlas=Image.new('RGB',(2048,1536),(15,24,21))
draw=ImageDraw.Draw(atlas)
for i,(name,config) in enumerate(data.items()):
    path=root/('maps/sucateia/preview_centre.png' if name=='centre' else f'maps/ferrugem_baixa/preview_{name}.png')
    image=ImageOps.contain(Image.open(path).convert('RGB'),(508,343))
    x=(i%4)*512;y=(i//4)*384
    atlas.paste(image,(x+(512-image.width)//2,y+32))
    draw.text((x+10,y+6),config['name'],font=font,fill=(217,189,128))
atlas.save(root/'maps/ferrugem_baixa/visual_audit.png')
approved=json.loads((root/'tools/approved_art_hashes.json').read_text(encoding='utf-8'))
for rel,digest in approved.items(): assert hashlib.sha256((root/rel).read_bytes()).hexdigest()==digest,rel
for log in ['test_slice.log','test_region.log','region_travel_test.log','test_continuity.log']:
    text=(root/'tools'/log).read_text(encoding='utf-8-sig')
    assert 'PASS:' in text and 'ERROR:' not in text and 'SCRIPT ERROR' not in text,log
assets={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted((root/'assets').rglob('*')) if p.is_file() and p.suffix in ['.png','.svg','.gdshader','.tres']}
checkpoint=root/'tools/checkpoints'
(checkpoint/'ferrugem_baixa_assets.json').write_text(json.dumps(assets,indent=2),encoding='utf-8')
old=checkpoint/'ferrugem_baixa_integrada.zip'
if old.exists() and not (checkpoint/'ferrugem_baixa_primeira_base.zip').exists(): shutil.copy2(old,checkpoint/'ferrugem_baixa_primeira_base.zip')
paths=[p for folder in ['maps','scripts','scenes','tests'] for p in (root/folder).rglob('*') if p.suffix in ['.gd','.tscn','.json']]
paths += list((root/'assets').rglob('*.gdshader'))
paths += [root/'project.godot',root/'licenses/assets.md',root/'tools/REGION_STATUS.md',root/'tools/build_region.gd',root/'tools/prepare_region.py',Path(__file__)]
paths += list((root/'tools').glob('*prompt*.json'))+list((root/'tools').glob('*art*.json'))+[checkpoint/'ferrugem_baixa_assets.json']
paths += [root/'tools/NORTH_CONNECTION_PLAN.md',root/'tools/refine_region_data.py',root/'tools/update_region_status.py']
paths += [root/'tools/FERRUGEM_CONTINUITY.md',root/'tools/plan_continuity.py']
paths += [root/'tools/test_continuity.log']
paths += [root/'docs/superpowers/plans/2026-10-02-ferrugem-continuidade.md']
paths += [root/'tools'/p for p in ['test_slice.log','test_region.log','region_travel_test.log']]
with zipfile.ZipFile(old,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(set(paths)): z.write(p,p.relative_to(root))
print('VERIFIED:',len(data),'maps;',sum(len(c['links']) for c in data.values()),'directed links; 5 protected sprites unchanged;',len(assets),'asset hashes;',len(set(paths)),'checkpoint files')
