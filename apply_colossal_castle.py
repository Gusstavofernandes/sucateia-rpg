import re

# 1. Ler sucateia.tscn
with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

# 2. Verificar ExtResource do Castelo
ext_id = 'ext_clock_castle'
if 'monumental_clock_castle.png' not in text:
    ext_decl = f'[ext_resource type="Texture2D" path="res://assets/generated/structures/monumental_clock_castle.png" id="{ext_id}"]\n'
    last_ext_idx = text.rfind('[ext_resource ')
    end_of_last_ext = text.find('\n', last_ext_idx) + 1
    text = text[:end_of_last_ext] + ext_decl + text[end_of_last_ext:]
    print("ExtResource do castelo adicionado.")
else:
    m = re.search(r'\[ext_resource[^\]]+monumental_clock_castle\.png"[^\]]+id="([^"]+)"', text)
    if m:
        ext_id = m.group(1)
        print(f"ExtResource encontrado: {ext_id}")

# 3. Remover nó GrandeLixao de RouteMarkers para restaurar as 9 rotas oficiais
text = re.sub(r'\[node name="GrandeLixao" type="Marker2D" parent="RouteMarkers"[^\]]*\]\s*position = Vector2\([^\)]+\)\s*', '', text)

# 4. Substituir house_3 pelo Castelo Monumental Colossal perfeitamente posicionado em Vector2(1060, 360)
house3_pattern = re.compile(r'\[node name="house_3" type="Node2D" parent="Structures"[^\n]*\n.*?(?=\n\[node name="[^"]+" type="Node2D" parent="Structures"|\Z)', re.DOTALL)
m_h3 = house3_pattern.search(text)
assert m_h3, "house_3 não encontrado em Structures!"

new_house3 = f'''[node name="house_3" type="Node2D" parent="Structures" unique_id=132531889]
position = Vector2(1060, 360)

[node name="Architecture" type="Sprite2D" parent="Structures/house_3" unique_id=1644269952]
z_as_relative = false
z_index = 3
position = Vector2(0, -948)
scale = Vector2(1.5, 1.5)
texture = ExtResource("{ext_id}")

[node name="BuildingFootprint" type="StaticBody2D" parent="Structures/house_3" unique_id=214941967]
position = Vector2(0, 0)

[node name="LeftWall" type="CollisionPolygon2D" parent="Structures/house_3/BuildingFootprint" unique_id=963675483]
polygon = PackedVector2Array(-600, -10, -130, -10, -130, -250, -600, -250)

[node name="RightWall" type="CollisionPolygon2D" parent="Structures/house_3/BuildingFootprint" unique_id=963675484]
polygon = PackedVector2Array(130, -10, 600, -10, 600, -250, 130, -250)

[node name="PortalBackWall" type="CollisionPolygon2D" parent="Structures/house_3/BuildingFootprint" unique_id=963675485]
polygon = PackedVector2Array(-130, -160, 130, -160, 130, -250, -130, -250)

[node name="DungeonEntrance" type="Area2D" parent="Structures/house_3" unique_id=963675486]
position = Vector2(0, -90)
collision_layer = 0
collision_mask = 2
script = ExtResource("57_fcssb")
metadata/dungeon_destination = "res://maps/dungeon_relogio/dungeon_relogio.tscn"
metadata/dungeon_name = "Masmorra do Grande Relógio"

[node name="CollisionPolygon2D" type="CollisionPolygon2D" parent="Structures/house_3/DungeonEntrance" unique_id=963675487]
polygon = PackedVector2Array(-90, -40, 90, -40, 90, 40, -90, 40)

[node name="Prompt" type="Label" parent="Structures/house_3/DungeonEntrance" unique_id=963675488]
visible = false
z_index = 25
offset_left = -180.0
offset_top = -60.0
offset_right = 180.0
offset_bottom = -32.0
theme_override_colors/font_color = Color(0.9098039, 0.7921569, 0.5529412, 1)
theme_override_colors/font_shadow_color = Color(0, 0, 0, 1)
theme_override_constants/shadow_offset_x = 2
theme_override_constants/shadow_offset_y = 2
text = "F — entrar · Masmorra do Relógio"
horizontal_alignment = 1

[node name="@Sprite2D@43" type="Sprite2D" parent="Structures/house_3" unique_id=304317092]
modulate = Color(0, 0, 0, 0.55)
z_as_relative = false
z_index = 2
position = Vector2(0, -10)
scale = Vector2(8.0, 2.0)
texture = ExtResource("7_xcrs8")
'''

text = text[:m_h3.start()] + new_house3 + text[m_h3.end():]

# Salvar
with open('maps/sucateia/sucateia.tscn', 'w', encoding='utf-8', newline='') as f:
    f.write(text)

print("Sucateia.tscn atualizado com sucesso!")
