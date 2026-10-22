from pathlib import Path
import hashlib,json,re,zipfile
root=Path(__file__).resolve().parents[1]
current=(root/'maps/sucateia/sucateia.tscn').read_text(encoding='utf-8')
if 'name="PassagemAmarrasDistrict"' in current:
    raise SystemExit('Historical Forjas checkpoint protected: Amarras now exists; use its own finalizer.')
before=(root/'tools/checkpoints/sucateia_before_forjas_direction.tscn').read_text(encoding='utf-8')
def cells(text,name):
    node=next(b for b in text.split('[node ') if b.startswith(f'name="{name}"'))
    return re.search(r'tile_map_data = PackedByteArray\("([^"]+)"\)',node).group(1)
for name in ['MarketFloor','AltoFloor','TerraceFloor','ForjasFloor']:assert cells(current,name)==cells(before,name),name
for path,digest in json.loads((root/'tools/approved_art_hashes.json').read_text(encoding='utf-8')).items():assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest,path
assert (root/'maps/fundo_ferro/fundo_ferro.tscn').read_bytes()==(root/'tools/checkpoints/fundo_before_functional_finish.tscn').read_bytes()
for label in ['ProductionDirectionFinish','PhysicalGroundContact','RegionalEdgeContext','DutoDeExaustaoLigado','LoadingStopsFinish']:assert label in current,label
tests=['test_forjas_production','test_forjas_refinement_preservation','test_forjas_functional_modules','test_forjas_render_order','test_forjas_rasas','test_forjas_preservation','test_alto_lixo','test_alto_refinement','test_lower_coast','test_market_expansion','test_slice','test_fundo_access','test_fundo_layout']
modes=['forjas_district','forjas_full','forjas_frontier','forjas_foundry','forjas_recycling','forjas_drain','forjas_market_central_landmark']
metrics={}
for test in tests:
    log=(root/'tools'/f'fundo_{test}.log').read_text(encoding='utf-8-sig');assert 'PASS:' in log and 'ERROR:' not in log,test
for mode in modes:
    log=(root/'tools'/f'capture_{mode}.log').read_text(encoding='utf-8-sig');assert '.png 0 ' in log and 'ERROR:' not in log,mode
    metrics[mode]=dict(zip(['draw_calls','nodes'],map(float,re.search(r'draw_calls=([\d.]+) nodes=([\d.]+)',log).groups())))
for logname in ['forjas_direction_integration','forjas_ports_integration','forjas_border_integration','forjas_ground_contact','forjas_logistics_finish']:
    log=(root/'tools'/f'{logname}.log').read_text(encoding='utf-8-sig');assert 'saved=0' in log and 'ERROR:' not in log,logname
(root/'tools/forjas_direction_metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
plan=root/'docs/superpowers/plans/2026-10-02-forjas-direction-correction.md'
plan_text=plan.read_text(encoding='utf-8').replace('- [ ]','- [x]')
if 'Passe de contato físico incorporado.' not in plan_text:plan_text+='\nPasse de contato físico incorporado. Resultado e limites: tools/FORJAS_DIRECTION_RESULT.md; aprovação visual humana permanece pendente.\n'
plan.write_text(plan_text,encoding='utf-8')
paragraph='\n\n## Correção de direção e contato físico — versão para revisão\n\nForjas na cena atual: faixa industrial20%, quatro pátios funcionais adicionais, chaminé anexada à fundição central, portos alinhados, resfriamento/drenagem, sombras e apoios nas bases reais, tubos sustentados e pontes ancoradas. Água/talude de contexto sem ampliar território jogável.13 testes distintos e7 capturas finais; relatório tools/FORJAS_DIRECTION_RESULT.md, antes/depois de fundição/máquina/passarela, manifesto complementar e checkpoint sucateia_forjas_direcao_integracao.zip. Original/Mercado/Alto-Lixo/pisos/colisões antigas e camada inferior preservados. Aprovação visual humana pendente; nenhum novo setor iniciado.\n'
for name in ['RECONSTRUCTION_STATUS.md','REGION_STATUS.md']:
    path=root/'tools'/name;text=path.read_text(encoding='utf-8')
    if '## Correção de direção e contato físico' not in text:path.write_text(text+paragraph,encoding='utf-8')
license=root/'licenses/assets.md';text=license.read_text(encoding='utf-8')
if 'complement_v1/manifest.json' not in text:license.write_text(text+'\n| Complementos funcionais Forjas:12 PNGs usados | Gerador integrado image_gen; assets/reconstruction/forjas_parallel/complement_v1/manifest.json | Gerados para este projeto; não são CC0 | Pátios, torre add-on, redutor, suportes, passarela e decals;13 selecionados, oficina extra não utilizada |\n',encoding='utf-8')
files=[root/'project.godot',root/'maps/sucateia/sucateia.tscn',root/'maps/fundo_ferro/fundo_ferro.tscn',Path(__file__),plan,license]
files+=list((root/'scripts').rglob('*.gd'))+list((root/'scenes').rglob('*.tscn'))
files+=[p for p in (root/'assets').rglob('*') if p.is_file() and not any(part in p.parts for part in ['source','cabos_parallel','docas_parallel']) and p.suffix in ['.png','.svg','.gdshader','.tres','.json']]
files+=[root/'tests'/f'{test}.gd' for test in tests]+[root/'tools'/f'fundo_{test}.log' for test in tests]
files+=[root/'maps/sucateia'/f'preview_{mode}.png' for mode in modes]+[root/'tools'/f'capture_{mode}.log' for mode in modes]
for name in ['FORJAS_DIRECTION_AUDIT.md','FORJAS_DIRECTION_RESULT.md','FORJAS_DIRECTION_REVIEW.md','forjas_direction_metrics.json','forjas_complement_art.md','approved_art_hashes.json','RECONSTRUCTION_STATUS.md','REGION_STATUS.md','correct_forjas_direction.gd','align_forjas_ports.gd','finish_forjas_border.gd','ground_forjas_structures.gd','extend_forjas_sea.gd','polish_forjas_logistics.gd','forjas_logistics_finish.log','run_forjas_refinement_checks.py','run_fundo_checks.py','run_forjas_captures.py']:
    files.append(root/'tools'/name)
for name in ['sucateia_before_forjas_direction.tscn','sucateia_before_forjas_refinement.tscn','fundo_before_functional_finish.tscn','forjas_before_direction.png','forjas_foundry_before_grounding.png','forjas_machine_before_grounding.png','forjas_walkway_before_grounding.png']:files.append(root/'tools/checkpoints'/name)
files+=list((root/'tools/certificate_restricted_evidence').glob('*'))
output=root/'tools/checkpoints/sucateia_forjas_acabamento_local.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(set(files)):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(output) as archive:assert archive.testzip() is None
print('PASS:13 verified test logs;7 final captures;4 preserved floors;protected PNG hashes;unchanged underground;checkpoint CRC')
print(output,output.stat().st_size,'bytes')
