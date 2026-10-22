import re

tscn_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn'
with open(tscn_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Ajustar PonteTravessia para z_index = 1 (passar por cima do cano)
content = re.sub(
    r'(\[node name="PonteTravessia" type="Sprite2D"[^\]]*\]\s*)position = Vector2\(2185, 642\)',
    r'\1z_index = 1\nposition = Vector2(2185, 642)',
    content
)

# 2. Fazer CanoLeste e BocalConexaoLeste comecarem dentro do bocal da caldeira (X=2716 em vez de 2732)
# BocalConexaoLeste em Vector2(2716, 618)
content = content.replace('position = Vector2(2732, 618)', 'position = Vector2(2716, 618)')
content = content.replace('position = Vector2(2732, 625)', 'position = Vector2(2716, 625)')

# CanoLeste_1: centro X = 2716 + 70.8 = 2787
content = content.replace('position = Vector2(2803, 618)', 'position = Vector2(2787, 618)')
content = content.replace('position = Vector2(2803, 625)', 'position = Vector2(2787, 625)')

# 3. Fazer BocalConexaoOeste penetrar no bocal esquerdo da caldeira (X=2568)
content = content.replace('position = Vector2(2558, 646)', 'position = Vector2(2568, 646)')
content = content.replace('position = Vector2(2558, 653)', 'position = Vector2(2568, 653)')

with open(tscn_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Ajustes de penetração dos bocais e z_index da ponte aplicados!")
