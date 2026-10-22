extends RefCounted
var b
func openings(builder) -> Array[Vector2]:
	var result: Array[Vector2] = []
	for edge in builder.config.get("continuity",{}).values():
		if edge.opening: result.append(Vector2(edge.anchor[0],edge.anchor[1]))
	return result
func wall(builder, a: Vector2, end: Vector2) -> void:
	var exits := openings(builder)
	var delta := end-a
	var count := maxi(1,ceili(delta.length()/18))
	var start := -1
	for i in range(count+1):
		var gap := i==count
		if not gap:
			var at := a.lerp(end,(i+.5)/count)
			for exit_at in exits:
				if at.distance_to(exit_at)<121: gap=true;break
		if not gap and start==-1: start=i
		if gap and start!=-1:
			var from := a.lerp(end,float(start)/count)
			var to := a.lerp(end,float(i)/count)
			builder.solid((from+to)*.5,Vector2(from.distance_to(to)+7,27),builder.world,delta.angle())
			start=-1
func near_opening(builder, at: Vector2) -> bool:
	for exit_at in openings(builder):
		if at.distance_to(exit_at)<165: return true
	return false
func install(builder) -> void:
	b=builder
	var root := Node2D.new()
	root.name="RegionalContinuity"
	root.z_index=-14
	b.add(root,b.world)
	var floor_layer: TileMapLayer = b.world.get_node_or_null("DistrictFloor")
	var outline := PackedVector2Array()
	for point in b.config.get("outline",[]): outline.append(Vector2(point[0],point[1]))
	if b.id != "centre" and b.config.style not in ["harbor","suspended","coastal_path","wreck_bank","gallery","salvage","ruins","freight_path"]:
		for child in b.world.get_children():
			if child is Polygon2D and child.z_index==-40:
				var mat := ShaderMaterial.new()
				mat.shader=load("res://assets/region/outskirts.gdshader")
				mat.set_shader_parameter("soil",load("res://assets/terrain/floor_atlas.png"))
				child.material=mat
	var space: PhysicsDirectSpaceState2D = b.world.get_world_2d().direct_space_state
	var query := PhysicsShapeQueryParameters2D.new()
	var shape := CircleShape2D.new()
	shape.radius=12
	query.shape=shape
	query.collision_mask=1
	var grid := AStarGrid2D.new()
	grid.region=Rect2i(0,0,110,85)
	grid.cell_size=Vector2(24,24)
	grid.offset=Vector2(12,12)
	grid.diagonal_mode=AStarGrid2D.DIAGONAL_MODE_NEVER
	grid.update()
	for y in range(85):
		for x in range(110):
			var point := Vector2(x*24+12,y*24+12)
			query.transform=Transform2D(0,point)
			var allowed: bool = b.id=="centre" or Geometry2D.is_point_in_polygon(point,outline)
			grid.set_point_solid(Vector2i(x,y),not allowed or not space.intersect_shape(query,1).is_empty())
	for dest in b.config.get("continuity",{}):
		var edge: Dictionary = b.config.continuity[dest]
		var anchor := Vector2(edge.anchor[0],edge.anchor[1])
		var direction := Vector2(edge.direction[0],edge.direction[1])
		var gate := Vector2(b.config.links[dest][0],b.config.links[dest][1])
		var join := Vector2(edge.join[0],edge.join[1])
		if edge.opening:
			var portal: Area2D = b.world.get_node("RegionPortals/To_"+dest)
			for distance in [58,44,28,0]:
				var offset: Vector2 = -direction*distance
				query.transform=Transform2D(0,gate+offset)
				if space.intersect_shape(query,1).is_empty():
					portal.set_meta("arrival_offset",offset)
					break
		if edge.opening:
			# Corridor extends the walkable footprint, with physical side rails.
			var first := anchor-direction*110
			var last := anchor+direction*156
			for y in range(0,34):
				for x in range(0,45):
					var at := Vector2(x*48+24,y*48+24)
					if Geometry2D.get_closest_point_to_segment(at,first,last).distance_to(at)<93:
						floor_layer.set_cell(Vector2i(x,y),0,Vector2i(x%16,y%16))
			for side in [-1,1]:
				var normal: Vector2 = Vector2(-direction.y,direction.x)*side
				var at: Vector2 = anchor+direction*75+normal*107
				b.solid(at,Vector2(174,22),b.world,direction.angle())
				b.art("infrastructure/retaining_edge.png",at,Vector2(173,46),root,direction.angle())
			b.solid(anchor+direction*158,Vector2(24,228),b.world,direction.angle())
		var start := Vector2i(join/24)
		var finish := Vector2i(gate/24)
		# Gate cells remain on the original footprint; A* uses actual building/drain collisions.
		var path := grid.get_point_path(start,finish)
		root.set_meta("route_cells_"+dest,path.size())
		var route := PackedVector2Array()
		for i in range(path.size()):
			if i==0 or i%4==0 or i==path.size()-1: route.append(path[i])
		# Do not simplify turns through obstacles: wear follows the sampled cells.
		for i in range(0,path.size(),3):
			var at: Vector2 = path[i]
			var shadow: Sprite2D = b.art("terrain/market_dirt.png",at,Vector2(90,60),root)
			shadow.modulate=Color(.83,.85,.70,.23)
		features(gate,anchor+direction*110,direction,edge.family,root)
		if b.id=="centre": features(gate-direction*80,gate,direction,edge.family,root)
		if edge.family!="vertical":
			var heading := Vector2(edge.heading[0],edge.heading[1])
			var vista_at := anchor+heading*330
			var size := Vector2(640,180) if edge.view_asset=="generated/structures/skyline.png" else Vector2(320,330)
			var vista: Sprite2D = b.art(edge.view_asset,vista_at,size,root)
			vista.z_as_relative=false
			vista.z_index=-35
			vista.modulate=Color(.43,.52,.50,.59)
		root.set_meta("border_"+dest,edge.shared_id)
func features(first: Vector2, last: Vector2, direction: Vector2, family: String, parent: Node) -> void:
	if family=="vertical":
		b.art("terrain/oil_hatch.png",first,Vector2(94,80),parent)
		return
	var delta := last-first
	var count := maxi(1,ceili(delta.length()/100))
	for i in range(count):
		var at := first.lerp(last,(i+.5)/count)
		if family in ["pipe","haul"]:
			var pipe: Sprite2D = b.art("generated/props/pipe.png",at+Vector2(-direction.y,direction.x)*54,Vector2(delta.length()/count+8,24),parent,delta.angle())
			pipe.modulate=Color(.86,.83,.71)
		if family in ["coast","cable","haul"]:
			b.art("infrastructure/walkway.png",at,Vector2(delta.length()/count+8,116),parent,delta.angle())
	if family in ["street","cable","coast"]:
		b.cable(PackedVector2Array([first+Vector2(0,-36),last+Vector2(0,-36)]),parent)
