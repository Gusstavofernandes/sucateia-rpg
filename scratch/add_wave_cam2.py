path = 'scripts/world/sucateia.gd'
content = open(path, 'r', encoding='utf-8').read()

target = '\t\telif capture_mode == "litoral_user_spot":\n\t\t\t$Structures/Player.position = Vector2(-1600, -90)\n\t\t\tcam.zoom = Vector2(0.95, 0.95)\n\t\t\tcam.limit_left = -14500; cam.limit_right = 1000'

insert = target + '\n\t\telif capture_mode == "wave_anim":\n\t\t\t$Structures/Player.position = Vector2(-1600, -45)\n\t\t\tcam.zoom = Vector2(1.10, 1.10)\n\t\t\tcam.limit_left = -14500; cam.limit_right = 1000'

if target in content:
    open(path, 'w', encoding='utf-8').write(content.replace(target, insert, 1))
    print('Camera wave_anim configurada com sucesso!')
else:
    print('Target nao encontrado!')
