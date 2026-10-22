with open('scripts/world/alto_west_cais.gd', 'r', encoding='utf-8') as f:
    c = f.read()

target = """\tvar barrier: StaticBody2D = world.get_node_or_null("WestCoastalBarrier")
\tif barrier:
\t\tfor child in barrier.get_children():
\t\t\tif child is CollisionPolygon2D:
\t\t\t\tvar poly := PackedVector2Array()"""

replacement = """\tvar barrier: StaticBody2D = world.get_node_or_null("WestCoastalBarrier")
\tif barrier:
\t\tfor child in barrier.get_children():
\t\t\tif child is CollisionPolygon2D:
\t\t\t\tchild.build_mode = CollisionPolygon2D.BUILD_SEGMENTS
\t\t\t\tvar poly := PackedVector2Array()"""

if target in c:
    c = c.replace(target, replacement, 1)
    with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Added BUILD_SEGMENTS to alto_west_cais.gd (LF)!")
else:
    target_crlf = target.replace('\n', '\r\n')
    replacement_crlf = replacement.replace('\n', '\r\n')
    if target_crlf in c:
        c = c.replace(target_crlf, replacement_crlf, 1)
        with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Added BUILD_SEGMENTS to alto_west_cais.gd (CRLF)!")
    else:
        print("Target not found!")
