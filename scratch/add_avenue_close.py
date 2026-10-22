# -*- coding: utf-8 -*-
with open("scripts/world/sucateia.gd", "r", encoding="utf-8") as f:
    text = f.read()

target = '''		elif capture_mode == "khemet_full":'''
replacement = '''		elif capture_mode == "khemet_avenue_close":
			get_viewport().size = Vector2i(2560, 1440)
			$Structures/Player.position = Vector2(-13300, -1500)
			cam.zoom = Vector2(0.62, 0.62)
			cam.limit_left = -22000; cam.limit_right = 9000; cam.limit_top = -6000; cam.limit_bottom = 6000
		elif capture_mode == "khemet_full":'''

text = text.replace(target, replacement, 1)

with open("scripts/world/sucateia.gd", "w", encoding="utf-8") as f:
    f.write(text)

print("Modo khemet_avenue_close adicionado!")
