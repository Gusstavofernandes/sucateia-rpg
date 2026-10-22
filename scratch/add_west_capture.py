with open('scripts/world/sucateia.gd', 'r', encoding='utf-8') as f:
    c = f.read()

target = """		elif capture_mode == "channel_test":
			$Structures/Player.position = Vector2(1730,1500)
			cam.zoom = Vector2(.85,.85)"""

replacement = """		elif capture_mode == "channel_test":
			$Structures/Player.position = Vector2(1730,1500)
			cam.zoom = Vector2(.85,.85)
		elif capture_mode == "west_expansion_test":
			$Structures/Player.position = Vector2(400, 850)
			cam.zoom = Vector2(0.85, 0.85)"""

if target in c:
    c = c.replace(target, replacement, 1)
    with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Added west_expansion_test!")
else:
    print("Target not found!")
