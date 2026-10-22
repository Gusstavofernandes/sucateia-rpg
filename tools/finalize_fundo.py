from pathlib import Path
import json,re,hashlib,zipfile
root=Path(__file__).resolve().parents[1]
surface=root/'maps/sucateia/sucateia.tscn'
under=root/'maps/fundo_ferro/fundo_ferro.tscn'
previous=(root/'tools/checkpoints/sucateia_before_fundo.tscn').read_text(encoding='utf-8')
current=surface.read_text(encoding='utf-8')
assert 'IndustrialGroundFinish' not in current,'Historical Fundo checkpoint must not be recreated after Forjas refinement'
def tile_data(text,name):
    block=next(b for b in text.split('[node ') if b.startswith(f'name="{name}"'))
    return re.search(r'tile_map_data = PackedByteArray\("([^"]+)"\)',block).group(1)
for name in ['MarketFloor','AltoFloor','TerraceFloor','ForjasFloor']:
    assert tile_data(current,name)==tile_data(previous,name),name
for name,digest in json.loads((root/'tools/approved_art_hashes.json').read_text(encoding='utf-8')).items():
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
tests=['test_fundo_layout','test_fundo_access','test_fundo_preservation','test_forjas_render_order','test_forjas_rasas','test_forjas_preservation','test_alto_lixo','test_alto_refinement','test_lower_coast','test_market_expansion','test_slice']
modes=['fundo_full']+['fundo_'+r for r in ['PocoVelho','Bombas','Descarte','Maquinas','Reservatorio','Ruinas','Valvulas']]+['fundo_surface_'+r for r in ['PocoVelho','DocaLeste','ForjasManutencao']]
captures=[]
for name in tests:
    text=(root/'tools'/f'fundo_{name}.log').read_text(encoding='utf-8-sig')
    assert 'PASS:' in text and 'ERROR:' not in text,name
for mode in modes:
    text=(root/'tools'/f'capture_{mode}.log').read_text(encoding='utf-8-sig')
    assert ' 0 draw_calls=' in text and 'ERROR:' not in text,mode
    path=root/('maps/sucateia' if mode.startswith('fundo_surface') else 'maps/fundo_ferro')/f'preview_{mode}.png'
    assert path.stat().st_size>100000;captures.append(path)
under.write_text(under.read_text(encoding='utf-8').replace('first underground stage built; validation pending','first underground stage validated; three paired physical accesses; no NPC/combat/economy'),encoding='utf-8')
plan=root/'docs/superpowers/plans/2026-10-02-fundo-ferro.md'
plan.write_text(plan.read_text(encoding='utf-8').replace('- [ ]','- [x]'),encoding='utf-8')
status=root/'tools/RECONSTRUCTION_STATUS.md'
text=status.read_text(encoding='utf-8').replace('## Etapa atual — Forjas Rasas, primeira implantação exterior','## Forjas Rasas — primeira implantação exterior').replace('| 4 | Fundo-Ferro | Pendente |','| 4 | Fundo-Ferro | Primeira camada subterrânea navegável validada; NPCs/sistemas pendentes |').replace('Controles atuais: WASD/setas, Shift, roda, R e F1.','Controles atuais: WASD/setas, Shift, roda, R e F1; F em proximidade nos três acessos físicos superfície/subsolo.')
text+='\n\n## Etapa atual — Fundo-Ferro, primeira camada inferior\n\nSete salas, oito rotas, circuito de retorno, duas pontes e três acessos físicos bidirecionais (F): Poço Velho, Doca Leste e manutenção sul de Forjas. Cena inferior separada por necessidade de camada, mantendo a cidade de superfície completa; nenhum portal E entre bairros reativado. Retorno e R usam chegadas seguras. Baseline: tools/checkpoints/sucateia_before_fundo.tscn.\n\n11 testes passaram: travessia física de todas as salas/trechos/pontes, água e máquinas bloqueadas, seis transições por input real, preservação completa da superfície e regressões. Onze capturas foram inspecionadas, incluindo panorama, sete salas e três acessos. Parede arruinada e motor abandonado gerados no image_gen integrado; prompts e fontes em tools/fundo_art_manifest.json. Auditoria: tools/FUNDO_FERRO_AUDIT.md. Planta: docs/fundo-ferro-planta-espacial.svg. Checkpoint: tools/checkpoints/sucateia_fundo_ferro_primeira_etapa.zip.\n\nPrimeira etapa de navegação/ambientação; sem NPCs, criaturas/gangues funcionais, combate ou economia. Próximo setor aguarda revisão. Os demais setores permanecem pendentes; Ferrugem Baixa não está concluída.\n'
status.write_text(text,encoding='utf-8')
(root/'tools/REGION_STATUS.md').write_text(text,encoding='utf-8')
license=root/'licenses/assets.md'
text=license.read_text(encoding='utf-8')
if 'fundo_art_manifest' not in text:
    text+='\n| Parede arruinada e motor abandonado em assets/reconstruction/fundo*.png | Gerador de imagem integrado OpenAI; tools/fundo_art_manifest.json | Gerados para este projeto; não são CC0 | Parede modular de túneis e landmark da Casa das Máquinas de Fundo-Ferro; referência exclusiva do benchmark original |\n'
license.write_text(text,encoding='utf-8')
files=[surface,under,root/'project.godot',Path(__file__),root/'tools/checkpoints/sucateia_before_fundo.tscn',root/'tools/FUNDO_FERRO_AUDIT.md',root/'tools/approved_art_hashes.json',root/'tools/fundo_art_manifest.json',root/'tools/fundo_spatial_plan.json',root/'tools/draw_fundo_spatial_plan.py',root/'tools/build_fundo_ferro.gd',root/'tools/refine_fundo_ferro.gd',root/'tools/run_fundo_checks.py',root/'tools/run_fundo_captures.py',status,root/'tools/REGION_STATUS.md',license,plan,root/'docs/fundo-ferro-planta-espacial.svg']
files+=[root/'tests'/f'{name}.gd' for name in tests]+[root/'tools'/f'fundo_{name}.log' for name in tests]
files+=[root/'tools'/f'capture_{name}.log' for name in modes]+captures
files+=list((root/'scripts').rglob('*.gd'))+list((root/'scenes').rglob('*.tscn'))
files+=[p for p in (root/'assets').rglob('*') if p.is_file() and 'source' not in p.parts and p.suffix in ['.png','.svg','.gdshader','.tres']]
output=root/'tools/checkpoints/sucateia_fundo_ferro_primeira_etapa.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(set(files)):archive.write(path,path.relative_to(root))
with zipfile.ZipFile(output) as archive:assert archive.testzip() is None
print('PASS: 11 tests, 11 inspected captures, four preserved floors, five protected PNG hashes, checkpoint CRC verified')
print(output,output.stat().st_size,'bytes')
