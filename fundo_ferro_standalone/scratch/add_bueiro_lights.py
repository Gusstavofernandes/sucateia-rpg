import re

scene_path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn'
with open(scene_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Add a PointLight2D to each Bueiro for its wall lantern
light_node = """
[node name="LuzLanternaBueiro" type="PointLight2D" parent="Bueiro_{num}"]
position = Vector2(-65, -45)
color = Color(1, 0.74, 0.38, 1)
energy = 1.4
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.8
"""

for num in [1, 2, 3]:
    target = f'[node name="ArcoPedra" type="Sprite2D" parent="Bueiro_{num}"]'
    replacement = light_node.format(num=num) + target
    text = text.replace(target, replacement, 1)

with open(scene_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Lantern lights added to Bueiros 1, 2, 3!")
