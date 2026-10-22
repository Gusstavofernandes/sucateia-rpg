with open('scripts/world/sucateia.gd', 'r', encoding='utf-8') as f:
    content = f.read()

target1 = '\t\telif capture_mode == "coast":\n\t\t\t$Structures/Player.position = Vector2(1600,1610)\n\t\t\tcam.offset = Vector2(265,60)\n\t\t\tcam.zoom = Vector2(.85,.85)'
if target1 not in content:
    # try with \r\n
    target1 = '\t\telif capture_mode == "coast":\r\n\t\t\t$Structures/Player.position = Vector2(1600,1610)\r\n\t\t\tcam.offset = Vector2(265,60)\r\n\t\t\tcam.zoom = Vector2(.85,.85)'

nl = '\r\n' if '\r\n' in content else '\n'

replacement1 = target1 + nl + '\t\telif capture_mode == "lixao_full":' + nl + \
    '\t\t\t$Structures/Player.position = Vector2(0, -2100)' + nl + \
    '\t\t\tcam.zoom = Vector2(0.24, 0.24)' + nl + \
    '\t\t\tcam.limit_left = -3200; cam.limit_right = 3200; cam.limit_top = -3600; cam.limit_bottom = 1000' + nl + \
    '\t\telif capture_mode == "lixao_montanha":' + nl + \
    '\t\t\t$Structures/Player.position = Vector2(-280, -2350)' + nl + \
    '\t\t\tcam.zoom = Vector2(0.55, 0.55)' + nl + \
    '\t\telif capture_mode == "lixao_dunas":' + nl + \
    '\t\t\t$Structures/Player.position = Vector2(650, -2150)' + nl + \
    '\t\t\tcam.zoom = Vector2(0.55, 0.55)' + nl + \
    '\t\telif capture_mode == "lixao_guindaste":' + nl + \
    '\t\t\t$Structures/Player.position = Vector2(-750, -2000)' + nl + \
    '\t\t\tcam.zoom = Vector2(0.55, 0.55)' + nl + \
    '\t\telif capture_mode == "lixao_colosso":' + nl + \
    '\t\t\t$Structures/Player.position = Vector2(850, -1700)' + nl + \
    '\t\t\tcam.zoom = Vector2(0.55, 0.55)'

target2 = 'func is_surface_walkable(point: Vector2) -> bool:'
replacement2 = target2 + nl + \
    '\tvar lixao: Node2D = get_node_or_null("GrandeLixaoDistrict")' + nl + \
    '\tif lixao and lixao.has_meta("land_polygon"):' + nl + \
    '\t\tif Geometry2D.is_point_in_polygon(point, lixao.get_meta("land_polygon")): return true'

assert target1 in content, f'target1 not found in content'
assert target2 in content, f'target2 not found in content'

content = content.replace(target1, replacement1, 1)
content = content.replace(target2, replacement2, 1)

with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
    f.write(content)
print('scripts/world/sucateia.gd updated successfully!')
