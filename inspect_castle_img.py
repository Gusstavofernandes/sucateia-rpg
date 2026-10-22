from PIL import Image

src_path = r"C:\Users\Usuario\.gemini\antigravity\brain\2b874476-d390-4406-8b89-b8e275f8f9f1\monumental_castle_facade_1792609083565.jpg"
im = Image.open(src_path)
print("Tamanho:", im.size)
print("Modo:", im.mode)
# Amostra dos cantos (fundo)
corners = [
    im.getpixel((0, 0)),
    im.getpixel((im.width - 1, 0)),
    im.getpixel((0, im.height - 1)),
    im.getpixel((im.width - 1, im.height - 1))
]
print("Cantos:", corners)
