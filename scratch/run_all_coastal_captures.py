import subprocess
import time

modes = [
    "litoral_transicao",
    "litoral_arenito",
    "litoral_praia_aberta",
    "litoral_cabo_extremo"
]

godot_bin = r"C:\Users\Usuario\Downloads\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe"
project_path = r"c:\Users\Usuario\Documents\jogo"

for m in modes:
    print(f"Iniciando captura: {m}...")
    cmd = [
        godot_bin,
        "--path", project_path,
        "res://maps/sucateia/sucateia.tscn",
        "--",
        f"--capture={m}"
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Concluido {m}: {p.stdout.strip()[:100]}")
    time.sleep(1)
print("Todas as capturas concluidas com sucesso!")
