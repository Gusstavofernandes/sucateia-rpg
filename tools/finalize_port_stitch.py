from pathlib import Path
import hashlib,json,re,zipfile
root=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
tests=['port_stitch_contacts','port_stitch','docas_contacts','docas_routes','fundo_access','port_approach','docas_preservation','forjas_functional_modules','slice']
modes=['stitch_overview','stitch_sorting','stitch_service','stitch_urban','stitch_mouths']
scene=root/'maps/sucateia/sucateia.tscn'
manifest=read(root/'assets/reconstruction/port_stitch/manifest.json')
for entry in manifest['assets']:assert sha(root/entry['path'])==entry['sha256'],entry['path']
protected=read(root/'assets/reconstruction/port_stitch/protected_hashes.json')
for name,value in protected.items():assert sha(root/name)==value,name
assert (root/'maps/fundo_ferro/fundo_ferro.tscn').read_bytes()==(root/'tools/checkpoints/fundo_before_functional_finish.tscn').read_bytes()
metrics={'tests':tests,'new_generated_assets':len(manifest['assets']),'protected_pngs':len(protected),'contact_samples':80,'economic_functions':5,'preserved_F_accesses':3,'preserved_R_landings':6,'new_supported_bays':1,'consultant_approval':'pending','scene_sha256':sha(scene),'captures':{}}
for name in tests:
    log=(root/'tools'/f'fundo_test_{name}.log').read_text(encoding='utf-8-sig')
    assert 'PASS:' in log and 'ERROR:' not in log,name
for name in modes:
    log=(root/'tools'/f'capture_{name}.log').read_text(encoding='utf-8-sig')
    assert '.png 0 ' in log and 'ERROR:' not in log,name
    calls,nodes=map(float,re.search(r'draw_calls=([\d.]+) nodes=([\d.]+)',log).groups())
    metrics['captures'][name]={'draw_calls':calls,'nodes':nodes,'sha256':sha(root/'maps/sucateia'/f'preview_{name}.png')}
assert len({c['nodes'] for c in metrics['captures'].values()})==1
metrics['runtime_hashes']={str(p.relative_to(root)).replace('\\','/'):sha(p) for p in (root/'scripts').rglob('*.gd')}
metrics_path=root/'tools/port_stitch_metrics.json';metrics_path.write_text(json.dumps(metrics,indent=2),encoding='utf-8')
files={root/'project.godot',scene,root/'maps/fundo_ferro/fundo_ferro.tscn',metrics_path,Path(__file__)}
for folder,glob in [('scripts','*.gd'),('scenes','*.tscn'),('tests','*.gd')]:files.update((root/folder).rglob(glob))
# Current scene dependencies and runtime load references; original PNGs remain intact.
for path in list(files):
    if path.suffix in {'.tscn','.gd'}:
        for rel in re.findall(r'res://([^"\s]+)',path.read_text(encoding='utf-8-sig')):
            target=root/rel
            if target.is_file():files.add(target)
files.update(p for p in (root/'assets').rglob('*') if p.is_file() and p.suffix in {'.png','.svg','.json','.gdshader','.tres'} and 'source' not in p.parts and not p.name.startswith('qa_'))
files.update((root/'tools').glob('*port_stitch*.gd'));files.update((root/'tools').glob('PORT_STITCH*.md'));files.add(root/'tools/CONSULTANT_PORT_STITCH_BRIEF.md');files.add(root/'tools/checkpoints/sucateia_before_port_stitch.tscn');files.add(root/'docs/superpowers/plans/2026-10-03-port-stitch.md')
files.update(root/'tools'/f'fundo_test_{name}.log' for name in tests);files.update(root/'tools'/f'capture_{name}.log' for name in modes);files.update(root/'maps/sucateia'/f'preview_{name}.png' for name in modes)
files.update([root/'tools/run_fundo_checks.py',root/'tools/run_stitch_captures.py'])
output=root/'tools/checkpoints/sucateia_port_stitch_verificada.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(files):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(output) as archive:
    assert archive.testzip() is None
    for dependency in re.findall(r'path="res://([^\"]+)"',scene.read_text(encoding='utf-8-sig')):assert dependency in archive.namelist(),dependency
    assert hashlib.sha256(archive.read('maps/sucateia/sucateia.tscn')).hexdigest()==metrics['scene_sha256']
print(f'PASS: {len(tests)} clean tests, {len(modes)} stable captures, {len(protected)} protected PNG hashes, {len(manifest["assets"])} selected generated assets; checkpoint CRC and scene dependencies')
print(output,output.stat().st_size,'bytes; local checkpoint only, no ZIP delivery')
