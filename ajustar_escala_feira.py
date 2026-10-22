import re

def update_feira_scales():
    path = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replacements for scales and lights
    content = content.replace(
        '''[node name="BarracaApostas_Principal" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3980, 830)
scale = Vector2(0.24, 0.24)''',
        '''[node name="BarracaApostas_Principal" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3950, 840)
scale = Vector2(0.32, 0.32)'''
    )

    content = content.replace(
        '''[node name="LuzLanternaApostas" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Principal"]
position = Vector2(95, -150)
color = Color(1, 0.65, 0.28, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.5''',
        '''[node name="LuzLanternaApostas" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaApostas_Principal"]
position = Vector2(95, -150)
color = Color(1, 0.70, 0.30, 1)
energy = 2.2
texture = SubResource("GradientTexture2D_light")
texture_scale = 6.5'''
    )

    content = content.replace(
        '''[node name="BarracaPecasRaras" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3440, 890)
scale = Vector2(0.25, 0.25)''',
        '''[node name="BarracaPecasRaras" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3420, 890)
scale = Vector2(0.33, 0.33)'''
    )

    content = content.replace(
        '''[node name="LuzCristaisArcanos" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaPecasRaras"]
position = Vector2(-30, -180)
color = Color(0.2, 0.9, 0.95, 1)
energy = 2.2
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.2

[node name="LuzLanternaBanca" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaPecasRaras"]
position = Vector2(250, -380)
color = Color(1, 0.72, 0.35, 1)
energy = 1.6
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.8''',
        '''[node name="LuzCristaisArcanos" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaPecasRaras"]
position = Vector2(-30, -180)
color = Color(0.25, 1.0, 1.0, 1)
energy = 2.6
texture = SubResource("GradientTexture2D_light")
texture_scale = 5.8

[node name="LuzLanternaBanca" type="PointLight2D" parent="FeiraClandestinaFundoFerro/BarracaPecasRaras"]
position = Vector2(250, -380)
color = Color(1, 0.75, 0.38, 1)
energy = 2.0
texture = SubResource("GradientTexture2D_light")
texture_scale = 5.0'''
    )

    content = content.replace(
        '''[node name="TapeteTrocaSucata_1" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3720, 970)
scale = Vector2(0.22, 0.22)''',
        '''[node name="TapeteTrocaSucata_1" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3690, 990)
scale = Vector2(0.28, 0.28)'''
    )

    content = content.replace(
        '''[node name="LuzLamparinaChao" type="PointLight2D" parent="FeiraClandestinaFundoFerro/TapeteTrocaSucata_1"]
position = Vector2(130, -320)
color = Color(1, 0.8, 0.42, 1)
energy = 1.5
texture = SubResource("GradientTexture2D_light")
texture_scale = 3.5''',
        '''[node name="LuzLamparinaChao" type="PointLight2D" parent="FeiraClandestinaFundoFerro/TapeteTrocaSucata_1"]
position = Vector2(130, -320)
color = Color(1, 0.82, 0.45, 1)
energy = 1.9
texture = SubResource("GradientTexture2D_light")
texture_scale = 5.0'''
    )

    content = content.replace(
        '''[node name="JaulaHumanoidesMercadoria" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3980, 1140)
scale = Vector2(0.26, 0.26)''',
        '''[node name="JaulaHumanoidesMercadoria" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(4000, 1150)
scale = Vector2(0.35, 0.35)'''
    )

    content = content.replace(
        '''[node name="LuzLanternaJaula" type="PointLight2D" parent="FeiraClandestinaFundoFerro/JaulaHumanoidesMercadoria"]
position = Vector2(380, -360)
color = Color(0.95, 0.55, 0.22, 1)
energy = 1.8
texture = SubResource("GradientTexture2D_light")
texture_scale = 4.0''',
        '''[node name="LuzLanternaJaula" type="PointLight2D" parent="FeiraClandestinaFundoFerro/JaulaHumanoidesMercadoria"]
position = Vector2(380, -360)
color = Color(1.0, 0.65, 0.25, 1)
energy = 2.2
texture = SubResource("GradientTexture2D_light")
texture_scale = 6.0'''
    )

    content = content.replace(
        '''[node name="TapeteTrocaSucata_2" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3420, 1180)
scale = Vector2(-0.21, 0.21)''',
        '''[node name="TapeteTrocaSucata_2" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3380, 1200)
scale = Vector2(-0.28, 0.28)'''
    )

    content = content.replace(
        '''[node name="BarracaApostas_Secundaria" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3700, 1280)
scale = Vector2(0.22, 0.22)''',
        '''[node name="BarracaApostas_Secundaria" type="Node2D" parent="FeiraClandestinaFundoFerro"]
y_sort_enabled = true
position = Vector2(3720, 1310)
scale = Vector2(0.30, 0.30)'''
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Feira scales and lights updated successfully!")

if __name__ == '__main__':
    update_feira_scales()
