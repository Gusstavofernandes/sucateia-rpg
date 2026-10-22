# -*- coding: utf-8 -*-
import subprocess
import time
import shutil
import os

godot_bin = r"C:\Users\Usuario\Downloads\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe"
project_path = r"c:\Users\Usuario\Documents\jogo"
artifacts_dir = r"C:\Users\Usuario\.gemini\antigravity\brain\a9b44d6f-a766-4d22-bddb-484555d5db10"

modes = [
    "mapa_completo",
    "khemet_full",
    "chapada_full",
    "sucateia_full"
]

results = []

for m in modes:
    print(f"--- Gerando captura: {m} ---")
    cmd = [
        godot_bin,
        "--path", project_path,
        "res://maps/sucateia/sucateia.tscn",
        "--",
        f"--capture={m}"
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    out_file = os.path.join(project_path, "maps", "sucateia", f"preview_{m}.png")
    if os.path.exists(out_file):
        dst_file = os.path.join(artifacts_dir, f"preview_{m}.png")
        shutil.copy2(out_file, dst_file)
        sz = os.path.getsize(dst_file)
        print(f"Sucesso: {m} -> {dst_file} ({sz} bytes)")
        results.append((m, dst_file))
    else:
        print(f"Aviso: {out_file} nao foi gerado. Stdout: {p.stdout[:200]}")

print("Concluido processamento de capturas!")
