with open('scripts/world/sucateia.gd', 'r', encoding='utf-8') as f:
    content = f.read()

target = '\t\telif capture_mode == "lixao_full":'
replacement = '\t\telif capture_mode == "cabos_bridge_cleaned":\n\t\t\t$Structures/Player.position = Vector2(2067, 1087)\n\t\t\tcam.zoom = Vector2(0.85, 0.85)\n' + target

if target in content:
    content = content.replace(target, replacement, 1)
    with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Added cabos_bridge_cleaned capture mode!")
else:
    print("Target not found!")
