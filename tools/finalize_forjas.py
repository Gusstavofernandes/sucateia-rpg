from pathlib import Path
import json, re, hashlib, zipfile
root=Path(__file__).resolve().parents[1]
scene=root/'maps/sucateia/sucateia.tscn'
source=scene.read_text(encoding='utf-8')
assert 'LayerEntrances' not in source,'Historical Forjas checkpoint must not be recreated after the underground stage'
previous=(root/'tools/checkpoints/sucateia_before_forjas.tscn').read_text(encoding='utf-8')
def tile_data(text,name):
    block=next(b for b in text.split('[node ') if b.startswith(f'name="{name}"'))
    return re.search(r'tile_map_data = PackedByteArray\("([^"]+)"\)',block).group(1)
for name in ['MarketFloor','AltoFloor','TerraceFloor']:assert tile_data(source,name)==tile_data(previous,name),name
for name,digest in json.loads((root/'tools/approved_art_hashes.json').read_text(encoding='utf-8')).items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
tests=['test_forjas_render_order','test_forjas_rasas','test_forjas_preservation','test_alto_lixo','test_alto_refinement','test_lower_coast','test_market_expansion','test_slice']
modes=['forjas_district','forjas_full','forjas_frontier','forjas_foundry','forjas_recycling','forjas_drain']
for name in tests:
    text=(root/'tools'/f'forjas_{name}.log').read_text(encoding='utf-8-sig')
    assert 'PASS:' in text and 'ERROR:' not in text,name
for mode in modes:
    text=(root/'tools'/f'capture_{mode}.log').read_text(encoding='utf-8-sig')
    assert '.png 0 ' in text and 'ERROR:' not in text,mode
    assert (root/'maps/sucateia'/f'preview_{mode}.png').stat().st_size>100000
assert 'ForjasIndustrialArchitecture' in source and 'ForjasStockAndService' in source
source=source.replace('built; pending current physical and visual validation','exterior first stage validated; external destinations reserved')
scene.write_text(source,encoding='utf-8')
plan=root/'docs/superpowers/plans/2026-10-02-forjas-rasas.md'
plan.write_text(plan.read_text(encoding='utf-8').replace('- [ ]','- [x]'),encoding='utf-8')
files=[scene,root/'project.godot',Path(__file__),root/'tools/checkpoints/sucateia_before_forjas.tscn',root/'tools/FORJAS_RASAS_AUDIT.md',root/'tools/approved_art_hashes.json',root/'tools/forjas_art_manifest.json',root/'tools/forjas_boiler_prompt.json',root/'tools/forjas_spatial_plan.json',root/'tools/draw_forjas_spatial_plan.py',root/'tools/build_forjas_rasas.gd',root/'tools/finish_forjas_depth.gd',root/'tools/run_forjas_checks.py',root/'tools/run_forjas_captures.py',root/'tools/RECONSTRUCTION_STATUS.md',root/'licenses/assets.md',plan,root/'docs/forjas-rasas-planta-espacial.svg',root/'docs/forjas-rasas-planta-espacial.png']
files+=[root/'tests'/f'{name}.gd' for name in tests]
files+=[root/'tools'/f'forjas_{name}.log' for name in tests]
files+=[root/'tools'/f'capture_{mode}.log' for mode in modes]
files+=[root/'maps/sucateia'/f'preview_{mode}.png' for mode in modes]
files+=list((root/'scripts').rglob('*.gd'))+list((root/'scenes').rglob('*.tscn'))
files+=[p for p in (root/'assets').rglob('*') if p.is_file() and 'source' not in p.parts and p.suffix in ['.png','.svg','.gdshader','.tres']]
output=root/'tools/checkpoints/sucateia_forjas_rasas_primeira_etapa.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(set(files)):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(output) as archive:assert archive.testzip() is None
(root/'tools/REGION_STATUS.md').write_text((root/'tools/RECONSTRUCTION_STATUS.md').read_text(encoding='utf-8'),encoding='utf-8')
print('PASS: eight tests, six captures, three preserved floor hashes, five protected PNG hashes, checkpoint CRC verified')
print(output,output.stat().st_size,'bytes')
