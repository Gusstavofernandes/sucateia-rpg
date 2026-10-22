from PIL import Image

im = Image.open("assets/machines/maquina_tanque_decantador_v1.png")
print("maquina_tanque_decantador_v1.png:", im.size, im.mode)

# Prompt do decantador existente:
with open("assets/machines/maquina_tanque_decantador_v1_prompt.txt", "r", encoding="utf-8") as f:
    print("Prompt original:", f.read())
