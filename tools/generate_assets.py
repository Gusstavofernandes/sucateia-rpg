from pathlib import Path
import random, math, zipfile
ROOT=Path(__file__).resolve().parents[1]
rng=random.Random(37)
def save(folder,name,w,h,body):
    p=ROOT/'assets'/folder/(name+'.svg')
    p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><defs><linearGradient id="wall" x2="20%" y2="100%"><stop stop-color="#706253"/><stop offset="1" stop-color="#302f2d"/></linearGradient><linearGradient id="roof" x2="70%" y2="100%"><stop stop-color="#94715a"/><stop offset="1" stop-color="#453c35"/></linearGradient><linearGradient id="iron" x2="100%" y2="100%"><stop stop-color="#596263"/><stop offset="1" stop-color="#252e31"/></linearGradient><radialGradient id="glow"><stop stop-color="#fff4c0" stop-opacity=".85"/><stop offset=".2" stop-color="#eea456" stop-opacity=".4"/><stop offset="1" stop-color="#eea456" stop-opacity="0"/></radialGradient></defs>{body}</svg>',encoding='utf8')
def rect(x,y,w,h,c,stroke='#20282a',sw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" stroke="{stroke}" stroke-width="{sw}"/>'
def line(x,y,x2,y2,c='#a68b69',sw=2):
    return f'<path d="M{x} {y} L{x2} {y2}" fill="none" stroke="{c}" stroke-width="{sw}"/>'
def poly(points,c,stroke='#20282a',sw=2):
    return f'<polygon points="{points}" fill="{c}" stroke="{stroke}" stroke-width="{sw}"/>'
def ellipse(x,y,rx,ry,c):
    opacity = int(c[7:9],16)/255 if len(c)==9 else 1
    c = c[:7]
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" fill-opacity="{opacity*.65}"/>'
def circle(x,y,r,c,stroke='none',sw=1):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{stroke}" stroke-width="{sw}"/>'
def rivets(x,y,w,h):
    return ''.join(circle(a,b,1.6,'#b39c79') for a,b in [(x+5,y+5),(x+w-5,y+5),(x+5,y+h-5),(x+w-5,y+h-5)])
def window(x,y,color='#ebb364'):
    s=rect(x,y,25,35,'#202b2c')+poly(f'{x+3},{y+32} {x+3},{y+11} {x+12},{y+3} {x+22},{y+11} {x+22},{y+32}',color,'#5b5143')
    return s+line(x+12,y+3,x+12,y+33,'#514331',3)+line(x+3,y+19,x+22,y+19,'#514331',3)+rect(x-3,y+34,31,5,'#766550')
# Terrain atlas: 4 materials x 4 deterministic variations, 48 px cells.
s=''
for row,base in enumerate(['#403e34','#645846','#4b5149','#383a35']):
    for col in range(4):
        x,y=col*48,row*48
        s+=rect(x,y,48,48,base,base,0)
        if row in (0,1):
            for j in range(3):
                for i in range(2):
                    px=x+i*25-(12 if j%2 else 0); py=y+j*17
                    s+=rect(px+1,py+1,23,15,['#595548','#625b4d','#504f44','#706351'][rng.randrange(4)],'#343b34',1)
                    s+=line(px+3,py+2,px+21,py+2,'#7d725b',.8)
        elif row==2:
            for j in range(0,48,8):
                s+=rect(x+1,y+j+1,46,6,'#565849','#313b35',1)
                s+=line(x+3,y+j+2,x+44,y+j+2,'#8d8263',1)
            s+=rivets(x,y,48,48)
        else:
            for j in range(8):
                s+=line(x+rng.randrange(48),y+rng.randrange(48),x+rng.randrange(48),y+rng.randrange(48),'#4c5044',1)
        for k in range(27):
            s+=circle(x+rng.randrange(48),y+rng.randrange(48),rng.choice([.4,.7,1]),rng.choice(['#aaa080','#292e2a','#817052']))
save('tiles','sucateia_atlas',192,192,s)
# Individually assembled modular buildings, textured patched roof, tall crooked upper storeys.
for variant in range(4):
    s=ellipse(159,298,132,20,'#121b1bd0')
    s+=poly('34,132 267,122 267,282 37,297','url(#wall)')
    s+=poly('267,122 290,100 290,263 267,282','#242d2d')
    for y in range(156,278,23):
        s+=line(37,y,266,y-10,'#3c3d37',2)
        for x in range(43,260,43): s+=line(x+(12 if y%2 else 0),y,x+(12 if y%2 else 0),y+22,'#48473f',1)
    s+=rect(43,218,40,66,'#4c4636')+rect(47,223,31,58,'#252e2b')
    for x in range(49,78,6): s+=line(x,225,x,280,'#615a43',1)
    s+=circle(72,253,2,'#dbb872')
    for x in (99,153,219): s+=window(x,221,['#f1b669','#75b4af','#ddae62','#9cb5a5'][variant])
    # asymmetric upper room and repaired roof
    s+=poly('27,135 139,58 285,105 267,179 42,191','url(#roof)')
    for j in range(5):
        for i in range(6):
            x=39+i*37+j*2;y=119+j*12-i*2
            s+=poly(f'{x},{y} {x+35},{y-3} {x+32},{y+12} {x-2},{y+15}',rng.choice(['#6b5140','#79634d','#486062','#8a6447','#565850']),'#373c36',1)
            s+=line(x+2,y+2,x+31,y-1,'#b08b61',.8)
    s+=poly('72,74 186,62 191,159 67,169','url(#wall)')
    for x in (89,143): s+=window(x,113,'#d7a365')
    s+=poly('64,79 118,27 192,59 191,96 65,107','url(#roof)')
    for x in range(77,186,14): s+=line(x,71,x-4,102,'#433f34',2)
    s+=poly('104,29 118,10 130,32','#716c56')
    s+=rect(227,60,20,69,'url(#iron)')+rect(222,56,30,10,'#8a6a4a')
    s+=line(38,195,269,182,'#b18c62',4)+line(36,199,269,186,'#2c3533',3)
    # bracing, signs, hanging lantern
    s+=line(39,198,39,291,'#8b7758',5)+line(266,185,266,278,'#8b7758',5)
    s+=line(266,198,215,278,'#6e6954',3)
    s+=rect(117,185,84,26,'#293e3c')+rivets(117,185,84,26)
    s+=f'<text x="159" y="203" text-anchor="middle" fill="#c6b795" font-size="12" font-family="serif">{["REMENDOS","FERRO &amp; FIO","PEÇAS VELHAS","CASA 07"][variant]}</text>'
    s+=line(82,173,82,207,'#292f28',2)+circle(82,215,26,'url(#glow)')+rect(76,207,12,19,'#e4ac57')
    # roof repairs, bolts and scratches
    for k in range(55):
        x=rng.randrange(50,258);y=rng.randrange(137,174)
        s+=line(x,y,x+rng.randrange(3,13),y-2,'#8c7859',.7)
    if variant == 2:
        s+=rect(253,164,39,93,'url(#iron)')+rect(248,157,48,14,'#8c7251')
        s+=window(261,180,'#87b2a1')
    if variant == 3:
        s+=rect(186,26,67,50,'url(#iron)')+ellipse(219,26,34,13,'#8c775a')
        for y in (38,62): s+=rect(181,y,76,6,'#ac8a5a')
        s+=line(249,66,249,150,'#887655',10)
    save('structures',f'house_{variant}',320,320,s)
# Workshop: furnace dominates a broad open frontage.
s=ellipse(202,337,175,23,'#101b1bd0')+poly('28,132 351,105 356,326 31,344','url(#wall)')
s+=poly('351,105 386,78 388,292 356,326','#253032')
s+=poly('21,140 158,51 387,79 360,177 32,205','url(#iron)')
for x in range(45,366,23): s+=line(x,137,x-7,195,'#788077',2)
for x in (66,295):
    s+=rect(x,12,28,145,'url(#iron)')+rect(x-6,16,40,13,'#887759')
    for y in (40,94): s+=rect(x-3,y,34,8,'#9b7252')
s+=rect(39,223,118,97,'#242927')+poly('45,318 45,249 93,223 151,249 151,317','#e8a455')
s+=poly('63,316 64,265 95,244 130,265 139,316','#ae512c')+poly('80,317 86,275 108,284 119,317','#ffd682')
for x in range(50,150,13): s+=line(x,252,x,318,'#38382d',4)
s+=rect(183,218,128,110,'#202a2b')+rect(191,272,115,14,'#a38b62')
for x in range(192,307,22): s+=rect(x,234,14,23,'#786d51')+circle(x+6,245,4,'#aac5b0')
s+=rect(161,187,159,27,'#48564d')+rivets(161,187,159,27)
s+='<text x="240" y="205" text-anchor="middle" fill="#ddd0a4" font-size="16" font-family="serif">FORJA DOS REMENDOS</text>'
s+=line(25,210,361,181,'#bc9565',5)
for x in (31,355): s+=line(x,206,x,329,'#8b795c',7)
s+=rect(324,210,16,113,'#8c7251')+line(332,220,375,220,'#8c7251',9)
s+=circle(333,266,18,'#344341','#a3936a',4)+circle(333,266,9,'#97d5cc')
save('structures','workshop',416,368,s)
# Local arcane pressure reactor, caged crystal and crooked gothic spire.
s=ellipse(129,272,109,22,'#10201ed0')+ellipse(127,250,90,29,'#4b4b3d')+rect(59,129,139,111,'url(#iron)')
s+=ellipse(128,239,70,23,'#565744')+ellipse(128,131,70,25,'#839081')
s+=poly('95,98 97,31 127,5 158,32 161,101','#5c695b')
s+=poly('111,112 105,58 127,22 148,61 140,117','#73d7d0','#c2e5c9',3)
for x in (82,105,151,174): s+=line(x,108,x,203,'#bc9664',5)
for y in (143,190,226): s+=rect(53,y,151,10,'#9f7b54')+rivets(53,y,151,10)
s+=rect(89,155,77,55,'#193b3e')
for x in range(99,161,14): s+=line(x,166,x,201,'#80c9bd',3)
s+=line(59,181,31,181,'#786e56',18)+line(31,181,31,247,'#786e56',18)
s+=line(194,168,219,168,'#786e56',18)+line(219,168,219,240,'#786e56',18)
s+=circle(128,223,13,'#273c3a','#b59c6a',4)+line(128,223,133,214,'#e1ba78',2)
s+=poly('111,8 127,-1 143,8 137,15 117,15','#ae9567')
save('structures','reactor',256,296,s)
for v in range(3):
    s=ellipse(101,132,93,14,'#0e1b1bcc')+rect(12,51,12,80,'#8a7251')+rect(168,47,10,82,'#8a7251')
    s+=poly('6,46 28,8 175,1 194,48 178,77 9,84', ['#7d6944','#627467','#946a4b'][v])
    for x in range(14,188,25): s+=poly(f'{x},44 {x+19},42 {x+18},75 {x},78',['#b6a176','#8b9d85','#b58c65'][v],'#4b5345',1)
    s+=rect(19,94,157,35,'#5c5741')+rect(16,92,165,9,'#b2a077')
    for k in range(9):
        x=25+k*16
        s+=circle(x,88,7,['#638e85','#ae9368','#626e62'][k%3],'#273633',2)
        if k%3==0:s+=line(x-5,80,x+5,94,'#d9b57f',2)
    s+=line(15,84,178,77,'#ccaf73',2)+rivets(19,97,157,29)
    save('props',f'stall_{v}',208,152,s)
s=ellipse(34,65,29,9,'#0f1a1bb0')+rect(9,13,49,48,'url(#roof)')
for y in range(17,60,9):s+=line(12,y,55,y,'#302f29',2)
s+=line(12,15,55,57,'#9b865e',5)+line(55,15,12,57,'#9b865e',5)+rivets(9,13,49,48)
save('props','crate',72,80,s)
s=ellipse(29,60,26,8,'#0e1a1bb0')+rect(8,16,41,39,'url(#iron)')+ellipse(28,17,21,9,'#8a7350')+ellipse(28,55,21,7,'#343d35')
for y in (25,45):s+=rect(6,y,46,5,'#a38255')
s+=circle(34,15,4,'#26352f')+line(14,29,14,44,'#ad8b60',2)
save('props','barrel',64,72,s)
s=''
for k in range(24):
    x=rng.randrange(12,145);y=rng.randrange(30,74)
    s+=poly(f'{x},{y} {x+20},{y-17} {x+29},{y+2} {x+8},{y+9}',rng.choice(['#5c5e50','#86674a','#3d524c','#756647']),'#293b34',1)
    s+=rivets(x,y-7,17,12)
save('props','scrap',184,100,s)
s=rect(0,0,96,72,'#222f2a')
for y in range(6,66,12):s+=rect(3,y,90,10,'#7a7055')+line(5,y,90,y,'#b4a07b',2)
for x in (5,88):s+=rect(x,0,4,72,'#474e43')
save('props','bridge_segment',96,72,s)
s=rect(0,0,144,96,'#333b33')
for y in range(0,96,12):s+=rect(0,y,144,10,'#6e6b55')+line(2,y,141,y,'#bbab84',2)
s+=rect(0,0,8,96,'#5c5f4c')+rect(136,0,8,96,'#5c5f4c')
save('props','stairs',144,96,s)
# Simple testing goblin, designed only for scale/readability.
s=ellipse(24,46,16,6,'#102421a0')+rect(16,29,6,15,'#2e3431')+rect(27,29,6,15,'#2e3431')
s+=poly('15,18 30,16 37,33 14,34','#766846')+poly('8,11 19,14 16,24','#839668')+poly('31,15 44,9 35,24','#839668')
s+=ellipse(25,19,12,11,'#8b9a69')+poly('12,15 14,6 20,9 24,2 29,7 38,6 36,17','#a54f35')+circle(21,21,2,'#efe4b0')+circle(31,21,2,'#efe4b0')
s+=rect(13,27,4,9,'#a2946b')+rect(33,27,4,9,'#a2946b')
save('props','test_goblin',48,56,s)
# Radial light texture / original, soft round alpha.
save('fx','light',256,256,'<defs><radialGradient id="l"><stop stop-color="white" stop-opacity=".75"/><stop offset=".18" stop-color="white" stop-opacity=".5"/><stop offset=".5" stop-color="white" stop-opacity=".16"/><stop offset="1" stop-color="white" stop-opacity="0"/></radialGradient></defs><circle cx="128" cy="128" r="128" fill="url(#l)"/>')
z=zipfile.ZipFile(ROOT/'tools/particle-pack.zip')
for name in ['smoke_01.png','spark_01.png']:
    matches=[n for n in z.namelist() if n.endswith('/'+name) and n.startswith('PNG (Transparent)')]
    if matches:(ROOT/'assets/fx'/name).write_bytes(z.read(matches[0]))
for n in z.namelist():
    if 'license' in n.lower() and not n.endswith('/'):
        (ROOT/'licenses/Kenney-CC0.txt').write_bytes(z.read(n)); break
(ROOT/'licenses/assets.md').write_text('''| Asset | Origem / Autor | Licença | Uso |
|---|---|---|---|
| Particle Pack | Kenney — https://kenney.nl/assets/particle-pack | CC0 1.0 — https://creativecommons.org/publicdomain/zero/1.0/ | smoke_01.png, spark_01.png |
| Módulos SVG, atlas, máscara de luz | Originais deste projeto; gerados por tools/generate_assets.py | Sem dependências externas | Ambiente de Sucateia |
| ispirações/ | Referências fornecidas pelo usuário | Não redistribuídas como assets | Direção visual somente |
''',encoding='utf8')
print('Módulos SVG e partículas preparados')
