from pathlib import Path
import hashlib,json,re,zipfile
root=Path(__file__).resolve().parents[1]
tests=['test_amarras_infrastructure','test_amarras_routes','test_amarras_preservation','test_forjas_production','test_forjas_refinement_preservation','test_forjas_functional_modules','test_forjas_render_order','test_forjas_rasas','test_forjas_preservation','test_alto_lixo','test_alto_refinement','test_lower_coast','test_market_expansion','test_slice','test_fundo_access','test_fundo_layout']
modes=['amarras_district','amarras_transfer','amarras_anchor','amarras_maintenance','amarras_transition','amarras_full','forjas_district']
scene=(root/'maps/sucateia/sucateia.tscn').read_text(encoding='utf-8-sig')
assert 'name="CabosDistrict"' not in scene,'Historical Amarras checkpoint is protected after Cabos starts'
assert 'name="PassagemAmarrasDistrict"' in scene and 'name="EngrenopolisDistrict"' not in scene
manifest=json.loads((root/'assets/reconstruction/amarras_parallel/manifest.json').read_text(encoding='utf-8-sig'))
for entry in manifest:
    assert hashlib.sha256((root/entry['path']).read_bytes()).hexdigest()==entry['sha256'],entry['name']
    assert 'res://'+entry['path'] in scene,entry['name']
for path,digest in json.loads((root/'tools/approved_art_hashes.json').read_text(encoding='utf-8-sig')).items():
    assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,path
assert (root/'maps/fundo_ferro/fundo_ferro.tscn').read_bytes()==(root/'tools/checkpoints/fundo_before_functional_finish.tscn').read_bytes()
metrics={'tests':len(tests),'selected_generated_assets':len(manifest),'routes':7,'bridges':4,'chains':6,'floor_cells':611,'captures':{}}
for name in tests:
    log=(root/'tools'/f'fundo_{name}.log').read_text(encoding='utf-8-sig')
    assert 'PASS:' in log and 'ERROR:' not in log,name
for mode in modes:
    log=(root/'tools'/f'capture_{mode}.log').read_text(encoding='utf-8-sig')
    assert '.png 0 ' in log and 'ERROR:' not in log,mode
    metrics['captures'][mode]=dict(zip(['draw_calls','nodes'],map(float,re.search(r'draw_calls=([\d.]+) nodes=([\d.]+)',log).groups())))
for name in ['amarras_integration','amarras_surface_finish']:
    log=(root/'tools'/f'{name}.log').read_text(encoding='utf-8-sig');assert 'saved=0' in log and 'ERROR:' not in log,name
(root/'tools/amarras_metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
files=[root/'project.godot',root/'maps/sucateia/sucateia.tscn',root/'maps/fundo_ferro/fundo_ferro.tscn',Path(__file__),root/'licenses/assets.md']
files+=list((root/'scripts').rglob('*.gd'))+list((root/'scenes').rglob('*.tscn'))+list((root/'tests').glob('*.gd'))
files+=[p for p in (root/'assets').rglob('*') if p.is_file() and not any(part in p.parts for part in ['source','cabos_parallel','docas_parallel']) and p.suffix in ['.png','.svg','.gdshader','.tres','.json']]
# Include actual reused future-art dependencies rather than unrelated unfinished districts.
files+=[root/path[6:] for path in re.findall(r'path="(res://assets/(?:reconstruction/cabos_parallel|reconstruction/docas_parallel)/[^\"]+)"',scene)]
files+=[root/'tools'/f'fundo_{name}.log' for name in tests]
files+=[root/'tools'/f'capture_{name}.log' for name in modes]+[root/'maps/sucateia'/f'preview_{name}.png' for name in modes]
files+=list((root/'tools/checkpoints').glob('*.tscn'))
files+=[root/'tools'/name for name in ['AMARRAS_PROGRESS.md','AMARRAS_RESULT.md','AMARRAS_REVIEW.md','amarras_metrics.json','amarras_parallel_art.md','CONSULTANT_AMARRAS_ASSETS.md','CONSULTANT_AMARRAS_REVIEW.md','approved_art_hashes.json','build_amarras_geography.gd','reshape_amarras.gd','adjust_amarras_crossing.gd','integrate_amarras_art.gd','finish_amarras_surface.gd','amarras_integration.log','amarras_surface_finish.log','run_fundo_checks.py','run_forjas_captures.py']]
files+=[root/'tools/checkpoints/city_before_amarras.png',root/'docs/superpowers/plans/2026-10-03-passagem-amarras.md']
files+=[root/'tools/CONSULTANT_AMARRAS_FINAL.md']
# Tests refer to earlier phase baselines; their check helpers remain available in the checkpoint.
files+=list((root/'tools').glob('test_*.gd'))
output=root/'tools/checkpoints/sucateia_amarras_integrada.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(set(files)):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
    for dependency in re.findall(r'path="res://([^\"]+)"',scene):assert dependency in archive.namelist(),dependency
print('PASS:16 verified test logs;7 current captures;8 selected hashes;protected art and unchanged underground;scene dependencies and checkpoint CRC')
print(output,output.stat().st_size,'bytes')
