import re

def clean_scene(path):
    print(f"Limpando cena: {path}")
    with open(path, "r", encoding="utf-8") as f:
        c = f.read()

    # 1. Remover DutoDecantadorSombra, DutoEntradaDecantador e DutoSaidaDecantadorCanal
    duto_pattern = r'\[node name="Duto(?:DecantadorSombra|EntradaDecantador|SaidaDecantadorCanal)" type="Line2D" parent="RedeIndustrialMaquinas"\].*?(?=\n\[node name|\Z)'
    c = re.sub(duto_pattern, '', c, flags=re.DOTALL)

    # 2. Remover TuboSuccaoCanal e CotoveloSuccaoCanal
    succao_pattern = r'\[node name="(?:TuboSuccaoCanal|CotoveloSuccaoCanal)" type="Sprite2D" parent="RedeIndustrialMaquinas"\].*?(?=\n\[node name|\Z)'
    c = re.sub(succao_pattern, '', c, flags=re.DOTALL)

    # 3. Corrigir CanoBombaLeste_5 scale para (0.11, 0.11)
    c = re.sub(
        r'(\[node name="CanoBombaLeste_5" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"\]\nposition = Vector2\(2515, 642\)\nscale = )Vector2\(0\.09, 0\.11\)',
        r'\1Vector2(0.11, 0.11)',
        c
    )
    c = re.sub(
        r'(\[node name="CanoBombaLesteSombra_5" type="Sprite2D" parent="RedeIndustrialMaquinas/CanoBombaCaldeiraModular"\]\nz_index = -2\nposition = Vector2\(2515, 650\)\nscale = )Vector2\(0\.09, 0\.11\)',
        r'\1Vector2(0.11, 0.11)',
        c
    )

    # 4. Corrigir FlangeParedeOeste para ser um Bocal de Passagem na Parede Oeste
    # Hoje: FlangeParedeOeste usa ExtResource("37_tubo_vertical")
    # Vamos trocar para usar ExtResource("52_cano_passagem") com scale = Vector2(-0.12, 0.12) para apontar para a parede oeste com moldura!
    flange_oeste_old = r'\[node name="FlangeParedeOeste" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"\]\nposition = Vector2\(120, 642\)\nscale = Vector2\(0\.12, 0\.12\)\ntexture = ExtResource\("37_tubo_vertical"\)'
    flange_oeste_new = '[node name="PassagemParedeOesteSombra" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]\nz_index = -3\nposition = Vector2(110, 650)\nscale = Vector2(-0.12, 0.12)\ntexture = ExtResource("53_cano_passagem_sombra")\n\n[node name="PassagemParedeOeste" type="Sprite2D" parent="RedeIndustrialMaquinas/TuboParedeOesteModular"]\nz_index = -1\nposition = Vector2(110, 643)\nscale = Vector2(-0.12, 0.12)\ntexture = ExtResource("52_cano_passagem")'
    c = re.sub(flange_oeste_old, flange_oeste_new, c)

    # 5. Ajustar Sucata_1 e Sucata_2 na margem norte para fora da rota do trilho da mina
    # O trilho entrará no canto noroeste (X=-100 a 100, Y=200 a 350)
    # Sucata_1 está em (-80, 390). Vamos deslocar para (-180, 420)
    # Sucata_2 está em (320, 400). Vamos deslocar para (360, 430)
    c = c.replace(
        '[node name="Sucata_1" type="StaticBody2D" parent="EntulhoESucataNoChao"]\nposition = Vector2(-80, 390)',
        '[node name="Sucata_1" type="StaticBody2D" parent="EntulhoESucataNoChao"]\nposition = Vector2(-180, 420)'
    )
    c = c.replace(
        '[node name="Sucata_2" type="StaticBody2D" parent="EntulhoESucataNoChao"]\nposition = Vector2(320, 400)',
        '[node name="Sucata_2" type="StaticBody2D" parent="EntulhoESucataNoChao"]\nposition = Vector2(360, 430)'
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    print(f"Cena {path} limpa com sucesso.")

clean_scene(r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn")
clean_scene(r"c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn")
