import re

for path in [r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn', r'c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn']:
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # 1. Sucata_8 de 2150 para 2080
    c = c.replace('[node name="Sucata_8" type="StaticBody2D" parent="EntulhoESucataNoChao"]\nposition = Vector2(2150, 720)',
                  '[node name="Sucata_8" type="StaticBody2D" parent="EntulhoESucataNoChao"]\nposition = Vector2(2080, 720)')

    # 2. PassarelaTravessiaCano_2 de 2210 para 2240
    c = c.replace('[node name="PassarelaTravessiaCano_2" type="Node2D" parent="."]\ny_sort_enabled = true\nposition = Vector2(2210, 642)',
                  '[node name="PassarelaTravessiaCano_2" type="Node2D" parent="."]\ny_sort_enabled = true\nposition = Vector2(2240, 642)')

    # 3. SubResource tamanhos do Centro1 e Centro2
    c = re.sub(
        r'\[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_c1"\]\nsize = Vector2\([^\)]+\)',
        '[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_c1"]\nsize = Vector2(270, 22)',
        c
    )
    c = re.sub(
        r'\[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_c2"\]\nsize = Vector2\([^\)]+\)',
        '[sub_resource type="RectangleShape2D" id="RectangleShape2D_pipe_block_c2"]\nsize = Vector2(285, 22)',
        c
    )

    # 4. Posições dos shapes do Centro1 e Centro2
    c = re.sub(
        r'(\[node name="ColTubo_Centro1" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"\]\nposition = )Vector2\([^\)]+\)',
        r'\1Vector2(2075, 642)',
        c
    )
    c = re.sub(
        r'(\[node name="ColTubo_Centro2" type="CollisionShape2D" parent="ColisaoTubulacaoIndustrial"\]\nposition = )Vector2\([^\)]+\)',
        r'\1Vector2(2412.5, 642)',
        c
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Atualizado {path} com sucesso.")
