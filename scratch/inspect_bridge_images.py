from PIL import Image

p1 = Image.open('fundo_ferro_standalone/assets/walkway.png')
print('walkway.png size:', p1.size, p1.mode)

p2 = Image.open('assets/pipes/passarela_travessia_completa_v1.png')
print('passarela_travessia_completa_v1.png size:', p2.size, p2.mode)
