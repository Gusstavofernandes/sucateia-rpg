path = 'scripts/world/sucateia.gd'
content = open(path, 'r', encoding='utf-8').read()

target = '\t\telif capture_mode == "litoral_full":\n\t\t\t$Structures/Player.position = Vector2(-2800, -350)\n\t\t\tcam.zoom = Vector2(0.14, 0.14)\n\t\t\tcam.limit_left = -6500; cam.limit_right = 1000; cam.limit_top = -2500; cam.limit_bottom = 2500\n\t\telif capture_mode == "litoral_transicao":\n\t\t\t$Structures/Player.position = Vector2(-1200, -50)\n\t\t\tcam.zoom = Vector2(0.55, 0.55)\n\t\t\tcam.limit_left = -6500\n\t\telif capture_mode == "litoral_amarelo_medio":\n\t\t\t$Structures/Player.position = Vector2(-2800, -320)\n\t\t\tcam.zoom = Vector2(0.55, 0.55)\n\t\t\tcam.limit_left = -6500\n\t\telif capture_mode == "litoral_extremo_oeste":\n\t\t\t$Structures/Player.position = Vector2(-4800, -520)\n\t\t\tcam.zoom = Vector2(0.55, 0.55)\n\t\t\tcam.limit_left = -6500'

replacement = '\t\telif capture_mode == "litoral_full":\n\t\t\t$Structures/Player.position = Vector2(-6500, -700)\n\t\t\tcam.zoom = Vector2(0.075, 0.075)\n\t\t\tcam.limit_left = -14500; cam.limit_right = 1000; cam.limit_top = -2800; cam.limit_bottom = 2800\n\t\telif capture_mode == "litoral_transicao":\n\t\t\t$Structures/Player.position = Vector2(-1500, -100)\n\t\t\tcam.zoom = Vector2(0.65, 0.65)\n\t\t\tcam.limit_left = -14500; cam.limit_right = 1000\n\t\telif capture_mode == "litoral_arenito":\n\t\t\t$Structures/Player.position = Vector2(-4800, -520)\n\t\t\tcam.zoom = Vector2(0.65, 0.65)\n\t\t\tcam.limit_left = -14500; cam.limit_right = 1000\n\t\telif capture_mode == "litoral_praia_aberta":\n\t\t\t$Structures/Player.position = Vector2(-8800, -820)\n\t\t\tcam.zoom = Vector2(0.65, 0.65)\n\t\t\tcam.limit_left = -14500; cam.limit_right = 1000\n\t\telif capture_mode == "litoral_cabo_extremo":\n\t\t\t$Structures/Player.position = Vector2(-12200, -1020)\n\t\t\tcam.zoom = Vector2(0.65, 0.65)\n\t\t\tcam.limit_left = -14500; cam.limit_right = 1000'

if target in content:
    open(path, 'w', encoding='utf-8').write(content.replace(target, replacement, 1))
    print("Atualizado com sucesso!")
else:
    print("Target nao encontrado!")
