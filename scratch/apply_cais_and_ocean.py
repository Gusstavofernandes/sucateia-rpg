import re

with open('maps/sucateia/sucateia.tscn.bak', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update IndustrialSea polygon
old_sea = 'polygon = PackedVector2Array(-900, 335, 3300, 335, 3300, 2600, -900, 2600)'
new_sea = 'polygon = PackedVector2Array(-1800, -800, 3300, -800, 3300, 2600, -1800, 2600)'
assert old_sea in content, "old_sea not found in backup!"
content = content.replace(old_sea, new_sea, 1)

# 2. Update WestWaterline and WestCoastalBarrier
barrier_points = [
    "-1380, -410", "-1130, -90", "-975, 15", "-790, 104", "-610, 130", "-420, 115", "-190, 92",
    "-130, 128", "-73, 166", "-18, 198", "38, 238", "94, 284", "138, 335", "146, 385", "148, 428",
    "148, 520", "130, 610", "143, 790", "159, 880", "145, 1050", "120, 1160",
    "200, 1250", "260, 1350", "290, 1415", "360, 1485", "395, 1535",
    "-1800, 2600", "-1800, -800", "-1380, -800"
]
barrier_str = "polygon = PackedVector2Array(" + ", ".join(barrier_points) + ")"

old_barrier = 'polygon = PackedVector2Array(148, 335, 148, 520, 130, 610, 143, 790, 159, 880, 145, 1050, 120, 1160, 200, 1250, 260, 1350, 290, 1415, 360, 1485, 395, 1535, -900, 2600, -900, 335)'
content = content.replace(old_barrier, barrier_str)

# 3. Create the perfected AltoLixoCais
cais_block = '''
[node name="AltoLixoCais" type="Node2D" parent="." unique_id=987654321]
z_index = -12
metadata/land_polygon = PackedVector2Array(-140, 120, -130, 128, -73, 166, -18, 198, 38, 238, 94, 284, 138, 335, 146, 385, 148, 428, 360, 428, 360, 140, 100, 140, -140, 120)

[node name="Paving" type="Node2D" parent="AltoLixoCais" unique_id=987654322]
z_index = -2

[node name="@Sprite2D@cais_found_blend_1" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654360]
modulate = Color(0.82, 0.76, 0.65, 0.85)
position = Vector2(250, 165)
scale = Vector2(0.48, 0.42)
texture = ExtResource("23_lu0vc")

[node name="@Sprite2D@cais_found_blend_2" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654361]
modulate = Color(0.82, 0.76, 0.65, 0.85)
position = Vector2(280, 215)
scale = Vector2(0.48, 0.42)
texture = ExtResource("23_lu0vc")

[node name="@Sprite2D@cais_found_blend_3" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654362]
modulate = Color(0.82, 0.76, 0.65, 0.85)
position = Vector2(295, 275)
scale = Vector2(0.48, 0.42)
texture = ExtResource("23_lu0vc")

[node name="@Sprite2D@cais_dirt_1" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654323]
modulate = Color(0.85, 0.78, 0.62, 0.7)
position = Vector2(40, 185)
scale = Vector2(0.55, 0.45)
texture = ExtResource("25_ritys")

[node name="@Sprite2D@cais_dirt_2" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654324]
modulate = Color(0.85, 0.78, 0.62, 0.7)
position = Vector2(110, 225)
scale = Vector2(0.55, 0.45)
texture = ExtResource("25_ritys")

[node name="@Sprite2D@cais_dirt_3" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654325]
modulate = Color(0.85, 0.78, 0.62, 0.7)
position = Vector2(175, 275)
scale = Vector2(0.55, 0.45)
texture = ExtResource("25_ritys")

[node name="@Sprite2D@cais_dirt_4" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654326]
modulate = Color(0.85, 0.78, 0.62, 0.7)
position = Vector2(230, 220)
scale = Vector2(0.55, 0.45)
texture = ExtResource("25_ritys")

[node name="@Sprite2D@cais_dirt_5" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654327]
modulate = Color(0.85, 0.78, 0.62, 0.7)
position = Vector2(235, 320)
scale = Vector2(0.55, 0.45)
texture = ExtResource("25_ritys")

[node name="@Sprite2D@cais_dirt_6" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654363]
modulate = Color(0.85, 0.78, 0.62, 0.7)
position = Vector2(180, 365)
scale = Vector2(0.55, 0.45)
texture = ExtResource("25_ritys")

[node name="@Sprite2D@cais_found_1" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654328]
position = Vector2(60, 215)
scale = Vector2(0.38, 0.38)
texture = ExtResource("23_lu0vc")

[node name="@Sprite2D@cais_found_2" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654329]
position = Vector2(135, 275)
scale = Vector2(0.38, 0.38)
texture = ExtResource("23_lu0vc")

[node name="@Sprite2D@cais_metal_1" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654330]
position = Vector2(90, 235)
scale = Vector2(0.3, 0.26)
texture = ExtResource("24_lm37y")

[node name="@Sprite2D@cais_metal_2" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654331]
position = Vector2(170, 310)
scale = Vector2(0.3, 0.26)
texture = ExtResource("24_lm37y")

[node name="@Sprite2D@cais_walk_0" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654364]
position = Vector2(-95, 145)
rotation = 0.52
scale = Vector2(0.35, 0.32)
texture = ExtResource("28_f3eo0")

[node name="@Sprite2D@cais_walk_1" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654332]
position = Vector2(-38, 182)
rotation = 0.52
scale = Vector2(0.35, 0.32)
texture = ExtResource("28_f3eo0")

[node name="@Sprite2D@cais_walk_2" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654333]
position = Vector2(25, 222)
rotation = 0.62
scale = Vector2(0.35, 0.32)
texture = ExtResource("28_f3eo0")

[node name="@Sprite2D@cais_walk_3" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654334]
position = Vector2(85, 268)
rotation = 0.72
scale = Vector2(0.35, 0.32)
texture = ExtResource("28_f3eo0")

[node name="@Sprite2D@cais_walk_4" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654335]
position = Vector2(132, 320)
rotation = 0.88
scale = Vector2(0.35, 0.32)
texture = ExtResource("28_f3eo0")

[node name="@Sprite2D@cais_walk_5" type="Sprite2D" parent="AltoLixoCais/Paving" unique_id=987654365]
position = Vector2(150, 385)
rotation = 1.35
scale = Vector2(0.35, 0.32)
texture = ExtResource("28_f3eo0")

[node name="RetainingWalls" type="Node2D" parent="AltoLixoCais" unique_id=987654336]
z_index = 1

[node name="@Sprite2D@cais_sh_0" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654366]
modulate = Color(0, 0, 0, 0.65)
position = Vector2(-102, 155)
scale = Vector2(0.55, 0.18)
texture = ExtResource("7_xcrs8")

[node name="@Sprite2D@cais_sh_1" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654337]
modulate = Color(0, 0, 0, 0.65)
position = Vector2(-42, 194)
scale = Vector2(0.55, 0.18)
texture = ExtResource("7_xcrs8")

[node name="@Sprite2D@cais_sh_2" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654338]
modulate = Color(0, 0, 0, 0.65)
position = Vector2(18, 236)
scale = Vector2(0.55, 0.18)
texture = ExtResource("7_xcrs8")

[node name="@Sprite2D@cais_sh_3" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654339]
modulate = Color(0, 0, 0, 0.65)
position = Vector2(78, 282)
scale = Vector2(0.55, 0.18)
texture = ExtResource("7_xcrs8")

[node name="@Sprite2D@cais_sh_4" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654340]
modulate = Color(0, 0, 0, 0.65)
position = Vector2(125, 335)
scale = Vector2(0.55, 0.18)
texture = ExtResource("7_xcrs8")

[node name="@Sprite2D@cais_sh_5" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654367]
modulate = Color(0, 0, 0, 0.65)
position = Vector2(142, 395)
scale = Vector2(0.55, 0.18)
texture = ExtResource("7_xcrs8")

[node name="@Sprite2D@cais_wall_0" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654368]
position = Vector2(-102, 145)
rotation = 0.52
scale = Vector2(0.35, 0.48)
texture = ExtResource("46_ohgu8")

[node name="@Sprite2D@cais_wall_1" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654341]
position = Vector2(-42, 185)
rotation = 0.52
scale = Vector2(0.35, 0.48)
texture = ExtResource("46_ohgu8")

[node name="@Sprite2D@cais_wall_2" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654342]
position = Vector2(18, 226)
rotation = 0.62
scale = Vector2(0.35, 0.48)
texture = ExtResource("46_ohgu8")

[node name="@Sprite2D@cais_wall_3" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654343]
position = Vector2(78, 272)
rotation = 0.72
scale = Vector2(0.35, 0.48)
texture = ExtResource("46_ohgu8")

[node name="@Sprite2D@cais_wall_4" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654344]
position = Vector2(125, 325)
rotation = 0.88
scale = Vector2(0.35, 0.48)
texture = ExtResource("46_ohgu8")

[node name="@Sprite2D@cais_wall_5" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654369]
position = Vector2(142, 385)
rotation = 1.35
scale = Vector2(0.35, 0.48)
texture = ExtResource("46_ohgu8")

[node name="@Sprite2D@cais_edge_0" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654370]
position = Vector2(-102, 137)
rotation = 0.52
scale = Vector2(0.38, 0.35)
texture = ExtResource("27_jyysc")

[node name="@Sprite2D@cais_edge_1" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654345]
position = Vector2(-42, 175)
rotation = 0.52
scale = Vector2(0.38, 0.35)
texture = ExtResource("27_jyysc")

[node name="@Sprite2D@cais_edge_2" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654346]
position = Vector2(18, 216)
rotation = 0.62
scale = Vector2(0.38, 0.35)
texture = ExtResource("27_jyysc")

[node name="@Sprite2D@cais_edge_3" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654347]
position = Vector2(78, 262)
rotation = 0.72
scale = Vector2(0.38, 0.35)
texture = ExtResource("27_jyysc")

[node name="@Sprite2D@cais_edge_4" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654348]
position = Vector2(125, 315)
rotation = 0.88
scale = Vector2(0.38, 0.35)
texture = ExtResource("27_jyysc")

[node name="@Sprite2D@cais_edge_5" type="Sprite2D" parent="AltoLixoCais/RetainingWalls" unique_id=987654371]
position = Vector2(142, 375)
rotation = 1.35
scale = Vector2(0.38, 0.35)
texture = ExtResource("27_jyysc")

[node name="Props" type="Node2D" parent="AltoLixoCais" unique_id=987654349]
z_index = 3

[node name="@Sprite2D@cais_lamp_1" type="Sprite2D" parent="AltoLixoCais/Props" unique_id=987654350]
position = Vector2(-28, 170)
scale = Vector2(0.32, 0.35)
texture = ExtResource("19_v1cvy")

[node name="@PointLight2D@cais_light_1" type="PointLight2D" parent="AltoLixoCais/Props" unique_id=987654351]
position = Vector2(-28, 158)
color = Color(0.88, 0.64, 0.32, 1)
energy = 0.42
texture = ExtResource("7_xcrs8")
texture_scale = 0.38

[node name="@Sprite2D@cais_lamp_2" type="Sprite2D" parent="AltoLixoCais/Props" unique_id=987654352]
position = Vector2(115, 252)
scale = Vector2(0.32, 0.35)
texture = ExtResource("19_v1cvy")

[node name="@PointLight2D@cais_light_2" type="PointLight2D" parent="AltoLixoCais/Props" unique_id=987654353]
position = Vector2(115, 240)
color = Color(0.88, 0.64, 0.32, 1)
energy = 0.42
texture = ExtResource("7_xcrs8")
texture_scale = 0.38

[node name="@Sprite2D@cais_bollard_1" type="Sprite2D" parent="AltoLixoCais/Props" unique_id=987654354]
position = Vector2(10, 210)
scale = Vector2(0.18, 0.18)
texture = ExtResource("15_dbypa")

[node name="@Sprite2D@cais_bollard_2" type="Sprite2D" parent="AltoLixoCais/Props" unique_id=987654355]
position = Vector2(70, 255)
scale = Vector2(0.18, 0.18)
texture = ExtResource("15_dbypa")

[node name="@Sprite2D@cais_crate" type="Sprite2D" parent="AltoLixoCais/Props" unique_id=987654356]
position = Vector2(32, 142)
scale = Vector2(0.22, 0.22)
texture = ExtResource("14_870px")

[node name="@Sprite2D@cais_barrel" type="Sprite2D" parent="AltoLixoCais/Props" unique_id=987654357]
position = Vector2(46, 145)
scale = Vector2(0.2, 0.2)
texture = ExtResource("13_3wu5b")

[node name="@Sprite2D@cais_pipe" type="Sprite2D" parent="AltoLixoCais/Props" unique_id=987654358]
position = Vector2(68, 140)
scale = Vector2(0.25, 0.25)
texture = ExtResource("5_fo6ws")
'''

target_pos = content.find('[node name="GoblinIndustrialQuay"')
assert target_pos != -1, "GoblinIndustrialQuay not found!"
content = content[:target_pos] + cais_block + "\n" + content[target_pos:]

with open('maps/sucateia/sucateia.tscn', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated sucateia.tscn with refined cais and complete connection!")
