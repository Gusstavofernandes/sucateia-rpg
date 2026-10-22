with open('scripts/world/sucateia.gd', 'r', encoding='utf-8') as f:
    content = f.read()

target = '\t\telif capture_mode == "alto_west_cais":\n\t\t\t$Structures/Player.position = Vector2(-380, 110)\n\t\t\tcam.zoom = Vector2(0.75, 0.75)'

replacement = '''\t\telif capture_mode == "alto_west_cais":
\t\t\t$Structures/Player.position = Vector2(-880, 50)
\t\t\tcam.zoom = Vector2(0.75, 0.75)
\t\t\tcam.limit_left = -3800; cam.limit_right = 3200; cam.limit_top = -2000; cam.limit_bottom = 2000
\t\telif capture_mode == "litoral_full":
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

if target in content:
    content = content.replace(target, replacement, 1)
    with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Modos de captura do litoral adicionados a sucateia.gd com sucesso!")
else:
    print("Target não encontrado!")
