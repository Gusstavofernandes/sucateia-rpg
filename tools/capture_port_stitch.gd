extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var mode := "stitch_overview"
	for arg in OS.get_cmdline_user_args():if arg.begins_with("--capture="):mode=arg.trim_prefix("--capture=")
	var views := {"stitch_overview":[Vector2(2700,1280),.48,Vector2(-160,-110)],"stitch_sorting":[Vector2(2500,1575),1.15,Vector2(0,-75)],"stitch_service":[Vector2(2983,925),1.5,Vector2(45,-55)],"stitch_urban":[Vector2(3130,224),1.2,Vector2(-40,0)],"stitch_mouths":[Vector2(1296,1572),1.15,Vector2(55,-50)]}
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false);var camera: Camera2D=player.get_node("Camera");var view: Array=views[mode];player.position=view[0];world.get_node("DocasDistrict").update_player_water();camera.zoom=Vector2.ONE*view[1];camera.offset=view[2];camera.position_smoothing_enabled=false;camera.limit_left=-4500;camera.limit_right=7800;camera.limit_top=-3400;camera.limit_bottom=4000;camera.reset_smoothing();world.get_node("MapInfo/Panel").hide()
	for portal in world.get_node("RegionPortals").get_children():portal.get_node("Prompt").hide();portal.get_node("Sign").hide()
	for i in range(80):await process_frame
	await RenderingServer.frame_post_draw;var path := "res://maps/sucateia/preview_"+mode+".png";var error := root.get_texture().get_image().save_png(path)
	print("CAPTURE ",path," ",error," draw_calls=",Performance.get_monitor(Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME)," nodes=",Performance.get_monitor(Performance.OBJECT_NODE_COUNT));world.queue_free();await process_frame;quit(error)
