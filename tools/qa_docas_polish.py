from pathlib import Path
from PIL import Image,ImageDraw
import json,hashlib
root=Path(__file__).resolve().parents[1];out=root/'assets/reconstruction/docas_parallel/complement_v1'
original=json.loads((root/'assets/reconstruction/docas_parallel/audit_v1/manifest.json').read_text(encoding='utf-8'));protected=original['protected_png_hashes']
assert all(hashlib.sha256((root/p).read_bytes()).hexdigest()==v for p,v in protected.items())
spec=[('pier_head_deep',270,{'deck_w':(145,417),'deck_e':(1390,417),'lug_w_n':(82,316),'lug_e_n':(1451,316),'lug_w_s':(64,549),'lug_e_s':(1470,549),'mooring_sw':(245,796),'pile_sw_foot':(137,938),'pile_se_foot':(1394,938)},[[88,884,195,975],[1340,884,1456,975]],{'clear_rectangle_native':[200,160,1325,640]},'Compact piled landing variation; shore continuity/support depths must be placed. Rear piles hidden below deck, front pile feet visible; not certified to seabed.'),('port_cargo_sling_cluster',110,{'lifting_ring':(765,78)},[[181,620,342,705],[705,859,893,975],[1233,529,1358,635]],{'largest_crate_native_width_estimated':540},'Bulk mixed cargo; largest crate about50px at scale, above prompt30 target. Use near loading station, no walking through cargo. Sling ring connection only to actual hook.'),('wet_wood_saltwear_decal',220,{},[],{'recommended_opacity':[.20,.30],'recommended_opacity_initial':.25},'Flat color/grain/salt marks; sample on timber at opacity.20/.30. No walking floor or physical support. Keep plank geometry visible.')]
entries=[];scaled={};qa=Image.new('RGB',(1200,600),(123,132,123));d=ImageDraw.Draw(qa)
for i,(name,width,pts,bases,extra,note) in enumerate(spec):
 p=out/(name+'.png');im=Image.open(p);a=im.getchannel('A');b=a.point(lambda x:255 if x>16 else 0).getbbox();w,h=im.size;s=width/(b[2]-b[0]);tile=im.resize((round(w*s),round(h*s)),Image.Resampling.LANCZOS);scaled[name]=tile
 e={'name':name,'path':p.relative_to(root).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'canvas':[w,h],'alpha_extrema':a.getextrema(),'visible_bbox_gt16':b,'minimum_visible_margin_px':min(b[0],b[1],w-b[2],h-b[3]),'scale_uniform':s,'visible_world_size':[width,round((b[3]-b[1])*s,2)],'connections_native_estimated':pts,'offset_center_world':{k:[round((x-w/2)*s,3),round((y-h/2)*s,3)] for k,(x,y) in pts.items()},'ground_contact_rectangles_native_estimated':bases,'measurements':extra,'notes':note,'status':'selected art; no scene/runtime validation'}
 if 'clear_rectangle_native' in extra:
  c=extra['clear_rectangle_native'];e['clear_world_size']=[(c[2]-c[0])*s,(c[3]-c[1])*s]
 entries.append(e);x=30+i*390;y=60;qa.paste(tile,(x,y),tile);d.text((x,20),f'{name}: {e["visible_world_size"]}',fill='white')
 for j,(k,(px,py)) in enumerate(pts.items(),1):
  qx=x+px*s;qy=y+py*s;d.ellipse((qx-2,qy-2,qx+2,qy+2),outline=(70,240,250));d.text((x,270+j*15),f'{j}: {k}',fill=(70,240,250))
 for c in bases:d.rectangle((x+c[0]*s,y+c[1]*s,x+c[2]*s,y+c[3]*s),outline=(255,220,40))
 if 'clear_rectangle_native' in extra:
  c=extra['clear_rectangle_native'];d.rectangle((x+c[0]*s,y+c[1]*s,x+c[2]*s,y+c[3]*s),outline=(70,240,250))
 d.line((x,480,x+24,480),fill='white',width=2);d.text((x,496),'24px',fill='white')
qa.save(out/'qa_gameplay_connections.png')
compare=Image.new('RGB',(1050,280),(123,132,123));dr=ImageDraw.Draw(compare)
for i,opacity in enumerate([0,.20,.30]):
 base=scaled['pier_head_deep'].copy();decal=scaled['wet_wood_saltwear_decal'].copy();decal.putalpha(decal.getchannel('A').point(lambda a:round(a*opacity)));base.alpha_composite(decal,(25,45));compare.paste(base,(20+i*345,35),base);dr.text((20+i*345,12),f'Timber original / coastal marks opacity {opacity}',fill='white')
compare.save(out/'qa_saltwear_on_timber.png')
prompts=json.loads((out/'prompts.json').read_text(encoding='utf-8'))
m={'authorization':'Human requests professional finish even if more assets; complements add concrete piled structure, slung cargo and material transition variety.','selected':entries,'prompts_sources':prompts,'variant_rejected':{'path':'assets/reconstruction/docas_parallel/complement_v1/pier_head_v1.png','reason':'Clear central depth insufficient for broad landing at compact size; preserved source.'},'qa':['qa_gameplay_connections.png','qa_saltwear_on_timber.png'],'accuracy':'Visual points ±10nativepx; conservative clear rectangle; source PNGs never edited with Pillow.','protected_png_count':len(protected),'protected_sources_unchanged':True}
(out/'manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(e['alpha_extrema'][0]==0 and e['minimum_visible_margin_px']>0 for e in entries)
assert entries[0]['clear_world_size'][1]>=85
print(json.dumps([{k:e[k] for k in ['name','scale_uniform','visible_world_size','minimum_visible_margin_px']} for e in entries],ensure_ascii=False));print('PASS:121 protected originals unchanged;3 selections plus preserved pier variant; transparent, contained; no runtime.')
