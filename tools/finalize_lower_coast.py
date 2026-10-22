from pathlib import Path
import hashlib, json, re, zipfile

root=Path(__file__).resolve().parents[1]
scene=root/'maps/sucateia/sucateia.tscn'
current=scene.read_text(encoding='utf-8')
previous=(root/'tools/checkpoints/sucateia_before_lower_coast.tscn').read_text(encoding='utf-8')
approved=json.loads((root/'tools/approved_art_hashes.json').read_text(encoding='utf-8'))
for name,digest in approved.items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
def data(source,name):
    block=next(b for b in source.split('[node ') if b.startswith(f'name="{name}"'))
    return re.search(r'tile_map_data = PackedByteArray\("([^"]+)"\)',block).group(1)
for name in ['MarketFloor','AltoFloor']:
    assert data(current,name)==data(previous,name),name
baseline=json.loads((root/'tools/checkpoints/market_ground_before_urban.json').read_text(encoding='utf-8'))
assert hashlib.sha256(data(current,'MarketFloor').encode()).hexdigest()==baseline['tile_map_sha256']
assert '[node name="LowerCoastReworked"' in current
logs=['test_lower_coast.log','lower_coast_original_test.log','lower_coast_market_test.log','capture_lower_coast.log','capture_lower_detail.log','lower_coast_build.log']
for name in logs:
    text=(root/'tools'/name).read_text(encoding='utf-8-sig')
    assert 'ERROR:' not in text and 'SCRIPT ERROR' not in text,name
    if 'test' in name:assert 'PASS:' in text,name
    if 'capture' in name:assert 'CAPTURE ' in text and '.png 0 ' in text,name
paths=[scene,root/'project.godot',Path(__file__),root/'tools/rework_lower_coast.gd',root/'tools/checkpoints/sucateia_before_lower_coast.tscn',root/'tools/checkpoints/market_ground_before_urban.json',root/'tools/approved_art_hashes.json',root/'tools/RECONSTRUCTION_STATUS.md',root/'tools/LOWER_COAST_AUDIT.md',root/'docs/superpowers/plans/2026-10-02-costa-inferior.md',root/'licenses/assets.md',root/'maps/sucateia/preview_lower_coast.png',root/'maps/sucateia/preview_lower_detail.png',root/'tools/alto_lixo_spatial_plan.json',root/'tools/alto_art_manifest.json']
paths += [root/'tools'/name for name in logs]
paths += [root/'tests'/name for name in ['test_lower_coast.gd','test_slice.gd','test_market_expansion.gd']]
paths += list((root/'scripts').rglob('*.gd'))+list((root/'scenes').rglob('*.tscn'))
paths += list((root/'assets/reconstruction').glob('*.png'))+list((root/'assets/reconstruction').glob('*.gdshader'))
output=root/'tools/checkpoints/sucateia_costa_inferior_retrabalhada.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(set(paths)):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(output) as archive:assert archive.testzip() is None
(root/'tools/REGION_STATUS.md').write_text((root/'tools/RECONSTRUCTION_STATUS.md').read_text(encoding='utf-8'),encoding='utf-8')
print('PASS: three current gameplay tests, two final captures, five approved PNG hashes, MarketFloor/AltoFloor unchanged and recoverable checkpoint CRC')
