from pathlib import Path
import json,shutil
import sys
root=Path(__file__).resolve().parents[1]
path=root/'maps/ferrugem_baixa/region.json'
if 'eng_nucleo' in json.loads(path.read_text(encoding='utf-8')):
    print('Refinement already applied; no duplicate buildings added')
    sys.exit(0)
shutil.copy2(path,root/'tools/checkpoints/region_before_density.json.bak')
data=json.loads(path.read_text(encoding='utf-8'))
data['engrenopolis']['links'].update(eng_nucleo=[770,355],eng_corredor=[1750,860])
data['engrenopolis']['buildings'] += [['cargo_depot',610,395,320,230],['machine_lane',1135,1100,270,200]]
data['engrenopolis']['markers']={'Montagem':[1200,1120],'Oficinas':[585,775]}
outline=[[144,288],[480,192],[960,144],[1344,192],[1728,288],[1920,624],[1824,960],[1872,1296],[1488,1344],[1056,1248],[672,1344],[240,1296],[96,864]]
def new(key,name,style,links,buildings,spawn,landmark,outline,markers):
    data[key]=dict(name=name,scene=f'res://maps/ferrugem_baixa/{key}.tscn',links=links,style=style,buildings=buildings,spawn=spawn,landmark=landmark,outline=outline,tint='#9a947c',markers=markers)
new('eng_nucleo','Engrenópolis — Vielas dos Artífices','precision',
    {'engrenopolis':[1000,1170],'eng_corredor':[1720,890]},
    [['tenement',410,565,330,330],['house_stack',740,580,235,235],['house',1150,520,265,265],['tenement',1560,555,330,330],
     ['house',300,960,250,250],['house_stack',610,935,260,260],['machine_lane',950,875,345,245],['workshop',1450,1005,330,270],
     ['house',450,1200,245,245],['cargo_depot',750,1200,285,215],['house_stack',1270,1195,235,235],
     ['house_stack',665,345,240,240],['cargo_depot',1160,335,275,190],['house',1770,1120,210,210]],
    [1000,1230],[1040,950],outline,{'PatioDosArtifices':[920,690],'BecoDasOficinas':[1260,910],'RuaDosMoradores':[490,660]})
corridor=[[192,912],[432,768],[720,768],[816,528],[1104,384],[1440,384],[1632,240],[1872,288],[1920,576],[1728,816],[1536,816],[1344,1056],[1056,1056],[864,1248],[528,1248],[192,1200]]
new('eng_corredor','Engrenópolis — Corredor das Caldeiras','precision',
    {'engrenopolis':[330,1060],'eng_nucleo':[1715,490]},
    [['gearworks',1270,640,450,320],['machine_lane',690,1030,325,225],['cargo_depot',1170,925,320,225],
     ['pump_station',1630,765,255,220],['workshop',850,740,290,245],['house_stack',445,1040,235,235]],
    [330,1120],[1230,1010],corridor,{'CargaDeTransmissoes':[1060,1020],'EstacaoDePressao':[1570,785]})
data['banco']['buildings'][0]=['wreck_cradle',1180,800,610,400]
data['banco']['buildings'] += [['cargo_depot',610,1080,350,235],['machine_lane',1570,1155,280,205],['wreck_cradle',1030,1230,340,220]]
data['banco']['markers']={'RecuperacaoDeCascos':[1200,925],'Depositos':[620,1150],'Atracacao':[1550,525]}
data['docas']['buildings'] += [['cargo_depot',695,425,305,210],['machine_lane',1430,460,320,225],['cargo_depot',1110,990,270,195]]
data['docas']['markers']={'TriagemDeCarga':[750,670],'Manutencao':[1410,550]}
data['fundo']['buildings'] += [['pump_station',530,535,290,225],['cargo_depot',1570,550,265,185]]
data['fundo']['markers']={'ColetorExterior':[470,750],'PatioDeValvulas':[1470,640]}
path.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
print(len(data),'maps',sum(len(c['links']) for c in data.values()),'connections')
