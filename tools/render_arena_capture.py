from pathlib import Path
import subprocess
import os
import sys

root = Path(r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone")
engine = Path(r"C:\Users\Usuario\Downloads\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64\Godot_v4.7.2-stable_mono_win64_console.exe")

tscn = root / "scenes" / "fundo_ferro_master.tscn"
text = tscn.read_text(encoding="utf-8")

cap_tscn = root / "scenes" / "captura_arena_temp.tscn"
cap_text = text.replace(
    '[ext_resource type="Script" path="res://scripts/player.gd" id="1_player_script"]',
    '[ext_resource type="Script" path="res://scripts/player.gd" id="1_player_script"]\n[ext_resource type="Script" path="res://scripts/captura_arena_render.gd" id="999_cap_script"]'
).replace(
    '[node name="FundoFerroMaster" type="Node2D"]',
    '[node name="FundoFerroMaster" type="Node2D"]\nscript = ExtResource("999_cap_script")'
)
cap_tscn.write_text(cap_text, encoding="utf-8")

env = dict(os.environ, APPDATA=str(root / ".runtime"), LOCALAPPDATA=str(root / ".runtime"))
try:
    res = subprocess.run(
        [str(engine), "--path", str(root), "scenes/captura_arena_temp.tscn"],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
        timeout=60
    )
    print("STDOUT:", res.stdout)
    print("RETURNCODE:", res.returncode)
finally:
    if cap_tscn.exists():
        cap_tscn.unlink()
