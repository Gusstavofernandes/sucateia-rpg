"""Audit existing art, write new metadata/QA; never change production PNGs."""
from pathlib import Path
import hashlib,json
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parents[1];out=root/'assets/reconstruction/docas_parallel/audit_v1';out.mkdir(exist_ok=True)
protected={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for folder in ['assets/reconstruction','assets/infrastructure','assets/region'] for p in (root/folder).rglob('*.png') if 'audit_v1' not in p.parts}
specs=[
 ('cargo_barge',330,{'bow_bollard':(232,420),'aft_rail_tie':(1372,650),'mid_rail_tie':(940,618),'winch_exit':(1360,547),'cargo_reach_s':(820,624)},[],{'waterline_guide_native_polyline':[(105,435),(330,640),(800,730),(1400,730),(1630,620)],'largest_crate_native_width_estimated':160},'Water object, E-W bow west/stern east. Loaded hold not walkable. Waterline is visual placement guide, not an alpha mask. Do not submerge/fade whole lower hull or fenders blindly.'),
 ('cargo_sorting_shelter',270,{'workfront_s':(690,890),'cupboard_threshold':(1120,938),'bollard_w_rope':(135,772),'rope_spool':(686,712)},[[110,835,360,900],[955,898,1050,960],[1230,900,1320,980]],{'cupboard_native_width_estimated':130,'overall_ground_envelope_estimated':[110,825,1320,980]},'Dry land. Floor is not included. Crates/bench obstruct southern interior; reserve external workfront space. Roof is slightly skewed; do not rotate/mirror to force coastal alignment.'),
 ('mooring_capstan',140,{'bollard_w_rope':(299,602),'bollard_e_rope':(1297,618),'drum_w_tangent':(600,580),'drum_e_tangent':(910,590)},[[133,710,480,790],[510,735,1010,832],[1080,704,1430,790]],{'drum_native_diameter_estimated':400},'Dry quay. Handles extend well beyond footprint. Tie boat to bollard waist; show traction tangent to drum with scene rope guide. Do not attach traction to axle/top bolt. Mechanical holding and base anchorage still need placement.'),
 ('naval_repair_cradle',220,{'bow_eye':(155,309),'stern_eye':(1580,250),'support_w':(550,792),'support_e':(1268,810),'service_access_s':(900,720)},[[400,755,725,824],[1120,768,1400,834]],{'overall_ground_envelope_estimated':[360,600,1460,834]},'Dry support frame. Both trestle feet must contact land/slipway. Shore water relation through nearby ramp/access/launch line, not by floating this trestle. Empty hull is repair equipment, not safe spawn platform.'),
]
entries=[];qa=Image.new('RGB',(1300,900),(121,132,124));d=ImageDraw.Draw(qa)
for i,(name,target,points,bases,extra,note) in enumerate(specs):
 path=f'assets/reconstruction/docas_parallel/{name}.png';im=Image.open(root/path);assert im.mode=='RGBA';w,h=im.size;a=im.getchannel('A');b=a.point(lambda v:255 if v>16 else 0).getbbox();s=target/(b[2]-b[0]);
 e={'name':name,'path':path,'sha256':hashlib.sha256((root/path).read_bytes()).hexdigest(),'canvas':[w,h],'alpha_extrema':a.getextrema(),'visible_bbox_gt16':b,'visible_margin_px':min(b[0],b[1],w-b[2],h-b[3]),'scale_uniform':s,'visible_world_size':[target,round((b[3]-b[1])*s,2)],'connections_native_estimated':points,'connections_offset_center_world':{k:[round((x-w/2)*s,2),round((y-h/2)*s,2)] for k,(x,y) in points.items()},'ground_contact_rectangles_native_estimated':bases,'ground_contact_world_sizes_estimated':[[round((p[2]-p[0])*s,2),round((p[3]-p[1])*s,2)] for p in bases],'visual_measurements':extra,'notes':note,'status':'art handoff only; scene placement/water/collision not validated'};entries.append(e)
 x=40+(i%2)*650;y=60+(i//2)*400;tile=im.resize((round(w*s),round(h*s)),Image.Resampling.LANCZOS);qa.paste(tile,(x,y),tile)
 d.text((x,y-30),f'{name} / world {e["visible_world_size"]} / scale {s:.6f}',fill='white')
 for j,(label,(px,py)) in enumerate(points.items(),1):
  qx=x+px*s;qy=y+py*s;d.ellipse((qx-2,qy-2,qx+2,qy+2),outline=(70,235,250));d.text((qx+4,qy-8),str(j),fill=(70,235,250))
  d.text((x,y+230+j*16),f'{j}: {label} native({px},{py})',fill=(70,235,250))
 for p in bases:d.rectangle((x+p[0]*s,y+p[1]*s,x+p[2]*s,y+p[3]*s),outline=(255,220,50),width=1)
 if 'waterline_guide_native_polyline' in extra:d.line([(x+px*s,y+py*s) for px,py in extra['waterline_guide_native_polyline']],fill=(65,145,250),width=2)
 d.line((x+450,y+60,x+474,y+60),fill='white',width=2);d.text((x+450,y+74),'24px',fill='white')
qa.save(out/'qa_gameplay_connections.png')
reuse=[{'path':p,'function':f} for p,f in [
 ('assets/infrastructure/coastal_wall.png','Existing quay stone cap, timber piles, embedded bollards and moss/waterline transition.'),
 ('assets/infrastructure/retaining_edge.png','Short urban stone retaining edge; not a broad walkable quay floor.'),
 ('assets/reconstruction/cabos_parallel/main_deck_ew_wide.png','Wide E-W deck on existing shoreline/pier supports; reuse .1411161 scale and75.5px clear painted depth. No loose floating pier.'),
 ('assets/infrastructure/walkway.png','N-S approach deck, .60 example scale; needs proper shore/support contact.'),
 ('assets/infrastructure/stairs.png','Pedestrian vertical access. Not a wheeled-cargo ramp.'),
 ('assets/infrastructure/crane.png','Existing loading crane with stone base/contained chain hook; land base and actual load connection required.'),
 ('assets/reconstruction/forjas_parallel/compact_loading_crane.png','Alternative compact crane; choose one per functional station, avoid duplicate clutter.'),
 ('assets/region/dock_warehouse.png','Existing storage building with cargo crane, public workfront and mooring rings.'),
 ('assets/region/wreck_cradle.png','Large derelict salvage hull structure; identity differs from actively repaired new cradle, not needed to duplicate repair function.'),
 ('assets/reconstruction/market_salvage_cart.png','General small cargo transport rather than ore-only port stock.'),
 ('assets/reconstruction/amarras_parallel/chain_winch_station.png','Technical traction from land; add guide/rope or chain connection to real load.'),
 ('assets/reconstruction/amarras_parallel/damp_anchor_runoff_decal_stains.png','Restrained rust/mineral damp stains; initial alpha.25; not a certified wood-limo texture.'),
 ('assets/reconstruction/amarras_parallel/chain_drag_wear_decal_marks.png','Flat cargo wheel/chain drag wear; initial alpha.30.'),
 ('assets/infrastructure/lantern.png','Existing functional light at cargo/access station.'),
]]
for e in reuse:assert (root/e['path']).exists()
m={'brief':'tools/CONSULTANT_DOCAS_BRIEF.md','decision':'Four existing production PNGs retained; no concrete missing production asset proven before placement. No new generation.','accuracy':'Visual native coordinates ±10 pixels; conservative floor/contact guides, not gameplay collision shapes.','assets':entries,'reusable_inventory':reuse,'protected_png_hashes':protected,'scope':'Only new audit metadata/QA/docs; source PNGs preserved; no scene/import/runtime executed.'}
(out/'manifest.json').write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(hashlib.sha256((root/p).read_bytes()).hexdigest()==v for p,v in protected.items())
assert all(e['alpha_extrema'][0]==0 and e['visible_margin_px']>0 for e in entries)
assert all(0<=x<e['canvas'][0] and 0<=y<e['canvas'][1] for e in entries for x,y in e['connections_native_estimated'].values())
print(json.dumps({'audited':4,'reuse_candidates':len(reuse),'protected_pngs':len(protected),'hashes_unchanged':True,'measurements':[{k:e[k] for k in ['name','scale_uniform','visible_world_size','visible_margin_px']} for e in entries]},ensure_ascii=False))
