# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(r"C:/Users/Usuario/.gemini/antigravity/brain/a9b44d6f-a766-4d22-bddb-484555d5db10/scratch")
from test_perfect_desmatting_v2 import process_perfect_asset

base_user = r"C:/Users/Usuario/.gemini/antigravity/brain/a9b44d6f-a766-4d22-bddb-484555d5db10/.user_uploaded"

tasks = [
    # 1. Crista de Duna Barchan (suave para blend no chão)
    (
        os.path.join(base_user, "media_1792677620771_af65a701.jpg"),
        "assets/reconstruction/chapada_dune_ridge_crest.png",
        "assets/reconstruction/chapada_dune_ridge_crest_sombra.png",
        False, True, 4
    ),
    # 2. Vale e Depressão de Areia (suave para blend no chão)
    (
        os.path.join(base_user, "media_1792677620899_8b38df1b.jpg"),
        "assets/reconstruction/chapada_dune_hollow_valley.png",
        "assets/reconstruction/chapada_dune_hollow_valley_sombra.png",
        False, True, 4
    ),
    # 3. Paredão de Cânion (corte de rocha sólido com erosão de 3px)
    (
        os.path.join(base_user, "media_1792677620907_4e5270f6.jpg"),
        "assets/reconstruction/chapada_canyon_cliff_wall.png",
        "assets/reconstruction/chapada_canyon_cliff_wall_sombra.png",
        False, False, 3
    ),
    # 4. Fenda Geológica e Fissura de Rocha
    (
        os.path.join(base_user, "media_1792677620918_fd6c780d.jpg"),
        "assets/reconstruction/chapada_rock_chasm_fissure.png",
        "assets/reconstruction/chapada_rock_chasm_fissure_sombra.png",
        False, False, 3
    ),
    # 5. Mesa / Platô de Arenito
    (
        os.path.join(base_user, "media_1792677620935_afec36c5.jpg"),
        "assets/reconstruction/chapada_sandstone_mesa_butte.png",
        "assets/reconstruction/chapada_sandstone_mesa_butte_sombra.png",
        False, False, 3
    )
]

for src, dst_png, dst_shd, is_veg, is_ground, erode in tasks:
    print(f"Processando {src} -> {dst_png} (is_ground={is_ground}, erode={erode})...")
    process_perfect_asset(src, dst_png, dst_shd, is_vegetation=is_veg, is_ground=is_ground, erode_px=erode)

print("--- TODOS OS 5 ASSETS DE TERRENO NATURAL PROCESSADOS COM SUCESSO! ---")
