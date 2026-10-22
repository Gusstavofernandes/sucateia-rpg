import re

scene_path = r"fundo_ferro_standalone/scenes/fundo_ferro_master.tscn"
with open(scene_path, "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect BedrockBackground, PisoBaseGeral and any collision shapes
for m in re.finditer(r'\[node name="([^"]+)"[^\]]*\](.*?)(?=\n\[|$)', text, re.DOTALL):
    name = m.group(1)
    body = m.group(2)
    if any(k in name.lower() for k in ["bedrock", "piso", "colisao", "muralha", "camera", "player", "limite"]):
        print(f"=== {name} ===")
        for line in body.strip().splitlines()[:10]:
            print(f"  {line}")
