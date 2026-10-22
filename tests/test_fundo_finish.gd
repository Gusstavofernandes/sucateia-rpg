extends "res://tests/test_docas_contacts.gd"
func run() -> void:
	var world: Node2D=load("res://maps/fundo_ferro/fundo_ferro.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	if not check(world.has_node("FundoFunctionalFinish/Functions"),"Seven underground environmental functions not integrated"):return
	var finish: Node2D=world.get_node("FundoFunctionalFinish");var paths: Array=[]
	for id in ["PocoVelho","Bombas","Descarte","Maquinas","Reservatorio","Ruinas","Valvulas"]:
		if not check(finish.get_node("Functions").has_node(id),"Environmental function missing "+id):return
		var fn: Node2D=finish.get_node("Functions/"+id)
		if not check(fn.get_meta("art_paths",[]).size()>0,"Function has only label/marker "+id):return
		for path in fn.get_meta("art_paths"):
			var art: CanvasItem=world.get_node_or_null(path)
			if not check(art!=null and art.is_visible_in_tree(),"Functional art hidden "+id):return
			paths.append(path)
	var route_root: Node=world.get_node("Routes")
	var manifold: Sprite2D=finish.get_node("Functions/Valvulas/DistributionManifold")
	for box: Rect2 in [Rect2(27,176,48,28),Rect2(181,176,48,28),Rect2(79,187,44,26),Rect2(133,187,44,26)]:
		var support: Vector2=manifold.global_position+(box.get_center()-Vector2(128,112))*0.52
		if not check(world.call("is_walkable",support),"Valve manifold support is not on dry walkable floor at "+str(support)):return
	var collapse: Sprite2D=finish.get_node("Functions/Ruinas/SupportedCollapsedCorner")
	for pixel: Vector2 in [Vector2(180,910),Vector2(520,922),Vector2(1160,922),Vector2(1515,910)]:
		var support: Vector2=collapse.to_global(pixel-Vector2(848.5,463.5))
		if not check(world.call("is_walkable",support),"Collapsed ruin support is not on dry floor at "+str(support)):return
	var ruin_route_clearance:=INF
	for route: Node in route_root.get_children():
		var route_points: PackedVector2Array=route.get_meta("points")
		for index in range(route_points.size()-1):
			ruin_route_clearance=minf(ruin_route_clearance,_point_segment_distance(Vector2(1580,1025),route_points[index],route_points[index+1]))
	if not check(ruin_route_clearance>=45.0,"Collapsed ruin exceeds safe margin into route clearance: "+str(ruin_route_clearance)):return
	var feed: Line2D=finish.get_node("Functions/Valvulas/FeedSpur")
	var return_line: Line2D=finish.get_node("Functions/Valvulas/ReturnSpur")
	var feed_socket:=manifold.to_global(Vector2(-118,-66))
	var return_socket:=manifold.to_global(Vector2(118,39))
	if not check(feed.to_global(feed.points[feed.points.size()-1]).distance_to(feed_socket)<2.0,"Valve feed spur misses manifold socket"):return
	if not check(return_line.to_global(return_line.points[0]).distance_to(return_socket)<2.0,"Valve return spur misses manifold socket"):return
	if not check(world.call("is_walkable",feed.to_global(feed.points[0])) and world.call("is_walkable",return_line.to_global(return_line.points[return_line.points.size()-1])),"Valve spurs leave the dry service margin"):return
	if not check(finish.has_node("Networks") and finish.get_node("Networks").get_child_count()==16,"All eight source routes need paired underlays"):return
	for route: Node in route_root.get_children():
		var id:=str(route.name)
		var base: Line2D=finish.get_node("Networks/"+id+"_ProtectedSleeve")
		var tracer: Line2D=finish.get_node("Networks/"+id+"_Inlay")
		var original: PackedVector2Array=route.get_meta("points")
		if not check(base.points==original and tracer.points==original,"Service overlay diverged from original route "+id):return
		if not check(base.get_meta("source")==tracer.get_meta("source") and base.get_meta("destination")==tracer.get_meta("destination"),"Network terminal metadata disagrees "+id):return
		if not check(str(base.get_meta("source"))!="service_corridor" and str(base.get_meta("destination"))!="service_corridor","Unresolved network endpoints "+id):return
		if not check(base.get_meta("route_id")==id and tracer.get_meta("route_id")==id,"Unlabelled authored service route "+id):return
	if not check(not _has_physics_body(finish),"Environmental finish adds collision/changes walking footprint"):return
	var before: Node=load("res://tools/checkpoints/fundo_before_finish_2026_10_04.tscn").instantiate();var current: Node=load("res://maps/fundo_ferro/fundo_ferro.tscn").instantiate()
	for name in ["Rooms","Routes","LayerEntrances","LayerArrivals"]:
		for old in before.get_node(name).get_children():
			var same: Node=current.get_node(name).get_node_or_null(str(old.name))
			if not check(same!=null and old.transform==same.transform,"Underground topology/access moved "+name+"/"+str(old.name)):return
			if old.has_meta("points") and not check(old.get_meta("points")==same.get_meta("points"),"Original route changed"):return
	var old_floor: TileMapLayer=before.get_node("GroundFloor");var new_floor: TileMapLayer=current.get_node("GroundFloor")
	if not check(old_floor.get_used_cells()==new_floor.get_used_cells(),"Underground floor territory changed"):return
	for cell in old_floor.get_used_cells():
		if not check(old_floor.get_cell_source_id(cell)==new_floor.get_cell_source_id(cell) and old_floor.get_cell_atlas_coords(cell)==new_floor.get_cell_atlas_coords(cell),"Underground floor cell replaced"):return
	if not check(before.get_meta("water_polygons")==current.get_meta("water_polygons"),"Water geometry altered"):return
	before.free();current.free();print("PASS: seven environmental functions have visible art, connected service networks and preserved rooms/routes/accesses/floor/water")
	world.queue_free();await process_frame;quit(0)

func _has_physics_body(node: Node) -> bool:
	if node is PhysicsBody2D or node is Area2D:
		return true
	for child: Node in node.get_children():
		if _has_physics_body(child):
			return true
	return false

func _point_segment_distance(point: Vector2, start: Vector2, end: Vector2) -> float:
	var delta:=end-start
	if delta.length_squared()<=0.001:
		return point.distance_to(start)
	var weight:=clampf((point-start).dot(delta)/delta.length_squared(),0.0,1.0)
	return point.distance_to(start+delta*weight)
