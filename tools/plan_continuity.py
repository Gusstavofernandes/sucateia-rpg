from pathlib import Path
import json,math
root=Path(__file__).resolve().parents[1]
path=root/'maps/ferrugem_baixa/region.json'
data=json.loads(path.read_text(encoding='utf-8'))
positions={'centre':[0,0],'alto':[0,-1],'forjas':[1,-.3],'cabos':[1,.7],'fundo':[0,.7],'docas':[1,1.5],'coroa':[.7,-1.7],'grande':[2,-.1],'chamines':[1.5,-1.9],'via_cais':[1.7,1.8],'banco':[2.5,2],'engrenopolis':[2.5,1],'via_engrenagens':[2.7,.3],'eng_nucleo':[2.5,.4],'eng_corredor':[3.4,.7],'galeria':[0,.7]}
functions={'centre':'comércio e distribuição das rotas de Sucateia','alto':'moradia em camadas e ligação às oficinas','forjas':'produção e alimentação industrial','cabos':'circulação suspensa entre níveis','fundo':'drenagem e serviços inferiores','docas':'expedição de carga e costa','coroa':'marco de poder e orientação urbana','grande':'recuperação de máquinas e suprimento de sucata','chamines':'usina e limite industrial norte','galeria':'manutenção das bombas do Poço Velho','via_cais':'circulação e amarras junto à água','banco':'recuperação de cascos e atracação','engrenopolis':'montagem e distribuição de transmissões','via_engrenagens':'transporte entre sucata e oficinas','eng_nucleo':'moradias e oficinas de artífices','eng_corredor':'pressão, montagem e circulação industrial'}
assets={'coroa':'region/crown.png','chamines':'region/chimney_bank.png','forjas':'region/foundry.png','cabos':'region/cable_tower.png','grande':'region/scrap_colossus.png','engrenopolis':'region/gearworks.png','banco':'region/wreck_cradle.png','docas':'region/dock_warehouse.png','alto':'region/tenement.png'}
def normalise(v):
    l=math.hypot(*v);return [v[0]/l,v[1]/l] if l else [0,1]
def family(a,b):
    styles={data[a].get('style','market'),data[b].get('style','market')}
    if {a,b}=={'fundo','galeria'}: return 'vertical'
    if 'suspended' in styles:return 'cable'
    if styles & {'undercity','gallery','forge','ruins'}:return 'pipe'
    if styles & {'harbor','coastal_path','wreck_bank'}:return 'coast'
    if styles & {'salvage','freight_path'}:return 'haul'
    return 'street'
features={'vertical':['escotilha','tubulações','drenagem'],'cable':['passarela','cabos','correntes'],'pipe':['tubulação','suportes','desgaste industrial'],'coast':['costa','contenção','amarras'],'haul':['trilha de carga','placas','remendos'],'street':['rua gasta','cabos','anexos']}
for id,cfg in data.items():
    cfg['function']=functions[id];cfg['regional_position']=positions[id]
    previous=cfg.get('continuity',{});cfg['continuity']={};chosen=[]
    outline=cfg.get('outline',[])
    centre=[sum(p[0] for p in outline)/len(outline),sum(p[1] for p in outline)/len(outline)] if outline else [1200,900]
    for dest,portal in cfg['links'].items():
        heading=normalise([positions[dest][0]-positions[id][0],positions[dest][1]-positions[id][1]])
        fam=family(id,dest);join=previous.get(dest,{}).get('join',portal[:])
        border=dict(shared_id='--'.join(sorted([id,dest])),family=fam,features=features[fam],join=join,heading=heading,transition=functions[id]+' → '+functions[dest],view_asset=assets.get(dest,'generated/structures/skyline.png'))
        if id=='centre' or fam=='vertical':
            border.update(anchor=portal[:],direction=heading,opening=False)
        else:
            candidates=[]
            for i,a in enumerate(outline):
                end=outline[(i+1)%len(outline)];delta=[end[0]-a[0],end[1]-a[1]];length=math.hypot(*delta)
                direction=normalise([delta[1],-delta[0]])
                for j in range(1,max(2,int(length/24))):
                    t=j/max(2,int(length/24));at=[a[0]+delta[0]*t,a[1]+delta[1]*t]
                    if any(math.dist(at,p)<215 for p in chosen):continue
                    gate=[at[0]-direction[0]*66,at[1]-direction[1]*66]
                    if any(abs(gate[0]-b[1])<b[3]*.325+35 and b[2]-min(118,b[4]*.24)-35<gate[1]<b[2]+35 for b in cfg.get('buildings',[])):continue
                    radial=normalise([at[0]-centre[0],at[1]-centre[1]])
                    score=sum(radial[k]*heading[k] for k in [0,1])*4-math.dist(at,join)*.0007
                    candidates.append((score,at,direction,gate))
            if not candidates:raise ValueError('No viable border '+id+' '+dest)
            _,at,direction,gate=max(candidates,key=lambda c:c[0]);chosen.append(at)
            border.update(anchor=[round(v,2) for v in at],direction=direction,opening=True)
            cfg['links'][dest]=[round(v,2) for v in gate]
        cfg['continuity'][dest]=border
path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# Ferrugem Baixa — contratos de continuidade','Cada cena é um recorte. Posições regionais são esquema de composição, não coordenadas métricas do mundo.','']
for id,c in data.items():
    lines += ['## '+c['name'],'Função: '+c['function']+'.','| Vizinho | Atravessa a fronteira | Referência distante | Transição |','|---|---|---|---|']
    for d,b in c['continuity'].items():lines.append('| '+data[d]['name']+' | '+', '.join(b['features'])+' | '+b['view_asset']+' | '+b['transition']+' |')
    lines.append('')
(root/'tools/FERRUGEM_CONTINUITY.md').write_text('\n'.join(lines),encoding='utf-8')
print('Planned',len(data),'sectors and',sum(len(c['links']) for c in data.values()),'directed borders')
