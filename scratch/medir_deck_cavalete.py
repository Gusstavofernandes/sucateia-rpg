from PIL import Image
import numpy as np

img_cav = Image.open('fundo_ferro_standalone/assets/rails/cavalete_alto_v1.png').convert("RGBA")
arr_cav = np.array(img_cav)

# Linha 150 (deck superior do cavalete)
alpha_150 = arr_cav[150, :, 3]
cols = np.where(alpha_150 > 50)[0]
left_deck = cols[0]
right_deck = cols[-1]
deck_w_tex = right_deck - left_deck
center_deck_tex = (left_deck + right_deck) / 2

print(f"Cavalete Alto V1 (Textura 770x995):")
print(f"  Deck topo (y=150): de col {left_deck} a {right_deck} -> largura = {deck_w_tex} px")
print(f"  Centro do deck na textura = {center_deck_tex:.1f} px (offset do centro: {center_deck_tex - 770/2:.1f} px)")
print(f"  Com escala 0.32:")
print(f"    Largura do deck no mundo = {deck_w_tex * 0.32:.1f} px")
print(f"  Com escala 0.20:")
print(f"    Largura do deck no mundo = {deck_w_tex * 0.20:.1f} px")
