# -*- coding: utf-8 -*-
with open("scripts/world/sucateia.gd", "r", encoding="utf-8") as f:
    text = f.read()

target = """		elif capture_mode == "khemet_pyramid":
			$Structures/Player.position = Vector2(-16300, -1850)
			cam.zoom = Vector2(0.85, 0.85)
			cam.limit_left = -20000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500
		elif capture_mode == "mapa_completo":
			$Structures/Player.position = Vector2(-6000, -850)
			cam.zoom = Vector2(0.08, 0.08)
			cam.limit_left = -20000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500"""

replacement = """		elif capture_mode == "khemet_pyramid":
			$Structures/Player.position = Vector2(-16300, -1850)
			cam.zoom = Vector2(0.85, 0.85)
			cam.limit_left = -20000; cam.limit_right = 9000; cam.limit_top = -4500; cam.limit_bottom = 4500
		elif capture_mode == "mapa_completo":
			get_viewport().size = Vector2i(3840, 1600)
			$Structures/Player.position = Vector2(-7500, -350)
			cam.zoom = Vector2(0.165, 0.165)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "khemet_full":
			get_viewport().size = Vector2i(2560, 1440)
			$Structures/Player.position = Vector2(-14000, -1700)
			cam.zoom = Vector2(0.30, 0.30)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "chapada_full":
			get_viewport().size = Vector2i(2560, 1440)
			$Structures/Player.position = Vector2(-5500, -850)
			cam.zoom = Vector2(0.32, 0.32)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "sucateia_full":
			get_viewport().size = Vector2i(2560, 1440)
			$Structures/Player.position = Vector2(1500, 300)
			cam.zoom = Vector2(0.35, 0.35)
			cam.limit_left = -6000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000"""

if target in text:
    text = text.replace(target, replacement, 1)
    with open("scripts/world/sucateia.gd", "w", encoding="utf-8") as f:
        f.write(text)
    print("Atualizado com sucesso!")
else:
    target_crlf = target.replace("\n", "\r\n")
    replacement_crlf = replacement.replace("\n", "\r\n")
    if target_crlf in text:
        text = text.replace(target_crlf, replacement_crlf, 1)
        with open("scripts/world/sucateia.gd", "w", encoding="utf-8") as f:
            f.write(text)
        print("Atualizado com sucesso (CRLF)!")
    else:
        print("Target nao encontrado!")
