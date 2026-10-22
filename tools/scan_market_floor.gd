extends SceneTree

var world: Node2D
var cam: Camera2D

func _init() -> void:
	world = load("res://maps/sucateia/sucateia.tscn").instantiate()
	root.add_child(world)
	
	var pcam = world.get_node_or_null("Structures/Player/Camera")
	if pcam:
		pcam.enabled = false
	
	cam = Camera2D.new()
	cam.enabled = true
	cam.zoom = Vector2(1.0, 1.0)
	world.add_child(cam)
	
	var floor_layer: TileMapLayer = world.get_node_or_null("MarketDistrict/MarketFloor")
	assert(floor_layer != null, "MarketFloor ausente!")
	
	# Pegar o bounding box de MarketFloor
	var used = floor_layer.get_used_cells()
	var min_x = 999999
	var max_x = -999999
	var min_y = 999999
	var max_y = -999999
	for cell in used:
		var lp = floor_layer.map_to_local(cell)
		min_x = min(min_x, lp.x)
		max_x = max(max_x, lp.x)
		min_y = min(min_y, lp.y)
		max_y = max(max_y, lp.y)
	
	print("MarketFloor bounds: X=[", min_x, ", ", max_x, "] Y=[", min_y, ", ", max_y, "]")
	
	# Vamos testar pontos na faixa central x entre 900 e 1300 a cada 150 px em Y
	var test_points = []
	for y in range(int(min_y), int(max_y), 200):
		test_points.append(Vector2(1100, y))
	
	_run_captures(test_points)

func _run_captures(points: Array) -> void:
	var player = world.get_node("Structures/Player")
	for i in range(points.size()):
		var p = points[i]
		cam.position = p
		player.position = p
		await process_frame
		await process_frame
		await process_frame
		var img = root.get_viewport().get_texture().get_image()
		var out_path = "C:/Users/Usuario/.gemini/antigravity/brain/2b874476-d390-4406-8b89-b8e275f8f9f1/market_y_%d.png" % int(p.y)
		img.save_png(out_path)
		print("Salvo: ", out_path)
	quit(0)
