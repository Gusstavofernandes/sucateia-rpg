from pathlib import Path
import json,hashlib
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1]; out=root/'assets/reconstruction/cabos_parallel/audit_v1'
path='assets/reconstruction/cabos_parallel/main_deck_ew_wide.png'
im=Image.open(root/path).convert('RGBA'); w,h=im.size;a=im.getchannel('A');b=a.point(lambda x:255 if x>16 else 0).getbbox(); s=220/(b[2]-b[0])
points={'deck_w':(155,422),'deck_e':(1440,422),'lug_w_n':(84,205),'lug_e_n':(1510,205),'lug_w_s':(51,714),'lug_e_s':(1547,714),'support_w':(400,935),'support_e':(1190,935)}
clear=[180,155,1410,690]; pitch=(1440-155)*s
protected=json.loads((out/'manifest.json').read_text(encoding='utf-8'))['protected_png_hashes']
assert all(hashlib.sha256((root/p).read_bytes()).hexdigest()==v for p,v in protected.items())
m={'path':path,'sha256':hashlib.sha256((root/path).read_bytes()).hexdigest(),'canvas':[w,h],'alpha_extrema':a.getextrema(),'visible_bbox_gt16':b,'visible_margin_px':min(b[0],b[1],w-b[2],h-b[3]),'scale_uniform':s,'visible_world_size':[220,round((b[3]-b[1])*s,2)],'clear_walking_rectangle_native_estimated':clear,'clear_world_size_estimated':[(clear[2]-clear[0])*s,(clear[3]-clear[1])*s],'connections_native_estimated':points,'connections_offset_center_world':{k:[round((x-w/2)*s,3),round((y-h/2)*s,3)] for k,(x,y) in points.items()},'repeat_pitch_world_estimated':pitch,'support_socket_bbox_native_estimated':[[366,911,443,955],[1155,911,1230,955]],'walk_terminal_native_y_range_estimated':[155,690],'terminal_band_overlap_world_estimated':5,'method':'built-in image_gen + two depth revisions; PNG preserved unmodified','prompts':'assets/reconstruction/cabos_parallel/audit_v1/main_deck_prompts.json','variants_rejected':['assets/reconstruction/cabos_parallel/main_deck_ew_v1.png','assets/reconstruction/cabos_parallel/main_deck_ew_v2.png'],'accuracy':'Visual native estimates ±10px; not physics/collision certification. Conservative clear depth75.5px at supplied scale.','integration':'Open E-W terminals with coplanar flat joining bands. Repeat pitch approximate; preview overlap lugs/rail ends. Short underdeck sockets need existing tower/beam supports, not ground feet. Rail ends need same deck elevation. Do not use bbox for collision.','protected_png_count':len(protected),'protected_hashes_unchanged':True}
(out/'main_deck_manifest.json').write_text(json.dumps(m,indent=2,ensure_ascii=False),encoding='utf-8')
qa=Image.new('RGB',(1100,550),(124,132,120));d=ImageDraw.Draw(qa);tile=im.resize((round(w*s),round(h*s)),Image.Resampling.LANCZOS)
for x,y,annotate in [(40,50,True),(400,50,False),(400+round(pitch),50,False)]:
 qa.paste(tile,(x,y),tile)
 if annotate:
  d.rectangle((x+clear[0]*s,y+clear[1]*s,x+clear[2]*s,y+clear[3]*s),outline=(80,230,250),width=1)
  for k,(px,py) in points.items():
   qx=x+px*s;qy=y+py*s;d.ellipse((qx-2,qy-2,qx+2,qy+2),outline=(255,220,40));d.text((qx+3,qy),k,fill=(255,220,40))
d.text((40,20),'Selected module: world220x129; clear central floor ~174x75.5',fill='white')
d.text((400,20),'Two repeats: provisional pitch181.3; overlapping lugs/flat end bands',fill='white')
d.line((40,240,64,240),fill='white',width=2);d.text((40,252),'24px ruler',fill='white')
# Existing narrow crossing at documented gameplay scale for proportional comparison.
old=Image.open(root/'assets/reconstruction/cabos_parallel/suspension_bridge_ew.png').convert('RGBA');old=old.resize((round(old.width*.26),round(old.height*.26)),Image.Resampling.LANCZOS);qa.paste(old,(40,325),old)
d.text((40,300),'Existing secondary bridge: scale0.26; clear depth27-39; not main deck',fill='white')
qa.save(out/'qa_main_deck_gameplay.png')
assert 70<=m['clear_world_size_estimated'][1]<=85
assert all(0<=x<w and 0<=y<h for x,y in points.values())
assert a.getextrema()[0]==0 and m['visible_margin_px']>0
print(json.dumps(m,ensure_ascii=False))
