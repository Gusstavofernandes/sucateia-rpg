# -*- coding: utf-8 -*-
with open("scripts/world/sucateia.gd", "r", encoding="utf-8") as f:
    text = f.read()

target = '		elif capture_mode == "khemet_full":'
replacement = '''		elif capture_mode == "khemet_dunas_relief":
			get_viewport().size = Vector2i(2560, 1440)
			$Structures/Player.position = Vector2(-12800, -1800)
			cam.zoom = Vector2(0.42, 0.42)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "khemet_full":'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open("scripts/world/sucateia.gd", "w", encoding="utf-8") as f:
        f.write(text)
    print("Modo khemet_dunas_relief configurado em sucateia.gd!")
