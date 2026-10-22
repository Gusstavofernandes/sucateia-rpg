from PIL import Image, ImageFilter
import numpy as np
from collections import deque

src_path = r"C:\Users\Usuario\.gemini\antigravity\brain\2b874476-d390-4406-8b89-b8e275f8f9f1\monumental_castle_facade_1792609083565.jpg"
out_path = r"assets\generated\structures\monumental_clock_castle.png"

im = Image.open(src_path).convert("RGBA")
w, h = im.size
arr = np.array(im)

# O fundo é branco/quase branco (R > 240, G > 240, B > 240) conectado às bordas externas
# Usamos flood fill / BFS a partir das 4 bordas para identificar apenas o fundo externo
r = arr[:, :, 0].astype(int)
g = arr[:, :, 1].astype(int)
b = arr[:, :, 2].astype(int)

# Condição para ser pixel de fundo branco:
# brilho alto e saturação baixa
brightness = (r + g + b) / 3.0
diff = np.maximum(np.abs(r - g), np.maximum(np.abs(r - b), np.abs(g - b)))

is_bg_candidate = (brightness > 232) & (diff < 18)

visited = np.zeros((h, w), dtype=bool)
q = deque()

# Adiciona todas as bordas externas que são candidatos a fundo
for x in range(w):
    if is_bg_candidate[0, x]:
        visited[0, x] = True
        q.append((0, x))
    if is_bg_candidate[h - 1, x]:
        visited[h - 1, x] = True
        q.append((h - 1, x))

for y in range(h):
    if is_bg_candidate[y, 0] and not visited[y, 0]:
        visited[y, 0] = True
        q.append((y, 0))
    if is_bg_candidate[y, w - 1] and not visited[y, w - 1]:
        visited[y, w - 1] = True
        q.append((y, w - 1))

# BFS
while q:
    cy, cx = q.popleft()
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < h and 0 <= nx < w:
            if not visited[ny, nx] and is_bg_candidate[ny, nx]:
                visited[ny, nx] = True
                q.append((ny, nx))

# visited é True para todo o fundo externo conectado
# Agora criamos o canal alfa com borda suave
alpha = np.ones((h, w), dtype=np.uint8) * 255
alpha[visited] = 0

# Para suavizar a borda e evitar halo branco:
# pixels vizinhos ao fundo com brilho alto recebem fade out
alpha_img = Image.fromarray(alpha, mode='L')
# Pequeno blur no alfa para antialiasing de 1px
alpha_smooth = alpha_img.filter(ImageFilter.GaussianBlur(radius=0.7))
alpha_smooth_arr = np.array(alpha_smooth)

# Forçar o que era fundo estrito a zero
alpha_smooth_arr[visited] = 0

arr[:, :, 3] = alpha_smooth_arr

res_img = Image.fromarray(arr, mode='RGBA')
res_img.save(out_path, format="PNG")
print("Processamento concluído com sucesso!")
print(f"Salvo em: {out_path}")
