import re
import os

lixao_ext_resources = """[ext_resource type="Texture2D" path="res://assets/props/lixao_montanha_sucata_principal.png" id="ext_lixao_montanha"]
[ext_resource type="Texture2D" path="res://assets/props/lixao_montanha_sucata_principal_sombra.png" id="ext_lixao_montanha_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/lixao_duna_tubos_engrenagens.png" id="ext_lixao_duna"]
[ext_resource type="Texture2D" path="res://assets/props/lixao_duna_tubos_engrenagens_sombra.png" id="ext_lixao_duna_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/lixao_guindaste_eletroima.png" id="ext_lixao_guindaste"]
[ext_resource type="Texture2D" path="res://assets/props/lixao_guindaste_eletroima_sombra.png" id="ext_lixao_guindaste_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/lixao_caixotes_engrenagens.png" id="ext_lixao_caixotes"]
[ext_resource type="Texture2D" path="res://assets/region/scrap_colossus.png" id="ext_lixao_scrap_colossus"]
[ext_resource type="Texture2D" path="res://assets/region/ruined_engine.png" id="ext_lixao_ruined_engine"]
[ext_resource type="Texture2D" path="res://assets/region/wreck_cradle.png" id="ext_lixao_wreck_cradle"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/fundo_abandoned_engine.png" id="ext_lixao_abandoned_engine"]
[ext_resource type="Texture2D" path="res://assets/reconstruction/fundo_sorting_bank.png" id="ext_lixao_sorting_bank"]
[ext_resource type="Texture2D" path="res://assets/region/salvage_ground.png" id="ext_lixao_salvage_ground"]
"""

sub_resources_lixao = """
[sub_resource type="RectangleShape2D" id="RectangleShape2D_lixao_montanha"]
size = Vector2(850, 180)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_lixao_duna"]
size = Vector2(950, 160)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_lixao_guindaste"]
size = Vector2(180, 140)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_lixao_colossus"]
size = Vector2(500, 180)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_lixao_ruined_engine"]
size = Vector2(550, 220)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_lixao_wreck_cradle"]
size = Vector2(400, 150)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_lixao_caixotes"]
size = Vector2(160, 90)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_lixao_sorting"]
size = Vector2(360, 60)
"""

