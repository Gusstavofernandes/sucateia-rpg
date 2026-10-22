with open('scripts/world/alto_west_cais.gd', 'r', encoding='utf-8') as f:
    c = f.read()

import re

target_block = """\tvar east_coast: Array[Vector2] = [
\t\tVector2(-735, 115), Vector2(-695, 118), Vector2(-635, 120),
\t\tVector2(-570, 122), Vector2(-505, 122), Vector2(-440, 120),
\t\tVector2(-375, 120), Vector2(-245, 120),
\t\tVector2(-180, 120), Vector2(-125, 120), Vector2(-73, 166),
\t\tVector2(-18, 198),  Vector2(38, 238),   Vector2(94, 284),
\t\tVector2(138, 335),  Vector2(146, 385),  Vector2(148, 428),
\t\tVector2(148, 520),  Vector2(130, 610),  Vector2(143, 790),
\t\tVector2(159, 880),  Vector2(145, 1050), Vector2(120, 1160),
\t\tVector2(200, 1250), Vector2(260, 1350), Vector2(290, 1415),
\t\tVector2(360, 1485), Vector2(395, 1535)
\t]"""

replacement_block = """\tvar east_coast: Array[Vector2] = [
\t\tVector2(-750, 80),
\t\tVector2(-800, 150),
\t\tVector2(-850, 260),
\t\tVector2(-880, 400),
\t\tVector2(-890, 560),
\t\tVector2(-890, 720),
\t\tVector2(-880, 860),
\t\tVector2(-870, 980),
\t\tVector2(-850, 1100),
\t\tVector2(-820, 1220),
\t\tVector2(-780, 1350),
\t\tVector2(-720, 1480),
\t\tVector2(-600, 1580),
\t\tVector2(-450, 1640),
\t\tVector2(-200, 1670),
\t\tVector2(50, 1670),
\t\tVector2(250, 1630),
\t\tVector2(395, 1535)
\t]"""

if target_block in c:
    c = c.replace(target_block, replacement_block, 1)
    with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Replaced in alto_west_cais.gd successfully (LF)!")
else:
    target_crlf = target_block.replace('\n', '\r\n')
    replacement_crlf = replacement_block.replace('\n', '\r\n')
    if target_crlf in c:
        c = c.replace(target_crlf, replacement_crlf, 1)
        with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Replaced in alto_west_cais.gd successfully (CRLF)!")
    else:
        # Regex replacement
        c = re.sub(r'var east_coast: Array\[Vector2\] = \[[^\]]+\]', replacement_block.strip(), c, count=1)
        with open('scripts/world/alto_west_cais.gd', 'w', encoding='utf-8') as f:
            f.write(c)
        print("Replaced in alto_west_cais.gd via regex!")
