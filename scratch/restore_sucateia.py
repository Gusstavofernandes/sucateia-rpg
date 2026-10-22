path = 'scripts/world/sucateia.gd'
content = open(path, 'r', encoding='utf-8').read()

target = '\tif capture_mode == "wave_anim":\n\t\tif capture_frames >= 30 and (capture_frames - 30) % 5 == 0 and capture_frames <= 90:\n\t\t\tawait RenderingServer.frame_post_draw\n\t\t\tvar idx := (capture_frames - 30) / 5\n\t\t\tvar path := "res://maps/sucateia/wave_frame_" + str(idx) + ".png"\n\t\t\tget_viewport().get_texture().get_image().save_png(path)\n\t\t\tprint("WAVE_FRAME ", idx)\n\t\tif capture_frames == 95:\n\t\t\tget_tree().quit(0)\n\telif capture_frames == 80:'

replacement = '\tif capture_frames == 80:'

if target in content:
    open(path, 'w', encoding='utf-8').write(content.replace(target, replacement, 1))
    print('sucateia.gd restaurado ao padrao normal!')
else:
    print('Target nao encontrado!')
