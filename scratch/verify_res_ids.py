with open('maps/sucateia/sucateia.tscn', 'r', encoding='utf-8') as f:
    text = f.read()

import re
res = re.findall(r'\[ext_resource type=\"([^\"]+)\" path=\"([^\"]+)\" id=\"([^\"]+)\"\]', text)
res_dict = {path: id_ for t, path, id_ in res}

checks = [
    "res://assets/infrastructure/coastal_wall.png",
    "res://assets/infrastructure/retaining_edge.png",
    "res://assets/terrain/foundation.png",
    "res://assets/terrain/metal_repair.png",
    "res://assets/terrain/market_dirt.png",
    "res://assets/infrastructure/walkway.png",
    "res://assets/infrastructure/lantern.png",
    "res://assets/fx/light.svg",
    "res://assets/infrastructure/scrap.png",
    "res://assets/generated/props/pipe.png",
    "res://assets/props/crate.svg",
    "res://assets/props/barrel.svg"
]

for c in checks:
    print(f"{c} -> {res_dict.get(c)}")