# Let's define the GrandeLixaoDistrict node tree
grande_lixao_district = """
[node name="GrandeLixaoDistrict" type="Node2D" parent="." unique_id=998800001]
y_sort_enabled = true
metadata/district_name = "O Grande Lixão — Campos de Sucata"
metadata/land_polygon = PackedVector2Array(-1700, -1300, 1500, -1300, 1500, -2950, -1700, -2950)

[node name="GroundIntegration" type="Node2D" parent="GrandeLixaoDistrict" unique_id=998800002]
z_index = -35

[node name="ChaoLixaoBase" type="Polygon2D" parent="GrandeLixaoDistrict/GroundIntegration" unique_id=998800003]
color = Color(0.18, 0.14, 0.11, 1)
polygon = PackedVector2Array(-1750, -1280, 1550, -1280, 1550, -3000, -1750, -3000)

[node name="PatchLama1" type="Sprite2D" parent="GrandeLixaoDistrict/GroundIntegration" unique_id=998800004]
modulate = Color(0.85, 0.75, 0.60, 0.70)
position = Vector2(100, -1600)
scale = Vector2(1.8, 1.8)
texture = ExtResource("ext_lixao_salvage_ground")

[node name="PatchLama2" type="Sprite2D" parent="GrandeLixaoDistrict/GroundIntegration" unique_id=998800005]
modulate = Color(0.80, 0.70, 0.55, 0.70)
position = Vector2(-600, -2000)
scale = Vector2(2.0, 2.0)
texture = ExtResource("ext_lixao_salvage_ground")

[node name="PatchLama3" type="Sprite2D" parent="GrandeLixaoDistrict/GroundIntegration" unique_id=998800006]
modulate = Color(0.85, 0.75, 0.60, 0.70)
position = Vector2(500, -2400)
scale = Vector2(2.2, 2.2)
texture = ExtResource("ext_lixao_salvage_ground")

[node name="PatchLama4" type="Sprite2D" parent="GrandeLixaoDistrict/GroundIntegration" unique_id=998800007]
modulate = Color(0.75, 0.65, 0.50, 0.70)
position = Vector2(-800, -2600)
scale = Vector2(2.0, 2.0)
texture = ExtResource("ext_lixao_salvage_ground")

[node name="ScrapMounds" type="Node2D" parent="GrandeLixaoDistrict" unique_id=998800010]
y_sort_enabled = true

[node name="MontanhaSucata_Oeste1" type="Node2D" parent="GrandeLixaoDistrict/ScrapMounds" unique_id=998800011]
y_sort_enabled = true
position = Vector2(-1150, -1850)
scale = Vector2(0.75, 0.75)

[node name="Sombra" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_Oeste1" unique_id=998800012]
z_index = -2
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("ext_lixao_montanha_sombra")
offset = Vector2(0, -430)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_Oeste1" unique_id=998800013]
texture = ExtResource("ext_lixao_montanha")
offset = Vector2(0, -430)

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_Oeste1" unique_id=998800014]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_Oeste1/Colisao" unique_id=998800015]
position = Vector2(0, -30)
shape = SubResource("RectangleShape2D_lixao_montanha")


[node name="DunaTubos_Oeste1" type="Node2D" parent="GrandeLixaoDistrict/ScrapMounds" unique_id=998800016]
y_sort_enabled = true
position = Vector2(-650, -1700)
scale = Vector2(0.65, 0.65)

[node name="Sombra" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Oeste1" unique_id=998800017]
z_index = -2
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("ext_lixao_duna_sombra")
offset = Vector2(0, -360)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Oeste1" unique_id=998800018]
texture = ExtResource("ext_lixao_duna")
offset = Vector2(0, -360)

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Oeste1" unique_id=998800019]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Oeste1/Colisao" unique_id=998800020]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_lixao_duna")


[node name="MontanhaSucata_Oeste2" type="Node2D" parent="GrandeLixaoDistrict/ScrapMounds" unique_id=998800021]
y_sort_enabled = true
position = Vector2(-1250, -2400)
scale = Vector2(-0.70, 0.70)

[node name="Sombra" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_Oeste2" unique_id=998800022]
z_index = -2
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("ext_lixao_montanha_sombra")
offset = Vector2(0, -430)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_Oeste2" unique_id=998800023]
texture = ExtResource("ext_lixao_montanha")
offset = Vector2(0, -430)

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_Oeste2" unique_id=998800024]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_Oeste2/Colisao" unique_id=998800025]
position = Vector2(0, -30)
shape = SubResource("RectangleShape2D_lixao_montanha")


[node name="DunaTubos_Centro2" type="Node2D" parent="GrandeLixaoDistrict/ScrapMounds" unique_id=998800026]
y_sort_enabled = true
position = Vector2(-700, -2250)
scale = Vector2(0.60, 0.60)

[node name="Sombra" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Centro2" unique_id=998800027]
z_index = -2
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("ext_lixao_duna_sombra")
offset = Vector2(0, -360)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Centro2" unique_id=998800028]
texture = ExtResource("ext_lixao_duna")
offset = Vector2(0, -360)

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Centro2" unique_id=998800029]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Centro2/Colisao" unique_id=998800030]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_lixao_duna")


[node name="MontanhaSucata_NorteTop" type="Node2D" parent="GrandeLixaoDistrict/ScrapMounds" unique_id=998800031]
y_sort_enabled = true
position = Vector2(250, -2750)
scale = Vector2(0.85, 0.85)

[node name="Sombra" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_NorteTop" unique_id=998800032]
z_index = -2
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("ext_lixao_montanha_sombra")
offset = Vector2(0, -430)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_NorteTop" unique_id=998800033]
texture = ExtResource("ext_lixao_montanha")
offset = Vector2(0, -430)

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_NorteTop" unique_id=998800034]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/ScrapMounds/MontanhaSucata_NorteTop/Colisao" unique_id=998800035]
position = Vector2(0, -30)
shape = SubResource("RectangleShape2D_lixao_montanha")


[node name="DunaTubos_Leste3" type="Node2D" parent="GrandeLixaoDistrict/ScrapMounds" unique_id=998800036]
y_sort_enabled = true
position = Vector2(1150, -2400)
scale = Vector2(0.60, 0.60)

[node name="Sombra" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Leste3" unique_id=998800037]
z_index = -2
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("ext_lixao_duna_sombra")
offset = Vector2(0, -360)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Leste3" unique_id=998800038]
texture = ExtResource("ext_lixao_duna")
offset = Vector2(0, -360)

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Leste3" unique_id=998800039]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/ScrapMounds/DunaTubos_Leste3/Colisao" unique_id=998800040]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_lixao_duna")


[node name="AncientMachinery" type="Node2D" parent="GrandeLixaoDistrict" unique_id=998800050]
y_sort_enabled = true

[node name="MotorTurbinaAncestral" type="Node2D" parent="GrandeLixaoDistrict/AncientMachinery" unique_id=998800051]
y_sort_enabled = true
position = Vector2(350, -2200)
scale = Vector2(0.65, 0.65)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/AncientMachinery/MotorTurbinaAncestral" unique_id=998800052]
texture = ExtResource("ext_lixao_ruined_engine")
offset = Vector2(0, -360)

[node name="LuzNucleoArcano" type="PointLight2D" parent="GrandeLixaoDistrict/AncientMachinery/MotorTurbinaAncestral" unique_id=998800053]
position = Vector2(-80, -280)
color = Color(0.20, 0.85, 1.0, 1)
energy = 2.4
texture = ExtResource("7_xcrs8")
texture_scale = 1.2

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/AncientMachinery/MotorTurbinaAncestral" unique_id=998800054]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/AncientMachinery/MotorTurbinaAncestral/Colisao" unique_id=998800055]
position = Vector2(0, -40)
shape = SubResource("RectangleShape2D_lixao_ruined_engine")


[node name="ColossoDeSucata" type="Node2D" parent="GrandeLixaoDistrict/AncientMachinery" unique_id=998800056]
y_sort_enabled = true
position = Vector2(950, -2050)
scale = Vector2(0.75, 0.75)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/AncientMachinery/ColossoDeSucata" unique_id=998800057]
texture = ExtResource("ext_lixao_scrap_colossus")
offset = Vector2(0, -280)

[node name="LuzLanternaColosso" type="PointLight2D" parent="GrandeLixaoDistrict/AncientMachinery/ColossoDeSucata" unique_id=998800058]
position = Vector2(60, -220)
color = Color(1.0, 0.65, 0.25, 1)
energy = 1.8
texture = ExtResource("7_xcrs8")
texture_scale = 0.9

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/AncientMachinery/ColossoDeSucata" unique_id=998800059]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/AncientMachinery/ColossoDeSucata/Colisao" unique_id=998800060]
position = Vector2(0, -35)
shape = SubResource("RectangleShape2D_lixao_colossus")


[node name="VaporEncalhadoCradle" type="Node2D" parent="GrandeLixaoDistrict/AncientMachinery" unique_id=998800061]
y_sort_enabled = true
position = Vector2(-120, -2480)
scale = Vector2(0.60, 0.60)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/AncientMachinery/VaporEncalhadoCradle" unique_id=998800062]
texture = ExtResource("ext_lixao_wreck_cradle")
offset = Vector2(0, -260)

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/AncientMachinery/VaporEncalhadoCradle" unique_id=998800063]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/AncientMachinery/VaporEncalhadoCradle/Colisao" unique_id=998800064]
position = Vector2(0, -30)
shape = SubResource("RectangleShape2D_lixao_wreck_cradle")


[node name="ScrapCranes" type="Node2D" parent="GrandeLixaoDistrict" unique_id=998800070]
y_sort_enabled = true

[node name="GuindasteEletroima1" type="Node2D" parent="GrandeLixaoDistrict/ScrapCranes" unique_id=998800071]
y_sort_enabled = true
position = Vector2(-450, -1950)
scale = Vector2(0.55, 0.55)

[node name="Sombra" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapCranes/GuindasteEletroima1" unique_id=998800072]
z_index = -2
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("ext_lixao_guindaste_sombra")
offset = Vector2(0, -560)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapCranes/GuindasteEletroima1" unique_id=998800073]
texture = ExtResource("ext_lixao_guindaste")
offset = Vector2(0, -560)

[node name="LuzCabineGuindaste" type="PointLight2D" parent="GrandeLixaoDistrict/ScrapCranes/GuindasteEletroima1" unique_id=998800074]
position = Vector2(160, -620)
color = Color(1.0, 0.70, 0.30, 1)
energy = 1.9
texture = ExtResource("7_xcrs8")
texture_scale = 0.8

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/ScrapCranes/GuindasteEletroima1" unique_id=998800075]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/ScrapCranes/GuindasteEletroima1/Colisao" unique_id=998800076]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_lixao_guindaste")


[node name="GuindasteEletroima2" type="Node2D" parent="GrandeLixaoDistrict/ScrapCranes" unique_id=998800077]
y_sort_enabled = true
position = Vector2(650, -2400)
scale = Vector2(-0.55, 0.55)

[node name="Sombra" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapCranes/GuindasteEletroima2" unique_id=998800078]
z_index = -2
position = Vector2(10, 15)
scale = Vector2(1.05, 1.05)
texture = ExtResource("ext_lixao_guindaste_sombra")
offset = Vector2(0, -560)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/ScrapCranes/GuindasteEletroima2" unique_id=998800079]
texture = ExtResource("ext_lixao_guindaste")
offset = Vector2(0, -560)

[node name="LuzCabineGuindaste" type="PointLight2D" parent="GrandeLixaoDistrict/ScrapCranes/GuindasteEletroima2" unique_id=998800080]
position = Vector2(160, -620)
color = Color(1.0, 0.70, 0.30, 1)
energy = 1.9
texture = ExtResource("7_xcrs8")
texture_scale = 0.8

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/ScrapCranes/GuindasteEletroima2" unique_id=998800081]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/ScrapCranes/GuindasteEletroima2/Colisao" unique_id=998800082]
position = Vector2(0, -25)
shape = SubResource("RectangleShape2D_lixao_guindaste")


[node name="SalvageStations" type="Node2D" parent="GrandeLixaoDistrict" unique_id=998800090]
y_sort_enabled = true

[node name="BancadaTriagem_Entrada1" type="Node2D" parent="GrandeLixaoDistrict/SalvageStations" unique_id=998800091]
y_sort_enabled = true
position = Vector2(380, -1500)
scale = Vector2(0.26, 0.26)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/SalvageStations/BancadaTriagem_Entrada1" unique_id=998800092]
texture = ExtResource("ext_lixao_sorting_bank")
offset = Vector2(0, -385)

[node name="LuzTriagem" type="PointLight2D" parent="GrandeLixaoDistrict/SalvageStations/BancadaTriagem_Entrada1" unique_id=998800093]
position = Vector2(0, -220)
color = Color(0.95, 0.80, 0.45, 1)
energy = 1.5
texture = ExtResource("7_xcrs8")
texture_scale = 0.6

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/SalvageStations/BancadaTriagem_Entrada1" unique_id=998800094]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/SalvageStations/BancadaTriagem_Entrada1/Colisao" unique_id=998800095]
position = Vector2(0, -20)
shape = SubResource("RectangleShape2D_lixao_sorting")


[node name="BancadaTriagem_Entrada2" type="Node2D" parent="GrandeLixaoDistrict/SalvageStations" unique_id=998800096]
y_sort_enabled = true
position = Vector2(20, -1500)
scale = Vector2(0.26, 0.26)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/SalvageStations/BancadaTriagem_Entrada2" unique_id=998800097]
texture = ExtResource("ext_lixao_sorting_bank")
offset = Vector2(0, -385)

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/SalvageStations/BancadaTriagem_Entrada2" unique_id=998800098]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/SalvageStations/BancadaTriagem_Entrada2/Colisao" unique_id=998800099]
position = Vector2(0, -20)
shape = SubResource("RectangleShape2D_lixao_sorting")


[node name="CaixotesSucata1" type="Node2D" parent="GrandeLixaoDistrict/SalvageStations" unique_id=998800100]
y_sort_enabled = true
position = Vector2(200, -1560)
scale = Vector2(0.22, 0.22)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/SalvageStations/CaixotesSucata1" unique_id=998800101]
texture = ExtResource("ext_lixao_caixotes")
offset = Vector2(0, -450)

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/SalvageStations/CaixotesSucata1" unique_id=998800102]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/SalvageStations/CaixotesSucata1/Colisao" unique_id=998800103]
position = Vector2(0, -20)
shape = SubResource("RectangleShape2D_lixao_caixotes")


[node name="CaixotesSucata2" type="Node2D" parent="GrandeLixaoDistrict/SalvageStations" unique_id=998800104]
y_sort_enabled = true
position = Vector2(-150, -1750)
scale = Vector2(-0.22, 0.22)

[node name="Sprite" type="Sprite2D" parent="GrandeLixaoDistrict/SalvageStations/CaixotesSucata2" unique_id=998800105]
texture = ExtResource("ext_lixao_caixotes")
offset = Vector2(0, -450)

[node name="Colisao" type="StaticBody2D" parent="GrandeLixaoDistrict/SalvageStations/CaixotesSucata2" unique_id=998800106]

[node name="Shape" type="CollisionShape2D" parent="GrandeLixaoDistrict/SalvageStations/CaixotesSucata2/Colisao" unique_id=998800107]
position = Vector2(0, -20)
shape = SubResource("RectangleShape2D_lixao_caixotes")


[node name="AtmosphericLighting" type="Node2D" parent="GrandeLixaoDistrict" unique_id=998800120]

[node name="LuzFogueiraLixao1" type="PointLight2D" parent="GrandeLixaoDistrict/AtmosphericLighting" unique_id=998800121]
position = Vector2(100, -1800)
color = Color(1.0, 0.55, 0.18, 1)
energy = 1.6
texture = ExtResource("7_xcrs8")
texture_scale = 2.0

[node name="LuzFogueiraLixao2" type="PointLight2D" parent="GrandeLixaoDistrict/AtmosphericLighting" unique_id=998800122]
position = Vector2(-200, -2300)
color = Color(1.0, 0.50, 0.15, 1)
energy = 1.8
texture = ExtResource("7_xcrs8")
texture_scale = 2.2

[node name="LuzVerdeQuimica" type="PointLight2D" parent="GrandeLixaoDistrict/AtmosphericLighting" unique_id=998800123]
position = Vector2(800, -2350)
color = Color(0.25, 0.95, 0.40, 1)
energy = 1.7
texture = ExtResource("7_xcrs8")
texture_scale = 1.8
"""

