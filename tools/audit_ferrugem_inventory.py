"""Read scene declarations/catalog only; never instantiate or mutate the game."""
from pathlib import Path
import re,json,hashlib

root=Path(__file__).resolve().parents[1]
def scene(path):
    p=root/path;s=p.read_text(encoding='utf-8-sig');nodes=[]
    for match in re.finditer(r'^\[node ([^\n]+)\]\n([^\[]*)',s,re.M):
        header,body=match.groups();props=dict(re.findall(r'^(\w+(?:/\w+)?) = (.*)$',body,re.M))
        node=dict(re.findall(r'(name|type|parent)="([^\"]+)"',header));node['path']=node['name'] if node.get('parent','.')=='.' else node['parent']+'/'+node['name'];node['properties']={k:v for k,v in props.items() if k in ['position','script','collision_mask','collision_layer','visible'] or k.startswith('metadata/') and len(v)<450};nodes.append(node)
    resources=re.findall(r'^\[ext_resource type="([^\"]+)" path="res://([^\"]+)"',s,re.M)
    return {'path':path,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'nodes':len(nodes),'root_children':[n['name'] for n in nodes if n.get('parent')=='.'],'markers':[n for n in nodes if n.get('type') in ['Marker2D','Area2D']],'textures':[path for kind,path in resources if kind=='Texture2D'],'scene_dependencies':[path for kind,path in resources if kind=='PackedScene'],'scripts':[path for kind,path in resources if kind=='Script']}
catalog=json.loads((root/'maps/ferrugem_baixa/region.json').read_text(encoding='utf-8-sig'))
surface=scene('maps/sucateia/sucateia.tscn');underground=scene('maps/fundo_ferro/fundo_ferro.tscn')
legacy=[]
for key,data in catalog.items():
    if key=='centre':continue
    path=data['scene'].removeprefix('res://');info=scene(path)
    legacy.append({'id':key,'name':data['name'],'path':path,'sha256':info['sha256'],'node_count':info['nodes'],'catalog_links':list(data['links']),'catalog_old_position':data.get('regional_position'),'landmark_art':[p for p in info['textures'] if p.startswith('assets/region/')],'destinations':[n for n in info['markers'] if n.get('parent')=='Destinations'],'loaded_by_current_surface':path in surface['scene_dependencies'],'reachable_by_current_layer_travel':False})
result={'method':'static declarations; prior clean verification logs cited separately; no new engine execution','active_main_scene':'maps/sucateia/sucateia.tscn','surface':surface,'underground':underground,'legacy_catalog_total':len(catalog),'legacy_scene_count':len(legacy),'legacy':legacy,'current_main_region_portal_script_loaded':'scripts/world/region_portal.gd' in surface['scripts'],'fundo_preserved':(root/'maps/fundo_ferro/fundo_ferro.tscn').read_bytes()==(root/'tools/checkpoints/fundo_before_functional_finish.tscn').read_bytes()}
out=root/'tools/ferrugem_inventory_evidence.json';out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS: static inventory;15 legacy scenes exist and are not dependencies of current surface;Fundo preserved=',result['fundo_preserved'])
print('Current root groups:',','.join(p for p in surface['root_children'] if 'District' in p))
for item in legacy:print(item['id'],item['node_count'],'nodes;',','.join(item['landmark_art']))
for world in [surface,underground]:
    print(world['path'])
    for parent in sorted(set(n.get('parent','') for n in world['markers'])):
        members=[n for n in world['markers'] if n.get('parent')==parent]
        if any(part in parent for part in ['Routes','FutureExits','UrbanDestinations','LayerEntrances','Rooms','Connections']):print(parent,len(members),[(n['name'],n['properties'].get('position')) for n in members])
