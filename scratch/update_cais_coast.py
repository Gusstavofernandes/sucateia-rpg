with open('scripts/world/alto_west_cais.gd', 'r', encoding='utf-8') as f:
    c = f.read()

target = """\t\tVector2(-18, 198),  Vector2(38, 238),   Vector2(94, 284),
\t\tVector2(138, 335),  Vector2(146, 385),  Vector2(148, 428),
\t\tVector2(148, 520),  Vector2(130, 610),  Vector2(143, 790),
\t\tVector2(159, 880),  Vector2(145, 1050), Vector2(120, 1160),
\t\tVector2(200, 1250), Vector2(260, 1350), Vector2(290, 1415),
\t\tVector2(360, 1485), Vector2(395, 1535)"""

replacement = """\t\tVector2(-18, 198),  Vector2(38, 238),   Vector2(94, 284),
\t\tVector2(70, 330),   Vector2(-40, 370),  Vector2(-240, 410),
\t\tVector2(-500, 470), Vector2(-720, 560), Vector2(-830, 680),
\t\tVector2(-860, 800), Vector2(-870, 950), Vector2(-850, 1100),
\t\tVector2(-790, 1220), Vector2(-660, 1310), Vector2(-450, 1380),
\t\tVector2(-220, 1430), Vector2(0, 1470), Vector2(180, 1505),
\t\tVector2(395, 1535)"""

if target in c:
    c = c.replace(target, replacement, 1)
    with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced LF!")
else:
    target_crlf = target.replace('\n', '\r\n')
    replacement_crlf = replacement.replace('\n', '\r\n')
    if target_crlf in c:
        c = c.replace(target_crlf, replacement_crlf, 1)
        with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Replaced CRLF!")
    else:
        print("Target not found!")
