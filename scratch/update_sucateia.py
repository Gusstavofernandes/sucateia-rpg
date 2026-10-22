with open('scripts/world/sucateia.gd', 'r', encoding='utf-8') as f:
    c = f.read()

target = """		elif capture_mode == "stairs_coast":
			$Structures/Player.position = Vector2(1512,1505)
			cam.zoom = Vector2(.95,.95)"""

replacement = """		elif capture_mode == "stairs_coast":
			$Structures/Player.position = Vector2(1512,1505)
			cam.zoom = Vector2(.95,.95)
		elif capture_mode == "channel_test":
			$Structures/Player.position = Vector2(1730,1500)
			cam.zoom = Vector2(.85,.85)"""

if target in c:
    c = c.replace(target, replacement, 1)
    with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced successfully!")
else:
    # try CRLF
    target_crlf = target.replace("\n", "\r\n")
    replacement_crlf = replacement.replace("\n", "\r\n")
    if target_crlf in c:
        c = c.replace(target_crlf, replacement_crlf, 1)
        with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Replaced CRLF successfully!")
    else:
        print("Target not found!")
