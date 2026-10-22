"""Read-only source audit; creates metadata and QA previews, never production sprites."""
from pathlib import Path
import hashlib,json
from PIL import Image,ImageDraw

root=Path(__file__).resolve().parents[1]
out=root/'assets/reconstruction/cabos_parallel/audit_v1'
out.mkdir(exist_ok=True)
specs=[
 ('hanging_house','assets/reconstruction/cabos_parallel/hanging_house.png',.28,{'beam_w':(210,112),'beam_e':(1160,112),'door_s':(565,931)},[350,900,1010,974],{'door_width_native':80},'Revised scale: visible total about367px; door22px. Upper beams need real structural attachments; roof is not a walkable surface.'),
 ('suspension_bridge_ew','assets/reconstruction/cabos_parallel/suspension_bridge_ew.png',.26,{'deck_w':(60,375),'deck_e':(2105,375),'anchor_w':(181,205),'anchor_e':(1980,205)},None,{'clear_projected_depth_native_range':[105,150]},'Secondary narrow crossing. Center sags; deck depth27–39px at this scale. Measure collision corridor separately.'),
 ('walkway_t_junction_clean','assets/reconstruction/cabos_parallel/walkway_t_junction_clean.png',.38,{'deck_w':(50,680),'deck_e':(1490,680),'deck_n':(772,170),'support_center':(774,740)},None,{'branch_clear_width_native_range':[95,120],'ew_clear_projected_depth_native_range':[85,105]},'Total width570px; north branch36–46px, E-W projected clear depth32–40px. Needs strengthened support under center. Not a spawn platform by itself.'),
 ('power_messenger_anchor','assets/reconstruction/cabos_parallel/power_messenger_anchor.png',.16,{'socket_w':(385,51),'socket_e':(1097,164),'base':(705,1070)},[577,1038,850,1098],{},'Visible width133px. Power/message mast; not a certified main load-bearing support.'),
 ('stairs_reuse','assets/infrastructure/stairs.png',.65,{'upper_n':(140,31),'lower_s':(141,189)},[56,181,238,211],{'clear_width_native_range':[76,132]},'Existing ground-to-walkway access. Clear width49–86px, upper landing is the bottleneck. Upper terminal must meet actual deck height; short stair flight is not a lift or high tower ladder.'),
 ('walkway_reuse','assets/infrastructure/walkway.png',.6,{'deck_n':(143,30),'deck_s':(143,246)},None,{'clear_width_native_range':[110,170]},'Clear N-S width66–102px. Existing wider access/landing segment. Place at stair/T transitions; preserve camera rather than rotate baked image indiscriminately.'),
 ('cable_tower_reuse','assets/region/cable_tower.png',.4,{'beam_w':(239,118),'beam_e':(488,158),'platform':(370,338),'base':(371,711)},[264,665,505,756],{},'Existing structural tower, suitable repeated intermediate anchorage near deck terminals and reinforced T. Beam points are at different projected heights; placement needs independent alignment. Keeps small hut/hoists; avoid dense repeated silhouette.'),
 ('service_arch_reuse','assets/infrastructure/service_arch.png',.8,{'crown':(105,54),'base':(105,134)},[8,113,196,141],{},'Low retaining/contact support at Forjas entrance, not full elevated-span support by itself.'),
]
protected={p.relative_to(root).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for folder in ['assets/reconstruction/cabos_parallel','assets/reconstruction/docas_parallel','assets/reconstruction/forjas_parallel','assets/reconstruction/amarras_parallel','assets/infrastructure','assets/region'] for p in (root/folder).rglob('*.png') if 'audit_v1' not in p.parts}
entries=[]
sheet=Image.new('RGB',(1800,1480),(119,129,119)); d=ImageDraw.Draw(sheet)
for i,(name,path,scale,points,base,measure,note) in enumerate(specs):
 im=Image.open(root/path).convert('RGBA'); a=im.getchannel('A'); bbox=a.point(lambda v:255 if v>16 else 0).getbbox(); w,h=im.size
 entry={'name':name,'path':path,'sha256':hashlib.sha256((root/path).read_bytes()).hexdigest(),'canvas':[w,h],'alpha_extrema':a.getextrema(),'visible_bbox_gt16':bbox,'visible_margin_px':min(bbox[0],bbox[1],w-bbox[2],h-bbox[3]),'suggested_uniform_scale':scale,'visible_world_size': [round((bbox[2]-bbox[0])*scale,1),round((bbox[3]-bbox[1])*scale,1)],'connections_native_estimated':points,'connections_offset_center_world':{k:[round((x-w/2)*scale,2),round((y-h/2)*scale,2)] for k,(x,y) in points.items()},'floor_contact_bbox_native_estimated':base,'visual_measurements_estimated':measure,'notes':note,'status':'art audit only; placement/collision/occlusion not validated'}
 entries.append(entry)
 col=i%2; row=i//2; x=col*900+30; y=row*370+45
 d.text((x,y-28),name+f'  scale {scale}  world {entry["visible_world_size"]}',fill='white')
 # Show full canvas at exactly proposed gameplay scale, no crop or source change.
 preview=im.resize((round(w*scale),round(h*scale)),Image.Resampling.LANCZOS)
 sheet.paste(preview,(x,y),preview)
 for label,(px,py) in points.items():
  qx=x+round(px*scale);qy=y+round(py*scale)
  d.ellipse((qx-3,qy-3,qx+3,qy+3),outline=(50,235,250),width=1)
  d.text((qx+5,qy),label,fill=(50,235,250))
 if base:
  d.rectangle((x+round(base[0]*scale),y+round(base[1]*scale),x+round(base[2]*scale),y+round(base[3]*scale)),outline=(255,224,60),width=1)
 d.line((x+650,y+30,x+674,y+30),fill='white',width=2);d.text((x+650,y+40),'24px',fill='white')
sheet.save(out/'qa_gameplay_connections.png')
manifest={'brief':'tools/CONSULTANT_CABOS_BRIEF.md','decision':'Reuse existing stairs and cable_tower; zero new production PNGs. Correct previous scale assumptions using measured artwork.','coordinate_accuracy':'visual estimates ±10 native pixels on large sprites, ±3 on small originals; not collision bounds','assets':entries,'protected_png_hashes':protected,'scope':'No source PNG, scene, import or runtime change; QA resized copies only.'}
(out/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(hashlib.sha256((root/p).read_bytes()).hexdigest()==v for p,v in protected.items())
print(json.dumps({'audited':len(entries),'protected_pngs':len(protected),'source_pngs_unchanged':True,'output':str(out),'assets':[{k:e[k] for k in ['name','canvas','visible_world_size','visible_margin_px']} for e in entries]},ensure_ascii=False))
