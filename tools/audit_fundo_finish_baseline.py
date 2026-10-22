"""Read saved scenes/images only; no Godot, import or runtime mutation."""
from pathlib import Path
import hashlib,json,re
from datetime import datetime,timezone,timedelta
root=Path(__file__).resolve().parents[1]
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def scene_nodes(path):
    text=path.read_text(encoding='utf-8-sig')
    nodes=[]
    for match in re.finditer(r'\[node ([^\n]+)\]\n(.*?)(?=\n\[node |\Z)',text,re.S):
        head,body=match.groups()
        node=dict(re.findall(r'(name|type|parent)="([^"]*)"',head))
        node['body']=body;nodes.append(node)
    return text,nodes
def vector(body,key='position'):
    match=re.search(re.escape(key)+r' = Vector2\(([-\d.]+), ([-\d.]+)\)',body)
    return list(map(float,match.groups())) if match else None
underground=root/'maps/fundo_ferro/fundo_ferro.tscn';surface=root/'maps/sucateia/sucateia.tscn'
text,nodes=scene_nodes(underground);_,surface_nodes=scene_nodes(surface)
rooms={n['name']:vector(n['body']) for n in nodes if n.get('parent')=='Rooms'}
routes={}
for node in nodes:
    if node.get('parent')!='Routes':continue
    match=re.search(r'metadata/points = PackedVector2Array\(([^)]+)\)',node['body'])
    values=list(map(float,match[1].split(',')));routes[node['name']]=[values[i:i+2] for i in range(0,len(values),2)]
accesses={n['name']:vector(n['body']) for n in nodes if n.get('parent')=='LayerEntrances' and n.get('type')=='Area2D'}
surface_accesses={n['name']:vector(n['body']) for n in surface_nodes if n.get('parent')=='LayerEntrances' and n.get('type')=='Area2D'}
captures={}
for folder,pattern in [('maps/fundo_ferro','preview_fundo_*.png'),('maps/sucateia','preview_fundo_surface_*.png')]:
    for path in (root/folder).glob(pattern):
        captures[str(path.relative_to(root)).replace('\\','/')]=dict(sha256=digest(path),modified_sao_paulo=datetime.fromtimestamp(path.stat().st_mtime,timezone(timedelta(hours=-3))).isoformat(),png_size_bytes=path.stat().st_size)
assets=re.findall(r'\[ext_resource type="Texture2D" path="res://([^\"]+)"',text)
report=dict(scope='static read-only; no fresh render/physics',underground_sha256=digest(underground),surface_sha256=digest(surface),underground_equals_pre_finish_checkpoint=underground.read_bytes()==(root/'tools/checkpoints/fundo_before_functional_finish.tscn').read_bytes(),serialized_nodes=len(nodes),rooms=rooms,routes=routes,underground_F=accesses,surface_F=surface_accesses,bridges=[dict(center=[1820,2100],painted_canvas=[97,139],tested_span=[[1820,2025],[1820,2170]]),dict(center=[2660,1127],painted_canvas=[97,148],tested_span=[[2660,1030],[2660,1220]])],blocked_machines={n['name']:vector(n['body'],'metadata/blocked_base') for n in nodes if 'metadata/blocked_base' in n['body']},wall_sprite_count=sum(n.get('parent')=='Structures/Walls' and n.get('type')=='Sprite2D' for n in nodes),textures={name:digest(root/name) for name in assets},captures=captures,runtime_hashes={str(p.relative_to(root)).replace('\\','/'):digest(p) for p in (root/'scripts').rglob('*.gd')},pending_finish_applied='[node name="FunctionalGroundFinish"' in text)
assert len(rooms)==7 and len(routes)==8 and len(accesses)==3 and report['underground_equals_pre_finish_checkpoint'] and not report['pending_finish_applied']
(root/'tools/fundo_finish_baseline_evidence.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print('READ-ONLY BASELINE:7 rooms,8 saved routes,2 known bridges,3 paired F accesses;',report['wall_sprite_count'],'repeated wall sprites; checkpoint identical; pending finish absent')
print('underground SHA256',report['underground_sha256'])
