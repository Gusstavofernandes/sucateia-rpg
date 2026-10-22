from pathlib import Path
import json,hashlib,zipfile,re
root=Path(__file__).resolve().parents[1]
scene=root/'maps/sucateia/sucateia.tscn'
source=scene.read_text(encoding='utf-8')
approved=json.loads((root/'tools/approved_art_hashes.json').read_text(encoding='utf-8'))
for name,digest in approved.items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
logs=['original_rebuild_test.log','reconstruction_market_test.log','test_market_expansion.log','capture_market_full.log','capture_market_plaza.log']
for log in logs:
    text=(root/'tools'/log).read_text(encoding='utf-8-sig')
    assert 'ERROR:' not in text and 'SCRIPT ERROR' not in text,log
    assert ('PASS:' if 'test' in log else 'CAPTURE ') in text,log
assert 'RegionalSectors' not in scene.read_text(encoding='utf-8')
baseline=json.loads((root/'tools/checkpoints/market_ground_before_urban.json').read_text(encoding='utf-8'))
block=next(b for b in source.split('[node ') if b.startswith('name="MarketFloor"'))
encoded=re.search(r'tile_map_data = PackedByteArray\("([^"]+)"\)',block).group(1)
assert hashlib.sha256(encoded.encode()).hexdigest()==baseline['tile_map_sha256'],'Market terrain changed'
assert 'limit_top = '+str(baseline['camera_top']) in source,'Market extent changed'
paths=[scene,root/'project.godot',root/'tools/rebuild_original.gd',Path(__file__),root/'tools/RECONSTRUCTION_STATUS.md',root/'tools/market_reconstruction_art.json',root/'licenses/assets.md',root/'assets/reconstruction/market_salvage_cart.png',root/'tests/test_original_rebuild.gd',root/'tests/test_slice.gd',root/'tools/approved_art_hashes.json',root/'maps/sucateia/preview_market.png',root/'tools/checkpoints/original_visual_benchmark.png',root/'tools/checkpoints/sucateia_before_world_extension.tscn',root/'docs/superpowers/plans/2026-10-02-reconstrucao-original.md']
paths += [root/'tools'/log for log in logs]
paths += [root/'tests/test_market_expansion.gd',root/'tools/MARKET_URBAN_AUDIT.md',root/'tools/alto_lixo_spatial_plan.json',root/'tools/draw_alto_spatial_plan.py',root/'tools/render_alto_spatial_plan.cjs',root/'tools/checkpoints/market_ground_before_urban.json',root/'maps/sucateia/preview_market_full.png',root/'maps/sucateia/preview_market_plaza.png',root/'docs/alto-lixo-planta-espacial.svg',root/'docs/alto-lixo-planta-espacial.png',root/'docs/superpowers/plans/2026-10-02-mercado-estrutura-urbana.md',root/'docs/superpowers/plans/2026-10-02-mercado-dimensionamento.md',root/'docs/superpowers/plans/2026-10-02-alto-lixo-oeste.md']
paths += list((root/'assets/reconstruction').glob('*.png'))+list((root/'assets/reconstruction').glob('*.gdshader'))
paths += list((root/'scripts').rglob('*.gd'))+list((root/'scenes').rglob('*.tscn'))
checkpoint=root/'tools/checkpoints/mercado_original_reconstruido.zip'
with zipfile.ZipFile(checkpoint,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(set(paths)):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(checkpoint) as archive:assert archive.testzip() is None
(root/'tools/REGION_STATUS.md').write_text((root/'tools/RECONSTRUCTION_STATUS.md').read_text(encoding='utf-8'),encoding='utf-8')
print('PASS: three gameplay tests; eight destinations, three alleys; floor hash and camera extent preserved; five protected sprites unchanged; two captures; checkpoint CRC')
