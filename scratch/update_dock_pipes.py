with open('scripts/world/connected_utilities.gd', 'r', encoding='utf-8') as f:
    c = f.read()

target = """\tvar infra: Node2D = world.get_node_or_null("FinishedInfrastructure")
\tif infra:
\t\tfor old in infra.get_children():
\t\t\tif old is Sprite2D and old.texture and old.texture.resource_path == PIPE:
\t\t\t\tif old.position.distance_to(Vector2(1703, 1448)) < 25.0 or old.position.distance_to(Vector2(1945, 1480)) < 25.0:
\t\t\t\t\told.hide()"""

replacement = """\tvar infra: Node2D = world.get_node_or_null("FinishedInfrastructure")
\tif infra:
\t\tfor old in infra.get_children():
\t\t\tif old is Sprite2D and old.texture and old.texture.resource_path == PIPE:
\t\t\t\tif old.position.distance_to(Vector2(1703, 1448)) < 25.0 or old.position.distance_to(Vector2(1945, 1480)) < 25.0 or (absf(old.position.y - 1550.0) < 15.0 and old.position.x >= 500.0 and old.position.x <= 1000.0):
\t\t\t\t\told.hide()"""

if target in c:
    c = c.replace(target, replacement, 1)
    with open('scripts/world/connected_utilities.gd', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated connected_utilities.gd with dock pipes!")
else:
    target_crlf = target.replace('\n', '\r\n')
    replacement_crlf = replacement.replace('\n', '\r\n')
    if target_crlf in c:
        c = c.replace(target_crlf, replacement_crlf, 1)
        with open('scripts/world/connected_utilities.gd', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated connected_utilities.gd (CRLF) with dock pipes!")
    else:
        print("Target not found!")
