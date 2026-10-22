from pathlib import Path
import os, subprocess, sys

root = Path(r"C:\Users\Usuario\Documents\jogo")
engine = Path(r'C:\Users\Usuario\Downloads\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe')
env = dict(os.environ, APPDATA=str(root / '.runtime'), LOCALAPPDATA=str(root / '.runtime'))

name = 'alto_cais'
log = root / 'tools' / f'capture_{name}.log'
print(f"Running capture for {name}...")
result = subprocess.run(
    [str(engine), '--path', str(root), '--log-file', str(log), '--', f'--capture={name}'],
    cwd=root, env=env, capture_output=True, text=True, timeout=120
)
print("Return code:", result.returncode)
if log.exists():
    text = log.read_text(encoding='utf-8-sig', errors='ignore')
    for line in text.splitlines()[-10:]:
        print(line)
