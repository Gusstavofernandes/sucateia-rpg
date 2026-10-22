from PIL import Image

img = Image.open('assets/terrain/market_dirt.png')
print("market_dirt:", img.size, img.mode)
print("market_dirt avg:", img.resize((1, 1)).getpixel((0, 0)))
