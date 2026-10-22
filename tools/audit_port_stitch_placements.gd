extends SceneTree
func _initialize() -> void:call_deferred("run")
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	var dock: Node2D=world.get_node("DocasDistrict");world.get_node("Structures/Player").set_physics_process(false)
	var zones := {"Triagem":Rect2(2360,1430,300,160),"Norte":Rect2(3190,530,200,150),"Almox":Rect2(3000,840,220,150),"Sul":Rect2(2750,1180,220,160),"Chegada":Rect2(2300,1260,150,200),"Carga":Rect2(2730,1590,380,100)}
	var report := {};var query := PhysicsShapeQueryParameters2D.new();query.collision_mask=1;var shape := RectangleShape2D.new();query.shape=shape;var space := world.get_world_2d().direct_space_state
	for zone in zones:
		var sizes_report := {};var bounds: Rect2=zones[zone]
		for size in [Vector2(120,18),Vector2(64,18),Vector2(35,14)]:
			shape.size=size;var points: Array=[]
			for y in range(int(bounds.position.y),int(bounds.end.y),6):
				for x in range(int(bounds.position.x),int(bounds.end.x),6):
					var point := Vector2(x,y);var valid := true
					for landing in dock.get_node("SafeLandings").get_children():
						if point.distance_to(landing.position)<35+size.length()*.5:valid=false
					for access in world.get_node("LayerEntrances").get_children():
						if access is Area2D and point.distance_to(access.position)<75+size.length()*.5:valid=false
					# Occupancy outside approved circulation strips: preserve their full authored width.
					for route in dock.get_node("Routes").get_children():
						var ends: PackedVector2Array=route.get_meta("points");var closest := Geometry2D.get_closest_point_to_segment(point,ends[0],ends[1]);var width: float=route.get_meta("clear_width")
						var lateral: float=size.y*.5 if absf(ends[0].y-ends[1].y)<1 else size.x*.5
						if point.distance_to(closest)<width*.5+lateral+2:valid=false
					for corner in [Vector2(-.5,-.5),Vector2(.5,-.5),Vector2(.5,.5),Vector2(-.5,.5)]:
						if not world.is_surface_walkable(point+corner*size):valid=false
					if not valid:continue
					query.transform=Transform2D(0,point);query.exclude=dock.water_exclusions(point)
					if space.intersect_shape(query,1).is_empty():points.append([x,y])
			sizes_report[str(size)]=points;print("STITCH placement ",zone," ",size," outside routes=",points.size())
		report[zone]=sizes_report
	var output := FileAccess.open("res://tools/port_stitch_placements.json",FileAccess.WRITE);output.store_string(JSON.stringify(report,"\t"));output.close();world.queue_free();await process_frame;quit(0)