def update_sucateia_scene(file_path):
    print(f"Atualizando {file_path} com o Grande Lixão...")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inserir ext_resources
    if 'ext_lixao_montanha' not in content:
        m = list(re.finditer(r'\[ext_resource[^\]]+\]', content))
        last_ext_end = m[-1].end()
        content = content[:last_ext_end] + "\n" + lixao_ext_resources + content[last_ext_end:]

    # 2. Inserir sub_resources antes de [node name="Sucateia"
    if 'RectangleShape2D_lixao_montanha' not in content:
        m_root = re.search(r'\[node name="Sucateia"', content)
        if m_root:
            root_start = m_root.start()
            content = content[:root_start] + sub_resources_lixao + "\n" + content[root_start:]

    # 3. Inserir GrandeLixaoDistrict
    if 'GrandeLixaoDistrict' not in content:
        # Colocar antes de [node name="AltoLixoDistrict" ou no final
        m_alto = re.search(r'\[node name="AltoLixoDistrict"', content)
        if m_alto:
            alto_start = m_alto.start()
            content = content[:alto_start] + grande_lixao_district + "\n" + content[alto_start:]

    # 4. Inserir RouteMarker para o Grande Lixão
    if 'name="GrandeLixao"' not in content:
        m_markers = re.search(r'\[node name="RouteMarkers"[^\]]*\]', content)
        if m_markers:
            marker_end = m_markers.end()
            marker_text = '\n\n[node name="GrandeLixao" type="Marker2D" parent="RouteMarkers" unique_id=998800130]\nposition = Vector2(200, -1850)'
            content = content[:marker_end] + marker_text + content[marker_end:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Sucesso ao atualizar {file_path}!")

update_sucateia_scene(r'c:\Users\Usuario\Documents\jogo\maps\sucateia\sucateia.tscn')
