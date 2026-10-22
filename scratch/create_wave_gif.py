import os
from PIL import Image

maps_dir = "maps/sucateia"
brain_dir = "C:/Users/Usuario/.gemini/antigravity/brain/24487463-0c7d-44b2-91e8-4982c2631f5b"

frames = []
for i in range(13):
    p = os.path.join(maps_dir, f"wave_frame_{i}.png")
    if os.path.exists(p):
        img = Image.open(p).convert("RGB")
        frames.append(img)

if frames:
    # 1. Salvar GIF animado completo
    gif_path = os.path.join(maps_dir, "animacao_onda_praia.gif")
    brain_gif = os.path.join(brain_dir, "animacao_onda_praia.gif")
    
    # Redimensionar suavemente para otimizar tamanho do GIF (ex: 800px de largura)
    w, h = frames[0].size
    new_w = 800
    new_h = int(h * (new_w / w))
    opt_frames = [f.resize((new_w, new_h), Image.Resampling.LANCZOS) for f in frames]
    
    # Fazer loop de ida e volta (ping-pong) para ciclo infinito perfeito
    loop_frames = opt_frames + opt_frames[-2:0:-1]
    
    loop_frames[0].save(
        gif_path,
        save_all=True,
        append_images=loop_frames[1:],
        duration=110, # 110ms por frame (~9 FPS suave)
        loop=0
    )
    loop_frames[0].save(
        brain_gif,
        save_all=True,
        append_images=loop_frames[1:],
        duration=110,
        loop=0
    )
    print("GIF animado salvo em:", brain_gif)
    
    # 2. Salvar 3 momentos estáticos chave em alta resolução
    # Fase 1: Recuo
    frames[0].save(os.path.join(brain_dir, "onda_fase1_recuo.png"))
    # Fase 2: Avanço
    frames[5].save(os.path.join(brain_dir, "onda_fase2_avanco.png"))
    # Fase 3: Pico / Arrebentação
    frames[9].save(os.path.join(brain_dir, "onda_fase3_arrebentacao.png"))
    print("Frames-chave salvos com sucesso!")
else:
    print("Nenhum frame encontrado!")
