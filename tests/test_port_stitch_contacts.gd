extends "res://tests/test_docas_contacts.gd"
func tile_floor(point: Vector2,node: Node) -> bool:
	if node is TileMapLayer and String(node.name).to_lower().contains("floor"):
		if node.get_cell_source_id(node.local_to_map(node.to_local(point)))!=-1:return true
	for child in node.get_children():if tile_floor(point,child):return true
	return false
func run() -> void:
	var world: Node2D=load("res://maps/sucateia/sucateia.tscn").instantiate();root.add_child(world);current_scene=world;await physics_frame;await physics_frame
	var dock: Node2D=world.get_node("DocasDistrict");world.get_node("Structures/Player").set_physics_process(false);var art: Array=[]
	for sprite in dock.get_node("WorkingDecks").get_children():
		if not sprite is Sprite2D or String(sprite.name)=="RampaNavalLeste":continue
		var img: Image=sprite.texture.get_image();if img.is_compressed():img.decompress()
		art.append([sprite,img])
	var samples := 0
	for object in world.get_node("Structures/PortStitchArchitecture").get_children():
		var sprite: Sprite2D=object.get_node("Artwork");var canvas := Vector2(sprite.texture.get_size());var envelope := Rect2();var first := true
		for bounds in object.get_meta("contact_rectangles_native"):
			for native in [bounds.position+Vector2(1,1),bounds.end-Vector2(1,1),bounds.get_center(),Vector2(bounds.position.x+1,bounds.end.y-1),Vector2(bounds.end.x-1,bounds.position.y+1)]:
				var point := sprite.to_global(native-canvas*.5)
				if not check(world.is_surface_walkable(point) and (dock_painted(point,art) or tile_floor(point,world)),"Stitch foot lacks dry painted support "+str(object.name)+" "+str(point)):return
				samples+=1
			var physical := Rect2(sprite.to_global(bounds.position-canvas*.5),bounds.size*sprite.scale)
			for access in world.get_node("LayerEntrances").get_children():
				if not access is Area2D:continue
				var closest := Vector2(clampf(access.position.x,physical.position.x,physical.end.x),clampf(access.position.y,physical.position.y,physical.end.y))
				if not check(closest.distance_to(access.position)>=75,"New base invades75px F reserve "+str(object.name)):return
			for landing in dock.get_node("SafeLandings").get_children():
				var closest := Vector2(clampf(landing.position.x,physical.position.x,physical.end.x),clampf(landing.position.y,physical.position.y,physical.end.y))
				if not check(closest.distance_to(landing.position)>=35,"New base invades35px R reserve "+str(object.name)):return
			for route in dock.get_node("Routes").get_children():
				var ends: PackedVector2Array=route.get_meta("points");var width: float=route.get_meta("clear_width");var strip: Rect2
				if absf(ends[0].y-ends[1].y)<1:strip=Rect2(Vector2(minf(ends[0].x,ends[1].x),ends[0].y-width*.5),Vector2(absf(ends[0].x-ends[1].x),width))
				else:strip=Rect2(Vector2(ends[0].x-width*.5,minf(ends[0].y,ends[1].y)),Vector2(width,absf(ends[0].y-ends[1].y)))
				if not check(not physical.intersects(strip),"New base narrows approved corridor "+str(route.name)+" "+str(object.name)):return
			envelope=physical if first else envelope.merge(physical);first=false
		if not check(absf(object.global_position.y-envelope.end.y)<.1,"New object depth differs from real foot "+str(object.name)):return
	var before: Node=load("res://tools/checkpoints/sucateia_before_port_stitch.tscn").instantiate();var original: Array=before.get_node("DocasDistrict").get_meta("walk_polygons");var current: Array=dock.get_meta("walk_polygons")
	if not check(current.size()==original.size()+1,"Unapproved broad floor expansion"):return
	for i in range(original.size()):if not check(original[i]==current[i],"Approved Dock floor changed"):return
	var port: Node2D=world.get_node("PortStitchInfrastructure");var bay: PackedVector2Array=port.get_meta("supported_bay");var min_point := bay[0];var max_point := bay[0]
	var endpoints: Array[Vector2]=[];var terminals: Array[Vector2]=[];terminals.assign(port.get_meta("drain_sockets"));terminals.append(port.get_meta("collector_source"));terminals.append(port.get_meta("drain_destination"))
	for piece in port.get_node("ServiceRigging").get_children():
		if piece.has_meta("ports_world"):
			for point in piece.get_meta("ports_world"):endpoints.append(point)
	for i in range(endpoints.size()):
		var joined := false
		for j in range(endpoints.size()):if i!=j and endpoints[i].distance_to(endpoints[j])<.1:joined=true
		for terminal in terminals:if endpoints[i].distance_to(terminal)<.1:joined=true
		if not check(joined,"Unconnected branch pipe flange "+str(endpoints[i])):return
	for terminal in terminals:
		var joined := false
		for point in endpoints:if point.distance_to(terminal)<.1:joined=true
		if not check(joined,"Drain functional terminal disconnected"):return
	if not check(not world.is_surface_walkable(port.get_meta("drain_destination")),"Drain outlet fails to reach channel water"):return
	var traction: Line2D=port.get_node("ServiceRigging/GuiaAtePoco")
	if not check(traction.points[0].distance_to(port.get_meta("winch_socket"))<.1 and traction.points[-1].distance_to(port.get_meta("winch_wall_lug"))<.1,"Winch guide detached from sockets"):return
	for point in bay:min_point=min_point.min(point);max_point=max_point.max(point)
	if not check(max_point.x-min_point.x<240 and max_point.y-min_point.y<130,"Equipment bay became district extension"):return
	for path in port.get_meta("opened_seam_shapes"):
		if not check(world.get_node(path).disabled,"Old water seam still blocks supported bay"):return
	var player: CharacterBody2D=world.get_node("Structures/Player");player.position=Vector2(2983,887);dock.update_player_water()
	if not check(player.move_and_collide(Vector2(0,-20))==null,"Supported bay entrance blocked"):return
	player.position=Vector2(2983,883);dock.update_player_water()
	if not check(player.move_and_collide(Vector2(160,0))!=null,"Bay permits escape into water"):return
	before.free();print("PASS: ",samples," new foot contacts on painted dry floors; feet-based depth;75px F/35px R reserves and original route widths clear; original Dock polygons unchanged; one compact bay with open seam and guarded water")
	world.queue_free();await process_frame;quit(0)
