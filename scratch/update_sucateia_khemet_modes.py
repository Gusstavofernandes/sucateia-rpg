# -*- coding: utf-8 -*-
with open('scripts/world/sucateia.gd', 'r', encoding='utf-8') as f:
    text = f.read()

target = """		elif capture_mode == "west_expansion_test":
			$Structures/Player.position = Vector2(400, 850)
			cam.zoom = Vector2(0.85, 0.85)
		elif capture_mode == "mapa_completo":
			$Structures/Player.position = Vector2(1550, -450)
			cam.zoom = Vector2(0.13, 0.13)
			cam.limit_left = -6000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500"""

replacement = """		elif capture_mode == "west_expansion_test":
			$Structures/Player.position = Vector2(400, 850)
			cam.zoom = Vector2(0.85, 0.85)
		elif capture_mode == "khemet_nexus":
			$Structures/Player.position = Vector2(-11600, -1400)
			cam.zoom = Vector2(0.85, 0.85)
			cam.limit_left = -20000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500
		elif capture_mode == "khemet_temple":
			$Structures/Player.position = Vector2(-13600, -1450)
			cam.zoom = Vector2(0.85, 0.85)
			cam.limit_left = -20000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500
		elif capture_mode == "khemet_pyramid":
			$Structures/Player.position = Vector2(-16300, -1850)
			cam.zoom = Vector2(0.85, 0.85)
			cam.limit_left = -20000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500
		elif capture_mode == "mapa_completo":
			$Structures/Player.position = Vector2(-6000, -850)
			cam.zoom = Vector2(0.08, 0.08)
			cam.limit_left = -20000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500"""

if target in text:
    new_text = text.replace(target, replacement)
    with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("sucateia.gd atualizado com sucesso!")
else:
    # Tenta com CRLF
    target_crlf = target.replace("\n", "\r\n")
    replacement_crlf = replacement.replace("\n", "\r\n")
    if target_crlf in text:
        new_text = text.replace(target_crlf, replacement_crlf)
        with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("sucateia.gd atualizado com sucesso (CRLF)!")
    else:
        print("Target nao encontrado!")
