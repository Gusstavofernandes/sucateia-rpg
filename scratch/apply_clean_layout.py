import re
import os

def apply_clean_layout(scene_path):
    print(f"Aplicando layout limpo e desobstruído em {scene_path}...")
    with open(scene_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Ajustar posições de cada nó
    replacements = [
        # Feira do Rolo (Oeste)
        (r'(\[node name="BarracaApostas_Principal"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>3350, 950\2'),
        
        (r'(\[node name="BarracaPecasRaras"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>3750, 950\2'),
        
        (r'(\[node name="cloth_stall"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>3350, 1260\2'),
        (r'(\[node name="BarracaPanosRoupas_Clandestina"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>3350, 1260\2'),

        (r'(\[node name="JaulaHumanoidesMercadoria"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>3750, 1260\2'),

        (r'(\[node name="market_salvage_cart"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>4120, 1260\2'),
        (r'(\[node name="CarrocaoSucateiro_Ambulante"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>4120, 1260\2'),

        (r'(\[node name="TapeteTrocaSucata_1"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>3350, 1520\2'),

        (r'(\[node name="TapeteTrocaSucata_2"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>3750, 1520\2'),

        (r'(\[node name="BarracaApostas_Secundaria"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>3350, 1780\2'),

        (r'(\[node name="fundo_sorting_bank"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>3900, 1780\2'),
        (r'(\[node name="BancadaTriagem_Metais"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>3900, 1780\2'),

        # Centro & Sul
        (r'(\[node name="exchange_pavilion"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>4450, 1460\2'),
        (r'(\[node name="PavilhaoCambio_AvaliacaoReliquias"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>4450, 1460\2'),

        (r'(\[node name="wholesale_arcade"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>4950, 1780\2'),
        (r'(\[node name="ArcadaAtacadista_MercadoRestos"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>4950, 1780\2'),

        # Distrito Mecânico (Leste)
        (r'(\[node name="forjas_recycler"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\)\nscale = Vector2\()[^)]+(\))',
         r'\g<1>4900, 1460\g<2>0.30, 0.30\3'),
        (r'(\[node name="RecicladorPesado_Sucateia"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\)\nscale = Vector2\()[^)]+(\))',
         r'\g<1>4900, 1460\g<2>0.30, 0.30\3'),

        (r'(\[node name="forjas_workshop"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>5400, 1460\2'),
        (r'(\[node name="OficinaArmeiros_Gladiadores"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>5400, 1460\2'),

        (r'(\[node name="fundo_abandoned_engine"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>5820, 1260\2'),
        (r'(\[node name="MotorSubterraneo_Ancestral"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>5820, 1260\2'),

        (r'(\[node name="forjas_boiler_hall"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>5850, 1650\2'),
        (r'(\[node name="SalaCaldeiras_ForjasRasas"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>5850, 1650\2'),

        (r'(\[node name="alto_cistern"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>6320, 1220\2'),
        (r'(\[node name="CisternaElevada_Residuos"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>6320, 1220\2'),

        (r'(\[node name="fundo_collapsed_corner"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>6380, 1580\2'),
        (r'(\[node name="CantoneiraAlvenaria_Rompida"[^\]]*\]\ny_sort_enabled = true\nposition = Vector2\()[^)]+(\))',
         r'\g<1>6380, 1580\2'),
    ]

    for pat, rep in replacements:
        content = re.sub(pat, rep, content)

    # 2. Atualizar limites de câmera do Player
    content = re.sub(r'limit_bottom = \d+', 'limit_bottom = 2000', content)

    with open(scene_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Sucesso ao aplicar layout limpo em {scene_path}!")

apply_clean_layout(r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn')
apply_clean_layout(r'c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn')
