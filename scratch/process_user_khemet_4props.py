# -*- coding: utf-8 -*-
import sys
import os

sys.path.append(r"C:/Users/Usuario/.gemini/antigravity/brain/a9b44d6f-a766-4d22-bddb-484555d5db10/scratch")
from test_perfect_desmatting_v2 import process_perfect_asset

base_user = r"C:/Users/Usuario/.gemini/antigravity/brain/a9b44d6f-a766-4d22-bddb-484555d5db10/.user_uploaded"

tasks = [
    # 1. Estela Sagrada com Glifos e Cristal
    (
        os.path.join(base_user, "media_1792673836356_6a37a90f.jpg"),
        "assets/reconstruction/khemet_glyph_stele_crystal.png",
        "assets/reconstruction/khemet_glyph_stele_crystal_sombra.png",
        3
    ),
    # 2. Esfinge Processional
    (
        os.path.join(base_user, "media_1792673836419_33f95eab.jpg"),
        "assets/reconstruction/khemet_avenue_sphinx_statue.png",
        "assets/reconstruction/khemet_avenue_sphinx_statue_sombra.png",
        3
    ),
    # 3. Sarcófago de Autômato na Areia
    (
        os.path.join(base_user, "media_1792673836544_99cc60fa.jpg"),
        "assets/reconstruction/khemet_automaton_sarcophagus.png",
        "assets/reconstruction/khemet_automaton_sarcophagus_sombra.png",
        3
    ),
    # 4. Braseiro Cerimonial de Bronze
    (
        os.path.join(base_user, "media_1792673836551_56839ae1.jpg"),
        "assets/reconstruction/khemet_bronze_brazier_altar.png",
        "assets/reconstruction/khemet_bronze_brazier_altar_sombra.png",
        3
    )
]

for src, dst_png, dst_shd, erode in tasks:
    print(f"Processando {src} -> {dst_png}...")
    process_perfect_asset(src, dst_png, dst_shd, is_vegetation=False, is_ground=False, erode_px=erode)

print("--- TODOS OS 4 ASSETS PROCESSADOS COM PERFEICAO! ---")
