extends SceneTree
var world: Node2D
var data: Dictionary
var sectors := {}
var positions := {"centre":Vector2.ZERO,"alto":Vector2(0,-1900),"forjas":Vector2(2400,0),"cabos":Vector2(2400,1900),"fundo":Vector2(0,1900),"docas":Vector2(2400,3800),"coroa":Vector2(2400,-1900),"chamines":Vector2(4800,-1900),"grande":Vector2(4800,0),"via_cais":Vector2(4800,3800),"banco":Vector2(7200,3800),"engrenopolis":Vector2(7200,1900),"via_engrenagens":Vector2(7200,0),"eng_nucleo":Vector2(9600,0),"eng_corredor":Vector2(9600,1900),"galeria":Vector2(0,3800)}
var grid := AStarGrid2D.new()
func _initialize() -> void: call_deferred("run")
func own(node: Node) -> void:
	for child in node.get_children():
		child.scene_file_path=""
		child.owner=world
		own(child)
func discard(node: Node) -> void:
	if node: node.get_parent().remove_child(node);node.free()
func sprite(file: String, point: Vector2, size: Vector2, parent: Node, angle: float=0) -> void:
	var art := Sprite2D.new()
	art.texture=load("res://assets/"+file)
	art.position=point
	art.scale=size/Vector2(art.texture.get_size())
	art.rotation=angle
	parent.add_child(art)
