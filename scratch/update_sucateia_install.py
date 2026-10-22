with open('scripts/world/sucateia.gd', 'r', encoding='utf-8') as f:
    c = f.read()

target = '\tload("res://scripts/world/alto_west_cais.gd").new().install(self)'
replacement = target + '\n\tload("res://scripts/world/sucateia_west_ground.gd").new().install(self)'

if target in c:
    c = c.replace(target, replacement, 1)
    with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated sucateia.gd (LF)!")
else:
    target_crlf = target.replace('\n', '\r\n')
    replacement_crlf = replacement.replace('\n', '\r\n')
    if target_crlf in c:
        c = c.replace(target_crlf, replacement_crlf, 1)
        with open('scripts/world/sucateia.gd', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated sucateia.gd (CRLF)!")
    else:
        print("Target not found!")
