path = 'scripts/world/sucateia.gd'
content = open(path, 'r', encoding='utf-8').read()

target = '\t\telif capture_mode == "litoral_user_spot":'
insert = '\t\telif capture_mode == "wave_anim":\n\t\t\t$Structures/Player.position = Vector2(-1600, -60)\n\t\t\tcam.zoom = Vector2(1.05, 1.05)\n\t\t\tcam.limit_left = -14500; cam.limit_right = 1000\n' + target

if target in content and '"wave_anim"' not in content:
    open(path, 'w', encoding='utf-8').write(content.replace(target, insert, 1))
    print('wave_anim camera adicionada!')
else:
    print('Ja existe ou target nao encontrado!')
