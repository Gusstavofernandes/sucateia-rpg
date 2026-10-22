from PIL import Image, ImageFilter, ImageDraw
import numpy as np

img = Image.open('scratch/boca_tunel_v2_raw_cut.png').convert("RGBA")
W, H = img.size

# Criar imagem de sombra separada
sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(sombra)

# A alvenaria de pedra termina em torno de y = 400
# Trilhos descem até y = H - 1
# Sombra de contato sob as bases dos pilares esquerdos e direitos
# Pilar esquerdo: x de 0 a 160, base y ~ 400
sdraw.ellipse([10, 380, 160, 420], fill=(0, 0, 0, 150))
# Pilar central esquerdo: x de 230 a 330, base y ~ 410
sdraw.ellipse([220, 390, 340, 430], fill=(0, 0, 0, 170))
# Pilar central direito: x de 670 a 770, base y ~ 410
sdraw.ellipse([660, 390, 780, 430], fill=(0, 0, 0, 170))
# Pilar direito: x de 850 a 1000, base y ~ 400
sdraw.ellipse([840, 380, 1000, 420], fill=(0, 0, 0, 150))

# Sombra suave sob as paredes laterais
sdraw.rectangle([5, 385, 230, 415], fill=(0, 0, 0, 110))
sdraw.rectangle([770, 385, 995, 415], fill=(0, 0, 0, 110))

# Sombra de contato suave sob os dormentes ao longo dos trilhos
sdraw.rectangle([390, 410, 615, H - 10], fill=(0, 0, 0, 80))

# Blur gaussiano para sombra suave e difusa
sombra = sombra.filter(ImageFilter.GaussianBlur(12))

# Salvar boca_tunel_v2.png oficial e sombra oficial
out_img = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2.png'
out_sombra = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2_sombra.png'
out_txt = 'fundo_ferro_standalone/assets/rails/boca_tunel_v2.txt'

img.save(out_img)
sombra.save(out_sombra)

# Sincronizar em assets/rails/ raiz
img.save('assets/rails/boca_tunel_v2.png')
sombra.save('assets/rails/boca_tunel_v2_sombra.png')

with open(out_txt, 'w', encoding='utf-8') as f:
    f.write("""Game asset, isometric 3/4 top-down view, high elevated camera angle (35 degrees downward, matching top-down dungeon wall perspective), hand-painted gritty industrial fantasy steampunk art style. A very wide dark stone and iron mine tunnel portal carved into an underground dungeon masonry wall. The weathered stone wall spans the entire full horizontal width from the far left edge to the far right edge of the frame. In the center, a deep vaulted mine entrance framed with heavy dark rusted timber beams, bolted iron reinforcement plates, large industrial rivets, cross-braced angled supports, and a glowing warm amber oil lantern hanging on an iron hook. Inside the dark cavern opening, straight vertical minecart railway tracks on aged wooden sleepers enter the darkness and extend straight down towards the bottom edge of the image. Warm amber directional lighting from the upper-left casting subtle soft contact shadows, cool ambient fill. Isolated on a solid flat pure magenta (#FF00FF) background, no floor cutoff, no characters, no text, no watermark, sharp crisp edges, full structure visible.""")

with open('assets/rails/boca_tunel_v2.txt', 'w', encoding='utf-8') as f:
    f.write("""Game asset, isometric 3/4 top-down view, high elevated camera angle (35 degrees downward, matching top-down dungeon wall perspective), hand-painted gritty industrial fantasy steampunk art style. A very wide dark stone and iron mine tunnel portal carved into an underground dungeon masonry wall. The weathered stone wall spans the entire full horizontal width from the far left edge to the far right edge of the frame. In the center, a deep vaulted mine entrance framed with heavy dark rusted timber beams, bolted iron reinforcement plates, large industrial rivets, cross-braced angled supports, and a glowing warm amber oil lantern hanging on an iron hook. Inside the dark cavern opening, straight vertical minecart railway tracks on aged wooden sleepers enter the darkness and extend straight down towards the bottom edge of the image. Warm amber directional lighting from the upper-left casting subtle soft contact shadows, cool ambient fill. Isolated on a solid flat pure magenta (#FF00FF) background, no floor cutoff, no characters, no text, no watermark, sharp edges, full object visible.""")

print("Texturas boca_tunel_v2.png, sombra e txt salvas com sucesso em standalone e raiz!")
