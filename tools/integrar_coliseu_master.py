import shutil
import os
import re

FILES = [
    r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scenes\fundo_ferro_master.tscn",
    r"c:\Users\Usuario\Documents\jogo\scenes\fundo_ferro_master.tscn"
]

for p in FILES:
    if not os.path.exists(p):
        continue
    shutil.copy2(p, p + ".bak_pre_coliseu")
    with open(p, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add ext_resource for ArenaColiseu
    if 'id="148_arena_coliseu_scene"' not in content:
        ext_line = '[ext_resource type="PackedScene" path="res://scenes/ArenaColiseu.tscn" id="148_arena_coliseu_scene"]\n'
        content = re.sub(
            r'(\[ext_resource type="Texture2D" path="res://assets/walls/mureta_baixa_pedra_ferro_v1_sombra\.png" id="147_mureta_baixa_sombra"\]\n)',
            r'\1' + ext_line,
            content
        )

    # 2. Replace the old temporary ArenaColiseu node block
    pattern = r'\[node name="ArenaColiseu" type="Node2D" parent="\."\][\s\S]*?(?=\[node name="Player" type="CharacterBody2D")'
    replacement = '[node name="ArenaColiseu" parent="." instance=ExtResource("148_arena_coliseu_scene")]\n\n'
    content = re.sub(pattern, replacement, content)

    # 3. Update player spawn to (3696, 352)
    content = re.sub(
        r'(\[node name="Player" type="CharacterBody2D" parent="\."\]\ny_sort_enabled = true\nposition = Vector2\()[\d\.\-]+,\s*[\d\.\-]+(\))',
        r'\g<1>3696, 352\2',
        content
    )

    # 4. Update camera limits
    content = re.sub(r'limit_right = \d+', 'limit_right = 4850', content)
    content = re.sub(r'limit_bottom = \d+', 'limit_bottom = 900', content)

    with open(p, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Atualizado com sucesso: {p}")
