from pathlib import Path
import json,re,html
root=Path(__file__).resolve().parents[1]
source=(root/'scripts/world/forjas_rasas_builder.gd').read_text(encoding='utf-8')
def points(text):return [[float(x),float(y)] for x,y in re.findall(r'Vector2\(([-\d.]+),\s*([-\d.]+)\)',text)]
outline=points(re.search(r'var outline := PackedVector2Array\(\[(.*?)\]\)',source).group(1))
routes=[dict(name=name,points=points(data),width=int(width)) for name,data,width in re.findall(r'add_route\("([^"]+)",PackedVector2Array\(\[(.*?)\]\),(\d+),routes\)',source)]
workshops=points(re.search(r'var points := \[(.*?)\]',source).group(1))
data=dict(source='scripts/world/forjas_rasas_builder.gd',boundary=outline,routes=routes,workshops=workshops,scope='continuous current city; exterior industrial first stage',neighbors={'west':'Mercado dos Restos built','north':'Chaminés Velhas reserved','east':'Grande Ferrugem reserved','south':'Fundo-Ferro service approach reserved'},reference='sobre.txt and Atlas Fantástico de Continentes Místicos.png; original playable-map benchmark')
(root/'tools/forjas_spatial_plan.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
def pairs(values):return ' '.join(f'{x},{y}' for x,y in values)
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1300" height="1050" viewBox="1350 -1970 2630 2390">','<rect x="1350" y="-1970" width="2630" height="2390" fill="#172022"/>','<text x="1400" y="-1870" fill="#efd6a8" font-size="55">Forjas Rasas — planta da implantação</text>','<path d="M1350,-1690 L1620,-1690 L1730,-600 L1670,330 L1350,330 Z" fill="#64543b" opacity=".55"/>','<text x="1380" y="-1600" fill="#e7ccb0" font-size="29">Mercado</text>',f'<polygon points="{pairs(outline)}" fill="#4b453c" stroke="#a57949" stroke-width="6"/>']
colors=['#dac283','#e0a463','#c5b29a','#ca8558','#899e8f','#b1a576','#6cbbbb','#70989b']
for route,color in zip(routes,colors):
    svg.append(f'<polyline points="{pairs(route["points"])}" fill="none" stroke="{color}" opacity=".67" stroke-width="{route["width"]}" stroke-linejoin="round"/>')
for x,y in workshops:svg.append(f'<rect x="{x-124}" y="{y-112}" width="248" height="137" rx="12" fill="#69573e" stroke="#c59863" stroke-width="3"/>')
drain=points(re.search(r'var drain := PackedVector2Array\(\[(.*?)\]\)',source).group(1))
svg.append(f'<polyline points="{pairs(drain)}" fill="none" stroke="#101f20" stroke-width="66"/>')
for x in [2620,3280]:svg.append(f'<rect x="{x-38}" y="75" width="76" height="185" fill="#a48154"/>')
for x,y,label in [(2150,-340,'Reparos'),(2470,-120,'Carga'),(2800,-610,'Fabricação'),(2700,-800,'Fundição'),(3270,-600,'Reciclagem')]:
    svg.append(f'<circle cx="{x}" cy="{y}" r="17" fill="#eed7a0"/><text x="{x-90}" y="{y+67}" fill="#ffecd0" font-size="34">{label}</text>')
for x,y,label in [(3100,-1550,'Chaminés (reservado)'),(3650,-760,'Grande Ferrugem'),(3000,260,'Manutenção / Fundo-Ferro')]:
    svg.append(f'<circle cx="{x}" cy="{y}" r="32" fill="none" stroke="#a9cac5" stroke-width="5" stroke-dasharray="9 6"/><text x="{x-170}" y="{y-53}" fill="#bbd7d0" font-size="29">{label}</text>')
svg.append('<text x="1450" y="385" fill="#cfba99" font-size="30">Mesma cena · escala 48 unidades/tile · saídas externas ainda reservadas</text></svg>')
(root/'docs/forjas-rasas-planta-espacial.svg').write_text('\n'.join(svg),encoding='utf-8')
print('Saved current builder-derived spatial JSON and SVG')
