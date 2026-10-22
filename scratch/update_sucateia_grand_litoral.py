with open('scripts/world/sucateia.gd', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''\t\telif capture_mode == "litoral_full":
\t\t\t$Structures/Player.position = Vector2(-1600, -250)
\t\t\tcam.zoom = Vector2(0.24, 0.24)
\t\t\tcam.limit_left = -3800; cam.limit_right = 1000; cam.limit_top = -1600; cam.limit_bottom = 1800
\t\telif capture_mode == "litoral_transicao":
\t\t\t$Structures/Player.position = Vector2(-880, 50)
\t\t\tcam.zoom = Vector2(0.70, 0.70)
\t\t\tcam.limit_left = -3800
\t\telif capture_mode == "litoral_recifes_azuis":
\t\t\t$Structures/Player.position = Vector2(-1700, -280)
\t\t\tcam.zoom = Vector2(0.60, 0.60)
\t\t\tcam.limit_left = -3800
\t\telif capture_mode == "litoral_falesias_amarelas":
\t\t\t$Structures/Player.position = Vector2(-2350, -480)
\t\t\tcam.zoom = Vector2(0.60, 0.60)
\t\t\tcam.limit_left = -3800'''

replacement = '''\t\telif capture_mode == "litoral_full":
\t\t\t$Structures/Player.position = Vector2(-2800, -350)
\t\t\tcam.zoom = Vector2(0.14, 0.14)
\t\t\tcam.limit_left = -6500; cam.limit_right = 1000; cam.limit_top = -2500; cam.limit_bottom = 2500
\t\telif capture_mode == "litoral_transicao":
\t\t\t$Structures/Player.position = Vector2(-1200, -50)
\t\t\tcam.zoom = Vector2(0.55, 0.55)
\t\t\tcam.limit_left = -6500
\t\telif capture_mode == "litoral_amarelo_medio":
\t\t\t$Structures/Player.position = Vector2(-2800, -320)
\t\t\tcam.zoom = Vector2(0.55, 0.55)
\t\t\tcam.limit_left = -6500
\t\telif capture_mode == "litoral_extremo_oeste":
\t\t\t$Structures/Player.position = Vector2(-4800, -520)
\t\t\tcam.zoom = Vector2(0.55, 0.55)
\t\t\tcam.limit_left = -6500'''

if target in content:
    content = content.replace(target, replacement, 1)
    with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Atualizado sucateia.gd com presets de 6000px de litoral!")
else:
    print("Target não encontrado!")
