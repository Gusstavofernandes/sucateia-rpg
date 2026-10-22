import re, shutil, os

base = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone'
art = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b'
for s in ['industrial_bomba_succao.png', 'industrial_tubo_travessia.png', 'industrial_caldeira_leste.png', 'industrial_tubo_leste_parede.png', 'industrial_manifold_oeste.png', 'industrial_decantador_norte.png']:
    shutil.copy2(os.path.join(base, s), os.path.join(art, 'antes_' + s))

text = open(os.path.join(base, 'scenes', 'fundo_ferro_master.tscn'), encoding='utf-8').read()
ext = dict(re.findall(r'path="([^"]+)" id="([^"]+)"', text))
ext = {v: k for k, v in ext.items()}
for m in re.finditer(r'\[node name="([^"]+)" type="([^"]+)" parent="([^"]+)"\]([\s\S]*?)(?=\n\[|\Z)', text):
    name, typ, parent, body = m.groups()
    if 'RedeIndustrial' not in parent and name != 'RedeIndustrialMaquinas':
        continue
    pos = re.search(r'position = (Vector2\([^)]*\))', body)
    tex = re.search(r'texture = ExtResource\("([^"]+)"\)', body)
    print(f'{parent.split("/")[-1]:>24} | {name:<28} {typ:<20} {pos.group(1) if pos else "":<24} {os.path.basename(ext.get(tex.group(1), "")) if tex else ""}')
