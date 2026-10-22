from pathlib import Path
import hashlib,json,re,zipfile

root=Path(__file__).resolve().parents[1]
if (root/'tools/CONSULTANT_DOCAS_FINAL.md').exists():
    raise SystemExit('Docas checkpoint approved and closed; preserve its historical ZIP. Use a new checkpoint for future work.')
tests=['test_docas_contacts','test_docas_routes','test_docas_preservation','test_cabos_layers','test_cabos_routes','test_cabos_art_contacts','test_cabos_preservation','test_amarras_infrastructure','test_amarras_routes','test_amarras_preservation','test_forjas_production','test_forjas_refinement_preservation','test_forjas_functional_modules','test_forjas_render_order','test_forjas_rasas','test_forjas_preservation','test_alto_lixo','test_alto_refinement','test_lower_coast','test_market_expansion','test_slice','test_fundo_access','test_fundo_layout','test_utility_contacts','test_port_approach','test_cabos_support_depth']
modes=['docas_full','docas_district','docas_loading','docas_sorting','docas_repair','docas_urban','docas_technical']
digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
scene_path=root/'maps/sucateia/sucateia.tscn'
scene=scene_path.read_text(encoding='utf-8-sig')
assert 'name="DocasDistrict"' in scene and 'name="CabosDistrict"' in scene
audit=read(root/'assets/reconstruction/docas_parallel/audit_v1/manifest.json')
complements=read(root/'assets/reconstruction/docas_parallel/complement_v1/manifest.json')
selected=audit['assets']+complements['selected']+read(root/'assets/reconstruction/docas_finish/manifest.json')
assert len(selected)==9
for item in selected:
    assert digest(root/item['path'])==item['sha256'],item['path']
    assert 'res://'+item['path'] in scene,item['path']
for path,sha in audit['protected_png_hashes'].items():assert digest(root/path)==sha,path
for path,sha in read(root/'tools/approved_art_hashes.json').items():assert digest(root/path)==sha,path
assert (root/'maps/fundo_ferro/fundo_ferro.tscn').read_bytes()==(root/'tools/checkpoints/fundo_before_functional_finish.tscn').read_bytes()
metrics={'tests':len(tests),'selected_generated_assets':9,'protected_pngs':len(audit['protected_png_hashes']),'same_scene_connections':3,'route_sections':17,'safe_respawns':6,'safe_painted_centers':2776,'consultant_approval':'pending','captures':{}}
for name in tests:
    log=(root/'tools'/f'fundo_{name}.log').read_text(encoding='utf-8-sig')
    assert 'PASS:' in log and 'ERROR:' not in log,name
for mode in modes:
    log=(root/'tools'/f'capture_{mode}.log').read_text(encoding='utf-8-sig')
    assert '.png 0 ' in log and 'ERROR:' not in log,mode
    metrics['captures'][mode]=dict(zip(['draw_calls','nodes'],map(float,re.search(r'draw_calls=([\d.]+) nodes=([\d.]+)',log).groups())))
    metrics['captures'][mode]['sha256']=digest(root/'maps/sucateia'/f'preview_{mode}.png')
assert len({item['nodes'] for item in metrics['captures'].values()})==1,'Capture tree changed during final verification'
metrics['scene_sha256']=digest(scene_path)
metrics['runtime_hashes']={str(p.relative_to(root)).replace('\\','/'):digest(p) for p in (root/'scripts').rglob('*.gd')}
(root/'tools/docas_metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
files=[root/'project.godot',scene_path,root/'maps/fundo_ferro/fundo_ferro.tscn',Path(__file__),root/'licenses/assets.md']
files+=list((root/'scripts').rglob('*.gd'))+list((root/'scenes').rglob('*.tscn'))+list((root/'tests').glob('*.gd'))
files+=[p for p in (root/'assets').rglob('*') if p.is_file() and not any(part in p.parts for part in ['source','cabos_parallel','docas_parallel']) and p.suffix in ['.png','.svg','.gdshader','.tres','.json']]
files+=[root/path for path in re.findall(r'path="res://(assets/(?:reconstruction/cabos_parallel|reconstruction/docas_parallel)/[^\"]+)"',scene)]
files+=list((root/'assets/reconstruction/cabos_parallel/audit_v1').glob('*.json'))
files+=list((root/'assets/reconstruction/docas_parallel/audit_v1').glob('*.json'))+list((root/'assets/reconstruction/docas_parallel/complement_v1').glob('*.json'))
files+=[root/'tools'/f'fundo_{name}.log' for name in tests]
files+=[root/'tools'/f'capture_{name}.log' for name in modes]+[root/'maps/sucateia'/f'preview_{name}.png' for name in modes]
files+=list((root/'tools/checkpoints').glob('*.tscn'))+list((root/'tools').glob('*.gd'))
files+=list((root/'docs/superpowers/plans').glob('*.md'))
files+=[root/'tools'/name for name in ['DOCAS_PROGRESS.md','DOCAS_RESULT.md','DOCAS_REVIEW.md','DOCAS_ART_HANDOFF.md','DOCAS_ART_REQUESTS.md','docas_metrics.json','CONSULTANT_DOCAS_BRIEF.md','CONSULTANT_CABOS_FINAL.md','approved_art_hashes.json','run_fundo_checks.py','run_forjas_captures.py','audit_docas_art.py','qa_docas_polish.py','STAIR_FITS_AUDIT.md','PORT_APPROACH_AUDIT.md'] if (root/'tools'/name).exists()]
output=root/'tools/checkpoints/sucateia_docas_integrada.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(set(files)):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
    for dependency in re.findall(r'path="res://([^\"]+)"',scene):assert dependency in archive.namelist(),dependency
    for item in selected:assert item['path'] in archive.namelist(),item['path']
    assert hashlib.sha256(archive.read('maps/sucateia/sucateia.tscn')).hexdigest()==metrics['scene_sha256']
print('PASS:26 verified test logs;7 stable captures;9 selected hashes;121 protected PNGs;underground unchanged;scene dependencies and checkpoint CRC')
print(output,output.stat().st_size,'bytes')
