extends Node2D
@export var region_id := ""
var frame := 0
var capture := false
var capture_mode := "region"
func _ready() -> void:
	var travel := get_node_or_null("/root/RegionTravel")
	if travel: travel.setup(self,region_id)
	$Structures/Player.spawn_point = $Structures/Player.position
	for arg in OS.get_cmdline_user_args():
		if arg == "--capture=region": capture = true
		if arg == "--capture=detail":
			capture = true
			capture_mode = "detail"
	if capture:
		$Structures/Player.set_physics_process(false)
		$Structures/Player/Camera.position_smoothing_enabled = false
		$Structures/Player/Camera.position = Vector2(1000,740)-$Structures/Player.position
		$Structures/Player/Camera.zoom = Vector2(.63,.63)
		$MapInfo/Panel.visible = false
		if capture_mode == "detail":
			var at: Vector2 = $RouteMarkers/Landmark.position
			$Structures/Player.position = at+Vector2(0,80)
			$Structures/Player/Camera.position = Vector2(0,-90)
			$Structures/Player/Camera.zoom = Vector2(1,1)
func _process(_delta: float) -> void:
	if not capture: return
	for portal in $RegionPortals.get_children(): portal.get_node("Prompt").visible = false; portal.get_node("Sign").visible = false
	frame += 1
	if frame == 80:
		await RenderingServer.frame_post_draw
		var path := scene_file_path.get_base_dir()+"/preview_"+region_id+".png"
		if capture_mode == "detail": path = path.replace(".png","_detail.png")
		var error := get_viewport().get_texture().get_image().save_png(path)
		print("CAPTURE ",region_id," ",error," draws=",Performance.get_monitor(Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME)," nodes=",Performance.get_monitor(Performance.OBJECT_NODE_COUNT))
		get_tree().quit(error)
