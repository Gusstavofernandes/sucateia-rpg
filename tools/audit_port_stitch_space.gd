extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	var dock: Node2D=world.get_node("DocasDistrict");var player: CharacterBody2D=world.get_node("Structures/Player");player.set_physics_process(false)
	var zones := {"TriagemMolhada":Rect2(2360,1460,300,140),"EsperaDeCarga":Rect2(2730,1605,380,65),"ServicosNorte":Rect2(3220,550,140,120),"Almoxarifado":Rect2(3030,870,155,110),"ServicosSul":Rect2(2780,1215,155,130),"BocaDocaLeste":Rect2(2110,1560,225,200),"BocaForjas":Rect2(2880,140,260,240),"BocaPoco":Rect2(1180,1480,260,180)}
	var entrances: Array[Vector2]=[];var landings: Array[Vector2]=[]
	for node in world.get_node("LayerEntrances").get_children():if node is Area2D:entrances.append(node.position)
	for node in dock.get_node("SafeLandings").get_children():landings.append(node.position)
	var query := PhysicsShapeQueryParameters2D.new();var shape := RectangleShape2D.new();shape.size=Vector2(60,24);query.shape=shape;query.collision_mask=1;var space := world.get_world_2d().direct_space_state;var report := {}
	for label in zones:
		var bounds: Rect2=zones[label];var free: Array[Vector2]=[]
		for y in range(int(bounds.position.y),int(bounds.end.y),12):
			for x in range(int(bounds.position.x),int(bounds.end.x),12):
				var point := Vector2(x,y);var valid := true
				for access in entrances:if point.distance_to(access)<110:valid=false
				for landing in landings:if point.distance_to(landing)<70:valid=false
				for corner in [Vector2(-30,-12),Vector2(30,-12),Vector2(-30,12),Vector2(30,12)]:
					if not world.is_surface_walkable(point+corner):valid=false
				if not valid:continue
				query.transform=Transform2D(0,point);query.exclude=dock.water_exclusions(point)
				if space.intersect_shape(query,1).is_empty():free.append(point)
		var points: Array=[];for point in free:points.append([point.x,point.y])
		report[label]={"study_bounds":[bounds.position.x,bounds.position.y,bounds.size.x,bounds.size.y],"footprint_checked":[60,24],"free_dry_candidates":points,"placement_certified":false}
		print("STITCH survey ",label," dry free60x24 foot candidates=",free.size())
	var file := FileAccess.open("res://tools/port_stitch_space.json",FileAccess.WRITE);file.store_string(JSON.stringify(report,"\t"));file.close()
	# Instanced overview only: leave the authored camera/scene/scripts unchanged.
	player.position=Vector2(2700,1280);dock.update_player_water();var camera: Camera2D=player.get_node("Camera");camera.position_smoothing_enabled=false;camera.zoom=Vector2.ONE*.48;camera.offset=Vector2(-160,-110);camera.limit_left=-4500;camera.limit_right=7800;camera.limit_top=-3400;camera.limit_bottom=4000;camera.reset_smoothing();world.get_node("MapInfo/Panel").hide()
	for portal in world.get_node("RegionPortals").get_children():portal.get_node("Prompt").hide();portal.get_node("Sign").hide()
	for i in range(80):await process_frame
	await RenderingServer.frame_post_draw
	var error := root.get_texture().get_image().save_png("res://maps/sucateia/preview_stitch_before.png")
	print("CAPTURE res://maps/sucateia/preview_stitch_before.png ",error," draw_calls=",Performance.get_monitor(Performance.RENDER_TOTAL_DRAW_CALLS_IN_FRAME)," nodes=",Performance.get_monitor(Performance.OBJECT_NODE_COUNT))
	world.queue_free();await process_frame;quit(error)
