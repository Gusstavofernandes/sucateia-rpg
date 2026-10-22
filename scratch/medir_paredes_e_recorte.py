from PIL import Image

wall = Image.open('fundo_ferro_standalone/assets/fundo_wall.png')
print("Wall image size:", wall.size)

# WallSeg1: position = Vector2(700, 140), scale = Vector2(0.85, 0.85)
w1_w = wall.size[0] * 0.85
w1_h = wall.size[1] * 0.85
w1_left = 700 - w1_w / 2
w1_right = 700 + w1_w / 2
w1_top = 140 - w1_h / 2
w1_bottom = 140 + w1_h / 2

print(f"WallSeg1 (pos=(700, 140), scale=0.85):")
print(f"  Width no mundo: {w1_w:.1f} px, Height no mundo: {w1_h:.1f} px")
print(f"  Bordas no mundo: Left = {w1_left:.1f}, Right = {w1_right:.1f}, Top = {w1_top:.1f}, Bottom = {w1_bottom:.1f}")

# ChaoPasseioGeral: offset_left = -500.0, offset_top = 180.0, offset_right = 3800.0, offset_bottom = 1100.0
print(f"ChaoPasseioGeral (piso): Top = 180.0 px, Left = -500.0 px")
