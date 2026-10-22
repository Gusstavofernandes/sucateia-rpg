from PIL import Image

w = Image.open('fundo_ferro_standalone/assets/fundo_wall.png')
# salvar um thumbnail para ver no artifact se necessário, ou inspecionar o canto esquerdo
print("Modo:", w.mode)
# Inspecionar transparência da borda esquerda
left_strip = w.crop((0, 0, 100, w.size[1]))
alpha = [left_strip.getpixel((0, y))[3] for y in range(0, w.size[1], 50)]
print("Alpha na coluna 0:", alpha)
