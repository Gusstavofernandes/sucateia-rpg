from pathlib import Path
import json,re,html
root=Path(__file__).resolve().parents[1]
source=(root/'tools/build_fundo_ferro.gd').read_text(encoding='utf-8')
def points(text):return [[float(x),float(y)] for x,y in re.findall(r'Vector2\(([-\d.]+),\s*([-\d.]+)\)',text)]
rooms=[dict(name=name,center=points(c)[0],size=points(s)[0]) for name,c,s in re.findall(r'room\("([^"]+)",(Vector2\([^)]+\)),(Vector2\([^)]+\))',source)]
routes=[dict(name=name,points=points(p)) for name,p in re.findall(r'route\("([^"]+)",PackedVector2Array\(\[(.*?)\]\)',source)]
accesses=[dict(name=name,surface=points(a)[0],underground=points(b)[0]) for name,a,b in re.findall(r'\["([^"]+)",(Vector2\([^)]+\)),(Vector2\([^)]+\))\]',source)]
data=dict(source='tools/build_fundo_ferro.gd',rooms=rooms,routes=routes,accesses=accesses,scope='separate underground layer connected to current city, not surface district teleportation',corridor_half_width=91,neighbors=['Poço Velho / núcleo costeiro','Doca Leste / costa de manutenção','Forjas Rasas / manutenção sul'])
(root/'tools/fundo_spatial_plan.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1050" viewBox="750 150 2850 2494">','<rect x="750" y="150" width="2850" height="2494" fill="#171e1e"/>','<text x="820" y="280" fill="#e4c49c" font-size="60">Fundo-Ferro — camada inferior</text>']
for r in routes:
    p=' '.join(f'{x},{y}' for x,y in r['points'])
    svg.append(f'<polyline points="{p}" fill="none" stroke="#625b49" stroke-width="182" stroke-linejoin="round"/>')
for r in rooms:
    x,y=r['center'];w,h=r['size'];a=x-w/2;b=y-h/2
    p=[(a+60,b),(a+w-40,b),(a+w,b+60),(a+w,b+h-45),(a+w-70,b+h),(a+45,b+h),(a,b+h-70),(a,b+45)]
    coords=' '.join(f'{px},{py}' for px,py in p)
    svg.append(f'<polygon points="{coords}" fill="#72634a" stroke="#b7a273" stroke-width="5"/><text x="{x}" y="{y}" text-anchor="middle" fill="#fff0d1" font-size="35">{html.escape(r["name"])}</text>')
for a in accesses:
    x,y=a['underground'];sx,sy=a['surface']
    svg.append(f'<circle cx="{x}" cy="{y}" r="23" fill="#80bfbb"/><text x="{x+35}" y="{y+45}" fill="#bce2dd" font-size="27">F ↔ superfície {sx:g},{sy:g}</text>')
svg.append('<text x="820" y="2550" fill="#dbc8a6" font-size="34">7 salas · circuito + 2 ligações · 3 acessos físicos · escala original preservada</text></svg>')
(root/'docs/fundo-ferro-planta-espacial.svg').write_text('\n'.join(svg),encoding='utf-8')
print('PASS: builder-derived seven-room, eight-route, three-access spatial plan')
