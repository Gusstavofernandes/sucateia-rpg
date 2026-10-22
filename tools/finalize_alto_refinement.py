from pathlib import Path
import json, re, hashlib, zipfile
root=Path(__file__).resolve().parents[1]
scene=root/'maps/sucateia/sucateia.tscn'
source=scene.read_text(encoding='utf-8')
previous=(root/'tools/checkpoints/sucateia_before_alto_refinement.tscn').read_text(encoding='utf-8')
def tile_data(text,name):
    block=next(b for b in text.split('[node ') if b.startswith(f'name="{name}"'))
    return re.search(r'tile_map_data = PackedByteArray\("([^"]+)"\)',block).group(1)
for name in ['MarketFloor','AltoFloor','TerraceFloor']:assert tile_data(source,name)==tile_data(previous,name),name
approved=json.loads((root/'tools/approved_art_hashes.json').read_text(encoding='utf-8'))
for name,digest in approved.items():assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
logs=['test_alto_lixo.log','test_alto_refinement.log','alto_finish_coast_test.log','alto_finish_market_test.log','alto_finish_original_test.log','alto_refinement_build.log','capture_alto_full.log','capture_alto_court.log','capture_alto_frontier.log','capture_alto_northwest.log']
for name in logs:
    text=(root/'tools'/name).read_text(encoding='utf-8-sig')
    assert 'ERROR:' not in text and 'SCRIPT ERROR' not in text,name
    if 'test' in name:assert 'PASS:' in text,name
    if 'capture' in name:assert 'CAPTURE ' in text and '.png 0 ' in text,name
assert 'ResidentialFinish' in source and 'LowerCoastReworked' in source
source=source.replace('residential finishing built; pending current physical/visual validation','residential finishing stage validated; external areas reserved')
scene.write_text(source,encoding='utf-8')
paths=[scene,root/'project.godot',Path(__file__),root/'tools/refine_alto_lixo.gd',root/'tools/checkpoints/sucateia_before_alto_refinement.tscn',root/'tools/approved_art_hashes.json',root/'tools/alto_landing_prompt.json',root/'tools/alto_art_manifest.json',root/'tools/alto_lixo_spatial_plan.json',root/'tools/ALTO_RESIDENTIAL_AUDIT.md',root/'tools/RECONSTRUCTION_STATUS.md',root/'tools/LOWER_COAST_AUDIT.md',root/'licenses/assets.md',root/'docs/superpowers/plans/2026-10-02-alto-lixo-acabamento.md']
paths += [root/'tools'/name for name in logs]
paths += [root/'tests'/name for name in ['test_alto_lixo.gd','test_alto_refinement.gd','test_lower_coast.gd','test_market_expansion.gd','test_slice.gd']]
paths += [root/'maps/sucateia'/f'preview_{mode}.png' for mode in ['alto_full','alto_court','alto_frontier','alto_northwest','lower_coast']]
paths += list((root/'scripts').rglob('*.gd'))+list((root/'scenes').rglob('*.tscn'))
paths += list((root/'assets/reconstruction').glob('*.png'))+list((root/'assets/reconstruction').glob('*.gdshader'))
output=root/'tools/checkpoints/sucateia_alto_lixo_acabamento.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(set(paths)):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(output) as archive:assert archive.testzip() is None
(root/'tools/REGION_STATUS.md').write_text((root/'tools/RECONSTRUCTION_STATUS.md').read_text(encoding='utf-8'),encoding='utf-8')
print('PASS: five current tests, four final captures, three floor hashes and five protected PNGs unchanged; finishing checkpoint CRC verified')