func run() -> void:
	data=JSON.parse_string(FileAccess.get_file_as_string("res://maps/ferrugem_baixa/region.json"))
	world=load("res://tools/checkpoints/sucateia_before_world_extension.tscn").instantiate()
	world.set_script(null)
	root.add_child(world)
	sectors.centre=world
	var group := Node2D.new();group.name="RegionalSectors";world.add_child(group)
	for id in data:
		if id=="centre":continue
		var sector: Node2D=load(data[id].scene).instantiate()
		sector.set_script(null)
		sector.scene_file_path=""
		sector.name=id
		sector.position=positions[id]
		discard(sector.get_node("Structures/Player"))
		discard(sector.get_node_or_null("MapInfo"))
		for child in sector.get_children():
			if child is Polygon2D and child.z_index==-40:discard(child)
		group.add_child(sector)
		sectors[id]=sector
	for id in sectors:
		var sector: Node2D=sectors[id]
		discard(sector.get_node_or_null("RegionPortals"))
		# Remove duplicated distant landmarks now that their real sector is present.
		var continuity := sector.get_node_or_null("RegionalContinuity")
		if continuity:
			for child in continuity.get_children():
				if child is Sprite2D and child.z_index==-35:discard(child)
		for edge in data[id].continuity.values():
			if not edge.opening:continue
			var cap := Vector2(edge.anchor[0],edge.anchor[1])+Vector2(edge.direction[0],edge.direction[1])*158
			for child in sector.get_children():
				if child is StaticBody2D and child.position.distance_to(cap)<3:discard(child)
	discard(world.get_node_or_null("Ground/NorthBoundary"))
	discard(world.get_node_or_null("DistantCity"))
	# Open the gallery's cutaway rock at its maintenance entry, preserving room walls elsewhere.
	var gallery: Node2D=sectors.galeria
	var entrance := Rect2(-40,1020,380,220)
	for body in gallery.get_children():
		if not body is StaticBody2D:continue
		var shape_node: CollisionShape2D=body.get_child(0)
		if not shape_node.shape is RectangleShape2D:continue
		var bounds := Rect2(body.position-shape_node.shape.size*.5,shape_node.shape.size)
		if not bounds.intersects(entrance):continue
		var cut := bounds.intersection(entrance)
		var pieces := [Rect2(bounds.position,Vector2(cut.position.x-bounds.position.x,bounds.size.y)),Rect2(Vector2(cut.end.x,bounds.position.y),Vector2(bounds.end.x-cut.end.x,bounds.size.y)),Rect2(Vector2(cut.position.x,bounds.position.y),Vector2(cut.size.x,cut.position.y-bounds.position.y)),Rect2(Vector2(cut.position.x,cut.end.y),Vector2(cut.size.x,bounds.end.y-cut.end.y))]
		discard(body)
		for piece in pieces:
			if piece.size.x<1 or piece.size.y<1:continue
			var replacement := StaticBody2D.new();replacement.position=piece.get_center()
			var collision := CollisionShape2D.new();var rectangle := RectangleShape2D.new();rectangle.size=piece.size;collision.shape=rectangle
			replacement.add_child(collision);gallery.add_child(replacement)
	for art in gallery.find_children("*","Sprite2D",true,false):
		if art.texture and art.texture.resource_path.ends_with("retaining_edge.png") and entrance.grow(20).has_point(art.position):discard(art)
	var player: CharacterBody2D=world.get_node("Structures/Player")
	player.set_physics_process(false)
	var camera: Camera2D=player.get_node("Camera")
	camera.limit_left=-650;camera.limit_top=-2450;camera.limit_right=12600;camera.limit_bottom=5900
	var ocean := Polygon2D.new();ocean.name="RegionalSea";ocean.z_index=-60
	ocean.polygon=PackedVector2Array([Vector2(-1000,-2700),Vector2(13000,-2700),Vector2(13000,6200),Vector2(-1000,6200)])
	var ocean_material := ShaderMaterial.new();ocean_material.shader=load("res://assets/infrastructure/sea.gdshader")
	ocean_material.set_shader_parameter("grime",load("res://assets/infrastructure/channel.png"));ocean.material=ocean_material;world.add_child(ocean)
	var floor := TileMapLayer.new();floor.name="ContinuousGround";floor.z_index=-20
	floor.tile_set=world.get_node("Ground/TerraceFloor").tile_set
	floor.material=world.get_node("Ground/TerraceFloor").material
	world.add_child(floor)
	var routes := Node2D.new();routes.name="ContinuousRoutes";routes.z_index=-14;world.add_child(routes)
	await physics_frame
	await physics_frame
	grid.region=Rect2i(-28,-105,565,367);grid.cell_size=Vector2(24,24);grid.offset=Vector2(12,12)
	grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER;grid.update()
	# Rasterize actual static colliders with clearance for the player; no water/void is treated as a finished route.
	for collider in world.find_children("*","CollisionShape2D",true,false):
		if not collider.get_parent() is StaticBody2D or collider.disabled:continue
		if not collider.shape is RectangleShape2D:continue
		var size: Vector2=collider.shape.size*.5+Vector2(12,12)
		var center: Vector2=collider.global_position
		var radius: float=size.length()
		var first := Vector2i((center-Vector2.ONE*radius)/24)-Vector2i.ONE
		var last := Vector2i((center+Vector2.ONE*radius)/24)+Vector2i.ONE
		for y in range(first.y,last.y+1):
			for x in range(first.x,last.x+1):
				var cell := Vector2i(x,y)
				if not grid.is_in_boundsv(cell):continue
				var local: Vector2=collider.to_local(grid.get_point_position(cell))
				if absf(local.x)<size.x and absf(local.y)<size.y:grid.set_point_solid(cell)
	# Include polygonal coast/channel collisions and transformed shapes, not only rectangular buildings.
	var query := PhysicsShapeQueryParameters2D.new()
	var clearance := CircleShape2D.new();clearance.radius=14
	query.shape=clearance;query.collision_mask=1
	var space := world.get_world_2d().direct_space_state
	for y in range(grid.region.position.y,grid.region.end.y):
		for x in range(grid.region.position.x,grid.region.end.x):
			var cell := Vector2i(x,y)
			if grid.is_point_solid(cell):continue
			query.transform=Transform2D(0,grid.get_point_position(cell))
			if not space.intersect_shape(query,1).is_empty():grid.set_point_solid(cell)
	var built := {}
	for id in data:
		for dest in data[id].links:
			var shared: String=data[id].continuity[dest].shared_id
			if built.has(shared):continue
			var a: Vector2=positions[id]+Vector2(data[id].links[dest][0],data[id].links[dest][1])
			var b: Vector2=positions[dest]+Vector2(data[dest].links[id][0],data[dest].links[id][1])
			var start := free_cell(Vector2i(a/24));var end := free_cell(Vector2i(b/24))
			var path := grid.get_point_path(start,end)
			if path.is_empty():push_error("No physical route "+shared);quit(1);return
			var route := Node2D.new();route.name=shared;route.set_meta("path",path);route.set_meta("family",data[id].continuity[dest].family);routes.add_child(route)
			for i in range(path.size()):
				var point: Vector2=path[i]
				var cell := floor.local_to_map(point)
				for y in range(-2,3):
					for x in range(-2,3):
						var tile := cell+Vector2i(x,y)
						floor.set_cell(tile,0,Vector2i(posmod(tile.x,16),posmod(tile.y,16)))
				if i%5!=0:continue
				var angle: float=(path[mini(i+1,path.size()-1)]-point).angle()
				sprite("terrain/market_dirt.png",point,Vector2(100,70),route,angle)
				if i%15==0:
					sprite("terrain/metal_repair.png",point+Vector2(0,60),Vector2(70,45),route,angle+.1)
				if data[id].continuity[dest].family in ["cable","coast","vertical"]:
					sprite("infrastructure/walkway.png",point,Vector2(175,120),route,angle)
				elif data[id].continuity[dest].family=="pipe":
					sprite("generated/props/pipe.png",point+Vector2(-sin(angle),cos(angle))*85,Vector2(168,28),route,angle)
			built[shared]=true
			print("CONNECTED ",shared," cells=",path.size())
	world.set_script(load("res://scripts/world/continuous_world.gd"))
	for label in world.find_children("*","Label",true,false):
		label.text=label.text.replace("E passagem","Caminhos contínuos")
	player.set_physics_process(true)
	own(world)
	var packed := PackedScene.new()
	var error := packed.pack(world)
	if error==OK:error=ResourceSaver.save(packed,"res://maps/sucateia/sucateia.tscn")
	print("EXTENDED existing Sucateia: ",built.size()," crossings; save=",error)
	quit(error)
func free_cell(at: Vector2i) -> Vector2i:
	for radius in range(0,8):
		for y in range(-radius,radius+1):
			for x in range(-radius,radius+1):
				var cell := at+Vector2i(x,y)
				if grid.is_in_boundsv(cell) and not grid.is_point_solid(cell):return cell
	return at
