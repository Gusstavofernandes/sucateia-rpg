from PIL import Image

for fname in [
    "fundo_ferro_standalone/captura_ponte_sem_carrinho_completo.png",
    "fundo_ferro_standalone/captura_ponte_canal_travessia.png",
    "fundo_ferro_standalone/captura_ponte_emenda_closeup.png"
]:
    im = Image.open(fname)
    print(f"{fname}: Size={im.size}, Mode={im.mode}")
