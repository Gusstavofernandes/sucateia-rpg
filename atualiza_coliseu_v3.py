def update_arena_scene():
    tscn_content = """[gd_scene load_steps=26 format=3 uid="uid://arena_coliseu_fundo_ferro_v1"]

[ext_resource type="Script" path="res://scripts/arena_coliseu.gd" id="1_arena_script"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_norte_v3.png" id="2_coliseu_norte"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_sul_v3.png" id="3_coliseu_sul"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_piso_v3.png" id="4_coliseu_piso"]
[ext_resource type="Texture2D" path="res://assets/props/arena_coliseu_imponente_sombra_v3.png" id="5_coliseu_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/arena_escada_lutadores_v1.png" id="16_escada"]
[ext_resource type="Texture2D" path="res://assets/props/arena_escada_lutadores_v1_sombra.png" id="17_escada_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/arena_galeria_coluna_v1.png" id="18_galeria_coluna"]
[ext_resource type="Texture2D" path="res://assets/props/arena_galeria_arco_v1.png" id="19_galeria_arco"]
[ext_resource type="Texture2D" path="res://assets/props/arena_piso_galeria_tabuas_v1.png" id="22_piso_galeria"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_apostas_v1.png" id="23_barraca"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_apostas_v1_sombra.png" id="24_barraca_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_quadro_odds_v1.png" id="25_quadro_odds"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_cofre_v1.png" id="26_cofre"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_fichas_v1.png" id="27_fichas"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_fila_decal_v1.png" id="28_fila_decal"]
[ext_resource type="Texture2D" path="res://assets/props/arena_plateia_camarote_guarda_corpo_v1.png" id="30_camarote"]
[ext_resource type="Texture2D" path="res://assets/props/arena_controle_mesa_alavancas_v1.png" id="31_mesa_alavancas"]
[ext_resource type="Texture2D" path="res://assets/props/arena_controle_painel_manometros_v1.png" id="32_painel_manometros"]
[ext_resource type="Texture2D" path="res://assets/machines/maquina_caldeira_vapor_v1.png" id="33_caldeira_vapor"]
[ext_resource type="Texture2D" path="res://assets/machines/maquina_reator_eletrodo_arena_v1.png" id="34_reator_eletrodo"]
[ext_resource type="Texture2D" path="res://assets/props/comporta_inundacao_arena_v1.png" id="35_comporta_inundacao"]
[ext_resource type="Texture2D" path="res://assets/props/portao_grade_arena_v1.png" id="36_portao_levadico_hall"]
[ext_resource type="Texture2D" path="res://assets/service_arch.png" id="37_arco_alvenaria"]
[ext_resource type="Texture2D" path="res://assets/parede_norte_ferro.png" id="38_parede_norte_portal"]

[sub_resource type="RectangleShape2D" id="RectangleShape2D_balcao_apostas"]
size = Vector2(80, 48)

[sub_resource type="RectangleShape2D" id="RectangleShape2D_escada"]
size = Vector2(64, 80)

[node name="ArenaColiseu" type="Node2D"]
y_sort_enabled = true
script = ExtResource("1_arena_script")

[node name="HallEntrada" type="Node2D" parent="."]

[node name="PisoHall_0" type="Sprite2D" parent="HallEntrada"]
z_index = -12
position = Vector2(3632, 320)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoHall_1" type="Sprite2D" parent="HallEntrada"]
z_index = -12
position = Vector2(3696, 320)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoHall_2" type="Sprite2D" parent="HallEntrada"]
z_index = -12
position = Vector2(3760, 320)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoHall_3" type="Sprite2D" parent="HallEntrada"]
z_index = -12
position = Vector2(3632, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoHall_4" type="Sprite2D" parent="HallEntrada"]
z_index = -12
position = Vector2(3696, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoHall_5" type="Sprite2D" parent="HallEntrada"]
z_index = -12
position = Vector2(3760, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="ParedeMuralhaNorteHall" type="Sprite2D" parent="HallEntrada"]
position = Vector2(3600, 215)
scale = Vector2(0.40, 0.40)
texture = ExtResource("38_parede_norte_portal")

[node name="ArcoEntrada" type="Sprite2D" parent="HallEntrada"]
position = Vector2(3600, 260)
scale = Vector2(0.52, 0.52)
texture = ExtResource("37_arco_alvenaria")

[node name="PortaoLevadico" type="Sprite2D" parent="HallEntrada"]
position = Vector2(3600, 350)
scale = Vector2(0.22, 0.22)
texture = ExtResource("36_portao_levadico_hall")

[node name="PisoFosso" type="Node2D" parent="."]
z_index = -20

[node name="PisoFossoRebaixado" type="Sprite2D" parent="PisoFosso"]
position = Vector2(4384, 520)
scale = Vector2(0.512, 0.512)
texture = ExtResource("4_coliseu_piso")

[node name="SombraFossoProfundo" type="Sprite2D" parent="PisoFosso"]
z_index = 2
position = Vector2(4384, 520)
scale = Vector2(0.512, 0.512)
texture = ExtResource("5_coliseu_sombra")

[node name="ArquibancadaMeiaLuaNorte" type="Sprite2D" parent="."]
z_index = -15
position = Vector2(4384, 520)
scale = Vector2(0.512, 0.512)
texture = ExtResource("2_coliseu_norte")

[node name="MuralhaSulArredondada" type="Sprite2D" parent="."]
z_index = 0
y_sort_enabled = true
position = Vector2(4384, 520)
scale = Vector2(0.512, 0.512)
texture = ExtResource("3_coliseu_sul")

[node name="GaleriaNivelAlto" type="Node2D" parent="."]
y_sort_enabled = true

[node name="PisoTabuasGaleria" type="Node2D" parent="GaleriaNivelAlto"]
z_index = -12

[node name="PisoOeste_0" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4000, 320)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoOeste_1" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4000, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoOeste_2" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4000, 448)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoOeste_3" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4000, 512)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoOeste_4" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4000, 576)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoOeste_5" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4000, 640)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoOeste_6" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4000, 704)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_0" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4064, 736)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_1" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4128, 736)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_2" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4192, 736)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_3" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4256, 736)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_4" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4320, 736)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_5" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4384, 736)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_6" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4448, 736)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_7" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4512, 736)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_8" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4576, 736)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="BarracaApostas" type="Node2D" parent="GaleriaNivelAlto"]
position = Vector2(3856, 336)

[node name="FilaDecal" type="Sprite2D" parent="GaleriaNivelAlto/BarracaApostas"]
position = Vector2(0, 72)
scale = Vector2(0.25, 0.25)
texture = ExtResource("28_fila_decal")

[node name="SombraBarraca" type="Sprite2D" parent="GaleriaNivelAlto/BarracaApostas"]
z_index = -3
position = Vector2(0, 10)
scale = Vector2(0.25, 0.25)
texture = ExtResource("24_barraca_sombra")

[node name="SpriteBarraca" type="Sprite2D" parent="GaleriaNivelAlto/BarracaApostas"]
scale = Vector2(0.25, 0.25)
texture = ExtResource("23_barraca")

[node name="QuadroOdds" type="Node2D" parent="GaleriaNivelAlto/BarracaApostas"]
position = Vector2(60, -10)
scale = Vector2(0.25, 0.25)

[node name="SpriteQuadro" type="Sprite2D" parent="GaleriaNivelAlto/BarracaApostas/QuadroOdds"]
texture = ExtResource("25_quadro_odds")

[node name="LabelOdd1" type="Label" parent="GaleriaNivelAlto/BarracaApostas/QuadroOdds"]
offset_left = -46.0
offset_top = -40.0
offset_right = 46.0
offset_bottom = -24.0
theme_override_font_sizes/font_size = 11
text = "G.FERRO  x 1.85"
horizontal_alignment = 1

[node name="LabelOdd2" type="Label" parent="GaleriaNivelAlto/BarracaApostas/QuadroOdds"]
offset_left = -46.0
offset_top = -16.0
offset_right = 46.0
offset_bottom = 0.0
theme_override_font_sizes/font_size = 11
text = "ESCAVAD. x 2.40"
horizontal_alignment = 1

[node name="LabelOdd3" type="Label" parent="GaleriaNivelAlto/BarracaApostas/QuadroOdds"]
offset_left = -46.0
offset_top = 8.0
offset_right = 46.0
offset_bottom = 24.0
theme_override_font_sizes/font_size = 11
text = "SUCATA   x 3.75"
horizontal_alignment = 1

[node name="LabelOdd4" type="Label" parent="GaleriaNivelAlto/BarracaApostas/QuadroOdds"]
offset_left = -46.0
offset_top = 32.0
offset_right = 46.0
offset_bottom = 48.0
theme_override_font_sizes/font_size = 11
text = "COLOSSO  x 6.00"
horizontal_alignment = 1

[node name="Cofre" type="Sprite2D" parent="GaleriaNivelAlto/BarracaApostas"]
position = Vector2(-36, 24)
scale = Vector2(0.25, 0.25)
texture = ExtResource("26_cofre")

[node name="Fichas" type="Sprite2D" parent="GaleriaNivelAlto/BarracaApostas"]
position = Vector2(-20, 28)
scale = Vector2(0.25, 0.25)
texture = ExtResource("27_fichas")

[node name="StaticBody2D" type="StaticBody2D" parent="GaleriaNivelAlto/BarracaApostas"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="GaleriaNivelAlto/BarracaApostas/StaticBody2D"]
position = Vector2(0, 8)
shape = SubResource("RectangleShape2D_balcao_apostas")

[node name="CamaroteVIP" type="Node2D" parent="GaleriaNivelAlto"]
position = Vector2(4790, 520)

[node name="SpriteCamarote" type="Sprite2D" parent="GaleriaNivelAlto/CamaroteVIP"]
scale = Vector2(0.25, 0.25)
texture = ExtResource("30_camarote")

[node name="CasaControle" type="Node2D" parent="GaleriaNivelAlto"]
position = Vector2(4780, 272)

[node name="PainelManometros" type="Sprite2D" parent="GaleriaNivelAlto/CasaControle"]
position = Vector2(0, -32)
scale = Vector2(0.25, 0.25)
texture = ExtResource("32_painel_manometros")

[node name="MesaAlavancas" type="Sprite2D" parent="GaleriaNivelAlto/CasaControle"]
position = Vector2(0, 16)
scale = Vector2(0.25, 0.25)
texture = ExtResource("31_mesa_alavancas")

[node name="CaldeiraVapor" type="Sprite2D" parent="GaleriaNivelAlto/CasaControle"]
position = Vector2(-48, 10)
scale = Vector2(0.20, 0.20)
texture = ExtResource("33_caldeira_vapor")

[node name="CorredorServicoSul" type="Node2D" parent="."]

[node name="Coluna_0" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(3968, 760)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_0" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4008, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_1" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4048, 760)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_1" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4088, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_2" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4128, 760)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_2" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4168, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_3" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4208, 760)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_3" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4248, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_4" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4288, 760)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_4" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4328, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_5" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4368, 760)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_5" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4408, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_6" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4448, 760)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_6" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4488, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_7" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4528, 760)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="EscadaLutadores" type="Node2D" parent="."]
position = Vector2(4016, 800)

[node name="Sombra" type="Sprite2D" parent="EscadaLutadores"]
z_index = -3
scale = Vector2(0.25, 0.25)
texture = ExtResource("17_escada_sombra")

[node name="SpriteEscada" type="Sprite2D" parent="EscadaLutadores"]
scale = Vector2(0.25, 0.25)
texture = ExtResource("16_escada")

[node name="StaticBody2D" type="StaticBody2D" parent="EscadaLutadores"]

[node name="CollisionShape2D" type="CollisionShape2D" parent="EscadaLutadores/StaticBody2D"]
shape = SubResource("RectangleShape2D_escada")

[node name="RedesArena" type="Node2D" parent="."]

[node name="ComportaEnchimentoOeste" type="Sprite2D" parent="RedesArena"]
position = Vector2(4025, 520)
scale = Vector2(0.22, 0.22)
texture = ExtResource("35_comporta_inundacao")

[node name="ReatorEletricoNO" type="Sprite2D" parent="RedesArena"]
position = Vector2(3980, 270)
scale = Vector2(0.20, 0.20)
texture = ExtResource("34_reator_eletrodo")

[node name="ReatorEletricoNE" type="Sprite2D" parent="RedesArena"]
position = Vector2(4760, 270)
scale = Vector2(0.20, 0.20)
texture = ExtResource("34_reator_eletrodo")
"""
    dest_files = [
        r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\ArenaColiseu.tscn',
        r'c:\Users\Usuario\Documents\jogo\scenes\ArenaColiseu.tscn'
    ]
    for df in dest_files:
        with open(df, "w", encoding="utf-8") as f:
            f.write(tscn_content)
    print("ArenaColiseu.tscn atualizada com o Coliseu Imponente v3 (+60%) e remoção das bancadas antigas!")

update_arena_scene()
