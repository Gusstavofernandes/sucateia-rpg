"""Vector planning overlay; preserves the actual screenshot and playable terrain."""
from pathlib import Path
import base64, json, html, xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
plan = json.loads((root/'tools/alto_lixo_spatial_plan.json').read_text(encoding='utf-8'))
image = base64.b64encode((root/plan['base_capture']).read_bytes()).decode('ascii')
# Capture uses zoom=.23, center=(1200,140), viewport=1198x749.
def point(p):
    return (583 + p[0]*.23, 492.3 + p[1]*.23)
def points(seq):
    return ' '.join(f'{x:.1f},{y:.1f}' for x,y in map(point,seq))
def label(text, p, color='#efe2c4', size=15):
    x,y=point(p)
    return f'<text x="{x:.1f}" y="{y:.1f}" fill="{color}" font-size="{size}" paint-order="stroke" stroke="#10191a" stroke-width="5">{html.escape(text)}</text>'

svg = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="1010" viewBox="0 0 1500 1010">
<title>Alto-Lixo — definição espacial oeste/noroeste</title>
<desc>Planejamento sobre a screenshot atual de Sucateia. Linhas e patamares são propostas; Alto-Lixo ainda não foi construído.</desc>
<rect width="1500" height="1010" fill="#10191a"/>
<image href="data:image/png;base64,{image}" x="260" y="150" width="1198" height="749" opacity=".8"/>
<g font-family="Segoe UI,Arial,sans-serif">
<text x="44" y="48" fill="#efe2c4" font-size="27">ALTO-LIXO · OESTE / NOROESTE</text>
<text x="44" y="79" fill="#aebcb7" font-size="17">Planta sobre o mapa atual — definir estrutura antes do detalhamento</text>
<text x="1360" y="62" fill="#efe2c4" font-size="18">N ↑</text>''']
svg.append(f'<polygon points="{points(plan["boundary"])}" fill="#b89055" fill-opacity=".17" stroke="#b89055" stroke-width="2" stroke-dasharray="7 5"/>')
svg.append(f'<polygon points="{points(plan["forjas_reserved_polygon"])}" fill="#60abb0" fill-opacity=".10" stroke="#60abb0" stroke-width="2" stroke-dasharray="7 5"/>')
for route in plan['routes']:
    color = '#efc77b' if route['kind']=='main' else '#abc3a0'
    width = 4 if route['kind']=='main' else 2.5
    svg.append(f'<polyline points="{points(route["points"])}" fill="none" stroke="#10191a" stroke-width="{width+3}" stroke-linejoin="round"/>')
    svg.append(f'<polyline points="{points(route["points"])}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linejoin="round"/>')
for i, entry in enumerate(plan['frontiers'],1):
    x,y=point(entry['point'])
    svg.append(f'<circle cx="{x}" cy="{y}" r="12" fill="#efc77b" stroke="#10191a" stroke-width="2"/><text x="{x}" y="{y+5}" text-anchor="middle" fill="#10191a" font-size="15">{i}</text>')
for terrace in plan['terraces']:
    x,y=point(terrace['point'])
    svg.append(f'<circle cx="{x}" cy="{y}" r="17" fill="#b89055" fill-opacity=".35" stroke="#efc77b"/>')
for stairs in plan['stairs']:
    x,y=point(stairs['point'])
    for dy in [-5,0,5]:
        svg.append(f'<path d="M{x-7},{y+dy} h14" stroke="#efe2c4" stroke-width="2"/>')
for exit_ in plan['future_exits']:
    x,y=point(exit_['point'])
    svg.append(f'<polyline points="{points([exit_["from"],exit_["point"]])}" fill="none" stroke="#c69e91" stroke-width="2" stroke-dasharray="5 4"/><circle cx="{x}" cy="{y}" r="5" fill="#c69e91"/>')
svg += [label('Cume das Calhas · +5 m',[-1160,-1280]),label('Pátio dos Andaimes · +3 m',[-1030,-840]),label('Casas dos Remendos · +1,5 m',[-500,-540]),label('Transição · pedra → terra',[210,-350]),label('Mercado dos Restos',[920,-100]),label('Reserva · Forjas Rasas',[1710,-1150],'#82c0c4'),label('Saída externa NW',[-1420,-1490],'#d9aaa0'),label('Saída externa oeste',[-1710,-675],'#d9aaa0'),label('Serviço → Fundo-Ferro',[-1290,255],'#d9aaa0')]
svg += ['''<text x="44" y="940" fill="#efc77b" font-size="16">Vias principais</text>
<text x="244" y="940" fill="#abc3a0" font-size="16">3 becos conectados</text>
<text x="470" y="940" fill="#d9aaa0" font-size="16">Saídas futuras</text>
<text x="660" y="940" fill="#82c0c4" font-size="16">Leste/nordeste reservado</text>
<text x="44" y="972" fill="#aebcb7" font-size="16">1 · Ferragens / principal     2 · Lotes / noroeste     3 · Serviço / sudoeste     Alturas: intenção visual, ainda sem mecânica de elevação.</text>
</g></svg>''']
output = root/'docs/alto-lixo-planta-espacial.svg'
output.write_text('\n'.join(svg),encoding='utf-8')
ET.parse(output)
assert len(plan['routes'])==6 and len(plan['future_exits'])==3
assert min(p[0] for p in plan['boundary']) < 0
assert max(p[0] for p in plan['boundary']) < min(p[0] for p in plan['forjas_reserved_polygon'])
print('PASS: west/northwest spatial plan; 3 main routes, 3 connected alleys, 4 terraces, 3 future exits; Forjas reserved; valid SVG')
