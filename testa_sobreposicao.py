from PIL import Image
import numpy as np

im_bleachers = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\arena_arquibancada_meia_lua_clean.png').convert("RGBA")
im_arena = Image.open(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\captura_arena_arredondada_obra_prima.png').convert("RGBA")

# Vamos criar um canvas grande
canvas = Image.new("RGBA", (1800, 1400), (0, 0, 0, 0))

# Se a arquibancada fica na borda superior norte da arena:
# Vamos testar colocar a arena no centro inferior, e a arquibancada no topo norte
arena_pos_x = (1800 - im_arena.width) // 2
arena_pos_y = 500

bleachers_pos_x = (1800 - im_bleachers.width) // 2
bleachers_pos_y = 100

canvas.paste(im_bleachers, (bleachers_pos_x, bleachers_pos_y), im_bleachers)
canvas.paste(im_arena, (arena_pos_x, arena_pos_y), im_arena)

canvas.save(r'C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\teste_sobreposicao_bleachers_arena.png')
print("Teste sobreposicao salvo!")
