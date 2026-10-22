path = 'scripts/world/sucateia.gd'
content = open(path, 'r', encoding='utf-8').read()
target = '\t\telif capture_mode == "litoral_transicao":'
insert = '\t\telif capture_mode == "litoral_user_spot":\n\t\t\t$Structures/Player.position = Vector2(-1600, -90)\n\t\t\tcam.zoom = Vector2(0.95, 0.95)\n\t\t\tcam.limit_left = -14500; cam.limit_right = 1000\n' + target
if target in content and 'litoral_user_spot' not in content:
    open(path, 'w', encoding='utf-8').write(content.replace(target, insert, 1))
    print('litoral_user_spot adicionado com sucesso!')
else:
    print('Ja existe ou target nao encontrado!')
