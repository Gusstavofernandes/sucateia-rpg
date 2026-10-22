from pathlib import Path
import json,shutil
root=Path(__file__).resolve().parents[1]
path=root/'maps/ferrugem_baixa/region.json'
data=json.loads(path.read_text(encoding='utf-8'))
if 'caelporto' in data:
    print('North route already registered');raise SystemExit()
shutil.copy2(path,root/'tools/checkpoints/region_before_vhal.json.bak')
data['chamines']['links']['north_expedition']=[1700,400]
def sector(key,name,style,region,links,buildings,spawn,outline,markers):
    data[key]=dict(name=name,region=region,scene=f'res://maps/vhal_kor/{key}.tscn',links=links,style=style,buildings=buildings,spawn=spawn,outline=outline,markers=markers,landmark=list(markers.values())[0],tint='#a4adb0',floor_texture='vhal/stone_ground.png')
edge=[[144,864],[384,720],[624,720],[816,480],[1104,480],[1344,288],[1728,240],[1920,432],[1776,720],[1536,720],[1296,960],[960,960],[720,1248],[336,1296],[144,1152]]
sector('north_expedition','Expedição Norte — Limite de Ferrugem','vhal_edge','FERRUGEM BAIXA',
{'chamines':[290,1100],'river_route':[1690,410]},
[['cargo_depot',540,1110,330,240],['chimney_bank',585,775,270,300],['dock_warehouse',1100,785,385,255],['port_warehouse',1580,550,395,275]],
[290,1160],edge,{'Expedicao':[680,1120],'PostoDePassagem':[1450,645]})
data['north_expedition']['floor_texture']='region/salvage_ground.png'
river=[[144,864],[432,768],[576,624],[864,624],[1056,288],[1344,192],[1584,240],[1728,480],[1584,720],[1344,720],[1152,864],[912,912],[768,1152],[528,1296],[192,1200]]
sector('river_route','Rota Fluvial — Caminho dos Mercadores','vhal_river','TRANSIÇÃO NORTE',
{'north_expedition':[285,1080],'caelporto':[1460,390]},
[['port_warehouse',570,860,355,245],['gothic_block',1360,620,405,315]],
[285,1140],river,{'TravessiaFluvial':[1060,760],'PostoComercial':[880,820]})
port=[[192,240],[672,144],[1104,192],[1488,144],[1872,288],[1920,720],[1776,864],[1776,1248],[1536,1344],[1344,1248],[1344,1008],[1104,1008],[1104,1344],[912,1392],[768,1296],[768,1008],[576,1008],[576,1248],[336,1344],[192,1152],[144,624]]
sector('caelporto','Caelporto — Cais de Pedra','vhal_port','VHAL-KOR',
{'river_route':[300,1050],'vhal_lower':[1000,300],'twin_plaza':[1710,630]},
[['port_warehouse',515,770,500,350],['port_warehouse',1430,810,520,355],['gothic_block',510,480,515,390],['gothic_block',1500,490,520,395],['arcane_station',1120,760,280,280],['port_warehouse',985,1030,295,220]],
[300,1110],port,{'CaisDeCarga':[950,1200],'MercadoFluvial':[790,820],'ElevadorPortuario':[1190,880]})
city=[[96,288],[432,144],[960,192],[1392,144],[1872,288],[1968,720],[1872,1200],[1536,1344],[960,1296],[528,1392],[144,1200],[96,768]]
sector('vhal_lower','Vhal-Kor — Bairros Inferiores','vhal_city','VHAL-KOR',
{'caelporto':[1010,1210],'twin_plaza':[1730,890]},
[['gothic_block',400,540,520,385],['gothic_block',1080,455,510,385],['gothic_block',1650,580,470,360],
 ['gothic_block',435,900,520,395],['gothic_block',1210,855,520,390],['gothic_block',1600,1210,500,380],
 ['gothic_block',400,1210,495,375],['port_warehouse',760,1110,335,260],
 ['arcane_station',950,760,300,300],['arcane_station',1410,1140,245,245],
 ['port_warehouse',750,535,310,230],['gothic_block',1750,340,255,220]],
[1010,1265],city,{'RuaDasOficinas':[760,850],'ElevadorInferior':[960,915],'BecoDasPontes':[1400,640]})
plaza=[[192,240],[624,144],[1008,192],[1488,144],[1824,336],[1920,816],[1776,1200],[1488,1344],[1056,1296],[576,1344],[192,1152],[144,624]]
sector('twin_plaza','Vhal-Kor — Torres Gêmeas','vhal_towers','VHAL-KOR',
{'vhal_lower':[320,1110],'caelporto':[1720,1110]},
[['twin_towers',1030,930,885,980],['gothic_block',380,795,390,300],['gothic_block',1630,795,380,295],
 ['arcane_station',585,1110,285,285],['port_warehouse',1420,1110,320,235]],
[320,1170],plaza,{'TorresGemeas':[1030,1080],'PonteDasTorres':[1030,1020],'PatioArcano':[780,1190]})
path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(len(data),'maps;',sum(len(c['links']) for c in data.values()),'directed connections')
