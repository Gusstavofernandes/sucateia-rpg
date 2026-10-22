from PIL import Image

src = r"C:\Users\Usuario\.gemini\antigravity\brain\24487463-0c7d-44b2-91e8-4982c2631f5b\ponte_travessia_unificada_arena_1792595041626.jpg"
im = Image.open(src)
print("Generated image size:", im.size, im.mode)

preview = im.resize((360, int(360 * im.size[1] / im.size[0])))
preview.save("scratch/preview_new_bridge.png")
print("Saved preview to scratch/preview_new_bridge.png")
