path = 'scripts/world/sucateia.gd'
content = open(path, 'r', encoding='utf-8').read()

target = '''	if capture_mode == "wave_anim":
\t\tif capture_frames >= 25 and (capture_frames - 25) % 5 == 0 and capture_frames <= 85:
\t\t\tawait RenderingServer.frame_post_draw
\t\t\tvar idx := (capture_frames - 25) / 5
\t\t\tvar path := "res://maps/sucateia/wave_frame_" + str(idx) + ".png"
\t\t\tget_viewport().get_texture().get_image().save_png(path)
\t\t\tprint("WAVE_FRAME ", idx)
\t\tif capture_frames == 90:
\t\t\tget_tree().quit(0)
\telif capture_frames == 80:'''

replacement = '''	if capture_frames == 80:'''

if target in content:
    open(path, 'w', encoding='utf-8').write(content.replace(target, replacement, 1))
    print('Restaurado com sucesso!')
else:
    print('Target nao encontrado!')
