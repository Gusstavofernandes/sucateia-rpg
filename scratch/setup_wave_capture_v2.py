path = 'scripts/world/sucateia.gd'
content = open(path, 'r', encoding='utf-8').read()

target = '	capture_frames += 1\n\tif capture_frames == 80:'
replacement = '''	capture_frames += 1
	if capture_mode == "wave_anim":
		if capture_frames >= 25 and (capture_frames - 25) % 5 == 0 and capture_frames <= 85:
			await RenderingServer.frame_post_draw
			var idx := (capture_frames - 25) / 5
			var path := "res://maps/sucateia/wave_frame_" + str(idx) + ".png"
			get_viewport().get_texture().get_image().save_png(path)
			print("WAVE_FRAME ", idx)
		if capture_frames == 90:
			get_tree().quit(0)
	elif capture_frames == 80:'''

if target in content:
    open(path, 'w', encoding='utf-8').write(content.replace(target, replacement, 1))
    print('wave_anim frames configurados com sucesso!')
else:
    print('Target nao encontrado!')
