from PIL import Image

try:
    im = Image.open('assets/pipes/cano_travessia_ponte.png')
    print('cano_travessia_ponte.png size:', im.size, im.mode)
    im2 = Image.open('assets/pipes/cano_travessia_ponte_sombra.png')
    print('cano_travessia_ponte_sombra.png size:', im2.size, im2.mode)
except Exception as e:
    print('error:', e)
