from PIL import Image

img = Image.open('C:/Users/Usuario/.gemini/antigravity/brain/a9b44d6f-a766-4d22-bddb-484555d5db10/.user_uploaded/media_1792608020316_018ed3b6.jpg')
w, h = img.size
print(f"Image resolution: {w}x{h}")

# Onde está o jogador na imagem?
# O jogador é o carinha verde com coroa no lado esquerdo
# Vamos amostrar a cor em várias colunas horizontais na altura média (y = h//2)
for x in range(0, w, 50):
    p = img.getpixel((x, h // 2))
    print(f"x={x}, y={h//2} -> RGB={p}")
