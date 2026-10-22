from PIL import Image

im = Image.open('assets/pipes/cano_travessia_ponte.png')
# let's resize to a smaller preview for quick inspection
preview = im.resize((480, int(480 * im.size[1] / im.size[0])))
preview.save('scratch/preview_cano_ponte.png')
print('Preview saved to scratch/preview_cano_ponte.png')
