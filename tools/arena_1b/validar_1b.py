"""Validacao 1B: alinhamento (<=1 px), transparencia dos vaos, escala vs goblin, fade, sobre fundo escuro e claro."""
import numpy as np
from PIL import Image, ImageDraw
D = r"c:\Users\Usuario\Documents\jogo\tools\arena_1b"
gx = Image.open(f"{D}\\arena_grade_reta_x_v1.png"); pl = Image.open(f"{D}\\arena_pilar_v1.png")
cn = Image.open(f"{D}\\arena_canto_v1.png"); gy = Image.open(f"{D}\\arena_grade_reta_y_v1.png")
a = np.array(gx)[..., 3]
res = {}
# 1) bordas esquerda/direita identicas (modulo repete) e continuidade trilhos
res["borda_esq_eq_dir_px"] = int((a[:, 0] != a[:, -1]).sum())
rows_l = np.where(a[:, 0] > 0)[0]; rows_r = np.where(a[:, -1] > 0)[0]
res["trilho_topo_linhas"] = (int(rows_l.min()), int(rows_l[rows_l < 100].max()))
# 2) barras: centros medidos (px final, 4 px = 1 mundo), medidos na linha y=200
row = a[200]; xs = np.where(row > 0)[0]
groups = np.split(xs, np.where(np.diff(xs) > 1)[0] + 1)
cent = [round((g[0] + g[-1] + 1) / 2 / 4, 2) for g in groups]
larg = [round(len(g) / 4, 2) for g in groups]
res["barras_centro_mundo"] = cent; res["barras_largura_mundo"] = larg
res["esperado_centro"] = [19, 32, 45]
# 3) vaos transparentes: area transparente entre trilhos
inner = a[40:380, :]
res["vao_transparente_%"] = round(100 * float((inner == 0).mean()), 1)
# 4) pixels magenta
for n, im in (("gx", gx), ("pl", pl), ("cn", cn), ("gy", gy)):
    t = np.array(im).astype(int); m = (t[..., 3] > 0) & (t[..., 0] > 120) & (t[..., 2] > 120) & (np.minimum(t[..., 0], t[..., 2]) - t[..., 1] > 60)
    res[f"magenta_{n}"] = int(m.sum())
print(res)

# composicao: 3 modulos X, pilares nas juncoes, goblin 48 de altura (192 px) sobre escuro e claro
def cena(bg, fade=1.0):
    W, H = 256 * 3 + 200, 560
    im = Image.new("RGBA", (W, H), bg)
    base = H - 40
    for k in range(3):
        g = gx.copy(); 
        if fade < 1: g.putalpha(g.split()[3].point(lambda v: int(v * fade)))
        im.alpha_composite(g, (100 + k * 256, base - g.height))
    for k in range(4):
        p = pl.copy()
        if fade < 1: p.putalpha(p.split()[3].point(lambda v: int(v * fade)))
        im.alpha_composite(p, (100 + k * 256 - 32, base - p.height))
    d = ImageDraw.Draw(im)   # goblin (48 mundo = 192 px de altura, 24 de largura = 96 px) atras da grade, a 3o modulo
    gx0 = 100 + 256 + 128 - 48
    d.rectangle([gx0, base - 192 - 40, gx0 + 96, base - 40], fill=(90, 138, 62, 255), outline=(0, 0, 0, 255))
    d.rectangle([gx0 + 16, base - 232 - 40 + 40, gx0 + 80, base - 192 - 40 + 24], fill=(235, 30, 30, 255))
    return im
cenas = [cena((30, 28, 34, 255)), cena((205, 195, 175, 255)), cena((30, 28, 34, 255), 0.35)]
W = sum(c.width for c in cenas); out = Image.new("RGBA", (W, cenas[0].height))
x = 0
for c in cenas: out.alpha_composite(c, (x, 0)); x += c.width
# canto e grade Y ao lado
out.save(f"{D}\\validacao_1b.png"); print("ok", out.size)
