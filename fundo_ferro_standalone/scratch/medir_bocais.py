from PIL import Image
import numpy as np

base = r'c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets'
art = r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b'

def perfil(path, scale, sprite_world, nome):
    im = Image.open(path).convert('RGBA')
    a = np.array(im)[:, :, 3]
    W, H = im.size
    print(f'== {nome}: {W}x{H}, scale {scale}')
    for side in ('esq', 'dir'):
        cols = range(0, 60) if side == 'esq' else range(W - 60, W)
        # para cada coluna próxima da borda, faixa vertical opaca
        for x in list(cols)[::15]:
            ys = np.where(a[:, x] > 128)[0]
            if len(ys):
                # agrupar segmentos contínuos
                segs, start = [], ys[0]
                for i in range(1, len(ys)):
                    if ys[i] != ys[i-1] + 1:
                        segs.append((start, ys[i-1])); start = ys[i]
                segs.append((start, ys[-1]))
                segs = [s for s in segs if s[1] - s[0] > 10]
                out = []
                for s in segs:
                    cy = (s[0] + s[1]) / 2
                    wy = sprite_world[1] + (cy - H / 2) * scale
                    wx = sprite_world[0] + (x - W / 2) * scale
                    out.append(f'y{s[0]}-{s[1]} (diam {s[1]-s[0]}px = {(s[1]-s[0])*scale:.1f}w) centro_mundo=({wx:.0f},{wy:.1f})')
                print(f'  {side} x={x}: ' + ' | '.join(out))
    im.thumbnail((600, 600))
    im.save(f'{art}\\thumb_{nome}.png')

perfil(base + r'\pump_station.png', 0.48, (1750, 630), 'bomba')
perfil(base + r'\pipes\cano_longo_industrial.png', 0.11, (0, 0), 'cano')
perfil(base + r'\pipes\passagem_parede_flange.png', 0.09, (3440, 618), 'passagem')
