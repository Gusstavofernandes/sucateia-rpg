from pathlib import Path
import json,re,hashlib,zipfile
root=Path(__file__).resolve().parents[1]
surface=root/'maps/sucateia/sucateia.tscn'
under=root/'maps/fundo_ferro/fundo_ferro.tscn'
before=(root/'tools/checkpoints/sucateia_before_forjas_refinement.tscn').read_text(encoding='utf-8')
current=surface.read_text(encoding='utf-8')
assert 'ProductionDirectionFinish' not in current,'Historic finalizer: newer scene requires the direction-correction checkpoint workflow'
assert 'ForjasFunctionalModules' in current and 'IndustrialGroundFinish' in current
def tile_data(text,name):
    block=next(b for b in text.split('[node ') if b.startswith(f'name="{name}"'))
    return re.search(r'tile_map_data = PackedByteArray\("([^"]+)"\)',block).group(1)
for name in ['MarketFloor','AltoFloor','TerraceFloor','ForjasFloor']:assert tile_data(current,name)==tile_data(before,name),name
for name,digest in json.loads((root/'tools/approved_art_hashes.json').read_text(encoding='utf-8')).items():assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
assert under.read_bytes()==(root/'tools/checkpoints/fundo_before_functional_finish.tscn').read_bytes(),'Underground layer was altered'
tests=['test_forjas_refinement_preservation','test_forjas_functional_modules','test_forjas_render_order','test_forjas_rasas','test_forjas_preservation','test_alto_lixo','test_alto_refinement','test_lower_coast','test_market_expansion','test_slice','test_fundo_access','test_fundo_layout']
modes=['forjas_market_landmark','forjas_cargo','forjas_boilers','forjas_foundry','forjas_recycling','forjas_drain','forjas_frontier','forjas_district','forjas_full']
metrics={}
for name in tests:
    text=(root/'tools'/f'fundo_{name}.log').read_text(encoding='utf-8-sig');assert 'PASS:' in text and 'ERROR:' not in text,name
for name in modes:
    text=(root/'tools'/f'capture_{name}.log').read_text(encoding='utf-8-sig');assert '.png 0 ' in text and 'ERROR:' not in text,name
    assert (root/'maps/sucateia'/f'preview_{name}.png').stat().st_size>100000
    metrics[name]=dict(zip(['draw_calls','nodes'],map(float,re.search(r'draw_calls=([\d.]+) nodes=([\d.]+)',text).groups())))
assert 'ERROR:' not in (root/'tools/forjas_parallel_integration.log').read_text(encoding='utf-8-sig')
current=current.replace('urban/industrial terrain progression; connected pressure and drain networks; work aprons; parallel art integration pending','urban/industrial terrain progression; connected pressure and drain networks; work aprons; five parallel art modules integrated and validated')
surface.write_text(current,encoding='utf-8')
plan=root/'docs/superpowers/plans/2026-10-02-forjas-refinamento.md';plan.write_text(plan.read_text(encoding='utf-8').replace('- [ ]','- [x]'),encoding='utf-8')
script=(root/'tools/refine_forjas_urban.gd').read_text(encoding='utf-8')
def points(text):return [[float(x),float(y)] for x,y in re.findall(r'Vector2\(([-\d.]+),\s*([-\d.]+)\)',text)]
networks=[dict(name=name,points=points(data)) for name,data in re.findall(r'pipe\("([^"]+)",PackedVector2Array\(\[(.*?)\]\)',script)]
networks.append(dict(name='LigacaoVasoCaldeiras',points=[[2832,-1382],[2918,-1382]]))
spatial=dict(scope='localized current city refinement; no floor expansion',reference='C:/Users/Usuario/Downloads/Mapa de Ferrugem Baixa.png',networks=networks,modules={'FornalhaDaEntrada':[2050,-275],'FerreiroDaRua':[1850,-8],'MinerioDaCarga':[2490,30],'GuindasteDaFundicao':[2945,-925],'VasoDeServico':[2840,-1390]},market_viewpoint=[1600,-275],existing_buildings_preserved=19,forjas_floor_cells=1590,exits={'ChaminesVelhas':'reserved','GrandeFerrugem':'reserved','CorredorParaOsCabos':'reserved','ManutencaoFundoFerro':'three-access lower layer connected'},metrics=metrics,metrics_limit='capture samples only; not prolonged FPS benchmark')
(root/'tools/forjas_refinement_spatial.json').write_text(json.dumps(spatial,ensure_ascii=False,indent=2),encoding='utf-8')
audit=root/'tools/FORJAS_REFINEMENT_AUDIT.md';text=audit.read_text(encoding='utf-8')
if '1802 draw calls' not in text:text+='\nMétricas finais de captura: geral 1802 draw calls, setor 483, detalhes 138–231; 3448 nós. Amostras de frame, não benchmark prolongado de FPS. Dados por captura em tools/forjas_refinement_spatial.json.\n'
audit.write_text(text,encoding='utf-8')
status=root/'tools/RECONSTRUCTION_STATUS.md';text=status.read_text(encoding='utf-8').replace('## Etapa atual — Fundo-Ferro, primeira camada inferior','## Fundo-Ferro — primeira camada inferior (acabamento adicional pendente)').replace('| 4 | Fundo-Ferro | Primeira camada subterrânea navegável validada; NPCs/sistemas pendentes |','| 4 | Fundo-Ferro | Navegação validada; acabamento visual adicional solicitado e interrompido pela prioridade Forjas |')
if '## Etapa atual — Forjas Rasas, refinamento localizado' not in text:
    text+='\n\n## Etapa atual — Forjas Rasas, refinamento localizado\n\nDireção humana restringe a etapa somente a Forjas na cena atual. Piso industrial com progressão gradual, nove redes/ligação de tubos, pátios de trabalho e cinco novos módulos funcionais da frente de arte paralela. Landmark visível da entrada leste do Mercado (captura market_landmark), ferreiro na transição, minério/carrinho em carga, guindaste na fundição e vaso de serviço ligado às caldeiras. Nenhum piso/território ampliado, 19 conjuntos anteriores preservados, quatro pisos idênticos em células/atlas e cinco PNGs aprovados por hash.\n\n12 testes distintos passaram, nove capturas inspecionadas, revisão independente estática sem problemas materiais. Acessos F existentes e cena inferior preservados. Auditoria tools/FORJAS_REFINEMENT_AUDIT.md; prompts tools/forjas_parallel_art.md e assets/reconstruction/forjas_parallel/manifest.json; dados/métricas tools/forjas_refinement_spatial.json. Checkpoint tools/checkpoints/sucateia_forjas_rasas_refinamento.zip com CRC.\n\nFundo-Ferro: acabamento adicional solicitado ainda não aplicado, registrado em tools/PENDING_FUNDO_FINISH.md. Não declarar aprovação visual daquela etapa. Não avançar a outro setor; Os Cabos/Chaminés/exterior continuam aproximações, não destinos concluídos. Sem NPCs, economia, combate ou produção simulada.\n'
