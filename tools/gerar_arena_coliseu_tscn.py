"""Gerador da cena oficial ArenaColiseu.tscn (Fase 1E - Versão Corrigida e Robusta).
Atende exatamente às correções do usuário:
  1. Piso do fosso robusto e antigo unificado (arena_piso_fosso_completo_robusto_v1.png sem magenta).
  2. Nova arquibancada norte construída com blocos de pedra entalhada e pranchas maciças.
  3. Hall de entrada e portal perfeitamente emoldurados na alvenaria com service_arch.
  4. Pavimentação completa do piso do hall de entrada (3600 a 3800).
"""
import os

OUT_STANDALONE = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\ArenaColiseu.tscn"
OUT_ROOT       = r"c:\Users\Usuario\Documents\jogo\scenes\ArenaColiseu.tscn"

SCENE_CONTENT = """[gd_scene load_steps=42 format=3 uid="uid://arena_coliseu_fundo_ferro_v1"]

[ext_resource type="Script" path="res://scripts/arena_coliseu.gd" id="1_arena_script"]
[ext_resource type="Texture2D" path="res://assets/props/arena_grade_reta_x_v1.png" id="2_grade_x"]
[ext_resource type="Texture2D" path="res://assets/props/arena_grade_reta_y_v1.png" id="3_grade_y"]
[ext_resource type="Texture2D" path="res://assets/props/arena_pilar_v1.png" id="4_pilar"]
[ext_resource type="Texture2D" path="res://assets/props/arena_canto_v1.png" id="5_canto"]
[ext_resource type="Texture2D" path="res://assets/props/arena_costela_arco_v1.png" id="6_costela_arco"]
[ext_resource type="Texture2D" path="res://assets/props/arena_costela_espinha_v1.png" id="7_costela_espinha"]
[ext_resource type="Texture2D" path="res://assets/props/arena_portao_lutadores_fechado_v1.png" id="8_portao_fechado"]
[ext_resource type="Texture2D" path="res://assets/props/arena_muro_interno_norte_v1.png" id="9_muro_norte"]
[ext_resource type="Texture2D" path="res://assets/props/arena_muro_borda_topo_x_v1.png" id="10_muro_borda_x"]
[ext_resource type="Texture2D" path="res://assets/props/arena_muro_borda_topo_y_v1.png" id="11_muro_borda_y"]
[ext_resource type="Texture2D" path="res://assets/props/arena_muro_canto_interno_v1.png" id="12_muro_canto"]
[ext_resource type="Texture2D" path="res://assets/props/arena_parapeito_grade_x_v1.png" id="13_parapeito_x"]
[ext_resource type="Texture2D" path="res://assets/props/arena_parapeito_grade_y_v1.png" id="14_parapeito_y"]
[ext_resource type="Texture2D" path="res://assets/props/arena_parapeito_canto_v1.png" id="15_parapeito_canto"]
[ext_resource type="Texture2D" path="res://assets/props/arena_escada_lutadores_v1.png" id="16_escada"]
[ext_resource type="Texture2D" path="res://assets/props/arena_escada_lutadores_v1_sombra.png" id="17_escada_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/arena_galeria_coluna_v1.png" id="18_galeria_coluna"]
[ext_resource type="Texture2D" path="res://assets/props/arena_galeria_arco_v1.png" id="19_galeria_arco"]
[ext_resource type="Texture2D" path="res://assets/props/arena_piso_fosso_completo_robusto_v1.png" id="20_piso_fosso_robusto"]
[ext_resource type="Texture2D" path="res://assets/props/arena_piso_galeria_tabuas_v1.png" id="22_piso_galeria"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_apostas_v1.png" id="23_barraca"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_apostas_v1_sombra.png" id="24_barraca_sombra"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_quadro_odds_v1.png" id="25_quadro_odds"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_cofre_v1.png" id="26_cofre"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_fichas_v1.png" id="27_fichas"]
[ext_resource type="Texture2D" path="res://assets/props/arena_barraca_fila_decal_v1.png" id="28_fila_decal"]
[ext_resource type="Texture2D" path="res://assets/props/arena_plateia_bancada_modulo_v1.png" id="29_bancada"]
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

[node name="PisoArenaRobusto" type="Sprite2D" parent="PisoFosso"]
position = Vector2(4288, 512)
scale = Vector2(0.25, 0.25)
texture = ExtResource("20_piso_fosso_robusto")

[node name="MuroContencao" type="Node2D" parent="."]
z_index = -15

[node name="MuroNorte_0" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4112, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("9_muro_norte")

[node name="MuroNorte_1" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4176, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("9_muro_norte")

[node name="MuroNorte_2" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4240, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("9_muro_norte")

[node name="MuroNorte_3" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4304, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("9_muro_norte")

[node name="MuroNorte_4" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4368, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("9_muro_norte")

[node name="MuroNorte_5" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4432, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("9_muro_norte")

[node name="MuroNorte_6" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4496, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("9_muro_norte")

[node name="BordaSul_0" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4112, 640)
scale = Vector2(0.25, 0.25)
texture = ExtResource("10_muro_borda_x")

[node name="BordaSul_1" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4176, 640)
scale = Vector2(0.25, 0.25)
texture = ExtResource("10_muro_borda_x")

[node name="BordaSul_2" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4240, 640)
scale = Vector2(0.25, 0.25)
texture = ExtResource("10_muro_borda_x")

[node name="BordaSul_4" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4368, 640)
scale = Vector2(0.25, 0.25)
texture = ExtResource("10_muro_borda_x")

[node name="BordaSul_5" type="Sprite2D" parent="MuroContencao"]
position = Vector2(4432, 640)
scale = Vector2(0.25, 0.25)
texture = ExtResource("10_muro_borda_x")

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
position = Vector2(4064, 704)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_1" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4128, 704)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_2" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4192, 704)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_3" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4256, 704)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_4" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4320, 704)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_5" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4384, 704)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_6" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4448, 704)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_7" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4512, 704)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoSul_8" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4576, 704)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoLeste_0" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4576, 384)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoLeste_1" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4576, 448)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoLeste_2" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4576, 512)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoLeste_3" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4576, 576)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="PisoLeste_4" type="Sprite2D" parent="GaleriaNivelAlto/PisoTabuasGaleria"]
position = Vector2(4576, 640)
scale = Vector2(0.25, 0.25)
texture = ExtResource("22_piso_galeria")

[node name="Parapeito" type="Node2D" parent="GaleriaNivelAlto"]

[node name="ParapOeste_0" type="Sprite2D" parent="GaleriaNivelAlto/Parapeito"]
position = Vector2(4032, 416)
scale = Vector2(0.25, 0.25)
texture = ExtResource("14_parapeito_y")

[node name="ParapOeste_1" type="Sprite2D" parent="GaleriaNivelAlto/Parapeito"]
position = Vector2(4032, 480)
scale = Vector2(0.25, 0.25)
texture = ExtResource("14_parapeito_y")

[node name="ParapOeste_2" type="Sprite2D" parent="GaleriaNivelAlto/Parapeito"]
position = Vector2(4032, 544)
scale = Vector2(0.25, 0.25)
texture = ExtResource("14_parapeito_y")

[node name="ParapOeste_3" type="Sprite2D" parent="GaleriaNivelAlto/Parapeito"]
position = Vector2(4032, 608)
scale = Vector2(0.25, 0.25)
texture = ExtResource("14_parapeito_y")

[node name="ParapSul_0" type="Sprite2D" parent="GaleriaNivelAlto/Parapeito"]
position = Vector2(4096, 672)
scale = Vector2(0.25, 0.25)
texture = ExtResource("13_parapeito_x")

[node name="ParapSul_1" type="Sprite2D" parent="GaleriaNivelAlto/Parapeito"]
position = Vector2(4160, 672)
scale = Vector2(0.25, 0.25)
texture = ExtResource("13_parapeito_x")

[node name="ParapSul_2" type="Sprite2D" parent="GaleriaNivelAlto/Parapeito"]
position = Vector2(4224, 672)
scale = Vector2(0.25, 0.25)
texture = ExtResource("13_parapeito_x")

[node name="ParapSul_3" type="Sprite2D" parent="GaleriaNivelAlto/Parapeito"]
position = Vector2(4352, 672)
scale = Vector2(0.25, 0.25)
texture = ExtResource("13_parapeito_x")

[node name="ParapSul_4" type="Sprite2D" parent="GaleriaNivelAlto/Parapeito"]
position = Vector2(4416, 672)
scale = Vector2(0.25, 0.25)
texture = ExtResource("13_parapeito_x")

[node name="ParapSul_5" type="Sprite2D" parent="GaleriaNivelAlto/Parapeito"]
position = Vector2(4480, 672)
scale = Vector2(0.25, 0.25)
texture = ExtResource("13_parapeito_x")

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
position = Vector2(4656, 512)

[node name="SpriteCamarote" type="Sprite2D" parent="GaleriaNivelAlto/CamaroteVIP"]
scale = Vector2(0.25, 0.25)
texture = ExtResource("30_camarote")

[node name="CasaControle" type="Node2D" parent="GaleriaNivelAlto"]
position = Vector2(4672, 272)

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

[node name="PlateiaBancadas" type="Node2D" parent="."]
position = Vector2(3968, 240)

[node name="Bancada_0" type="Sprite2D" parent="PlateiaBancadas"]
position = Vector2(32, 0)
scale = Vector2(0.25, 0.25)
texture = ExtResource("29_bancada")

[node name="Bancada_1" type="Sprite2D" parent="PlateiaBancadas"]
position = Vector2(96, 0)
scale = Vector2(0.25, 0.25)
texture = ExtResource("29_bancada")

[node name="Bancada_2" type="Sprite2D" parent="PlateiaBancadas"]
position = Vector2(160, 0)
scale = Vector2(0.25, 0.25)
texture = ExtResource("29_bancada")

[node name="Bancada_3" type="Sprite2D" parent="PlateiaBancadas"]
position = Vector2(224, 0)
scale = Vector2(0.25, 0.25)
texture = ExtResource("29_bancada")

[node name="Bancada_4" type="Sprite2D" parent="PlateiaBancadas"]
position = Vector2(288, 0)
scale = Vector2(0.25, 0.25)
texture = ExtResource("29_bancada")

[node name="Bancada_5" type="Sprite2D" parent="PlateiaBancadas"]
position = Vector2(352, 0)
scale = Vector2(0.25, 0.25)
texture = ExtResource("29_bancada")

[node name="Bancada_6" type="Sprite2D" parent="PlateiaBancadas"]
position = Vector2(416, 0)
scale = Vector2(0.25, 0.25)
texture = ExtResource("29_bancada")

[node name="Bancada_7" type="Sprite2D" parent="PlateiaBancadas"]
position = Vector2(480, 0)
scale = Vector2(0.25, 0.25)
texture = ExtResource("29_bancada")

[node name="Bancada_8" type="Sprite2D" parent="PlateiaBancadas"]
position = Vector2(544, 0)
scale = Vector2(0.25, 0.25)
texture = ExtResource("29_bancada")

[node name="Bancada_9" type="Sprite2D" parent="PlateiaBancadas"]
position = Vector2(608, 0)
scale = Vector2(0.25, 0.25)
texture = ExtResource("29_bancada")

[node name="CorredorServicoSul" type="Node2D" parent="."]

[node name="Coluna_0" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(3968, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_0" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4008, 696)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_1" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4048, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_1" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4088, 696)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_2" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4128, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_2" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4168, 696)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_3" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4208, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_3" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4248, 696)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_4" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4288, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_4" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4328, 696)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_5" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4368, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_5" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4408, 696)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_6" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4448, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="Arco_6" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4488, 696)
scale = Vector2(0.25, 0.25)
texture = ExtResource("19_galeria_arco")

[node name="Coluna_7" type="Sprite2D" parent="CorredorServicoSul"]
position = Vector2(4528, 728)
scale = Vector2(0.25, 0.25)
texture = ExtResource("18_galeria_coluna")

[node name="EscadaLutadores" type="Node2D" parent="."]
position = Vector2(4016, 776)

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

[node name="RedomaGrades" type="Node2D" parent="."]
y_sort_enabled = true

[node name="GradeNorte" type="Node2D" parent="RedomaGrades"]
position = Vector2(0, 384)

[node name="Sec_0" type="Sprite2D" parent="RedomaGrades/GradeNorte"]
position = Vector2(4096, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_1" type="Sprite2D" parent="RedomaGrades/GradeNorte"]
position = Vector2(4160, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_2" type="Sprite2D" parent="RedomaGrades/GradeNorte"]
position = Vector2(4224, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_3" type="Sprite2D" parent="RedomaGrades/GradeNorte"]
position = Vector2(4288, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_4" type="Sprite2D" parent="RedomaGrades/GradeNorte"]
position = Vector2(4352, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_5" type="Sprite2D" parent="RedomaGrades/GradeNorte"]
position = Vector2(4416, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_6" type="Sprite2D" parent="RedomaGrades/GradeNorte"]
position = Vector2(4480, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="GradeOeste" type="Node2D" parent="RedomaGrades"]
position = Vector2(4064, 0)

[node name="Sec_0" type="Sprite2D" parent="RedomaGrades/GradeOeste"]
position = Vector2(0, 416)
scale = Vector2(0.25, 0.25)
texture = ExtResource("3_grade_y")

[node name="Sec_1" type="Sprite2D" parent="RedomaGrades/GradeOeste"]
position = Vector2(0, 480)
scale = Vector2(0.25, 0.25)
texture = ExtResource("3_grade_y")

[node name="Sec_2" type="Sprite2D" parent="RedomaGrades/GradeOeste"]
position = Vector2(0, 544)
scale = Vector2(0.25, 0.25)
texture = ExtResource("3_grade_y")

[node name="Sec_3" type="Sprite2D" parent="RedomaGrades/GradeOeste"]
position = Vector2(0, 608)
scale = Vector2(0.25, 0.25)
texture = ExtResource("3_grade_y")

[node name="GradeLeste" type="Node2D" parent="RedomaGrades"]
position = Vector2(4512, 0)

[node name="Sec_0" type="Sprite2D" parent="RedomaGrades/GradeLeste"]
position = Vector2(0, 416)
scale = Vector2(0.25, 0.25)
texture = ExtResource("3_grade_y")

[node name="Sec_1" type="Sprite2D" parent="RedomaGrades/GradeLeste"]
position = Vector2(0, 480)
scale = Vector2(0.25, 0.25)
texture = ExtResource("3_grade_y")

[node name="Sec_2" type="Sprite2D" parent="RedomaGrades/GradeLeste"]
position = Vector2(0, 544)
scale = Vector2(0.25, 0.25)
texture = ExtResource("3_grade_y")

[node name="Sec_3" type="Sprite2D" parent="RedomaGrades/GradeLeste"]
position = Vector2(0, 608)
scale = Vector2(0.25, 0.25)
texture = ExtResource("3_grade_y")

[node name="GradeSul" type="Node2D" parent="RedomaGrades"]
position = Vector2(0, 640)

[node name="Sec_0" type="Sprite2D" parent="RedomaGrades/GradeSul"]
position = Vector2(4096, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_1" type="Sprite2D" parent="RedomaGrades/GradeSul"]
position = Vector2(4160, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_2" type="Sprite2D" parent="RedomaGrades/GradeSul"]
position = Vector2(4224, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_4" type="Sprite2D" parent="RedomaGrades/GradeSul"]
position = Vector2(4352, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_5" type="Sprite2D" parent="RedomaGrades/GradeSul"]
position = Vector2(4416, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="Sec_6" type="Sprite2D" parent="RedomaGrades/GradeSul"]
position = Vector2(4480, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("2_grade_x")

[node name="PortaoLutadores" type="Node2D" parent="RedomaGrades"]
position = Vector2(4256, 640)

[node name="SpritePortao" type="Sprite2D" parent="RedomaGrades/PortaoLutadores"]
position = Vector2(64, -20)
scale = Vector2(0.25, 0.25)
texture = ExtResource("8_portao_fechado")

[node name="Pilares" type="Node2D" parent="RedomaGrades"]

[node name="CantoNO" type="Sprite2D" parent="RedomaGrades/Pilares"]
position = Vector2(4064, 376)
scale = Vector2(0.25, 0.25)
texture = ExtResource("5_canto")

[node name="CantoNE" type="Sprite2D" parent="RedomaGrades/Pilares"]
position = Vector2(4512, 376)
scale = Vector2(0.25, 0.25)
texture = ExtResource("5_canto")

[node name="CantoSE" type="Sprite2D" parent="RedomaGrades/Pilares"]
position = Vector2(4512, 632)
scale = Vector2(0.25, 0.25)
texture = ExtResource("5_canto")

[node name="CantoSO" type="Sprite2D" parent="RedomaGrades/Pilares"]
position = Vector2(4064, 632)
scale = Vector2(0.25, 0.25)
texture = ExtResource("5_canto")

[node name="Pilar_1_0" type="Sprite2D" parent="RedomaGrades/Pilares"]
position = Vector2(4128, 376)
scale = Vector2(0.25, 0.25)
texture = ExtResource("4_pilar")

[node name="Pilar_2_0" type="Sprite2D" parent="RedomaGrades/Pilares"]
position = Vector2(4192, 376)
scale = Vector2(0.25, 0.25)
texture = ExtResource("4_pilar")

[node name="Pilar_3_0" type="Sprite2D" parent="RedomaGrades/Pilares"]
position = Vector2(4256, 376)
scale = Vector2(0.25, 0.25)
texture = ExtResource("4_pilar")

[node name="Pilar_4_0" type="Sprite2D" parent="RedomaGrades/Pilares"]
position = Vector2(4320, 376)
scale = Vector2(0.25, 0.25)
texture = ExtResource("4_pilar")

[node name="Pilar_5_0" type="Sprite2D" parent="RedomaGrades/Pilares"]
position = Vector2(4384, 376)
scale = Vector2(0.25, 0.25)
texture = ExtResource("4_pilar")

[node name="Pilar_6_0" type="Sprite2D" parent="RedomaGrades/Pilares"]
position = Vector2(4448, 376)
scale = Vector2(0.25, 0.25)
texture = ExtResource("4_pilar")

[node name="Costelas" type="Node2D" parent="RedomaGrades"]
z_index = 10

[node name="ArcoTrans_0" type="Sprite2D" parent="RedomaGrades/Costelas"]
position = Vector2(4192, 512)
scale = Vector2(0.25, 0.25)
texture = ExtResource("6_costela_arco")

[node name="ArcoTrans_1" type="Sprite2D" parent="RedomaGrades/Costelas"]
position = Vector2(4320, 512)
scale = Vector2(0.25, 0.25)
texture = ExtResource("6_costela_arco")

[node name="ArcoTrans_2" type="Sprite2D" parent="RedomaGrades/Costelas"]
position = Vector2(4448, 512)
scale = Vector2(0.25, 0.25)
texture = ExtResource("6_costela_arco")

[node name="EspinhaLong_0" type="Sprite2D" parent="RedomaGrades/Costelas"]
position = Vector2(4288, 480)
scale = Vector2(0.25, 0.25)
texture = ExtResource("7_costela_espinha")

[node name="RedesArena" type="Node2D" parent="."]

[node name="ComportaEnchimentoOeste" type="Sprite2D" parent="RedesArena"]
position = Vector2(4048, 512)
scale = Vector2(0.22, 0.22)
texture = ExtResource("35_comporta_inundacao")

[node name="ReatorEletricoNO" type="Sprite2D" parent="RedesArena"]
position = Vector2(4000, 304)
scale = Vector2(0.20, 0.20)
texture = ExtResource("34_reator_eletrodo")

[node name="ReatorEletricoNE" type="Sprite2D" parent="RedesArena"]
position = Vector2(4576, 304)
scale = Vector2(0.20, 0.20)
texture = ExtResource("34_reator_eletrodo")
"""

os.makedirs(os.path.dirname(OUT_STANDALONE), exist_ok=True)
os.makedirs(os.path.dirname(OUT_ROOT), exist_ok=True)

with open(OUT_STANDALONE, "w", encoding="utf-8") as f:
    f.write(SCENE_CONTENT)

with open(OUT_ROOT, "w", encoding="utf-8") as f:
    f.write(SCENE_CONTENT)

print("ArenaColiseu.tscn regerada com sucesso!")
