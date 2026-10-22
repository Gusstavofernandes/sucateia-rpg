with open('scripts/world/connected_utilities.gd', 'r', encoding='utf-8') as f:
    c = f.read()

target = """\tvar feeder:=group(utility,"CoreFeeder")
\tfor parent_name in ["GroundDetails","FinishedInfrastructure"]:"""

replacement = """\t# Remoção dos 3 canos no canal sul solicitados pelo usuário
\tvar lower_coast: Node2D = world.get_node_or_null("LowerCoastReworked")
\tif lower_coast:
\t\tfor old in lower_coast.get_children():
\t\t\tif old is Sprite2D and old.texture and old.texture.resource_path == PIPE:
\t\t\t\tif old.position.distance_to(Vector2(1770, 1510)) < 25.0:
\t\t\t\t\told.hide()
\tvar infra: Node2D = world.get_node_or_null("FinishedInfrastructure")
\tif infra:
\t\tfor old in infra.get_children():
\t\t\tif old is Sprite2D and old.texture and old.texture.resource_path == PIPE:
\t\t\t\tif old.position.distance_to(Vector2(1703, 1448)) < 25.0 or old.position.distance_to(Vector2(1945, 1480)) < 25.0:
\t\t\t\t\told.hide()

\tvar feeder:=group(utility,"CoreFeeder")
\tfor parent_name in ["GroundDetails","FinishedInfrastructure"]:"""

if target in c:
    c = c.replace(target, replacement, 1)
    with open('scripts/world/connected_utilities.gd', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated connected_utilities.gd (LF)!")
else:
    target_crlf = target.replace('\n', '\r\n')
    replacement_crlf = replacement.replace('\n', '\r\n')
    if target_crlf in c:
        c = c.replace(target_crlf, replacement_crlf, 1)
        with open('scripts/world/connected_utilities.gd', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated connected_utilities.gd (CRLF)!")
    else:
        print("Target not found!")
