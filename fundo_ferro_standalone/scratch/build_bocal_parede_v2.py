"""Monta tubo_bocal_parede_v2.png: bloco de parede (Nano Banana r2) + toco de cano real horizontal.

O toco gerado pela IA saiu afunilado/inclinado. Ele é removido (fora do bloco) e coberto (sobre o bloco)
por uma faixa horizontal recortada do próprio cano_longo_industrial.png, garantindo o mesmo diâmetro,
pátina e luz do cano que chega.
"""
import sys
import numpy as np
from PIL import Image, ImageDraw
sys.path.insert(0, r"c:\Users\Usuario\Documents\jogo\tools")
from process_asset_v3 import process, ROOTS  # noqa: E402

ART = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b"
SRC = ART + r"\tubo_bocal_parede_r2_1791331161794.jpg"
PROMPT = r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\scratch\prompts\tubo_bocal_parede_v2.txt"
TMP = ART + r"\scratch_bocal_parede_composto.png"

# 1) Recorte limpo do bloco (sem salvar nos destinos ainda): reaproveita o pipeline padrão num arquivo temporário
src = Image.open(SRC).convert("RGB")
W, H = src.size
canvas = Image.new("RGB", (W, H), (255, 0, 255))
# 2) Apaga o toco fora do bloco (o bloco começa em x≈200)
block = src.crop((200, 0, W, H))
canvas.paste(block, (200, 0))

# 3) Faixa de cano real: diâmetro 320 px, centro y=532, de x=60 até x=440
pipe = Image.open(r"c:\Users\Usuario\Documents\jogo\fundo_ferro_standalone\assets\pipes\cano_longo_industrial.png").convert("RGBA")
tube = pipe.crop((420, 42, 820, 272))  # trecho liso, sem anéis
D, CY, X0, X1 = 320, 532, 60, 440
tube = tube.resize((X1 - X0, D), Image.Resampling.LANCZOS)
canvas_rgba = canvas.convert("RGBA")
canvas_rgba.alpha_composite(tube, (X0, CY - D // 2))

# 4) Anel de topo na ponta esquerda (flange curto) para o encaixe ler como peça
ring = pipe.crop((205, 30, 345, 286)).resize((60, D + 30), Image.Resampling.LANCZOS)
canvas_rgba.alpha_composite(ring, (X0 - 10, CY - (D + 30) // 2))

out = Image.new("RGB", (W, H), (255, 0, 255))
out.paste(canvas_rgba, (0, 0), canvas_rgba)
out.save(TMP)
process(TMP, "pipes", "tubo_bocal_parede_v2.png", PROMPT, 0.25)
print("centro do toco (px na imagem bruta): y=", CY, " ponta esquerda x=", X0 - 10)
