from PIL import Image

im = Image.open('assets/generated/structures/monumental_clock_castle.png')
# Top 300
top = im.crop((0, 0, im.width, 300))
top.save('C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_top.png')

# Bottom 300
bot = im.crop((0, im.height - 300, im.width, im.height))
bot.save('C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/castle_bot.png')
print("Salvo top e bot")
