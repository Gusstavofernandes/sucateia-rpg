import re

tscn_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn'
with open(tscn_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir o bloco de ExtResources de pipes (de id=50 em diante ate o ShaderMaterial)
pipe_resources = """[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_industrial.png" id="50_cano_longo"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_industrial_sombra.png" id="51_cano_longo_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/passagem_parede_flange.png" id="52_cano_passagem"]
[ext_resource type="Texture2D" path="res://assets/pipes/passagem_parede_flange_sombra.png" id="53_cano_passagem_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_valvula.png" id="54_cano_valvula"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_valvula_sombra.png" id="55_cano_valvula_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_berco_apoio.png" id="56_cano_berco"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_berco_apoio_sombra.png" id="57_cano_berco_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_travessia_ponte.png" id="58_cano_ponte"]
[ext_resource type="Texture2D" path="res://assets/pipes/cano_travessia_ponte_sombra.png" id="59_cano_ponte_sombra"]
[ext_resource type="Texture2D" path="res://assets/pipes/boca_bocal_conexao.png" id="60_bocal_conexao"]
[ext_resource type="Texture2D" path="res://assets/pipes/boca_bocal_conexao_sombra.png" id="61_bocal_conexao_sombra"]
"""

# Substitui da ocorrencia de [ext_resource ... id="50_cano_longo"] ate [sub_resource type="ShaderMaterial" id="ShaderMaterial_bedrock"]
pattern = r'\[ext_resource type="Texture2D" path="res://assets/pipes/cano_longo_industrial\.png"[\s\S]*?(?=\[sub_resource type="ShaderMaterial")'
content = re.sub(pattern, pipe_resources + '\n', content)

# Atualizar load_steps
content = re.sub(r'load_steps=\d+', 'load_steps=70', content)

with open(tscn_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Cabeçalho corrigido com IDs únicos de 50 a 61!")
