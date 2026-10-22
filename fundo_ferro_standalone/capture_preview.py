import subprocess
import os

godot_exe = r"C:\Users\Usuario\Downloads\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64.exe"
project_path = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone"
output_png = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\standalone_fundo_ferro_preview.png"

cmd = [
    godot_exe,
    "--path", project_path,
    "--headless",
    "--resolution", "1280x720",
    "--write-movie", output_png
]

print("Running Godot render capture for standalone Fundo-Ferro...")
res = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
print("Godot return code:", res.returncode)
