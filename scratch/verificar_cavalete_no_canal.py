from PIL import Image

img_cavalete = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png')
cw, ch = img_cavalete.size
print(f"Cavalete textura: {cw} x {ch}")

fator = 1.25
escala_trilho = 0.20 * fator # 0.250
escala_cavalete = 0.32 * fator # 0.400

# offset_y = 25 no teste
# pos_y_trilho = 406.0 + 475 * escala_trilho - 25.0
pos_y_trilho = 406.0 + 475 * 0.25 - 25.0 # = 406.0 + 118.75 - 25.0 = 499.75 px
# Posição Y do nó CavaleteElevadoCanal:
# Como TrilhosSobreCavalete tem position = Vector2(0, -75 * fator):
# pos_y_cavalete = pos_y_trilho + 75 * fator = 499.75 + 93.75 = 593.5 px
pos_y_cavalete = pos_y_trilho + 75.0 * 1.25
pos_x_ponte = (-190.5 + 4.0 * escala_trilho) + (3.0 / 2.0) # shift world x = +1.5 px -> -190.5 + 1.0 + 1.5 = -188.0 px

print(f"Posição do nó CavaleteElevadoCanal no mundo: Vector2({pos_x_ponte:.2f}, {pos_y_cavalete:.2f})")
print(f"Escala do CavaleteSprite: Vector2({escala_cavalete:.4f}, {escala_cavalete:.4f})")
print(f"Escala do TrilhosSobreCavalete: Vector2({escala_trilho:.4f}, {escala_trilho:.4f})")

# Limites do cavalete no mundo:
cavalete_world_w = cw * escala_cavalete
cavalete_world_h = ch * escala_cavalete
c_top_y = pos_y_cavalete - cavalete_world_h / 2.0
c_bot_y = pos_y_cavalete + cavalete_world_h / 2.0

print(f"\nCavalete no mundo: largura = {cavalete_world_w:.1f} px, altura = {cavalete_world_h:.1f} px")
print(f"Topo do cavalete em Y: {c_top_y:.2f} px")
print(f"Base dos pilares do cavalete em Y: {c_bot_y:.2f} px")

# Verificar onde fica o canal na cena master
with open('fundo_ferro_standalone/scenes/fundo_ferro_master.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m_canal = re.search(r'\[node name="CanalDeEsgoto"[\s\S]*?(?=\[node name="MuretasCanal")', text)
if m_canal:
    print("\nCanalDeEsgoto:")
    print(m_canal.group(0)[:300])

m_mureta = re.search(r'\[node name="MuretasCanal"[\s\S]*?(?=\[node name="PonteServico_1")', text)
if m_mureta:
    print("\nMuretasCanal:")
    for l in m_mureta.group(0).splitlines()[:15]:
        print(l)
