extends Node2D
var frames := 0
var capture := ""
func _ready() -> void:
	get_node("/root/LayerTravel").setup(self,"underground")
	for arg in OS.get_cmdline_user_args():
		if arg.begins_with("--capture="):capture=arg.trim_prefix("--capture=")
	if capture!="":
		var camera: Camera2D=$Structures/Player/Camera;camera.position_smoothing_enabled=false
		if capture=="fundo_full":$Structures/Player.position=Vector2(2210,1400);camera.zoom=Vector2(.34,.34);camera.limit_left=200;camera.limit_right=4200;camera.limit_top=-300;camera.limit_bottom=3000
		else:
			var room: Node2D=get_node("Rooms/"+capture.trim_prefix("fundo_"));$Structures/Player.position=room.position;camera.zoom=Vector2(.9,.9)
		$HUD.visible=false
func is_walkable(point: Vector2) -> bool:
	for polygon in get_meta("water_polygons",[]):
		if Geometry2D.is_point_in_polygon(point,polygon):return false
	return $GroundFloor.get_cell_source_id($GroundFloor.local_to_map(point))!=-1
func _process(_delta: float) -> void:
	if capture=="":return
	frames+=1
	if frames==80:
		await RenderingServer.frame_post_draw
		var error := get_viewport().get_texture().get_image().save_png("res://maps/fundo_ferro/preview_"+capture+".png")
		print("CAPTURE FUNDO ",capture," ",error," draw_calls=",Performance.get_monitor(Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME)," nodes=",Performance.get_monitor(Performance.OBJECT_NODE_COUNT));get_tree().quit(error)
func _unhandled_input(event: InputEvent) -> void:
	if event is InputEventKey and event.pressed and not event.echo and event.keycode==KEY_F1:$HUD.visible=not $HUD.visible
