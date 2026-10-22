import re

tscn_path = r'maps/sucateia/sucateia.tscn'

with open(tscn_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remover BombaDaMargem e seus nós filhos
pattern_bomba = r'\[node name="BombaDaMargem"[\s\S]*?(?=\[node name="PortStitchArchitecture")'
assert re.search(pattern_bomba, content), "BombaDaMargem não encontrada"
content = re.sub(pattern_bomba, '', content)

# 2. Remover BombaDaMargemContact
pattern_bomba_contact = r'\[node name="BombaDaMargemContact"[\s\S]*?(?=\[node name="CascoNaAgua")'
assert re.search(pattern_bomba_contact, content), "BombaDaMargemContact não encontrada"
content = re.sub(pattern_bomba_contact, '', content)

# 3. Remover os canos da bomba (EntradaDaBomba0, EntradaDaBomba1, CotoveloNaMargem)
pattern_pipes = r'\[node name="EntradaDaBomba0"[\s\S]*?(?=\[node name="PortStitchInfrastructure")'
assert re.search(pattern_pipes, content), "Canos da bomba não encontrados"
content = re.sub(pattern_pipes, '', content)

# 4. Remover TecnicoInterior0_0 e TecnicoInterior0_1
pattern_tecnico_interior = r'\[node name="TecnicoInterior0_0"[\s\S]*?(?=\[node name="Junta3990Interior0_0")'
assert re.search(pattern_tecnico_interior, content), "TecnicoInterior não encontrado"
content = re.sub(pattern_tecnico_interior, '', content)

# 5. Substituir RecuperacaoLeste00 e RecuperacaoLeste01 pela nova PlataformaCaisTrabalhada
nova_plataforma = """[node name="PlataformaCaisTrabalhada" type="Sprite2D" parent="DocasDistrict/WorkingDecks" unique_id=1523029524]
position = Vector2(3185, 610)
scale = Vector2(0.24, 0.24)
texture = ExtResource("114_plataforma_cais")

"""
pattern_recuperacao = r'\[node name="RecuperacaoLeste00"[\s\S]*?(?=\[node name="TecnicoDrenagem00")'
assert re.search(pattern_recuperacao, content), "RecuperacaoLeste00 não encontrada"
content = re.sub(pattern_recuperacao, nova_plataforma, content)

# 6. Remover Junta3890ApoioRemendado se existir
pattern_junta = r'\[node name="Junta3890ApoioRemendado"[\s\S]*?(?=\[node name="TecnicoForjasContencao00")'
if re.search(pattern_junta, content):
    content = re.sub(pattern_junta, '', content)

# 7. Remover as antigas estacas recortadas RecuperacaoLesteContencao00 e 01
pattern_contencoes = r'\[node name="RecuperacaoLesteContencao00"[\s\S]*?(?=\[node name="TecnicoDrenagemContencao00")'
assert re.search(pattern_contencoes, content), "Contencoes não encontradas"
content = re.sub(pattern_contencoes, '', content)

with open(tscn_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Modificações aplicadas com sucesso em maps/sucateia/sucateia.tscn!")
