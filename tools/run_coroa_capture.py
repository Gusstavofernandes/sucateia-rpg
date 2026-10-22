from pathlib import Path
import os
import subprocess

root = Path(__file__).resolve().parents[1]
engine = Path(r"C:\Users\Usuario\Downloads\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe")
env = dict(os.environ, APPDATA=str(root / ".runtime"), LOCALAPPDATA=str(root / ".runtime"))
log = root / "tools" / "capture_coroa_study.log"
result = subprocess.run([str(engine), "--path", str(root), "res://maps/sucateia/sucateia.tscn", "--log-file", str(log), "--", "--capture=coroa_study"], cwd=root, env=env, capture_output=True, text=True, timeout=120)
output = log.read_text(encoding="utf-8-sig") if log.exists() else result.stdout + result.stderr
fatal = [line for line in output.splitlines() if "ERROR:" in line and "Failed to read the root certificate store" not in line]
if result.returncode or fatal or "CAPTURE" not in output:
    print(output)
    raise SystemExit(1)
print(output.splitlines()[-1])
