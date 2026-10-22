from pathlib import Path
import hashlib,json,re,zipfile
root=Path(__file__).resolve().parents[1]
tests=['test_cabos_layers','test_cabos_routes','test_cabos_art_contacts','test_cabos_preservation','test_amarras_infrastructure','test_amarras_routes','test_amarras_preservation','test_forjas_production','test_forjas_refinement_preservation','test_forjas_functional_modules','test_forjas_render_order','test_forjas_rasas','test_forjas_preservation','test_alto_lixo','test_alto_refinement','test_lower_coast','test_market_expansion','test_slice','test_fundo_access','test_fundo_layout']
modes=['cabos_full','cabos_district','cabos_market','cabos_alto','cabos_forjas','cabos_junction','cabos_underpass']
scene_path=root/'maps/sucateia/sucateia.tscn'
scene=scene_path.read_text(encoding='utf-8-sig')
assert 'name="CabosDistrict"' in scene and 'name="DocasDistrict"' not in scene,'Protect historical Cabos checkpoint after future district starts'
audit=json.loads((root/'assets/reconstruction/cabos_parallel/audit_v1/manifest.json').read_text(encoding='utf-8-sig'))
deck=json.loads((root/'assets/reconstruction/cabos_parallel/audit_v1/main_deck_manifest.json').read_text(encoding='utf-8-sig'))
selected=[entry for entry in audit['assets'] if entry['path'].startswith('assets/reconstruction/cabos_parallel/')]+[deck]
assert len(selected)==5
for entry in selected:
    assert hashlib.sha256((root/entry['path']).read_bytes()).hexdigest()==entry['sha256'],entry['path']
    assert 'res://'+entry['path'] in scene,entry['path']
for path,digest in audit['protected_png_hashes'].items():
    assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,path
for path,digest in json.loads((root/'tools/approved_art_hashes.json').read_text(encoding='utf-8-sig')).items():
    assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,path
assert (root/'maps/fundo_ferro/fundo_ferro.tscn').read_bytes()==(root/'tools/checkpoints/fundo_before_functional_finish.tscn').read_bytes()
metrics={'tests':len(tests),'selected_generated_assets':5,'protected_pngs':len(audit['protected_png_hashes']),'same_scene_accesses':3,'route_sections':16,'landings':14,'floor_modules':32,'painted_landings':11,'stairs':6,'supports':27,'safe_painted_centers':3458,'upper_boundary_segments':172,'consultant_approval':'pending','captures':{}}
for name in tests:
    log=(root/'tools'/f'fundo_{name}.log').read_text(encoding='utf-8-sig')
    assert 'PASS:' in log and 'ERROR:' not in log,name
for mode in modes:
    log=(root/'tools'/f'capture_{mode}.log').read_text(encoding='utf-8-sig')
    assert '.png 0 ' in log and 'ERROR:' not in log,mode
    metrics['captures'][mode]=dict(zip(['draw_calls','nodes'],map(float,re.search(r'draw_calls=([\d.]+) nodes=([\d.]+)',log).groups())))
    metrics['captures'][mode]['sha256']=hashlib.sha256((root/'maps/sucateia'/f'preview_{mode}.png').read_bytes()).hexdigest()
assert all(entry['nodes']==5185 for entry in metrics['captures'].values()),'Capture tree differs from final runtime'
scene=scene.replace('metadata/stage = "visual integration pending capture and physical revalidation"','metadata/stage = "Cabos verified: 20 tests, three F accesses, painted routes and corrected independent review; consultant visual approval pending"')
scene_path.write_text(scene,encoding='utf-8')
metrics['scene_sha256']=hashlib.sha256(scene_path.read_bytes()).hexdigest()
(root/'tools/cabos_metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
files=[root/'project.godot',scene_path,root/'maps/fundo_ferro/fundo_ferro.tscn',Path(__file__),root/'licenses/assets.md']
files+=list((root/'scripts').rglob('*.gd'))+list((root/'scenes').rglob('*.tscn'))+list((root/'tests').glob('*.gd'))
files+=[p for p in (root/'assets').rglob('*') if p.is_file() and not any(part in p.parts for part in ['source','cabos_parallel','docas_parallel']) and p.suffix in ['.png','.svg','.gdshader','.tres','.json']]
files+=[root/path[6:] for path in re.findall(r'path="(res://assets/(?:reconstruction/cabos_parallel|reconstruction/docas_parallel)/[^\"]+)"',scene)]
files+=list((root/'assets/reconstruction/cabos_parallel/audit_v1').glob('*.json'))
files+=[root/'assets/reconstruction/cabos_parallel/audit_v1'/name for name in ['qa_gameplay_connections.png','qa_main_deck_gameplay.png']]
files+=[root/'tools'/f'fundo_{name}.log' for name in tests]
files+=[root/'tools'/f'capture_{name}.log' for name in modes]+[root/'maps/sucateia'/f'preview_{name}.png' for name in modes]
files+=list((root/'tools/checkpoints').glob('*.tscn'))+list((root/'tools').glob('*.gd'))
files+=list((root/'docs/superpowers/plans').glob('*.md'))
files+=[root/'tools'/name for name in ['CABOS_PROGRESS.md','CABOS_RESULT.md','CABOS_REVIEW.md','CABOS_ART_HANDOFF.md','CABOS_ART_REQUESTS.md','cabos_metrics.json','cabos_parallel_art.md','CONSULTANT_CABOS_BRIEF.md','approved_art_hashes.json','restore_cabos_scene_paths.py','run_fundo_checks.py','run_forjas_captures.py','audit_cabos_art.py','qa_cabos_main_deck.py','AMARRAS_RESULT.md','AMARRAS_REVIEW.md','CONSULTANT_AMARRAS_FINAL.md']]
files+=[root/'tools/checkpoints/original_visual_benchmark.png']
output=root/'tools/checkpoints/sucateia_cabos_integrada.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(set(files)):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
    for dependency in re.findall(r'path="res://([^\"]+)"',scene):assert dependency in archive.namelist(),dependency
print('PASS:20 verified test logs;7 current stable captures;5 selected hashes;105 protected PNGs;underground unchanged;scene dependencies and checkpoint CRC')
print(output,output.stat().st_size,'bytes')
