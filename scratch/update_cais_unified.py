with open('scripts/world/alto_west_cais.gd', 'r', encoding='utf-8') as f:
    c = f.read()

target = """\t# Transio e cais urbano a leste
\tvar east_coast: Array[Vector2] = [
\t\tVector2(-735, 115), Vector2(-695, 118), Vector2(-635, 120),
\t\tVector2(-570, 122), Vector2(-505, 122), Vector2(-440, 120),
\t\tVector2(-375, 120), Vector2(-245, 120),
\t\tVector2(-180, 120), Vector2(-125, 120), Vector2(-73, 166),
\t\tVector2(-18, 198),  Vector2(38, 238),   Vector2(94, 284),
\t\tVector2(70, 330),   Vector2(-40, 370),  Vector2(-240, 410),
\t\tVector2(-500, 470), Vector2(-720, 560), Vector2(-830, 680),
\t\tVector2(-860, 800), Vector2(-870, 950), Vector2(-850, 1100),
\t\tVector2(-790, 1220), Vector2(-660, 1310), Vector2(-450, 1380),
\t\tVector2(-220, 1430), Vector2(0, 1470), Vector2(180, 1505),
\t\tVector2(395, 1535)
\t]"""

replacement = """\t# Litoral oeste continuo unificado de Sucateia e Alto-Lixo
\tvar east_coast: Array[Vector2] = [
\t\tVector2(-750, 80),
\t\tVector2(-800, 150),
\t\tVector2(-850, 260),
\t\tVector2(-880, 400),
\t\tVector2(-890, 560),
\t\tVector2(-890, 720),
\t\tVector2(-880, 860),
\t\tVector2(-870, 980),
\t\tVector2(-850, 1100),
\t\tVector2(-790, 1220),
\t\tVector2(-660, 1310),
\t\tVector2(-450, 1380),
\t\tVector2(-220, 1430),
\t\tVector2(0, 1470),
\t\tVector2(180, 1505),
\t\tVector2(395, 1535)
\t]"""

if target in c:
    c = c.replace(target, replacement, 1)
    with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Updated alto_west_cais.gd (LF)!")
else:
    # try CRLF
    target_crlf = target.replace('\n', '\r\n')
    replacement_crlf = replacement.replace('\n', '\r\n')
    if target_crlf in c:
        c = c.replace(target_crlf, replacement_crlf, 1)
        with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated alto_west_cais.gd (CRLF)!")
    else:
        # replace more loosely
        import re
        c = re.sub(r'var east_coast: Array\[Vector2\] = \[[^\]]+\]', replacement.strip(), c, count=1)
        with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Updated alto_west_cais.gd via regex!")