status.write_text(text,encoding='utf-8');(root/'tools/REGION_STATUS.md').write_text(text,encoding='utf-8')
license=root/'licenses/assets.md';text=license.read_text(encoding='utf-8')
if 'forjas_parallel' not in text:text+='\n| Cinco módulos funcionais em assets/reconstruction/forjas_parallel/ | Gerador integrado image_gen; manifest.json e tools/forjas_parallel_art.md | Gerados para este projeto; não são CC0 | Fornalha/chaminé, estoque de minério/carrinho, ferreiro aberto, vaso/tubos de serviço e guindaste de carga |\n'
license.write_text(text,encoding='utf-8')
files=[surface,under,root/'project.godot',Path(__file__),root/'tools/checkpoints/sucateia_before_forjas_refinement.tscn',root/'tools/checkpoints/fundo_before_functional_finish.tscn',root/'tools/checkpoints/forjas_before_refinement.png',root/'tools/FORJAS_REFINEMENT_AUDIT.md',root/'tools/approved_art_hashes.json',root/'tools/forjas_parallel_art.md',root/'assets/reconstruction/forjas_parallel/manifest.json',root/'tools/forjas_refinement_spatial.json',root/'tools/refine_forjas_urban.gd',root/'tools/integrate_forjas_art.gd',root/'tools/run_forjas_refinement_checks.py',root/'tools/run_fundo_checks.py',root/'tools/run_forjas_captures.py',root/'tools/PENDING_FUNDO_FINISH.md',status,root/'tools/REGION_STATUS.md',license,plan,root/'tools/forjas_parallel_integration.log']
files+=[root/'tests'/f'{name}.gd' for name in tests]+[root/'tools'/f'fundo_{name}.log' for name in tests]
files+=[root/'tools/CONSULTANT_FORJAS_REVIEW.md']
files+=[root/'tools'/f'capture_{name}.log' for name in modes]+[root/'maps/sucateia'/f'preview_{name}.png' for name in modes]
files+=list((root/'scripts').rglob('*.gd'))+list((root/'scenes').rglob('*.tscn'))
files+=[p for p in (root/'assets').rglob('*') if p.is_file() and not any(part in p.parts for part in ['source','cabos_parallel','docas_parallel']) and p.suffix in ['.png','.svg','.gdshader','.tres']]
output=root/'tools/checkpoints/sucateia_forjas_rasas_refinamento.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(set(files)):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(output) as archive:assert archive.testzip() is None
print('PASS: 12 checks, 9 inspected captures, four preserved floors, five protected PNG hashes, unchanged underground layer, checkpoint CRC')
print(output,output.stat().st_size,'bytes')
